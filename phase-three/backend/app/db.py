from __future__ import annotations

import os
from typing import AsyncGenerator

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL env var is required")

print("[db] DATABASE_URL:", DATABASE_URL)

# For asyncpg, pass ssl via connect_args; keep URL clean (no sslmode).
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    connect_args={"ssl": True},
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db() -> None:
    """Create tables if they do not exist (for dev). Prefer migrations in prod."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
