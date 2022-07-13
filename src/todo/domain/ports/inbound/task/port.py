from typing import Protocol
from uuid import UUID

from todo.domain.entities.task import Task

from .dtos import CreateUpdateTaskDto


class CreateTaskInterface(Protocol):
    def create_task(
        self,
        dto: CreateUpdateTaskDto,
    ) -> Task:
        ...


class UpdateTaskInterface(Protocol):
    def update_task(
        self,
        task_id: UUID,
        dto: CreateUpdateTaskDto,
    ) -> Task:
        ...
