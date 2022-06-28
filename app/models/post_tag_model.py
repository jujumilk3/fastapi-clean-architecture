from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME

from app.core.database import BaseModel
from app.models.post_model import PostModel
from app.models.tag_model import TagModel
from app.utils.date import get_now


class PostTagModel(BaseModel):
    __tablename__ = 'post_tag'

    id = Column(INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True)

    post_id = Column(INTEGER(unsigned=True), ForeignKey(PostModel.id))
    tag_id = Column(INTEGER(unsigned=True), ForeignKey(TagModel.id))

    memo = Column(VARCHAR(255), nullable=True)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)

