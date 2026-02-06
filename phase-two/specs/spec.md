# Feature Specification: Full-Stack Todo Application (Phase II)

**Feature Branch**: `[phase-two-fullstack]`  
**Created**: 2026-02-04  
**Status**: Draft  
**Input**: User description: "Full-stack web app with Next.js frontend, FastAPI backend, JWT auth, and Neon Postgres persistence."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Authenticate and Maintain Session (Priority: P1)

As a user I can sign up, log in, and stay authenticated via JWT so my requests are authorized and scoped to me.

**Why this priority**: All other features depend on authenticated context; must be reliable and secure.

**Independent Test**: Call `/auth/signup` then `/auth/login` to receive a JWT; use it on `/tasks` and get a 200 instead of 401.

**Acceptance Scenarios**:
1. **Given** valid credentials, **When** I log in, **Then** I receive a JWT with expiry and can call `/tasks` successfully.
2. **Given** an invalid or expired token, **When** I call `/tasks`, **Then** I receive 401 with a clear error message.

---

### User Story 2 - Create and List My Tasks (Priority: P1)

As an authenticated user I can create tasks with title/description and list only my own tasks.

**Why this priority**: Core product value; must enforce user isolation from the start.

**Independent Test**: POST `/tasks` with JWT, then GET `/tasks` and see only tasks owned by that user.

**Acceptance Scenarios**:
1. **Given** a valid token, **When** I create a task, **Then** it stores with status `open` and returns the task with my user ID.
2. **Given** another user’s token, **When** they list tasks, **Then** they never see tasks from other users.

---

### User Story 3 - Update, Complete, and Delete Tasks (Priority: P2)

As an authenticated user I can update my tasks’ fields, toggle completion, and delete them.

**Why this priority**: Essential lifecycle operations once creation/listing work.

**Independent Test**: Update title/description, toggle completion, delete task, then GET `/tasks` to confirm changes.

**Acceptance Scenarios**:
1. **Given** I own a task, **When** I PATCH its title, **Then** the response reflects the new title and `updated_at` changes.
2. **Given** I toggle a task, **When** I fetch it, **Then** `status` flips between `open` and `done`.
3. **Given** I delete my task, **When** I list tasks, **Then** it no longer appears.

---

### User Story 4 - Responsive Frontend (Priority: P2)

As a user I can manage tasks via a responsive web UI on desktop and mobile.

**Why this priority**: Usability and accessibility are required for adoption.

**Independent Test**: Navigate to the app, log in, create/update/toggle/delete tasks with visible confirmation; layout adapts under 768px.

**Acceptance Scenarios**:
1. **Given** I open the app on mobile width, **When** I view the task list, **Then** layout is readable and controls are usable.
2. **Given** I perform CRUD actions in the UI, **When** they succeed, **Then** the UI updates without stale data.

---

### Edge Cases
- Expired or malformed JWT → 401 with clear error; no data leakage.
- Duplicate email on signup → 409 conflict.
- Missing required fields on task creation → 400 with validation details.
- Accessing another user’s task by ID → 404 (not found) without revealing existence.
- Database connectivity failure → 503 with retry-safe response.
- Token replay after logout/rotation → rejected per configured policy (to be defined in plan).

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: Users MUST be able to sign up and log in to obtain a JWT; passwords stored hashed.
- **FR-002**: All task CRUD endpoints MUST require a valid JWT and scope operations to the token’s user.
- **FR-003**: System MUST support create, list (per user), update (partial), toggle completion, and delete for tasks.
- **FR-004**: Frontend MUST provide forms and views for auth and task CRUD, updating optimistically or after confirmed responses.
- **FR-005**: Duplicate user emails MUST be rejected with a clear error.
- **FR-006**: Unauthorized or expired tokens MUST yield 401; forbidden cross-user access MUST yield 404/403 without leaking data.
- **FR-007**: Task payloads MUST include id, title, description, status (`open`|`done`), user_id, and timestamps.
- **FR-008**: API responses MUST be JSON with consistent error shape (code, message).

### Key Entities
- **User**: `id`, `email` (unique), `password_hash`, `created_at`.
- **Task**: `id`, `user_id`, `title`, `description`, `status`, `created_at`, `updated_at`.
- **Auth Token (JWT)**: subject = user id, includes expiry; signed with server secret.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: Authenticated requests to `/tasks` succeed with 200; unauthenticated return 401.
- **SC-002**: Cross-user access attempts never return another user’s task (404/403).
- **SC-003**: Frontend CRUD flows work on desktop and mobile widths without layout breakage.
- **SC-004**: Backend tests cover auth and task CRUD; frontend has at least one integration test for happy-path CRUD.
