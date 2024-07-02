# chains/retrieval_chain.py
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from vectorstore.vectorstore import load_vectorstore
from llm.model import load_llm
from prompts.templates import get_prompt_template

def create_my_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()
    llm = load_llm()
    prompt = get_prompt_template()
    doc_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, doc_chain)
