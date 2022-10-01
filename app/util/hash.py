import uuid


def get_rand_hash(length=16):
    return uuid.uuid4().hex[:length]
