"use client";

import { useRouter } from "next/navigation";
import { useCallback, useEffect, useState } from "react";
import { createTask, deleteTask, listTasks, toggleTask } from "@/lib/api";

type Task = { id: number; title: string; description: string; status: "open" | "done" };

export default function TasksPage() {
  const router = useRouter();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [token, setToken] = useState<string | null>(null);
  const [userId, setUserId] = useState<number | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const stored = typeof window !== "undefined" ? localStorage.getItem("token") : null;
    const storedUserId = typeof window !== "undefined" ? localStorage.getItem("user_id") : null;
    setToken(stored);
    setUserId(storedUserId ? Number(storedUserId) : null);
    setReady(true);
  }, []);

  const refresh = useCallback(async (currentToken: string) => {
    if (!currentToken || userId == null) return;
    try {
      const data = await listTasks(currentToken, userId);
      setTasks(data);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Failed to load tasks";
      setError(message);
      if (String(message).includes("401")) router.push("/login");
    }
  }, [router, userId]);

  useEffect(() => {
    if (!ready) return;
    if (!token || userId == null) {
      router.push("/login");
      return;
    }
    refresh(token);
  }, [ready, token, userId, refresh, router]);

  async function onCreate(e: React.FormEvent) {
    e.preventDefault();
    if (!token || userId == null || !title.trim()) return;
    setError("");
    setLoading(true);
    try {
      await createTask(token, userId, title, description);
      setTitle("");
      setDescription("");
      await refresh(token);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Create failed";
      setError(message);
    } finally {
      setLoading(false);
    }
  }

  async function onToggle(id: number) {
    if (!token || userId == null) return;
    await toggleTask(token, userId, id);
    await refresh(token);
  }

  async function onDelete(id: number) {
    if (!token || userId == null) return;
    await deleteTask(token, userId, id);
    await refresh(token);
  }

  function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user_id");
    router.push("/login");
  }

  if (!ready) return null;

  return (
    <main className="page-shell grid min-h-screen place-items-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
      <div className="w-full max-w-3xl space-y-4">
        <div className="card p-6 bg-white/95 dark:bg-slate-900/85">
          <header className="mb-4 space-y-1 text-center">
            <p className="text-sm uppercase tracking-wide text-slate-500">Today</p>
            <h1 className="text-3xl font-semibold">My Tasks</h1>
          </header>
          <form onSubmit={onCreate} className="space-y-3">
            {error && <p className="text-sm text-red-500 text-center">{error}</p>}
            <input
              className="w-full border border-slate-200 dark:border-slate-800 focus:border-[var(--accent)] focus:ring-2 focus:ring-[var(--accent)]/15 p-3 rounded-lg transition bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100"
              placeholder="Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
            <textarea
              className="w-full border border-slate-200 dark:border-slate-800 focus:border-[var(--accent)] focus:ring-2 focus:ring-[var(--accent)]/15 p-3 rounded-lg transition bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100"
              placeholder="Description (optional)"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
            <button className="btn-primary w-full inline-flex items-center justify-center disabled:opacity-70" type="submit" disabled={loading}>
              {loading ? "Adding..." : "Add Task"}
            </button>
            <button className="w-full text-sm text-red-500 hover:text-red-600 mt-1" type="button" onClick={logout}>
              Log out
            </button>
          </form>
        </div>

        <section className="card p-6 bg-white/95 dark:bg-slate-900/85 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold text-slate-900 dark:text-slate-50">Task Board</h2>
            <span className="pill text-xs">{tasks.length} tasks</span>
          </div>
          <div className="grid gap-3">
            {tasks.map((t) => (
              <div
                key={t.id}
                className="border border-slate-100 dark:border-slate-800 rounded-xl p-4 bg-white dark:bg-slate-800/80 flex items-start justify-between gap-3"
              >
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <p className="font-semibold text-slate-900 dark:text-slate-100">{t.title}</p>
                    <span className="pill text-xs">
                      {t.status === "open" ? "Open" : "Done"}
                    </span>
                  </div>
                  {t.description && <p className="text-sm text-slate-600 dark:text-slate-300">{t.description}</p>}
                </div>
                <div className="flex gap-2 shrink-0">
                  <button
                    className="text-sm px-3 py-1 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition"
                    onClick={() => onToggle(t.id)}
                  >
                    {t.status === "open" ? "Mark done" : "Reopen"}
                  </button>
                  <button
                    className="text-sm px-3 py-1 rounded-lg bg-rose-100 text-rose-800 hover:bg-rose-200 transition"
                    onClick={() => onDelete(t.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
            {tasks.length === 0 && (
              <div className="border border-dashed border-slate-300 dark:border-slate-700 rounded-xl p-6 text-center text-slate-500">
                No tasks yet. Add your first task to get started.
              </div>
            )}
          </div>
        </section>
      </div>
    </main>
  );
}
