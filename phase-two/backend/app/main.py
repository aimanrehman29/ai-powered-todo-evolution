from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import init_db
from .routes import auth as auth_routes
from .routes import tasks as task_routes


def create_app() -> FastAPI:
    app = FastAPI(title="Todo API - Phase II")

    allowed_origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-powered-todo-evolution.vercel.app",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_routes.router)
    app.include_router(task_routes.router)
    app.include_router(task_routes.legacy_router)

    @app.on_event("startup")
    async def _startup() -> None:
        await init_db()

    return app


app = create_app()
