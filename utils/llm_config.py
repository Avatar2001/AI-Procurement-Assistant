import os
from crewai import LLM

def get_basic_llm():
    return LLM(
        model="gemini/gemini-2.0-flash",
        temperature=0,
        api_key=os.getenv("GOOGLE_API_KEY")
    )