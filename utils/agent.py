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
    tools = [search_mom_regulation, check_rights_tool, translate_lang_for_processing]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)

    return agent


@tool
def search_mom_regulation(query: str) -> str:
    """
    Search the employment act clause related to the user's query.

    Args:
        query (str): The user's search query.

    Returns:
        str: The relevant clause.
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

    You are a helpful assistant that use the tools available to find the relevant MOM regulations to the query for HR practitioners.

    Query: {query}

    Find the answers to the query using the tools available. 
    Your response should be professional and concise for HR practitioners.
    Do not use the Intenet. If you cannot find the answer, respond with "Please refer to the MOM website for more information."
    If the query is not related to MOM regulations, respond with "This query is not related to MOM regulations."
    """

    return agent.run(prompt)


def agent_ally_search(query):

    # create the agent
    agent = create_agent()

    prompt = f"""

    You are a helpful assistant that use the tools available to help workers address their concerns.

    Query: {query}

    Find the answers to the query using the tools available. 
    Your response should be like a friend, though not overly casual.
    Do not use the Intenet. If you cannot find the answer, respond with "Sorry, I am unable to help you in this matter. Please call the MOM helpline at 61234567 for assistance."
    If the query is not related to MOM or employment matters, respond with "Sorry, this is not related to employment matters."
    """

    return agent.run(prompt)
