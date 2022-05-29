from app.services.base_service import BaseService
from app.repositories.post_repository import PostRepository


class PostService(BaseService):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
        super().__init__(post_repository)
