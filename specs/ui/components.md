# UI Components Specification

## Overview
Reusable UI components for the Todo application with responsive design and proper authentication integration.

## Core Components

### 1. Auth Components
#### AuthProvider
- Context provider for authentication state
- Handles JWT token storage and retrieval
- Provides authentication status to child components
- Manages user session state

#### LoginForm
- Email and password input fields
- Form validation for email format and required fields
- Loading state during authentication
- Error messaging for failed attempts
- Link to signup page

#### SignupForm
- Email, name, and password input fields
- Form validation for email format, password strength, and required fields
- Loading state during registration
- Error messaging for failed attempts
- Link to login page

### 2. Layout Components
#### Header
- Navigation links (Dashboard, Profile, Settings)
- User profile dropdown with logout option
- Responsive mobile menu toggle
- Branding/logo area

#### MainLayout
- Responsive grid layout container
- Sidebar navigation (mobile collapse)
- Main content area with consistent padding
- Footer area

#### ProtectedRoute
- Higher-order component for route protection
- Redirects unauthenticated users to login
- Checks JWT token validity
- Preserves intended destination

### 3. Task Components
#### TaskForm
- Title input field (required, 1-200 chars)
- Description textarea (optional, max 1000 chars)
- Submit button with loading state
- Form validation and error messaging
- Cancel button to discard changes

#### TaskItem
- Checkbox for completion status
- Task title with strikethrough when completed
- Task description (truncated if long)
- Created date display
- Action buttons (Edit, Delete)
- Hover effects for interactivity

#### TaskList
- Container for multiple TaskItem components
- Empty state message when no tasks
- Loading state during data fetch
- Refresh capability
- Sort controls (by date, status)

#### TaskActions
- Edit button with modal/popup
- Delete button with confirmation
- Complete/incomplete toggle
- Responsive design for mobile

### 4. Utility Components
#### LoadingSpinner
- Visual indicator for loading states
- Accessible loading message
- Consistent styling across the app

#### ErrorMessage
- Consistent error message display
- Dismissible error alerts
- Color-coded severity levels
- Proper accessibility attributes

#### Modal
- Reusable modal component
- Overlay background
- Close functionality (X button, escape key, backdrop click)
- Accessible focus management

## Styling Guidelines
- Use Tailwind CSS utility classes consistently
- Follow a consistent color palette
- Maintain proper spacing and typography hierarchy
- Ensure adequate contrast for accessibility
- Mobile-first responsive design approach

## Responsive Design
- Mobile (max-width: 640px): Single column layout
- Tablet (640px - 1024px): Two-column layout possible
- Desktop (min-width: 1024px): Multi-column layout

## Accessibility Requirements
- Proper semantic HTML structure
- ARIA labels for interactive elements
- Keyboard navigation support
- Screen reader compatibility
- Focus management for modals and forms

## State Management
- Component-local state for form inputs
- Context API for authentication state
- Global state management for tasks if needed
- Proper error boundary implementation

## Event Handling
- Form submission with proper validation
- Click handlers with loading states
- Keyboard event support (Enter, Escape)
- Proper event propagation handling

## Performance Considerations
- Memoization of expensive components
- Lazy loading for non-critical components
- Efficient re-rendering patterns
- Code splitting for large components