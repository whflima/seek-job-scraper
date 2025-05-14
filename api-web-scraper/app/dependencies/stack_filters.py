from typing import Optional
from fastapi import Query


class StackFilters:
    def __init__(
        self,
        id: Optional[int] = Query(None, description="Filter by stack ID."),
        category: Optional[str] = Query(None, description="Filter by stack category."),
        subcategory: Optional[str] = Query(None, description="Filter by stack subcategory."),
        stack: Optional[str] = Query(None, description="Filter by stack name."),
        sort_by: str = Query("id", enum=["id", "category", "subcategory", "stack"], description="Field to sort by."),
        order: str = Query("asc", enum=["asc", "desc"], description="Sort order direction."),
    ):
        self.id = id
        self.category = category
        self.subcategory = subcategory
        self.stack = stack
        self.sort_by = sort_by
        self.order = order