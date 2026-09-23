# SCCD 入库方案（待审核）

## 内容依据

- 审核通过的摘要：`review/sccd-understanding-draft.md`
- 来源文档：`raw/1-s2.0-S003442572030540X-main.md`

## 拟执行变更

1. 新建来源页：`wiki/sources/1-s2-0-s003442572030540x-main.md`
   - 记录论文背景、任务、核心方法、主要结果和原文行号。
   - 标签：`remote-sensing`、`forest-disturbance`、`landsat`、`change-detection`。
2. 新建概念页：`wiki/concepts/SCCD.md`
   - 重点说明 SCCD 如何递推更新、为何适合近实时监测，以及对微弱扰动的作用。
3. 新建概念页：`wiki/concepts/CCDC.md`、`wiki/concepts/COLD.md`、`wiki/concepts/KalmanFilter.md`
   - 只记录理解 SCCD 所需的定义和差异，不扩展论文未支持的内容。
4. 更新 `wiki/index.md`
   - 加入上述来源页和概念页。
5. 更新 `wiki/overview.md`
   - 增加一段 SCCD 与 CCDC、COLD 关系的简短总览。
6. 更新 `wiki/log.md`
   - 追加本次 ingest 记录。
7. 页面链接
   - 来源页链接至 `[[SCCD]]`、`[[CCDC]]`、`[[COLD]]`、`[[KalmanFilter]]`。
   - 四个概念页之间仅建立论文明确支持的关系。

## 检查结论

- 当前 Wiki 尚无已入库来源，因此没有发现内容冲突。
- 正式入库后将检查断链、索引同步和日志覆盖。

> 状态：等待入库方案审核；尚未修改 `wiki/`。
