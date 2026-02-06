# Constitution for Full-Stack Todo Application (Phase 2)

## Purpose
Extend the in-memory Todo app into a full-stack web application with a Next.js frontend and FastAPI backend. Provide user-scoped task CRUD with JWT-based authentication and persistence in Neon Serverless PostgreSQL.

## Core Principles

### I. User Isolation
Every request is scoped to the authenticated user; no cross-tenant visibility or leakage.

### II. Security by Default
All APIs require JWT auth; enforce HTTPS, input validation, and least-privilege database access. Secrets stay out of code and are injected via environment config.

### III. Layered Separation
Frontend, backend, and database concerns stay decoupled. API contracts are explicit; shared types/schemas are generated or centrally defined to avoid drift.

### IV. Stateless Authentication
Use signed JWTs for stateless auth; avoid server-side session storage. Tokens include expiry and are rotated as needed.

### V. Resilient & Observable
Add structured logging, basic metrics, and meaningful error responses. Handle failure modes gracefully (auth failure, validation, DB errors) with clear status codes.

### VI. Performance & Responsiveness
Frontend must be responsive on mobile/desktop; backend should keep p95 API latency low (<200ms for simple CRUD) under typical loads.

## Delivery Constraints
- Frontend: Next.js (TypeScript), responsive and accessible UI.
- Backend: FastAPI (Python 3.13), typed routes/schemas (Pydantic), JWT auth, task CRUD.
- Database: Neon Serverless PostgreSQL; migrations required for schema changes.
- Security: HTTPS assumed; JWT required for protected routes; parameterized queries/ORM to prevent SQL injection.
- Testing: Automated tests for backend (unit/integration) and at least happy-path frontend flows; lint/format per stack norms.
- Tooling: Use Spec-Kit Plus for specs/plans/tasks; capture PHRs per prompt.

## Workflow Expectations
- Sequence: spec → plan → tasks → implement → test → document → release.
- API contracts defined before frontend consumption; mock/stub APIs allowed during frontend development with clear parity tests.
- CI steps should include lint, tests, and type checks where applicable.
- Documentation must cover setup, env vars (JWT secret, DB URL), migrations, and run commands for frontend/backend.

## Governance
This constitution governs Phase 2 full-stack work. Amendments require updating this file with rationale and dates, and aligning open specs and plans accordingly.

**Version**: 2.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
