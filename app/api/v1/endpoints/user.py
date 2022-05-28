from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.base_schema import Blank
from app.schema.user_schema import FindUser, User, UpsertUser, FindUserResult
from app.services.user_service import UserService


router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.get('', response_model=FindUserResult)
@inject
async def get_user_list(
        find_query: FindUser = Depends(),
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_list(find_query)


@router.get('/{id}', response_model=User)
@inject
async def get_user(
        id: int,
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_by_id(id)


@router.post('', response_model=User)
@inject
async def create_user(
        user: UpsertUser,
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.add(user)


@router.patch('/{id}', response_model=User)
@inject
async def update_user(
        id: int,
        user: UpsertUser,
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.patch(id, user)


@router.delete('/{id}', response_model=Blank)
@inject
async def delete_user(
        id: int,
        service: UserService = Depends(Provide[Container.user_service]),
):
    return service.remove_by_id(id)
