from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from app.repositories.base_repository import BaseRepository
from app.models.user_model import UserModel


class UserRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, UserModel)
