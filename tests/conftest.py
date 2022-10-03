import os

import pytest

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)

from fastapi.testclient import TestClient
from loguru import logger
from sqlmodel import SQLModel, create_engine

from app.core.config import settings
from app.main import AppCreator
from app.core.container import Container


def reset_db():
    engine = create_engine(settings.DATABASE_URI_MAPPER["test"])
    logger.info(engine)
    with engine.begin() as conn:
        SQLModel.metadata.drop_all(conn)
        SQLModel.metadata.create_all(conn)
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
