---

description: "Task list for todo-cli feature"
---

# Tasks: todo-cli

**Input**: Design documents from `/specs/todo-cli/`  
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 [P] [US1] Create project layout `src/todo/` with `__init__.py` and `__main__.py` entrypoint wiring.
- [ ] T002 [P] [US1] Add test layout `tests/unit/` and configure `python -m unittest` discovery.

---

## Phase 2: User Story 1 - Capture and View Tasks (Priority: P1)

**Goal**: Add and list tasks with status.

**Independent Test**: `python -m todo add "Title" --description "Detail"` then `python -m todo list`.

- [ ] T101 [P] [US1] Implement `Task` dataclass in `src/todo/models.py` with id/title/description/completed.
- [ ] T102 [P] [US1] Implement `TaskStore.add` and `TaskStore.list_all` in `src/todo/store.py`.
- [ ] T103 [US1] Implement CLI `add` and `list` subcommands in `src/todo/cli.py` delegating to the store.
- [ ] T104 [US1] Add unit tests for add/list happy paths and empty list message in `tests/unit/test_store.py`.
- [ ] T105 [US1] Add CLI exit-code/error handling tests for missing title or unknown command in `tests/unit/test_cli.py`.

**Checkpoint**: User can add and list tasks with correct statuses.

---

## Phase 3: User Story 2 - Update and Toggle Tasks (Priority: P2)

**Goal**: Update task fields and toggle completion.

**Independent Test**: Update task title/description and toggle status twice.

- [ ] T201 [P] [US2] Implement `TaskStore.update` in `src/todo/store.py` with partial field updates.
- [ ] T202 [P] [US2] Implement `TaskStore.toggle` in `src/todo/store.py`.
- [ ] T203 [US2] Wire `update` and `toggle` subcommands in `src/todo/cli.py` with validation and messaging.
- [ ] T204 [US2] Add unit tests for update/toggle success and unknown ID behavior in `tests/unit/test_store.py`.
- [ ] T205 [US2] Add CLI tests for update/toggle exit codes and messages in `tests/unit/test_cli.py`.

**Checkpoint**: User can edit details and flip completion state.

---

## Phase 4: User Story 3 - Remove Tasks (Priority: P3)

**Goal**: Delete tasks by ID.

**Independent Test**: Delete one of two tasks and confirm only the remaining task lists.

- [ ] T301 [US3] Implement `TaskStore.delete` in `src/todo/store.py`.
- [ ] T302 [US3] Wire `delete` subcommand in `src/todo/cli.py` with error handling for unknown IDs.
- [ ] T303 [US3] Add unit and CLI tests for delete success/failure cases in `tests/unit/test_store.py` and `tests/unit/test_cli.py`.

**Checkpoint**: User can remove tasks and see updated list.

---

## Phase 5: Polish & Cross-Cutting

- [ ] T401 [P] Add README quickstart commands and usage examples.
- [ ] T402 [P] Ensure help text and error messages are concise and consistent across commands.
- [ ] T403 Validate `python -m unittest` passes and document expected outputs.

---

## Dependencies & Execution Order

- Phase 1 precedes all other work.
- User Story 1 tasks precede User Stories 2 and 3.
- User Stories 2 and 3 can proceed after foundational add/list functions exist.
- Polish tasks run after functional stories complete.
