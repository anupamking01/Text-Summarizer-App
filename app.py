import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")

def text_summary(text, max_length=100, model="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model)
    result = summarizer(text, max_length=max_length, min_length=100, do_sample=False)
    return result

def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document"])

models = {
    "BART (facebook/bart-large-cnn)": "facebook/bart-large-cnn",
    "T5 (t5-large)": "t5-large",
    "Falcon ai" : "Falconsai/text_summarization",
    "BART(philschmid/bart-large-cnn-samsum)" : "philschmid/bart-large-cnn-samsum",
    "multilingual_model" : "csebuetnlp/mT5_multilingual_XLSum"
}

selected_model = st.sidebar.selectbox("Select model", list(models.keys()))

if choice == "Summarize Text":
    st.subheader("Summarize Text using transformers library")
    input_text = st.text_area("Enter your text here")
    max_length = st.number_input("Max Length", min_value=50, max_value=1000, value=100, step=50)
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text, max_length=max_length, model=models[selected_model])
                st.success(result[0]['summary_text'])

elif choice == "Summarize Document":
    st.subheader("Text Summarizer")
    input_file = st.file_uploader("Upload your document here", type=['pdf'])
    if input_file is not None:
        if st.button("Summarize Document"):
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1,1])
            with col1:
                st.info("File uploaded successfully")
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("**Extracted Text is Below:**")
                st.info(extracted_text)
            with col2:
                st.markdown("**Summary Result**")
                doc_summary = text_summary(extracted_text, model=models[selected_model])
                st.success(doc_summary[0]['summary_text'])
