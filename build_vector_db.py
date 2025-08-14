import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from utils.vector_store import load_and_index_documents

if __name__ == "__main__":
    print("Building Chroma vector store from MOM documents...")
    load_and_index_documents()
    print("✅ Building done.")

# # the API key will be loaded from .env and available in os.environ
# load_dotenv()

# # Create the RAG pipeline
# from langchain.chains import RetrievalQA

# # improving..TODO later:
# # ⚠️⚠️⚠️ This is the key step
# # We can set the threshold for the retriever, this is the minimum similarity score for the retrieved documents
# # retriever_w_threshold = vectordb.as_retriever(
# #         search_type="similarity_score_threshold",
# #         # There is no universal threshold, it depends on the use case
# #         search_kwargs={"similarity_score_threshold": 0.20}
# # )
