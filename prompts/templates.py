# prompts/templates.py
from langchain_core.prompts import ChatPromptTemplate

def get_prompt_template():
    template = """
    You are an assistant for question-answering tasks.
    Use the provided context only to answer the following question:

    <context>
    {context}
    </context>

    Question: {input}
    """
    return ChatPromptTemplate.from_template(template)
