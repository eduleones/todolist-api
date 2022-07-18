from http import HTTPStatus
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from todo.adapters.inbound.rest.containers import UseCases
from todo.adapters.inbound.rest.v1.presenters.task import TaskResponse
from todo.domain.ports.inbound.task.dtos import CreateUpdateTaskDto

router = APIRouter()


@router.post(
    "/v1/tasks",
    status_code=HTTPStatus.CREATED,
    response_model=TaskResponse,
)
@inject
async def create_task(
    task_in: CreateUpdateTaskDto,
    use_case=Depends(Provide[UseCases.create_task]),
):
    task = use_case.create_task(task_in)
    return TaskResponse.from_entity(task)


@router.put(
    "/v1/tasks/{task_id}",
    status_code=HTTPStatus.OK,
    response_model=TaskResponse,
)
@inject
async def update_task(
    task_id: UUID,
    task_dto: CreateUpdateTaskDto,
    use_case=Depends(Provide[UseCases.update_task]),
):
    task = use_case.update_task(task_id, task_dto)
    return TaskResponse.from_entity(task)
