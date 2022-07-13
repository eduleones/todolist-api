from todo.domain.entities.task import Task
from todo.domain.ports.inbound.task.dtos import CreateUpdateTaskDto


class CreateTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def create_task(self, dto: CreateUpdateTaskDto) -> Task:
        task = Task(
            title=dto.title,
            description=dto.description,
            status=dto.status,
        )
        self.task_repository.create(task)
        return task
