---
id: 008
title: Claude guide update
stage: misc
date: 2026-01-02
surface: agent
model: gpt-5
feature: none
branch: master
user: user
command: codex-cli session
labels: [documentation, guide]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - CLAUDE.md
tests:
 - none
---

## Prompt

<environment_context>
  <cwd>c:\aiman rehman\ai driven development\hackthone2-101</cwd>
  <approval_policy>never</approval_policy>
  <sandbox_mode>danger-full-access</sandbox_mode>
  <network_access>enabled</network_access>
  <shell>powershell</shell>
</environment_context>

/sp.implement claude‑guide

Generate a CLAUDE.md file that explains:
- How to use Spec‑Kit Plus for this project
- How to run all /sp commands
- How to generate code via Claude Code
- Example workflows for each phase

## Response snapshot

Updated CLAUDE.md with Spec-Kit Plus quickstart, /sp command usage, code-generation guidance, and example phase-by-phase workflows tailored to the todo CLI project.

## Outcome

- ƒo. Impact: Added concise how-to guide for Spec-Kit Plus and Claude Code usage.
- dY¦ Tests: none
- dY"? Files: CLAUDE.md updated.
- dY"? Next prompts: None pending.
- dYÿ Reflection: Guidance stays project-specific and aligned with existing structure.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): N/A
