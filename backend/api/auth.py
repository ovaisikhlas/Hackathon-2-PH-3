from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from datetime import timedelta
from sqlmodel import Session, select
from models.user import User
from core.auth import create_access_token, get_current_user
from database.database import get_session
from core.config import settings
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# Request/response models
class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str

    class Config:
        from_attributes = True  # Enable ORM mode

class Token(BaseModel):
    access_token: str
    token_type: str

class SignInRequest(BaseModel):
    email: str
    password: str

# Password hashing utility (using passlib)
from passlib.context import CryptContext
import logging

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        result = pwd_context.verify(plain_password, hashed_password)
        logging.info(f"Password verification result: {result}")
        return result
    except Exception as e:
        logging.error(f"Error during password verification: {e}")
        return False

def get_password_hash(password: str) -> str:
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

import uuid
from datetime import datetime
from sqlalchemy import text

@router.post("/sign-up", response_model=UserResponse)
def sign_up(user_data: UserCreate, session: Session = Depends(get_session)):
    try:
        print(f"Attempting to sign up user with email: {user_data.email}")

        # Check if user already exists using SQLModel select to avoid raw SQL issues
        statement = select(User).where(User.email == user_data.email)
        result = session.exec(statement)
        existing_user = result.first()

        if existing_user:
            print(f"User with email {user_data.email} already exists")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists"
            )

        print(f"Creating new user with email: {user_data.email}")

        # Hash the password
        hashed_password = get_password_hash(user_data.password)
        print(f"Password hashed successfully")

        # Create new user using SQLModel
        user = User(
            email=user_data.email,
            name=user_data.name,
            hashed_password=hashed_password
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"User created successfully with ID: {user.id}")

        # Return the created user data
        return UserResponse(id=user.id, email=user.email, name=user.name)
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        print(f"Error during sign up: {str(e)}")
        session.rollback()  # Rollback in case of error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )

from sqlalchemy import text

@router.post("/sign-in/credentials", response_model=Token)
def sign_in(user_credentials: SignInRequest, session: Session = Depends(get_session)):
    try:
        print(f"Attempting to sign in user with email: {user_credentials.email}")

        # Find user by email using SQLModel select to avoid raw SQL issues
        statement = select(User).where(User.email == user_credentials.email)
        result = session.exec(statement)
        user = result.first()

        print(f"Looking for user with email: {user_credentials.email}")
        print(f"Found user: {user is not None}")

        if user:
            print(f"User ID: {user.id}")
            print(f"User email: {user.email}")
            print(f"User name: {user.name}")
            print(f"Hashed password in DB (first 30 chars): {user.hashed_password[:30] if user.hashed_password else 'None'}")

        if not user:
            print(f"User with email {user_credentials.email} not found in database")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        print(f"User found, verifying password.")

        # Verify the password
        password_verified = verify_password(user_credentials.password, user.hashed_password)
        print(f"Password verification result: {password_verified}")

        if not password_verified:
            print(f"Password verification failed for user {user_credentials.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        print(f"Sign-in successful for user {user.email}")

        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTP exceptions (like 401) as-is
        raise
    except Exception as e:
        # Log the full error for debugging
        import traceback
        error_details = traceback.format_exc()
        print(f"Sign-in error details: {error_details}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during sign in: {str(e)}"
        )

@router.post("/sign-out")
def sign_out():
    # In a real implementation, you might add the token to a blacklist
    return {"message": "Successfully signed out"}

@router.post("/refresh")
def refresh_token(current_user: User = Depends(get_current_user)):
    # Create a new access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": current_user.id}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}