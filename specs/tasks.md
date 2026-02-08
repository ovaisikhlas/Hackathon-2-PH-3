# Todo Tasks Feature Specification

## Overview
This document specifies the tasks feature for the Todo application, including the ability to create, read, update, delete, and manage tasks with various statuses and properties.

## Features

### 1. Task Creation
- Users can create new tasks with a title and optional description
- Tasks are associated with the authenticated user
- Tasks have a default "pending" status when created
- Tasks include timestamps for creation and last update

### 2. Task Listing
- Users can view all their tasks
- Tasks are displayed with title, description, status, and timestamps
- Tasks can be filtered by status (all, active, completed)
- Tasks can be sorted by various criteria (creation date, update date, title)

### 3. Task Details
- Users can view detailed information about a specific task
- Includes title, description, status, creation date, and last update date

### 4. Task Updates
- Users can update task title and description
- Users can mark tasks as complete or incomplete
- Update timestamp is automatically updated when changes are made

### 5. Task Deletion
- Users can delete tasks they own
- Deletion is permanent and cannot be undone
- Associated data is cleaned up appropriately

## Data Model

### Task Entity
- `id`: Unique identifier (UUID)
- `title`: Task title (required, 1-200 characters)
- `description`: Task description (optional, max 1000 characters)
- `completed`: Boolean indicating completion status (default: false)
- `user_id`: Foreign key linking to the user who owns the task
- `created_at`: Timestamp when task was created
- `updated_at`: Timestamp when task was last updated

## API Endpoints

### Create Task
- `POST /api/{user_id}/tasks`
- Request body: `{title: string, description?: string}`
- Response: Task object with 201 status

### List Tasks
- `GET /api/{user_id}/tasks`
- Query params: `status` (optional: all|active|completed)
- Response: Array of Task objects

### Get Task
- `GET /api/{user_id}/tasks/{task_id}`
- Response: Single Task object

### Update Task
- `PUT /api/{user_id}/tasks/{task_id}`
- Request body: `{title?: string, description?: string, completed?: boolean}`
- Response: Updated Task object

### Delete Task
- `DELETE /api/{user_id}/tasks/{task_id}`
- Response: 204 No Content

### Toggle Task Completion
- `PATCH /api/{user_id}/tasks/{task_id}/complete`
- Response: Updated Task object

## Business Rules
- Users can only access their own tasks
- Task titles must be between 1 and 200 characters
- Task descriptions can be up to 1000 characters
- Users must be authenticated to perform any task operations
- Completed tasks remain accessible but are marked as such

## Error Handling
- 401 Unauthorized: User not authenticated
- 403 Forbidden: User attempting to access another user's tasks
- 404 Not Found: Task does not exist
- 422 Unprocessable Entity: Invalid input data

## Security Considerations
- JWT tokens are required for all endpoints
- User ID in URL path must match authenticated user
- No cross-user access to tasks is permitted