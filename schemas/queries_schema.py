from pydantic import BaseModel, Field
from typing import List

class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(description="List of suggested search queries", min_items=1, max_items=10)