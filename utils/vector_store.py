import os

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import Chroma


CHROMA_PATH = "../data/chroma_store"


def get_embedding_model_name():
    return "text-embedding-3-small"


def load_and_index_documents():
    docs_dir = "data/"
    list_of_documents_loaded = []

    # load documents from the data directory
    for filename in os.listdir(docs_dir):
        try:
            # try to load the document based on its file type
            path = os.path.join(docs_dir, filename)
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(path)
            elif filename.endswith(".txt"):
                loader = TextLoader(path)
            else:
                continue
            # loads the document and adds it to the list of loaded documents
            print(f"Loading {filename}...")
            list_of_documents_loaded.extend(loader.load())

        except Exception as e:
            # if there is error loading the document, print error and continue to the next document
            print(f"Error loading {filename}: {e}")
            continue

    print("Total documents loaded:", len(list_of_documents_loaded))

    # split documents into smaller overlapping chunks
    chunk_size = 300
    chunk_overlap = 30
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(list_of_documents_loaded)

    # the API key will be loaded from .env and available in os.environ
    load_dotenv()

    # embedding model
    embeddings_model = OpenAIEmbeddings(model=get_embedding_model_name())

    # create the chroma vector store from the chunks
    vector_store = Chroma.from_documents(
        collection_name="mom_collection",
        documents=chunks,
        embedding=embeddings_model,
        persist_directory=CHROMA_PATH,
    )


def get_retriever():
    # embedding model
    embeddings_model = OpenAIEmbeddings(model=get_embedding_model_name())

    # load vector_store from the persisted directory
    vector_store = Chroma(
        "mom_collection",
        embedding_function=embeddings_model,
        persist_directory=CHROMA_PATH,
    )
    return vector_store.as_retriever()
