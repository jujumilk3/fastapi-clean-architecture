from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME, TEXT
from sqlalchemy.orm import relationship

from app.core.database import BaseModel
from app.models.user_model import UserModel
from app.utils.date import get_now


class PostModel(BaseModel):
    __tablename__ = 'post'

    id = Column(INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey(UserModel.id))

    title = Column(VARCHAR(255), nullable=False)
    content = Column(TEXT, nullable=False)
    is_published = Column(BOOLEAN, default=False)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)

    user = relationship('User', foreign_key='PostModel.user_id')
