# Backend Todo API - Implementation Plan

## Overview
This document outlines the implementation plan for the Todo API backend, detailing the phases, tasks, and timeline for development.

## Project Goals
- Implement a secure, performant FastAPI backend with Neon PostgreSQL persistence
- Strict JWT authentication using Better Auth tokens
- User isolation and complete support for the 5 Basic Todo features
- Full compatibility with the frontend's /lib/api.ts client

## Implementation Phases

### Phase 1: Project Initialization & Environment Setup
**Duration:** 1 day
**Tasks:**
- [x] Create backend folder structure: main.py, models.py, db.py, middleware/auth.py, routes/tasks.py, schemas.py
- [x] Set up requirements.txt with: fastapi, uvicorn, sqlmodel, pydantic, pyjwt, python-dotenv
- [x] Implement .env loading using pydantic-settings
- [x] Define Settings class with: DATABASE_URL, BETTER_AUTH_SECRET, SECRET_KEY, ENVIRONMENT
- [x] Create basic FastAPI app in main.py: title, version, CORS middleware (origins: ["http://localhost:3000"]), root endpoint
- [x] Add global exception handlers for validation and HTTP errors

### Phase 2: Database Connection & SQLModel Models
**Duration:** 1 day
**Tasks:**
- [x] In db.py: Create engine from DATABASE_URL, Session maker, get_session dependency
- [x] Add startup event to create_all tables (dev only)
- [x] In models.py:
  - [x] User model (id: str PK, email: str unique, name: str, created_at: datetime)
  - [x] Task model (id: int PK, user_id: str FK, title: str not null, description: str nullable, completed: bool default False, created_at: datetime, updated_at: datetime)
  - [x] Add indexes on user_id and completed
- [x] In schemas.py: Define Pydantic models
  - [x] TaskCreate: title (constr min=1 max=200), description (str | None)
  - [x] TaskUpdate: title/description (Optional)
  - [x] TaskOut: full task fields

### Phase 3: JWT Authentication Middleware
**Duration:** 1 day
**Tasks:**
- [x] In core/auth.py:
  - [x] Create async middleware to extract Bearer token
  - [x] Verify signature and expiry using pyjwt with BETTER_AUTH_SECRET (HS256)
  - [x] Decode payload to extract user_id (sub field)
  - [x] Attach user_id to request state
  - [x] Raise HTTPException(401) on any failure
- [x] Create dependency: def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security))
- [x] Verify token and extract user information

### Phase 4: Tasks Router & CRUD Endpoints
**Duration:** 2 days
**Tasks:**
- [x] In api/tasks.py: APIRouter(prefix="/api/{user_id}", dependencies=[Depends(get_current_user)])
- [x] Implement endpoints using Session:
  - [x] GET /tasks: Filter by user_id, return List[TaskResponse]
  - [x] POST /tasks: Accept TaskCreate, create task with user_id, return TaskResponse (201)
  - [x] GET /tasks/{id}: Fetch by id + user_id match, return TaskResponse or 404
  - [x] PUT /tasks/{id}: Partial update with TaskUpdate, check ownership, return TaskResponse
  - [x] DELETE /tasks/{id}: Delete if owned, return 204
  - [x] PATCH /tasks/{id}/complete: Toggle completed, check ownership, return TaskResponse
- [x] Enforce ownership check: if task.user_id != current_user.id → 403
- [x] Use session.exec/select/add/commit/refresh as needed

### Phase 5: Validation, Error Handling & Security Polish
**Duration:** 1 day
**Tasks:**
- [x] Add Pydantic validation in models/schemas
- [x] Implement global exception handler for validation errors → 422 JSON
- [x] Add custom 401/403/404 handlers with consistent JSON format
- [x] Enable OpenAPI security scheme (Bearer JWT) in app.openapi_tags
- [x] Configure CORS headers to allow frontend Authorization header
- [x] Add health check: GET /health → {"status": "healthy"}

### Phase 6: Documentation, Testing & Final Integration Checks
**Duration:** 1 day
**Tasks:**
- [x] Ensure Swagger UI shows all endpoints with auth lock icon
- [x] Write basic pytest tests using TestClient:
  - [x] Protected endpoints reject missing/invalid tokens
  - [x] CRUD operations enforce user isolation
  - [x] Validation errors return 422
- [x] Update backend README.md:
  - [x] Required .env variables
  - [x] Running commands
  - [x] Example curl requests with JWT
  - [x] Integration notes for frontend
- [x] Verify end-to-end compatibility: endpoints return shapes expected by frontend's api client

## Resources Required
- Development environment with Python 3.8+
- Neon PostgreSQL database instance
- Better Auth configuration for JWT tokens
- Frontend application for integration testing

## Risk Assessment
- **High Risk**: JWT token compatibility with Better Auth - Mitigation: Thorough testing with actual Better Auth tokens
- **Medium Risk**: Database connection issues - Mitigation: Multiple connection retry logic
- **Low Risk**: CORS configuration issues - Mitigation: Proper origin configuration

## Success Criteria
- [x] All 5 Basic Todo features implemented (Add, View/List, Update, Delete, Mark Complete)
- [x] Secure JWT authentication with Better Auth tokens
- [x] Multi-user isolation enforced
- [x] Full compatibility with frontend API client
- [x] Comprehensive error handling
- [x] Proper documentation and testing