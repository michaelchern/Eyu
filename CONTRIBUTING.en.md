<p align="right"><a href="CONTRIBUTING.md">简体中文</a> · <strong>English</strong></p>

# Contributing to Eyu

Eyu is a C++20 scripting-language learning repository. Live source, CMake, and tests define implemented behavior. See `AGENTS.md` for detailed agent rules.

## Before Starting

- Inspect `git status --short --branch` and preserve existing branches, worktrees, and uncommitted work.
- Keep one clear goal per branch and PR. Do not commit credentials, personal data, unrelated generated files, or accidental binaries.
- Deliver through a PR from a non-default task branch. Do not push directly to `main`.

## Branches and Commits

Branches use `<type>/<english-kebab-description>`. Commit and PR subjects use:

```text
<type>(<scope>)!: <Chinese description>
```

Publishable types are `feat/fix/refactor/perf/docs/test/build/ci/style/chore/revert`. Normal commit bodies are optional; breaking changes, `chore(wip)`, or material compatibility/runtime risk require a Chinese body. `spike/*` and WIP commits are local-only.

## Validation

- Publication policy: `python3 ./tools/check_pr_policy.py --title "<PR title>" --base <base>`.
- Agent material: `python3 ./tools/sync-agents.py --check`.
- CMake: run at least `cmake --list-presets=all`, then configure, build, and test in proportion to the change.
- Language behavior: add focused tests or `.eyu` behavior validation.
- Staged diff: `git diff --cached --check`.

Never report an unrun check as passed. Failed required validation cannot be committed normally or published; only an explicitly requested local `chore(wip): ...` checkpoint is allowed.

## Pull Requests

Complete `.github/PULL_REQUEST_TEMPLATE.md` with scope, actual and omitted validation, risk, and rollback. Create a draft PR and wait for `quality-gate`. `main` uses Squash merge only; do not mark ready or merge without explicit authorization.

The repository does not require DCO, signed commits, CODEOWNERS, automated code review, or a full C++ build CI.
