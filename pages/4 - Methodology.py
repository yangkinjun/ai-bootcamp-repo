import streamlit as st

st.set_page_config(layout="wide", page_title="My Streamlit App - Methodology")
st.title("Methodology")

st.markdown(
    """
## Data Flows & Implementation Details
This application uses a Retrieval-Augmented Generation (RAG) pipeline and agentic AI to answer user queries about employment regulations and workplace issues. The main data flow involves:
- Document ingestion and indexing (PDFs, guidelines, MOM docs)
- Embedding documents using language models
- Storing embeddings in a vector database (ChromaDB)
- Retrieving relevant documents based on user queries
- Generating responses using a Large Language Model (LLM)

### Agentic AI Approach
In addition to RAG, the application leverages agentic AI—intelligent agents that can reason, plan, and orchestrate the use of multiple tools to solve complex queries. Agents:
- Interpret user intent and select the best tool (e.g., search, translation, rights summarization)
- Perform multi-step reasoning, such as searching for regulations, translating queries, and summarizing legal rights
- Enable extensibility for future tools and workflows

### Build Chroma Vector Store  (developer-mode)
This application has a developer-mode to build the ChromaDB vector store, which is protected by a password. This allows developers to update the vector store periodically to include new documents of changes in regulations.
The ChromaDB vector store is built using the following steps (one-time before start of using the application):
1. Load documents from official MOM websites and guidelines.
2. Use a language model to embed the text content of these documents into vector representations.
3. Store these embeddings in ChromaDB for fast retrieval during user queries.
4. The Chroma vector store is shared by Use Cases 1 and 2.
"""
)
st.image(
    "image/vector_store.png",
    caption="Build Chroma vector store",
    use_container_width=False,
)

st.markdown(
    """
### Implementation Highlights
- Uses LangChain and OpenAI for LLM and embeddings
- Agentic AI for tool orchestration and multi-step reasoning
- ChromaDB for fast vector search
- Streamlit for interactive UI
- Multilingual support via translation tools

---
## Use Case 1: 💬 Employment Regulations Chatbot
Below is a flowchart describing the process:


## Use Case 2: 🤝 Workplace Ally
Below is a flowchart describing the process:

---
This capstone project is developed for AI Champions Bootcamp 2025.
"""
)
