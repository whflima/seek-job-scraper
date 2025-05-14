from typing import Optional
from fastapi import Query


class AdvertiserFilters:
    def __init__(
        self,
        id: Optional[int] = Query(None, description="Filter by advertiser ID."),
        name: Optional[str] = Query(None, description="Filter by advertiser name."),
        sort_by: str = Query("id", enum=["id", "name"], description="Field to sort by."),
        order: str = Query("asc", enum=["asc", "desc"], description="Sort order direction."),
    ):
        self.id = id
        self.name = name
        self.sort_by = sort_by
        self.order = order
        
