# Database Schema Specification

## Overview
Database schema for the Todo application using Neon Serverless PostgreSQL with proper indexing for performance.

## Database System
- Type: Neon Serverless PostgreSQL
- Connection: Environment-based configuration
- ORM: SQLModel for database operations

## Tables

### 1. Users Table (Managed by Better Auth)
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Fields:**
- `id`: Primary key, auto-incrementing integer
- `email`: Unique user identifier, required
- `name`: User's display name, optional
- `created_at`: Timestamp of account creation
- `updated_at`: Timestamp of last account update

**Indexes:**
- Primary key index on `id`
- Unique index on `email`

### 2. Tasks Table
```sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Fields:**
- `id`: Primary key, auto-incrementing integer
- `user_id`: Foreign key referencing users table, required
- `title`: Task title, 1-200 characters, required
- `description`: Task description, optional, max 1000 characters
- `completed`: Boolean indicating completion status, defaults to false
- `created_at`: Timestamp of task creation
- `updated_at`: Timestamp of last task update

**Indexes:**
- Primary key index on `id`
- Foreign key index on `user_id` (critical for user isolation queries)
- Index on `completed` (for filtering completed/incomplete tasks)

## Indexes

### Required Indexes
```sql
-- Index on tasks.user_id for efficient user-based queries
CREATE INDEX idx_tasks_user_id ON tasks(user_id);

-- Index on tasks.completed for efficient status-based queries
CREATE INDEX idx_tasks_completed ON tasks(completed);
```

### Additional Recommended Indexes
```sql
-- Composite index for common queries (user_id and completion status)
CREATE INDEX idx_tasks_user_id_completed ON tasks(user_id, completed);

-- Index on created_at for chronological ordering
CREATE INDEX idx_tasks_created_at ON tasks(created_at);
```

## Constraints

### Primary Keys
- `users.id` - Primary key
- `tasks.id` - Primary key

### Foreign Keys
- `tasks.user_id` references `users.id` with cascade delete

### Unique Constraints
- `users.email` - Unique constraint

### Check Constraints
- `tasks.title` length: 1-200 characters
- `tasks.description` length: max 1000 characters

## Relationships
- One-to-many relationship between users and tasks
- Each user can have zero or many tasks
- Tasks are automatically deleted when user is deleted (CASCADE)

## Security Considerations
- Foreign key constraints ensure referential integrity
- CASCADE DELETE ensures data cleanup when users are removed
- Indexes on user_id enable efficient user isolation
- No direct access to other users' data possible through schema

## Performance Considerations
- Index on user_id essential for user isolation queries
- Index on completed status for filtering
- Proper normalization prevents data duplication
- Timestamps enable audit trails and sorting

## Migration Strategy
- Use SQLModel's migration capabilities
- Maintain backward compatibility during schema evolution
- Test migrations thoroughly in staging environment
- Backup before production schema changes