from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from sqlalchemy.orm import relationship

from app.core.database import BaseModel
from app.models.post_tag_model import PostTagModel
from app.utils.date import get_now


class TagModel(BaseModel):
    __tablename__ = 'tag'

    id = Column(INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True)

    name = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255), nullable=True)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)

    posts = relationship('PostModel', secondary=PostTagModel, overlaps='tags')
