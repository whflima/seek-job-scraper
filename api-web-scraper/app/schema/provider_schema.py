from typing import List
from pydantic import BaseModel

from app.schema.pagination_schema import PaginationSchema

class ProviderSchema(BaseModel):
    website_provider_id: int
    created_at: str
    name: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class PaginatedProviderSchema(BaseModel):
    pagination: PaginationSchema
    items: List[ProviderSchema]