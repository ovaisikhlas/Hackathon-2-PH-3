// CLAUDE.md for backend
# Claude Code Rules - Backend

## Backend Development Guidelines

**Technology Stack:**
- Python FastAPI framework
- SQLModel ORM for database operations
- Pydantic for request/response validation
- Better Auth with JWT plugin for authentication
- Neon Serverless PostgreSQL for persistence

**File Structure:**
- `app/` - Main application and startup configuration
- `models/` - SQLModel database models
- `schemas/` - Pydantic request/response schemas
- `database/` - Database connection and session management
- `api/` - API route definitions
- `core/` - Core configurations and utilities
- `utils/` - Helper functions

**Development Standards:**
- RESTful API design following specification
- JWT authentication middleware implementation
- Proper request/response validation with Pydantic
- Database operations using SQLModel
- Error handling with appropriate HTTP status codes
- Type hints for all functions and endpoints

**Security:**
- JWT token validation on all protected endpoints
- User data isolation via user_id filtering
- Input validation to prevent injection attacks
- Proper CORS configuration
- Secure password hashing and handling

**Performance:**
- Efficient database queries with proper indexing
- Connection pooling for database operations
- Async operations where appropriate
- Proper pagination for large datasets