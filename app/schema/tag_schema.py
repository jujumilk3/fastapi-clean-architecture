from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.utils.schema import AllOptional


class BaseTag(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class Tag(ModelBaseInfo, BaseTag, metaclass=AllOptional):
    ...


class FindTag(FindBase, BaseTag, metaclass=AllOptional):
    ...


class UpsertTag(BaseTag, metaclass=AllOptional):
    ...


class FindTagResult(BaseModel):
    founds: Optional[List[Tag]]
    search_options: Optional[SearchOptions]
