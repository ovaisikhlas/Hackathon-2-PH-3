# Backend Todo API Specification

## Overview
This specification defines the backend API for the Todo application, implementing a secure, performant FastAPI backend that fully supports the 5 Basic Level features (Add, View/List, Update, Delete, Mark Complete) with Neon PostgreSQL persistence via SQLModel ORM. The API integrates seamlessly with the Next.js frontend through JWT authentication middleware (using Better Auth tokens), enforcing multi-user isolation and task ownership.

## API Endpoints

### Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

### Base Path
`/api/{user_id}/tasks`

### 1. List Tasks
```
GET /api/{user_id}/tasks
```
**Description:** Retrieve all tasks for the authenticated user

**Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- status (optional): Filter by status (all|pending|completed)

**Response:**
- 200: Array of task objects
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch)

### 2. Create Task
```
POST /api/{user_id}/tasks
```
**Description:** Create a new task for the authenticated user

**Request Body:**
```json
{
  "title": "Task title (1-200 chars)",
  "description": "Optional task description (max 1000 chars)"
}
```

**Response:**
- 201: Created task object
- 400: Bad Request (validation errors)
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch)

### 3. Get Single Task
```
GET /api/{user_id}/tasks/{task_id}
```
**Description:** Retrieve a specific task for the authenticated user

**Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- task_id: The ID of the task to retrieve

**Response:**
- 200: Task object
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

### 4. Update Task
```
PUT /api/{user_id}/tasks/{task_id}
```
**Description:** Update a specific task for the authenticated user

**Request Body:**
```json
{
  "title": "Updated task title (1-200 chars)",
  "description": "Updated task description (max 1000 chars)"
}
```

**Response:**
- 200: Updated task object
- 400: Bad Request (validation errors)
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

### 5. Delete Task
```
DELETE /api/{user_id}/tasks/{task_id}
```
**Description:** Delete a specific task for the authenticated user

**Response:**
- 204: No Content (task deleted successfully)
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

### 6. Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{task_id}/complete
```
**Description:** Toggle the completion status of a specific task

**Response:**
- 200: Updated task object with toggled completion status
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

## Data Models

### Task Model
```sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  user_id VARCHAR(255) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_completed ON tasks(completed);
```

### User Model
```sql
CREATE TABLE users (
  id VARCHAR(255) PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Authentication & Security

### JWT Token Verification
- Verify JWT signature using BETTER_AUTH_SECRET
- Extract user_id from token payload
- Compare extracted user_id with the one in the URL path
- Return 401 for invalid/missing/expired tokens
- Return 403 for ownership violations

### Input Validation
- Title: Required, 1-200 characters
- Description: Optional, max 1000 characters
- All inputs sanitized to prevent injection attacks

## Error Handling

### HTTP Status Codes
- 200: OK (successful GET, PATCH)
- 201: Created (successful POST)
- 204: No Content (successful DELETE)
- 400: Bad Request (validation errors)
- 401: Unauthorized (invalid/missing JWT token)
- 403: Forbidden (attempting to access resources not owned by the user)
- 404: Not Found (resource doesn't exist)
- 422: Unprocessable Entity (validation errors)
- 500: Internal Server Error (unexpected server error)

### Error Response Format
```json
{
  "detail": "Error message"
}
```

## Dependencies
- FastAPI
- SQLModel
- Pydantic
- PyJWT
- python-jose
- psycopg2-binary

## Configuration
- DATABASE_URL: PostgreSQL connection string
- BETTER_AUTH_SECRET: Secret key for JWT verification
- ALLOWED_ORIGINS: CORS configuration for frontend domains

## Deployment
- Backend runs on port 8000
- Connects to Neon PostgreSQL database
- Compatible with Docker deployment