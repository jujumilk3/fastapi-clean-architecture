from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func, Integer


class BaseDatetimeColumns:
    id: int = Column(Integer, primary_key=True, index=True)
    created_at: datetime = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), default=datetime.utcnow
    )
    updated_at: datetime = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), default=datetime.utcnow
    )


BaseModel = declarative_base(cls=BaseDatetimeColumns)
