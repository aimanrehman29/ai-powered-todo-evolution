from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Conversation(SQLModel, table=True):
    """Chat conversation per user."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # SQLModel will infer target from annotation; keep concrete typing (no future annotations).
    messages: List["Message"] = Relationship(back_populates="conversation")


class Message(SQLModel, table=True):
    """Individual chat message."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    conversation_id: int = Field(foreign_key="conversation.id")
    role: str = Field(index=True)  # "user" | "assistant"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    conversation: Optional["Conversation"] = Relationship(back_populates="messages")


class Task(SQLModel, table=True):
    """Simple task table (kept for tool stubs)."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    title: str
    description: str = ""
    status: str = Field(default="open")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
