from app.services.base_service import BaseService
from app.repositories.user_repository import UserRepository


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)
