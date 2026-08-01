# Eyu Agent Entry
<!-- AGENTS_ZH_CN_SHA256: e026b3630ca73531b1556bb767655112a9131df405e3dc287aacc3b5f409928b -->

> `AGENTS.zh-CN.md` is the Chinese source for this root entry.
> Other Chinese sources live in `docs/agents/zh-CN/`, `docs/tasks/zh-CN/`, and `.agents/skills/*/SKILL.zh-CN.md`.

## 1. Core Rules

Eyu is a C++20 learning repository for building a scripting language from scratch. The live root build currently contains only the `eyu` CLI from `app/main.cpp`, and tests cover only `--help` and `--version`. The scanner, parser, AST, bytecode, VM, runtime, and garbage collector remain roadmap items.

When working in this repository:

- Read this file first, then load only the required `docs/agents/*.md` context.
- Run `git status --short --branch` before edits. Do not overwrite, revert, stash, or clean user work.
- Treat live source, CMake, and tests as authoritative. README roadmap text expresses goals only.
- Use PR-first delivery by default. Changes enter `main` from a non-default branch through Squash merge and must pass the lightweight `quality-gate`.
- Do not push to `main`, mark a draft PR ready, or merge without explicit user authorization.
- Pair language behavior changes with focused tests; compilation alone does not prove semantics.
- State source, version, and learning purpose when using external material.
- Report the exact validation commands, results, and covered scope for meaningful changes.

## 2. Context Router

- Index: `docs/agents/index.md`
- CMake, compilers, builds, and tests: `docs/agents/build.md`
- Branches, commits, pushes, and PRs: `docs/agents/git.md`
- clang-format, comments, and format-only work: `docs/agents/formatting.md`
- Symbols, call chains, and refactor impact: `docs/agents/codegraph.md`
- Learning plans, language-design evidence, and sources: `docs/agents/learning.md`

Shared workflow skill: `.agents/skills/eyu-workflow/SKILL.md`.

## 3. Key Paths

- `CMakeLists.txt` and `CMakePresets.json`: live build and preset authority.
- `app/main.cpp`: current CLI implementation.
- `src/`: planned language modules; confirm live CMake integration.
- `tests/`: test entrypoints.
- `.clang-format`: C++ formatting authority.
- `docs/agents/` and `.agents/skills/`: durable context and shared workflows.
- `.github/workflows/pr-quality.yml`: lightweight title, diff, sync, and preset gate.
- `tools/`: synchronization and PR policy tools.

## 4. Default Validation

After changing agent documents or skills:

```bash
python3 ./tools/sync-agents.py --check
git diff --check
```

Windows PowerShell:

```powershell
.\tools\sync-agents.ps1 -Check
```

For C++, CMake, or test changes, run the smallest relevant validation. The default full entrypoint is:

```bash
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

## 5. Project Commands

### `=sa`

Synchronize English agent files and skill metadata from Chinese sources. Generate the marker prompt first, edit only English targets, then run the sync check.

### `=ca`

Run only the platform-appropriate synchronization check. Do not modify files; tell the user to run `=sa` if it fails.

### `=ai`

Store stable, reusable, evidence-backed Eyu context in the correct Chinese owner: root rules in `AGENTS.zh-CN.md`, focused knowledge in `docs/agents/zh-CN/`, and shared workflow in `SKILL.zh-CN.md`. Do not create task-state documents by default; use `docs/tasks/` only when the user explicitly requests persistence. Do not preserve guesses, transcripts, secrets, or inventories discoverable from live files.

### `=br <purpose>`

Follow `docs/agents/git.md` to create a `<type>/<english-kebab-description>` branch. Create from current `HEAD` by default, preserve uncommitted work, and stop if the ref exists. Create only; do not commit or push.

### `=gc`

Run a strictly read-only publication preflight covering status, complete diff, untracked files, validation, and risk. Do not stage, commit, push, or create a PR.

### `=cm`

Stage only current-task files and commit locally. Normal commit bodies are optional; breaking changes, `chore(wip)`, or material compatibility/runtime risk require a Chinese body. Do not push or create a PR.

### `=gh`

Commit under `=cm`, run the PR policy checker, push the current non-default task branch, complete the template, create a draft PR, and wait for `quality-gate`. Do not mark ready or merge without separate authorization.

## 6. Synchronization Rules

Chinese files are human-maintained sources; English files are the default AI entrypoints:

- `AGENTS.zh-CN.md` -> `AGENTS.md`
- `docs/agents/zh-CN/*.md` -> `docs/agents/*.md`
- `docs/tasks/zh-CN/*.md` -> `docs/tasks/*.md`
- `.agents/skills/*/SKILL.zh-CN.md` -> `.agents/skills/*/SKILL.md`

English targets need one current SHA256 marker and no untranslated Chinese body text. `agents/openai.yaml` must match the English `SKILL.md` hash, skill name, and interface fields. Chinese wins on conflict. Use `SKILL.zh-CN.md` for Chinese skill sources; never create `zh-CN/SKILL.md`.
