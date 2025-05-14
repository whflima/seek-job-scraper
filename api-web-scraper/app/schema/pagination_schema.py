from typing import Optional
from pydantic import BaseModel


class PaginationSchema(BaseModel):
   total_records: int
   current_page: int
   total_pages: int
   next_page: Optional[int]
   prev_page: Optional[int]
   
   class Config:
    from_attributes = True