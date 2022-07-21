from dependency_injector import containers, providers

from todo.adapters.outbound.db.database import Database
from todo.adapters.outbound.db.task_repository import TaskRepository
from todo.domain.ports.outbound.repository.port import TaskRepositoryInterface


class Adapters(containers.DeclarativeContainer):
    db = providers.Singleton(Database, db_url="sqlite:///:memory:")
    task_repository: TaskRepositoryInterface = providers.Factory(
        TaskRepository,
        session_factory=db.provided.session,
    )
