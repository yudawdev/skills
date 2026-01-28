---
name: before-dev
description: Ensure development starts from the latest main/master, create a new branch (or worktree when requested), then begin coding. Use when the user asks for new changes or a new feature, says "start a new task", "new requirement", "new changes", or in Chinese "现在帮我开发一个新的需求" / "现在要进行新的改动"; also trigger when the user mentions worktree or parallel development.
---

# Before Dev

## Overview

Enforce a pre-dev workflow: sync from the latest default branch, create a new branch (or worktree), then proceed with the requested work. Provide both Chinese and English acknowledgements when replying.

## Workflow Decision Tree

1) Detect intent
- If user mentions worktree or parallel development, create a worktree first.
- Otherwise, use the current repo workspace.

2) Confirm base branch
- Prefer `origin/main`; if missing, use `origin/master`.
- If neither exists, ask the user which base branch to use.

3) Sync from remote
- Run `git fetch origin`.
- If local `main`/`master` is diverged, do not merge by default; create the new branch from `origin/<default>`.
- If user asks to update local `main`/`master`, ask whether to rebase or merge.

4) Create branch
- If user provides a branch name, use it.
- Otherwise, propose a branch name based on the request summary and confirm.

5) Start development
- Only after the branch/worktree is ready.

## Branch Naming Guidance

- Choose a prefix based on intent: `feature/`, `fix/`, `chore/`, `docs/`, `refactor/`, `hotfix/`.
- Use a concise, kebab-case summary.
- Keep under ~50 characters when possible.
- If the user gives a summary, auto-generate and confirm.

## Required Responses (Bilingual)

- Acknowledge the pre-dev step in Chinese and English.
- Ask for missing inputs (branch name, base branch, worktree path) in Chinese and English.

## Command Recipes

- Detect default branch:
  - `git symbolic-ref refs/remotes/origin/HEAD`
- Create branch from remote base:
  - `git checkout -b <branch> origin/main`
- Worktree flow:
  - `git worktree add -b <branch> <path> origin/main`

## References

- See `references/before-dev-workflow.md` for detailed steps and edge cases.
- Use `scripts/suggest_branch_name.py` to generate a branch name from a summary.
- See `assets/branch-name-examples.txt` for naming examples.
