import pytest
from httpx import AsyncClient

from todo.adapters.inbound.rest.main import app


@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(
        app=app, base_url="http://localhost", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
