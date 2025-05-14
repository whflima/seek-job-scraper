from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.stack import Stack
from app.schema.stack_schema import PaginatedStacksSchema
from app.schema.pagination_schema import PaginationSchema
from app.dependencies.stack_filters import StackFilters
from app.dependencies.pagination_params import PaginationParams

class StackRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self._session_factory = session_factory
        self.model = Stack
    
    def get_all(self):
        with self._session_factory() as session:
            return session.query(self.model).all()
    
    def get_stack(self, filters: StackFilters, pagination: PaginationParams):
        with self._session_factory() as session:
            query = session.query(self.model)

            if filters.id:
                query = query.filter(Stack.tech_stack_id == filters.id)            
            if filters.stack:
                query = query.filter(Stack.stack.ilike(f"%{filters.stack}%"))
            if filters.category:
                query = query.filter(Stack.category.ilike(f"%{filters.category}%"))
            if filters.subcategory:
                query = query.filter(Stack.subcategory.ilike(f"%{filters.subcategory}%"))
                   
            sort_column = getattr(Stack, filters.sort_by, Stack.tech_stack_id)
            if filters.order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())
            
            total_records = query.count()
            total_pages = (total_records + pagination.limit - 1) // pagination.limit
            current_page = pagination.page
            next_page = current_page + 1 if current_page < (total_pages - 1) else None
            prev_page = current_page - 1 if current_page > 1 else None
   
            page_info = PaginationSchema(total_records=total_records, current_page=current_page, next_page=next_page, total_pages=total_pages, prev_page=prev_page)
            items = query.offset(pagination.skip).limit(pagination.limit).all()
            return PaginatedStacksSchema(items=items, pagination=page_info)