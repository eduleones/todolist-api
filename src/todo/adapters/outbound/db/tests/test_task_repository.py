import uuid

import pytest

from todo.domain.ports.outbound.repository.exceptions import TaskNotFoundError


class TestTaskRepository:
    def test_create_task(self, task_repository, task):
        task_repository.create(task)

        assert task_repository.find_by_id(task.id) == task

    def test_update_task(self, task_repository, task):
        task_repository.create(task)
        task.title = "Updated title"
        task_repository.update(task.id, task)

        assert task_repository.find_by_id(task.id) == task

    def test_find_all_tasks(self, task_repository, task):
        task_repository.create(task)

        tasks = task_repository.find_all()
        assert task in tasks

    def test_delete_task(self, task_repository, task):
        task_repository.create(task)
        task_repository.delete(task.id, task)

        tasks = task_repository.find_all()
        assert task not in tasks

    def test_find_by_id_task(self, task_repository, task):
        task_repository.create(task)

        assert task_repository.find_by_id(task.id) == task

    def test_find_by_id_task_not_found(self, task_repository):
        with pytest.raises(TaskNotFoundError):
            task_repository.find_by_id(str(uuid.uuid4()))
