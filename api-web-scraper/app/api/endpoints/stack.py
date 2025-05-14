from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.stack_schema import StackSchema, PaginatedStacksSchema
from app.service.stack_service import StackService
from app.dependencies.stack_filters import StackFilters
from app.dependencies.pagination_params import PaginationParams


router = APIRouter(
    prefix="/stack",
    tags=["stack"]
)

@router.get("/", response_model=Optional[List[StackSchema]])
@inject
def get_all(service: StackService = Depends(Provide[Container.stack_service])):
    return service.get_all()

@router.get("/search", response_model=Optional[PaginatedStacksSchema])
@inject
def get_advertiser(
    filters: StackFilters = Depends(),
    pagination: PaginationParams = Depends(),
    service: StackService = Depends(Provide[Container.stack_service])):
    return service.get_stack(filters, pagination=pagination)