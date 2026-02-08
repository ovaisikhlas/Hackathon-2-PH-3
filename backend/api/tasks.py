import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select
from database.database import get_session
from models.task import Task, TaskBase
from schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskToggleComplete
from core.auth import get_current_user
from models.user import User
import logging

router = APIRouter()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@router.get("/tasks", response_model=List[TaskResponse])
def read_tasks(
    user_id: str,  # Changed from int to str
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access these tasks"
        )

    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    return tasks


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,  # Changed from int to str
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    logger.debug(f"Creating task for user_id: {user_id}")
    logger.debug(f"Current user ID: {current_user.id}")
    logger.debug(f"Task data: {task}")
    
    if current_user.id != user_id:
        logger.error(f"User ID mismatch: current_user.id={current_user.id}, path user_id={user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create tasks for this user"
        )

    try:
        # Fixed task creation - using model_validate instead of from_orm
        db_task = Task(
            title=task.title,
            description=task.description,
            completed=task.completed,
            user_id=user_id,
            category=task.category
        )
        logger.debug(f"Created task object: {db_task}")
        
        session.add(db_task)
        logger.debug("Added task to session")
        
        session.commit()
        logger.debug("Committed session")
        
        session.refresh(db_task)
        logger.debug(f"Refreshed task: {db_task}")
        
        return db_task
    except Exception as e:
        logger.error(f"Error creating task: {str(e)}", exc_info=True)
        raise


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(
    user_id: str,  # Changed from int to str
    task_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )

    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    user_id: str,  # Changed from int to str
    task_id: str,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    db_task = session.get(Task, task_id)
    if not db_task or db_task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Update only provided fields
    for field, value in task_update.model_dump(exclude_unset=True).items():
        setattr(db_task, field, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: str,  # Changed from int to str
    task_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )

    db_task = session.get(Task, task_id)
    if not db_task or db_task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    session.delete(db_task)
    session.commit()
    return


@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
def toggle_task_complete(
    user_id: str,  # Changed from int to str
    task_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    db_task = session.get(Task, task_id)
    if not db_task or db_task.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Toggle the completed status
    db_task.completed = not db_task.completed
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task
