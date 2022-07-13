from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy_utils import UUIDType
from sqlmodel import Column, Field, SQLModel

from todo.domain.entities.enums import TaskStatus


class TaskDB(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4, sa_column=Column(UUIDType(), primary_key=True)
    )
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
