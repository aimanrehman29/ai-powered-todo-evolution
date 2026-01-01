# Feature Specification: Add Task Command

**Feature Branch**: `[002-add-task]`  
**Created**: 2026-01-02  
**Status**: Draft  
**Input**: User description: "Define a detailed specification for adding tasks in the CLI todo app."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task Successfully (Priority: P1)

As a CLI user I can add a task with a required title and optional description so it appears in my current session.

**Why this priority**: Core capability; nothing else matters if tasks cannot be created.

**Independent Test**: Run `python -m todo add "Title" --description "Detail"` and confirm success message with an ID; listing shows the new task as `open`.

**Acceptance Scenarios**:
1. **Given** no tasks exist, **When** I run `add "Title" --description "Detail"`, **Then** the CLI exits 0 and prints `Added task <id>: Title` with status defaulting to `open` when listed.
2. **Given** an existing task, **When** I add another task with the same title, **Then** the CLI still succeeds, assigns a new unique ID, and both tasks list separately.

---

### User Story 2 - Reject Missing Title (Priority: P2)

As a CLI user I am warned when I omit or provide an empty title so I can correct input without creating invalid tasks.

**Why this priority**: Prevents unusable tasks and keeps data valid.

**Independent Test**: Run `python -m todo add ""` and expect exit code 1 with an error message; no task is added when listing.

**Acceptance Scenarios**:
1. **Given** I run `add ""`, **When** the title is empty or whitespace, **Then** the CLI prints an error to stderr, returns non-zero, and no tasks are created.
2. **Given** I omit the title argument entirely, **When** I execute the command, **Then** argparse reports missing arguments with non-zero exit code.

---

### Edge Cases

- Title containing only whitespace is rejected.
- Description may be empty; storing an empty string is allowed.
- Duplicate titles are allowed; IDs must always be unique and incremental.
- Extremely long titles/descriptions should be accepted but trimmed of leading/trailing whitespace for titles.
- Interactive mode should present the same validations as one-shot mode.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept `add <title> [--description TEXT]` and create a new task with status defaulting to `open`.
- **FR-002**: System MUST validate title is non-empty after trimming whitespace; otherwise return non-zero and print a clear error.
- **FR-003**: System MUST store description as provided (may be empty) without blocking task creation.
- **FR-004**: System MUST assign each task a unique, incrementing ID and include it in the success message.
- **FR-005**: System MUST allow duplicate titles but list them as separate entries with distinct IDs.
- **FR-006**: System MUST surface errors to stderr and successes to stdout with deterministic exit codes.

### Key Entities *(include if feature involves data)*

- **Task**: Fields `id:int`, `title:str`, `description:str`, `completed:bool` default `False`.
- **TaskStore**: Provides `add(title, description="") -> Task` enforcing validation and ID generation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `python -m todo add "Sample"` returns exit code 0 and prints task ID + title.
- **SC-002**: `python -m todo add ""` returns non-zero, prints validation error, and `list` shows no new tasks.
- **SC-003**: Adding two tasks with identical titles results in two distinct IDs visible in `list`.
- **SC-004**: Interactive mode enforces the same validation and messaging as one-shot mode.
