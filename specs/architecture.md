# Todo App Architecture - Phase II

## System Architecture
The application follows a classic three-tier architecture with clean separation of concerns:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   Frontend      │◄──►│    Backend       │◄──►│   Database (Neon)   │
│   (Next.js)     │    │   (FastAPI)      │    │   (PostgreSQL)      │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
```

## Component Architecture

### Frontend (Next.js 16+)
- App Router for navigation
- Server Components for initial rendering
- Client Components for interactivity
- Better Auth integration for authentication
- API client in `/lib/api.ts` for JWT-attached calls

### Backend (FastAPI)
- RESTful API endpoints following `/api/{user_id}/tasks` pattern
- JWT authentication middleware
- SQLModel ORM for database operations
- Pydantic models for request/response validation
- Dependency injection for authentication

### Database (Neon Serverless PostgreSQL)
- Users table with id, email, name, created_at
- Tasks table with id, user_id (FK), title, description, completed, timestamps
- Proper indexing on foreign keys and boolean fields

## Security Architecture
- JWT-based authentication with Better Auth
- User data isolation via user_id filtering
- Stateful sessions via JWT tokens
- Automatic token expiration (7 days)

## Data Flow
1. User authenticates via Better Auth
2. JWT token is stored and sent with API requests
3. Backend verifies token and extracts user_id
4. All database queries are filtered by authenticated user_id
5. Response data contains only user's tasks

## API Contract
- Base URL: `/api/{user_id}/tasks`
- Methods: GET, POST, PUT, DELETE, PATCH
- Authentication: Bearer token in Authorization header
- Error handling: Standard HTTP status codes

## Integration Points
- Frontend ↔ Backend: REST API with JWT authentication
- Backend ↔ Database: SQLModel ORM
- Auth Service: Better Auth for user management