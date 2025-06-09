from crewai import Crew, Process
from agents.report_author_agent import get_report_author_agent
from agents.report_verifier_agent import get_report_verifier_agent
from agents.scraping_agent import get_scraping_agent
from agents.search_engine_agent import get_search_engine_agent
from context.company_context import get_company_context
from tasks.report_author_task import get_report_author_task
from tasks.report_verifier_task import get_report_verifier_task
from tasks.scraping_task import get_scraping_task
from tasks.search_engine_task import get_search_engine_task
from utils.llm_config import get_basic_llm
from agents.search_query_agent import get_search_query_agent
from tasks.search_query_task import get_search_query_task
...

output_dir = "./ai-agent-output1"

llm = get_basic_llm()
company_context = get_company_context()

company = Crew(
    agents=[
        get_search_query_agent(llm),
        get_search_engine_agent(llm),
        get_scraping_agent(llm),
        get_report_author_agent(llm),
        get_report_verifier_agent(llm)
    ],
    tasks=[
        get_search_query_task(get_search_query_agent(llm), output_dir),
        get_search_engine_task( get_search_engine_agent(llm),output_dir),
        get_scraping_task(get_scraping_agent(llm),output_dir),
        get_report_author_task(get_report_author_agent(llm),output_dir),
        get_report_verifier_task(get_report_verifier_agent(llm),output_dir)
    ],
    process=Process.sequential,
    knowledge_sources=[company_context]

)
crew_result=company.kickoff(
    inputs={
        "product_name":"coffe machine for the office",
        "websites_list":["www.amazon.eg","www.jumia.com.eg","www.noon.com/egypt-en"],
        "country_name":"Egypt",
        "no_keywords":10,
        "language":"Arabic",
        "score_threeshold":0.10,
        "top_recommendations_no":10

    }

)
