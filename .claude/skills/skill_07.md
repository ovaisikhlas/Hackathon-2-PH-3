# MCP Server Setup Skill

## Description
Set up and configure the full MCP server using the Official MCP SDK, including endpoint registration, tool discovery, authentication enforcement (JWT middleware), request/response handling, and integration with FastAPI.

## Assigned to
MCP Tools Engineer Agent

## Usage
- Initialize MCP server in FastAPI (e.g., /mcp endpoint or integrated)
- Register all 5 tools with MCP SDK
- Apply JWT middleware to protect MCP requests
- Handle MCP protocol messages (tool discovery, invocation, result return)
- Ensure stateless execution (no server-side state)
- Test MCP server independently (e.g., via curl or MCP client)
- Document setup in @specs/api/mcp-tools.md