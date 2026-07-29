# Eyu Agent Context Index
<!-- AGENT_DOCS_INDEX_ZH_CN_SHA256: 90535adbc002e15c2206b683569bb987d1a6a66ef165a22238fbbb2fc9438d83 -->

Read root `AGENTS.md` first, then select the smallest useful context from this router.

## Router

- CMake, compilers, builds, tests, or build failures: `docs/agents/build.md`
- Branches, commits, pushes, PRs, or publication checks: `docs/agents/git.md`
- Learning plans, language design, sources, topic state, or conversation distillation: `docs/agents/learning.md`

## Default Flow

1. Inspect `git status --short --branch`.
2. Decide whether the task is build, Git, learning/design, or direct source implementation.
3. Load only the matching context. If no focused pack exists, inspect live source directly.
4. Report validation commands, results, and scope after changes.

## Do Not

- Do not treat the README roadmap as implemented behavior.
- Do not assume a directory under `src/` is connected to the root build.
- Do not turn temporary discussion or unsettled designs into durable rules.
