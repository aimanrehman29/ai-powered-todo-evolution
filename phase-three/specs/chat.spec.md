# Phase III – Chat Endpoint Specification

Endpoint: `POST /api/{user_id}/chat`

Request:
- `conversation_id` (int, optional) – if absent, create a new conversation for this user
- `message` (string, required) – user’s message

Response:
- `conversation_id` (int)
- `response` (string) – assistant reply
- `tool_calls` (array) – MCP tool calls executed

Behavior:
1) Authenticate via Bearer JWT; reject if token user_id ≠ path user_id.
2) Load conversation + messages for user_id; if conversation_id missing, create one.
3) Store the user message in DB.
4) Run OpenAI Agent (Agents SDK) with MCP tools registered.
5) Store assistant response in DB.
6) Return response + tool_calls. No server-side session state; each request is self-contained.

Errors:
- 401 no/invalid token
- 403 user mismatch
- 404 conversation_id not found for this user
- 500 tool/agent failure (include friendly message)

Notes:
- Truncate history to reasonable limit (e.g., last 20 messages) per request to control tokens.
- Respect rate limits and timeouts on the agent run.
