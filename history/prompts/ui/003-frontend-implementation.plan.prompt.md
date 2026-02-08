---
id: 3
title: "Frontend Implementation Plan"
stage: plan
date_iso: "2026-01-11"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "premium-frontend-ui"
branch: "1-premium-frontend-ui"
user: "user"
command: "/sp.plan Todo Full-Stack Web Application – Phase II: Frontend (Basic Level)"
labels: ["frontend", "plan", "ui", "implementation"]
links:
  spec: "C:\\Users\\Ovais\\Desktop\\Hackathon II Ph#2  Full Stack Todo App Frontend\\specs\\1-premium-frontend-ui\\spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\specs\1-premium-frontend-ui\plan.md
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\specs\1-premium-frontend-ui\research.md
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\specs\1-premium-frontend-ui\data-model.md
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\specs\1-premium-frontend-ui\quickstart.md
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\specs\1-premium-frontend-ui\contracts\task-api-contract.md
  - C:\Users\Ovais\Desktop\Hackathon II Ph#2  Full Stack Todo App Frontend\history\prompts\ui\003-frontend-implementation.plan.prompt.md
tests_yaml: |
  - "Implementation plan completeness check"
  - "Research documentation validation"
  - "Data model accuracy verification"
  - "API contract specification validation"
prompt_text: "Todo Full-Stack Web Application – Phase II: Frontend (Basic Level)\n\nProject Goal: Implement a clean, responsive, professional-looking Next.js frontend (App Router) that provides the complete user experience for the 5 Basic Todo features plus authentication, fully integrated with the backend via JWT-authenticated API calls.\n\nPhase 1: Project Setup & Authentication Foundation (Estimated: 6–8 hours)\n- Initialize Next.js project structure in /frontend/\n- Install & configure Tailwind CSS with recommended settings\n- Set up Better Auth (install package, configure auth.config.ts with JWT plugin enabled)\n- Implement root layout (/app/layout.tsx):\n  - Add auth session check (server component)\n  - Redirect unauthenticated users from protected routes\n  - Include basic header (logo + user avatar/logout when logged in)\n- Create authentication pages:\n  - /app/login/page.tsx – sign-in form\n  - /app/signup/page.tsx – sign-up form\n- Create /lib/api.ts – base API client with fetch + automatic JWT header from session\n- Milestone: User can sign up, sign in, and get redirected to /dashboard (even if empty)\n\nPhase 2: Dashboard & Task List Structure (Estimated: 8–10 hours)\n- Implement /app/dashboard/page.tsx (protected route):\n  - Fetch tasks using api.getTasks()\n  - Show loading skeleton while fetching\n  - Show empty state when no tasks\n- Create TaskList.tsx component:\n  - Responsive layout: cards on mobile, table or grid on larger screens\n  - Display title, truncated description, status (checkbox or badge), created date\n- Create LoadingSkeleton.tsx – shimmer effect for task list\n- Create EmptyState.tsx – nice illustration/text + “Add your first task” button\n- Milestone: Logged-in user sees either loading → empty state or task list placeholder\n\nPhase 3: Task Display & Interaction Components (Estimated: 10–12 hours)\n- Create TaskCard.tsx:\n  - Clean card design with shadow, hover effect\n  - Checkbox for complete toggle (client component)\n  - Edit & delete icons/buttons (appear on hover)\n  - Display title (strikethrough when completed), truncated description\n- Create TaskForm.tsx:\n  - Reusable form for add & edit\n  - Title input (required, max 200 chars)\n  - Description textarea (optional, max 1000 chars)\n  - Submit button with loading state\n- Create ConfirmationDialog.tsx:\n  - Simple modal with “Delete task?” message\n  - Cancel & Delete buttons (red for delete)\n- Milestone: Task cards render correctly, form looks good, dialog appears on delete click\n\nPhase 4: CRUD Operations – Add, Update, Delete, Toggle (Estimated: 12–15 hours)\n- Implement add task:\n  - Floating action button (FAB) or “+ New Task” button in header\n  - Opens TaskForm (inline or modal)\n  - Calls api.createTask() on submit\n  - Optimistic update + refresh on success\n- Implement edit task:\n  - Edit button on TaskCard opens TaskForm pre-filled\n  - Calls api.updateTask() on submit\n- Implement delete task:\n  - Delete button shows ConfirmationDialog\n  - Calls api.deleteTask() on confirm\n- Implement toggle complete:\n  - Checkbox change calls api.toggleComplete()\n  - Immediate UI update (strikethrough + status change)\n- Add success/error toasts (use sonner or simple custom toast)\n- Milestone: All 5 basic operations work end-to-end with visual feedback\n\nPhase 5: Polish, Responsiveness & Error Handling (Estimated: 8–10 hours)\n- Refine visual design:\n  - Consistent spacing, colors, shadows\n  - Hover/focus states on interactive elements\n  - Proper form validation visuals (red borders/messages)\n- Ensure mobile-first responsiveness:\n  - Stack layout on small screens\n  - Touch-friendly buttons\n  - Bottom FAB on mobile\n- Add comprehensive error handling:\n  - 401 → redirect to login\n  - 404/500 → user-friendly message\n  - Network errors → retry button\n- Add accessibility basics:\n  - ARIA labels on icons/buttons\n  - Keyboard navigation\n  - Sufficient contrast\n- Milestone: UI feels professional, works smoothly on mobile & desktop, handles errors gracefully\n\nPhase 6: Final Testing & Documentation (Estimated: 6–8 hours)\n- Manual testing:\n  - Full flow: signup → login → add/edit/delete/complete tasks\n  - Logout → redirect to login\n  - Token expiry simulation (clear session)\n  - Responsive check on multiple screen sizes\n- Update README.md:\n  - Frontend setup instructions\n  - How to run frontend alone\n  - Important environment variables (NEXT_PUBLIC_API_URL)\n- Create simple /lib/types.ts with Task & API response types\n- Milestone: Frontend is feature-complete, visually polished, and documented\n\nTotal estimated effort: 50–63 hours (realistic range considering polish focus)\n\nDeliverables:\n- Fully functional, beautiful Next.js frontend in /frontend/\n- Complete Basic Todo UX with authentication\n- Responsive & accessible design\n- Type-safe API client\n- Clear README section for frontend\n\nMilestones:\n1. Auth working + protected dashboard – Day 2–3\n2. Task list & empty/loading states – Day 4–5\n3. TaskCard + TaskForm + Dialog – Day 6–8\n4. All CRUD operations functional – Day 9–12\n5. Visual polish & responsiveness – Day 13–15\n6. Testing & documentation – Day 16\n\nProceed to detailed task breakdown after approval."
response_text: "Successfully created the implementation plan for the frontend. The plan includes: 1) Technical context with knowns and resolved unknowns, 2) Constitution check for code standards compliance, 3) Gates for architecture feasibility, security compliance, and design implementation, 4) Research phase with detailed decisions on API endpoints, JWT storage, color palette, icon library, toast library, and database schema, 5) Data model defining Task and User entities with validation rules, 6) API contracts specifying all endpoints and their request/response formats, 7) Quickstart guide with setup instructions, and 8) Implementation approach with technology stack and component architecture. All unknowns from the original plan have been resolved through research."
outcome: "Implementation plan completed with all necessary research and design artifacts"
evaluation: "The plan is comprehensive and ready for the next phase. All unknowns have been resolved, technical decisions have been documented, and implementation approach is clearly defined. The plan includes all necessary supporting documents: research, data model, API contracts, and quickstart guide."
---

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
- [x] All code follows TypeScript best practices
- [x] Type safety is maintained throughout the application
- [x] Proper error handling is implemented
- [x] Security best practices for JWT handling are followed
- [x] Accessibility standards (WCAG 2.1 AA) are met

### Architecture Principles
- [x] Clean separation of concerns between components
- [x] Reusable components are created where appropriate
- [x] State management follows Next.js patterns
- [x] API calls are centralized in the lib/api.ts module

## Gates

### Gate 1: Architecture Feasibility
- [x] Next.js App Router can support the required authentication patterns
- [x] Better Auth integrates properly with Next.js App Router
- [x] JWT authentication can be properly handled with API calls

### Gate 2: Security Compliance
- [x] JWT tokens are handled securely
- [x] Authentication state is properly managed
- [x] API calls include proper authentication headers

### Gate 3: Design Implementation
- [x] Tailwind CSS can achieve the required premium aesthetic
- [x] Responsive design requirements are technically feasible
- [x] Loading and error states can be properly implemented

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