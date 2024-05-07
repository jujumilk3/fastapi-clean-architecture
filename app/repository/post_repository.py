from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.model.post import Post
from app.repository.base_repository import BaseRepository
from app.schema.post_tag_schema import UpsertPostWithTags


class PostRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Post)

    def create_with_tags(self, schema: UpsertPostWithTags, tags):
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            session.add(query)
            if tags:
                query.tags = tags
            session.commit()
            session.refresh(query)
            return query

    def update_with_tags(self, id: int, schema: UpsertPostWithTags, tags):
        with self.session_factory() as session:
            session.query(self.model).filter(self.model.id == id).update(schema.dict(exclude_none=True))
            query = session.query(self.model).filter(self.model.id == id).first()
            if tags:
                query.tags = []
                session.flush()
                query.tags = tags
            else:
                query.tags = []
            session.commit()
            session.refresh(query)
            return self.read_by_id(id)
