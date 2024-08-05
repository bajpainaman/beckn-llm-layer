
# beckn-llm-layer

This project implements an Adaptive RAG (Retrieval-Augmented Generation) system using LangChain and various other libraries.

## Project Structure

```
adaptive_rag/
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── environment.py
├── index.py
├── llms.py
├── graph.py
├── utils/
│   ├── document_processing.py
│   ├── routing.py
│   ├── grading.py
│   └── search.py
```

## Installation

To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Configuration

Set your API keys in `config.py`. You can either directly set them in the file or export them as environment variables before running the project.

Example configuration in `config.py`:

```python
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<your-api-key>")
COHERE_API_KEY = os.getenv("COHERE_API_KEY", "<your-api-key>")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "<your-api-key>")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "<your-api-key>")
```

## Running the Project

To run the project, use the following command:

```bash
python main.py
```

## Overview of Files

- `main.py`: The entry point of the project. It sets the environment, builds the index, compiles the graph, and runs the workflow.
- `config.py`: Contains configuration settings for API keys and other environment variables.
- `environment.py`: Sets the necessary environment variables for the project.
- `index.py`: Handles the creation of the document index using LangChain.
- `llms.py`: Defines the language models and related configurations.
- `graph.py`: Builds and compiles the state graph for the Adaptive RAG workflow.
- `utils/`: A directory containing helper modules:
  - `document_processing.py`: Functions for document retrieval, generation, grading, and query transformation.
  - `routing.py`: Functions for routing questions and deciding the next steps in the workflow.
  - `grading.py`: Functions for grading the generated answers against the documents and questions.
  - `search.py`: Functions for performing web searches.

## Example Usage

To run an example workflow, ensure your API keys are set, and then execute `main.py`. The project will process the input question through the Adaptive RAG workflow, retrieving relevant documents, generating answers, and grading the output.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

This project utilizes the following libraries:
- LangChain
- Tiktoken
- Langchain-OpenAI
- Langchain-Cohere
- Langchainhub
- ChromaDB
- Langgraph
- Tavily-Python

Special thanks to the developers and contributors of these libraries for their invaluable tools and resources.
