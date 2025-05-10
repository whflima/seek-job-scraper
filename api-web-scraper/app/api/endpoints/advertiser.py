from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.service.advertiser_service import AdvertiserService


router = APIRouter(
    prefix="/advertiser",
    tags=["advertiser"]
)

@router.get("/")
@inject
def get_all(service: AdvertiserService = Depends(Provide[Container.advertiser_service])):
    return service.get_all()