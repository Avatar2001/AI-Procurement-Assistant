from crewai import Agent
from tools.search_engine_tool import search_engine_tool

def get_search_engine_agent(llm):
    return Agent(
        role="Search Engine Agent",
        goal="Find ecommerce links for suggested search queries",
        backstory="Uses search engine tool to find real-time product pages",
        llm=llm,
        verbose=True,
        tools=[search_engine_tool]
    )