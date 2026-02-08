#!/usr/bin/env python3
"""
Debug script to test the database and task creation functionality
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlmodel import Session, select
from database.database import engine, get_session
from models.task import Task, TaskBase
from models.user import User
from core.auth import get_current_user
from api.tasks import create_task
from fastapi import Depends
import uuid

def test_database_connection():
    """Test basic database connectivity"""
    print("Testing database connection...")
    
    try:
        # Create a session
        with Session(engine) as session:
            print("[OK] Database connection successful")
            
            # Check if users exist
            users = session.exec(select(User)).all()
            print(f"Found {len(users)} users in database")
            
            if users:
                for user in users:
                    print(f"  - User ID: {user.id}, Email: {user.email}")
                    
                # Test creating a task for the first user
                test_user = users[0]  # Use the first user
                print(f"\nTesting task creation for user: {test_user.email}")
                
                # Create a test task directly
                test_task = Task(
                    title="Test Task from Debug Script",
                    description="This is a test task created by the debug script",
                    completed=False,
                    user_id=test_user.id,
                    category="debug"
                )
                
                session.add(test_task)
                session.commit()
                session.refresh(test_task)
                
                print(f"[OK] Task created successfully with ID: {test_task.id}")
                
                # Query the task back
                retrieved_task = session.get(Task, test_task.id)
                if retrieved_task:
                    print(f"[OK] Task retrieved successfully: {retrieved_task.title}")
                else:
                    print("[ERROR] Failed to retrieve the task")
                    
    except Exception as e:
        print(f"[ERROR] Error connecting to database: {e}")
        import traceback
        traceback.print_exc()

def test_table_creation():
    """Test if tables are created properly"""
    print("\nTesting table creation...")
    try:
        from database.database import create_db_and_tables
        create_db_and_tables()
        print("[OK] Tables created successfully")
    except Exception as e:
        print(f"[ERROR] Error creating tables: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=== Database Debug Script ===")
    
    # First, test table creation
    test_table_creation()
    
    # Then test database operations
    test_database_connection()
    
    print("\n=== Debug Complete ===")