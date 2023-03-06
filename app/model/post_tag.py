from sqlalchemy import Column, Integer, String

from app.model.base_model import BaseModel


class PostTag(BaseModel):
    __tablename__ = "post_tag"
    post_id: int = Column(foreign_key="post.id", primary_key=True, index=True, nullable=False)
    tag_id: int = Column(foreign_key="tag.id", primary_key=True, index=True, nullable=False)
