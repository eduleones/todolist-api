from fastapi import FastAPI

from todo.adapters.inbound.rest.containers import UseCases, get_adapter
from todo.adapters.inbound.rest.v1.controllers.healthcheck import (
    router as healthcheck_router,
)
from todo.adapters.inbound.rest.v1.controllers.task import (
    router as task_router,
)
from todo.settings import settings


def get_application() -> FastAPI:
    adapter_container = get_adapter()
    container = UseCases(adapters=adapter_container)
    container.wire(modules=["todo.adapters.inbound.rest.v1.controllers.task"])

    db = adapter_container.db()
    db.create_database()

    application = FastAPI(
        title=settings.PROJECT_NAME,
    )
    application.container = container
    application.include_router(healthcheck_router)
    application.include_router(task_router)

    return application


app = get_application()
