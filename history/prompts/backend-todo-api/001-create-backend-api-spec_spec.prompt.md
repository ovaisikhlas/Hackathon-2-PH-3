# Create Backend API Specification for Todo App

## Prompt
Create a comprehensive specification for the backend API of a Todo application that implements the 5 Basic Level features (Add, View/List, Update, Delete, Mark Complete) with secure multi-user isolation.

## Context
The Todo application needs a robust backend API that works seamlessly with a Next.js frontend and Better Auth authentication system. The backend should use FastAPI with SQLModel ORM and Neon PostgreSQL for data persistence.

## Requirements

### Core Functionality
- Implement RESTful API endpoints for task management
- Support all 5 Basic Level features: Add, View/List, Update, Delete, Mark Complete
- Enforce multi-user isolation with proper authentication and authorization
- Use JWT tokens for authentication (compatible with Better Auth frontend)

### Technical Specifications
- Use FastAPI framework for the backend
- Implement SQLModel ORM for database operations
- Use Neon Serverless PostgreSQL for data persistence
- Ensure all endpoints are properly secured
- Implement proper error handling with appropriate HTTP status codes

### API Endpoints Required
1. GET /api/{user_id}/tasks - List all tasks for a user
2. POST /api/{user_id}/tasks - Create a new task
3. GET /api/{user_id}/tasks/{id} - Get a specific task
4. PUT /api/{user_id}/tasks/{id} - Update a task
5. DELETE /api/{user_id}/tasks/{id} - Delete a task
6. PATCH /api/{user_id}/tasks/{id}/complete - Toggle task completion

### Security Requirements
- All endpoints must require valid JWT authentication
- Users must only access their own tasks (enforce user_id matching)
- Return appropriate error codes (401, 403, 404, etc.) for unauthorized access
- Validate all inputs to prevent injection attacks

### Data Models
- User model with id (string), email, name, timestamps
- Task model with id, user_id (foreign key), title, description, completed status, timestamps
- Proper indexing for efficient queries (especially on user_id and completed fields)

### Response Format
- Consistent JSON responses compatible with frontend API client
- Proper HTTP status codes for all operations
- Meaningful error messages for different failure scenarios

## Expected Output
Provide a complete API specification document that includes:
- Detailed endpoint descriptions with request/response schemas
- Database schema specification
- Authentication and authorization requirements
- Error handling specification
- Integration requirements with frontend
- Security considerations
- Performance requirements