import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.vectorstores import Chroma
from utils.vector_store import load_and_index_documents, get_retriever

# if __name__ == "__main__":
#     print("Building Chroma vector store from MOM documents...")
#     load_and_index_documents()
#     print("✅ Building done.")

# The API key will be loaded from .env and available in os.environ
load_dotenv()

    # Create the RAG pipeline
from langchain.chains import RetrievalQA

# llm to be used in RAG pipeplines in this notebook
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, seed=42)

# The `llm` is defined earlier in the notebook (using GPT-4o-mini)
rag_chain = RetrievalQA.from_llm(
    retriever=get_retriever(), llm=llm
)

llm_response = rag_chain.invoke('can a persom be dismissed without notice?')
print(llm_response['result'])
