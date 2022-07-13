from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from todo.domain.entities.enums import TaskStatus


class Task(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
