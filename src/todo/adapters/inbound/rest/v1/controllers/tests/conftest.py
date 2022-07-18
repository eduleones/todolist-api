import uuid
from datetime import datetime

import pytest

from todo.domain.entities.enums import TaskStatus
from todo.domain.entities.task import Task


@pytest.fixture
def create_update_task_payload():
    return {
        "title": "Mocked Test Task",
        "description": "Mocked Test Task Description",
        "status": "TODO",
    }


@pytest.fixture
def task_response():
    return Task(
        id=uuid.uuid4(),
        title="Mocked Test Task",
        description="Mocked Test Task Description",
        status=TaskStatus.TODO,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
