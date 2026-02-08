# Task CRUD Feature Specification

## Overview
Implement the 5 Basic Level features (Add, Delete, Update, View/List, Mark Complete) for user tasks with proper authentication and data isolation.

## Functional Requirements

### 1. Add Task (CREATE)
- Users can create new tasks with required title and optional description
- Title validation: 1-200 characters
- Description validation: max 1000 characters
- Task is associated with authenticated user_id
- Created timestamp is automatically set
- Completed status defaults to false

### 2. View/List Tasks (READ)
- Users can view all their tasks
- Tasks are filtered by authenticated user_id
- Display includes: title, description, completion status, creation date
- Tasks are sorted by creation date (newest first)
- Responsive display suitable for mobile and desktop

### 3. Update Task (UPDATE)
- Users can modify task title and description
- Prevent modification of other users' tasks
- Updated timestamp is automatically updated
- Preserve original creation timestamp

### 4. Delete Task (DELETE)
- Users can delete their own tasks
- Prevent deletion of other users' tasks
- Confirmation for deletion (UX consideration)

### 5. Mark Complete (PATCH)
- Users can toggle task completion status
- Only the completed field can be modified
- Updated timestamp is automatically updated
- Prevent modification of other users' tasks

## Data Model
```sql
-- Tasks table
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
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

## Validation Rules
- Title: Required, 1-200 characters
- Description: Optional, max 1000 characters
- User association: Must match authenticated user_id
- Access control: Users can only access their own tasks

## Error Handling
- 401: Unauthorized (invalid/missing JWT token)
- 403: Forbidden (attempting to access other user's tasks)
- 404: Not Found (task doesn't exist)
- 422: Unprocessable Entity (validation errors)

## Security Considerations
- All endpoints require valid JWT token
- All operations enforce user_id matching
- No cross-user data access allowed
- Proper authentication middleware on all routes