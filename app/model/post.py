from app.model.base_model import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Post(Base):
    user_token: str = Column(String, nullable=False, unique=True)

    title: str = Column(String, default="", nullable=False)
    content: str = Column(String, default="", nullable=False)
    is_published: bool = Column(Boolean, default=False, nullable=False)
