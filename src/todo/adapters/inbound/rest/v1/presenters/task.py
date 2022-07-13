from pydantic import BaseModel

from todo.domain.entities.task import Task


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    status: str
    created_at: str
    updated_at: str

    @classmethod
    def from_entity(cls, task: "Task") -> "TaskResponse":
        return cls(
            id=str(task.id),
            title=task.title,
            description=task.description,
            status=task.status.value,
            created_at=task.created_at.isoformat(),
            updated_at=task.updated_at.isoformat(),
        )

    @classmethod
    def from_entities(cls, tasks: "Task") -> "TaskResponse":
        return [cls.from_entity(task) for task in tasks]
