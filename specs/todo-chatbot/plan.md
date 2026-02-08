# Implementation Plan: Todo Chatbot Integration (Phase III)

## Overview
This plan outlines the implementation of the AI chatbot integration for the Todo application, extending the Phase II full-stack application with a conversational interface using Google Gemini API and LangChain.

## Technical Context
- Frontend: Next.js 16+ with App Router and Tailwind CSS
- Backend: FastAPI with SQLModel ORM
- Database: Neon PostgreSQL (reuse Phase II schema)
- Authentication: Better Auth with JWT
- AI: Google Gemini API via langchain-google-genai
- Agent Framework: LangChain with tool calling capabilities

## Architecture
- Frontend: Floating chatbot icon with expandable conversation panel
- Backend: Stateful chat endpoint with conversation persistence
- AI Layer: LangChain agent with Gemini LLM and custom tools
- Database: Extended schema with Conversation and Message tables

## Implementation Steps

### 1. Database Extensions
- [ ] Add Conversation model (user_id FK, id PK, timestamps)
- [ ] Add Message model (conversation_id FK, role, content, timestamps)
- [ ] Update existing models to support chat functionality if needed

### 2. Backend Implementation
- [ ] Create JWT middleware for chat endpoint authentication
- [ ] Implement chat endpoint: POST /api/{user_id}/chat
- [ ] Set up LangChain agent with Google Gemini
- [ ] Create MCP-style tools (add_task, list_tasks, complete_task, delete_task, update_task)
- [ ] Implement conversation history retrieval and storage
- [ ] Add error handling and validation

### 3. Frontend Implementation
- [ ] Add floating chatbot icon component (bottom-right, fixed position)
- [ ] Create conversation panel/modal component
- [ ] Implement message display with user/assistant differentiation
- [ ] Add message input field with send functionality
- [ ] Integrate with JWT-authenticated chat endpoint
- [ ] Add loading indicators and error handling
- [ ] Style to match Phase II design language

### 4. AI Integration
- [ ] Configure Google Gemini API access
- [ ] Set up LangChain agent with tool calling
- [ ] Implement natural language processing for task commands
- [ ] Create helpful response generation
- [ ] Add confirmation messages for actions

### 5. Testing and Validation
- [ ] Unit tests for backend endpoints
- [ ] Integration tests for AI tool calling
- [ ] Frontend component tests
- [ ] End-to-end flow testing
- [ ] Security validation (JWT enforcement)

## Dependencies to Install
- Frontend: @google/generative-ai (if needed for client-side), react-icons for chat icon
- Backend: langchain, langchain-google-genai, google-generativeai, pydantic

## Environment Variables
- GEMINI_API_KEY: Google Gemini API key
- DATABASE_URL: Neon PostgreSQL connection string
- BETTER_AUTH_SECRET: Shared secret for JWT validation

## Known Challenges
- Ensuring proper JWT validation on chat endpoint
- Managing conversation state between frontend and backend
- Proper error handling for AI responses
- Matching UI/UX with existing Phase II design

## Success Metrics
- Floating chatbot icon appears and functions correctly
- Natural language commands work for all 5 basic task operations
- Conversation history persists across sessions
- Proper user isolation maintained
- AI responses are helpful and accurate