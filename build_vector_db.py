import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from utils.vector_store import load_and_index_documents

if __name__ == "__main__":
    print("Building Chroma vector store from MOM documents...")
    load_and_index_documents()
    print("✅ Building done.")
