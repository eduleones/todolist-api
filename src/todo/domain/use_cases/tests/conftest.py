import pytest

from todo.domain.entities.enums import TaskStatus
from todo.domain.ports.inbound.task.dtos import CreateUpdateTaskDto


@pytest.fixture
def task_dto():
    return CreateUpdateTaskDto(
        title="Test Task",
        description="Test Task Description",
        status=TaskStatus.TODO,
    )
