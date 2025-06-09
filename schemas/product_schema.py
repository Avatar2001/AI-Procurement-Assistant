from pydantic import BaseModel, Field
from typing import List

class ProductSpecs(BaseModel):
    specification_name: str
    specification_value: str

class SingleExtractedProduct(BaseModel):
    page_url: str
    product_title: str
    product_image_url: str
    product_url: str
    product_current_price: float
    product_original_price: float = None
    product_discount_percentage: float = None
    product_description: str
    product_specs: List[ProductSpecs] = Field(min_items=1, max_items=5)
    agent_recommendation_rank: int = Field(..., title="1-5, higher is better")
    agent_recommendation_notes: str

class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]
