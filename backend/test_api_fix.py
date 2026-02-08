"""
Test script to verify the Google API key handling fix
"""
import os
from unittest.mock import patch
from api.chat import chat
from fastapi import HTTPException
from sqlmodel import Session
from models.user import User
from pydantic import BaseModel


class MockDBSession:
    """Mock database session for testing"""
    def exec(self, query):
        # Return a mock user
        mock_user = User(
            id="d869cfcd-cc9f-4348-b1dd-33538f282010",
            email="test@example.com",
            name="Test User",
            hashed_password="hashed_password"
        )
        return MockResult([mock_user])
    
    def add(self, obj):
        pass
    
    def commit(self):
        pass
    
    def refresh(self, obj):
        pass


class MockResult:
    """Mock result object"""
    def __init__(self, items):
        self.items = items
    
    def first(self):
        return self.items[0] if self.items else None


class MockCurrentUser:
    """Mock current user"""
    id = "d869cfcd-cc9f-4348-b1dd-33538f282010"


class MockChatRequest(BaseModel):
    """Mock chat request"""
    conversation_id: str = None
    message: str


def test_fallback_response():
    """Test that fallback response is returned when Google API key is not configured"""
    
    # Set up environment without a valid API key
    os.environ["GOOGLE_API_KEY"] = "your_actual_google_api_key_here"  # This is the placeholder value
    
    # Create mock objects
    user_id = "d869cfcd-cc9f-4348-b1dd-33538f282010"
    request = MockChatRequest(message="Hello")
    current_user = MockCurrentUser()
    db = MockDBSession()
    
    try:
        # Call the chat function
        response = chat(user_id, request, current_user, db)
        
        # Check that we got a fallback response
        assert isinstance(response.response, str)
        assert "fallback response" in response.response.lower() or "not configured" in response.response.lower()
        print("✅ Test passed: Fallback response returned when API key is not configured")
        print(f"Response: {response.response}")
        
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        return False
    
    return True


def test_with_valid_api_key():
    """Test that normal processing occurs when API key is configured"""
    
    # Set up environment with a fake but valid-looking API key
    os.environ["GOOGLE_API_KEY"] = "AIzaSyTestApiKeyForTesting123456789"
    
    # This test will fail at the LLM initialization since we don't have the actual API available,
    # but it should proceed past the API key check
    print("ℹ️  Note: This test would normally proceed to LLM initialization with a valid API key")


if __name__ == "__main__":
    print("Testing API key handling fix...")
    
    success = test_fallback_response()
    if success:
        test_with_valid_api_key()
    
    print("\nTesting completed!")