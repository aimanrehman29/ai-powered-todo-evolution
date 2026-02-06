# Frontend Guidelines
- Next.js 16 App Router, TypeScript, Tailwind 4
- Use server components by default; client when interactivity needed
- API calls go through src/lib/api.ts
- Include Authorization: Bearer token and user_id path
- Env: NEXT_PUBLIC_API_BASE=http://127.0.0.1:8000

## Run
npm run dev
