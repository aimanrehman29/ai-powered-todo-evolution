# Task CRUD Operations

## Endpoints
- GET /api/{user_id}/tasks
- POST /api/{user_id}/tasks
- GET /api/{user_id}/tasks/{id}
- PUT /api/{user_id}/tasks/{id}
- DELETE /api/{user_id}/tasks/{id}
- PATCH /api/{user_id}/tasks/{id}/complete

## Rules
- Title required (1-200 chars), description optional.
- Only tasks belonging to authenticated user_id.
- Status: open|done
