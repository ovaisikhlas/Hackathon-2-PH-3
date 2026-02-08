from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class User(SQLModel, table=True):
    __tablename__ = "user"
    id: str = Field(default_factory=generate_uuid, primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str = Field(default="")
    hashed_password: str = Field(default="")
