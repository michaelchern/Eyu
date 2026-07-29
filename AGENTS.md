# Eyu Agent Entry
<!-- AGENTS_ZH_CN_SHA256: 7abfaf3fc30fb201029bb6470574931afd1434470cd55caad8ce3871ffe263f3 -->

> `AGENTS.zh-CN.md` is the Chinese source for this root AI entry.
> Other Chinese sources live in `docs/agents/zh-CN/`, `docs/tasks/zh-CN/`, and `.agents/skills/*/SKILL.zh-CN.md`.
> English files are the default AI entrypoints and must stay aligned with the Chinese sources.

## 1. Core Rules

Eyu is a C++20 learning repository for implementing a scripting language from scratch. The live root CMake project currently builds only the `eyu` CLI from `app/main.cpp`, and tests only `--help` and `--version`. The scanner, parser, AST, bytecode, VM, runtime, and garbage collector remain roadmap items; planned directories or README text do not prove that they are implemented.

When working in this repository:

- Read this file first, then load only the relevant file from `docs/agents/`.
- Check `git status --short --branch` before edits. Never revert or overwrite user changes.
- Treat live source, `CMakeLists.txt`, `CMakePresets.json`, and tests as authoritative. The README roadmap expresses goals only.
- Keep context narrow instead of loading build, Git, and learning state together by default.
- Preserve clear scanner, parser, compiler, bytecode, VM, and runtime responsibilities. Do not add abstractions before a concrete need exists.
- Pair language behavior changes with the smallest relevant tests. Compilation alone does not prove behavior.
- State the source, version, and learning purpose when using books, papers, or other interpreter implementations.
- Report validation commands, results, and the exact scope covered for every meaningful change.

## 2. Context Router

- Index and context selection: `docs/agents/index.md`
- CMake, compilers, builds, and tests: `docs/agents/build.md`
- Branches, commits, pushes, and PRs: `docs/agents/git.md`
- Learning plans, language-design evidence, and durable state: `docs/agents/learning.md`

Shared project skill:

- `.agents/skills/eyu-workflow/SKILL.md`: repository workflow, project commands, and context routing.

Add focused scanner, parser, bytecode, or runtime context only after the corresponding implementation becomes stable. Do not create empty context packs in advance.

## 3. Key Paths

- `CMakeLists.txt`: root build authority.
- `CMakePresets.json`: shared configure, build, and test presets.
- `app/main.cpp`: current CLI implementation entrypoint.
- `src/`: planned language implementation modules; verify live CMake and source before claiming they are connected.
- `tests/`: unit, integration, and language behavior tests.
- `docs/agents/`: durable AI context loaded on demand.
- `docs/tasks/`: committable topic state, evidence, failed explorations, and validation recipes.
- `.agents/skills/`: shared project skills.
- `tools/`: agent sync checks and lightweight project tools.

## 4. Default Validation

After changing agent documents or skills, run:

```bash
python3 ./tools/sync_agents.py --check
git diff --check
```

On Windows, use `py -3` or a Python 3 `python` command if `python3` is unavailable.

For C++, CMake, or test changes, run the smallest relevant validation. The default full entrypoint is:

```bash
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

Docs-only changes normally do not require a rebuild. When build commands are first recorded or changed, verify them directly.

## 5. Project Commands

Commands use the `=` prefix to avoid conflicts with slash commands and mention syntax.

### `=sa`

Synchronize every English agent file from its Chinese source. Do not modify Chinese sources. Keep English concise, update each SHA256 marker, and finish with `python3 ./tools/sync_agents.py --check`.

### `=ca`

Run only `python3 ./tools/sync_agents.py --check`. Do not edit files. Report missing targets, stale markers, orphaned English files, or untranslated Chinese body text.

### `=ai`

Distill stable, reusable Eyu context from recent conversations into project AI materials.

- Inspect the worktree and search existing owners and older conclusions first.
- Preserve only content that reduces future misreads, fixes a validation entrypoint, or records a settled design.
- Put root rules in `AGENTS.zh-CN.md`, durable focused knowledge in `docs/agents/zh-CN/*.md`, topic state and evidence in `docs/tasks/zh-CN/*.md`, and shared workflows or commands in `SKILL.zh-CN.md`.
- Treat facts discoverable from live code or configuration as live-file data instead of duplicating full inventories.
- Do not promote undecided syntax ideas, temporary guesses, one-off logs, raw chat history, or secrets into durable rules.
- Synchronize the matching English files and run the sync check after editing Chinese sources.

### `=br <purpose>`

Create and switch to a local `<type>/<english-kebab-description>` branch. Inspect the current branch, worktree, and known refs first. Create from the current `HEAD` by default while preserving uncommitted changes. Stop if the name exists; do not append a suffix automatically. Do not commit or push.

### `=gc`

Check publication readiness only: inspect status, diffs, untracked files, and relevant validation. Do not stage, commit, push, or create a PR.

### `=cm`

Commit only files clearly owned by the current task to the local branch. Do not default to `git add .`. Use a concise title and a Chinese body explaining what changed, why, and what was verified. Do not push or create a PR.

### `=gh`

Check and commit the intended files, push the current branch, and create a draft PR. Stop on failed validation unless the user explicitly asks to continue.

## 6. Sync Rule

Chinese files are human-maintained sources; English files are default AI entrypoints:

- `AGENTS.zh-CN.md` -> `AGENTS.md`
- `docs/agents/zh-CN/*.md` -> `docs/agents/*.md`
- `docs/tasks/zh-CN/*.md` -> `docs/tasks/*.md`
- `.agents/skills/*/SKILL.zh-CN.md` -> `.agents/skills/*/SKILL.md`

Every English file must contain a SHA256 marker matching its Chinese source normalized to UTF-8/LF. If the two languages conflict, the Chinese source wins. Do not create `.agents/skills/*/zh-CN/SKILL.md`, because it may be discovered as a duplicate skill.
