---
id: 012
title: Phase two constitution
stage: constitution
date: 2026-01-02
surface: agent
model: gpt-5
feature: none
branch: main
user: user
command: codex-cli session
labels: [constitution, phase2, fullstack]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - phase-two/.specify/memory/constitution.md
 - phase-two/history/phase-two-history.md
tests:
 - none
---

## Prompt

/sp.constitution
---
# Constitution for Full-Stack Todo Application (Phase 2)

## Purpose
The purpose of this phase is to extend the in-memory Todo app into a full-stack web application using Next.js for the frontend and FastAPI for the backend. The app must support user authentication with JWT and task CRUD operations, while ensuring persistence using Neon Serverless PostgreSQL.

## Principles
- **User Isolation**: Each user should only see their own tasks.
- **Security**: All API endpoints must be secured with JWT tokens.
- **Scalability**: The application should be built for scalability, with clean separation between frontend, backend, and database.
- **Responsiveness**: The frontend must be responsive and accessible on both mobile and desktop devices.
- **Stateless Authentication**: Use JWT for stateless user authentication.

## Response snapshot

Recorded Phase II constitution under `phase-two/.specify/memory/constitution.md`, capturing purpose (Next.js + FastAPI + Neon, JWT auth) and principles (user isolation, security, scalability, responsiveness, stateless auth).

## Outcome

- ƒo. Impact: Phase II governance established in its own directory.
- dY¦ Tests: none
- dY"? Files: phase-two/.specify/memory/constitution.md, phase-two/history/phase-two-history.md updated.
- dY"? Next prompts: Draft Phase II spec/plan/tasks under phase-two/specs/.
- dYÿ Reflection: Constitution now localized to Phase II folder.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): N/A
