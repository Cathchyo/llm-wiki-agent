<!-- 最小周报模板：只填写本周相对上周的变化；没有数据填“未知”。 -->

# 森林扰动遥感监测周报

> **报告周期**：{{report_period}}  
> **系统更新时间**：{{system_update_time}}  
> **监测范围**：大兴安岭、四川盆地、云南高原、湘中盆地、长江平原  
> **数据来源**：{{data_source}}

## 1. 本周摘要

{{summary_paragraph}}

## 2. 总体与状态变化

### 2.1 总体指标

| 指标 | 本周 | 较上周 |
|---|---:|---:|
| 新增异常斑块数 | {{new_patch_count}} | {{delta_new_patch_count}} |
| 新增异常面积（ha） | {{new_area_ha}} | {{delta_new_area_ha}} |
| 未确认 → 已确认斑块数 | {{new_confirmed_count}} | {{delta_confirmed_count}} |
| 持续未确认斑块数 | {{ongoing_unconfirmed_count}} | {{delta_ongoing_count}} |

### 2.2 三种状态层

日期和具体定义以系统当期页面为准。

| 状态层 | 数量/面积 | 本周变化 | 简要说明 |
|---|---:|---:|---|
| 已确认（Confirmed disturbance after {{confirmed_start_date}}） | {{confirmed_count}} / {{confirmed_area}} | {{confirmed_delta}} | 已进入确认层 |
| 近期未确认（Recent but unconfirmed after {{unconfirmed_cutoff_date}}） | {{recent_unconfirmed_count}} / {{recent_unconfirmed_area}} | {{recent_unconfirmed_delta}} | 新近发现，尚未确认 |
| 较早未确认（Unconfirmed before {{unconfirmed_cutoff_date}}） | {{old_unconfirmed_count}} / {{old_unconfirmed_area}} | {{old_unconfirmed_delta}} | 较早发现，仍待核查 |

## 3. 五个区域的变化

| 区域 | 本周新增/确认 | 主要类型 | 与上周相比 | 关注事项 |
|---|---|---|---|---|
| 大兴安岭 | {{dx_change}} | {{dx_types}} | {{dx_comparison}} | {{dx_attention}} |
| 四川盆地 | {{sb_change}} | {{sb_types}} | {{sb_comparison}} | {{sb_attention}} |
| 云南高原 | {{yn_change}} | {{yn_types}} | {{yn_comparison}} | {{yn_attention}} |
| 湘中盆地 | {{xb_change}} | {{xb_types}} | {{xb_comparison}} | {{xb_attention}} |
| 长江平原 | {{yp_change}} | {{yp_types}} | {{yp_comparison}} | {{yp_attention}} |

## 4. 三类扰动解译

| 类型 | 涉及区域 | 数量/面积 | 本周变化 | 简要描述 |
|---|---|---:|---|---|
| 野火（Wildfire） | {{wildfire_regions}} | {{wildfire_count_area}} | {{wildfire_change}} | {{wildfire_description}} |
| 采伐/人为清除（Logging） | {{logging_regions}} | {{logging_count_area}} | {{logging_change}} | {{logging_description}} |
| 胁迫（Stress） | {{stress_regions}} | {{stress_count_area}} | {{stress_change}} | {{stress_description}} |

## 5. 重点事件与后续

| 区域/位置 | 类型 | 状态变化 | 规模 | 需要关注的原因/下一步 |
|---|---|---|---:|---|
| {{event_1_location}} | {{event_1_type}} | {{event_1_status_change}} | {{event_1_size}} | {{event_1_action}} |
| {{event_2_location}} | {{event_2_type}} | {{event_2_status_change}} | {{event_2_size}} | {{event_2_action}} |
| {{event_3_location}} | {{event_3_type}} | {{event_3_status_change}} | {{event_3_size}} | {{event_3_action}} |

**下周重点关注**：{{next_week_focus}}

> **解译边界**：野火、采伐、胁迫是模型归类，不等同于现场事实；未确认结果使用“遥感发现/疑似”，胁迫不直接断定具体虫害或干旱，采伐不直接写成“非法采伐”。统计单位和面积口径：{{counting_rule}}。
