# llm/model.py
from langchain_openai import ChatOpenAI
from utils.constants import OPENAI_API_HOST, OPENAI_API_KEY, OPENAI_MODEL

def load_llm():
    return ChatOpenAI(base_url=OPENAI_API_HOST, api_key=OPENAI_API_KEY, model=OPENAI_MODEL) # type: ignore
