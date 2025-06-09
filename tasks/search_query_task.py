from crewai import Task
from schemas.queries_schema import SuggestedSearchQueries
import os

def get_search_query_task(agent, output_dir):
    return Task(
            description="\n".join([
        "company is looking to buy {product_name} at the best prices (value for a price strategy)",
        "the company target any of these websites to buy from:{websites_list}",
        "the company wants to reach all available poducts on the intenet to be compared later in another stage.",
        "the stores must sell the poduct in {country_name}",
        "Generate only {no_keywords} querries.",
        "The search keywords must be in {language} language.",
        "Search keywods could mention specific brands, types o technologies",
        "The search query must an ecommerce webpage for product, and not a blog or listing page."



    ]),
        expected_output="JSON list of queries",
        output_json=SuggestedSearchQueries,
        output_file=os.path.join(output_dir, "search_queries.json"),
        agent=agent
    )