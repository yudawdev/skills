# Before Dev Workflow Reference

## Quick Checklist

- Confirm whether user requested worktree/parallel development
- Identify default branch (`origin/main` or `origin/master`)
- Fetch from remote
- Create new branch from `origin/<default>`
- Start development only after branch/worktree is ready

## Edge Cases

- Local `main` or `master` diverged from `origin/<default>`
  - Do not merge by default
  - Base the new branch on `origin/<default>`
  - Ask the user if they want local `main` updated, and whether to rebase or merge

- No `origin/main` or `origin/master`
  - Ask the user to specify the base branch name

- Worktree requested
  - Ask for preferred worktree path if not provided
  - Use: `git worktree add -b <branch> <path> origin/<default>`

## Branch Name Examples

- feature/add-user-onboarding
- fix/login-redirect-loop
- docs/update-api-setup
- refactor/simplify-tool-parser
- chore/update-deps-2026-01-28

## Suggested Prompting (Bilingual)

- "我会先同步最新的 main/master 并创建新分支，然后再开始开发。需要我用哪个分支名？"
- "I will sync the latest main/master and create a new branch before coding. What branch name should I use?"
