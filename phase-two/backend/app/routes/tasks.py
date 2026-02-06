from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..models import Task, User
from ..schemas import TaskCreate, TaskRead, TaskUpdate
from ..deps import get_current_user, get_db


router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])
# Legacy router to support older frontend calls without user_id in path during transition.
legacy_router = APIRouter(prefix="/tasks", tags=["tasks-legacy"])


@router.post("", response_model=TaskRead, status_code=201)
async def create_task(
    user_id: int,
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    task = Task(
        title=task_in.title.strip(),
        description=task_in.description or "",
        status="open",
        user_id=current_user.id,
    )
    if not task.title:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title is required")
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


@router.get("", response_model=List[TaskRead])
async def list_tasks(
    user_id: int,
    current_user: User = Depends(get_current_user), session: AsyncSession = Depends(get_db)
) -> List[TaskRead]:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    result = await session.execute(select(Task).where(Task.user_id == current_user.id))
    return result.scalars().all()


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    task = await session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=TaskRead)
async def update_task(
    user_id: int,
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    task = await session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task_in.title is not None:
        new_title = task_in.title.strip()
        if not new_title:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title cannot be empty")
        task.title = new_title
    if task_in.description is not None:
        task.description = task_in.description
    if task_in.status is not None:
        task.status = task_in.status
    task.updated_at = datetime.utcnow()

    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


@router.patch("/{task_id}/complete", response_model=TaskRead)
async def toggle_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    task = await session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    task.status = "done" if task.status == "open" else "open"
    task.updated_at = datetime.utcnow()
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


@router.delete("/{task_id}", status_code=204, response_model=None)
async def delete_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> Response:
    if user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    task = await session.get(Task, task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    await session.delete(task)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# ---------- Legacy endpoints without user_id in path ----------

@legacy_router.post("", response_model=TaskRead, status_code=201)
async def legacy_create_task(
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    return await create_task(current_user.id, task_in, current_user, session)


@legacy_router.get("", response_model=List[TaskRead])
async def legacy_list_tasks(
    current_user: User = Depends(get_current_user), session: AsyncSession = Depends(get_db)
) -> List[TaskRead]:
    return await list_tasks(current_user.id, current_user, session)


@legacy_router.get("/{task_id}", response_model=TaskRead)
async def legacy_get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    return await get_task(current_user.id, task_id, current_user, session)


@legacy_router.patch("/{task_id}", response_model=TaskRead)
async def legacy_update_task(
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    return await update_task(current_user.id, task_id, task_in, current_user, session)


@legacy_router.patch("/{task_id}/complete", response_model=TaskRead)
async def legacy_toggle_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> TaskRead:
    return await toggle_task(current_user.id, task_id, current_user, session)


@legacy_router.delete("/{task_id}", status_code=204, response_model=None)
async def legacy_delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
) -> Response:
    return await delete_task(current_user.id, task_id, current_user, session)
