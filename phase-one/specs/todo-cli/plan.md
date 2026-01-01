# Implementation Plan: todo-cli

**Branch**: `[001-todo-cli]` | **Date**: 2026-01-02 | **Spec**: specs/todo-cli/spec.md  
**Input**: Feature specification from `/specs/todo-cli/spec.md`

## Summary

Build a small Python CLI that manages tasks entirely in memory. Core logic lives in a `TaskStore` service that tracks `Task` objects with incremental IDs. The CLI uses `argparse` subcommands (`add`, `list`, `update`, `toggle`, `delete`) and routes to the store. Standard library only; no persistence beyond process lifetime. Tests cover the store behavior and basic CLI command parsing for happy and error paths.

## Technical Context

**Language/Version**: Python 3.13  
**Primary Dependencies**: Standard library only (`argparse`, `dataclasses`, `textwrap`)  
**Storage**: In-memory list/dict of tasks, no filesystem or database writes  
**Testing**: `python -m unittest` for unit coverage of store and CLI dispatch  
**Target Platform**: Any environment with Python 3.13+ and console access  
**Project Type**: Single CLI project  
**Performance Goals**: Handle dozens of tasks instantly; no perf risk  
**Constraints**: In-memory only; deterministic exits and messages; avoid side effects beyond stdout/stderr  
**Scale/Scope**: Single-user, single-process CLI session

## Constitution Check

- Spec-first: spec documented at `specs/todo-cli/spec.md`.
- CLI clarity: subcommands with help/exit codes defined; stdout for normal output, stderr for errors.
- In-memory simplicity: no persistence layers or external services.
- Testable units: store and parser extracted for unit tests.
- Small diffs: minimal modules under `src/todo`.

## Project Structure

```text
specs/
└─ todo-cli/
   ├─ spec.md
   ├─ plan.md
   └─ tasks.md

src/
└─ todo/
   ├─ __init__.py
   ├─ __main__.py        # enables python -m todo
   ├─ cli.py             # argparse parsing and dispatch
   ├─ models.py          # Task dataclass and helpers
   └─ store.py           # In-memory TaskStore service

tests/
└─ unit/
   ├─ test_store.py      # store behavior and edge cases
   └─ test_cli.py        # CLI dispatch and exit codes
```

**Structure Decision**: Single-project layout with `src/todo` for code and `tests/unit` for verification.

**Notes**: Root-level `todo/` package and `sitecustomize.py` are shims to make `python -m todo` work from the repository root without installation; application code still lives under `src/todo`.

## Complexity Tracking

No constitution violations identified; no extra complexity to justify.
