from typing import Dict, List
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from sqlmodel import Session, select
from models.task import Task


class ListTasksInput(BaseModel):
    """Input for listing tasks."""
    user_id: str = Field(..., description="ID of the user")


class ListTasksTool(BaseTool):
    name: str = "list_tasks"
    description: str = "List all tasks for a user"
    args_schema: type = ListTasksInput

    def __init__(self, db_session: Session):
        super().__init__()
        self.db_session = db_session

    def _run(self, user_id: str) -> str:
        """Run the tool synchronously."""
        try:
            # Query tasks for the user
            tasks = self.db_session.exec(
                select(Task).where(Task.user_id == user_id)
            ).all()

            if not tasks:
                return "No tasks found for this user."

            task_list = []
            for task in tasks:
                status = "completed" if task.completed else "pending"
                task_list.append(f"- {task.title} ({status})")

            return "Tasks:\n" + "\n".join(task_list)
        except Exception as e:
            return f"Error listing tasks: {str(e)}"

    async def _arun(self, user_id: str) -> str:
        """Asynchronously run the tool."""
        return self._run(user_id)