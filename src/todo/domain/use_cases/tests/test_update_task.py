import uuid

import pytest

from todo.domain.entities.enums import TaskStatus
from todo.domain.entities.task import Task
from todo.domain.exceptions.task_exceptions import (
    InvalidTaskException,
    TaskNotFoundException,
)
from todo.domain.use_cases.create_task import CreateTask
from todo.domain.use_cases.update_task import UpdateTask


class TestUpdateTask:
    def test_update_task(self, task_dto, task_repository):
        task = CreateTask(task_repository).create_task(dto=task_dto)

        task_dto.title = "Updated title"
        task_dto.status = TaskStatus.DONE

        updated_task = UpdateTask(task_repository).update_task(
            id=task.id, dto=task_dto
        )

        assert isinstance(updated_task, Task)
        assert updated_task.id is not None
        assert updated_task.title == task_dto.title
        assert updated_task.status == task_dto.status

    def test_update_task_with_invalid_id(self, task_dto, task_repository):
        with pytest.raises(InvalidTaskException):
            UpdateTask(task_repository).update_task(id=None, dto=task_dto)

    def test_update_task_not_found(self, task_dto, task_repository):
        with pytest.raises(TaskNotFoundException):
            UpdateTask(task_repository).update_task(
                id=str(uuid.uuid4()), dto=task_dto
            )
