// CLAUDE.md for frontend
# Claude Code Rules - Frontend

## Frontend Development Guidelines

**Technology Stack:**
- Next.js 16+ with App Router
- TypeScript
- Tailwind CSS
- Better Auth for authentication
- API client in `/lib/api.ts` for JWT-attached calls

**File Structure:**
- `app/` - Next.js App Router pages and layouts
- `lib/` - Shared utilities and API client
- `components/` - Reusable UI components
- `types/` - TypeScript type definitions

**Development Standards:**
- Server Components by default for initial rendering
- Client Components only when interactivity is needed
- Proper authentication state management
- JWT token handling and API integration
- Responsive design with Tailwind CSS
- Type safety with TypeScript interfaces

**Security:**
- Secure JWT token storage and transmission
- Proper authentication checks on protected routes
- Input validation and sanitization
- Prevention of cross-site scripting (XSS)

**Performance:**
- Efficient data fetching patterns
- Component memoization when appropriate
- Code splitting for large components
- Proper loading and error state handling