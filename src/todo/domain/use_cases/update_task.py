from uuid import UUID

from todo.domain.entities.task import Task
from todo.domain.exceptions.task_exceptions import (
    InvalidTaskException,
    TaskNotFoundException,
)
from todo.domain.ports.inbound.task.dtos import CreateUpdateTaskDto
from todo.domain.ports.outbound.repository.exceptions import TaskNotFoundError


class UpdateTask:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def _validate_task_by_id(self, id: UUID):
        if not id:
            raise InvalidTaskException("Task is required")

        try:
            self.task_repository.find_by_id(id)
        except TaskNotFoundError:
            raise TaskNotFoundException("Task not found")

    def update_task(self, id: UUID, dto: CreateUpdateTaskDto) -> Task:
        self._validate_task_by_id(id)

        updated_task = Task(
            title=dto.title,
            description=dto.description,
            status=dto.status,
        )
        self.task_repository.update(id, updated_task)
        return updated_task
