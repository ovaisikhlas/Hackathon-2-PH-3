# Todo Full-Stack Web Application – Phase III: AI Chatbot Integration (Basic Level)

Target audience: Logged-in users who want to manage their personal todos through natural language conversation via a beautiful, floating chatbot UI — in addition to the existing Phase II web interface.

Focus: Extend the Phase II full-stack Todo application with a conversational AI chatbot that allows users to perform all 5 Basic Level features (add task, list tasks, mark complete, update task, delete task) + show logged-in user details using natural language commands. Use Google Gemini API as the LLM, LangChain for agentic tool-calling logic (OpenAI Agents SDK-like pattern), MCP-style stateless tools exposed via FastAPI, persistent conversation state in Neon DB, and a floating chatbot icon in the frontend UI.

## Success criteria:
- Floating chatbot icon appears in Phase II dashboard (bottom-right, toggleable)
- Clicking icon opens ChatKit-style conversation panel (or modal) with input field
- Chatbot understands natural language commands for all Basic tasks + user details
- All tool calls are user-scoped (validated by Better Auth JWT)
- Conversation history persisted in Neon DB (Conversation + Message models)
- Stateless backend: /api/{user_id}/chat endpoint holds no memory
- AI responses are helpful, confirmatory, and error-resilient
- Full integration: Chatbot → FastAPI chat endpoint → LangChain agent (Gemini LLM) → MCP-style tools → Neon DB (reusing Phase II Task model)
- Responsive & premium UI: Matches Phase II Tailwind design language
- Secure: JWT required for chat requests; no cross-user access

## Constraints:
- Frontend: Next.js 16+ (App Router), Tailwind CSS, integrate floating chatbot icon + conversation UI
- Backend: FastAPI; chat endpoint /api/{user_id}/chat (POST)
- AI: Google Gemini API (gemini-1.5-flash or gemini-1.5-pro) via google-generativeai SDK + LangChain for agent/tool-calling
- Tools: Stateless, MCP-style (add_task, list_tasks, complete_task, delete_task, update_task), exposed via FastAPI
- Database: Reuse Phase II Task model; add Conversation (user_id FK, id PK, timestamps), Message (conversation_id FK, role, content, timestamps)
- Auth: Better Auth JWT; middleware verifies token on chat endpoint
- Env vars: GEMINI_API_KEY (Google), DATABASE_URL, BETTER_AUTH_SECRET
- No real-time (WebSockets); simple request-response chat
- Basic Level only – no advanced features (due dates, priorities, multi-turn reasoning)

## Required frontend additions (Phase II extension):
- Floating chatbot icon (bottom-right, fixed, animated on hover)
- Conversation panel/modal (opens on icon click): input field, message bubbles (user/assistant), loading indicator
- Display logged-in user name/email in chat header
- Persist conversation_id in localStorage/session for resume
- Send messages to /api/{user_id}/chat with JWT Bearer header

## Required backend additions (Phase II extension):
- Chat endpoint: POST /api/{user_id}/chat (body: {conversation_id?: int, message: string})
- LangChain agent setup: Gemini LLM + tool calling (OpenAI-style pattern)
- MCP-style tools exposed via FastAPI (e.g., /mcp endpoint or internal)
- 5 tools: add_task, list_tasks, complete_task, delete_task, update_task (as defined)
- Persist user message + assistant response in Message table
- Reuse Phase II JWT middleware for user_id extraction

## Not building in this specification:
- Advanced multi-turn reasoning or memory beyond DB history
- Real-time streaming responses (simple request-response)
- Voice input/output
- Custom LLM fine-tuning

This specification defines the AI chatbot layer that integrates seamlessly with the Phase II full-stack Todo app, using Google Gemini + LangChain agents and a floating chatbot UI icon.

## Summary of Key Changes / Integration Points

LLM: Replaced OpenAI/Cohere with Google Gemini (via google-generativeai + LangChain)
Agent Framework: LangChain (agent + tools pattern — very similar to OpenAI Agents SDK)
Frontend: Floating chatbot icon + conversation panel added to Phase II dashboard
Backend: New chat endpoint + LangChain agent runner + MCP-style tools
Tools: Same 5 tools as before (add/list/complete/delete/update), but implemented with Gemini compatibility
DB: Reuses Task model + adds Conversation/Message for history