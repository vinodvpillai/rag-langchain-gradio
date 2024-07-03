# loaders/text_splitter.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    return text_splitter.split_documents(documents)
