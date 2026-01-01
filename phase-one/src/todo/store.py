from __future__ import annotations

from typing import Dict, List, Optional

from .models import Task


class TaskNotFoundError(ValueError):
    pass


class TaskStore:
    """
    In-memory store for tasks. Not safe for concurrent mutation but sufficient
    for single-process CLI use.
    """

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str, description: str = "") -> Task:
        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Title is required.")
        task = Task(id=self._next_id, title=cleaned_title, description=description, completed=False)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list_all(self) -> List[Task]:
        return [self._tasks[key] for key in sorted(self._tasks)]

    def update(self, task_id: int, *, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        if title is None and description is None:
            raise ValueError("Provide at least one field to update.")
        task = self._get(task_id)
        if title is not None:
            cleaned_title = title.strip()
            if not cleaned_title:
                raise ValueError("Title cannot be empty.")
            task.title = cleaned_title
        if description is not None:
            task.description = description
        return task

    def toggle(self, task_id: int) -> Task:
        task = self._get(task_id)
        task.completed = not task.completed
        return task

    def delete(self, task_id: int) -> Task:
        task = self._get(task_id)
        del self._tasks[task_id]
        return task

    def _get(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise TaskNotFoundError(f"Task with id {task_id} not found.") from exc
