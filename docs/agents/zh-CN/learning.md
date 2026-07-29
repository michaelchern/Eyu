# Eyu Learning Context

只在学习计划、语言设计、资料研究、概念解释、主题状态或长期沉淀任务中加载本文件。

## 知识归属

- 仓库级长期规则：`AGENTS.zh-CN.md`
- 长期专项上下文：`docs/agents/zh-CN/*.md`
- 某个主题的状态、证据、失败探索和验证：`docs/tasks/zh-CN/*.md`
- 共享工作流、口令和意图识别：`.agents/skills/eyu-workflow/SKILL.zh-CN.md`

## 语言设计证据

- 区分“候选设计”“已决定设计”和“已实现行为”。三者不能混写。
- 已实现行为必须能指向实时代码和测试。
- 已决定但未实现的设计应记录动机、约束、替代方案和实现前提。
- 未决定方案保留在主题 task 的 Active Items 或 Failed Explorations 中，不升级为根规则。
- 引用 Crafting Interpreters、论文、语言规范或其他实现时，记录来源、版本/commit、相关章节和学习目的。
- 外部实现是参考，不自动成为 Eyu 的架构约束。

## 长任务状态

主题记录优先使用 `docs/tasks/zh-CN/study-template.md`，至少维护：

- Current facts
- Top next action
- Active items
- Evidence
- Failed explorations
- Validation

只保存可恢复、可验证、对下一次工作有帮助的内容。不要提交原始聊天记录、临时命令流水或没有结论的脑暴。

## 教学与实现风格

- 解释概念时先说它解决什么问题，再说明实现机制和 Eyu 中的最小落点。
- 先实现语义正确、结构清晰且可测试的最小版本，再考虑优化。
- 用户表示没看懂时，先用具体源代码、Token、AST、栈或字节码执行过程解释，再给形式化定义。
