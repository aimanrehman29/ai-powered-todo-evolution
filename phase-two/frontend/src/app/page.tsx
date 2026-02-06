/*import Link from "next/link";

export default function Home() {
  return (
    <main className="page-shell grid place-items-center">
      <div className="card max-w-xl w-full p-8 space-y-5 bg-white/92">
        <p className="text-sm uppercase tracking-wide text-slate-500"></p>
        <h1 className="text-3xl font-semibold text-slate-900">Todo App</h1>
        <p className="text-slate-600">
         Your Day, Organized.
        </p>
        <div className="flex gap-3">
          <Link href="/login" className="btn-primary flex-1 text-center">
            Log in
          </Link>
          <Link
            href="/signup"
            className="flex-1 text-center rounded-xl border border-[var(--accent)] px-4 py-3 text-[var(--accent-strong)] font-semibold hover:bg-[var(--accent)]/10 transition"
          >
            Sign up
          </Link>
        </div>
      </div>
    </main>
  );
}
*/
import Link from "next/link";

export default function Home() {
  return (
    <main className="page-shell grid min-h-screen place-items-center bg-gradient-to-br from-indigo-900 via-purple-900 to-slate-900 text-white">
      <div className="relative max-w-xl w-full">
        <div className="absolute inset-0 blur-3xl bg-gradient-to-r from-indigo-400/30 via-fuchsia-400/20 to-cyan-400/25" />
        <div className="relative card bg-white/95 text-slate-900 p-10 space-y-7 border border-white/60 shadow-2xl rounded-3xl">
          <div className="flex items-center gap-2 text-xs font-semibold text-indigo-700">
            <span className="px-3 py-1 rounded-full bg-indigo-50">Phase II</span>
            <span className="px-3 py-1 rounded-full bg-slate-100 text-slate-600">Full-stack</span>
          </div>
          <div className="space-y-3">
            <h1 className="text-3xl sm:text-4xl font-semibold leading-tight text-slate-900">
              Your day, beautifully organized.
            </h1>
            <p className="text-slate-600 text-lg">
              FastAPI + Next.js + Neon with JWT security. Light/dark aware, responsive, ready to ship.
            </p>
          </div>
          <div className="flex flex-col sm:flex-row gap-3">
            <Link href="/login" className="btn-primary flex-1 text-center">
              Log in
            </Link>
            <Link
              href="/signup"
              className="flex-1 text-center rounded-xl border border-indigo-200 px-4 py-3 text-indigo-700 font-semibold hover:bg-indigo-50 transition"
            >
              Sign up
            </Link>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-sm text-slate-600">
            <div className="p-3 rounded-lg bg-slate-50 border border-slate-100">Secure JWT auth</div>
            <div className="p-3 rounded-lg bg-slate-50 border border-slate-100">FastAPI + Neon DB</div>
            <div className="p-3 rounded-lg bg-slate-50 border border-slate-100">Responsive UI</div>
          </div>
        </div>
      </div>
    </main>
  );
}
