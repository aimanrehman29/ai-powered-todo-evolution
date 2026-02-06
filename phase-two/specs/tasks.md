---

description: "Tasks for Phase II full-stack Todo application"
---

# Tasks: Phase II Full-Stack

**Input**: phase-two/specs/spec.md, phase-two/specs/plan.md  
**Prerequisites**: Phase II constitution, clarifications on JWT transport and auth UX

## Phase 0: Setup & Tooling
- [ ] P0-01 [P] Initialize backend (FastAPI/SQLModel) scaffold under `backend/`; configure lint/format (ruff/black).
- [ ] P0-02 [P] Initialize frontend (Next.js + Tailwind) scaffold under `frontend/`; configure ESLint/Prettier.
- [ ] P0-03 [P] Configure env management docs: DB URL (Neon), JWT secret, CORS origins, ports.

## Phase 1: Backend Auth (P1)
- [ ] B1-01 Define `User` model (id, email unique, password_hash, created_at) in `backend/app/models.py` and schema in `backend/app/schemas.py`.
- [ ] B1-02 Implement password hashing and JWT utilities in `backend/app/auth.py` (expiry, secret).
- [ ] B1-03 Add `/auth/signup` and `/auth/login` routes in `backend/app/routes/auth.py` with duplicate email handling (409).
- [ ] B1-04 Add dependency to extract user from `Authorization: Bearer` JWT in `backend/app/deps.py`; 401 on invalid/expired.
- [ ] B1-05 Tests: pytest for signup/login success/failure and token validation in `backend/tests/test_auth.py`.

## Phase 2: Backend Tasks CRUD (P1/P2)
- [ ] B2-01 Define `Task` model (id, user_id FK, title, description, status, created_at, updated_at) in `backend/app/models.py`; schemas in `backend/app/schemas.py`.
- [ ] B2-02 Implement `/tasks` routes in `backend/app/routes/tasks.py`: create (default status open), list (user-scoped), get by id (404 if not owner), update (partial), toggle status, delete.
- [ ] B2-03 Enforce user_id scoping on all queries; return 404 for cross-user access.
- [ ] B2-04 Tests: pytest for CRUD success, validation errors (missing title), unauthorized/expired token handling in `backend/tests/test_tasks.py`.
- [ ] B2-05 Migrations: create initial migration for users/tasks tables in `backend/migrations/`.

## Phase 3: Database Integration (P1)
- [ ] DB-01 Configure Neon PostgreSQL connection (async engine) in `backend/app/db.py`.
- [ ] DB-02 Document migration workflow (alembic/SQLModel) and add scripts/commands.
- [ ] DB-03 Add seed/dev helper for local testing (optional).

## Phase 4: Frontend Auth (P1)
- [ ] F1-01 Build `/signup` and `/login` pages with forms and validation in `frontend/app` (or `pages/`).
- [ ] F1-02 Implement API client in `frontend/lib/api.ts` to call auth endpoints and store JWT (header-based).
- [ ] F1-03 Handle auth errors and token expiry (redirect to login on 401).
- [ ] F1-04 Tests: happy-path auth flow (Playwright/Cypress) in `frontend/tests/`.

## Phase 5: Frontend Tasks UI (P2)
- [ ] F2-01 Build `/tasks` view: list tasks, create inline, show status, show errors/loading.
- [ ] F2-02 Build task detail/edit (page or modal) for update/toggle/delete.
- [ ] F2-03 Wire API calls with JWT header; handle 401/404/validation errors gracefully.
- [ ] F2-04 Responsive styles with Tailwind; ensure mobile usability.
- [ ] F2-05 Tests: happy-path CRUD UI flow (Playwright/Cypress).

## Phase 6: Cross-Cutting
- [ ] X1-01 Define error response shape and document in README/API docs.
- [ ] X1-02 Add CORS config for frontend origin.
- [ ] X1-03 Add basic observability: structured logging on backend.
- [ ] X1-04 Update top-level README with Phase II setup, env vars, run commands, and links to specs.

## Dependencies & Order
- Backend auth (Phase 1) blocks tasks CRUD and frontend auth integration.
- Backend tasks (Phase 2) blocks frontend task UI.
- Database setup (Phase 3) is required before running backend tests against real DB; use in-memory/SQLite for fast unit tests if desired.
- Frontend auth (Phase 4) depends on backend auth; frontend tasks (Phase 5) depends on backend tasks.
