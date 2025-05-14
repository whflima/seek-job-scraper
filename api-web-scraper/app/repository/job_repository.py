from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session, selectinload

from app.model.job import Job
from app.model.advertiser import Advertiser
from app.schema.job_schema import PaginatedJobSchema
from app.schema.pagination_schema import PaginationSchema
from app.dependencies.job_filters import JobFilters
from app.dependencies.pagination_params import PaginationParams
from app.utils.job_utils import convert_jobs_to_schema

class JobRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self._session_factory = session_factory
        self.model = Job
    
    def get_all(self):
        with self._session_factory() as session:
            items = session.query(self.model).options(selectinload(Job.advertiser))    
            return convert_jobs_to_schema(items)
    
    def get_job(self, filters: JobFilters, pagination: PaginationParams):
        with self._session_factory() as session:
            query = session.query(self.model).options(selectinload(Job.advertiser))
            query = self._apply_filters(query, filters)
            query = self._apply_sorting(query, filters)
            
            total_records = query.count()
            items = query.offset(pagination.skip).limit(pagination.limit).all()
            
            jobs_schema = convert_jobs_to_schema(items)
            page_info = self._get_pagination_info(total_records, pagination)
            return PaginatedJobSchema(items=jobs_schema, pagination=page_info)

    def _apply_filters(self, query, filters: JobFilters):
        if filters.id:
            query = query.filter(Job.job_id == filters.id)            
        if filters.title:
            query = query.filter(Job.title.ilike(f"%{filters.title}%"))
        if filters.advertiser_name:
            query = query.join(Job.advertiser).filter(Advertiser.name.ilike(f"%{filters.advertiser_name}%"))
        return query
    
    def _apply_sorting(self, query, filters: JobFilters):
        sort_column = getattr(Job, filters.sort_by, Job.job_id)
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