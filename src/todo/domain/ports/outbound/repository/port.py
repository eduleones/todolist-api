from typing import List, NoReturn, Protocol
from uuid import UUID

from todo.domain.entities.task import Task


class TaskRepositoryInterface(Protocol):
    def find_all(self) -> List[Task]:
        ...

    def find_by_id(self, id: UUID) -> Task:
        ...

    def create(self, task: Task) -> NoReturn:
        ...

    def update(self, id: UUID, task: Task) -> NoReturn:
        ...

    def delete(self, id: UUID, task: Task) -> NoReturn:
        ...
