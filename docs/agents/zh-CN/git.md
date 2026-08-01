# Eyu Git Workflow Context

只在 `=br`、`=gc`、`=cm`、`=gh`、分支、提交、推送、PR 或发布检查任务中加载本文件。

## 交付原则

- 默认 PR-first；`main` 只接受 Squash merge，并要求 strict `quality-gate`。
- 一个分支和 PR 只处理一个清晰目标；保留已有分支、worktree 与未提交改动。
- 未经用户明确授权，不直推 `main`、转 ready、合并或发布。
- 必要验证失败时不得正常提交或发布；用户明确要求时可创建本地 `chore(wip): ...` 检查点，但不得 push 或建 PR。

## 分支命名

使用 `<type>/<english-kebab-description>`，不添加工具名、用户名或日期。允许 `feat/fix/docs/refactor/perf/test/build/ci/style/chore/revert/spike`；`spike` 只用于本地实验。描述只含小写字母、数字和单连字符，完整名称不超过 63 字符，并通过 `git check-ref-format --branch`。

## Commit 与 PR 标题

```text
<type>(<scope>)!: <中文简述>
```

scope 与 `!` 可省略。可发布 type 为 `feat/fix/refactor/perf/docs/test/build/ci/style/chore/revert`。描述必须包含中文并说明结果；`spike`、`wip:` 和 `chore(wip):` 不可发布。

普通本地 commit 正文可省略。以下情况必须写中文正文：

- breaking change：增加 `BREAKING CHANGE:`，说明影响和迁移。
- `chore(wip)`：记录失败命令和阻断原因。
- 重大兼容性、语言 runtime 或回滚风险：说明风险和缓解。

完整范围、验证、未验证项、风险和回滚以 PR Description 为权威记录。

## 验证门禁

- 暂存前检查完整 diff 和未跟踪文件；暂存后运行 `git diff --cached --check`。
- 发布前运行 `python3 ./tools/check_pr_policy.py --title "<PR 标题>" --base <base>`。
- Agent 文档运行同步检查；C++/CMake/测试按 build 与 formatting 上下文运行最小验证。
- `quality-gate` 固定检查 policy、PR diff、Agent 同步和 CMake preset 解析；它不替代本地编译或语言行为测试。

## 口令行为

- `=br`：检查状态和引用，从当前 `HEAD` 创建分支并保留未提交改动；同名存在时停止。只创建，不提交。
- `=gc`：只读检查状态、完整 diff、未跟踪文件、验证和风险；不改变 Git 状态。
- `=cm`：只暂存目标文件，检查 staged diff，完成必要验证后本地提交并停止。
- `=gh`：确认当前为可发布非默认分支，按 `=cm` 提交，运行 policy checker，推送并创建 draft PR，等待 `quality-gate`。

不得默认 `git add .`、覆盖无关改动、发布失败验证、推送 `spike/*`，或在没有用户额外授权时转 ready/合并。
