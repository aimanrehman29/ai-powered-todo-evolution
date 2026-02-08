# Phase III – Tasks

- T1 DB: add Conversation and Message models/migration (SQLModel).
- T2 MCP: implement task tools (add/list/complete/delete/update) via MCP SDK.
- T3 Agent runner: configure OpenAI Agents SDK; tool calling wired to MCP.
- T4 API: POST /api/{user_id}/chat (stateless history fetch/store, run agent).
- T5 Frontend: ChatKit UI (/chat), chat API client with JWT + user_id, show history.
- T6 Deploy config: set HF env (DB, JWT_SECRET, OPENAI_API_KEY, etc.) and Vercel env (API_BASE, DOMAIN_KEY).
