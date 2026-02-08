from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class MessageBase(SQLModel):
    conversation_id: str
    role: str  # 'user' or 'assistant'
    content: str


class Message(MessageBase, table=True):
    id: str = Field(default_factory=generate_uuid, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)