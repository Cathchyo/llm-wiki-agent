# 2026-09-12 森林扰动遥感监测周报（人工试写）

> **报告状态**：已完成 2026-09-12 单期快照版；周环比和状态转移待补  
> **报告周期**：截至 2026-09-12（当前数据不能单独确定本周新增窗口）  
> **系统更新时间**：2026-09-12  
> **监测范围**：大兴安岭、四川盆地、云南高原、湘中盆地、长江平原  
> **数据目录**：tmp/20260912  
> **数据文件**：slgr_confirm.shp、slgr_detected.shp、slgr_detected_rec.shp

## 1. 本周摘要

截至 2026-09-12，确认层包含 **750,627** 个要素、面积约 **821,347.49 ha**；检测层包含 **21,918** 个要素、面积约 **26,158.95 ha**；近期检测子集包含 **3,391** 个要素、面积约 **3,641.36 ha**。

近期检测子集以**采伐/人为清除**为主：3,383 个要素、约 **3,625.51 ha**；另有 8 个野火要素、约 **15.84 ha**；暂未出现胁迫要素。近期子集面积中约 **70.3%** 位于大兴安岭、约 **16.4%** 位于湘中盆地。以上是当前快照，不代表本周新增量；周环比需要上一期数据。

## 2. 总体与状态变化

### 2.1 当前快照

| 图层/暂定含义 | 要素数 | 几何面积（ha） | 备注 |
|---|---:|---:|---|
| slgr_confirm.shp：确认层 | 750,627 | 821,347.4867 | 当前导出快照 |
| slgr_detected.shp：未确认检测层 | 21,918 | 26,158.9475 | 需确认是否为未确认总集合 |
| slgr_detected_rec.shp：近期检测子集 | 3,391 | 3,641.3567 | 与检测层存在重叠 |

> **不能把三行直接相加。** 几何核对显示，近期检测子集的记录都能在未确认检测层中找到，因此近期层很可能是检测层的子集，而不是独立的第三批斑块。

### 2.2 与上一期相比

| 变化指标 | 结果 |
|---|---:|
| 新增异常要素 | 待上一期 SHP |
| 未确认 → 已确认 | 待上一期 SHP |
| 持续未确认 | 待上一期 SHP |
| 本期未再观测到 | 待上一期 SHP |

## 3. 五个区域的当前分布

以下映射依据 province 字段和系统五个研究区名称：daxing→大兴安岭、sichuan→四川盆地、yunnan→云南高原、hunan→湘中盆地、zhejiang→长江平原。正式发布前需与系统配置确认。

| 区域 | 确认层（要素/ha） | 检测层（要素/ha） | 近期子集（要素/ha） | 近期主要类型 |
|---|---:|---:|---:|---|
| 大兴安岭 | 126,028 / 166,780.62 | 3,077 / 3,285.80 | 2,373 / 2,559.77 | 采伐为主，另有 3 个野火 |
| 四川盆地 | 79,254 / 113,199.20 | 4,031 / 4,059.67 | 310 / 304.20 | 采伐 |
| 云南高原 | 152,184 / 143,801.73 | 2,731 / 3,486.51 | 27 / 15.20 | 采伐 |
| 湘中盆地 | 278,682 / 301,546.50 | 8,447 / 12,098.37 | 518 / 596.27 | 采伐为主，另有 5 个野火 |
| 长江平原 | 114,479 / 96,019.44 | 3,632 / 3,228.59 | 163 / 165.91 | 采伐 |

> 面积为几何面积（ha），按 `province` 汇总。表中仍是**要素数**，不是去重后的事件数；三个图层存在包含关系，不能跨层相加。

## 4. 三类扰动解译

| 类型 | 确认层（要素/ha） | 检测层（要素/ha） | 近期子集（要素/ha） | 初步解读 |
|---|---:|---:|---:|---|
| 采伐/人为清除（Logging） | 622,234 / 624,890.59 | 20,889 / 25,124.69 | 3,383 / 3,625.51 | 三层中均占主导；不直接写成“非法采伐” |
| 胁迫（Stress） | 80,226 / 63,275.25 | 708 / 640.34 | 0 / 0.00 | 近期子集中未出现；不能据此断言没有胁迫 |
| 野火（Fire/Wildfire） | 48,167 / 133,181.65 | 321 / 393.92 | 8 / 15.84 | 近期子集中数量和面积较少；仍需影像或外部火点核查 |

> agent 字段中的 fire 在周报中统一写作“野火”。三类是模型归类，不等同于现场事实；未确认结果使用“遥感发现/疑似”。

## 5. 当前重点关注

近期检测子集面积最大的 10 个要素全部属于采伐类，检测日期均为 2026-09-12。它们主要分布在大兴安岭、湘中盆地和四川盆地：

| 排名 | 区域 | 类型 | 面积（ha） | 中心经度 | 中心纬度 |
|---:|---|---|---:|---:|---:|
| 1 | 大兴安岭 | 采伐 | 40.8924 | 123.257142 | 51.167442 |
| 2 | 大兴安岭 | 采伐 | 33.2364 | 122.804506 | 51.688811 |
| 3 | 四川盆地 | 采伐 | 29.8914 | 100.332560 | 28.568003 |
| 4 | 湘中盆地 | 采伐 | 28.4055 | 114.129493 | 26.701730 |
| 5 | 大兴安岭 | 采伐 | 26.5711 | 122.751845 | 51.531594 |
| 6 | 大兴安岭 | 采伐 | 25.1283 | 122.211237 | 51.620818 |
| 7 | 大兴安岭 | 采伐 | 23.2385 | 122.790491 | 51.681094 |
| 8 | 湘中盆地 | 采伐 | 21.4305 | 112.115257 | 25.245642 |
| 9 | 湘中盆地 | 采伐 | 21.1603 | 112.115234 | 25.245630 |
| 10 | 四川盆地 | 采伐 | 17.4663 | 100.365975 | 28.566460 |

**重点判断**：大兴安岭占近期子集面积约 70.3%，且进入最大 10 个要素中的 5 个；应优先核查。湘中盆地第 8、9 个要素中心点几乎重合，可能是相邻或重复记录，不能直接当作两个独立事件。

**下周重点关注**：优先回看上述坐标对应的遥感影像，核实采伐解译、空间聚集和记录重复情况；在上一期数据到位后，再判断哪些属于本周新增。

> **当前解译边界**：三个图层与三种状态的正式对应关系尚待系统定义；模型类型不是现场事实。统计单位和面积口径将在去重规则确认后统一。

## 6. 仍需补充的数据

这份快照版已经可以作为第一版人工试写稿。要把它变成“本周相对上周”的正式周报，按优先级还需要：

1. **上一期同类 SHP**（优先，约 2026-09-05），用于计算新增、持续未确认、未确认转已确认和本期未再观测到的对象。
2. **系统对三个图层的正式定义**，尤其是 `slgr_detected` 与 `slgr_detected_rec` 的筛选窗口和状态含义；目前只能按“检测层/近期子集”暂称，不能把两者相加。
3. **统计口径确认**：一个要素是否等于一个斑块/事件，以及重复几何如何去重。确认前正文统一使用“要素”，不写“事件数”。
4. **区域名称映射确认**：`daxing`、`sichuan`、`yunnan`、`hunan`、`zhejiang` 与报告中的五个中文区域名称需以系统配置为准。

> 代码 C、D 已完成运行，区域/类型面积和最大 10 个近期要素已写入本稿；暂时不需要重复运行。

---

# QGIS 数据提取记录与复用代码

以下代码已经在 `tmp/20260912` 数据上运行完成；保留在报告中，供下次更新数据时复用。

## 代码 C：按区域和类型统计面积

把 DATA_DIR 改成 SHP 所在文件夹，在 QGIS Python 控制台的编辑器中运行：

```python
from pathlib import Path
from collections import defaultdict
from qgis.core import QgsVectorLayer, QgsDistanceArea, QgsProject

DATA_DIR = Path(r"C:\personal\Jason\llm-wiki-agent\tmp\20260912")
FILES = {
    "confirm": "slgr_confirm.shp",
    "detected": "slgr_detected.shp",
    "detected_rec": "slgr_detected_rec.shp",
}

def text(value):
    if value is None or str(value).strip() == "":
        return "unknown"
    return str(value).strip()

for layer_label, filename in FILES.items():
    layer = QgsVectorLayer(str(DATA_DIR / filename), layer_label, "ogr")
    if not layer.isValid():
        print(filename, "无法读取")
        continue

    area_calc = QgsDistanceArea()
    area_calc.setSourceCrs(
        layer.crs(),
        QgsProject.instance().transformContext()
    )
    area_calc.setEllipsoid("WGS84")

    groups = defaultdict(lambda: [0, 0.0])
    total_count = 0
    total_area = 0.0

    for i, feature in enumerate(layer.getFeatures(), start=1):
        agent = text(feature["agent"])
        province = text(feature["province"])
        geometry = feature.geometry()

        area_ha = 0.0
        if geometry and not geometry.isEmpty():
            area_ha = area_calc.measureArea(geometry) / 10000.0

        groups[(province, agent)][0] += 1
        groups[(province, agent)][1] += area_ha
        total_count += 1
        total_area += area_ha

        if i % 100000 == 0:
            print(filename, "processed", i)

    print("\n===", filename, "===")
    print("TOTAL|features={}|area_ha={:.4f}".format(
        total_count, total_area
    ))
    print("province|agent|features|area_ha")
    for (province, agent), (count, area) in sorted(groups.items()):
        print("{}|{}|{}|{:.4f}".format(
            province, agent, count, area
        ))
```

本次代码 C 的输出已补入正文；更换数据目录后可重新运行。

## 代码 D：提取近期子集最大的斑块

这一步用于填写“重点关注要素”。本次输出已补入正文；更换数据目录后可重新运行：

```python
from pathlib import Path
from heapq import heappush, heappop
from qgis.core import QgsVectorLayer, QgsDistanceArea, QgsProject

DATA_DIR = Path(r"C:\personal\Jason\llm-wiki-agent\tmp\20260912")
path = DATA_DIR / "slgr_detected_rec.shp"
layer = QgsVectorLayer(str(path), "detected_rec", "ogr")

area_calc = QgsDistanceArea()
area_calc.setSourceCrs(
    layer.crs(),
    QgsProject.instance().transformContext()
)
area_calc.setEllipsoid("WGS84")

TOP_N = 10
largest = []

for feature in layer.getFeatures():
    geometry = feature.geometry()
    if not geometry or geometry.isEmpty():
        continue

    area_ha = area_calc.measureArea(geometry) / 10000.0
    point = geometry.centroid().asPoint()
    row = (
        area_ha,
        str(feature["agent"]),
        str(feature["province"]),
        str(feature["detection"]),
        point.x(),
        point.y(),
    )

    if len(largest) < TOP_N:
        heappush(largest, row)
    elif area_ha > largest[0][0]:
        heappop(largest)
        heappush(largest, row)

print("area_ha|agent|province|detection|longitude|latitude")
for row in sorted(largest, reverse=True):
    print("{:.4f}|{}|{}|{}|{:.6f}|{:.6f}".format(*row))
```

## 代码 E：周环比和状态转移（暂缓）

这部分必须先拿到上一期 SHP，并确认三个图层的正式定义。否则无法可靠判断：

- 哪些是本周新增；
- 哪些是持续未确认；
- 哪些由未确认转为已确认；
- 哪些只是同一斑块在不同图层中的重复记录。
