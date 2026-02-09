from __future__ import annotations

from typing import Any, Dict, List
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from .models import Task


async def add_task(session: AsyncSession, user_id: int, title: str, description: str = "") -> Dict[str, Any]:
    title = title.strip()
    if not title:
        raise ValueError("Title required")
    task = Task(user_id=user_id, title=title, description=description or "")
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return {"task_id": task.id, "status": "created", "title": task.title}


async def list_tasks(session: AsyncSession, user_id: int, status: str | None = None) -> List[Dict[str, Any]]:
    query = select(Task).where(Task.user_id == user_id)
    if status and status != "all":
        query = query.where(Task.status == ("done" if status == "completed" else "open"))
    res = await session.execute(query)
    tasks = res.scalars().all()
    return [{"id": t.id, "title": t.title, "completed": t.status == "done"} for t in tasks]


async def complete_task(session: AsyncSession, user_id: int, task_id: int) -> Dict[str, Any]:
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise ValueError("Task not found")
    task.status = "done"
    session.add(task)
    await session.commit()
    return {"task_id": task.id, "status": "completed", "title": task.title}


async def delete_task(session: AsyncSession, user_id: int, task_id: int) -> Dict[str, Any]:
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise ValueError("Task not found")
    await session.delete(task)
    await session.commit()
    return {"task_id": task_id, "status": "deleted", "title": task.title}


async def update_task(
    session: AsyncSession, user_id: int, task_id: int, title: str | None = None, description: str | None = None
) -> Dict[str, Any]:
    task = await session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise ValueError("Task not found")
    if title is not None:
        t = title.strip()
        if not t:
            raise ValueError("Title required")
        task.title = t
    if description is not None:
        task.description = description
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return {"task_id": task.id, "status": "updated", "title": task.title}
