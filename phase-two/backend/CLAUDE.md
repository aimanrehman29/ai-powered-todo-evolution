# Backend Guidelines
- FastAPI + SQLModel
- Routes under /auth and /api/{user_id}/tasks
- Require JWT bearer; sub=user_id
- Use AsyncSession via get_db
- Env: DATABASE_URL, JWT_SECRET, JWT_EXPIRE_MINUTES, BETTER_AUTH_SECRET (same as JWT_SECRET)

Run:
uvicorn --env-file .env app.main:app --reload
