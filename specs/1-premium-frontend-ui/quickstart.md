# Frontend Quickstart Guide

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Backend API running (typically on http://localhost:8000)

## Setup Instructions

### 1. Clone and Navigate
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
# or
yarn install
```

### 3. Environment Configuration
Create a `.env.local` file in the frontend root directory:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
```

### 4. Run Development Server
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

## Key Files and Directories

### Core Application Structure
- `app/` - Next.js App Router pages and layouts
- `lib/` - Shared utilities, API client, and types
- `components/` - Reusable UI components
- `types/` - TypeScript type definitions

### Important Files
- `app/layout.tsx` - Root layout with authentication check
- `app/login/page.tsx` - Login page component
- `app/signup/page.tsx` - Signup page component
- `app/dashboard/page.tsx` - Main dashboard with task list
- `lib/api.ts` - Centralized API client with JWT handling
- `components/TaskCard.tsx` - Individual task display component
- `components/TaskForm.tsx` - Task creation/editing form
- `components/ProtectedRoute.tsx` - Authentication wrapper

## API Integration

### Base URL Configuration
The application uses `NEXT_PUBLIC_API_BASE_URL` from environment variables to connect to the backend API.

### Authentication Flow
1. User authenticates via Better Auth
2. Session token is stored securely
3. All API requests automatically include the JWT token in the Authorization header
4. Unauthorized requests are redirected to the login page

### Available API Functions
In `lib/api.ts`:
- `getTasks(userId)` - Fetch all tasks for a user
- `createTask(userId, taskData)` - Create a new task
- `updateTask(userId, taskId, taskData)` - Update an existing task
- `deleteTask(userId, taskId)` - Delete a task
- `toggleTaskComplete(userId, taskId)` - Toggle task completion status

## Running Tests
```bash
npm run test
# or for watch mode
npm run test:watch
```

## Building for Production
```bash
npm run build
npm run start
```

## Troubleshooting

### Common Issues
1. **API Connection Errors**: Verify `NEXT_PUBLIC_API_BASE_URL` is set correctly and backend is running
2. **Authentication Issues**: Ensure Better Auth is properly configured on both frontend and backend
3. **Environment Variables**: Make sure all required environment variables are set in `.env.local`

### Development Tips
- Use `console.log` statements to debug API calls
- Check browser developer tools for network requests and errors
- Ensure backend API endpoints are accessible from frontend origin