"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";
import { login, signup } from "@/lib/api";

export default function SignupPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await signup(email, password);
      const res = await login(email, password);
      localStorage.setItem("token", res.access_token);
      localStorage.setItem("user_id", String(res.user_id));
      router.push("/tasks");
    } catch (err) {
      const message = err instanceof Error ? err.message : "Signup failed";
      setError(message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page-shell min-h-screen grid place-items-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white">
      <div className="relative max-w-md w-full">
        <div className="pointer-events-none absolute inset-0 blur-2xl bg-gradient-to-r from-indigo-500/30 via-fuchsia-500/20 to-cyan-400/25" />
        <form
          onSubmit={onSubmit}
          className="relative z-10 card w-full p-8 space-y-5 bg-white/95 dark:bg-slate-900/90 border border-white/40 shadow-2xl rounded-2xl"
        >
          <div className="space-y-2 text-center">
            <p className="text-sm uppercase tracking-wide text-slate-500">Join us</p>
            <h1 className="text-3xl font-semibold text-slate-900 dark:text-slate-50">Sign up</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400">Create your account to sync tasks securely.</p>
          </div>
          {error && <p className="text-sm text-red-500 text-center">{error}</p>}
          <div className="space-y-3">
            <input
              className="w-full border border-slate-200 dark:border-slate-700 focus:border-[var(--accent)] focus:ring-2 focus:ring-[var(--accent)]/15 p-3 rounded-lg transition bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100"
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              className="w-full border border-slate-200 dark:border-slate-700 focus:border-[var(--accent)] focus:ring-2 focus:ring-[var(--accent)]/15 p-3 rounded-lg transition bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100"
              type="password"
              placeholder="Password (min 8 chars)"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button className="w-full btn-primary disabled:opacity-70" type="submit" disabled={loading}>
            {loading ? "Creating account..." : "Sign up"}
          </button>
          <p className="text-sm text-slate-600 dark:text-slate-400 text-center">
            Have an account?{" "}
            <a className="text-[var(--accent-strong)] font-medium hover:underline" href="/login">
              Log in
            </a>
          </p>
        </form>
      </div>
    </main>
  );
}
