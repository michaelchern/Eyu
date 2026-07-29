# Eyu Git Workflow Context
<!-- AGENT_DOCS_GIT_ZH_CN_SHA256: b3783a6f811b0e06f7bbe5fcdfa75e7db09240c8ee640d6863c85dc49cc597b3 -->

Load this file only for `=br`, `=gc`, `=cm`, `=gh`, branch, commit, push, PR, or publication-check tasks.

## Branch Naming

Use `<type>/<english-kebab-description>` without tool, user, or date prefixes. Allowed types:

- `feat`: new language or tool behavior.
- `fix`: incorrect behavior fixes.
- `docs`: documentation, agent material, or learning records only.
- `refactor`: structure changes without external behavior changes.
- `perf`: performance or resource improvements.
- `test`: tests and test data.
- `build`: CMake, dependencies, presets, or toolchains.
- `style`: formatting, comments, or text-style-only changes.
- `chore`: other repository maintenance.
- `spike`: temporary language experiments or technical validation.

Use only lowercase letters, digits, and single hyphens in the description. Keep the full name at most 63 characters and validate it with `git check-ref-format --branch`.

## `=br <purpose>`

1. Inspect the current branch, `HEAD`, and worktree state.
2. Check known local and remote refs without automatically fetching for naming.
3. Derive and validate the branch name.
4. Stop if the ref exists. Do not append a suffix or switch to an existing branch automatically.
5. Create from current `HEAD` with `git switch -c` by default. Preserve uncommitted changes; do not stash, reset, clean, or revert.
6. Create and switch only. Do not commit, push, or create a PR.

## `=gc`

- Do not modify files.
- Inspect `git status --short --branch`, relevant diffs, and untracked files.
- Run the sync check for agent files and the smallest relevant validation for source, CMake, or tests.
- Report intended files, risks, and validation results.

## `=cm`

- Inspect status, diffs, and validation results.
- Stage only current-task files. Do not default to `git add .`.
- Run `git diff --cached --check` and relevant validation after staging.
- Use a concise title and a Chinese body explaining what changed, why, and what was verified.
- Stop after the local commit. Do not push or create a PR.

## `=gh`

- Perform the `=gc` scope checks and relevant validation.
- Commit uncommitted work under the `=cm` rules.
- Push the current branch to `origin` and create a draft PR.
- Report branch, commit, PR URL, and validation results.

## Safety Rules

- Preserve unrelated worktree changes and never stage unrelated files.
- Do not push failed validation unless the user explicitly asks to continue.
- `=cm` never pushes or creates a PR. `=gh` creates a draft PR by default.
