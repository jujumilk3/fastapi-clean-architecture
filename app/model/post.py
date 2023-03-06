from app.model.base_model import Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Post(Base):
    user_token: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    title: Mapped[str] = mapped_column(String, default="", nullable=False)
    content: Mapped[str] = mapped_column(String, default="", nullable=False)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
