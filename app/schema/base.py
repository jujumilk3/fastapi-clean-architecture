from datetime import datetime

from pydantic import BaseModel


class ModelBaseInfo(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
