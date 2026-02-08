# Full-Stack Todo App with AI Chatbot Integration – Phases II & III (Basic Level)

**Project**: Build a complete full-stack Todo application with multi-user support, persistent storage in Neon PostgreSQL, and integrate an AI-powered chatbot for natural language task management. The chatbot supports all 5 Basic Level features (add, delete, mark complete, list tasks, show user details) using LangChain for agentic logic (adapted from OpenAI Agents SDK patterns) and Cohere API as the LLM backend. The system uses FastAPI backend, Next.js frontend, SQLModel ORM, Neon PostgreSQL database, and Better Auth for authentication. Development is strictly agentic using Spec-Kit Plus + Claude Code workflow — no manual coding allowed.

## Core Principles

- **Agentic spec-driven workflow**: Specs → Plans → Tasks → Implementation via Claude Code
- **Stateless architecture**: All endpoints and tools hold no memory; state (tasks, conversations, messages) persisted in Neon DB
- **Secure multi-user isolation**: Better Auth JWT enforces scoping; every request/tool call validated for user_id ownership
- **Natural & helpful AI**: Understands intent, chains tools, provides confirmations and error handling via Cohere LLM
- **Extensibility**: Designed for future advanced features (due dates, priorities, recurrence)
- **Reviewable process**: All prompts, specs, plans, tasks, and iterations preserved for judging

## Key Standards

### Monorepo Structure
- `.spec-kit/config.yaml`, `specs/` (overview.md, architecture.md, features/task-crud.md, features/authentication.md, features/chatbot.md, api/rest-endpoints.md, api/mcp-tools.md, database/schema.md, ui/components.md, ui/pages.md), CLAUDE.md (root, frontend, backend), frontend/ (Next.js app), backend/ (FastAPI app), docker-compose.yml

### Frontend
- Next.js 16+ (App Router), OpenAI ChatKit UI (hosted, domain allowlist); responsive with Tailwind CSS

### Backend
- Python FastAPI; REST endpoints /api/{user_id}/tasks; chat endpoint /api/{user_id}/chat

### AI Logic
- LangChain agents (adapted from OpenAI Agents SDK patterns) with message history + MCP tool calling; use Cohere API as LLM

### MCP Server
- Official MCP SDK; expose tools: add_task, list_tasks, complete_task, delete_task, update_task (stateless, user-scoped)

### ORM
- SQLModel for models/queries

### Database
- Neon Serverless PostgreSQL; models: User, Task, Conversation (user_id FK, id PK, timestamps), Message (conversation_id FK, role, content, created_at)

### Authentication
- Better Auth with JWT plugin; shared BETTER_AUTH_SECRET; middleware verifies on all endpoints/tools

### Env vars
- StwEoE9fBjw9KDZ32E165ieHf4AnKsTXIWWXJuYzs, DATABASE_URL, BETTER_AUTH_SECRET (shared), NEXT_PUBLIC_OPENAI_DOMAIN_KEY (ChatKit)

### Tools
- Stateless, require/validate user_id, return structured JSON

## Constraints

- No manual coding; all implementation via Claude Code using Spec-Kit Plus workflow
- Stateless server: No in-memory state; everything in DB
- Basic Level: Focus on core task commands + user details
- Security: JWT validation on all requests; no cross-user access
- Performance: Efficient queries with indexes on user_id, conversation_id
- Frontend: ChatKit hosted; domain allowlist required for production; local dev without key

## Success Criteria

- Users signup/signin via Better Auth; manage tasks via responsive UI or chatbot
- Chatbot understands natural language for all Basic tasks + showing user details
- AI agent invokes correct MCP tools (e.g., "add task buy groceries" → add_task)
- Conversation history persisted in DB; resumes after refresh/restart
- Helpful responses with confirmations (e.g., "Task 'Buy groceries' added!")
- Strict user isolation: Separate tasks/conversations per user
- Full integration: ChatKit → FastAPI chat endpoint → LangChain agents (Cohere LLM) → MCP tools → Neon DB
- Runs via docker-compose; ChatKit configured with domain key
- All specs, plans, tasks, and agent outputs preserved in /specs/ for review

## Defined Agents (10 total – Phases II & III)

1. Spec Writer Agent – creates/refines specs
2. Architecture Planner Agent – designs system architecture
3. Backend Engineer Agent – implements FastAPI routes/endpoints
4. Database Engineer Agent – handles SQLModel models/persistence
5. Frontend Engineer Agent – implements general UI
6. Integration Tester Agent – validates full-stack flows
7. MCP Tools Engineer Agent – builds/exposes MCP tools
8. Chatbot Backend Engineer Agent – implements chat endpoint + LangChain agents runner (with Cohere LLM)
9. Frontend Chatbot Engineer Agent – builds/configures ChatKit UI
10. Coordinator Agent – orchestrates all agents, resolves conflicts, ensures workflow adherence

## Governance

This constitution governs the integrated full-stack Todo app with AI chatbot development, using Cohere API for LLM in the agentic workflow.