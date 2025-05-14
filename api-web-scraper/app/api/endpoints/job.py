from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.job_schema import JobSchema, PaginatedJobSchema
from app.service.job_service import JobService
from app.dependencies.job_filters import JobFilters
from app.dependencies.pagination_params import PaginationParams


router = APIRouter(
    prefix="/job",
    tags=["job"]
)

@router.get("/", response_model=Optional[List[JobSchema]])
@inject
def get_all(service: JobService = Depends(Provide[Container.job_service])):
    return service.get_all()

@router.get("/search", response_model=Optional[PaginatedJobSchema])
@inject
def get_job(
    filters: JobFilters = Depends(),
    pagination: PaginationParams = Depends(),
    service: JobService = Depends(Provide[Container.job_service])):
    return service.get_job(filters, pagination=pagination)