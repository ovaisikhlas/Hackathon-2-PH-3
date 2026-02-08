from typing import Dict, List
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from sqlmodel import Session, select, delete
from models.task import Task


class DeleteTaskInput(BaseModel):
    """Input for deleting a task."""
    task_id: str = Field(..., description="ID of the task to delete")
    user_id: str = Field(..., description="ID of the user")


class DeleteTaskTool(BaseTool):
    name: str = "delete_task"
    description: str = "Delete a task"
    args_schema: type = DeleteTaskInput

    def __init__(self, db_session: Session):
        super().__init__()
        self.db_session = db_session

    def _run(self, task_id: str, user_id: str) -> str:
        """Run the tool synchronously."""
        try:
            # Find the task
            task = self.db_session.exec(
                select(Task).where(Task.id == task_id).where(Task.user_id == user_id)
            ).first()

            if not task:
                return f"Task with ID {task_id} not found or doesn't belong to user."

            # Delete the task
            self.db_session.delete(task)
            self.db_session.commit()

            return f"Task '{task.title}' deleted successfully."
        except Exception as e:
            return f"Error deleting task: {str(e)}"

    async def _arun(self, task_id: str, user_id: str) -> str:
        """Asynchronously run the tool."""
        return self._run(task_id, user_id)