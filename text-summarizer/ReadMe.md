# Text Summarizer Feature

## Overview
This project implements a Text Summarizer as an extension to the Chatbot_ML repository. The feature allows users to obtain a concise summary of any provided content. Users have two options for input:

1. **Upload a Text File:** Upload a `.txt` file that contains the text to be summarized.
2. **Direct Text Input:** Paste or type plain text directly into the chat interface.

The system uses a pre-trained NLP model from Hugging Face (e.g., Facebook's BART for summarization) to generate summaries that are both clear and concise while retaining critical information.

## Features
- **File Upload Support:**  
  Users can upload text files (`.txt` format only) for summarization.

- **Direct Text Input:**  
  Users can enter plain text directly into the interface.

- **Accurate Summarization:**  
  Summarization is powered by a Hugging Face Transformers model, ensuring that both short and long texts are handled effectively.

- **Robust Error Handling:**  
  The system checks for invalid inputs such as empty texts, unsupported file formats, or empty files, and displays appropriate error messages.

- **User-Friendly Output:**  
  Summarized output is displayed clearly in the chat interface.

## Technical Details
- **Summarization Model:**  
  The summarizer uses a Hugging Face Transformers pipeline (for example, `facebook/bart-large-cnn`). Parameters like `max_length` and `min_length` are configurable to balance summary detail with conciseness.

- **Interface:**  
  The feature is integrated with a Gradio-based web interface, which allows easy interaction and demonstration of the summarization functionality.

- **File Parsing:**  
  Uploaded files are validated to ensure they are in the `.txt` format and are then read (using UTF-8 encoding) before being processed by the summarizer.

- **Modularity:**  
  The code is structured in a modular fashion (see `text_summarizer.py`), making it easy to maintain and extend.

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Tech-Society-SEC/Chatbot_ML.git
   cd Chatbot_ML
   ```

2. **Install Required Libraries:**
   ```bash
   pip install transformers gradio
   ```
   Ensure you also have any other dependencies installed as needed.

3. **Configure Environment (if required):**  
   Set up any necessary environment variables or API keys. For this feature, none are required unless you decide to extend functionality.

## Running the Text Summarizer
To launch the text summarizer interface, run the following command:
```bash
python text_summarizer.py
```
This will open a Gradio interface in your default browser where you can either paste text or upload a `.txt` file to receive a summarized version of the content.

## Testing the Feature
Unit tests have been implemented using Python’s built-in `unittest` framework. These tests cover:
- Handling of empty text inputs.
- Summarization of valid plain text inputs.
- File upload validations (e.g., unsupported file formats, empty files).
- Summarization from valid `.txt` files.

### Running Tests
To run the tests, execute:
```bash
python test_text_summarizer.py
```
This command will run all the test cases and report any failures, ensuring that the summarizer behaves as expected.


## References
- [Hugging Face Summarization Models](https://huggingface.co/models?pipeline_tag=summarization&sort=trending)
- [Gradio Documentation](https://www.gradio.app/docs)
- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html)
