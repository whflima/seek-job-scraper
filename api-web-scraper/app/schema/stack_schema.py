from typing import List
from pydantic import BaseModel

from app.schema.pagination_schema import PaginationSchema

class StackSchema(BaseModel):
    tech_stack_id: int
    category: str
    subcategory: str
    stack: str
    created_at: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class PaginatedStacksSchema(BaseModel):
    pagination: PaginationSchema
    items: List[StackSchema]