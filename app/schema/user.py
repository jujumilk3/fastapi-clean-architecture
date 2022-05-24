from typing import List, Optional

from pydantic import BaseModel

from app.schema.base import ModelBaseInfo
from app.utils.schema import AllOptional


class BaseUser(BaseModel):
    email: str
    password: str
    name: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
    ...
