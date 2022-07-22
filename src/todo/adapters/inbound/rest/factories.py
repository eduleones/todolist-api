from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from todo.adapters.inbound.rest.containers import Adapters, UseCases
from todo.adapters.inbound.rest.v1.controllers.healthcheck import (
    router as healthcheck_router,
)
from todo.adapters.inbound.rest.v1.controllers.task import (
    router as task_router,
)
from todo.settings import settings


def get_application(container: DeclarativeContainer = None) -> FastAPI:
    if container is None:
        container = UseCases(adapters=Adapters())

    container.wire(modules=["todo.adapters.inbound.rest.v1.controllers.task"])

    db = container.adapters.db()
    db.create_database()

    application = FastAPI(
        title=settings.PROJECT_NAME,
    )
    application.container = container
    application.include_router(healthcheck_router)
    application.include_router(task_router)

    return application
