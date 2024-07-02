# utils/constants.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_HOST = os.getenv("OPENAI_API_HOST")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

VECTOR_STORE_DB_PATH : str = os.getenv("VECTOR_STORE_DB_PATH") # type: ignore