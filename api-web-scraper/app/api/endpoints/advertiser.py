from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.advertiser_schema import AdvertiserSchema
from app.service.advertiser_service import AdvertiserService


router = APIRouter(
    prefix="/advertiser",
    tags=["advertiser"]
)

@router.get("/", response_model=Optional[List[AdvertiserSchema]])
@inject
def get_all(service: AdvertiserService = Depends(Provide[Container.advertiser_service])):
    return service.get_all()