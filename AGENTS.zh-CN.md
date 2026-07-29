# Eyu AI 入口

> 本文件是根 AI 入口的中文源文件。修改根规则时，先改这里，再同步更新 `AGENTS.md`。
> 其他中文源位于 `docs/agents/zh-CN/`、`docs/tasks/zh-CN/` 和 `.agents/skills/*/SKILL.zh-CN.md`。
> 英文文件是 AI 默认读取入口，必须与中文源保持一致。

## 1. 核心原则

Eyu 是一个使用 C++20 从零实现脚本语言的学习仓库。当前根 CMake 只构建 `app/main.cpp` 中的 `eyu` CLI，测试只覆盖 `--help` 和 `--version`；扫描器、解析器、AST、字节码、虚拟机、运行时和垃圾回收仍属于路线图，不能因为目录或 README 中存在规划就视为已实现。

AI 在本仓库工作时必须：

- 先读本文件，再按任务读取 `docs/agents/*.md`。
- 修改前查看 `git status --short --branch`，不要回滚或覆盖用户已有改动。
- 以实时源码、`CMakeLists.txt`、`CMakePresets.json` 和测试为权威；README 路线图只表达目标。
- 只加载当前任务需要的上下文，避免把构建、Git 和学习状态一次性塞满上下文。
- 保持扫描器、解析器、编译器、字节码、虚拟机和运行时职责清晰，不要提前引入尚无需求的抽象。
- 语言行为改动必须配套最小相关测试；实现成功不能只靠编译通过证明。
- 引用教材、论文或其他解释器实现时，说明来源、版本和学习目的，不要无说明地大段复制。
- 每次实质改动都报告验证命令、结果和实际覆盖范围。

## 2. 上下文路由

按任务只读需要的文件：

- 总索引和上下文选择：`docs/agents/index.md`
- CMake、编译器、构建和测试：`docs/agents/build.md`
- 分支、提交、推送和 PR：`docs/agents/git.md`
- 学习计划、语言设计证据和长期状态：`docs/agents/learning.md`

项目内共享 Agent skill：

- `.agents/skills/eyu-workflow/SKILL.md`：仓库工作流、项目口令和上下文路由。

当扫描器、解析器、字节码或运行时形成稳定实现后，再增加相应专项上下文；不要提前创建空文档。

## 3. 关键路径

- `CMakeLists.txt`：根构建入口和目标权威。
- `CMakePresets.json`：共享 configure、build 和 test preset。
- `app/main.cpp`：当前唯一 CLI 实现入口。
- `src/`：规划中的语言实现模块；是否已接入以实时 CMake 和源码为准。
- `tests/`：单元测试、集成测试和语言行为测试入口。
- `docs/agents/`：按需加载的长期 AI 上下文。
- `docs/tasks/`：可提交的主题状态、证据、失败探索和验证配方。
- `.agents/skills/`：项目共享 Agent skill。
- `tools/`：Agent 同步检查和轻量项目工具。

## 4. 默认验证

Agent 文档或 skill 改动后运行：

```bash
python3 ./tools/sync_agents.py --check
git diff --check
```

Windows 环境若没有 `python3` 命令，可使用 `py -3` 或指向 Python 3 的 `python` 执行同一脚本。

C++、CMake 或测试改动按需运行最小相关验证，默认完整入口为：

```bash
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

纯文档改动通常不要求重新构建。首次记录或修改构建命令时，应实际验证对应入口。

## 5. 项目口令

口令使用 `=` 前缀，避免与 slash command 和 mention 语法冲突。

### `=sa`

根据中文源同步所有英文 Agent 文件。

- 不修改中文源。
- 同步根 `AGENTS.md`、`docs/agents/*.md`、`docs/tasks/*.md` 和项目 skill。
- 英文保持简洁、直接，并更新对应 SHA256 marker。
- 完成后运行 `python3 ./tools/sync_agents.py --check`。

### `=ca`

只运行 `python3 ./tools/sync_agents.py --check` 检查中英文同步，不修改文件。若失败，报告缺失目标、过期 marker、孤立英文文件或残留中文正文。

### `=ai`

把近期对话中稳定、可复用的 Eyu 上下文沉淀到项目 AI 资料。

- 先检查工作区，搜索已有所有者和旧结论。
- 只保存能减少未来误判、固定验证入口或明确已决定设计的内容。
- 根规则写入 `AGENTS.zh-CN.md`；专项长期知识写入 `docs/agents/zh-CN/*.md`；主题状态和证据写入 `docs/tasks/zh-CN/*.md`；共享工作流和口令写入 `SKILL.zh-CN.md`。
- 可从代码或配置实时发现的动态事实以实时文件为准，不复制第二份完整清单。
- 未决定的语法方案、临时猜测、一次性日志、聊天流水和秘密信息不得升级为长期规则。
- 修改中文源后同步英文文件，并运行同步检查。

### `=br <用途>`

创建并切换到 `<type>/<english-kebab-description>` 形式的本地分支。先检查当前分支、工作区和已有引用；默认从当前 `HEAD` 创建并保留未提交改动。同名引用已存在时停止询问，不自动追加编号。只创建分支，不提交或推送。

### `=gc`

只检查当前改动是否适合发布：检查状态、diff、未跟踪文件和相关验证，不暂存、提交、推送或创建 PR。

### `=cm`

只提交当前意图明确的文件到本地分支。不要默认 `git add .`；提交包含简洁标题和中文正文，说明改了什么、为什么以及验证了什么。不要推送或创建 PR。

### `=gh`

检查并提交当前意图明确的文件，推送当前分支，并创建 draft PR。验证失败时默认停止，除非用户明确要求继续。

## 6. 同步规则

中文文件是人类维护源，英文文件是 AI 默认读取入口：

- `AGENTS.zh-CN.md` -> `AGENTS.md`
- `docs/agents/zh-CN/*.md` -> `docs/agents/*.md`
- `docs/tasks/zh-CN/*.md` -> `docs/tasks/*.md`
- `.agents/skills/*/SKILL.zh-CN.md` -> `.agents/skills/*/SKILL.md`

英文文件顶部必须包含匹配中文源规范化 UTF-8/LF 内容的 SHA256 marker。中文和英文冲突时以中文为准。不要创建 `.agents/skills/*/zh-CN/SKILL.md`，避免被发现为重复 skill。
