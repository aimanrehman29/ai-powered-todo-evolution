# Phase III – Plan (high level)

1) DB
   - Add Conversation, Message models & migration.

2) MCP
   - Implement stateless MCP tools for task CRUD (add/list/complete/delete/update) backed by DB.

3) Agent
   - Wire OpenAI Agents SDK runner; map tool calls to MCP server.

4) API
   - POST /api/{user_id}/chat: auth, load history, store user msg, run agent, store assistant msg, return response + tool_calls.

5) Frontend
   - ChatKit UI at /chat; call chat endpoint with JWT + user_id; render history, loading, errors.

6) Config/Deploy
   - Backend env: DATABASE_URL, JWT_SECRET, JWT_EXPIRE_MINUTES, OPENAI_API_KEY, OPENAI_MODEL, CORS for frontend domain.
   - Frontend env: NEXT_PUBLIC_API_BASE, NEXT_PUBLIC_OPENAI_DOMAIN_KEY.

7) Tests
   - Unit tests for MCP tools.
   - Integration: /auth/login + /api/{user_id}/chat happy path.
