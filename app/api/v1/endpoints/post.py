from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_active_user
from app.model.post import Post
from app.model.user import User
from app.schema.base_schema import Blank
from app.schema.post_tag_schema import (
    FindPost,
    FindPostWithTagsResult,
    PostWithTags,
    UpsertPostWithTags,
)
from app.services.post_service import PostService

router = APIRouter(
    prefix="/post",
    tags=["post"],
)


@router.get("", response_model=FindPostWithTagsResult)
@inject
async def get_post_list(
    find_query: FindPost = Depends(),
    service: PostService = Depends(Provide[Container.post_service]),
):
    return service.get_list(find_query)


@router.get("/{id}", response_model=PostWithTags)
@inject
async def get_post(
    id: int,
    service: PostService = Depends(Provide[Container.post_service]),
):
    return service.get_by_id(id)


@router.post("", response_model=PostWithTags)
@inject
async def create_post(
    post: UpsertPostWithTags,
    service: PostService = Depends(Provide[Container.post_service]),
    current_user: User = Depends(get_current_active_user),
):
    post.user_token = current_user.user_token
    return service.add(post)


@router.patch("/{id}", response_model=PostWithTags)
@inject
async def update_post(
    id: int,
    post: UpsertPostWithTags,
    service: PostService = Depends(Provide[Container.post_service]),
    current_user: User = Depends(get_current_active_user),
):
    return service.patch(id, post)


@router.delete("/{id}", response_model=Blank)
@inject
async def delete_post(
    id: int,
    service: PostService = Depends(Provide[Container.post_service]),
    current_user: User = Depends(get_current_active_user),
):
    return service.remove_by_id(id)
