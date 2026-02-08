# UI Pages Specification

## Overview
Page structure and routing for the Todo application with authentication flow and task management features.

## Page Structure

### 1. Authentication Pages

#### /signup
- User registration form with email, name, and password
- Form validation and error handling
- Link to login page for existing users
- Success redirect to dashboard after registration
- Responsive layout for all device sizes

#### /login
- User login form with email and password
- Form validation and error handling
- Link to signup page for new users
- Success redirect to dashboard after login
- "Remember me" option for persistent sessions
- Password reset link

### 2. Main Application Pages

#### /dashboard (or /)
- Main task management interface
- Welcome message for authenticated user
- Task creation form at the top
- List of user's tasks with completion status
- Filtering options (all, active, completed)
- Empty state when no tasks exist
- Loading state during data fetch

#### /tasks/[id] (Optional - individual task view)
- Detailed view of a single task
- Edit functionality in place
- Creation/modification timestamps
- Back to dashboard link

### 3. Protected Routes
- All task-related pages require authentication
- Redirect to login if JWT token is invalid/expired
- Preserve intended destination after login

## Page Components Integration

### /signup Page
```
MainLayout
├── Header (minimal - no nav for auth pages)
├── SignupForm
│   ├── Email input
│   ├── Name input
│   ├── Password input
│   ├── Submit button
│   └── Login link
└── Footer
```

### /login Page
```
MainLayout
├── Header (minimal - no nav for auth pages)
├── LoginForm
│   ├── Email input
│   ├── Password input
│   ├── Remember me checkbox
│   ├── Submit button
│   ├── Signup link
│   └── Forgot password link
└── Footer
```

### /dashboard Page
```
MainLayout
├── Header (with user profile dropdown)
├── TaskForm (for creating new tasks)
├── TaskList
│   ├── Filter controls (All/Active/Completed)
│   ├── TaskItem (repeated for each task)
│   │   ├── Completion checkbox
│   │   ├── Task details
│   │   └── Action buttons
│   └── Empty state message
└── Footer
```

## Navigation Structure
- Header navigation for authenticated users
- Mobile-responsive hamburger menu
- Active link highlighting
- Breadcrumb support if needed

## SEO Considerations
- Proper meta tags for each page
- Title tags reflecting page content
- Structured data where appropriate
- Canonical URLs

## Error Handling
- 404 page for non-existent routes
- 500 page for server errors
- Authentication error handling
- Network error states in UI

## Loading States
- Page loading indicators
- Skeleton screens for content areas
- Form submission loading states
- Data fetching indicators

## Data Flow per Page

### /signup
1. User enters registration details
2. Form validation occurs
3. API call to registration endpoint
4. JWT token received and stored
5. Redirect to dashboard

### /login
1. User enters login credentials
2. Form validation occurs
3. API call to login endpoint
4. JWT token received and stored
5. Redirect to dashboard

### /dashboard
1. Verify JWT token validity
2. Fetch user's tasks from API
3. Display tasks in organized list
4. Handle user interactions (create, update, delete)
5. Update UI based on API responses

## URL Structure
- `/signup` - Registration page
- `/login` - Login page
- `/dashboard` or `/` - Main application
- `/tasks/:id` - Individual task view (if implemented)

## Responsive Design
- Mobile-first approach
- Appropriate touch targets (min 44px)
- Responsive typography
- Flexible grid layouts
- Collapsible navigation on small screens

## Performance Requirements
- Fast initial page load (< 3 seconds)
- Efficient data fetching patterns
- Optimized images and assets
- Code splitting for better loading
- Caching strategies for API responses