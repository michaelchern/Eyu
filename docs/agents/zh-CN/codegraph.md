# Eyu Codegraph Context

只在符号查找、调用链、架构理解或重构影响面任务中加载本文件。

1. 用 `rg --files` 确认真实目录与文件。
2. 用 `rg` 查声明、定义、调用、测试和 CMake 接入点。
3. 沿 include、namespace、目标依赖和 CLI 入口追踪数据流。
4. 检查目标文件现有 diff，避免把用户未提交改动当成基线。

README 中的 scanner/parser/VM 架构是规划，不证明符号已经存在。重构前列出所有调用者、测试与构建消费者；找不到实现时明确区分规划接口和实时接口。
