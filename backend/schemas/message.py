from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageBase(BaseModel):
    conversation_id: str
    role: str
    content: str

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    content: Optional[str] = None

class MessageResponse(MessageBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True