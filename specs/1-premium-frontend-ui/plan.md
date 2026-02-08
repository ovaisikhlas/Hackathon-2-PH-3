# Implementation Plan: Todo Full-Stack Web Application – Phase II: Frontend (Basic Level)

## Technical Context

### Knowns
- **Frontend Framework**: Next.js 16+ with App Router
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth with JWT plugin
- **Backend API**: REST API endpoints for tasks with JWT authentication
- **5 Basic Features**: Add, View/List, Update, Delete, Mark Complete
- **UI Requirements**: Premium aesthetic, responsive design, accessibility
- **Components**: Header, TaskCard, TaskForm, ConfirmationDialog, LoadingSkeleton, EmptyState
- **Pages**: Login, Signup, Dashboard

### Unknowns (NEEDS CLARIFICATION)
(None - all unknowns resolved in research phase)

## Constitution Check

### Code Standards Compliance
- [ ] All code follows TypeScript best practices
- [ ] Type safety is maintained throughout the application
- [ ] Proper error handling is implemented
- [ ] Security best practices for JWT handling are followed
- [ ] Accessibility standards (WCAG 2.1 AA) are met

### Architecture Principles
- [ ] Clean separation of concerns between components
- [ ] Reusable components are created where appropriate
- [ ] State management follows Next.js patterns
- [ ] API calls are centralized in the lib/api.ts module

## Gates

### Gate 1: Architecture Feasibility
- [ ] Next.js App Router can support the required authentication patterns
- [ ] Better Auth integrates properly with Next.js App Router
- [ ] JWT authentication can be properly handled with API calls

### Gate 2: Security Compliance
- [ ] JWT tokens are handled securely
- [ ] Authentication state is properly managed
- [ ] API calls include proper authentication headers

### Gate 3: Design Implementation
- [ ] Tailwind CSS can achieve the required premium aesthetic
- [ ] Responsive design requirements are technically feasible
- [ ] Loading and error states can be properly implemented

## Phase 0: Research & Resolution of Unknowns

### research.md

#### API Endpoint Details
**Decision**: The backend API follows the pattern `/api/{user_id}/tasks` with standard HTTP methods
**Rationale**: This follows REST conventions and allows for proper user data isolation
**Details**:
- GET `/api/{user_id}/tasks` - Get all tasks for user
- POST `/api/{user_id}/tasks` - Create new task
- GET `/api/{user_id}/tasks/{task_id}` - Get specific task
- PUT `/api/{user_id}/tasks/{task_id}` - Update task
- DELETE `/api/{user_id}/tasks/{task_id}` - Delete task
- PATCH `/api/{user_id}/tasks/{task_id}/complete` - Toggle completion status

#### JWT Token Storage
**Decision**: Use Better Auth's default session management with cookies
**Rationale**: Better Auth is designed to handle session management securely with httpOnly cookies by default
**Implementation**: Leverage Better Auth's built-in session handling

#### Color Palette
**Decision**: Use indigo as the primary accent color with a soft neutral gray palette
**Rationale**: Indigo provides a professional, trustworthy appearance that works well for productivity tools
**Details**:
- Primary: indigo-600 (#4f46e5)
- Secondary: gray-100 to gray-900 range
- Success: green-500 (#22c55e)
- Danger: red-500 (#ef4444)

#### Icon Library
**Decision**: Use lucide-react for iconography
**Rationale**: Lucide React provides clean, consistent icons with a professional appearance that fits the premium aesthetic
**Size**: 20x20px for most interface icons

#### Toast Library
**Decision**: Use sonner for toast notifications
**Rationale**: Sonner provides beautiful, accessible toast notifications with good customization options
**Features**: Success, error, and info variants with auto-dismiss

#### Database Schema
**Decision**: Tasks have id, user_id, title, description, completed, created_at, updated_at fields
**Rationale**: This matches the requirements from the backend specification
**Validation**: Title (1-200 chars), Description (max 1000 chars), Completed (boolean)

## Phase 1: Design & Contracts

### data-model.md

#### Task Entity
- **id**: number (primary key)
- **user_id**: number (foreign key to user)
- **title**: string (1-200 characters, required)
- **description**: string (optional, max 1000 characters)
- **completed**: boolean (default: false)
- **created_at**: string (ISO date string)
- **updated_at**: string (ISO date string)

#### User Entity
- **id**: number (primary key)
- **email**: string (unique, required)
- **name**: string (optional)
- **created_at**: string (ISO date string)
- **updated_at**: string (ISO date string)

#### Validation Rules
- Title must be 1-200 characters
- Description must be max 1000 characters
- Completed defaults to false
- Created and updated timestamps are automatically managed

### API Contracts

#### Task Endpoints
```
GET /api/{user_id}/tasks
Response: Task[]
Status: 200

POST /api/{user_id}/tasks
Request: { title: string, description?: string }
Response: Task
Status: 201

PUT /api/{user_id}/tasks/{task_id}
Request: { title: string, description?: string }
Response: Task
Status: 200

DELETE /api/{user_id}/tasks/{task_id}
Response: none
Status: 204

PATCH /api/{user_id}/tasks/{task_id}/complete
Response: Task
Status: 200
```

### quickstart.md

#### Frontend Setup
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Create a `.env.local` file with:
   ```
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   ```
4. Start the development server: `npm run dev`
5. Visit `http://localhost:3000`

#### Required Environment Variables
- `NEXT_PUBLIC_API_BASE_URL` - Base URL for the backend API

## Phase 2: Implementation Approach

### Technology Stack
- Next.js 16+ with App Router
- TypeScript for type safety
- Tailwind CSS for styling
- Better Auth for authentication
- lucide-react for icons
- sonner for toast notifications
- jwt-decode for token manipulation (if needed)

### Component Architecture
- Server Components for initial rendering and authentication checks
- Client Components for interactive elements (forms, checkboxes, modals)
- Reusable UI components for consistent design system

### State Management
- Better Auth for user session state
- React state for form inputs and UI interactions
- SWR or React Query for data fetching and caching (considering Next.js App Router patterns)

## Phase 3: Development Tasks

### Week 1: Authentication Foundation
1. Set up Next.js project with Tailwind CSS
2. Integrate Better Auth for authentication
3. Create login and signup pages
4. Implement protected route wrapper
5. Set up root layout with header

### Week 2: Dashboard & Task Display
1. Create dashboard page with task fetching
2. Implement TaskList component
3. Create LoadingSkeleton component
4. Create EmptyState component
5. Style basic UI elements

### Week 3: Task Operations
1. Create TaskCard component
2. Create TaskForm component
3. Create ConfirmationDialog component
4. Implement CRUD operations
5. Add toast notifications

### Week 4: Polish & Testing
1. Implement responsive design
2. Add accessibility features
3. Error handling and edge cases
4. Performance optimization
5. Testing and documentation