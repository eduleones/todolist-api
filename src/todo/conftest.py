import pytest
from httpx import AsyncClient

from todo.adapters.inbound.rest.containers import UseCases
from todo.adapters.inbound.rest.factories import get_application
from todo.adapters.inbound.rest.tests.containers import Adapters


@pytest.fixture(scope="module")
def fastapi_app():
    container = UseCases(adapters=Adapters())
    return get_application(container=container)


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
    Adapters.db().create_database()


@pytest.fixture(scope="session")
def task_repository():
    return Adapters.task_repository()
