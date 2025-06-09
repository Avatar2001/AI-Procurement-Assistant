from crewai.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_engine_tool(query: str):
    """Search the web for the given query."""
    return client.search(query)