from todo.domain.entities.task import Task
from todo.domain.use_cases.create_task import CreateTask


class TestCreateTask:
    def test_create_task(self, task_dto, task_repository):
        task = CreateTask(task_repository).create_task(dto=task_dto)

        assert isinstance(task, Task)
        assert task.id is not None
