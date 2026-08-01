# Eyu Git Workflow Context
<!-- AGENT_DOCS_GIT_ZH_CN_SHA256: c8cd8fe24de2b2c6b1dc6ef0f43fb20492c8dcd828da003f0447d75a0e679f33 -->

Load only for `=br`, `=gc`, `=cm`, `=gh`, branches, commits, pushes, PRs, or publication checks.

## Delivery

- Use PR-first delivery. `main` accepts Squash merge only and requires strict `quality-gate`.
- One branch and PR handle one clear goal. Preserve existing branches, worktrees, and uncommitted work.
- Do not push to `main`, mark ready, merge, or publish without explicit authorization.
- Failed required validation cannot be committed normally or published. An explicitly requested `chore(wip): ...` checkpoint stays local.

## Branches and Subjects

Branches use `<type>/<english-kebab-description>` with no tool, user, or date prefix. Use lowercase letters, digits, and single hyphens, keep the name at most 63 characters, and validate it with Git. `spike/*` is local-only.

Commit and PR subjects use:

```text
<type>(<scope>)!: <Chinese description>
```

Scope and `!` are optional. Publishable types are `feat/fix/refactor/perf/docs/test/build/ci/style/chore/revert`. Descriptions must contain Chinese. `spike`, `wip:`, and `chore(wip):` are not publishable.

Normal local commit bodies are optional. A Chinese body is required for breaking changes, WIP checkpoints, or material compatibility/runtime/rollback risk. The PR Description is authoritative for scope, validation, omissions, risk, and rollback.

## Gates and Commands

- Review the full diff and untracked files before staging; run `git diff --cached --check` afterward.
- Before publication run `python3 ./tools/check_pr_policy.py --title "<PR title>" --base <base>`.
- Run agent sync checks and the smallest relevant CMake, source, or test validation.
- `quality-gate` checks policy, PR diff, Agent synchronization, and CMake preset parsing. It does not replace local builds or language behavior tests.
- `=br` creates from current `HEAD` by default and preserves changes; it never commits.
- `=gc` is read-only.
- `=cm` stages only target files, validates, commits locally, and stops.
- `=gh` requires a publishable non-default branch, applies `=cm`, checks policy, pushes, creates a draft PR, and waits for `quality-gate`.

Never default to `git add .`, overwrite unrelated work, publish failed validation, publish `spike/*`, or mark ready/merge without separate user authorization.
