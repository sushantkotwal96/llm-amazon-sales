# llm-amazon-sales

# Context-Aware Q&A System

This project is a Context-Aware Q&A System designed to provide accurate responses based on user-uploaded data. It leverages the Langchain framework and OpenAI instruct models to enable context-aware responses. The system also includes a custom CSV agent, Python REPL tool, and FAISS vector database for efficient embedding and retrieval operations. Additionally, the project uses Streamlit to create a user-friendly interface for file uploads and interactive Q&A sessions.

## Features

- **Context-Aware Responses**: Provides accurate and context-aware responses based on the uploaded data.
- **Retrieval-Augmented Generation (RAG)**: Utilizes RAG chains for enhanced question answering.
- **Custom CSV Agent**: Handles CSV files using a custom agent.
- **Python REPL Tool**: Executes Python code for dynamic response generation.
- **FAISS Vector Database**: Efficiently retrieves relevant data using embedding and retrieval operations.
- **Streamlit Interface**: Offers a user-friendly interface for uploading files and interactive Q&A sessions.


## Usage
1. Start the Streamlit application:

```
sh
streamlit run app.py
```

2. Upload your CSV file via the Streamlit interface.

3. Ask questions in the Q&A section. The system will use the uploaded data to provide context-aware responses.

# Thank You
