from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Conversation(SQLModel, table=True):
    __tablename__ = "conversation"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    messages: List["Message"] = Relationship(back_populates="conversation")


class Message(SQLModel, table=True):
    __tablename__ = "message"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    conversation_id: int = Field(foreign_key="conversation.id")
    role: str = Field(index=True)  # "user" | "assistant"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    conversation: Optional[Conversation] = Relationship(back_populates="messages")


# Placeholder Task model if needed for tool stubs (actual tasks live in phase-two codebase)
class Task(SQLModel, table=True):
    __tablename__ = "task"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    title: str
    description: str = ""
    status: str = Field(default="open")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
