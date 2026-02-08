from __future__ import annotations

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..db import get_session
from ..models import Conversation, Message
from ..schemas import ChatRequest, ChatResponse
from ..agents import run_agent
from .. import mcp_tools


router = APIRouter(prefix="/api/{user_id}/chat", tags=["chat"])


async def get_messages(session: AsyncSession, conversation_id: int, user_id: int) -> List[Message]:
    res = await session.execute(
        select(Message).where(Message.conversation_id == conversation_id, Message.user_id == user_id).order_by(Message.created_at)
    )
    return res.scalars().all()


@router.post("", response_model=ChatResponse)
async def chat(
    user_id: int,
    payload: ChatRequest,
    session: AsyncSession = Depends(get_session),
) -> ChatResponse:
    # TODO: replace with real auth that checks token.user_id == user_id
    # Conversation
    convo: Conversation
    if payload.conversation_id:
        convo = await session.get(Conversation, payload.conversation_id)
        if not convo or convo.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    else:
        convo = Conversation(user_id=user_id)
        session.add(convo)
        await session.commit()
        await session.refresh(convo)

    # store user message
    user_msg = Message(user_id=user_id, conversation_id=convo.id, role="user", content=payload.message)
    session.add(user_msg)
    await session.commit()

    # load history (trim last 20)
    history = await get_messages(session, convo.id, user_id)
    history = history[-20:]
    agent_messages = [{"role": m.role, "content": m.content} for m in history]

    # tools schema placeholder (Agents SDK tool schema expected)
    tools_schema = []

    try:
        reply_text, tool_calls = await run_agent(agent_messages, tools_schema)
    except Exception as e:
        # Fallback to avoid 500s if LLM/tool call fails
        reply_text = "Sorry, I couldn't process that right now."
        tool_calls = []
        # Optionally log the error
        print("run_agent error:", e)

    # store assistant message
    assistant_msg = Message(user_id=user_id, conversation_id=convo.id, role="assistant", content=reply_text or "")
    session.add(assistant_msg)
    await session.commit()

    return ChatResponse(conversation_id=convo.id, response=reply_text or "", tool_calls=tool_calls or [])
