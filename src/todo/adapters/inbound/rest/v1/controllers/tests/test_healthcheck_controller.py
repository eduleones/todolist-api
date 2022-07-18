from http import HTTPStatus

import pytest

pytestmark = pytest.mark.anyio


class TestHealthCheckAPI:
    async def test_health_check(self, async_client):
        response = await async_client.get(
            "/healthcheck",
        )
        assert response.status_code == HTTPStatus.OK
