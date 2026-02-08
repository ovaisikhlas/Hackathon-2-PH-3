from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    category: Optional[str] = None


class TaskCreate(TaskBase):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    category: Optional[str] = None


class TaskResponse(TaskBase):
    id: str  # Changed from int to str to match the UUID in the model
    user_id: str  # Changed from int to str to match Better Auth
    created_at: datetime
    updated_at: datetime


class TaskToggleComplete(BaseModel):
    completed: bool