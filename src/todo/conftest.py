import pytest
from httpx import AsyncClient

from todo.adapters.inbound.rest.containers import TestAdapters
from todo.adapters.inbound.rest.main import app


@pytest.fixture(scope="module")
def fastapi_app():
    return app


@pytest.fixture(scope="module")
async def async_client(fastapi_app):
    async with AsyncClient(
        app=fastapi_app, base_url="http://localhost", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module", autouse=True)
def create_database():
    TestAdapters.db().create_database()


@pytest.fixture(scope="session")
def task_repository():
    return TestAdapters.task_repository()
