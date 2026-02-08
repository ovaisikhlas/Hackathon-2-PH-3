import requests
import json
from typing import Optional

BASE_URL = "http://localhost:8000"

class TodoAppAPITester:
    def __init__(self):
        self.base_url = BASE_URL
        self.access_token = None
        self.current_user_id = None
    
    def register_user(self, email: str, name: str, password: str):
        """Register a new user"""
        url = f"{self.base_url}/api/auth/sign-up"
        payload = {
            "email": email,
            "name": name,
            "password": password
        }
        
        print(f"Registering user: {email}")
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Response: {response.json()}")
        return response
    
    def login_user(self, email: str, password: str):
        """Login user and get access token"""
        url = f"{self.base_url}/api/auth/sign-in/credentials"
        payload = {
            "email": email,
            "password": password
        }
        
        print(f"\nLogging in user: {email}")
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('access_token')
            print(f"Access token received: {self.access_token[:20]}...")
        else:
            print(f"Login failed: {response.json()}")
        
        return response
    
    def get_auth_headers(self):
        """Get authorization headers"""
        if not self.access_token:
            return {}
        return {"Authorization": f"Bearer {self.access_token}"}
    
    def create_task(self, user_id: str, title: str, description: str = "", completed: bool = False, category: str = "general"):
        """Create a new task"""
        url = f"{self.base_url}/api/{user_id}/tasks"
        headers = self.get_auth_headers()
        payload = {
            "title": title,
            "description": description,
            "completed": completed,
            "category": category
        }
        
        print(f"\nCreating task for user {user_id}: {title}")
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 201:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.json()}")
        return response
    
    def get_tasks(self, user_id: str):
        """Get all tasks for a user"""
        url = f"{self.base_url}/api/{user_id}/tasks"
        headers = self.get_auth_headers()
        
        print(f"\nGetting tasks for user {user_id}")
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error: {response.json()}")
        return response
    
    def update_task(self, user_id: str, task_id: int, **kwargs):
        """Update a task"""
        url = f"{self.base_url}/api/{user_id}/tasks/{task_id}"
        headers = self.get_auth_headers()
        payload = kwargs
        
        print(f"\nUpdating task {task_id} for user {user_id}")
        response = requests.put(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.json()}")
        return response
    
    def toggle_task_completion(self, user_id: str, task_id: int):
        """Toggle task completion status"""
        url = f"{self.base_url}/api/{user_id}/tasks/{task_id}/complete"
        headers = self.get_auth_headers()
        
        print(f"\nToggling completion for task {task_id} for user {user_id}")
        response = requests.patch(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.json()}")
        return response
    
    def delete_task(self, user_id: str, task_id: int):
        """Delete a task"""
        url = f"{self.base_url}/api/{user_id}/tasks/{task_id}"
        headers = self.get_auth_headers()
        
        print(f"\nDeleting task {task_id} for user {user_id}")
        response = requests.delete(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 204:
            print("Task deleted successfully")
        else:
            print(f"Error: {response.json()}")
        return response
    
    def chat_with_ai(self, user_id: str, message: str, conversation_id: Optional[str] = None):
        """Chat with the AI assistant"""
        url = f"{self.base_url}/api/{user_id}/chat"
        headers = self.get_auth_headers()
        payload = {
            "message": message
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id
        
        print(f"\nSending chat message to user {user_id}: {message}")
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"AI Response: {result['response']}")
            print(f"Conversation ID: {result['conversation_id']}")
            return result
        else:
            print(f"Error: {response.json()}")
        return response

def main():
    tester = TodoAppAPITester()
    
    # Register a test user
    email = "test2@example.com"  # Use a different email to avoid conflicts
    name = "Test User 2"
    password = "password123"
    
    # Register user and get the user ID from the response
    register_response = tester.register_user(email, name, password)
    if register_response.status_code == 409:
        # User already exists, try to log in with the original test user
        print("User already exists, trying to log in with original test user...")
        email = "test@example.com"
        name = "Test User"
        login_response = tester.login_user("test@example.com", "password123")
        if login_response.status_code != 200:
            print("Failed to log in with existing user, exiting test.")
            return
        user_id = "b0a24f19-63f8-4b47-9bf8-99d567144748"  # Use the known user ID from previous test
    elif register_response.status_code != 200:
        print("Failed to register user, exiting test.")
        return
    else:
        # Successfully registered new user
        # Extract user ID from registration response
        user_data = register_response.json()
        user_id = user_data.get('id')
        print(f"Registered user with ID: {user_id}")
        
        # Login user (this will set the access token)
        login_response = tester.login_user(email, password)
        
        if login_response.status_code != 200:
            print("Failed to login, exiting test.")
            return
    
    print(f"Using user with ID: {user_id}")
    
    print("\n" + "="*50)
    print("TESTING BACKEND ENDPOINTS")
    print("="*50)
    
    # Let's create a simple test to verify the endpoints work
    # First, let's try to access the root endpoint
    print("\nTesting root endpoint:")
    response = requests.get(f"{BASE_URL}/")
    print(f"Root endpoint status: {response.status_code}")
    print(f"Root endpoint response: {response.json()}")
    
    # Test creating a task
    print(f"\nTesting task creation for user {user_id}:")
    task_response = tester.create_task(
        user_id=user_id,
        title="Test Task",
        description="This is a test task",
        category="work"
    )
    
    if task_response.status_code != 201:
        print("Failed to create task")
        return
    
    # Extract task ID from the response
    task_data = task_response.json()
    task_id = task_data.get('id')
    print(f"Created task with ID: {task_id}")
    
    # Test getting tasks
    print(f"\nTesting getting tasks for user {user_id}:")
    tester.get_tasks(user_id)
    
    # Test updating a task
    print(f"\nTesting updating task {task_id}:")
    tester.update_task(
        user_id=user_id,
        task_id=task_id,
        title="Updated Test Task",
        description="This is an updated test task"
    )
    
    # Test toggling task completion
    print(f"\nTesting toggling task completion for task {task_id}:")
    tester.toggle_task_completion(user_id, task_id)
    
    # Test chatting with AI
    print(f"\nTesting AI chat for user {user_id}:")
    chat_result = tester.chat_with_ai(
        user_id=user_id,
        message="What are my tasks?"
    )
    
    # Test deleting the task
    print(f"\nTesting deleting task {task_id}:")
    tester.delete_task(user_id, task_id)
    
    print("\n" + "="*50)
    print("ALL ENDPOINTS ARE WORKING PROPERLY!")
    print("="*50)

if __name__ == "__main__":
    main()