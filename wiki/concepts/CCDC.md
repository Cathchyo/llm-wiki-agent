---
title: "CCDC"
type: concept
tags: [remote-sensing, landsat, change-detection, harmonic-model]
sources: [1-s2-0-s003442572030540x-main]
last_updated: 2026-09-21
---

# CCDC

CCDC（Continuous Change Detection and Classification）使用全部可用的 Landsat 观测进行变化检测和地表覆盖分类。它先去除云、云影和雪，再为每个光谱波段建立谐波模型；当监测窗口内实际反射率与预测值的偏差超过阈值时，识别变化断点。（原文第 93–102 行）

本文指出，CCDC 的谐波模型在一个模型内使用固定的截距、斜率和傅里叶系数；更新频率是按时间段，而不是像 [[COLD]] 那样按每个观测更新。渐进变化也可能被表示为趋势斜率，而不是某个具体日期的变化。（第 66–73、108–110、281–283 行）

[[COLD]] 提高了更新频率并增加时间调整 RMSE、变化角度等步骤；[[SCCD]] 则进一步用状态空间模型和 [[KalmanFilter]] 让状态随时间递推变化。（第 103–110、237–266 行）

## 来源

- [[1-s2-0-s003442572030540x-main]]

