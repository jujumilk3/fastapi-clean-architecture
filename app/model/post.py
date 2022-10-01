from sqlmodel import Field

from app.model.base_model import BaseModel


class Post(BaseModel, table=True):
    user_token: str = Field()

    title: str = Field(default=None, nullable=True)
    content: str = Field(default=None, nullable=True)
    is_published: bool = Field(default=False)
