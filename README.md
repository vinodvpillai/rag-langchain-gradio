# RAG-Based Question-Answering Chatbot

This project demonstrates a sophisticated question-answering (Q&A) chatbot using Retrieval Augmented Generation (RAG) with LangChain and Gradio. The chatbot uses the OpenAI LLM model to answer questions based on the content of uploaded documents.

## Features

- Allows users to upload files (TXT, PDF, DOCX, XLSX)
- Processes and stores document content in a vector database using FAISS
- Enables users to ask questions based on the uploaded document content
- Provides a feature to clear the existing data from the vector database

## Libraries Used

- **Document Loading:** `PyPDFLoader`, `Docx2txtLoader`, `TextLoader` from `langchain_community.document_loaders`
- **Text Splitting:** `RecursiveCharacterTextSplitter` from `langchain.text_splitter`
- **Embedding:** `HuggingFaceEmbeddings` from `langchain_community.embeddings`
- **Storage:** `FAISS` from `langchain_community.vectorstores`
- **LLM Model:** `ChatOpenAI` from `langchain_openai`
- **Interface:** `Gradio`

## Project Structure
```
.
├── app.py
├── loaders
│ ├── document_loader.py
│ └── text_splitter.py
├── embeddings
│ └── embeddings.py
├── vectorstore
│ └── vectorstore.py
├── llm
│ └── model.py
├── prompts
│ └── templates.py
├── utils
│ └── constants.py
├── chains
│ └── retrieval_chain.py
└── data
```

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project root directory and add your OpenAI API key:**

    ```env
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_API_HOST=https://api.openai.com
    OPENAI_MODEL=gpt-3.5-turbo
    ```

5. **Run the application:**

    ```sh
    python app.py
    ```

6. **Access the application:**
   Open your web browser and go to `http://localhost:7860`.

## Usage

### Upload Document

1. Go to the "Upload Document" tab.
2. Upload your document (PDF, DOCX, TXT).
3. Click the "Upload" button to process and store the document content in the vector database.

### Ask Question

1. Go to the "Ask Question" tab.
2. Enter your question in the textbox.
3. Click the "Ask" button to get an answer based on the uploaded document content.

### Clear Database

1. Click the "Clear Database" button to remove all the stored data from the vector database.

## Contributing

If you want to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
