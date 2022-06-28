from app.services.base_service import BaseService
from app.repositories.tag_repository import TagRepository


class TagService(BaseService):
    def __init__(self, tag_repository: TagRepository):
        self.tag_repository = tag_repository
        super().__init__(tag_repository)
