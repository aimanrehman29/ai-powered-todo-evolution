# Phase III – MCP Tools Specification (stateless)

Tools (all must validate user_id and task ownership):
- `add_task(user_id: str, title: str, description?: str) -> {task_id, status, title}`
- `list_tasks(user_id: str, status?: "all"|"pending"|"completed") -> [tasks]`
- `complete_task(user_id: str, task_id: int) -> {task_id, status, title}`
- `delete_task(user_id: str, task_id: int) -> {task_id, status, title}`
- `update_task(user_id: str, task_id: int, title?: str, description?: str) -> {task_id, status, title}`

Rules:
- Stateless: tools do not store memory; all state is in DB via SQLModel.
- Errors: task not found -> raise descriptive error; invalid status -> 400-equivalent.
- Input trimming: title must be non-empty after trim; max lengths enforced by model.

Return shapes should be minimal, confirming action and echoing title.
