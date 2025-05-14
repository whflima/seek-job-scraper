from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.provider_schema import ProviderSchema, PaginatedProviderSchema
from app.service.provider_service import ProviderService
from app.dependencies.provider_filters import ProviderFilters
from app.dependencies.pagination_params import PaginationParams


router = APIRouter(
    prefix="/provider",
    tags=["provider"]
)

@router.get("/", response_model=Optional[List[ProviderSchema]])
@inject
def get_all(service: ProviderService = Depends(Provide[Container.provider_service])):
    return service.get_all()

@router.get("/search", response_model=Optional[PaginatedProviderSchema])
@inject
def get_advertiser(
    filters: ProviderFilters = Depends(),
    pagination: PaginationParams = Depends(),
    service: ProviderService = Depends(Provide[Container.provider_service])):
    return service.get_provider(filters, pagination=pagination)