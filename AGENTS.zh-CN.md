# Eyu AI 入口

> 本文件是根 AI 入口的中文源文件。修改根规则时先改这里，再同步 `AGENTS.md`。
> 其他中文源位于 `docs/agents/zh-CN/`、`docs/tasks/zh-CN/` 和 `.agents/skills/*/SKILL.zh-CN.md`。

## 1. 核心原则

Eyu 是使用 C++20 从零实现脚本语言的学习仓库。当前根构建只包含 `app/main.cpp` 的 `eyu` CLI，测试只覆盖 `--help` 与 `--version`；扫描器、解析器、AST、字节码、虚拟机、运行时和垃圾回收仍是路线图，不能因 README 或目录存在而视为已实现。

AI 在本仓库工作时必须：

- 先读本文件，再按任务只加载需要的 `docs/agents/*.md`。
- 修改前运行 `git status --short --branch`，不要覆盖、回滚、stash 或清理用户已有工作。
- 以实时源码、CMake 和测试为权威；README 路线图只表达目标。
- 默认采用 PR-first：从非默认分支通过 Squash merge 进入 `main`；发布前必须通过轻量 `quality-gate`。
- 未经用户明确授权，不直推 `main`、把 draft PR 转为 ready 或合并 PR。
- 语言行为改动必须配套最小相关测试；编译成功不能证明语义正确。
- 引用教材、规范、论文或参考实现时说明来源、版本和学习目的。
- 每次实质改动都报告实际验证命令、结果和覆盖范围。

## 2. 上下文路由

- 总索引：`docs/agents/index.md`
- CMake、编译器、构建和测试：`docs/agents/build.md`
- 分支、commit、推送和 PR：`docs/agents/git.md`
- clang-format、注释和 format-only：`docs/agents/formatting.md`
- 符号、调用链和重构影响面：`docs/agents/codegraph.md`
- 学习计划、语言设计证据和资料来源：`docs/agents/learning.md`

共享 workflow skill：`.agents/skills/eyu-workflow/SKILL.md`。

## 3. 关键路径

- `CMakeLists.txt`、`CMakePresets.json`：实时构建入口和 preset 权威。
- `app/main.cpp`：当前 CLI 实现入口。
- `src/`：规划中的语言实现模块；是否接入以实时 CMake 为准。
- `tests/`：测试入口。
- `.clang-format`：C++ 格式权威。
- `docs/agents/`、`.agents/skills/`：长期上下文与共享工作流。
- `.github/workflows/pr-quality.yml`：标题、diff、同步与 preset 的轻量门禁。
- `tools/`：同步和 PR policy 工具。

## 4. 默认验证

Agent 文档或 skill 改动：

```bash
python3 ./tools/sync-agents.py --check
git diff --check
```

Windows PowerShell：

```powershell
.\tools\sync-agents.ps1 -Check
```

C++、CMake 或测试改动按影响范围运行最小验证。默认完整入口：

```bash
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

## 5. 项目口令

### `=sa`

根据中文源同步所有英文 Agent 文件和 skill 元数据。先运行同步脚本生成 marker 提示，只修改英文目标，最后运行同步检查。

### `=ca`

只运行平台适用的同步检查，不修改文件；失败时提示运行 `=sa`。

### `=ai`

把稳定、可复用且有证据的 Eyu 上下文写入正确中文源：根规则放 `AGENTS.zh-CN.md`，专项知识放 `docs/agents/zh-CN/`，共享工作流放 `SKILL.zh-CN.md`。默认不创建单次任务状态文档；只有用户明确要求持久化时才使用 `docs/tasks/`。不要保存临时猜测、聊天流水、秘密或可从实时文件发现的动态清单。

### `=br <用途>`

按 `docs/agents/git.md` 创建 `<type>/<english-kebab-description>` 分支。默认从当前 `HEAD` 创建并保留未提交改动；同名引用存在时停止询问。只创建分支，不提交或推送。

### `=gc`

严格只读地检查状态、完整 diff、未跟踪文件、验证与风险；不暂存、提交、推送或创建 PR。

### `=cm`

只暂存本次目标文件并提交到当前本地分支。普通 commit 正文可省略；breaking change、`chore(wip)` 或重大兼容性/runtime 风险必须写中文正文。不要推送或创建 PR。

### `=gh`

按 `=cm` 规则提交，运行 PR policy checker，推送当前非默认任务分支，填写模板并创建 draft PR，等待 `quality-gate`。未经另外授权，不转 ready 或合并。

## 6. 同步规则

中文文件是人类维护源，英文文件是默认 AI 入口：

- `AGENTS.zh-CN.md` -> `AGENTS.md`
- `docs/agents/zh-CN/*.md` -> `docs/agents/*.md`
- `docs/tasks/zh-CN/*.md` -> `docs/tasks/*.md`
- `.agents/skills/*/SKILL.zh-CN.md` -> `.agents/skills/*/SKILL.md`

英文目标必须有唯一且匹配的 SHA256 marker，不得残留中文正文。`agents/openai.yaml` 必须与英文 `SKILL.md` 的 hash、skill 名称和界面字段一致。中文与英文冲突时以中文为准；中文 skill 源使用 `SKILL.zh-CN.md`，不要创建 `zh-CN/SKILL.md`。
