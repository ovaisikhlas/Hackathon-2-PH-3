from typing import Dict, List, TYPE_CHECKING
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from sqlmodel import Session, select
from models.task import Task
import uuid


class AddTaskInput(BaseModel):
    """Input for adding a task."""
    title: str = Field(..., description="Title of the task")
    description: str = Field("", description="Description of the task")
    user_id: str = Field(..., description="ID of the user")


class AddTaskTool(BaseTool):
    name: str = "add_task"
    description: str = "Add a new task for a user"
    args_schema: type = AddTaskInput

    def __init__(self, db_session: Session):
        super().__init__()
        self.db_session = db_session

    def _run(self, title: str, description: str = "", user_id: str = "") -> str:
        """Run the tool synchronously."""
        try:
            # Create new task
            task = Task(
                title=title,
                description=description,
                user_id=user_id,
                completed=False
            )

            self.db_session.add(task)
            self.db_session.commit()
            self.db_session.refresh(task)

            return f"Task '{title}' added successfully with ID: {task.id}"
        except Exception as e:
            return f"Error adding task: {str(e)}"

    async def _arun(self, title: str, description: str = "", user_id: str = "") -> str:
        """Asynchronously run the tool."""
        return self._run(title, description, user_id)