from typing import Dict, List
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from sqlmodel import Session, select
from models.task import Task


class UpdateTaskInput(BaseModel):
    """Input for updating a task."""
    task_id: str = Field(..., description="ID of the task to update")
    title: str = Field("", description="New title of the task (optional)")
    description: str = Field("", description="New description of the task (optional)")
    completed: bool = Field(None, description="New completion status (optional)")
    user_id: str = Field(..., description="ID of the user")


class UpdateTaskTool(BaseTool):
    name: str = "update_task"
    description: str = "Update an existing task"
    args_schema: type = UpdateTaskInput

    def __init__(self, db_session: Session):
        super().__init__()
        self.db_session = db_session

    def _run(self, task_id: str, user_id: str, title: str = "", description: str = "", completed: bool = None) -> str:
        """Run the tool synchronously."""
        try:
            # Find the task
            task = self.db_session.exec(
                select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
            ).first()

            if not task:
                return f"Task with ID {task_id} not found or doesn't belong to user."

            # Update task fields if provided
            if title:
                task.title = title
            if description is not None:
                task.description = description
            if completed is not None:
                task.completed = completed

            self.db_session.add(task)
            self.db_session.commit()

            return f"Task '{task.title}' updated successfully."
        except Exception as e:
            return f"Error updating task: {str(e)}"

    async def _arun(self, task_id: str, user_id: str, title: str = "", description: str = "", completed: bool = None) -> str:
        """Asynchronously run the tool."""
        return self._run(task_id, user_id, title, description, completed)