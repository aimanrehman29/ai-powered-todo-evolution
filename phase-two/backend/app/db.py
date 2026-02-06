from __future__ import annotations

import os
from typing import AsyncGenerator

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/todo")

# Enforce TLS when talking to Neon or any hosted Postgres. asyncpg expects a boolean or SSLContext.
engine = create_async_engine(DATABASE_URL, echo=False, future=True, connect_args={"ssl": True})
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
