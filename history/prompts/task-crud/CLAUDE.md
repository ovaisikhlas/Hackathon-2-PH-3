# Claude Code Rules - Task CRUD Feature

## Feature-Specific Guidelines

**Focus Area:**
- Task creation, reading, updating, deletion, and completion marking
- User-specific task isolation
- Validation and error handling

**Key Standards:**
- Title: 1-200 characters
- Description: optional, max 1000 characters
- User data isolation via user_id filtering
- Proper authentication checks on all endpoints

**Security Considerations:**
- All operations must be scoped to authenticated user
- No cross-user data access allowed
- Proper error responses (401, 403, 404)