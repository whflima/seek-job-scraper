from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.job_schema import JobSchema
from app.service.job_service import JobService


router = APIRouter(
    prefix="/job",
    tags=["job"]
)

@router.get("/", response_model=Optional[List[JobSchema]])
@inject
def get_all(service: JobService = Depends(Provide[Container.job_service])):
    return service.get_all()