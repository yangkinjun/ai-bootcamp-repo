__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import streamlit as st

from openai import OpenAI
from smolagents import tool, CodeAgent, OpenAIServerModel
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA


from utils.vector_store import get_retriever


def create_agent():
    # loads the API key
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    # create the model for agent to use
    agent_model = OpenAIServerModel(
        model_id="gpt-4o-mini", api_key=OPENAPI_API_KEY, temperature=0.5
    )

    # create an agent with tools
    tools = [search_mom_regulation]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)
    print("Agent created with tools:", tools)
    return agent


def create_agent_ally():
    # loads the API key
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    # create the model for agent to use
    agent_model = OpenAIServerModel(
        model_id="gpt-4o-mini", api_key=OPENAPI_API_KEY, temperature=0.5
    )

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

    Example:
      result = search_mom_regulation('What is the retirement age in Singapore in 2022?')
    """

    print("in search_mom_regulation()")

    # loads the API key
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    # llm to be used
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        seed=42,
        streaming=True,
        api_key=OPENAPI_API_KEY,
    )

    # Create the retriever (your existing get_retriever function)
    retriever = get_retriever()

    # retrieve documents from the vector store
    # and use the LLM to answer questions based on the retrieved documents
    rag_chain = RetrievalQA.from_llm(retriever=get_retriever(), llm=llm)
    response = rag_chain.invoke(query)

    return response["result"]


@tool
def check_rights_tool(issue: str) -> str:
    """
    Summarises the rights a worker in Singapore has regarding this issue.

    Args:
        issue (str): The issue the worker is facing.

    Returns:
        str: The summary of the worker's rights.

    Example:
      result = check_rights_tool('我在短短的一天 被公司解雇了 。这是合理的吗?')
    """

    # loads the API key
    OPENAPI_API_KEY = st.secrets["OPENAI_API_KEY"]

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAPI_API_KEY)
    prompt = f"""
    Summarise the legal rights a worker in Singapore has regarding {issue}
    """
    return llm.invoke(prompt).content


def agent_search(agent, query):

    prompt = f"""

    You are a helpful assistant that uses the provided tools to find the relevant MOM (Ministry of Manpower) regulations for HR practitioners.

    Query: {query}

    Rules:
    1. Respond in a professional and concise manner for HR practitioners.
    2. Do not use the Internet or any external sources other than the tools provided to you.
    3. If the documents do not contain relevant information, or you do not have enough information to answer, reply exactly with: **"Please refer to the MOM website for more information."**
    4. For rule 3, use the text exactly as written - do not add, remove or change any characters.
    """

    return agent.run(prompt)


def agent_ally_search(agent, query):

    prompt = f"""

    You are the Worker Ally Assistant — a multilingual, AI-powered grievance assistant that helps workers understand their rights, express workplace concerns clearly, and explore resolution pathways.

    Query: {query}

    Rules:
    1. Be friendly, empathetic, and supportive.
    2. Do not use the Internet or any external sources other than the tools provided to you.
    3. If the documents do not contain relevant information, or you do not have enough information to answer, reply exactly with: **"Sorry, I am unable to help you in this matter. Please call the MOM helpline at 61234567 for assistance."**
    4. For rule 3, use the text exactly as written - do not add, remove or change any characters.
    """

    return agent.run(prompt)
