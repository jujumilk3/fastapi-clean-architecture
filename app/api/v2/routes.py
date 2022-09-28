from fastapi import APIRouter

from app.api.v2.endpoints.auth import router as auth_router

routers = APIRouter()
router_list = [auth_router]

for router in router_list:
    router.tags = routers.tags.append("v2")
    routers.include_router(router)
