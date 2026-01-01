---

description: "Tasks for add-task feature"
---

# Tasks: add-task

**Input**: add-task.spec.md, add-task.plan.md  
**Prerequisites**: existing `Task`/`TaskStore`/CLI structure in `src/todo/`

## Phase 1: Model & Storage

- [ ] AT-001 [P] Define/confirm `Task` dataclass fields (`id`, `title`, `description`, `completed=False`) in `src/todo/models.py`.
- [ ] AT-002 [P] Ensure `TaskStore` maintains in-memory collection with auto-increment IDs in `src/todo/store.py`.

## Phase 2: Input & Validation

- [ ] AT-101 [P] Ensure CLI `add` subcommand requires `title` and optional `--description/-d` in `src/todo/cli.py`.
- [ ] AT-102 Validate title is non-empty after trim; on failure, write error to stderr and return exit code 1 in `TaskStore.add` and CLI handler.
- [ ] AT-103 Allow duplicate titles; verify unique IDs assigned per insertion.

## Phase 3: Creation & Output

- [ ] AT-201 [P] Implement/confirm `TaskStore.add` sets `completed=False`, appends to in-memory store, returns Task with ID.
- [ ] AT-202 On success, CLI prints `Added task <id>: <title>` to stdout with exit code 0.
- [ ] AT-203 Ensure interactive loop routes `add` through same path; no special cancel syntax beyond `exit/quit` or Ctrl+C.

## Phase 4: Tests

- [ ] AT-301 Add/extend unit tests in `tests/unit/test_store.py` for add success, duplicate titles (unique IDs), and empty/whitespace title rejection.
- [ ] AT-302 Add/extend unit tests in `tests/unit/test_cli.py` for add success output, duplicate titles, and validation errors (stderr, exit code 1).

## Phase 5: Docs

- [ ] AT-401 Update `README.md` add-command description if messaging changes; note duplicate titles allowed and ID uniqueness.
- [ ] AT-402 Confirm plan/spec cross-reference remains accurate (add-task.plan.md).
