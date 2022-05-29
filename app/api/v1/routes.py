from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.post import router as post_router
from app.api.v1.endpoints.user import router as user_router

routers = APIRouter()
routers.include_router(auth_router)
routers.include_router(post_router)
routers.include_router(user_router)
