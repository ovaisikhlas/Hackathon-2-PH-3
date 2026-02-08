import requests
import json

BASE_URL = "http://localhost:8000"

def test_basic_functionality():
    print("Testing basic backend functionality...\n")
    
    # Test root endpoint
    print("1. Testing root endpoint:")
    response = requests.get(f"{BASE_URL}/")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}\n")
    
    # Test registering a user
    print("2. Testing user registration:")
    register_payload = {
        "email": "test_user@example.com",
        "name": "Test User",
        "password": "securepassword123"
    }
    response = requests.post(f"{BASE_URL}/api/auth/sign-up", json=register_payload)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(f"   Response: {user_data}")
    elif response.status_code == 409:
        print("   User already exists (this is OK)")
        # Use a known user ID for testing
        user_id = "df61726c-0e04-4dfd-be7a-50287fb1ba91"  # From previous test
    else:
        print(f"   Error: {response.text}")
        return
    
    # Test logging in
    print("\n3. Testing user login:")
    login_payload = {
        "email": "test_user@example.com",
        "password": "securepassword123"
    }
    response = requests.post(f"{BASE_URL}/api/auth/sign-in/credentials", json=login_payload)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        print(f"   Token received (first 30 chars): {access_token[:30]}...")
        headers = {"Authorization": f"Bearer {access_token}"}
    else:
        # Try with the fallback user
        login_payload = {
            "email": "test@example.com",
            "password": "password123"
        }
        response = requests.post(f"{BASE_URL}/api/auth/sign-in/credentials", json=login_payload)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data['access_token']
            print(f"   Token received (first 30 chars): {access_token[:30]}...")
            headers = {"Authorization": f"Bearer {access_token}"}
            user_id = "b0a24f19-63f8-4b47-9bf8-99d567144748"  # Original test user ID
        else:
            print(f"   Error: {response.text}")
            return
    
    # Test getting tasks (should be empty initially)
    print(f"\n4. Testing get tasks for user {user_id}:")
    response = requests.get(f"{BASE_URL}/api/{user_id}/tasks", headers=headers)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        tasks = response.json()
        print(f"   Tasks: {len(tasks)} found")
    else:
        print(f"   Error: {response.text}")
    
    # Test creating a task
    print(f"\n5. Testing create task for user {user_id}:")
    task_payload = {
        "title": "Test Task from Verification Script",
        "description": "This is a test task created during backend verification",
        "completed": False,
        "category": "testing"
    }
    response = requests.post(f"{BASE_URL}/api/{user_id}/tasks", json=task_payload, headers=headers)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        task_data = response.json()
        task_id = task_data['id']
        print(f"   Created task with ID: {task_id}")
        print(f"   Task: {task_data['title']}")
    else:
        print(f"   Error: {response.text}")
        # Print server error details if available
        try:
            error_detail = response.json()
            print(f"   Error details: {error_detail}")
        except:
            print(f"   Raw error response: {response.text}")
    
    print(f"\nBackend endpoints verification complete!")

if __name__ == "__main__":
    test_basic_functionality()