from pydantic import BaseModel

from todo.domain.entities.enums import TaskStatus


class CreateUpdateTaskDto(BaseModel):
    title: str
    description: str
    status: TaskStatus
