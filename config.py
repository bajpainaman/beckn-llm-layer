import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<your-api-key>")
COHERE_API_KEY = os.getenv("COHERE_API_KEY", "<your-api-key>")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "<your-api-key>")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "<your-api-key>")
