# Eyu Build Context

只在 CMake、编译器、构建、测试或构建错误任务中加载本文件。

## 当前状态

- 要求 CMake 3.28+ 与 C++20。
- 根构建只生成 `eyu` executable 和 `Eyu::eyu` alias。
- `EYU_BUILD_TESTS` 默认开启；当前测试只覆盖 `--help` 与 `--version`。
- `debug` / `release` 提供便携 Ninja 单配置入口；Windows 提供 MSVC、Clang 多配置 preset，macOS 提供 Ninja Multi-Config preset。
- 所有构建目录位于 `out/build/<preset>`；本机覆盖写入被忽略的 `CMakeUserPresets.json`。

## 权威与边界

- 目标、源文件、选项和 preset 以实时 CMake 文件为准。
- `src/` 下规划模块尚未接入；新增模块必须显式增加目标、依赖和测试。
- 编译链接成功只证明构建完成，语言语义必须用测试或 `.eyu` 行为用例验证。

## 常用命令

```bash
cmake --list-presets=all
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

macOS 多配置示例：

```bash
cmake --preset ninja-macos
cmake --build --preset macos-debug
ctest --preset macos-debug
```

构建失败时定位第一条 `CMake Error`、`FAILED:`、`fatal error` 或编译器 error。不要默认删除构建目录或用户缓存。
