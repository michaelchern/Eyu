# Eyu Build Context

只在 CMake、编译器、构建、测试或构建错误任务中加载本文件。

## 当前状态

- Eyu 要求 CMake 3.28+ 和 C++20，默认使用 Ninja。
- 根构建当前只生成 `eyu` executable，并提供 `Eyu::eyu` 别名。
- `EYU_BUILD_TESTS` 默认开启；`BUILD_TESTING` 开启时进入 `tests/`。
- 当前测试只验证 `eyu --help` 和 `eyu --version`。
- Debug 和 Release 使用独立的单配置构建目录 `out/build/<preset>`。
- `src/` 下的规划模块尚未接入根构建；新增模块必须显式添加目标、依赖和测试。

## 权威与边界

- 实际目标、源文件、选项和版本以实时 `CMakeLists.txt`、`CMakePresets.json` 和子目录 CMake 文件为准。
- README 中的扫描器、解析器、字节码、VM 和 GC 是路线图，不是当前构建事实。
- 成功编译只能证明编译和链接；语言语义必须通过单元测试、集成测试或 `.eyu` 行为用例验证。
- 不把个人编译器绝对路径写入共享 preset；本机覆盖使用被忽略的 `CMakeUserPresets.json`。

## 默认命令

```bash
cmake --list-presets
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

Release 验证将 `debug` 替换为 `release`。构建后可直接检查 CLI：

```bash
./out/build/debug/bin/eyu --help
./out/build/debug/bin/eyu --version
```

Windows 上可执行文件名为 `eyu.exe`。

## 修改与验证

- 修改前查看工作区，不覆盖用户已有改动。
- CMake 或 preset 改动后至少运行 `cmake --list-presets`、目标配置、构建和测试。
- 新增模块时优先建立目标级 include、compile feature 和依赖范围，不使用全局 include 或编译选项代替。
- 新增语言功能时，先运行最小目标测试，再按风险运行完整 `ctest`。
- 构建失败时先找第一条 `CMake Error`、`FAILED:`、`fatal error` 或编译器 error，不从最后的退出码反推根因。
- 纯 Agent 文档改动只需同步检查和 `git diff --check`；首次记录或改变构建入口时应实测命令。
