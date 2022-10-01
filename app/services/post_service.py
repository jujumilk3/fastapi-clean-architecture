from app.repository.post_repository import PostRepository
from app.repository.tag_repository import TagRepository
from app.schema.post_tag_schema import FindTag, UpsertPostWithTags
from app.services.base_service import BaseService


class PostService(BaseService):
    def __init__(self, post_repository: PostRepository, tag_repository: TagRepository):
        self.post_repository = post_repository
        self.tag_repository = tag_repository
        super().__init__(post_repository)

    def add(self, schema: UpsertPostWithTags):
        find_tag = FindTag()
        find_tag.page_size = "all"
        tags = None
        if len(schema.tag_ids):
            find_tag.id__in = ",".join(map(str, schema.tag_ids))
            tags = self.tag_repository.read_by_options(find_tag)["founds"]
        delattr(schema, "tag_ids")
        return self.post_repository.create_with_tags(schema, tags)

    def patch(self, id: int, schema: UpsertPostWithTags):
        find_tag = FindTag()
        find_tag.page_size = "all"
        tags = None
        if schema.tag_ids:
            find_tag.id__in = ",".join(map(str, schema.tag_ids))
            tags = self.tag_repository.read_by_options(find_tag)["founds"]
        delattr(schema, "tag_ids")
        return self.post_repository.update_with_tags(id, schema, tags)
