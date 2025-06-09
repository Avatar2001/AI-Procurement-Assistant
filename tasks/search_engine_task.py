from crewai import Task
from schemas.search_result_schema import AllSearchResults
import os

def get_search_engine_task(agent, output_dir):
    return Task(
    description="\n".join([
        "the task is to search for products based on the suggested search query.",
        "You have to collect results from multpile search queries.",
        "Ignore any susbicious links or not an ecommerce single website link.",
        "Ignore any search results with confidence score less than ({score_threeshold}).",
        "The search result will be used to compare prices of products from diffferent websites."
    ]),
        expected_output="List of search results with score and query.",
        output_json=AllSearchResults,
        output_file=os.path.join(output_dir, "search_results.json"),
        agent=agent
    )