# Eyu Learning Context
<!-- AGENT_DOCS_LEARNING_ZH_CN_SHA256: 2c8ccaee1164c6ba0bc358a15831c7dfd473e924cf1b9c1858a41b98f5acb3ab -->

Load this file only for learning plans, language design, source research, concept explanations, topic state, or durable knowledge tasks.

## Knowledge Ownership

- Repository-wide durable rules: `AGENTS.zh-CN.md`
- Durable focused context: `docs/agents/zh-CN/*.md`
- Topic state, evidence, failed explorations, and validation: `docs/tasks/zh-CN/*.md`
- Shared workflows, commands, and intent recognition: `.agents/skills/eyu-workflow/SKILL.zh-CN.md`

## Language-Design Evidence

- Keep candidate designs, settled designs, and implemented behavior distinct.
- Implemented behavior must point to live code and tests.
- A settled but unimplemented design should record motivation, constraints, alternatives, and implementation prerequisites.
- Keep unsettled options in a topic task's Active Items or Failed Explorations instead of promoting them to root rules.
- When using Crafting Interpreters, papers, language specifications, or other implementations, record the source, version or commit, relevant section, and learning purpose.
- External implementations are references, not automatic Eyu architecture constraints.

## Long-Running Topic State

Prefer `docs/tasks/zh-CN/study-template.md` and maintain at least:

- Current facts
- Top next action
- Active items
- Evidence
- Failed explorations
- Validation

Preserve only recoverable, verifiable content that helps the next work session. Do not commit raw chat transcripts, temporary command streams, or unresolved brainstorming.

## Teaching and Implementation Style

- Explain the problem a concept solves before its mechanism and smallest Eyu implementation.
- Implement the smallest semantically correct, clear, testable version before optimizing.
- When the user is confused, use concrete source, tokens, ASTs, stacks, or bytecode execution before formal definitions.
