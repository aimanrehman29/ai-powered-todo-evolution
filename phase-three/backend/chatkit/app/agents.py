from __future__ import annotations

import os
from typing import List, Tuple

import google.generativeai as genai

# System prompt to enrich responses and mark urgency
SYSTEM_PROMPT = (
    "You are Todo Assistant. Keep replies under 80 words and practical. "
    "If the user mentions urgency (urgent, asap, important, now, high priority), "
    "prefix with '🔥 Urgent:' and give a terse action plan (bullets acceptable). "
    "Do not invent tasks that were not mentioned."
)

# We repurpose OPENAI_* envs for Gemini per user request.
GEMINI_KEY = os.environ.get("OPENAI_API_KEY")
GEMINI_MODEL = os.environ.get("OPENAI_MODEL", "gemini-2.5-flash")

if not GEMINI_KEY:
    raise RuntimeError("OPENAI_API_KEY (Gemini key) is required")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)


async def run_agent(messages: List[dict], tools: List[dict]) -> Tuple[str, List[dict]]:
    """
    Lightweight Gemini runner. Tool calls are not wired; returns text only.
    messages: [{"role": "user"/"assistant", "content": str}, ...]
    tools: ignored for now (Gemini function calling wiring TBD)
    """
    transcript = SYSTEM_PROMPT + "\n\n"
    for m in messages:
        prefix = "User:" if m["role"] == "user" else "Assistant:"
        transcript += f"{prefix} {m['content']}\n"
    resp = model.generate_content(transcript.strip())
    reply = resp.text or ""
    return reply, []  # tool_calls empty until Gemini tool-calling is added
