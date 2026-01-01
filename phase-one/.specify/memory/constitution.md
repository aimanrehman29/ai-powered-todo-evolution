# Evolution of Todo Constitution

## Core Principles

### I. Spec-First Delivery
Every change begins with a spec and plan grounded in user intent. Code updates must trace back to the active feature spec, and deviations require an amended spec before implementation.

### II. CLI Clarity
Commands use verb-noun patterns with explicit help text, clear exit codes, and human-readable output. Errors go to stderr; normal results go to stdout.

### III. Testable Units
Business logic lives in importable modules with deterministic behavior. Each public function is unit-testable without CLI parsing or I/O side effects.

### IV. In-Memory Simplicity
Data stays in memory for Phase I. Avoid persistence, background daemons, and unnecessary dependencies; prefer standard library utilities.

### V. Small, Reversible Changes
Prefer the smallest viable diffs. Keep functions short, avoid premature abstractions, and document any complexity that cannot be simplified.

## Delivery Constraints
- Language: Python 3.13; prefer standard library only.
- Storage: In-memory only for tasks; no files or external databases.
- UX: Single-process CLI usable via `python -m todo` or `python -m todo <command>`.
- Observability: Minimal structured messages for user output; avoid hidden side effects.

## Workflow Expectations
- Sequence: spec → plan → tasks → implement → test → document.
- Each feature includes acceptance criteria and runnable examples in README.
- Tests accompany non-trivial logic; CLI parsing is thin and delegates to services.
- Document run commands and expected outputs for manual verification.

## Governance
This constitution guides all feature work for Evolution of Todo. Amendments require updating this file with rationale and dates, and aligning open specs and plans to the new rules.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
