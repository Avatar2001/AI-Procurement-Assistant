from crewai import Agent

def get_search_query_agent(llm):
    return Agent(
        role="Search Queries Recommendation Agent",
        goal="Generate specific and varied search queries for ecommerce",
        backstory="Supports company procurement by listing strategic product queries",
        llm=llm,
        verbose=True
    )