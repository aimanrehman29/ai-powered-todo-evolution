# Implementation Plan: add-task

**Branch**: `[002-add-task]` | **Date**: 2026-01-02 | **Spec**: specs/todo-cli/add-task.spec.md  
**Input**: Feature specification from `/specs/todo-cli/add-task.spec.md`

## Summary
Add-task command already exists; this plan locks behavior to spec: use auto-incrementing integer IDs, optional description, validation for non-empty trimmed title, and success confirmation on stdout. The in-memory `TaskStore.add` handles ID generation and validation; CLI routes `add` subcommand and prints confirmation. Tests cover success, duplicate titles, empty title rejection, and missing args.

## Technical Context
**Language/Version**: Python 3.13  
**Primary Dependencies**: Standard library only (`argparse`, `dataclasses`).  
**Storage**: In-memory store via `TaskStore` (dict keyed by int).  
**Testing**: `python -m unittest discover -s tests -t .` with unit tests in `tests/unit/`.  
**Target Platform**: CLI on Python 3.13+.  
**Project Type**: Single CLI project.  
**Performance Goals**: O(1) add; negligible overhead.  
**Constraints**: No persistence, no external deps; stdout for success, stderr for errors.

## Constitution Check
- Spec-first and CLI clarity satisfied (subcommand + help).
- In-memory simplicity observed; no persistence.
- Testable units: store and CLI separated.
- Small diffs: only touch add flow/tests/docs if needed.

## Project Structure
```text
specs/todo-cli/
  add-task.spec.md
  add-task.plan.md
src/todo/
  models.py   # Task dataclass
  store.py    # TaskStore.add validation + ID
  cli.py      # argparse, add handler prints confirmation
tests/unit/
  test_store.py
  test_cli.py
```
**Structure Decision**: Reuse existing single-project layout; no new modules.

## Implementation Steps
1) **Validate spec alignment**: Ensure `TaskStore.add` trims title, rejects empty, allows duplicates, sets `completed=False`, returns Task with ID.  
2) **CLI behavior**: Confirm `add` subcommand requires title arg, accepts optional `--description/-d`, and on success prints `Added task <id>: <title>` with exit code 0; errors go to stderr with exit code 1.  
3) **Interactive parity**: Verify interactive loop routes `add` through same path; no special cancel syntax beyond `exit/quit` or Ctrl+C.  
4) **Tests**: Expand/adjust unit tests to cover duplicate titles creating unique IDs, empty/whitespace-only title rejection, and confirmation messaging.  
5) **Docs**: Update README if messaging or usage changes.

## Complexity Tracking
No new complexity beyond existing pattern; no violations identified.
