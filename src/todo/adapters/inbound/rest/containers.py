from dependency_injector import containers, providers

from todo.adapters.outbound.db.database import Database
from todo.adapters.outbound.db.task_repository import TaskRepository
from todo.domain.ports.inbound.task.port import (
    CreateTaskInterface,
    UpdateTaskInterface,
)
from todo.domain.ports.outbound.repository.port import TaskRepositoryInterface
from todo.domain.use_cases.create_task import CreateTask
from todo.domain.use_cases.update_task import UpdateTask
from todo.settings import settings


class Adapters(containers.DeclarativeContainer):
    db = providers.Singleton(Database, db_url=settings.DB_URL)
    task_repository: TaskRepositoryInterface = providers.Factory(
        TaskRepository,
        session_factory=db.provided.session,
    )


class TestAdapters(containers.DeclarativeContainer):
    db = providers.Singleton(Database, db_url="sqlite:///:memory:")
    task_repository: TaskRepositoryInterface = providers.Factory(
        TaskRepository,
        session_factory=db.provided.session,
    )


class UseCases(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    create_task: CreateTaskInterface = providers.Factory(
        CreateTask,
        task_repository=adapters.task_repository,
    )
    update_task: UpdateTaskInterface = providers.Factory(
        UpdateTask,
        task_repository=adapters.task_repository,
    )


def get_adapter():
    import os

    if os.getenv("ENVIRONMENT") == "TEST":
        return TestAdapters()
    return Adapters()
