from fastapi import FastAPI

from todo.adapters.inbound.rest.settings import settings
from todo.adapters.inbound.rest.v1.controllers.healthcheck import (
    router as healthcheck_router,
)


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.todo,
    )
    application.include_router(healthcheck_router)

    return application


app = get_application()
