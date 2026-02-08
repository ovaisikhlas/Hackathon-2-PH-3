# Backend Todo API - Tasks Module

## Overview
This document specifies the backend implementation of the tasks module for the Todo application. It details the API endpoints, data models, business logic, and integration points for task management functionality.

## API Endpoints

### Task Management Endpoints

#### 1. Create Task
- **Endpoint**: `POST /api/{user_id}/tasks`
- **Description**: Creates a new task for the specified user
- **Path Parameter**: `user_id` (string) - The ID of the user creating the task
- **Request Body**:
  ```json
  {
    "title": "string (required, 1-200 chars)",
    "description": "string (optional, max 1000 chars)",
    "category": "string (optional)"
  }
  ```
- **Response**: 201 Created with Task object
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path

#### 2. List Tasks
- **Endpoint**: `GET /api/{user_id}/tasks`
- **Description**: Retrieves all tasks for the specified user
- **Path Parameter**: `user_id` (string) - The ID of the user whose tasks to retrieve
- **Query Parameters**:
  - `status` (optional): Filter by completion status ("all", "active", "completed")
- **Response**: 200 OK with array of Task objects
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path

#### 3. Get Specific Task
- **Endpoint**: `GET /api/{user_id}/tasks/{task_id}`
- **Description**: Retrieves a specific task by ID
- **Path Parameters**:
  - `user_id` (string) - The ID of the user
  - `task_id` (integer) - The ID of the task to retrieve
- **Response**: 200 OK with Task object
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path and own the task

#### 4. Update Task
- **Endpoint**: `PUT /api/{user_id}/tasks/{task_id}`
- **Description**: Updates an existing task
- **Path Parameters**:
  - `user_id` (string) - The ID of the user
  - `task_id` (integer) - The ID of the task to update
- **Request Body**:
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "completed": "boolean (optional)",
    "category": "string (optional)"
  }
  ```
- **Response**: 200 OK with updated Task object
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path and own the task

#### 5. Delete Task
- **Endpoint**: `DELETE /api/{user_id}/tasks/{task_id}`
- **Description**: Deletes a specific task
- **Path Parameters**:
  - `user_id` (string) - The ID of the user
  - `task_id` (integer) - The ID of the task to delete
- **Response**: 204 No Content
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path and own the task

#### 6. Toggle Task Completion
- **Endpoint**: `PATCH /api/{user_id}/tasks/{task_id}/complete`
- **Description**: Toggles the completion status of a task
- **Path Parameters**:
  - `user_id` (string) - The ID of the user
  - `task_id` (integer) - The ID of the task to toggle
- **Response**: 200 OK with updated Task object
- **Authentication**: JWT Bearer token required
- **Authorization**: User must match the user_id in the path and own the task

## Data Models

### Task Model
```python
class Task(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=1000)
    completed: bool = Field(default=False)
    user_id: str
    category: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

### Task Schemas
```python
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=1000)
    completed: bool = Field(default=False)
    category: Optional[str] = Field(default=None)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = Field(default=None)
    category: Optional[str] = Field(default=None)

class TaskResponse(TaskBase):
    id: str
    created_at: datetime
    updated_at: datetime
```

## Business Logic

### Validation Rules
1. Task titles must be between 1 and 200 characters
2. Task descriptions must not exceed 1000 characters
3. Users can only access their own tasks
4. Task IDs must be valid integers
5. User IDs in the path must match the authenticated user

### Authorization Checks
1. Verify JWT token is valid
2. Extract user ID from token
3. Compare extracted user ID with user ID in the path
4. Ensure user owns the resource being accessed

### Error Handling
- **400 Bad Request**: Invalid input parameters
- **401 Unauthorized**: Missing or invalid JWT token
- **403 Forbidden**: User attempting to access another user's resources
- **404 Not Found**: Resource does not exist
- **422 Unprocessable Entity**: Validation failed

## Dependencies

### External Libraries
- FastAPI: Web framework
- SQLModel: ORM and database modeling
- Pydantic: Request/response validation
- python-jose: JWT handling
- bcrypt: Password hashing
- Better Auth: Authentication management

### Internal Modules
- `database.database`: Database session management
- `models.task`: Task data model
- `schemas.task`: Request/response schemas
- `core.auth`: Authentication utilities
- `models.user`: User data model

## Security Considerations
- All endpoints require JWT authentication
- User ID in path must match authenticated user
- No cross-user access to tasks
- Input validation on all request parameters
- SQL injection prevention via SQLModel parameter binding

## Performance Considerations
- Indexes on user_id for efficient filtering
- Connection pooling for database operations
- Efficient query patterns to minimize database load
- Caching strategies for frequently accessed data

## Testing Strategy
- Unit tests for individual functions
- Integration tests for API endpoints
- Authentication and authorization tests
- Error condition tests
- Performance tests for concurrent access