# Phase III Guidelines

- Stack: FastAPI + SQLModel + OpenAI Agents SDK + MCP SDK; Frontend ChatKit.
- Auth: current JWT acceptable short-term; plan Better Auth alignment later.
- Routes: `/api/{user_id}/chat` only for chat; tasks via MCP tools.
- DB: Conversation, Message tables; truncate history per request to keep tokens manageable.
- Env: DATABASE_URL, JWT_SECRET, OPENAI_API_KEY, OPENAI_MODEL, NEXT_PUBLIC_API_BASE, NEXT_PUBLIC_OPENAI_DOMAIN_KEY.
- CORS: allow Vercel domain.
- Workflow: read specs in /specs, implement per plan/tasks, keep code clean and modular.
