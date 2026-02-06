---
id: 019
title: Backend DB SSL fix
stage: green
date: 2026-02-04
surface: agent
model: gpt-5
feature: phase-two
branch: main
user: user
command: codex-cli session
labels: [backend, db, ssl, fix]
links:
  spec: phase-two/specs/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - phase-two/backend/app/db.py
 - phase-two/backend/.env
 - phase-two/backend/app/.env
tests:
 - python -c "import asyncio; from app.db import init_db; asyncio.run(init_db()); print('db ok')"
---

## Prompt

(.venv) PS C:\aiman rehman\ai driven development\hackthone2-101\phase-two\backend> uvicorn --env-file .env app.main:app --reload
...
asyncpg.exceptions._base.ClientConfigurationError: `sslmode` parameter must be one of: disable, allow, prefer, require, verify-ca, verify-full

## Response snapshot

Switched DB URL to plain DSN (no sslmode params) and enforced TLS via SQLAlchemy connect_args `{"ssl": True}`. Updated both .env files and verified connectivity with `init_db` script.

## Outcome

- ƒo. Impact: Backend now connects to Neon via asyncpg without SSL parameter errors.
- dY¦ Tests: python -c "import asyncio; from app.db import init_db; asyncio.run(init_db()); print('db ok')" (pass)
- dY"? Files: app/db.py changed to set connect_args ssl; env files updated to DSN without query params.
- dY"? Next prompts: Restart uvicorn with updated .env.
- dYÿ Reflection: asyncpg rejected sslmode/ssl query params; using connect_args with ssl=True is reliable.

## Evaluation notes (flywheel)

- Failure modes observed: asyncpg config errors due to sslmode/ssl query params.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): None needed.
