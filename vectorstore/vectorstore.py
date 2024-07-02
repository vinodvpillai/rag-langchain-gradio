# vectorstore/vectorstore.py
from langchain.vectorstores import FAISS
from embeddings.embeddings import get_embeddings
from utils.constants import VECTOR_STORE_DB_PATH

def create_vectorstore(documents, embeddings):
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(VECTOR_STORE_DB_PATH)
    return vectorstore

def load_vectorstore():
    embeddings = get_embeddings()  # Ensure the embeddings are loaded
    return FAISS.load_local(VECTOR_STORE_DB_PATH, embeddings, allow_dangerous_deserialization=True)
