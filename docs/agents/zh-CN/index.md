# Eyu Agent 上下文索引

先读根 `AGENTS.md`，再从本路由中选择最小必要上下文。

## 路由

- CMake、编译器、构建、测试或构建错误：`docs/agents/build.md`
- 分支、commit、推送、PR 或发布检查：`docs/agents/git.md`
- 学习计划、语言设计、资料来源、主题状态或对话沉淀：`docs/agents/learning.md`

## 默认流程

1. 查看 `git status --short --branch`。
2. 确认任务属于构建、Git、学习/设计，还是直接源码实现。
3. 只加载匹配的上下文；缺少专项包时直接检查实时源码。
4. 修改后报告验证命令、结果和覆盖范围。

## 不要

- 不要把 README 的路线图当成已实现能力。
- 不要因为 `src/` 中存在目录就假设它已接入根构建。
- 不要把临时讨论或未决定设计写成长期规则。
