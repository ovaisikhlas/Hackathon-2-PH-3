from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class TaskBase(SQLModel):
    title: str
    description: str = ""
    completed: bool = False
    user_id: str
    category: Optional[str] = None


class Task(TaskBase, table=True):
    id: str = Field(default_factory=generate_uuid, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
