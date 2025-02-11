from transformers import pipeline
import gradio as gr

# Initializing the Hugging Face summarization pipeline.
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """
    Summarize the provided text using the pre-trained summarization model.
    
    Args:
        text (str): The text to summarize.
    
    Returns:
        str: The summarized text.
    """
    if not text.strip():
        return "Error: Provided text is empty."
    try:
        # You may adjust max_length and min_length parameters as needed.
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {str(e)}"

def process_input(input_text, file):
    """
    Processes the user input by either reading the uploaded .txt file or using the provided text.
    
    Args:
        input_text (str): Text provided directly by the user.
        file (file-like object): Uploaded file (should be .txt).
    
    Returns:
        str: The summary or an error message.
    """
    # If a file is uploaded, attempt to read its content.
    if file is not None:
        try:
            # Ensure the file is a .txt file.
            filename = file.name
            if not filename.endswith('.txt'):
                return "Error: Unsupported file format. Please upload a .txt file."
            
            # Read the file content (assuming UTF-8 encoding).
            file_content = file.read().decode("utf-8")
            if not file_content.strip():
                return "Error: Uploaded file is empty."
            text_to_summarize = file_content
        except Exception as e:
            return f"Error reading file: {str(e)}"
    else:
        # Use the direct text input.
        text_to_summarize = input_text
        if not text_to_summarize.strip():
            return "Error: No text provided for summarization."
    
    # Return the summary.
    return summarize_text(text_to_summarize)

# Create the Gradio interface.
iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.inputs.Textbox(lines=10, label="Enter Text for Summarization"),
        gr.inputs.File(label="Or Upload a .txt File")
    ],
    outputs="text",
    title="Text Summarizer",
    description="Upload a .txt file or enter text to generate a concise summary of the content."
)

if __name__ == "__main__":
    iface.launch()
