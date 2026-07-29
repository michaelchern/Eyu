---
name: eyu-workflow
description: Repository workflow for AI agents working in the Eyu C++20 scripting-language learning project. Use when editing Eyu, handling =sa/=ca/=ai/=br/=gc/=cm/=gh commands, routing to build/Git/learning context, recording language-design evidence, or validating project changes.
---
<!-- EYU_WORKFLOW_SKILL_ZH_CN_SHA256: f09458f0c3c2bce87e607e0cd53a3a6fe03989c7571a0f6d96dd65a39a411748 -->

# Eyu Workflow

Use this workflow to keep repository work scoped, evidence-based, and recoverable across AI agents.

## Start

1. Read root `AGENTS.md`.
2. Inspect `git status --short --branch` before edits.
3. Load only the relevant file from `docs/agents/`.
4. Treat live code, CMake, and tests as authoritative; the README roadmap is not implementation evidence.
5. Keep changes scoped to the user request and report validation results.

## Command Routing

- `=sa`: synchronize all English agent files from Chinese sources.
- `=ca`: check whether all English agent files are synchronized.
- `=ai`: distill stable Eyu context from recent conversations.
- `=br <purpose>`: create and switch to a conventionally named local branch.
- `=gc`: check publication readiness without changing Git state.
- `=cm`: commit intended changes to the current local branch only.
- `=gh`: commit intended changes and publish a draft PR.

For `=sa` and `=ca`, use `python3 ./tools/sync_agents.py`. On Windows, use `py -3` or a Python 3 `python` command when `python3` is unavailable. The script discovers Chinese-source pairs and checks normalized SHA256 markers, missing targets, orphaned English files, duplicate markers, and untranslated Chinese body text.

For `=ai`:

1. Inspect the worktree and preserve user changes.
2. Search the owning document and older conclusions before writing.
3. Preserve only settled, reusable content that reduces future misreads, fixes a validation entrypoint, or records an explicit project decision.
4. Put repository rules in `AGENTS.zh-CN.md`, durable domain context in `docs/agents/zh-CN/*.md`, topic state and evidence in `docs/tasks/zh-CN/*.md`, and shared workflows or commands in `SKILL.zh-CN.md`.
5. Keep candidate, settled, and implemented language designs distinct. Implemented behavior must point to live code and tests.
6. Treat versions, target lists, and paths discoverable from live files as live-file data instead of duplicating full inventories.
7. Do not preserve temporary guesses, undecided syntax debates, one-off logs, raw chat history, or secrets.
8. Synchronize matching English files and run `python3 ./tools/sync_agents.py --check` after editing Chinese sources.

For `=br`, `=gc`, `=cm`, and `=gh`, also read `docs/agents/git.md`.

## Context Routing

- CMake, compilers, builds, and tests: `docs/agents/build.md`
- Branches, commits, pushes, and PRs: `docs/agents/git.md`
- Learning, language design, sources, and topic state: `docs/agents/learning.md`

If a focused context pack does not exist, inspect live files directly and state assumptions. Add a new context pack only after a domain has stable implementation facts or a repeated misread risk.

## Language Implementation Boundaries

- Do not infer implemented scanner, parser, AST, bytecode, VM, runtime, or GC behavior from planned directories or README text.
- Preserve explicit module responsibilities and add new abstractions only for a concrete current need.
- Pair language behavior changes with focused tests. Compilation alone is insufficient evidence.
- Record external books, specifications, papers, or reference implementations with source, version, relevant section, and learning purpose.
- Keep external designs as references unless Eyu explicitly adopts them.

## Long-Running Work

Use `docs/tasks/zh-CN/study-template.md` for topic state, next actions, evidence, failed explorations, and validation. Preserve concise recovery information rather than session transcripts. Distill only stable results into long-lived context.

## Non-Negotiables

- Never revert or overwrite user changes unless explicitly asked.
- Never stage unrelated files or default to `git add .`.
- Do not push failed validation unless the user explicitly asks to continue.
- Do not claim roadmap features are implemented without live code and test evidence.
- Use `SKILL.zh-CN.md` for Chinese skill sources; do not create `zh-CN/SKILL.md`, which may be discovered as a duplicate skill.
