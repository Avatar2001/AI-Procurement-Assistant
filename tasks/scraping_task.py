from crewai import Task
from schemas.product_schema import AllExtractedProducts
import os

def get_scraping_task(agent, output_dir):
    return Task(
     description="\n".join([
        "The task is to extract products details from any ecommerce store page url.",
        "The task has to collect results from multpile pages urls.",
        "Collect the best {top_recommendations_no} products from the search results.",

    ]),
        expected_output="Detailed JSON of products",
        output_json=AllExtractedProducts,
        output_file=os.path.join(output_dir, "extracted_details.json"),
        agent=agent
    )