# Authentication

Use Better Auth on Next.js to issue JWT; FastAPI verifies with shared secret BETTER_AUTH_SECRET / JWT_SECRET.

## Flows
- Signup: email, password -> create user, return JWT and user_id.
- Login: email, password -> JWT and user_id.
- All API calls include Authorization: Bearer token.

## Claims
- sub = user_id
- exp = configured expiry
