import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
#from sentence_transformers import SentenceTransformer
#from langchain_community.embeddings import SentenceTransformerEmbeddings

CHROMA_PATH = "../data/chroma_store"

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

    # Split documents into smaller overlapping chunks
    chunk_size = 300
    chunk_overlap = 30
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(list_of_documents_loaded)

    #print(type(chunks[0]))

    # Print the number of documents after splitting
    #print(f"Number of documents after splitting: {len(chunks)}")
    
    # The API key will be loaded from .env and available in os.environ
    load_dotenv()
   
    # Embedding model
    embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')
    
    # embed_model_name = "BAAI/bge-small-en-v1.5"
    #embed_model_name =  "all-MiniLM-L6-v2"
    #embed_func = HuggingFaceEmbeddings(model_name=embed_model_name)

    # Use a verified working model
    #model_name = "all-MiniLM-L6-v2"
    #sbert = SentenceTransformer(model_name)

    # Wrap with LangChain-compatible class
    #embed_func = SentenceTransformerEmbeddings(model=sbert)

    # llm to be used in RAG pipeplines
    #llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, seed=42)

    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings_model, collection_name="mom_collection", persist_directory=CHROMA_PATH)
    #vectordb.persist()

def get_retriever():
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings()).as_retriever()
