from typing import List
from pydantic import BaseModel

from app.schema.pagination_schema import PaginationSchema

class AdvertiserSchema(BaseModel):
    advertiser_id: int
    name: str
    
    class Config:
        orm_mode = True
        from_attributes = True

class PaginatedAdvertisersSchema(BaseModel):
    pagination: PaginationSchema
    items: List[AdvertiserSchema]