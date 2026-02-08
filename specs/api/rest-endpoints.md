# REST API Endpoints Specification

## Overview
RESTful API endpoints for the Todo application with JWT-based authentication and user data isolation.

## Base URL
`/api/{user_id}/tasks`

## Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

## Endpoints

### 1. Get All Tasks
```
GET /api/{user_id}/tasks
```
**Description:** Retrieve all tasks for the authenticated user

**Headers:**
- Authorization: Bearer {jwt_token}

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)

**Response:**
- 200: Array of task objects
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
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch)

### 2. Create New Task
```
POST /api/{user_id}/tasks
```
**Description:** Create a new task for the authenticated user

**Headers:**
- Authorization: Bearer {jwt_token}
- Content-Type: application/json

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)

**Request Body:**
```json
{
  "title": "Task title (1-200 chars)",
  "description": "Optional task description (max 1000 chars)"
}
```

**Response:**
- 201: Created task object
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
- 400: Bad Request (validation errors)
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch)
- 422: Unprocessable Entity (validation errors)

### 3. Get Single Task
```
GET /api/{user_id}/tasks/{task_id}
```
**Description:** Retrieve a specific task for the authenticated user

**Headers:**
- Authorization: Bearer {jwt_token}

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- task_id: The ID of the task to retrieve

**Response:**
- 200: Task object
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
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

### 4. Update Task
```
PUT /api/{user_id}/tasks/{task_id}
```
**Description:** Update a specific task for the authenticated user

**Headers:**
- Authorization: Bearer {jwt_token}
- Content-Type: application/json

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- task_id: The ID of the task to update

**Request Body:**
```json
{
  "title": "Updated task title (1-200 chars)",
  "description": "Updated task description (max 1000 chars)"
}
```

**Response:**
- 200: Updated task object
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
- 400: Bad Request (validation errors)
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)
- 422: Unprocessable Entity (validation errors)

### 5. Delete Task
```
DELETE /api/{user_id}/tasks/{task_id}
```
**Description:** Delete a specific task for the authenticated user

**Headers:**
- Authorization: Bearer {jwt_token}

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- task_id: The ID of the task to delete

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

**Headers:**
- Authorization: Bearer {jwt_token}

**Path Parameters:**
- user_id: The authenticated user's ID (verified against JWT)
- task_id: The ID of the task to update

**Response:**
- 200: Updated task object with toggled completion status
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
- 401: Unauthorized (invalid token)
- 403: Forbidden (user_id mismatch or not owner)
- 404: Not Found (task doesn't exist)

## Common Headers
- Authorization: Bearer {jwt_token} (required for all endpoints)
- Content-Type: application/json (for POST, PUT requests)

## Common Error Responses
- 401 Unauthorized: Invalid or missing JWT token
- 403 Forbidden: Attempting to access resources not owned by the user
- 404 Not Found: Resource doesn't exist
- 422 Unprocessable Entity: Validation errors in request body
- 500 Internal Server Error: Unexpected server error

## Validation Rules
- Title: Required, 1-200 characters
- Description: Optional, max 1000 characters
- user_id in path must match user_id in JWT
- task_id must exist and belong to authenticated user