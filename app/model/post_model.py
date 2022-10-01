from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import BOOLEAN, DATETIME, INTEGER, TEXT, VARCHAR
from sqlalchemy.orm import relationship

from app.core.database import BaseModel
from app.model.post_tag_model import PostTagModel
from app.model.user import User
from app.utils.date import get_now


class PostModel(BaseModel):
    __tablename__ = 'post'

    id = Column(INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey(User.id))

    title = Column(VARCHAR(255), nullable=True)
    content = Column(TEXT, nullable=True)
    is_published = Column(BOOLEAN, default=False)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)

    user = relationship('User', foreign_keys='PostModel.user_id')
    tags = relationship('TagModel', secondary=PostTagModel, overlaps='posts', lazy='joined')
