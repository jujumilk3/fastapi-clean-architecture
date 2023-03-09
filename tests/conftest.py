import json
import os

import pytest

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

from fastapi.testclient import TestClient
from loguru import logger
from sqlmodel import SQLModel, create_engine

from app.core.config import configs
from app.core.container import Container
from app.main import AppCreator
from app.model.post import Post
from app.model.user import User


def insert_default_data(conn):
    user_default_file = open("./tests/test_data/users.json", "r")
    user_default_data = json.load(user_default_file)
    for user in user_default_data:
        conn.execute(
            User.__table__.insert(),
            {
                "email": user["email"],
                "password": user["password"],
                "user_token": user["user_token"],
                "name": user["name"],
                "is_active": user["is_active"],
                "is_superuser": user["is_superuser"],
            },
        )
    post_default_file = open("./tests/test_data/posts.json", "r")
    post_default_data = json.load(post_default_file)
    for post in post_default_data:
        conn.execute(
            Post.__table__.insert(),
            {
                "title": post["title"],
                "content": post["content"],
                "user_token": post["user_token"],
                "is_published": post["is_published"],
            },
        )


def reset_db():
    engine = create_engine(configs.DATABASE_URI)
    logger.info(engine)
    with engine.begin() as conn:
        if "test" in configs.DATABASE_URI:
            SQLModel.metadata.drop_all(conn)
            SQLModel.metadata.create_all(conn)
            insert_default_data(conn)
        else:
            raise Exception("Not in test environment")
    return engine


@pytest.fixture
def client():
    reset_db()
    app_creator = AppCreator()
    app = app_creator.app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def container():
    return Container()


@pytest.fixture
def test_name(request):
    return request.node.name
