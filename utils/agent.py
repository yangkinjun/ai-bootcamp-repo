from dotenv import load_dotenv
from langchain.tools import tool
from openai import OpenAI
from smolagents import tool, CodeAgent, OpenAIServerModel
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

from utils.vector_store import get_retriever


def create_agent():
    # the API key will be loaded from .env and available in os.environ
    load_dotenv()

    # create the model for agent to use
    agent_model = OpenAIServerModel(model_id="gpt-4.1-mini")

    # create an agent with tools
    tools = [get_mom_regulation]
    agent = CodeAgent(tools, model=agent_model, add_base_tools=False, max_steps=5)

    return agent


@tool
def get_mom_regulation(query: str) -> dict:
    """
    Search MOM docs for matching regulations.

    Args:
        query (str): The user's search query.

    Returns:
        dict: The matching regulations.
    """

    # the API key will be loaded from .env and available in os.environ
    load_dotenv()

    # llm to be used in RAG pipeplines
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, seed=42, streaming=True)

    # retrieve documents from the vector store
    # and use the LLM to answer questions based on the retrieved documents
    rag_chain = RetrievalQA.from_llm(retriever=get_retriever(), llm=llm)

    response = rag_chain.invoke(query)

    print(response)
    return response["result"]


def run_agent(query):

    # create the agent
    agent = create_agent()

    prompt = f"""

    You are a helpful assistant that use the tools available to find the relevant information to the query.

    Query: {query}

    Find the answers to the query using the tools available. 
    Your response should be professional and concise.
    Do not use the Intenet. If you cannot find the answer, respond with "Please refer to the MOM website for more information."
    If the query is not related to MOM regulations, respond with "This query is not related to MOM regulations."
    """

    return agent.run(prompt)
