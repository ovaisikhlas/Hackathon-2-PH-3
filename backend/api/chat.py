from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
import logging
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from database.database import get_session
from core.auth import get_current_user
from models.user import User
from models.conversation import Conversation
from models.message import Message

router = APIRouter(tags=["chat"])

logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    response: str
    conversation_id: str

@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    """
    Simplified chat endpoint that just returns a response from Gemini
    """
    print("\n=== CHAT REQUEST ===")
    print(f"User ID: {user_id}")
    print(f"Message: {request.message}")

    # Security check
    if current_user.id != user_id:
        print("Access denied")
        raise HTTPException(status_code=403, detail="Access denied")

    # Get or create conversation
    conversation = None
    if request.conversation_id:
        conversation = db.exec(
            select(Conversation)
            .where(Conversation.id == request.conversation_id)
            .where(Conversation.user_id == user_id)
        ).first()
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = Conversation(user_id=user_id)
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    print(f"Conversation ID: {conversation.id}")

    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message
    )
    db.add(user_message)
    db.commit()

    # Load API key
    google_api_key = os.getenv("GOOGLE_API_KEY")
    print(f"API Key loaded: {'YES' if google_api_key else 'NO'}")

    if not google_api_key:
        ai_response = "AI service not available (missing API key)."
    else:
        try:
            # Initialize LLM with working model
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=google_api_key,
                temperature=0.7,
                max_output_tokens=500,
            )
            print("LLM initialized successfully")

            # Create a simple prompt
            prompt = f"You are a helpful assistant. User message: {request.message}. Respond in a friendly way."
            message = HumanMessage(content=prompt)
            
            # Get response from Gemini
            response = llm.invoke([message])
            ai_response = response.content
            print(f"AI Response: {ai_response}")
            
        except Exception as e:
            print(f"Error calling Gemini: {str(e)}")
            ai_response = f"Sorry, I encountered an error: {str(e)}"

    # Save AI response
    ai_message = Message(
        conversation_id=conversation.id,
        role="assistant",
        content=ai_response
    )
    db.add(ai_message)
    db.commit()

    return ChatResponse(response=ai_response, conversation_id=str(conversation.id))