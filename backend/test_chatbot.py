import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_chatbot():
    print("Testing the AI Chatbot functionality...")
    
    # Step 1: Register a test user
    print("\n1. Creating a test user...")
    import uuid
    unique_email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
    user_data = {
        "email": unique_email,
        "name": "Test User",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/sign-up", json=user_data)
        if response.status_code == 200:
            user_info = response.json()
            print(f"[SUCCESS] User created successfully: {user_info}")
            user_id = user_info['id']
        else:
            print(f"[ERROR] Failed to create user: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Error creating user: {e}")
        return False

    # Step 2: Sign in to get authentication token
    print("\n2. Signing in to get authentication token...")
    login_data = {
        "email": unique_email,  # Use the same unique email
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/sign-in/credentials", json=login_data)
        if response.status_code == 200:
            auth_result = response.json()
            print(f"[SUCCESS] Signed in successfully")
            token = auth_result['access_token']
            print(f"[SUCCESS] Got token: {token[:20]}...")
        else:
            print(f"[ERROR] Failed to sign in: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Error signing in: {e}")
        return False

    # Step 3: Test the chatbot endpoint
    print("\n3. Testing the chatbot endpoint...")
    
    # Headers with the authentication token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    # Test message
    chat_data = {
        "message": "Hello, can you help me add a task?",
        "conversation_id": None
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/{user_id}/chat", headers=headers, json=chat_data)
        if response.status_code == 200:
            chat_result = response.json()
            print(f"[SUCCESS] Chat response received:")
            print(f"  Response: {chat_result['response']}")
            print(f"  Conversation ID: {chat_result['conversation_id']}")
            
            # Test a second message in the same conversation
            print("\n4. Testing second message in same conversation...")
            chat_data2 = {
                "message": "Add a task called 'Buy groceries'",
                "conversation_id": chat_result['conversation_id']
            }
            
            response2 = requests.post(f"{BASE_URL}/api/{user_id}/chat", headers=headers, json=chat_data2)
            if response2.status_code == 200:
                chat_result2 = response2.json()
                print(f"[SUCCESS] Second chat response received:")
                print(f"  Response: {chat_result2['response']}")
                print(f"  Conversation ID: {chat_result2['conversation_id']}")
            else:
                print(f"[ERROR] Failed second chat request: {response2.status_code} - {response2.text}")
                
        else:
            print(f"[ERROR] Failed chat request: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Error testing chat: {e}")
        return False

    print("\n[SUCCESS] Chatbot test completed successfully!")
    return True

if __name__ == "__main__":
    test_chatbot()