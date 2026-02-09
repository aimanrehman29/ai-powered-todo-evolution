from __future__ import annotations

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    conversation_id: Optional[int] = None
    message: str = Field(min_length=1)


class ToolCall(BaseModel):
    name: str
    arguments: dict
    result: Optional[dict] = None


class ChatResponse(BaseModel):
    conversation_id: int
    response: str
    tool_calls: List[ToolCall] = []


class MessageRead(BaseModel):
    id: int
    conversation_id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
