from contextlib import AbstractContextManager
from typing import Callable, List, NoReturn
from uuid import UUID

from sqlmodel import Session

from todo.adapters.outbound.db.models import TaskDB
from todo.domain.entities.task import Task
from todo.domain.ports.outbound.repository.exceptions import TaskNotFoundError


class TaskRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def _build_task_to_db(self, task: Task) -> TaskDB:
        return TaskDB(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=task.created_at,
            updated_at=task.updated_at,
        )

    def _build_db_to_task(self, task_db: TaskDB) -> Task:
        return Task(
            id=task_db.id,
            title=task_db.title,
            description=task_db.description,
            status=task_db.status,
            created_at=task_db.created_at,
            updated_at=task_db.updated_at,
        )

    def find_all(self) -> List[Task]:
        with self.session_factory() as session:
            tasks_db = session.query(TaskDB).all()
            return [self._build_db_to_task(task_db) for task_db in tasks_db]

    def find_by_id(self, id: UUID) -> Task:
        with self.session_factory() as session:
            task_db = session.query(TaskDB).filter(TaskDB.id == id).first()
            if not task_db:
                raise TaskNotFoundError(id)
            return self._build_db_to_task(task_db)

    def create(self, task: Task) -> NoReturn:
        with self.session_factory() as session:
            task_db = self._build_task_to_db(task)
            session.add(task_db)
            session.commit()

    def update(self, id: UUID, task: Task) -> NoReturn:
        with self.session_factory() as session:
            session.query(TaskDB).filter(TaskDB.id == id).update(
                {
                    "title": task.title,
                    "description": task.description,
                    "status": task.status,
                }
            )
            session.commit()

    def delete(self, id: UUID, task: Task) -> NoReturn:
        with self.session_factory() as session:
            session.query(TaskDB).filter(TaskDB.id == id).delete()
            session.commit()
