# loaders/text_splitter.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter()
    return text_splitter.split_documents(documents)
