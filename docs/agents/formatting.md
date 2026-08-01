# Eyu Formatting Context
<!-- AGENT_DOCS_FORMATTING_ZH_CN_SHA256: fc6cc437b50d0fe3739d9b29f83ea8e24be90236b408d5742ebbc7df7fb02630 -->

Load only for clang-format, comments, encoding, line endings, or format-only work.

- `.clang-format` is the C++ formatting authority. Format only files touched by the task.
- A format-only task must not rename, refactor, reorder includes, edit comments, or fix logic.
- Inspect declarations, implementations, and call sites before adding public comments. Explain responsibilities, ownership, preconditions, and why.
- Do not hide encoding problems with BOMs, deleted non-English text, or weakened rules.
- `git diff --check` does not inspect untracked files; review them explicitly before publication.

When clang-format is available:

```bash
clang-format --dry-run --Werror --style=file <changed-cpp-files>
```
