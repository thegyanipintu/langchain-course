from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
import os
from dotenv import load_dotenv
import pprint

load_dotenv(".env", override=True)


@tool
def search(query: str) -> str:
    """
    Tool that searches for a string/query over Internet.
    Args:
        query: The query to search for
    Returns:
        The search results in string format
    """
    print(f"Searching for '{query}'...", query)
    tav = TavilyClient()
    return tav.search(query=query)


llm = ChatOpenAI(
    model="gemma-4-e4b-it-qat",
    base_url=os.getenv("LMS_BASE_URL"),
    api_key=os.getenv("LMS_TOKEN"),
    default_headers={"authorization": "Bearer " + os.getenv("LMS_TOKEN")},
)

tools = [search]

agent = create_agent(model=llm, tools=tools)

result = agent.invoke(
    {"messages": [HumanMessage(content="Tell me how is the weather of Tokyo")]}
)
pprint.pprint(result)
