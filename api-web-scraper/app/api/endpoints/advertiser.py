from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.advertiser_schema import AdvertiserSchema, PaginatedAdvertisersSchema
from app.service.advertiser_service import AdvertiserService
from app.dependencies.advertiser_filters import AdvertiserFilters
from app.dependencies.pagination_params import PaginationParams


router = APIRouter(
    prefix="/advertiser",
    tags=["advertiser"]
)

@router.get("/", response_model=Optional[List[AdvertiserSchema]])
@inject
def get_all(service: AdvertiserService = Depends(Provide[Container.advertiser_service])):
    return service.get_all()

@router.get("/search", response_model=Optional[PaginatedAdvertisersSchema])
@inject
def get_advertiser(
    filters: AdvertiserFilters = Depends(),
    pagination: PaginationParams = Depends(),
    service: AdvertiserService = Depends(Provide[Container.advertiser_service])):
    return service.get_advertiser(filters, pagination=pagination)