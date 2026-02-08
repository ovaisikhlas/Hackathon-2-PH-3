from sqlmodel import create_engine, Session
from models import User, Task, Conversation, Message  # Import models for table creation
from core.config import settings
import logging

# Create database engine
engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    from sqlmodel import SQLModel
    try:
        # Create all tables (only create, don't drop for persistence)
        SQLModel.metadata.create_all(engine)
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Error creating database tables: {e}")
        raise

def get_session():
    with Session(engine) as session:
        yield session