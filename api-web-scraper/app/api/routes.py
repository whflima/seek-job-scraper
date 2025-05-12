from fastapi import APIRouter

from app.api.endpoints.advertiser import router as advertiser_router
from app.api.endpoints.provider import router as provider_router

routers = APIRouter()
router_list = [advertiser_router, provider_router]

for router in router_list:
    routers.include_router(router)