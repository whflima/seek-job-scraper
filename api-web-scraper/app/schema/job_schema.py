from typing import List, Optional
from pydantic import BaseModel

from app.schema.pagination_schema import PaginationSchema

class JobSchema(BaseModel):
    job_id: int
    title: str
    link: str
    created_at: str
    advertiser_name: Optional[str]
    
    class Config:
        orm_mode = True
        from_attributes = True

class PaginatedJobSchema(BaseModel):
    pagination: PaginationSchema
    items: List[JobSchema]