import os

from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

MODEL = "gemini/gemini-3.5-flash-lite"

def get_api_key() -> str | None:
    return os.getenv("GEMINI_API_KEY")

def get_llm() -> LLM:
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY não encontrada. Crie um arquivo .env com a chave."
        )
    return LLM(model=MODEL, api_key=api_key)
