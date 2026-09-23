---
title: "Overview"
type: synthesis
tags: []
sources: [1-s2-0-s003442572030540x-main, 1-s2-0-s0034425724000828-main, liaopdf]
last_updated: 2026-09-21
---

# Overview

*This page is maintained by the LLM. It is updated on every ingest to reflect the current synthesis across all sources.*

当前 Wiki 收录了一项基于 Landsat 时间序列的森林扰动监测研究。[[CCDC]] 用谐波模型描述像元的长期趋势和季节周期；[[COLD]] 将模型提高到逐观测更新，但需要反复读取历史数据并重建模型。[[SCCD]] 在 COLD 框架中引入状态空间模型和 [[KalmanFilter]]，把历史信息保存在状态与协方差中，从而递推处理新观测。

SCCD 的主要价值是提高近实时计算效率，并减少部分低幅度森林扰动的漏检；其总体最佳 F1 仅略高于 COLD，且在综合地类测试中略低，因此目前不能概括为所有场景下都更准确。详见 [[1-s2-0-s003442572030540x-main]]。

另一项研究将 [[SCCD]]/S-CCD 作为异常生成基础，在其后增加 [[SupervisedLandDisturbanceMonitoring]] 的历史监督判别层。该层利用变化方向、季节、扰动前状态和历史案例判断早期异常，主要改善检测级的及时性与误报控制：达到稳定效果的时间从 22 天提前到 15 天，F1 从 0.546 提升到 0.733；但连续 6 次异常的最终确认仍约需 35 天。详见 [[1-s2-0-s0034425724000828-main]]。

进一步的研究把任务从“是否发生森林扰动”扩展到“扰动是什么原因”。[[ForestDisturbanceAgentAttribution]] 使用 [[SCCD]]/S-CCD 产生异常，再通过跨地区样本筛选、中国专家核验和分阶段模型，将异常归因为野火、砍伐、胁迫或非扰动。该框架在五个中国代表性区域实现每周近实时更新，整体首次正确报警约 11.6 天、稳定阶段约 15.5 天；这些指标对应的是原因归因任务，不与前一研究的二分类指标直接排名。详见 [[liaopdf]]。
