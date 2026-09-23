# 《Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset》入库方案（待逐项批准）

## 方案状态

- 依据：`review/liao-forest-disturbance-agent-understanding-draft.md`（用户已确认摘要）
- 原始资料：`raw/Liaopdf.md`
- 本方案只描述拟议变更，当前尚未修改 `wiki/`。

## 1. 拟新增来源页

### `wiki/sources/liaopdf.md`

- **标题**：Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset
- **类型**：`source`
- **日期**：`2026-05-06`（论文在线发表日期）
- **标签**：`remote-sensing`、`forest-disturbance`、`disturbance-agent`、`near-real-time`、`HLS`、`machine-learning`
- **内容范围**：
  - 背景：多数近实时系统只报告森林“发生了扰动”，不能及时说明野火、砍伐还是胁迫；
  - 方法：S-CCD 异常检测、美国历史样本迁移、目标区域初步分类、专家核验、本地分阶段随机森林和每周更新；
  - 分类对象：野火、砍伐、胁迫，以及非扰动异常/无异常森林；
  - 结果：整体首次正确报警延迟约 11.6 天、稳定阶段约 15.5 天；总体准确率约 77.5% 和 84.0%；相比 DIST-ALERT 准确率更高、误报更少，但首次报警平均慢约 3.7 天；
  - 限制：跨地区样本迁移仍需专家核验，胁迫最难识别，光学观测受云层影响；
  - 明确说明：美国样本是参考和样本启动器，最终分类依赖中国本地核验样本训练的模型。
- **拟建立的知识链接**：
  - `[[ForestDisturbanceAgentAttribution]]`：森林扰动原因归因的概念与流程；
  - `[[SupervisedLandDisturbanceMonitoring]]`：从“是否发生扰动”扩展到“属于哪类扰动”；
  - `[[SCCD]]`：负责生成和更新光谱异常；
  - `[[CCDC]]`：S-CCD/SCCD 所属的连续变化检测谱系。
- **不创建**：不为作者、DIST-ALERT、HLS 或随机森林单独创建实体/概念页；这些内容在来源页和概念页中作为背景说明。

## 2. 拟新增概念页

### `wiki/concepts/ForestDisturbanceAgentAttribution.md`

- **标题**：森林扰动原因归因
- **类型**：`concept`
- **标签**：`remote-sensing`、`forest-disturbance`、`disturbance-agent`、`near-real-time`
- **拟写内容**：
  1. 定义：在发现森林异常后，进一步判断其主要原因，而不是只输出“是否发生扰动”；
  2. 目标类别：野火、砍伐、胁迫和非扰动异常；
  3. 核心流程：S-CCD 圈出异常 → 迁移相似外部样本 → 生成中国区域初步分类图 → 专家核验 → 建立本地训练样本 → 按异常阶段分类；
  4. 关键思想：外部样本不直接替中国下结论，只用于减少从零开始标注的工作；最终模型使用经过中国本地核验的样本；
  5. 近实时输出：根据连续异常次数调用阶段模型，结合光谱变化幅度、方向、持续时间、季节和扰动前状态，每周更新原因地图；
  6. 边界：样本迁移受地区差异影响，胁迫类信号较弱，原因分类不等于损失评估或责任认定。
- **拟链接**：
  - `[[liaopdf]]`；
  - `[[SCCD]]`；
  - `[[SupervisedLandDisturbanceMonitoring]]`；
  - `[[CCDC]]`。

## 3. 拟修改现有概念页

### `wiki/concepts/SCCD.md`

拟作最小增量修改：

- 在 `sources` 中增加 `liaopdf`；
- 增加“在森林扰动原因归因中的角色”小节：说明本文使用 S-CCD 负责发现异常，后续随机森林负责区分野火、砍伐、胁迫和非扰动；
- 链接 `[[ForestDisturbanceAgentAttribution]]` 和 `[[liaopdf]]`；
- 保留 SCCD 原有的递推状态更新和森林扰动检测内容，不把本文的原因分类准确率写成 SCCD 单独的结果。

### `wiki/concepts/SupervisedLandDisturbanceMonitoring.md`

拟作增补修改：

- 在 `sources` 中增加 `liaopdf`；
- 增加一节说明该方法从 2024 年论文中的“扰动/非扰动二分类”扩展到本文的“野火/砍伐/胁迫/非扰动多类别归因”；
- 说明两篇文章都使用分阶段模型和历史样本思路，但评价目标不同，不能直接混用 F1、延迟等数字；
- 增加指向 `[[ForestDisturbanceAgentAttribution]]` 和 `[[liaopdf]]` 的链接。

## 4. 拟修改索引、概览和日志

### `wiki/index.md`

- 在 Sources 下增加 `liaopdf` 来源页及一句话摘要；
- 在 Concepts 下增加 `ForestDisturbanceAgentAttribution`；
- 不新增实体条目。

### `wiki/overview.md`

- 在 `sources` 中增加 `liaopdf`；
- 增加一段知识演进总结：现有 Wiki 已覆盖从“发现森林是否发生扰动”到“进一步判断扰动原因”的两层任务；
- 明确 `[[SCCD]]` 是异常生成基础，`[[SupervisedLandDisturbanceMonitoring]]` 和 `[[ForestDisturbanceAgentAttribution]]` 分别对应扰动检测判别与原因归因；
- 记录本文的整体延迟和准确率，但不与前一篇论文的指标直接排名。

### `wiki/log.md`

正式入库时追加：

`## [2026-09-21] ingest | Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset`

## 5. 链接与一致性检查方案

正式写入后将检查：

- 新来源页和新概念页是否都出现在 `wiki/index.md`；
- 所有 `[[...]]` 是否指向实际存在的文件名 stem；
- `S-CCD`、`SCCD`、监督式扰动检测和原因归因之间的角色是否清楚；
- 不把“外部样本迁移”表述成“直接把美国模型套到中国”；
- 不把原因分类结果误写成灾害损失评估或具体责任认定；
- 不把本文与前一篇论文的延迟、F1 直接做不具可比性的排名。

## 6. 可能的内容冲突与处理建议

1. **任务层级不同**：已有 `SupervisedLandDisturbanceMonitoring` 主要描述“是否发生扰动”，本文描述“扰动属于哪一类原因”。建议写成递进关系，不判定为矛盾。
2. **S-CCD/SCCD 名称**：本文使用 S-CCD 拼写，已有概念页使用 SCCD；统一链接到 `[[SCCD]]`，在来源页和概念页说明连字符差异。
3. **指标不可直接横比**：本文的 11.6/15.5 天和 77.5%/84.0% 是多类别原因归因任务的整体结果；与前一篇二分类扰动检测论文的指标仅作背景关联，不作直接排名。

## 待逐项批准

请确认以下项目：

- [ ] 批准新增 `wiki/sources/liaopdf.md` 及其标题、日期、标签；
- [ ] 批准新增 `wiki/concepts/ForestDisturbanceAgentAttribution.md`；
- [ ] 批准按上述范围增补 `SCCD.md`；
- [ ] 批准按上述范围增补 `SupervisedLandDisturbanceMonitoring.md`；
- [ ] 批准更新 `wiki/index.md`、`wiki/overview.md`、`wiki/log.md`；
- [ ] 接受 S-CCD/SCCD、样本迁移和指标可比性的限定表述；
- [ ] 若有删改，请指出具体页面或条目。

只有在上述方案获得明确的“批准进入 Wiki”或同等明确授权后，才执行正式写入。

