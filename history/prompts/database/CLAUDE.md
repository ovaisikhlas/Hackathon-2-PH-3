# Claude Code Rules - Database Schema

## Feature-Specific Guidelines

**Focus Area:**
- SQLModel database models
- PostgreSQL schema design
- Indexing strategy
- Data relationships

**Key Standards:**
- Neon Serverless PostgreSQL compatibility
- Proper indexing on user_id and completed fields
- Foreign key relationships with cascade delete
- Validation constraints

**Security Considerations:**
- Referential integrity through foreign keys
- Data isolation through user_id filtering
- Proper constraint enforcement
- Safe query patterns to prevent injection