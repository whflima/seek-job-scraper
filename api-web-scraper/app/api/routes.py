from fastapi import APIRouter

from app.api.endpoints.advertiser import router as advertiser_router
from app.api.endpoints.provider import router as provider_router
from app.api.endpoints.job import router as job_router
from app.api.endpoints.stack import router as stack_router

routers = APIRouter()
router_list = [advertiser_router, provider_router, job_router, stack_router]

for router in router_list:
    routers.include_router(router)