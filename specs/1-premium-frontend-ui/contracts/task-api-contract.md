# Task API Contract

## Overview
This document defines the API contract between the frontend and backend for task management operations. All endpoints require JWT authentication in the Authorization header.

## Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

## Base URL
All endpoints are prefixed with the base API URL configured in environment variables.

## Endpoints

### Get All Tasks
```
GET /api/{user_id}/tasks
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
- **Headers**:
  - `Authorization: Bearer {token}`

#### Response
- **Success (200)**:
  ```typescript
  Task[]
  ```
  Example:
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

- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch

### Create New Task
```
POST /api/{user_id}/tasks
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
- **Headers**:
  - `Authorization: Bearer {token}`
  - `Content-Type: application/json`
- **Body**:
  ```typescript
  {
    title: string, // 1-200 characters
    description?: string // optional, max 1000 characters
  }
  ```

#### Response
- **Success (201)**:
  ```typescript
  Task
  ```
  Example:
  ```json
  {
    "id": 1,
    "user_id": 123,
    "title": "New task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
  ```

- **Bad Request (400)**: Validation errors
- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch
- **Unprocessable Entity (422)**: Validation errors

### Get Single Task
```
GET /api/{user_id}/tasks/{task_id}
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
  - `task_id` (number): The ID of the task to retrieve
- **Headers**:
  - `Authorization: Bearer {token}`

#### Response
- **Success (200)**:
  ```typescript
  Task
  ```

- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch or not owner
- **Not Found (404)**: Task doesn't exist

### Update Task
```
PUT /api/{user_id}/tasks/{task_id}
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
  - `task_id` (number): The ID of the task to update
- **Headers**:
  - `Authorization: Bearer {token}`
  - `Content-Type: application/json`
- **Body**:
  ```typescript
  {
    title?: string, // 1-200 characters if provided
    description?: string // max 1000 characters if provided
  }
  ```

#### Response
- **Success (200)**:
  ```typescript
  Task
  ```

- **Bad Request (400)**: Validation errors
- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch or not owner
- **Not Found (404)**: Task doesn't exist
- **Unprocessable Entity (422)**: Validation errors

### Delete Task
```
DELETE /api/{user_id}/tasks/{task_id}
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
  - `task_id` (number): The ID of the task to delete
- **Headers**:
  - `Authorization: Bearer {token}`

#### Response
- **Success (204)**: No content (task deleted successfully)

- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch or not owner
- **Not Found (404)**: Task doesn't exist

### Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{task_id}/complete
```

#### Request
- **Path Parameters**:
  - `user_id` (number): The authenticated user's ID (verified against JWT)
  - `task_id` (number): The ID of the task to update
- **Headers**:
  - `Authorization: Bearer {token}`

#### Response
- **Success (200)**:
  ```typescript
  Task
  ```
  With toggled completion status

- **Unauthorized (401)**: Invalid or missing token
- **Forbidden (403)**: User_id mismatch or not owner
- **Not Found (404)**: Task doesn't exist

## Common Response Types

### Task Object
```typescript
{
  id: number,
  user_id: number,
  title: string, // 1-200 characters
  description?: string, // optional, max 1000 characters
  completed: boolean,
  created_at: string, // ISO 8601 format
  updated_at: string // ISO 8601 format
}
```

### Error Response
```typescript
{
  detail: string
}
```

## Validation Rules
- Title: Required, 1-200 characters
- Description: Optional, max 1000 characters
- user_id in path must match user_id in JWT
- task_id must exist and belong to authenticated user

## Common Headers
- `Authorization: Bearer {token}` (required for all endpoints)
- `Content-Type: application/json` (for POST, PUT requests)