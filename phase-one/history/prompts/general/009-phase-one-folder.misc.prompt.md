---
id: 009
title: Phase one folder reorg
stage: misc
date: 2026-01-02
surface: agent
model: gpt-5
feature: none
branch: master
user: user
command: codex-cli session
labels: [restructure, todo, organization]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - README.md
 - phase-one/README.md
 - phase-one/CLAUDE.md
 - phase-one/.specify
 - phase-one/specs
 - phase-one/specs-history
 - phase-one/history
 - phase-one/src
 - phase-one/tests
 - phase-one/todo
 - phase-one/sitecustomize.py
tests:
 - python -m unittest discover -s tests -t . (workdir: phase-one)
 - python -m todo list (workdir: phase-one)
---

## Prompt

can u add todo app in phase one folder so file will be organize

## Response snapshot

Moved all project assets into `phase-one/`, added a root README pointing there, updated phase-one README and CLAUDE snapshot to note location, and re-ran tests plus a CLI smoke check.

## Outcome

- ƒo. Impact: Project now organized under `phase-one/`; root README points to it.
- dY¦ Tests: python -m unittest discover -s tests -t . (pass); python -m todo list (pass)
- dY"? Files: Core project dirs/files moved into phase-one; READMEs and CLAUDE updated.
- dY"? Next prompts: None.
- dYÿ Reflection: Run all commands from `phase-one/` going forward.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): N/A
