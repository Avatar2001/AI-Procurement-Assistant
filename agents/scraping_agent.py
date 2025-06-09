from crewai import Agent
from tools.scraping_tool import Web_Scraping_tool

def get_scraping_agent(llm):
    return Agent(
        role="Web Scraping Agent",
        goal="Extract product details from ecommerce pages",
        backstory="Scrapes product pages to collect pricing, specs, and recommendations",
        llm=llm,
        verbose=True,
        tools=[Web_Scraping_tool]
    )