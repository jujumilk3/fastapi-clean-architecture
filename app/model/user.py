from sqlalchemy import Column, String, Boolean
from app.model.base_model import BaseModel


class User(BaseModel, table=True):
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False, unique=True)
    user_token: str = Column(String, nullable=False, unique=True)

    name: str = Column(String, default="", nullable=False)
    is_active: bool = Column(Boolean, default=False, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
