# Eyu Formatting Context

只在 clang-format、注释、编码、换行或 format-only 任务中加载本文件。

- `.clang-format` 是 C++ 格式权威；只格式化本次任务触及的源码。
- format-only 任务不得重命名、重构、调整 include、改注释或顺手修逻辑。
- 添加公共注释前检查声明、实现和调用位置；解释职责、所有权、前置条件和“为什么”，不复述代码。
- 不用 BOM、删除中文或放宽规则掩盖编码问题。
- `git diff --check` 不覆盖未跟踪文件，发布前必须显式检查。

若本机有 clang-format，运行：

```bash
clang-format --dry-run --Werror --style=file <changed-cpp-files>
```
