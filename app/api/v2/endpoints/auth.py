from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_active_user
from app.schema.auth_schema import SignIn, SignUp, SignInResponse
from app.schema.user_schema import User as UserSchema
from app.models.user_model import UserModel
from app.services.auth_service import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/sign-in', response_model=SignInResponse)
@inject
async def sign_in(
    user_info: SignIn,
    service: AuthService = Depends(Provide[Container.auth_service])
):
    return service.sign_in(user_info)


@router.post('/sign-up', response_model=UserSchema)
@inject
async def sign_up(
    user_info: SignUp,
    service: AuthService = Depends(Provide[Container.auth_service])
):
    return service.sign_up(user_info)


@router.get('/me', response_model=UserSchema)
@inject
async def get_me(
    current_user: UserModel = Depends(get_current_active_user)
):
    user = UserSchema()
    user.name = current_user.name
    user.email = current_user.email
    user.created_at = current_user.created_at
    return user
