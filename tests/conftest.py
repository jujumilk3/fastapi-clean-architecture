import os

import pytest
from fastapi.testclient import TestClient

from app.main import app

os.environ["ENV"] = "test"

if os.getenv("ENV") not in ["test"]:
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
