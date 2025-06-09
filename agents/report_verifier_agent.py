from crewai import Agent

def get_report_verifier_agent(llm):
    return Agent(
        role="Report Verifier Agent",
        goal="Verify and annotate procurement HTML report",
        backstory="Ensures report has all sections, structure, Bootstrap, and formatting",
        llm=llm,
        verbose=True
    )