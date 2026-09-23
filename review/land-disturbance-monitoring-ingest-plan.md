# 《Leveraging past information and machine learning to accelerate land disturbance monitoring》入库方案（待逐项批准）

## 方案状态

- 依据：`review/land-disturbance-monitoring-understanding-draft.md`（已获摘要审核通过）
- 原始资料：`raw/1-s2.0-S0034425724000828-main.md`
- 本方案只描述拟议变更，当前尚未修改 `wiki/`。

## 1. 拟新增来源页

### `wiki/sources/1-s2-0-s0034425724000828-main.md`

- **标题**：Leveraging past information and machine learning to accelerate land disturbance monitoring
- **类型**：`source`
- **日期**：`2024-02-26`（论文在线发表日期）
- **标签**：`remote-sensing`、`land-disturbance`、`near-real-time`、`machine-learning`、`change-detection`
- **内容范围**：
  - 背景：近实时土地扰动监测的救灾和生态管理需求；
  - 问题：固定阈值和连续异常确认造成早期误报与确认延迟；
  - 方法：历史回溯标注、按连续异常次数分阶段的随机森林、S-CCD 异常生成、像元概率到扰动斑块的输出；
  - 结果：检测级 Level Off Point 从 22 天降到 15 天，F1 从 0.546 升到 0.733，误报率从 44.4% 降到 17.7%；确认级仍约需 35 天；
  - 限制：美国历史样本的迁移性、短暂扰动确认困难、云和有效观测不足造成的等待；
  - 明确说明：论文判断的是“是否发生土地扰动”，不是灾种分类。
- **拟建立的知识链接**：
  - `[[SupervisedLandDisturbanceMonitoring]]`：本文提出的监督式分阶段判别框架；
  - `[[SCCD]]`：作为光谱异常生成和时间序列处理基础；
  - `[[CCDC]]`：S-CCD/SCCD 的方法谱系与传统连续变化检测背景。
- **不创建**：不为作者、HLS 或随机森林单独创建实体/概念页，避免把通用背景拆成过多页面。

## 2. 拟新增概念页

### `wiki/concepts/SupervisedLandDisturbanceMonitoring.md`

- **标题**：监督式土地扰动监测
- **类型**：`concept`
- **标签**：`remote-sensing`、`land-disturbance`、`near-real-time`、`supervised-learning`
- **拟写内容**：
  1. 定义：用历史已确认扰动训练模型，判断早期光谱异常是否是真实扰动；
  2. 核心流程：异常生成 → 历史标注 → 1–8 次异常对应的阶段模型 → 概率输出 → 空间斑块 → 检测级/确认级；
  3. 特征类别：变化幅度和方向、异常一致性与跨度、发生季节、扰动前地表状态；
  4. 与传统固定阈值法的区别：从“数异常次数”转为“结合历史经验判断异常可信度”；
  5. 与 `[[SCCD]]` 的关系：SCCD 是前端异常生成器，监督式模型是其后的判别层，二者不是同一个方法；
  6. 边界：早期预警加快，但最终确认仍依赖连续观测，不能消除卫星重访、云层和数据发布延迟。
- **拟链接**：
  - `[[1-s2-0-s0034425724000828-main]]`；
  - `[[SCCD]]`；
  - `[[CCDC]]`。

## 3. 拟修改现有概念页

### `wiki/concepts/SCCD.md`

拟作**最小增量修改**：

- 在 `sources` 中增加 `1-s2-0-s0034425724000828-main`；
- 增加“在监督式土地扰动监测中的角色”小节：说明当前论文使用 S-CCD（论文中的连字符写法）产生异常记录，监督随机森林负责判断异常是否像真实扰动；
- 增加指向 `[[SupervisedLandDisturbanceMonitoring]]` 和新来源页的链接；
- 保留现有关于 SCCD 递推更新、计算效率和森林扰动表现的内容，不把本论文的 F1 结果误写成 SCCD 本身的改进结果。

不新增 `S-CCD.md`，以免与已有 `SCCD.md` 形成重复页面；在来源页中保留论文原有的 `S-CCD` 拼写并说明名称关系。

## 4. 拟修改索引、概览和日志

### `wiki/index.md`

- 在 Sources 下增加新来源页及一句话摘要；
- 在 Concepts 下增加 `SupervisedLandDisturbanceMonitoring`；
- 不新增实体条目。

### `wiki/overview.md`

在现有 SCCD/CCDC/COLD 总结后增加一段，明确区分两层能力：

- SCCD/S-CCD 负责高效地产生和更新光谱异常；
- 本文的监督式分阶段模型利用历史扰动经验，主要改善早期异常的真假判断；
- 因而它把检测级稳定效果从 22 天提前到 15 天，但最终确认仍约需 35 天。

### `wiki/log.md`

正式入库时追加：

`## [2026-09-21] ingest | Leveraging past information and machine learning to accelerate land disturbance monitoring`

## 5. 链接与一致性检查方案

正式写入后将检查：

- 新来源页、新概念页是否都出现在 `wiki/index.md`；
- 所有 `[[...]]` 是否指向实际存在的文件名 stem；
- 新来源页与概念页是否形成双向可追溯链接；
- `S-CCD` 与已有 `SCCD` 的命名说明是否避免重复建页；
- 不把“早期检测加速”误写成“最终确认时间同样缩短”。

## 6. 可能的内容冲突与处理建议

1. **S-CCD / SCCD 的名称与方法谱系**：当前论文称 S-CCD 为 CCDC 的近实时改造；已有来源页侧重其与 COLD 的关系。暂定在 SCCD 概念页并列说明“方法谱系”和“本文使用角色”，不判定为实质矛盾。
2. **“更快”含义**：当前论文的主要提升是检测级早期识别和误报控制，不是观测获取或最终确认规则本身变快。概览和来源页将保留这一限定。
3. **跨研究指标**：本文与其他研究的数据、事件和确认规则不同，入库时只记录论文内部对比，不把不同研究的 MTL/F1 直接排名。

## 待逐项批准

请确认以下项目：

- [ ] 批准新增来源页及其标题、日期、标签；
- [ ] 批准新增 `SupervisedLandDisturbanceMonitoring` 概念页；
- [ ] 批准按上述范围增补 `SCCD.md`；
- [ ] 批准更新 `wiki/index.md`、`wiki/overview.md`、`wiki/log.md`；
- [ ] 接受上述 S-CCD/SCCD 命名说明及两项限制性表述；
- [ ] 若有删改，请指出具体页面或条目。

只有在上述方案获得明确的“批准进入 Wiki”或同等明确授权后，才执行正式写入。

