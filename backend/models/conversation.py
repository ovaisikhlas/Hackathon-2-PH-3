from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class ConversationBase(SQLModel):
    user_id: str
    title: Optional[str] = None


class Conversation(ConversationBase, table=True):
    id: str = Field(default_factory=generate_uuid, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)