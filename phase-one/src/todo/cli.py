from __future__ import annotations

import argparse
import shlex
import sys
from typing import List, Optional

from .models import Task
from .store import TaskNotFoundError, TaskStore


class ParserError(Exception):
    pass


class TodoArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ParserError(message)


def build_parser() -> argparse.ArgumentParser:
    parser = TodoArgumentParser(
        prog="todo",
        description="In-memory todo list (session lasts for the life of the process).",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title for the task")
    add_parser.add_argument("--description", "-d", default="", help="Optional task description")

    subparsers.add_parser("list", help="List all tasks")

    update_parser = subparsers.add_parser("update", help="Update a task's title and/or description")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("--title", "-t", help="New title")
    update_parser.add_argument("--description", "-d", help="New description")

    toggle_parser = subparsers.add_parser("toggle", help="Toggle completion status for a task")
    toggle_parser.add_argument("id", type=int, help="ID of the task to toggle")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    return parser


def run(argv: Optional[List[str]] = None, *, store: Optional[TaskStore] = None) -> int:
    store = store or TaskStore()
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except ParserError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    except SystemExit as exc:  # argparse uses SystemExit for --help
        return exc.code if isinstance(exc.code, int) else 0

    return dispatch(args, store)


def dispatch(args: argparse.Namespace, store: TaskStore) -> int:
    if args.command == "add":
        return _handle_add(store, args.title, args.description)
    if args.command == "list":
        return _handle_list(store)
    if args.command == "update":
        return _handle_update(store, args.id, args.title, args.description)
    if args.command == "toggle":
        return _handle_toggle(store, args.id)
    if args.command == "delete":
        return _handle_delete(store, args.id)
    sys.stderr.write("Unknown command.\n")
    return 1


def _handle_add(store: TaskStore, title: str, description: str) -> int:
    try:
        task = store.add(title, description)
    except ValueError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    sys.stdout.write(f"Added task {task.id}: {task.title}\n")
    return 0


def _handle_list(store: TaskStore) -> int:
    tasks = store.list_all()
    if not tasks:
        sys.stdout.write("No tasks yet. Add one with: add \"Title\" --description \"Detail\"\n")
        return 0
    lines = [_format_task(task) for task in tasks]
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


def _handle_update(store: TaskStore, task_id: int, title: Optional[str], description: Optional[str]) -> int:
    try:
        updated = store.update(task_id, title=title, description=description)
    except TaskNotFoundError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    except ValueError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    sys.stdout.write(f"Updated task {updated.id}.\n")
    return 0


def _handle_toggle(store: TaskStore, task_id: int) -> int:
    try:
        task = store.toggle(task_id)
    except TaskNotFoundError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    status = "done" if task.completed else "open"
    sys.stdout.write(f"Marked task {task.id} as {status}.\n")
    return 0


def _handle_delete(store: TaskStore, task_id: int) -> int:
    try:
        store.delete(task_id)
    except TaskNotFoundError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1
    sys.stdout.write(f"Deleted task {task_id}.\n")
    return 0


def _format_task(task: Task) -> str:
    header = f"[{task.id}] ({task.status}) {task.title}"
    if task.description:
        return f"{header}\n    {task.description}"
    return header


def interactive_loop(store: Optional[TaskStore] = None) -> int:
    store = store or TaskStore()
    parser = build_parser()
    sys.stdout.write("Todo CLI (in-memory session). Type 'help' for commands, 'exit' to quit.\n")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            sys.stdout.write("\n")
            break

        if not line:
            continue
        if line in {"exit", "quit"}:
            break
        if line in {"help", "?"}:
            parser.print_help()
            continue

        try:
            argv = shlex.split(line)
        except ValueError as exc:
            sys.stderr.write(f"Error parsing command: {exc}\n")
            continue

        exit_code = run(argv, store=store)
        if exit_code not in (0, None):
            continue
    return 0


def main() -> int:
    if len(sys.argv) == 1:
        return interactive_loop(TaskStore())
    return run(sys.argv[1:], store=TaskStore())


if __name__ == "__main__":
    sys.exit(main())
