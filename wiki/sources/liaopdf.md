---
title: "Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset"
type: source
tags: [remote-sensing, forest-disturbance, disturbance-agent, near-real-time, HLS, machine-learning]
sources: []
date: 2026-05-06
source_file: raw/Liaopdf.md
last_updated: 2026-09-21
---

## Summary

本文研究如何用 Harmonized Landsat and Sentinel-2（HLS）数据，在中国近实时判断森林扰动的原因。多数近实时系统只能告诉管理者“哪里发生了森林变化”，不能及时区分野火、砍伐和虫害或干旱等胁迫；已有原因识别方法又常常需要年度数据或较长的扰动后观测。作者先用 S-CCD 发现异常，再从美国历史扰动档案中挑选与中国目标区域植被和地形相似的样本，生成初步分类结果，由中国专家核验后形成本地训练样本，最后用分阶段随机森林模型每周输出原因分类图。

## Key Claims

- 本文将近实时任务从“发现森林是否发生扰动”扩展为“判断扰动原因”，主要类别为野火、砍伐、胁迫和非扰动异常。
- 美国历史样本不是直接套用到中国的最终模型，而是用于启动样本迁移；专家核验初步分类斑块后，才形成中国本地训练样本。
- S-CCD 负责从 HLS 时间序列中产生和更新光谱异常；后续的分阶段随机森林负责根据异常阶段及光谱—时间特征进行原因分类。
- 作者为连续异常次数 1–8 个阶段分别构建模型，使模型能够处理扰动刚出现时和持续一段时间后的不同表现。
- 在中国五个代表性区域的评估中，整体首次正确报警延迟约 11.6 天，达到稳定效果约 15.5 天；总体准确率分别约为 77.5% 和 84.0%。
- 与全球 DIST-ALERT 产品的二分类比较中，本文方法误报更少、准确率更高，但首次报警平均慢约 3.7 天；它额外提供了扰动原因信息。
- 胁迫类扰动最难识别，因为信号较弱，容易与季节变化和噪声混淆；跨地区样本迁移仍不能替代本地专家核验。

## Key Quotes

> “most near-real-time (NRT) monitoring systems focus solely on detecting disturbance locations and timing of generic disturbances, lacking attribution of causal agents” — 论文摘要对现有系统局限的概括。

> “transferring-guided sampling strategy” — 作者对跨地区样本筛选并结合本地核验的样本构建策略的称呼。

## Connections

- [[ForestDisturbanceAgentAttribution]] — 本文关注的森林扰动原因归因任务与流程。
- [[SupervisedLandDisturbanceMonitoring]] — 从扰动/非扰动判断扩展到多类别原因分类的相关框架。
- [[SCCD]] — 负责生成和更新光谱异常，本文在其输出上进行原因分类。
- [[CCDC]] — S-CCD/SCCD 所属的连续变化检测方法谱系。

## Contradictions

- 与已有内容没有实质性结论冲突；本文是对“是否发生扰动”监测的任务扩展，增加了原因归因。
- 本文的 11.6/15.5 天和 77.5%/84.0% 针对多类别原因归因任务，不应与其他论文的二分类延迟和 F1 直接排名。
- “样本迁移”不能表述为把美国模型直接套到中国；最终结果依赖中国本地专家核验样本和本地模型。

