# Phase III – Data Models

Conversation
- id (PK, int, autoincrement)
- user_id (int, FK users.id)
- created_at, updated_at (timestamptz)

Message
- id (PK, int, autoincrement)
- user_id (int, FK users.id)
- conversation_id (int, FK conversations.id)
- role (enum: "user" | "assistant")
- content (text)
- created_at (timestamptz)

Notes:
- Retain existing Task model.
- Consider indexes: conversation_id, user_id, created_at for fast retrieval in order.
