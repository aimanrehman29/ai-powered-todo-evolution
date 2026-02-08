# Phase III Backend (Chat + MCP)

Run locally
```
cd phase-three/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Env vars (required)
- DATABASE_URL
- JWT_SECRET
- JWT_EXPIRE_MINUTES
- OPENAI_API_KEY (now used for Gemini key per user)
- OPENAI_MODEL (default gemini-2.5-flash)

API
- POST /api/{user_id}/chat  (stateless chat; stores messages; uses OpenAI Agents SDK + MCP tools)

Notes
- Auth is stubbed; wire real JWT/Better Auth before production.
- MCP tools and agent runner are placeholders; refine schemas and error handling as you integrate. Gemini tool-calling is not wired yet; tool_calls will be empty.
