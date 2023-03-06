from sqlalchemy import Column, String, Boolean
from app.model.base_model import BaseModel


class User(BaseModel, table=True):
    email: str = Column(unique=True)
    password: str = Column()
    user_token: str = Column(unique=True)

    name: str = Column(default=None, nullable=True)
    is_active: bool = Column(default=True)
    is_superuser: bool = Column(default=False)
