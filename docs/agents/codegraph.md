# Eyu Codegraph Context
<!-- AGENT_DOCS_CODEGRAPH_ZH_CN_SHA256: 06e2871de6a16e8a0411aec5cb0b41e9e4843e57b1dbe18a60a03ec0ba131ad0 -->

Load only for symbol lookup, call chains, architecture, or refactor impact.

1. Use `rg --files` to confirm real paths.
2. Use `rg` to find declarations, definitions, calls, tests, and CMake integration.
3. Trace data flow through includes, namespaces, target dependencies, and the CLI entrypoint.
4. Inspect existing diffs before treating a file as baseline.

README scanner/parser/VM architecture is a roadmap, not symbol evidence. List all callers, tests, and build consumers before refactoring; distinguish planned interfaces from live ones.
