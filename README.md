
## Demo
1. **Demo Video**: https://www.loom.com/share/8c05f9f4f0cc4a7eacfcb223f9becf85?t=414&sid=ad861779-396f-49a8-a39a-c7cac0ea1521

# Text Summarizer

This is a Streamlit application that allows you to summarize text or documents using the Hugging Face Transformers library. You can choose from different summarization models to generate concise summaries of text inputs or PDF documents.

## Features

- Summarize Text: Input your text and select a summarization model to generate a summary.
- Summarize Document: Upload a PDF document, and the application will extract the text and generate a summary.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/anupamking01/Text-summarizer.git
cd Text-summarizer
```
2.
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Run the Streamlit application:
```bash
streamlit run app.py
```
## Steps

1. Select your choice (Summarize Text or Summarize Document) from the sidebar.
2. Choose a model from the available options.
3. Input your text or upload a PDF document.
4. Select max-Text length
5. Click the "Summarize" button to generate the summary.


## Models
### The following summarization models are available:

- BART (facebook/bart-large-cnn)
- T5 (t5-large)
- Falcon ai
- BART (philschmid/bart-large-cnn-samsum)
- Multilingual Model (csebuetnlp/mT5_multilingual_XLSum)
Feel free to explore and select the model that best suits yourneeds.

## License
This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.


```bibtex
@misc{pdfsumm2024,
  author = {Anupam Poddar},
  title = {PDF-Summarizer},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/anupamking01/Text-summarizer}}
}
