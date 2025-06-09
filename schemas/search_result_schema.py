from pydantic import BaseModel
from typing import List

class SingleSeachResult(BaseModel):
    title: str
    link: str
    content: str
    score: float
    search_query: str

class AllSearchResults(BaseModel):
    results: List[SingleSeachResult]