# Eyu Build Context
<!-- AGENT_DOCS_BUILD_ZH_CN_SHA256: b4d9aee4b88a0853f51d5e0ee7d1768f5d929fd4c1997d21b9bf5e923a54290f -->

Load this file only for CMake, compiler, build, test, or build-failure tasks.

## Current State

- Eyu requires CMake 3.28+ and C++20 and uses Ninja by default.
- The root build currently creates only the `eyu` executable and the `Eyu::eyu` alias.
- `EYU_BUILD_TESTS` defaults to on; the root enters `tests/` when `BUILD_TESTING` is enabled.
- Current tests cover only `eyu --help` and `eyu --version`.
- Debug and Release use separate single-config build trees under `out/build/<preset>`.
- Planned modules under `src/` are not connected to the root build. Add targets, dependencies, and tests explicitly when implementing them.

## Authority and Boundaries

- Treat live `CMakeLists.txt`, `CMakePresets.json`, and subdirectory CMake files as authoritative for targets, sources, options, and versions.
- Scanner, parser, bytecode, VM, and GC descriptions in the README are roadmap goals, not build facts.
- Successful compilation proves compilation and linking only. Verify language semantics with unit, integration, or `.eyu` behavior tests.
- Do not commit personal compiler paths to shared presets. Put local overrides in ignored `CMakeUserPresets.json`.

## Default Commands

```bash
cmake --list-presets
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

Replace `debug` with `release` for Release validation. After building, the CLI can be checked directly:

```bash
./out/build/debug/bin/eyu --help
./out/build/debug/bin/eyu --version
```

The executable is named `eyu.exe` on Windows.

## Change and Validation Rules

- Inspect the worktree before editing and preserve user changes.
- After CMake or preset changes, run at least `cmake --list-presets`, configure, build, and tests for the affected preset.
- Add new modules with target-scoped includes, compile features, and dependency visibility instead of global settings.
- For language features, run the smallest focused tests first, then full `ctest` in proportion to risk.
- Diagnose the first `CMake Error`, `FAILED:`, `fatal error`, or compiler error instead of reasoning backward from the final exit code.
- Agent-doc-only changes require the sync check and `git diff --check`. Verify build commands directly when first recording or changing them.
