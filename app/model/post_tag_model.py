from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, VARCHAR

from app.core.database import BaseModel
from app.utils.date import get_now

PostTagModel = Table('post_tag', BaseModel.metadata,
                     Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True),
                     Column('post_id', INTEGER(unsigned=True), ForeignKey('post.id'), primary_key=True),
                     Column('tag_id', INTEGER(unsigned=True), ForeignKey('tag.id'), primary_key=True),
                     Column('memo', VARCHAR(255), nullable=True),
                     Column('created_at', DATETIME, nullable=True, default=get_now),
                     Column('updated_at', DATETIME, nullable=True, default=get_now, onupdate=get_now)
                     )
