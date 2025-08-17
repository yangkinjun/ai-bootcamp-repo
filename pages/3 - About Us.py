import streamlit as st

st.set_page_config(layout="wide", page_title="My Streamlit App - About Us")
st.title("About Us")


st.markdown(
    """
## Project Scope
This project aims to build an AI-powered chatbot for employment regulations and an assistant for workplace support in Singapore. The solution leverages advanced language models and retrieval-augmented generation to provide accurate, context-aware answers to users.

## Objectives
Employment Regulations Chatbot
- Help users (HR practitioners) understand employment regulations and workplace rights in Singapore.
- Enable HR practitioners to quickly access MOM guidelines and legal information.

Workplace Ally
- Empower workers to express grievances / concerns and explore resolution pathways.
- Provide multilingual support for workers from diverse backgrounds.

## Data Sources
Documents from official MOM websites:
- Singapore Employment Act 1968 (PDF) (https://sso.agc.gov.sg/Act/EmA1968)
- List of tripartite guidelines and advisories that supplement MOM laws (https://www.mom.gov.sg/employment-practices/tripartism-in-singapore/tripartite-guidelines-and-advisories)


## Features
- Employment Regulations Chatbot: Ask questions about Singapore employment law and get instant answers.
- Workplace Ally: Multilingual grievance assistant for workers, with translation and empathetic support.
- RAG Pipeline: Combines LLMs with document retrieval for accurate, up-to-date responses.
- Secure API Key management and environment setup.
- Modern, user-friendly Streamlit interface.

---
This capstone project is developed for AI Champions Bootcamp 2025.
"""
)
