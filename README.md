# Chatbot - ML

Welcome to the Chatbot - ML Repository!

This repository contains a machine learning project designed to process PDF documents, extract text, split it into smaller chunks, generate embeddings using Google’s Generative AI, and store them in a FAISS vector store for fast retrieval. The system enables question answering based on the contents of the document.

## Features

- **PDF Parsing:** Extract text from PDF files using PyMuPDF (fitz).
- **Text Splitting:** Split large text documents into smaller, manageable chunks using `RecursiveCharacterTextSplitter` from Langchain.
- **Embeddings:** Generate text embeddings using Google’s Generative AI, enabling semantic search.
- **Vector Store:** Store embeddings in a FAISS vector store for efficient similarity-based retrieval.
- **Question Answering:** Answer user queries based on the document's content using Langchain’s question-answering chain.

## Progress So Far

### Core Functionality Implemented:
- **PDF Text Extraction:**  
  PDF text extraction is fully functional using PyMuPDF.
  
- **Text Splitting:**  
  Text splitting with Langchain's `RecursiveCharacterTextSplitter` operates seamlessly.
  
- **Embedding Generation:**  
  Integration with Google’s Generative AI API for embedding generation is fully operational.
  
- **Vector Storage & Retrieval:**  
  Embeddings are stored in a FAISS vector store, enabling fast similarity-based retrieval.
  
- **Question Answering:**  
  Basic question-answering using Langchain’s QA chain is successfully working.

### Recent Updates & Enhancements:
- **Enhanced Error Handling:**  
  Added error checks for invalid PDF inputs and missing API keys to improve reliability.
  
- **Improved Code Modularity:**  
  Refactored code into modular components to simplify maintenance and future expansion.
  
- **Unit Testing:**  
  Initial unit tests for key functionalities (e.g., PDF extraction and text splitting) have been implemented.
  
- **Performance Optimizations:**  
  Integrated Intel’s Scikit-learn extension to boost performance.
  
- **Documentation and Comments:**  
  Expanded inline comments and documentation have been added to facilitate onboarding and troubleshooting.

## Code Functionality Explained

The project’s main functionalities are structured into several distinct components:

### 1. Extracting Text from PDFs
- **Purpose:**  
  Load a PDF file and extract its text content.
  
- **Implementation:**  
  Utilizes PyMuPDF (fitz) to open a PDF and iterate through each page, concatenating the text.
  
- **Example Code:**
  ```python
  import fitz
  pdf = fitz.open("document.pdf")
  text = "\n".join(page.get_text() for page in pdf)
  ```

### 2. Splitting Text into Chunks
- **Purpose:**  
  Divide large text documents into smaller, more manageable chunks to enhance embedding generation.
  
- **Implementation:**  
  Uses Langchain's `RecursiveCharacterTextSplitter` with configurable chunk size and overlap.
  
- **Example Code:**
  ```python
  from langchain.text_splitter import RecursiveCharacterTextSplitter
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  chunks = text_splitter.split_text(text)
  ```

### 3. Generating Text Embeddings
- **Purpose:**  
  Transform text chunks into numerical embeddings that represent semantic content.
  
- **Implementation:**  
  Integrates with Google’s Generative AI via Langchain's Google Generative AI embeddings module.
  
- **Example Code:**
  ```python
  from langchain_google_genai import GoogleGenerativeAIEmbeddings
  embeddings = GoogleGenerativeAIEmbeddings(api_key="YOUR_API_KEY")
  vector_store = FAISS.from_texts(chunks, embeddings)
  ```

### 4. Storing and Retrieving Embeddings
- **Purpose:**  
  Efficiently store the generated embeddings and retrieve them based on similarity.
  
- **Implementation:**  
  Utilizes FAISS as the vector store, enabling quick similarity-based searches.
  
- **Functionality:**  
  When a user poses a query, the system compares the query’s embedding to those stored, retrieving the most relevant document sections.

### 5. Question Answering
- **Purpose:**  
  Provide answers to user queries by leveraging the stored embeddings and document content.
  
- **Implementation:**  
  Employs Langchain’s question-answering chain (using methods like map-reduce) to generate answers.
  
- **Example Code:**
  ```python
  from langchain.chains import load_qa_chain
  qa_chain = load_qa_chain(ChatGoogleGenerativeAI(), chain_type="map_reduce")
  result = qa_chain.run(input_document=document, question="Your question here")
  ```

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tech-Society-SEC/Chatbot_ML.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Chatbot_ML
   ```

3. **Install the necessary libraries:**
   ```bash
   pip install scikit-learn-intelex pymupdf langchain-google-genai langchain-community python-dotenv faiss-cpu
   ```

4. **Mount Google Drive (if needed):**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

5. **Configure the API Key:**  
   Create a `.env` file and store your Google API key:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   api_key = os.getenv('GOOGLE_API_KEY')
   ```

6. **Optimize scikit-learn:**
   ```python
   from sklearnex import patch_sklearn
   patch_sklearn()
   ```

## Beginner-Friendly Issues

We welcome contributions! Here are some beginner-friendly tasks:

- **Improve Documentation:**  
  Enhance inline comments and expand the README with more examples and troubleshooting tips.

- **Add Unit Tests:**  
  Develop tests for functionalities like text extraction, text splitting, and embedding generation.

- **Enhance Error Handling:**  
  Implement checks and meaningful error messages for cases such as invalid PDFs or absent API keys.

- **Create a Simple CLI:**  
  Build a command-line interface for loading PDFs, submitting queries, and displaying results.

- **Optimize Chunk Size:**  
  Experiment with different text chunk sizes to find the optimal balance for embedding quality and performance.

## Repository URL

For more details and to access the code, visit the [GitHub Repository](https://github.com/Tech-Society-SEC/Chatbot_ML).
