# Chatbot - ML

### Welcome to the Chatbot - ML Repository!

This repository contains a machine learning project designed to process PDF documents, extract text, split it into smaller chunks, generate embeddings using Google’s Generative AI, and store them in a FAISS vector store for fast retrieval. The system enables question answering based on the contents of the document.

### Features
- **PDF Parsing**: Extract text from PDF files using PyMuPDF (fitz).
- **Text Splitting**: Split large text documents into smaller, manageable chunks using `RecursiveCharacterTextSplitter` from Langchain.
- **Embeddings**: Generate text embeddings using Google’s Generative AI, enabling semantic search.
- **Vector Store**: Store embeddings in a FAISS vector store for efficient similarity-based retrieval.
- **Question Answering**: Answer user queries based on the document's content using Langchain’s question-answering chain.

### Progress So Far
- **Core Functionality Implemented**:
  - PDF text extraction is fully functional using PyMuPDF.
  - Text splitting using Langchain's `RecursiveCharacterTextSplitter` works seamlessly.
  - Embedding generation is integrated with Google’s Generative AI API and is fully operational.
  - Vector storage and retrieval using FAISS are implemented and tested.
  - Basic question-answering functionality using Langchain’s chain is working.

- **Optimizations**:
  - Intel’s Scikit-learn extension is integrated for enhanced performance.
  - Environment setup instructions are provided for easy replication.


### Code Functionality
The project’s main functionalities include:

1. **Extracting Text from PDFs**:
   - Load a PDF file and extract text content using PyMuPDF.
   - Example:
     ```python
     import fitz
     pdf = fitz.open("document.pdf")
     text = "\n".join(page.get_text() for page in pdf)
     ```

2. **Splitting Text**:
   - Split extracted text into smaller chunks for better embedding generation.
   - Example:
     ```python
     from langchain.text_splitter import RecursiveCharacterTextSplitter
     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
     chunks = text_splitter.split_text(text)
     ```

3. **Generating Embeddings**:
   - Convert text chunks into embeddings using Google’s Generative AI.
   - Example:
     ```python
     from langchain_google_genai import GoogleGenerativeAIEmbeddings
     embeddings = GoogleGenerativeAIEmbeddings(api_key="YOUR_API_KEY")
     vector_store = FAISS.from_texts(chunks, embeddings)
     ```

4. **Storing Embeddings**:
   - Store the generated embeddings in a FAISS vector database for efficient retrieval.

5. **Question Answering**:
   - Use the stored embeddings to answer user queries based on the document content.
   - Example:
     ```python
     from langchain.chains import load_qa_chain
     qa_chain = load_qa_chain(ChatGoogleGenerativeAI(), chain_type="map_reduce")
     result = qa_chain.run(input_document=document, question="Your question here")
     ```

### Installation

To set up the project, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/Tech-Society-SEC/Chatbot_ML.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Chatbot_ML
   ```

3. Install the necessary libraries:
   ```bash
   pip install scikit-learn-intelex pymupdf langchain-google-genai langchain-community python-dotenv faiss-cpu
   ```

4. Mount Google Drive to access your files:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

5. Set up the Google API key by creating a `.env` file and storing your API key:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   api_key = os.getenv('GOOGLE_API_KEY')
   ```

6. Optimize scikit-learn for better performance:
   ```python
   from sklearnex import patch_sklearn
   patch_sklearn()
   ```

### Beginner-Friendly Issues
We welcome contributions! Below are some beginner-friendly issues to help you get started:

1. **Improve Documentation**:
   - Add more detailed comments in the code to explain the purpose of each section.
   - Expand the README with examples of common errors and troubleshooting tips.
   
2. **Add Unit Tests**:
   - Write unit tests for each functionality (e.g., text splitting, embedding generation).

3. **Enhance Error Handling**:
   - Identify potential points of failure (e.g., invalid PDF, missing API key).
   - Add meaningful error messages and fallback mechanisms.

4. **Create a Simple CLI**:
   - Develop a command-line interface for running the system end-to-end.
   - Include options for loading a PDF, asking a question, and displaying results.

5. **Optimize Chunk Size**:
   - Experiment with different chunk sizes for text splitting.
   - Evaluate how it impacts embedding quality and performance.


### Repository URL

For more details and to access the code, visit the GitHub Repository: [https://github.com/Tech-Society-SEC/Chatbot_ML](https://github.com/Tech-Society-SEC/Chatbot_ML)
