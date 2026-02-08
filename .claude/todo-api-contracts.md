# Todo API Contracts

## Overview
This document defines the API contracts for the Todo application, including all endpoints, request/response formats, authentication requirements, and error handling patterns.

## Base URL
All API endpoints are relative to: `https://api.todoapp.com/v1` (or `http://localhost:8000/v1` for development)

## Authentication
All endpoints require JWT authentication in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

## Common Headers
- `Authorization: Bearer {token}` (required for all endpoints)
- `Content-Type: application/json` (for POST, PUT, PATCH requests)

## Common Error Responses
- **400 Bad Request**: Validation errors
  ```json
  {
    "detail": "Validation error details"
  }
  ```

- **401 Unauthorized**: Invalid or missing token
  ```json
  {
    "detail": "Authentication credentials were not provided"
  }
  ```

- **403 Forbidden**: User not authorized to access resource
  ```json
  {
    "detail": "Access forbidden"
  }
  ```

- **404 Not Found**: Resource not found
  ```json
  {
    "detail": "Resource not found"
  }
  ```

- **422 Unprocessable Entity**: Validation errors in request body
  ```json
  {
    "detail": "Validation failed",
    "errors": [
      {
        "field": "title",
        "message": "Title must be between 1 and 200 characters"
      }
    ]
  }
  ```

- **500 Internal Server Error**: Server error
  ```json
  {
    "detail": "Internal server error"
  }
  ```

## Endpoints

### Task Management

#### Get All Tasks
```
GET /api/{user_id}/tasks
```

**Description**: Retrieve all tasks for the authenticated user

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)

**Headers**:
- `Authorization: Bearer {token}`

**Response**:
- **200 Success**:
  ```json
  [
    {
      "id": 1,
      "user_id": 123,
      "title": "Sample task",
      "description": "Task description",
      "completed": false,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
  ```

#### Create New Task
```
POST /api/{user_id}/tasks
```

**Description**: Create a new task for the authenticated user

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)

**Headers**:
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "Task title (1-200 chars)",
  "description": "Optional task description (max 1000 chars)"
}
```

**Response**:
- **201 Created**:
  ```json
  {
    "id": 1,
    "user_id": 123,
    "title": "Sample task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

#### Get Single Task
```
GET /api/{user_id}/tasks/{task_id}
```

**Description**: Retrieve a specific task for the authenticated user

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)
- `task_id` (integer): The ID of the task to retrieve

**Headers**:
- `Authorization: Bearer {token}`

**Response**:
- **200 Success**:
  ```json
  {
    "id": 1,
    "user_id": 123,
    "title": "Sample task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

#### Update Task
```
PUT /api/{user_id}/tasks/{task_id}
```

**Description**: Update a specific task for the authenticated user

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)
- `task_id` (integer): The ID of the task to update

**Headers**:
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "Updated task title (1-200 chars)",
  "description": "Updated task description (max 1000 chars)"
}
```

**Response**:
- **200 Success**:
  ```json
  {
    "id": 1,
    "user_id": 123,
    "title": "Updated sample task",
    "description": "Updated task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
  ```

#### Delete Task
```
DELETE /api/{user_id}/tasks/{task_id}
```

**Description**: Delete a specific task for the authenticated user

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)
- `task_id` (integer): The ID of the task to delete

**Headers**:
- `Authorization: Bearer {token}`

**Response**:
- **204 No Content**: Task deleted successfully

#### Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{task_id}/complete
```

**Description**: Toggle the completion status of a specific task

**Path Parameters**:
- `user_id` (integer): The authenticated user's ID (verified against JWT)
- `task_id` (integer): The ID of the task to update

**Headers**:
- `Authorization: Bearer {token}`

**Response**:
- **200 Success**:
  ```json
  {
    "id": 1,
    "user_id": 123,
    "title": "Sample task",
    "description": "Task description",
    "completed": true,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
  ```

### User Management

#### User Registration
```
POST /auth/register
```

**Description**: Register a new user

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "User Name"
}
```

**Response**:
- **201 Created**:
  ```json
  {
    "id": 123,
    "email": "user@example.com",
    "name": "User Name",
    "created_at": "2023-01-01T00:00:00Z"
  }
  ```

#### User Login
```
POST /auth/login
```

**Description**: Authenticate user and return JWT token

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response**:
- **200 Success**:
  ```json
  {
    "access_token": "jwt_token_string",
    "token_type": "bearer",
    "expires_in": 604800,
    "user": {
      "id": 123,
      "email": "user@example.com",
      "name": "User Name"
    }
  }
  ```

#### User Profile
```
GET /auth/profile
```

**Description**: Get authenticated user's profile information

**Headers**:
- `Authorization: Bearer {token}`

**Response**:
- **200 Success**:
  ```json
  {
    "id": 123,
    "email": "user@example.com",
    "name": "User Name",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

## Data Models

### Task Object
```json
{
  "id": 1,
  "user_id": 123,
  "title": "Task title",
  "description": "Task description",
  "completed": false,
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

**Validation Rules**:
- `id`: Auto-generated integer, read-only
- `user_id`: Integer, required, references user
- `title`: String, 1-200 characters, required
- `description`: String, optional, max 1000 characters
- `completed`: Boolean, default false
- `created_at`: ISO 8601 datetime, read-only
- `updated_at`: ISO 8601 datetime, read-only

### User Object
```json
{
  "id": 123,
  "email": "user@example.com",
  "name": "User Name",
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

**Validation Rules**:
- `id`: Auto-generated integer, read-only
- `email`: String, valid email format, required, unique
- `name`: String, optional, max 255 characters
- `created_at`: ISO 8601 datetime, read-only
- `updated_at`: ISO 8601 datetime, read-only

## Validation Rules

### Task Validation
- Title: Required, 1-200 characters
- Description: Optional, max 1000 characters
- Completed: Boolean value (true/false)
- user_id must match authenticated user

### User Validation
- Email: Required, valid email format, unique
- Password: Required, minimum 8 characters with complexity
- Name: Optional, max 255 characters

## Rate Limiting
- API requests are limited to 1000 requests per hour per user
- Exceeding rate limit returns 429 Too Many Requests

## Versioning
- API version is included in the URL path (e.g., `/v1/`)
- Breaking changes will result in a new version (e.g., `/v2/`)
- Backwards-compatible changes will be added to existing version