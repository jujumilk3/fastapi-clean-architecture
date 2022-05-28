class BaseService:
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_list(self, schema):
        return self._repository.read_by_options(schema)

    def get_by_id(self, id: int):
        return self._repository.read_by_id(id)

    def add(self, schema):
        return self._repository.create(schema)

    def patch(self, id: int, schema):
        return self._repository.update(id, schema)

    def patch_attr(self, id: int, attr: str, value):
        return self._repository.update_attr(id, attr, value)

    def put_update(self, id: int, schema):
        return self._repository.whole_update(id, schema)

    def remove_by_id(self, id):
        return self._repository.delete_by_id(id)
