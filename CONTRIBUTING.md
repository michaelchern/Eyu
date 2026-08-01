<p align="right"><strong>简体中文</strong> · <a href="CONTRIBUTING.en.md">English</a></p>

# Eyu 贡献指南

Eyu 是 C++20 脚本语言学习仓库。实时构建目标与语言行为以源码、CMake 和测试为准；详细 Agent 规则见 `AGENTS.md`。

## 开始之前

- 查看 `git status --short --branch`，保留已有分支、worktree 和未提交改动。
- 一个分支和 PR 只处理一个目标；不要提交凭证、个人数据、无关生成文件或意外二进制资源。
- 默认从非默认任务分支通过 PR 进入 `main`，不要直推 `main`。

## 分支与提交

分支使用 `<type>/<english-kebab-description>`。commit 与 PR 标题使用：

```text
<type>(<scope>)!: <中文简述>
```

允许 `feat/fix/refactor/perf/docs/test/build/ci/style/chore/revert`。普通 commit 正文可省略；breaking change、`chore(wip)` 或重大兼容性/runtime 风险必须写中文正文。`spike/*` 与 WIP commit 不得发布。

## 验证

- 发布前：`python3 ./tools/check_pr_policy.py --title "<PR 标题>" --base <base>`。
- Agent 文档：`python3 ./tools/sync-agents.py --check`。
- CMake：至少运行 `cmake --list-presets=all`，并按改动范围配置、构建和测试。
- 语言行为：增加最小相关测试或 `.eyu` 行为验证。
- 暂存后：`git diff --cached --check`。

不要把未执行的验证写成已通过。必要验证失败时不得正常提交或发布；明确需要防丢检查点时才可创建本地 `chore(wip): ...`。

## Pull Request

填写 `.github/PULL_REQUEST_TEMPLATE.md` 的摘要、包含/不包含范围、实际与未执行验证、风险和回滚。默认创建 draft PR 并等待 `quality-gate`。`main` 只使用 Squash merge；未经明确授权，不转 ready 或合并。

仓库不要求 DCO、签名提交、CODEOWNERS、自动 Code Review 或完整 C++ 构建 CI。
