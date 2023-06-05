from typing import Generator
import pytest
from fastapi.testclient import TestClient
from python_boilerplate.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
