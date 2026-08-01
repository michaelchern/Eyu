# Eyu Learning Context
<!-- AGENT_DOCS_LEARNING_ZH_CN_SHA256: 541495d4827f5e66562c07ab908aa21ff4921874eebbf0fa574f9cc27f9bcc57 -->

Load this file only for learning plans, language design, source research, concept explanations, topic state, or durable knowledge tasks.

## Knowledge Ownership

- Repository-wide durable rules: `AGENTS.zh-CN.md`
- Durable focused context: `docs/agents/zh-CN/*.md`
- Topic state, evidence, failed explorations, and validation may use `docs/tasks/zh-CN/*.md` only when the user explicitly requests persistence.
- Shared workflows, commands, and intent recognition: `.agents/skills/eyu-workflow/SKILL.zh-CN.md`

## Language-Design Evidence

- Keep candidate designs, settled designs, and implemented behavior distinct.
- Implemented behavior must point to live code and tests.
- A settled but unimplemented design should record motivation, constraints, alternatives, and implementation prerequisites.
- Keep unsettled options in a topic task's Active Items or Failed Explorations instead of promoting them to root rules.
- When using Crafting Interpreters, papers, language specifications, or other implementations, record the source, version or commit, relevant section, and learning purpose.
- External implementations are references, not automatic Eyu architecture constraints.

## Long-Running Topic State

Use `docs/tasks/zh-CN/study-template.md` only when the user explicitly requests a repository task document. Maintain at least:

- Current facts
- Top next action
- Active items
- Evidence
- Failed explorations
- Validation

Keep active state in the current conversation by default. Preserve only recoverable, verifiable content that helps the next work session. Do not commit raw chat transcripts, temporary command streams, or unresolved brainstorming.

## Teaching and Implementation Style

- Explain the problem a concept solves before its mechanism and smallest Eyu implementation.
- Implement the smallest semantically correct, clear, testable version before optimizing.
- When the user is confused, use concrete source, tokens, ASTs, stacks, or bytecode execution before formal definitions.
