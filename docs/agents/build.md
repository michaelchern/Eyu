# Eyu Build Context
<!-- AGENT_DOCS_BUILD_ZH_CN_SHA256: 770d175c9825d97e7aca4f4c8b0150b6883030f253f071b32701536b0ed587fc -->

Load only for CMake, compiler, build, test, or build-error tasks.

## Current State

- Eyu requires CMake 3.28+ and C++20.
- The root build creates only the `eyu` executable and `Eyu::eyu` alias.
- `EYU_BUILD_TESTS` defaults on; tests currently cover only `--help` and `--version`.
- `debug` and `release` provide portable single-config Ninja entries. Windows has MSVC and Clang multi-config presets; macOS has a Ninja Multi-Config preset.
- Build trees live under `out/build/<preset>`. Put machine-specific overrides in ignored `CMakeUserPresets.json`.

Live CMake files are authoritative. Planned modules under `src/` are not connected until targets, dependencies, and tests are added explicitly. Compilation and linking do not prove language semantics.

```bash
cmake --list-presets=all
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

macOS multi-config example:

```bash
cmake --preset ninja-macos
cmake --build --preset macos-debug
ctest --preset macos-debug
```

Diagnose the first CMake, Ninja, or compiler error. Do not delete build trees or caches by default.
