# loaders/document_loader.py
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
import os

def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        loader = PyPDFLoader(file_path)
    elif ext in ['.docx', '.doc']:
        loader = Docx2txtLoader(file_path)
    elif ext == '.txt':
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type")
    return loader.load()
