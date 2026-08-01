---
name: eyu-workflow
description: Vendor-neutral workflow for the Eyu C++20 scripting-language learning repository. Use when an agent edits Eyu, handles =sa/=ca/=ai/=br/=gc/=cm/=gh, or needs routing to CMake, Git, formatting, codegraph, or learning context.
---
<!-- EYU_WORKFLOW_SKILL_ZH_CN_SHA256: 1f64d65e7b9c1f39f5e079a16ff0c5f9d9c6530fdbd3343debe067fa5cce1335 -->

# Eyu Workflow

## Start

1. Read root `AGENTS.md`.
2. Inspect `git status --short --branch` before edits.
3. Confirm facts from live source, CMake, and tests.
4. Load only relevant `docs/agents/` context.
5. Keep scope narrow and report exact validation.

## Commands

- `=sa`: synchronize English Agent files and skill metadata from Chinese sources.
- `=ca`: run only the synchronization check.
- `=ai`: preserve stable, evidence-backed Eyu context.
- `=br <purpose>`: create a conventionally named local branch while preserving changes.
- `=gc`: run a strictly read-only publication preflight.
- `=cm`: commit only intended files locally.
- `=gh`: commit, push, and create a GitHub draft PR.

Use `python3 ./tools/sync-agents.py` or the PowerShell counterpart for `=sa/=ca`. Read `docs/agents/git.md` before `=br/=gc/=cm/=gh`.

## Routing

- CMake, builds, tests: `docs/agents/build.md`
- Git and GitHub: `docs/agents/git.md`
- clang-format and comments: `docs/agents/formatting.md`
- Symbols and impact: `docs/agents/codegraph.md`
- Learning, language design, sources: `docs/agents/learning.md`

## Delivery Contract

- Use `<type>/<english-kebab-description>` branches.
- Use `<type>(<scope>)!: <Chinese description>` commit and PR subjects.
- Normal commit bodies are optional; breaking changes, WIP, or material risk require a body.
- Never default to `git add .`, publish `chore(wip)`, or push directly to `main`.
- `=gh` runs policy checks, completes the template, creates a draft PR, and waits for `quality-gate`.
- Do not mark ready or merge without explicit authorization.

## Boundaries

- Do not infer scanner, parser, AST, bytecode, VM, runtime, or GC implementation from roadmap text.
- Add abstractions only for concrete needs and prove language behavior with tests.
- Record source, version, chapter, and purpose for external material.
- Do not create task-state documents by default; use `docs/tasks/` only when explicitly requested.
- Never overwrite, revert, stash, or clean user changes; never stage unrelated files or overstate validation.
- Use `SKILL.zh-CN.md` for Chinese skill sources, never `zh-CN/SKILL.md`.
