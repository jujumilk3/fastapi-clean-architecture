from sqlmodel import Field

from app.model.base_model import BaseModel


class PostTag(BaseModel, table=True):
    __tablename__ = "post_tag"
    post_id: int = Field(foreign_key="post.id", primary_key=True, index=True, nullable=False)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True, index=True, nullable=False)
