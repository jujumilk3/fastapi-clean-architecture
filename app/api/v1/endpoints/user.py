from fastapi import APIRouter, Depends


router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.get('')
async def get_user():
    return {'hello': 'world'}
