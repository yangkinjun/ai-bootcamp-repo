import streamlit as st
from dotenv import load_dotenv

# from langchain.tools import tool
from openai import OpenAI
from smolagents import tool, CodeAgent, OpenAIServerModel
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from utils.translate import translate_text
from utils.vector_store import search_mom_docs, get_retriever


def create_agent():
    # the API key will be loaded from .env and available in os.environ
    # load_dotenv()
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    # create the model for agent to use
    agent_model = OpenAIServerModel(model_id="gpt-4o-mini", api_key=OPENAPI_API_KEY)

    # create an agent with tools
    tools = [search_mom_regulation]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)
    print("Agent created with tools:", tools)
    return agent


def create_agent_ally():
    # the API key will be loaded from .env and available in os.environ
    load_dotenv()

    # create the model for agent to use
    agent_model = OpenAIServerModel(model_id="gpt-4o-mini")

    # create an agent with tools
    tools = [search_mom_regulation, check_rights_tool]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)

    return agent


@tool
def search_mom_regulation(query: str) -> str:
    """
    Search documents for matching Singapore MOM regulations.

    Args:
        query (str): The user's search query.
        chat_history (list, optional): List of previous messages for conversational context.

    Returns:
        dict: The matching regulations.
    """

    print("in search_mom_regulation()")
    # the API key will be loaded from .env and available in os.environ
    # oad_dotenv()
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    # llm to be used
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        seed=42,
        streaming=True,
        api_key=OPENAPI_API_KEY,
    )
    print("after llm")

    # create memory for conversation history
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    print("after memory")

    # Create the retriever (your existing get_retriever function)
    retriever = get_retriever()
    print("after get_retriever")

    # # Create the conversational chain
    # conv_chain = ConversationalRetrievalChain.from_llm(
    #     llm=llm, retriever=retriever, memory=memory
    # )
    # retrieve documents from the vector store
    # and use the LLM to answer questions based on the retrieved documents
    rag_chain = RetrievalQA.from_llm(retriever=get_retriever(), llm=llm)
    response = rag_chain.invoke(query)

    # print("after conv_chain")

    # # To use the chain, pass both the query and the chat history:
    # response = conv_chain({"question": query, "chat_history": chat_history})

    # result = response.get("result") or response.get("answer")
    # if not isinstance(result, str):
    #     result = str(result)
    # return result

    return response["result"]


@tool
def check_rights_tool(issue: str) -> str:
    """
    Summarises the rights a worker in Singapore has regarding this issue.

    Args:
        issue (str): The issue the worker is facing.

    Returns:
        str: The summary of the worker's rights.
    """

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"Summarise the legal rights a worker in Singapore has regarding {issue}"
    return llm.invoke(prompt).content


def agent_search(agent, query):

    # create the agent
    # agent = create_agent()

    # if chat_history is None:
    #     chat_history = []

    prompt = f"""

    You are a helpful assistant that uses the provided tools to find the relevant MOM (Ministry of Manpower) regulations for HR practitioners.

    Query: {query}

    Rules:
    1. Respond in a professional and concise manner for HR practitioners.
    2. Do not use the Internet or any external sources other than the provided tools.
    3. If the query is not related to MOM regulations, reply exactly with:
       "This query is not related to MOM regulations."
    4. If the query is related to MOM regulations but you do not have enough information or confidence to answer, reply exactly with:
       "Please refer to the MOM website for more information."
    5. Always follow these rules exactly. Do not change the wording in rules 3 or 4.
    """

    print("Running agent_search with query:", query)
    return agent.run(prompt)


def agent_ally_search(query):

    # create the agent
    agent = create_agent_ally()

    prompt = f"""

    You are the Worker Ally Assistant — a multilingual, AI-powered grievance assistant that helps workers understand their rights, express workplace concerns clearly, and explore resolution pathways.

    Query: {query}

    Rules:
    1. Be friendly, empathetic, and supportive.
    2. Do not use the Internet or any external sources other than the provided tools.
    3. If the query is not related to employment matters, reply exactly with:
       "Sorry, this is not related to employment matters."
    4. If the query is related to employment matters but you do not have enough information or confidence to answer, reply exactly with:
       "Sorry, I am unable to help you in this matter. Please call the MOM helpline at 61234567 for assistance."
    5. Always follow these rules exactly. Do not change the wording in rules 3 or 4.
    """

    return agent.run(prompt)
