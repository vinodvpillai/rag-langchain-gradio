from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from utils import constants
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# load a PDF  
loader = PyPDFLoader("content/document_review.pdf")
documents = loader.load()

# split document content
text_splitter = RecursiveCharacterTextSplitter()
text = text_splitter.split_documents(documents)

# load embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", encode_kwargs = {"normalize_embeddings": True})

# create vectorstore using FAISS
vectorstore = FAISS.from_documents(text, embeddings)

# Save the documents and embeddings
vectorstore.save_local("vectorstore.db")

# Create retriever
retriever = vectorstore.as_retriever()

# Load the llm 
llm = ChatOpenAI(base_url=constants.OPENAI_API_HOST, api_key=constants.OPENAI_API_KEY, model=constants.OPENAI_MODEL) # type: ignore

# Define prompt template
template = """
You are an assistant for question-answering tasks.
Use the provided context only to answer the following question:

<context>
{context}
</context>

Question: {input}
"""

# Create a prompt template
prompt = ChatPromptTemplate.from_template(template)

# Create a chain 
doc_chain = create_stuff_documents_chain(llm, prompt)
chain = create_retrieval_chain(retriever, doc_chain)


# User query 
response = chain.invoke({"input": "Tell me?"})

# Get the Answer only
print(response['answer'])