# Todo App - Spec-Kit/Claude Guide

## Structure
- /.spec-kit/config.yaml
- /specs/**/* (overview, features, api, database, ui)
- /phase-two/frontend (Next.js)
- /phase-two/backend (FastAPI)

## Workflow
1) Read relevant spec in /specs
2) Follow phase-specific CLAUDE.md
3) Use spec-driven prompts (/sp.*) when generating

## Commands
- Frontend: cd phase-two/frontend && npm run dev
- Backend: cd phase-two/backend && uvicorn --env-file .env app.main:app --reload
