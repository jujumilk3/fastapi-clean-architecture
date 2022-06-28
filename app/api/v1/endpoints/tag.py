from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_active_user
from app.core.security import JWTBearer
from app.models.user_model import UserModel
from app.schema.base_schema import Blank
from app.schema.post_tag_schema import FindTag, Tag, UpsertTag, FindTagResult
from app.services.tag_service import TagService

router = APIRouter(
    prefix='/tag',
    tags=['tag'],
)


@router.get('', response_model=FindTagResult)
@inject
async def get_tag_list(
        find_query: FindTag = Depends(),
        service: TagService = Depends(Provide[Container.tag_service]),
):
    return service.get_list(find_query)


@router.get('/{id}', response_model=Tag)
@inject
async def get_tag(
        id: int,
        service: TagService = Depends(Provide[Container.tag_service]),
):
    return service.get_by_id(id)


@router.post('', response_model=Tag)
@inject
async def create_tag(
        tag: UpsertTag,
        service: TagService = Depends(Provide[Container.tag_service]),
        current_user: UserModel = Depends(get_current_active_user)
):
    return service.add(tag)


@router.patch('/{id}', response_model=Tag)
@inject
async def update_tag(
        id: int,
        tag: UpsertTag,
        service: TagService = Depends(Provide[Container.tag_service]),
        current_user: UserModel = Depends(get_current_active_user)
):
    return service.patch(id, tag)


@router.delete('/{id}', response_model=Blank)
@inject
async def delete_tag(
        id: int,
        service: TagService = Depends(Provide[Container.tag_service]),
        current_user: UserModel = Depends(get_current_active_user)
):
    return service.remove_by_id(id)
