from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.advertiser import Advertiser
from app.schema.advertiser_schema import PaginatedAdvertisersSchema
from app.schema.pagination_schema import PaginationSchema
from app.dependencies.advertiser_filters import AdvertiserFilters
from app.dependencies.pagination_params import PaginationParams

class AdvertiserRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self._session_factory = session_factory
        self.model = Advertiser
    
    def get_all(self):
        with self._session_factory() as session:
            return session.query(self.model).all()
    
    def get_advertiser(self, filters: AdvertiserFilters, pagination: PaginationParams):
        with self._session_factory() as session:
            query = session.query(self.model)
            query = self._apply_filters(query, filters)
            query = self._apply_sorting(query, filters)
            
            total_records = query.count()
            items = query.offset(pagination.skip).limit(pagination.limit).all()
   
            page_info = self._get_pagination_info(total_records, pagination)
            return PaginatedAdvertisersSchema(items=items, pagination=page_info)
    
    def _apply_filters(self, query, filters: AdvertiserFilters):
        if filters.id:
            query = query.filter(Advertiser.advertiser_id == filters.id)            
        if filters.name:
            query = query.filter(Advertiser.name.ilike(f"%{filters.name}%"))
        return query
    
    def _apply_sorting(self, query, filters: AdvertiserFilters):
        sort_column = getattr(Advertiser, filters.sort_by, Advertiser.advertiser_id)
        if filters.order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())
        return query
    
    def _get_pagination_info(self, total_records: int, pagination: PaginationParams):
        total_pages = (total_records + pagination.limit - 1) // pagination.limit
        current_page = pagination.page
        next_page = current_page + 1 if current_page < (total_pages - 1) else None
        prev_page = current_page - 1 if current_page > 1 else None
        
        return PaginationSchema(
            total_records=total_records, 
            current_page=current_page, 
            next_page=next_page, 
            total_pages=total_pages, 
            prev_page=prev_page
        )