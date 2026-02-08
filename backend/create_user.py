#!/usr/bin/env python3
"""
Script to create a user in the database for testing purposes.
"""

from sqlmodel import Session, select
from database.database import engine, create_db_and_tables
from models.user import User
from passlib.context import CryptContext
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize password context (same as in auth.py)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")

def get_password_hash(password: str) -> str:
    """
    Hash a password with bcrypt, ensuring it's under 72 bytes.
    """
    # Ensure the password is definitely under 72 bytes for bcrypt
    # First, encode to bytes
    password_bytes = password.encode('utf-8')

    # Truncate to exactly 72 bytes if needed
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
        logging.info(f"Password truncated from {len(password.encode('utf-8'))} to {len(password_bytes)} bytes for bcrypt compatibility")

    # Decode back to string, handling any potential issues with incomplete characters
    safe_password = password_bytes.decode('utf-8', errors='ignore')

    # Double-check the length to ensure it's definitely under 72 bytes
    if len(safe_password.encode('utf-8')) > 72:
        # If somehow the decoded string is still too long, truncate by characters
        safe_password = safe_password[:72]
        # And double-check the byte length again
        safe_bytes = safe_password.encode('utf-8')[:72]
        safe_password = safe_bytes.decode('utf-8', errors='ignore')

    try:
        hashed = pwd_context.hash(safe_password)
        logging.info(f"Password hashed successfully")
        return hashed
    except ValueError as ve:
        # If we still get the bcrypt error, log it and raise
        logging.error(f"Bcrypt error despite truncation: {ve}")
        raise
    except Exception as e:
        logging.error(f"Error during password hashing: {e}")
        raise

def create_user(email: str, name: str, password: str):
    # Create tables if they don't exist
    create_db_and_tables()
    
    # Create a session
    with Session(engine) as session:
        # Check if user already exists
        statement = select(User).where(User.email == email)
        result = session.exec(statement)
        existing_user = result.first()
        
        if existing_user:
            print(f"User with email {email} already exists!")
            print(f"ID: {existing_user.id}")
            print(f"Name: {existing_user.name}")
            return existing_user
        
        # Create new user
        hashed_password = get_password_hash(password)
        user = User(
            email=email,
            name=name,
            hashed_password=hashed_password
        )
        
        session.add(user)
        session.commit()
        session.refresh(user)
        
        print(f"User created successfully!")
        print(f"ID: {user.id}")
        print(f"Email: {user.email}")
        print(f"Name: {user.name}")
        
        return user

if __name__ == "__main__":
    # Create the 'aiman@gmail.com' user for testing
    create_user(
        email="aiman@gmail.com",
        name="Aiman",
        password="password123"  # Use a secure password in production
    )