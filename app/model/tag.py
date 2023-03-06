from app.model.base_model import BaseModel
from sqlalchemy import Column, String, Boolean


class Tag(BaseModel):
    user_token: str = Column()

    name: str = Column(unique=True)
    description: str = Column(default=None, nullable=True)
