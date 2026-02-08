from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
import logging
from pydantic import BaseModel
from database.database import get_session
from core.auth import get_current_user
from models.user import User
from models.conversation import Conversation
from models.message import Message
from schemas.conversation import ConversationCreate

router = APIRouter(tags=["chat"])

logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    response: str
    conversation_id: str

@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat_mock(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    """
    Mock chat endpoint that simulates AI responses without requiring external API
    """
    # Verify the user_id in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    # Retrieve or create conversation
    conversation = None
    if request.conversation_id:
        conversation = db.exec(
            select(Conversation).where(Conversation.id == request.conversation_id)
            .where(Conversation.user_id == user_id)
        ).first()

        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found or access denied")
    else:
        # Create new conversation
        conversation_data = ConversationCreate(user_id=user_id)
        conversation = Conversation.model_validate(conversation_data)
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message
    )
    db.add(user_message)
    db.commit()

    # Simulate AI response based on user message
    user_msg_lower = request.message.lower()
    
    if "hello" in user_msg_lower or "hi" in user_msg_lower:
        ai_response = "Hello! I'm your AI assistant. How can I help you with your tasks today?"
    elif "task" in user_msg_lower and ("add" in user_msg_lower or "create" in user_msg_lower):
        ai_response = "I can help you add a task. Please provide the task title and description."
    elif "list" in user_msg_lower or "show" in user_msg_lower:
        ai_response = "I can help you list your tasks. You have 2 active tasks: 'Sample Task 1' and 'Sample Task 2'."
    elif "complete" in user_msg_lower or "done" in user_msg_lower:
        ai_response = "I can help you mark a task as complete. Which task would you like to mark as done?"
    elif "delete" in user_msg_lower:
        ai_response = "I can help you delete a task. Which task would you like to delete?"
    elif "update" in user_msg_lower:
        ai_response = "I can help you update a task. Which task would you like to update?"
    else:
        ai_response = f"I understand you said: '{request.message}'. I'm your AI assistant and can help you manage your tasks. You can ask me to add, list, update, or complete tasks."

    # Save AI response
    ai_message = Message(
        conversation_id=conversation.id,
        role="assistant",
        content=ai_response
    )
    db.add(ai_message)
    db.commit()

    return ChatResponse(
        response=ai_response,
        conversation_id=conversation.id
    )