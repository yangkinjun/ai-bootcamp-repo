import streamlit as st

st.set_page_config(layout="wide", page_title="My Streamlit App - About Us")
st.title("About Us")


st.markdown(
    """
## Project Scope
This project aims to transform how HR practitioners and workers in Singapore access, understand, and act on employment regulations and workplace rights. By integrating AI technologies, the solution provides:

- **Automated, reliable guidance** on employment law and workplace issues, reducing the need for manual research and interpretation.
- **Multilingual, inclusive support** for Singapore’s diverse workforce, ensuring accessibility for non-English speakers.
- **Scalable, updatable knowledge base** that can ingest new MOM documents and guidelines as regulations evolve.
- **Secure, privacy-conscious architecture** for handling sensitive workplace queries and user data.
- **User-centric design** with intuitive interfaces for both HR professionals and workers, supporting both quick lookups and in-depth grievance assistance.

The project is structured around two main use cases:

### Use Case 1: 💬 Employment Regulations Chatbot
- An AI-powered chatbot that answers questions about Singapore employment law, MOM guidelines, and HR best practices. It leverages retrieval-augmented generation (RAG) to provide context-aware, document-backed responses.

### Use Case 2: 🤝 Workplace Ally
- An AI-powered assistant that helps workers articulate grievances, understand their rights, and explore resolution pathways. It supports multilingual input and empathetic, supportive guidance.

The solution is designed for extensibility, allowing future integration with additional data sources, regulatory updates, and new conversational features.


## Objectives
### Use Case 1: 💬 Employment Regulations Chatbot
- Empower HR practitioners to make informed decisions by providing instant, reliable access to employment regulations and MOM guidelines.
- Reduce compliance risks and improve HR policy implementation through accurate, up-to-date legal information.
- Enhance productivity by minimizing time spent searching for regulatory details and best practices.
- Support continuous learning and professional development for HR teams with AI-driven insights and explanations.

### Use Case 2: 🤝 Workplace Ally
- Enable workers to confidently articulate workplace grievances and concerns, regardless of language or background.
- Foster a fair and supportive work environment by helping users understand their rights and available resolution pathways.
- Bridge communication gaps between workers and HR, especially for non-native English speakers, through multilingual support and translation.
- Promote mental well-being and workplace harmony by providing empathetic, AI-powered assistance and guidance.

## Data Sources
Documents from official government website:
- Singapore Employment Act 1968 (PDF) (https://sso.agc.gov.sg/Act/EmA1968)
- List of tripartite guidelines and advisories that supplement MOM laws (https://www.mom.gov.sg/employment-practices/tripartism-in-singapore/tripartite-guidelines-and-advisories)

## Features
- Employment Regulations Chatbot: Ask questions about Singapore employment law and get instant answers.
- Workplace Ally: Multilingual grievance assistant for workers, with translation and empathetic support.
- Developer mode: Load and build Vector Datastore (for adding new documents).
- RAG Pipeline: Combines LLMs with document retrieval for accurate, up-to-date responses.
- Secure API Key management and environment setup.
- Modern, user-friendly Streamlit interface.

---
This capstone project is developed for AI Champions Bootcamp 2025.
"""
)
