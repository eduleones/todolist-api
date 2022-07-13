import uuid
from http import HTTPStatus
from unittest import mock

import pytest

from todo.domain.ports.inbound.task.port import (
    CreateTaskInterface,
    UpdateTaskInterface,
)

pytestmark = pytest.mark.anyio


class TestTaskAPI:
    async def test_create_task_api(
        self,
        fastapi_app,
        async_client,
        create_update_task_payload,
        task_response,
    ):
        use_case_mock = mock.Mock(spec=CreateTaskInterface)
        use_case_mock.create_task.return_value = task_response

        with fastapi_app.container.create_task.override(use_case_mock):

            response = await async_client.post(
                "/v1/tasks", json=create_update_task_payload
            )

            result = response.json()

            assert response.status_code == HTTPStatus.CREATED

            assert result["id"] is not None
            assert result["title"] == create_update_task_payload["title"]
            assert (
                result["description"]
                == create_update_task_payload["description"]
            )
            assert result["status"] == create_update_task_payload["status"]

    async def test_update_task_api(
        self,
        fastapi_app,
        async_client,
        create_update_task_payload,
        task_response,
    ):
        use_case_mock = mock.Mock(spec=UpdateTaskInterface)
        use_case_mock.update_task.return_value = task_response

        with fastapi_app.container.update_task.override(use_case_mock):

            task_id = uuid.uuid4()
            response = await async_client.put(
                f"/v1/tasks/{task_id}", json=create_update_task_payload
            )

            result = response.json()

            assert response.status_code == HTTPStatus.OK

            assert result["id"] is not None
            assert result["title"] == create_update_task_payload["title"]
            assert (
                result["description"]
                == create_update_task_payload["description"]
            )
            assert result["status"] == create_update_task_payload["status"]
