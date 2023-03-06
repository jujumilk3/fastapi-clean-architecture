from app.model.base_model import BaseModel
from sqlalchemy import Column, String, Boolean


class Tag(BaseModel):
    user_token: str = Column(String, nullable=False, unique=True)

    name: str = Column(String, default="", nullable=False)
    description: str = Column(String, default="", nullable=False)
