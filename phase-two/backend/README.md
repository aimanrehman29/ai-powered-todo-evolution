# Backend (Phase II) - FastAPI + SQLModel

## Setup
```bash
cd phase-two/backend
python -m venv .venv
. .venv/Scripts/activate  # PowerShell: .\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
export DATABASE_URL="postgresql+asyncpg://<user>:<pass>@<host>:<port>/<db>"
export JWT_SECRET="<secret>"
export JWT_EXPIRE_MINUTES=60
uvicorn app.main:app --reload
```

Alternatively, copy `.env.example` to `.env`, fill values, and run with:
```bash
uvicorn --env-file .env app.main:app --reload
```

## API Summary
- `POST /auth/signup` — create user (409 on duplicate)
- `POST /auth/login` — OAuth2 form; returns JWT
- `GET /tasks` — list current user tasks (JWT)
- `POST /tasks` — create (title required, status defaults open)
- `GET /tasks/{id}` — fetch own task
- `PATCH /tasks/{id}` — update title/description/status
- `POST /tasks/{id}/toggle` — flip status open/done
- `DELETE /tasks/{id}` — remove task

All protected endpoints expect `Authorization: Bearer <token>`.
