# Evolution of Todo (Phase I): In-Memory Python CLI

> Run commands from this directory (`phase-one/`). Each invocation is in-memory and lasts for the life of the process.

Simple, spec-driven todo list that keeps tasks in memory for the lifetime of the process. Supports add, list, update, toggle complete/incomplete, and delete commands via an interactive CLI.

## Requirements
- Python 3.13+
- No external dependencies; runs with the standard library.
- No install step needed; the repository includes a shim so `python -m todo` works from the repo root.

## Quickstart (interactive session)
State lasts only while the process runs. Start an interactive session to perform multiple actions:

```bash
python -m todo
> add "Write README" --description "Draft quickstart"
> list
> toggle 1
> update 1 --title "Ship README"
> delete 1
> exit
```

One-shot commands are available (e.g., `python -m todo list`), but each invocation has a fresh in-memory store.

## Commands
- `add <title> [--description TEXT]` — create a task (title required).
- `list` — list tasks with ID and status (`open`|`done`).
- `update <id> [--title TEXT] [--description TEXT]` — change task fields; at least one field required.
- `toggle <id>` — flip completion status.
- `delete <id>` — remove a task.

All success paths return exit code 0. Validation errors print to stderr and return non-zero.

## How the CLI works (add/remove)
- In-memory store: Tasks live only while the process runs; each run starts clean.
- Add flow: `add "<title>" --description "<text>"` → validates non-empty title → assigns next ID → prints `Added task <id>: <title>`.
- Remove flow: `delete <id>` → errors if ID missing/unknown → on success prints `Deleted task <id>.`
- Status: new tasks start `open`; `toggle <id>` flips between `open` and `done`.
- Listing: `list` prints `[id] (status) title` and description on the next indented line if provided.

## Tests
Run unit tests:

```bash
python -m unittest discover -s tests -t .
```

## Project Structure
```
specs/
  todo-cli/          # spec, plan, tasks
src/
  todo/              # CLI code (argparse) and in-memory store
tests/
  unit/              # unit tests for store and CLI dispatch
```

## Specs & Workflow
- Constitution: `.specify/memory/constitution.md`
- Spec: `specs/todo-cli/spec.md`
- Plan: `specs/todo-cli/plan.md`
- Tasks: `specs/todo-cli/tasks.md`

The CLI uses stdout for normal output and stderr for errors. No data is persisted after the process exits.
