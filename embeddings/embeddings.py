# embeddings/embeddings.py
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", encode_kwargs={"normalize_embeddings": True})
