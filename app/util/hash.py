import uuid


def get_rand_hash(length: int = 16) -> str:
    return uuid.uuid4().hex[:length]
