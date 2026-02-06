# Implementation Plan: Full-Stack Todo Application (Phase II)

**Branch**: `[phase-two-fullstack]` | **Date**: 2026-02-04 | **Spec**: phase-two/specs/spec.md  
**Input**: Feature specification from `/phase-two/specs/spec.md`

## Summary
Deliver a full-stack Todo app with Next.js (TypeScript, Tailwind) frontend and FastAPI backend backed by Neon Postgres. Users sign up/log in to receive JWTs, and all task CRUD is scoped to the authenticated user. API contracts are JSON, with consistent error shapes. Frontend consumes the REST API and provides responsive, accessible UI for auth and task management.

## Technical Context
**Language/Version**: Frontend: TypeScript/Next.js; Backend: Python 3.13/FastAPI  
**Primary Dependencies**: Next.js, React, Tailwind CSS; FastAPI, SQLModel, Pydantic, PyJWT (or equivalent), async DB driver (asyncpg)  
**Storage**: Neon Serverless PostgreSQL (tasks, users)  
**Testing**: Backend: pytest + httpx/fastapi.testclient; Frontend: Playwright or Cypress for happy-path UI; unit tests where feasible  
**Target Platform**: Web frontend (desktop/mobile), backend deployable to cloud with HTTPS termination  
**Project Type**: Full-stack (separate frontend and backend directories)  
**Performance Goals**: p95 API latency <200ms for CRUD under nominal load; responsive UI under 200ms interactions for basic operations  
**Constraints**: JWT-protected APIs, user isolation, responsive UI, migrations required for schema changes

## Constitution Check
- User isolation enforced via user_id scoping on all task queries.
- Security: JWT required on protected endpoints; hashed passwords; env-based secrets/DB URL.
- Separation: frontend/backend/db concerns decoupled with explicit API contracts.
- Responsiveness: Tailwind-based responsive layout; accessible components.
- Stateless auth: JWT with expiry; avoid server-side sessions.

## Project Structure

```text
phase-two/
├─ frontend/                 # Next.js app
│  ├─ app/ or pages/         # routes: /login, /signup, /tasks, /task/[id]
│  ├─ components/            # UI components (forms, task list, layout)
│  ├─ lib/api.ts             # API client (JWT header handling)
│  ├─ styles/                # Tailwind config
│  └─ tests/                 # UI/integration tests (Playwright/Cypress)
├─ backend/                  # FastAPI app
│  ├─ app/
│  │  ├─ main.py             # ASGI app, routes include auth/tasks
│  │  ├─ models.py           # SQLModel models: User, Task
│  │  ├─ schemas.py          # Pydantic schemas for I/O
│  │  ├─ auth.py             # JWT utilities, password hashing
│  │  ├─ deps.py             # dependencies (auth, DB session)
│  │  ├─ routes/
│  │  │  ├─ auth.py          # /auth/signup, /auth/login
│  │  │  └─ tasks.py         # /tasks CRUD scoped to user
│  │  └─ db.py               # DB engine/session, migrations hook
│  ├─ tests/                 # pytest-based tests (auth + tasks)
│  └─ migrations/            # Alembic/SQLModel migrations
└─ specs/
   ├─ spec.md
   ├─ plan.md
   └─ tasks.md (pending)
```

**Structure Decision**: Split frontend and backend into separate directories to keep concerns isolated and match deployment targets.

## Implementation Steps

1) **Backend Foundations**
   - Initialize FastAPI app, DB connection (Neon via asyncpg/SQLModel), Alembic/SQLModel migrations.
   - Define models: User (id, email unique, password_hash, created_at), Task (id, user_id FK, title, description, status, timestamps).
   - Define schemas: request/response DTOs with consistent error shapes.

2) **Auth**
   - Password hashing (e.g., passlib/bcrypt); JWT generation/verification (secret, expiry).
   - Routes: `/auth/signup` (create user, 409 on duplicate), `/auth/login` (issue JWT).
   - Dependency to extract user from Authorization: Bearer token; return 401 on invalid/expired.

3) **Task CRUD**
   - Routes under `/tasks`: POST create (status default `open`), GET list (user-scoped), GET by id (404 if not owner), PATCH update/toggle, DELETE remove.
   - Enforce user_id filtering on all queries; return 404 for cross-user access.

4) **Frontend**
   - Pages: `/login`, `/signup`, `/tasks` (list/create inline), `/task/[id]` (detail/edit) or modal-based edit.
   - API client wraps fetch with base URL and Authorization header from stored JWT (e.g., localStorage).
   - Responsive layout with Tailwind; accessible forms and buttons; loading/error states.

5) **Error Handling & UX**
   - Backend: JSON error shape `{code, message}` with appropriate status codes (400/401/403/404/409/500).
   - Frontend: surface errors inline on forms; handle token expiry by redirecting to login.

6) **Testing & Tooling**
   - Backend: pytest covering auth success/failure, task CRUD scoping, validation errors.
   - Frontend: at least one happy-path auth+CRUD flow (Playwright/Cypress) and key component tests if feasible.
   - Lint/format: Prettier/ESLint for frontend; ruff/black (or isort) for backend.

## Complexity Tracking
No additional complexity beyond constitution; separation of frontend/backend chosen for clarity and deployment readiness.
