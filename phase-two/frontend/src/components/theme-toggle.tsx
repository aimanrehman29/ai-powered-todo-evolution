"use client";

import { useTheme } from "./theme-provider";

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  const btn =
    "inline-flex items-center gap-2 px-3 py-2 rounded-full border text-sm font-medium transition";

  return (
    <div className="fixed right-4 top-4 z-50 flex items-center gap-2 bg-white/70 dark:bg-slate-900/70 backdrop-blur px-2 py-2 rounded-full shadow-md">
      <button
        type="button"
        onClick={() => setTheme("light")}
        className={`${btn} ${
          theme === "light"
            ? "bg-white text-slate-800 border-slate-200 shadow"
            : "bg-transparent text-slate-500 border-transparent hover:bg-white/60"
        }`}
      >
        ☀️ Light
      </button>
      <button
        type="button"
        onClick={() => setTheme("dark")}
        className={`${btn} ${
          theme === "dark"
            ? "bg-slate-800 text-slate-100 border-slate-700 shadow"
            : "bg-transparent text-slate-500 border-transparent hover:bg-slate-800/40"
        }`}
      >
        🌙 Dark
      </button>
    </div>
  );
}
