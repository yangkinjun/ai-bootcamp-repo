from dotenv import load_dotenv
from langchain.tools import tool
from openai import OpenAI
from smolagents import tool, CodeAgent, OpenAIServerModel
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

from utils.translate import translate_text
from utils.vector_store import search_mom_docs


def create_agent():
    # the API key will be loaded from .env and available in os.environ
    load_dotenv()

    # create the model for agent to use
    agent_model = OpenAIServerModel(model_id="gpt-4o-mini")

    # create an agent with tools
    tools = [search_mom_regulation]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)

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
    Search MOM docs for matching regulations.

    Args:
        query (str): The user's search query.

    Returns:
        dict: The matching regulations.
    """

    # search the MOM docs for matching regulations
    return search_mom_docs(query)


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


def agent_search(query):

    # create the agent
    agent = create_agent()

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
