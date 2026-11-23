# S-CCD 论文引言中文翻译

- **论文原题**：A near-real-time approach for monitoring forest disturbance using Landsat time series: stochastic continuous change detection
- **中文题名**：利用 Landsat 时间序列近实时监测森林扰动的方法：随机连续变化检测
- **作者**：Su Ye、John Rogan、Zhe Zhu、J. Ronald Eastman
- **期刊**：Remote Sensing of Environment，252（2021），112167；在线发表于 2020 年 11 月 5 日。
- **DOI**：[10.1016/j.rse.2020.112167](https://doi.org/10.1016/j.rse.2020.112167)
- **翻译范围**：原 PDF 第 1—2 页，第 1 节 Introduction 全文；结合所提供的两张截图核对段落顺序及跨页、跨栏衔接，不含摘要和第 2 节正文。
- **原始文件**：[论文 PDF](<../raw/ccdc_deep_learning/SCCD/A near-real-time approach for monitoring forest disturbance using Landsat time series- Stochastic continuous change detection.pdf>)

## 1. 引言

过去二十年来，随着近年来气温升高和长期干旱，全球许多地区均有记录表明，森林扰动的发生频率和严重程度有所增加（Dale et al., 2001; Seidl et al., 2017; Turner et al., 1998），例如虫害暴发（Kautz et al., 2017; Paritsis and Veblen, 2011）、野火（Pechony and Shindell, 2010; Westerling, 2016）和干旱（Allen et al., 2015）。森林扰动事件通过木材的氧化和分解直接向大气排放碳（Masek et al., 2008），并对国家森林所提供的气候调节、生物多样性保护等生态系统服务产生显著影响（Curran and Trigg, 2006）。因此，准确、及时且系统地收集森林扰动的范围、发生时间和幅度等信息十分重要，这有助于开展早期预警和有效管理，防止森林面积进一步损失（Rogan and Mietkiewicz, 2015）。

几十年来，卫星遥感一直被视为业务化森林监测的重要数据来源（Pasquarella et al., 2017）。尤其是 Landsat 历史档案的开放（Woodcock et al., 2008），为利用长期、一致的 Landsat 时间序列刻画森林扰动提供了更多机会（Zhu, 2017）。与中分辨率成像光谱仪（MODIS，分辨率为 250—1000 米）等较粗分辨率的数据集相比，Landsat 时间序列提供了长达 40 年的全球观测记录，时间跨度充足，空间分辨率也更精细（30 米）（Masek et al., 2013）。因此，Landsat 数据通常被认为是全面识别各类扰动事件的最佳免费遥感数据源（Cohen et al., 2017; Cohen et al., 2016; Kennedy et al., 2014; Ye et al., 2018）。近年来，Landsat 分析就绪数据（Analysis Ready Data，ARD）的发布，降低了大范围森林扰动自动化监测的难度（Dwyer et al., 2018）。Landsat ARD 将所有可用的 Landsat-4 和 Landsat-5 TM、Landsat-7 ETM+ 以及 Landsat-8 OLI/TIRS 数据统一到阿尔伯斯等积圆锥投影（Albers Equal Area，AEA）的网格中，并进行一致的几何配准和大气校正，因而达到了可直接使用所要求的最高科学标准和处理水平（Zhu, 2019）。Landsat ARD 将用户在数据预处理方面的工作量降至最低，极大地便利了大范围、长期时间序列分析（Dwyer et al., 2018）。

针对土地覆盖变化的检测与刻画，研究者已开发出大量基于卫星时间序列分析的方法（Kennedy et al., 2010; Verbesselt et al., 2010a; Zhu and Woodcock, 2014b; Zhu et al., 2012）。这些方法通常按照监测策略分为离线监测和在线监测两类（Bullock et al., 2019; Zhu, 2017）。离线监测侧重于在时间序列数据收集完成后开展回溯分析，以重建森林扰动历史。其代表性方法包括 LandTrendr（Kennedy et al., 2010）、DBEST（Jamali et al., 2015）以及集成方法（Bullock et al., 2019）。在线监测则适用于新观测数据不断获取并得到及时处理的实际场景，因此可用于近实时监测。代表性在线监测方法包括加性季节与趋势断点监测算法（Breaks for Additive Season and Trend Monitor，BFAST Monitor）（Verbesselt et al., 2012），以及连续变化检测与分类算法（Continuous Change Detection and Classification，CCDC）（Zhu and Woodcock, 2014b; Zhu et al., 2020）；不过，这些方法也适用于离线监测。BFAST 最初用于对 MODIS 时间序列进行时间分段（Verbesselt et al., 2010a），后来被改进为 BFAST Monitor，以实现对干旱相关植被扰动的近实时检测（Verbesselt et al., 2012）。BFAST Monitor 是一种使用单个光谱波段或指数的单变量方法。然而，已有研究指出，使用多个波段或指数更为合适，因为森林扰动具有多光谱表现，需要多波段输入（Cohen et al., 2017; Zhu et al., 2020）。

CCDC 是一种多变量时间序列模型，利用所有可用的 Landsat 4—8 数据进行变化刻画和土地覆盖分类（Zhu and Woodcock, 2014b）。CCDC 首先使用 Fmask（Zhu and Woodcock, 2012）和 Tmask 算法（Zhu and Woodcock, 2014a）筛除云、云影和积雪，再利用剩余的晴空观测，为各个光谱波段分别建立谐波模型。当一个监测窗口内各光谱波段实际反射率与预测反射率之间的最小差异大于预先设定的变化阈值时，就识别出一个指示扰动发生时间的断点（Zhu and Woodcock, 2014b）。最近，研究者在 CCDC 的基础上开发了一种改进算法，称为土地扰动连续监测（COntinuous Monitoring of Land Disturbance，COLD）（Zhu et al., 2020）。COLD 引入了多项改进，包括扰动提取、经时间调整的均方根误差（Root Mean Square Error，RMSE），以及用于扰动确认的变化角度（Zhu et al., 2020）。关于 COLD 的一项重要发现是，以最高频率更新谐波模型，即每获得一次观测就更新模型，而不像 CCDC 那样每隔一段时间才更新，可以减少约 20% 的误报错误（Zhu et al., 2020）。Zhu et al.（2020）利用在美国本土连续地区随机选取的 7200 个 Landsat 时间序列样地测试了 COLD 的性能，并报告称，COLD 在多种土地扰动类型上的漏报率为 27%、误报率为 28%，其精度高于 CCDC（后者的误报率约为 20%、漏报率约为 82%，见 Cohen et al., 2017）。

然而，尽管 COLD 算法提高了变化检测精度，仍存在若干限制其业务化监测应用的问题。首先，COLD 的计算开销很大：根据我们的测试，使用最初的 MATLAB 软件处理一个 Landsat ARD 瓦片的数据（1000—3000 景影像），需要约 5000 个计算小时。较高的计算需求限制了 COLD 在广泛科学研究中的应用，尤其是在州级或大陆尺度等大范围制图中的应用。其运行速度慢的原因在于逐观测更新的方法（Zhu et al., 2020）。例如，如果单个像元的时间序列包含 500 次晴空观测，COLD 就需要使用最小绝对收缩与选择算子（Least Absolute Shrinkage and Selection Operator，LASSO）算法重新训练模型约 500 次，才能完成该像元的检测。每向时间序列加入一次新观测，都从头重建模型，由此产生了重复计算。其次，COLD 的前身 CCDC 是为检测突发性土地覆盖变化而设计的，对于光谱变化幅度较小至中等的扰动，检测效果较差（Brown et al., 2019; Cohen et al., 2017; Zhu et al., 2020）。已有研究提出，一个可能的原因是，CCDC 将渐变识别为谐波回归模型中的斜率，而没有将其归因于某一具体日期发生的变化（Bullock et al., 2019）。虽然 COLD 缓解了这一问题，但仍未将其完全解决；其对“胁迫”（stress）类扰动的生产者精度仅为 60%，便说明了这一点（Zhu et al., 2020）。第三，在当前 COLD 工作流程中，近实时监测尚未完全实现业务化，原因有二：其一，COLD 对内存的需求较高，每获得一次新观测，都需要加载所有影像，以更新模型系数并计算经时间调整的 RMSE；其二，COLD 的某些步骤，例如最小 RMSE 的计算，需要使用当前监测日期之后采集的数据，无法满足近实时监测的需求。将这些步骤改写为递归形式，可以使系统不必在每次获取新观测时都加载全部历史影像，从而大幅提高近实时场景下的计算效率。

目前，大多数业务化近实时产品都基于 MODIS 系统，例如 Terra-i（Reymondin et al., 2012）和 FORMA 预警系统（Hammer et al., 2014）。据我们所知，全球土地分析与发现系统（Global Land Analysis and Discovery，GLAD）是唯一在 Landsat 像元尺度上对林地提供近实时监测的业务化系统（Hansen et al., 2016）。GLAD 使用预先训练的决策树模型对晴空观测进行分类；如果连续四次观测中至少有两次被归为扰动类别，就发出预警。由于该产品仅针对热带常绿林设计和实施，而且系统没有考虑物候变化（Hansen et al., 2016），因此，它在中高纬度地区的表现尚不清楚；这些地区的扰动信号在光谱上常常与季节性落叶相似。

本研究介绍一种名为“随机连续变化检测”（Stochastic Continuous Change Detection，S-CCD）的新算法，旨在以递归方式从 Landsat 时间序列中普遍检测森林扰动。S-CCD 将状态空间理论引入现有的 COLD 框架，力求实现三个目标：（1）在保持较低误报率的同时提高检测精度，尤其是提高对光谱变化幅度较小的森林变化的检测精度；（2）提供一个可用于业务化近实时监测的框架；（3）提高计算效率，使利用长期时间序列刻画大范围森林扰动成为可能。

下文首先对状态空间模型和卡尔曼滤波作直观说明，介绍 S-CCD 的数学基础（第 2 节）；随后描述 S-CCD 算法，重点介绍其与 COLD 不同的步骤（第 3 节）；接着介绍参考数据集与验证指标（第 4 节），展示定量和定性评价结果（第 5 节）；最后讨论 S-CCD 的优势及未来工作（第 6 节）。特别需要指出的是，第 5.3 节介绍了一个使用 C 语言实现、同时支持 S-CCD 和 COLD 的高性能软件包。

---

**译注（非原文）**：本文统一将 commission error 译为“误报率／误报错误”，将 omission error 译为“漏报率”，将 operational 译为“业务化”。引言中的历史表述和数值均按原文保留，包括 CCDC 约 20% 的误报率、约 82% 的漏报率，以及 COLD 的 27% 漏报率和 28% 误报率；未另行核查其所引文献。“减少约 20% 的误报错误”沿用原文说法，不擅自解释为降低 20 个百分点。