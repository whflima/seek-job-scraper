from typing import List, Optional
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.provider_schema import ProviderSchema
from app.service.provider_service import ProviderService


router = APIRouter(
    prefix="/provider",
    tags=["provider"]
)

@router.get("/", response_model=Optional[List[ProviderSchema]])
@inject
def get_all(service: ProviderService = Depends(Provide[Container.provider_service])):
    return service.get_all()