from sqlmodel import Field

from app.model.base_model import BaseModel


class User(BaseModel, table=True):
    email: str = Field(unique=True)
    password: str = Field()
    user_token: str = Field(unique=True)

    name: str = Field(default=None, nullable=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
