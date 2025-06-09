from crewai import Agent

def get_report_author_agent(llm):
    return Agent(
        role="Procurement Report Author Agent",
        goal="Write a professional procurement report in HTML",
        backstory="Analyzes data and formats it in a Bootstrap-based HTML report",
        llm=llm,
        verbose=True
    )