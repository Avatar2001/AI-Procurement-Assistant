import json
from crewai.tools import tool
from scrapegraph_py import Client
import os
from schemas.product_schema import SingleExtractedProduct

client = Client(api_key=os.getenv("SCRAPEGRAPH_API_KEY"))

@tool
def Web_Scraping_tool(page_url: str,required_fields: list):
    """
    Scrapes the specified web page and extracts data according to the SingleExtractedProduct JSON schema.

    Args:
        page_url (str): The URL of the web page to scrape.

    Returns:
        dict: The extracted data in the format defined by SingleExtractedProduct.schema_json().
    """
    return client.smartscraper(
        website_url=page_url,
        user_prompt="Extract this JSON schema:\n" + json.dumps(required_fields, ensure_ascii=False)+"from the page.",
       # output_schema=SingleExtractedProduct.schema_json(),
      #  required_fields=required_fields
    )