from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME

from app.core.database import BaseModel
from app.utils.date import get_now


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True)

    email = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)

    name = Column(VARCHAR(255), nullable=True)

    is_active = Column(BOOLEAN, default=True)
    is_superuser = Column(BOOLEAN, default=False)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)
