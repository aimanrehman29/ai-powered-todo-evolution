# Constitution for Full-Stack Todo Application (Phase 2)

## Purpose
Extend the in-memory Todo app into a full-stack web application using Next.js for the frontend and FastAPI for the backend. Support user authentication with JWT and task CRUD operations with persistence in Neon Serverless PostgreSQL.

## Core Principles

### I. User Isolation
Each authenticated user only sees and mutates their own tasks; enforce per-user scoping at every layer.

### II. Security
All API endpoints require JWT auth; validate inputs, use least-privilege DB access, and keep secrets in environment configuration. Serve over HTTPS in deployed environments.

### III. Scalability & Separation
Keep frontend, backend, and database concerns decoupled. Use explicit API contracts and shared types/schemas to prevent drift.

### IV. Responsiveness & Accessibility
Frontend must be responsive on mobile and desktop with accessible components and sensible loading states.

### V. Stateless Authentication
JWT-based, stateless auth with expiry and rotation considerations; avoid server-side session storage.

## Delivery Constraints
- Frontend: Next.js (TypeScript), responsive UI, accessibility considered.
- Backend: FastAPI (Python 3.13), Pydantic schemas, JWT-secured routes, task CRUD.
- Database: Neon Serverless PostgreSQL with migrations for schema changes.
- Security: HTTPS assumed in production; parameterized queries/ORM to avoid injection.
- Testing: Backend unit/integration tests; frontend happy-path flows; lint/format per stack.
- Tooling: Spec-Kit Plus for specs/plans/tasks; PHRs for prompts.

## Workflow Expectations
- Sequence: spec → plan → tasks → implement → test → document.
- Define API contracts before frontend consumption; mocks allowed with parity tests.
- Document setup: env vars (DB URL, JWT secret), migration steps, run commands for frontend/backend.
- CI should include lint, tests, and type checks.

## Governance
This constitution governs Phase 2 full-stack work. Amendments require updating this file with rationale, date, and alignment of active specs/plans.

**Version**: 2.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
