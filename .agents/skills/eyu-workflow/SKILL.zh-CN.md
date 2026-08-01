---
name: eyu-workflow
description: Eyu C++20 脚本语言学习仓库的通用工作流。Agent 编辑 Eyu、处理 =sa/=ca/=ai/=br/=gc/=cm/=gh，或需要路由 CMake、Git、formatting、codegraph 与学习上下文时使用。
---

# Eyu Workflow

## 开始

1. 阅读根 `AGENTS.md`。
2. 编辑前查看 `git status --short --branch`。
3. 从实时源码、CMake 和测试确认事实。
4. 只加载相关 `docs/agents/` 上下文。
5. 保持改动范围并报告准确验证结果。

## 口令路由

- `=sa`：从中文源同步英文 Agent 文件和 skill 元数据。
- `=ca`：只运行同步检查。
- `=ai`：沉淀稳定、有证据的 Eyu 上下文。
- `=br <用途>`：创建规范命名的本地分支并保留未提交改动。
- `=gc`：严格只读的发布预检。
- `=cm`：只提交当前目标文件到本地分支。
- `=gh`：提交、推送并创建 GitHub draft PR。

`=sa` / `=ca` 使用 `python3 ./tools/sync-agents.py` 或 PowerShell 对应入口。`=br/=gc/=cm/=gh` 前读取 `docs/agents/git.md`。

## 上下文路由

- CMake、构建、测试：`docs/agents/build.md`
- Git 与 GitHub：`docs/agents/git.md`
- clang-format 与注释：`docs/agents/formatting.md`
- 符号和影响面：`docs/agents/codegraph.md`
- 学习、语言设计、资料来源：`docs/agents/learning.md`

## Git 交付

- 分支使用 `<type>/<english-kebab-description>`。
- commit/PR 标题使用 `<type>(<scope>)!: <中文简述>`。
- 普通 commit 正文可省略；breaking、WIP 或重大风险必须写正文。
- 不默认 `git add .`，不发布 `chore(wip)`，不直推 `main`。
- `=gh` 必须运行 policy checker、填写 PR 模板、创建 draft PR 并等待 `quality-gate`。
- 未经用户明确授权，不转 ready 或合并。

## 语言实现边界

- 不从 README 或规划目录推断 scanner、parser、AST、bytecode、VM、runtime 或 GC 已实现。
- 只为当前需求增加抽象；语言行为必须用测试证明。
- 引用外部材料时记录来源、版本、章节和学习目的。
- 默认不为单次任务创建状态文档；用户明确要求时才使用 `docs/tasks/`。

## 不可违反

- 不覆盖、回滚、stash、clean 用户改动。
- 不暂存无关文件，不扩大验证结论。
- 中文 skill 源使用 `SKILL.zh-CN.md`，不要创建 `zh-CN/SKILL.md`。
