---
title: "COLD"
type: concept
tags: [remote-sensing, landsat, forest-disturbance, change-detection]
sources: [1-s2-0-s003442572030540x-main]
last_updated: 2026-09-21
---

# COLD

COLD（COntinuous monitoring of Land Disturbance）是在 [[CCDC]] 基础上改进的 Landsat 扰动监测算法。它把谐波模型提高到逐观测更新，并加入扰动提取、时间调整 RMSE 和变化角度确认等步骤。（原文第 103–115 行）

## 如何判断异常

COLD 根据与当前监测时段最接近的 24 个历史观测计算时间调整 RMSE，再用 RMSE 标准化各波段的预测偏差，并结合连续异常观测及变化方向确认断点。（第 371–391、524–541 行）

## 主要限制

每增加一个新观测，COLD 都要重新读取历史影像并用 LASSO 重建谐波模型；一个像元若有 500 个清晰观测，论文举例称大约需要重新训练 500 次。它还包含依赖当前监测日期之后数据的静态最小 RMSE 步骤，因此难以直接作为完整的近实时流程运行。（第 59–65、75–83、117–121 行）

[[SCCD]] 保留了 COLD 的总体检测框架，但用 [[KalmanFilter]] 更新状态和协方差，并将时间调整 RMSE等步骤递推化。（第 497–514、742–754 行）

## 来源

- [[1-s2-0-s003442572030540x-main]]

