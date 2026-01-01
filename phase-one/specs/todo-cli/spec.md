# Feature Specification: Evolution of Todo - Phase I (In-Memory CLI)

**Feature Branch**: `[001-todo-cli]`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "Build an in-memory Python CLI todo app with add, view, update, delete, and toggle complete/incomplete commands."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Capture and View Tasks (Priority: P1)

As a CLI user I can add tasks with a title and description and list them with their status so I can track work in the current session.

**Why this priority**: Without adding and viewing tasks the app has no value; this story delivers the minimum usable product.

**Independent Test**: Run `python -m todo add "Title" --description "Detail"` followed by `python -m todo list` and confirm the task appears with status `open`.

**Acceptance Scenarios**:

1. **Given** no tasks exist, **When** I run `python -m todo list`, **Then** the CLI reports "no tasks" and exits 0.
2. **Given** I add a task with title and description, **When** I list tasks, **Then** the task shows an auto-assigned ID, title, description, and status `open`.

---

### User Story 2 - Update and Toggle Tasks (Priority: P2)

As a CLI user I can update a task’s title/description and toggle its completion state so I keep details current.

**Why this priority**: Editing tasks is common and should work before deletion; toggling status is a core workflow.

**Independent Test**: Add a task, run `python -m todo update <id> --title "New" --description "New detail"`, then `python -m todo toggle <id>` and list to verify fields and status change.

**Acceptance Scenarios**:

1. **Given** a task exists, **When** I update only its title, **Then** the title changes while description and status remain unchanged.
2. **Given** a task is open, **When** I toggle it, **Then** its status becomes `done`; when toggled again it returns to `open`.

---

### User Story 3 - Remove Tasks (Priority: P3)

As a CLI user I can delete a task by ID so I can remove items that are no longer relevant.

**Why this priority**: Deletion is useful but not required for the initial workflows once add/update/toggle exist.

**Independent Test**: Add two tasks, delete one with `python -m todo delete <id>`, then list and confirm only the remaining task appears.

**Acceptance Scenarios**:

1. **Given** tasks exist, **When** I delete one by its ID, **Then** it is removed and subsequent listings omit it.
2. **Given** I attempt to delete a non-existent ID, **When** I run the delete command, **Then** the CLI returns a clear error message and non-zero exit code.

---

### Edge Cases

- What happens when the title is missing or empty? -> Reject with helpful error and non-zero exit code.
- How does the system handle unknown task IDs? -> Print "Task not found" and return non-zero exit code without mutating data.
- How does listing behave with no tasks? -> Output a friendly message and exit 0.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a task with a title (required) and description (optional but captured).
- **FR-002**: System MUST list all tasks with ID, title, description, and status (`open`|`done`).
- **FR-003**: Users MUST be able to update a task’s title and/or description by ID.
- **FR-004**: System MUST toggle a task’s status between complete and incomplete by ID.
- **FR-005**: System MUST delete a task by ID with confirmation messaging.
- **FR-006**: System MUST validate input and return non-zero exit codes on invalid commands or missing IDs.

### Key Entities *(include if feature involves data)*

- **Task**: Fields include `id` (int), `title` (str), `description` (str), `completed` (bool).
- **TaskStore**: In-memory collection managing Task creation, retrieval, updates, deletions, and status toggling.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All five CLI commands (add, list, update, toggle, delete) run successfully with exit code 0 on valid input.
- **SC-002**: Invalid IDs or missing required fields produce exit code 1 and actionable error messages.
- **SC-003**: Listing with no tasks produces a user-friendly message without crashing or non-zero exit codes.
- **SC-004**: README contains copy-pasteable commands that execute as documented on Python 3.13+.
