"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Moon, Sun, Sparkles, Bot, Send, ListChecks } from "lucide-react";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://127.0.0.1:8000";

type Theme = "dark" | "light";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

interface ChatResponse {
  conversation_id: number;
  response: string;
  tool_calls: any[];
}

export default function Home() {
  const [userId, setUserId] = useState("1");
  const [conversationId, setConversationId] = useState<number | null>(null);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [theme, setTheme] = useState<Theme>("dark");
  const listRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages]);

  const canSend = useMemo(() => input.trim().length > 0 && !loading, [input, loading]);

  async function sendMessage() {
    if (!canSend) return;
    setLoading(true);
    setError(null);
    const nextMessages: ChatMessage[] = [...messages, { role: "user" as const, content: input.trim() }];
    setMessages(nextMessages);
    const body = {
      message: input.trim(),
      conversation_id: conversationId,
    };
    try {
      const res = await fetch(`${API_BASE}/api/${userId}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(text || res.statusText);
      }
      const data: ChatResponse = await res.json();
      setConversationId(data.conversation_id);
      setMessages([
        ...nextMessages,
        { role: "assistant" as const, content: data.response || "(no reply)" },
      ]);
      setInput("");
    } catch (e: any) {
      setError(e.message || "Request failed");
      setMessages(nextMessages);
    } finally {
      setLoading(false);
    }
  }

  function handleKey(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  const bg = theme === "dark" ? "bg-slate-950 text-slate-50" : "bg-slate-50 text-slate-900";
  const card = theme === "dark" ? "bg-slate-900/80 border-slate-800" : "bg-white border-slate-200";
  const sidebar = theme === "dark" ? "bg-slate-900/60 border-slate-800" : "bg-white border-slate-200";
  const inputBg = theme === "dark" ? "bg-slate-900 text-slate-100" : "bg-white text-slate-900";
  const bubbleUser = theme === "dark" ? "bg-indigo-500 text-white" : "bg-indigo-500 text-white";
  const bubbleBot =
    theme === "dark"
      ? "bg-slate-800 text-slate-100 border border-slate-700"
      : "bg-slate-100 text-slate-900 border border-slate-200";

  return (
    <div className={`min-h-screen ${bg} flex items-center justify-center p-4 transition-colors`}>
      <div className="w-full max-w-6xl grid md:grid-cols-[240px_1fr] gap-4">
        {/* Sidebar */}
        <aside className={`rounded-2xl ${sidebar} border shadow-lg p-4 flex flex-col gap-4`}>
          <div className="flex items-center gap-2">
            <div className="h-10 w-10 rounded-2xl bg-indigo-500/20 flex items-center justify-center text-indigo-400">
              <Bot size={20} />
            </div>
            <div>
              <p className="text-xs text-slate-400">Phase III</p>
              <p className="font-semibold">AI Todo Chat</p>
            </div>
          </div>

          <div className="flex items-center justify-between rounded-xl border border-slate-700/40 px-3 py-2">
            <span className="text-sm">Theme</span>
            <button
              onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
              className="flex items-center gap-2 rounded-lg px-3 py-2 bg-indigo-500/10 text-indigo-400 hover:bg-indigo-500/20 transition"
            >
              {theme === "dark" ? <Sun size={16} /> : <Moon size={16} />}
              {theme === "dark" ? "Light" : "Dark"}
            </button>
          </div>

          <div className="space-y-2 text-sm">
            <p className="text-slate-400">Quick prompts</p>
            {[
              "Add a task to buy milk",
              "Show my pending tasks",
              "Mark task 3 as complete",
              "Update task 2 to call mom tonight",
            ].map((q) => (
              <button
                key={q}
                onClick={() => setInput(q)}
                className="w-full text-left rounded-lg border border-slate-700/30 px-3 py-2 hover:border-indigo-400/60 hover:text-indigo-300 transition"
              >
                {q}
              </button>
            ))}
          </div>

          <div className="mt-auto space-y-2">
            <p className="text-xs text-slate-400">User ID</p>
            <input
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              className="w-full rounded-lg border border-slate-700/40 bg-slate-800/30 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
            />
          </div>
        </aside>

        {/* Chat area */}
        <div className={`rounded-2xl ${card} border shadow-xl overflow-hidden flex flex-col`}>
          <header className="flex items-center gap-3 px-6 py-4 border-b border-slate-800/60 bg-gradient-to-r from-indigo-500/20 via-blue-500/10 to-transparent">
            <div className="h-10 w-10 rounded-2xl bg-indigo-500/20 flex items-center justify-center text-indigo-400">
              <Sparkles size={18} />
            </div>
            <div>
              <p className="text-xs text-slate-400">Chat</p>
              <p className="font-semibold flex items-center gap-2">
                Todo Assistant <ListChecks size={16} className="text-indigo-400" />
              </p>
            </div>
            <div className="ml-auto text-xs text-slate-500">
              Backend: {API_BASE.replace(/^https?:\/\//, "")}
            </div>
          </header>

          <div ref={listRef} className="flex-1 overflow-y-auto px-6 py-5 space-y-4">
            {messages.length === 0 && (
              <div className="text-center text-slate-400 text-sm">
                Start by sending a message like &quot;Add a task to buy milk&quot;.
              </div>
            )}
            {messages.map((m, i) => (
              <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                <div className={`max-w-[80%] whitespace-pre-wrap rounded-2xl px-4 py-3 text-sm shadow-lg ${m.role === "user" ? bubbleUser : bubbleBot}`}>
                  {m.content}
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start">
                <div className={`px-4 py-3 text-sm rounded-2xl ${bubbleBot} animate-pulse`}>
                  Thinking…
                </div>
              </div>
            )}
          </div>

          <div className="border-t border-slate-800/60 bg-slate-900/40 px-6 py-4 space-y-2">
            {error && (
              <div className="text-sm text-rose-300 bg-rose-950/40 border border-rose-800 rounded-lg px-3 py-2">
                {error}
              </div>
            )}
            <div className="flex gap-3">
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKey}
                rows={2}
                placeholder="Type a message…"
                className={`flex-1 resize-none rounded-xl border border-slate-800 bg-slate-900 px-4 py-3 text-sm shadow-inner focus:outline-none focus:ring-2 focus:ring-indigo-400 ${inputBg}`}
              />
              <button
                onClick={sendMessage}
                disabled={!canSend}
                className="self-end inline-flex items-center gap-2 rounded-xl bg-indigo-500 px-4 py-3 text-sm font-semibold text-white shadow-lg shadow-indigo-500/30 transition hover:bg-indigo-400 disabled:opacity-50"
              >
                <Send size={16} />
                Send
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
