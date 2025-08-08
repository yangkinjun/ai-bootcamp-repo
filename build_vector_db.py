import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from utils.vector_store import load_and_index_documents, get_retriever

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

# # llm to be used in RAG pipeplines
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, seed=42)

# # retrieve documents from the vector store
# # and use the LLM to answer questions based on the retrieved documents
# rag_chain = RetrievalQA.from_llm(retriever=get_retriever(), llm=llm)

# llm_response = rag_chain.invoke("who has the right to terminate employment contract?")
# print(llm_response["result"])


# response = rag_chain.stream("who has the right to terminate employment contract?")
# print(f"Response type: {type(response)}")
# print(response)
# for chunk in response:
#     if "answer" in chunk:
#         print(chunk["answer"])
