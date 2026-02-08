# Todo App Backend API Documentation

## Overview
This is the backend API for the AI-Powered Todo ChatBot application. It provides endpoints for user authentication, task management, and AI-powered chat functionality.

## Base URL
`http://localhost:8000` (for local development)

## Authentication
Most endpoints require authentication using JWT tokens. Tokens are obtained through the sign-in endpoint and must be included in the Authorization header as a Bearer token.

## Endpoints

### Authentication
- `POST /api/auth/sign-up` - Register a new user
- `POST /api/auth/sign-in/credentials` - Login with email and password

### Tasks
- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion status
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task

### AI Chat
- `POST /api/{user_id}/chat` - Chat with the AI assistant

## AI Chat Endpoint Details

### POST /api/{user_id}/chat

#### Description
Interact with the AI assistant to manage your tasks using natural language.

#### Headers
- `Authorization: Bearer {token}` - Required authentication token
- `Content-Type: application/json` - Required content type

#### Path Parameters
- `user_id` (string) - The ID of the authenticated user

#### Request Body
```json
{
  "message": "Your message to the AI assistant",
  "conversation_id": "optional conversation ID to continue an existing conversation"
}
```

#### Response
```json
{
  "response": "AI-generated response",
  "conversation_id": "ID of the conversation (new or existing)"
}
```

#### Example Request
```bash
curl -X POST http://localhost:8000/api/user123/chat \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Add a new task to buy groceries",
    "conversation_id": null
  }'
```

#### Example Response
```json
{
  "response": "I've added the task 'buy groceries' to your list.",
  "conversation_id": "conv_abc123"
}
```

## Error Responses

Common error responses:
- `400 Bad Request`: Invalid request format
- `401 Unauthorized`: Missing or invalid authentication token
- `403 Forbidden`: User not authorized to access the resource
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side error

## Environment Variables

The application uses the following environment variables:
- `GOOGLE_API_KEY` - API key for Google Generative AI services
- `DATABASE_URL` - Database connection string
- `SECRET_KEY` - Secret key for JWT token signing
- `ALGORITHM` - Algorithm for JWT token encoding
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Access token expiration time

## Running the Application

To run the backend locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in a `.env` file

3. Run the application:
   ```bash
   python -m uvicorn app.main:app --reload --port 8000
   ```

## Testing

Run the test suite:
```bash
python test_endpoints.py
```