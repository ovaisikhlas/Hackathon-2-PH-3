# Backend Todo API - Specification

## Overview
This document provides a comprehensive specification for the Todo API backend, detailing the architecture, endpoints, data models, and integration requirements.

## Architecture

### Technology Stack
- **Framework**: FastAPI (latest stable)
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens (compatible with Better Auth)
- **Validation**: Pydantic
- **Security**: PyJWT, python-jose

### Service Layer
- **API Layer**: FastAPI with async support
- **Business Logic**: Encapsulated in route handlers
- **Data Access**: SQLModel ORM operations
- **Authentication**: JWT middleware
- **Configuration**: Pydantic Settings

## API Endpoints

### Base URL
`/api/{user_id}/tasks`

### Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

### 1. List Tasks
```
GET /api/{user_id}/tasks
```
**Description:** Retrieve all tasks for the authenticated user

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)

**Query Parameters (Optional):**
- `status`: Filter by status ("all", "pending", "completed")

**Headers:**
- `Authorization: Bearer {jwt_token}`

**Response:**
- `200 OK`: Array of task objects
```json
[
  {
    "id": 1,
    "user_id": "user123",
    "title": "Sample task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
]
```
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: User ID mismatch

### 2. Create Task
```
POST /api/{user_id}/tasks
```
**Description:** Create a new task for the authenticated user

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)

**Headers:**
- `Authorization: Bearer {jwt_token}`
- `Content-Type: application/json`

**Request Body:**
```json
{
  "title": "Task title (1-200 chars)",
  "description": "Optional task description (max 1000 chars)"
}
```

**Response:**
- `201 Created`: Created task object
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Sample task",
  "description": "Task description",
  "completed": false,
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```
- `400 Bad Request`: Validation errors
- `401 Unauthorized`: Invalid token
- `403 Forbidden`: User ID mismatch
- `422 Unprocessable Entity`: Validation errors

### 3. Get Single Task
```
GET /api/{user_id}/tasks/{task_id}
```
**Description:** Retrieve a specific task for the authenticated user

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)
- `task_id`: The ID of the task to retrieve

**Headers:**
- `Authorization: Bearer {jwt_token}`

**Response:**
- `200 OK`: Task object
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Sample task",
  "description": "Task description",
  "completed": false,
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```
- `401 Unauthorized`: Invalid token
- `403 Forbidden`: User ID mismatch or not owner
- `404 Not Found`: Task doesn't exist

### 4. Update Task
```
PUT /api/{user_id}/tasks/{task_id}
```
**Description:** Update a specific task for the authenticated user

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)
- `task_id`: The ID of the task to update

**Headers:**
- `Authorization: Bearer {jwt_token}`
- `Content-Type: application/json`

**Request Body:**
```json
{
  "title": "Updated task title (1-200 chars)",
  "description": "Updated task description (max 1000 chars)"
}
```

**Response:**
- `200 OK`: Updated task object
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Updated sample task",
  "description": "Updated task description",
  "completed": false,
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-02T00:00:00Z"
}
```
- `400 Bad Request`: Validation errors
- `401 Unauthorized`: Invalid token
- `403 Forbidden`: User ID mismatch or not owner
- `404 Not Found`: Task doesn't exist
- `422 Unprocessable Entity`: Validation errors

### 5. Delete Task
```
DELETE /api/{user_id}/tasks/{task_id}
```
**Description:** Delete a specific task for the authenticated user

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)
- `task_id`: The ID of the task to delete

**Headers:**
- `Authorization: Bearer {jwt_token}`

**Response:**
- `204 No Content`: Task deleted successfully
- `401 Unauthorized`: Invalid token
- `403 Forbidden`: User ID mismatch or not owner
- `404 Not Found`: Task doesn't exist

### 6. Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{task_id}/complete
```
**Description:** Toggle the completion status of a specific task

**Path Parameters:**
- `user_id`: The authenticated user's ID (verified against JWT)
- `task_id`: The ID of the task to update

**Headers:**
- `Authorization: Bearer {jwt_token}`

**Response:**
- `200 OK`: Updated task object with toggled completion status
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Sample task",
  "description": "Task description",
  "completed": true,
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-02T00:00:00Z"
}
```
- `401 Unauthorized`: Invalid token
- `403 Forbidden`: User ID mismatch or not owner
- `404 Not Found`: Task doesn't exist

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
- `200 OK`: Successful GET, PATCH operations
- `201 Created`: Successful POST operation
- `204 No Content`: Successful DELETE operation
- `400 Bad Request`: Validation errors
- `401 Unauthorized`: Invalid/missing JWT token
- `403 Forbidden`: Attempting to access resources not owned by the user
- `404 Not Found`: Resource doesn't exist
- `422 Unprocessable Entity`: Validation errors
- `500 Internal Server Error`: Unexpected server error

### Error Response Format
```json
{
  "detail": "Error message"
}
```

## Configuration

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `BETTER_AUTH_SECRET`: Secret key for JWT verification
- `SECRET_KEY`: General secret key for encryption
- `ENVIRONMENT`: Environment setting (development/production)
- `ALLOWED_ORIGINS`: CORS configuration for frontend domains

### CORS Configuration
- Allow origins: ["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"]
- Allow credentials: true
- Allow methods: ["*"]
- Allow headers: ["*"]

## Integration Requirements

### Frontend Compatibility
- API responses must match shapes expected by frontend's /lib/api.ts client
- JWT tokens must be compatible with Better Auth frontend implementation
- Error formats must be consistent for frontend error handling
- Response timestamps must be in ISO 8601 format

### Backend Dependencies
- FastAPI
- SQLModel
- Pydantic
- PyJWT
- python-jose
- psycopg2-binary
- python-dotenv

## Performance Requirements

### Response Times
- API endpoints should respond within 500ms under normal load
- Database queries should complete within 200ms
- Authentication checks should complete within 50ms

### Concurrency
- Support at least 100 concurrent connections
- Efficient connection pooling
- Proper resource management

## Deployment Requirements

### Infrastructure
- Server: Python 3.8+ runtime
- Database: Neon Serverless PostgreSQL or compatible PostgreSQL
- Memory: Minimum 512MB RAM
- Storage: Sufficient for application code and dependencies

### Scaling
- Horizontal scaling support
- Load balancing capabilities
- Auto-scaling based on demand

## Monitoring & Observability

### Logging
- Structured logging for all API requests
- Error logging with stack traces
- Performance metrics logging

### Health Checks
- `/health` endpoint for infrastructure monitoring
- Database connectivity check
- External service dependency checks