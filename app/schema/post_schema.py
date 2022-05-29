from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.utils.schema import AllOptional


class BasePost(BaseModel):
    title: str
    content: str
    is_published: bool

    class Config:
        orm_mode = True


class Post(ModelBaseInfo, BasePost, metaclass=AllOptional):
    ...


class FindPost(FindBase, BasePost, metaclass=AllOptional):
    ...


class UpsertPost(BasePost, metaclass=AllOptional):
    ...


class FindPostResult(BaseModel):
    founds: Optional[List[Post]]
    search_options: Optional[SearchOptions]
