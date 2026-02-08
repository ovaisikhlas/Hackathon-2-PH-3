# Claude Code Rules - API Endpoints

## Feature-Specific Guidelines

**Focus Area:**
- RESTful API design
- Endpoint implementation
- Request/response validation
- Error handling

**Key Standards:**
- Follow specified endpoint patterns: /api/{user_id}/tasks
- JWT authentication on all endpoints
- Proper HTTP status codes
- Consistent request/response schemas

**Security Considerations:**
- Authentication middleware on all routes
- User_id verification in path parameters
- Input validation and sanitization
- Proper error responses to prevent information disclosure