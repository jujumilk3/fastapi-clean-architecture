from sqlmodel import Field

from app.model.base_model import BaseModel


class User(BaseModel, table=True):
    email: str = Field(default=None, nullable=True)
    password: str = Field(default=None, nullable=True)

    name: str = Field(default=None, nullable=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
