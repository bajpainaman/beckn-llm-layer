import os
from config import *

def set_environment():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    os.environ["COHERE_API_KEY"] = COHERE_API_KEY
    os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
    os.environ["LANGCHAIN_TRACING_V2"] = LANGCHAIN_TRACING_V2
    os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_ENDPOINT
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
