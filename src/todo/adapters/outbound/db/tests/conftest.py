import pytest

from todo.domain.entities.enums import TaskStatus
from todo.domain.entities.task import Task


@pytest.fixture
def task():
    return Task(
        title="Test Task",
        description="Test Task Description",
        status=TaskStatus.TODO,
    )
