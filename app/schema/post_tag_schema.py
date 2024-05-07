# many to many schemas must be contained at one schema file to prevent cyclic reference
from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional


class BasePost(BaseModel):
    user_token: str
    title: str
    content: str
    is_published: bool

    class Config:
        orm_mode = True


class Post(ModelBaseInfo, BasePost, metaclass=AllOptional): ...


class FindPost(FindBase, BasePost, metaclass=AllOptional): ...


class UpsertPost(BasePost, metaclass=AllOptional): ...


class FindPostResult(BaseModel):
    founds: Optional[List[Post]]
    search_options: Optional[SearchOptions]


class BaseTag(BaseModel):
    user_token: str
    name: str
    description: str

    class Config:
        orm_mode = True


class Tag(ModelBaseInfo, BaseTag, metaclass=AllOptional): ...


class FindTag(FindBase, BaseTag, metaclass=AllOptional):
    id__in: str


class UpsertTag(BaseTag, metaclass=AllOptional): ...


class FindTagResult(BaseModel):
    founds: Optional[List[Tag]]
    search_options: Optional[SearchOptions]


# for many to many


class PostWithTags(Post):
    tags: Optional[List[Tag]]


class TagWithPosts(Tag):
    posts: Optional[List[Post]]


class UpsertPostWithTags(UpsertPost):
    tag_ids: Optional[List[int]]


class UpsertTagWithPosts(UpsertTag):
    post_ids: Optional[List[int]]


class FindPostWithTagsResult(BaseModel):
    founds: Optional[List[PostWithTags]]
    search_options: Optional[SearchOptions]


class FindTagWithPostsResult(BaseModel):
    founds: Optional[List[TagWithPosts]]
    search_options: Optional[SearchOptions]
