Remote Sensing of Environment 342 (2026) 115461
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Near-real-time mapping for causal agents of forest disturbances in China
using harmonized Landsat and Sentinel-2 dataset
Ronghua Liaoa,b, Chengcheng Guob, Lingkun Chena,b, Yulin Jianga,b, Yuchen Taoa,b,
Jiani Liaoa,b, Rui Lua,b, Huaguo Huangc, Zhou Shia,b, Su Yea,b,*
aState Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China
bZhejiang Key Laboratory of Agricultural Remote Sensing and Information Technology, Zhejiang University, Hangzhou 310058, China
cState Forestry and Grassland Administration Key Laboratory of Forest Resources and Environmental Management, Beijing Forestry University, Beijing 100083, China
A R T I C L E I N F O A B S T R A C T
Edited by Marie Weiss Timely identification of forest disturbance agents is essential for effective ecosystem management and rapid
response to natural and anthropogenic threats. However, most near-real-time (NRT) monitoring systems focus
Keywords: solely on detecting disturbance locations and timing of generic disturbances, lacking attribution of causal agents
Forest disturbance that is critical for operational decision making. This study presents a novel NRT framework to map major forest
Near-real-time disturbance agents—wildfire, logging, and stress—across China using the Harmonized Landsat and Sentinel-2
Disturbance agent
(HLS) dataset. To address the scarcity of local training data, we introduced a transferring-guided sampling
Time-series
strategy that efficiently generated tile-specific local samples by leveraging disturbance archives from the
Latency
conterminous United States and subsequent expert verification. Stage-based random forest models were subse-
quently constructed using 16 temporally dynamic features derived from HLS spectral trajectories to classify
anomalies at varying disturbance stages. The system achieved an overall first-alert lag of 11.6 days and a level-off
lag of 15.5 days, with corresponding overall accuracies of 77.5% and 84.0%. Wildfire disturbances exhibited the
shortest detection lag and the highest accuracy, followed by logging and stress, reflecting differences in spectral
separability among agents. Compared with the global DIST-ALERT product, the proposed framework achieved
higher accuracy and fewer false detections, at a trade-off of a 3.7-day longer first-alert lag, while providing
actionable information on disturbance causality. These results demonstrate the feasibility of operationally
mapping disturbance agents in near real-time at a national scale. The proposed framework offers a transferable,
data-efficient solution for rapid forest disturbance attribution and provides a foundation for global-scale NRT
disturbance monitoring initiatives.
1. Introduction 2014).
As of 2020, China's forest area reached approximately 220 million
Driven by climate change and anthropogenic factors, a growing hectares, making up about 5% of the world's total forest cover (Sarre,
number of forest disturbances from wildfires, logging and insect out- 2020). Given China's large forested areas and rapid economic expansion,
breaks have emerged globally in recent years (Cohen et al., 2016; Seidl effective monitoring helps address forest fragmentation, habitat
et al., 2014; Tyukavina et al., 2017). With increasing frequency and destruction, and other ecological challenges. Globally exacerbated
severity, the disturbance events disrupt forest structure and composi- climate warming also intensifies natural disturbances in China, such as
tion, causing severe ecological and economic consequences (Dee et al., wildfires (Wu et al., 2019; Zhang et al., 2023) and pest outbreaks (Xu
2025; Thom and Seidl, 2016). Only with timely and detailed disturbance et al., 2023). Particularly, China hosts the world's largest planted forest
maps can forest managers implement mitigation against natural di- area (Cheng et al., 2024), and these planted forests might be more
sasters (e.g., wildfire) through rapid damage assessment and evacuation vulnerable to climate-induced disturbance due to their lower species
planning (Oddo and Bolten, 2019), or enact actions against illegal and richness and greater structural homogeneity (Zhong et al., 2021),
unsustainable forest harvesting (Hansen et al., 2016; Wheeler et al., necessitating timely alerting and intervention.
* Corresponding author at: State Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China.
E-mail address: su.ye@zju.edu.cn(S. Ye).
https://doi.org/10.1016/j.rse.2026.115461
Received 23 October 2025; Received in revised form 7 April 2026; Accepted 26 April 2026
Available online 6 May 2026
0034-4257/© 2026 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Near-real-time (NRT) disturbance monitoring refers to performing a were originally designed for historical disturbance mapping, their per-
disturbance mapping task with minimal delay between remotely sensed formance under a lack of long-term post-disturbance features remains
image acquisition and decision making. The reported delay ranges from uncertain for the NRT scenario. To our knowledge, Slagter et al. (2023)
several days (Tang et al., 2023; Ye et al., 2024) to two/three months is the only study for addressing disturbance agent mapping in an NRT
(Bullock et al., 2022; Reiche et al., 2018; Tang et al., 2019), depending scenario. Slagter et al. (2023) tested Convolutional Neural Network
on the temporal resolution of the datasets and the chosen algorithm. The (CNN) on Sentinel-1 and Sentinel-2 data composited over a period
earlier NRT disturbance-related studies focused on coarse-resolution ranging from 1 to 6 months after the disturbance for mapping the driver
datasets (> 30 m) with high temporal frequency, such as the MODIS for small-scale tropical forest disturbances (e.g., road development, se-
products (Reymondin et al., 2012; Verbesselt et al., 2012). Methods such lective logging, and mining), reporting that the F1 score increased along
as BFAST Monitor (Verbesselt et al., 2012) and the Terra-I system with the increasing post-disturbance period for compositing (1 month:
(Reymondin et al., 2012) have been widely applied to MODIS daily 0.785; 6 months: 0.851). However, this approach suffers two primary
observations to provide rapid disturbance alerts at global or continental limitations when being operationalized for elsewhere in the world: 1) at
scales. With the open-access policy for Landsat (Woodcock et al., 2008), least one month of detection latency due to its contingency on cloud-free
the NRT monitoring was subsequently extended to the medium- monthly composite; 2) incapability of monitoring deciduous forest dis-
resolution dataset (10–30 m) using such as Landsat (Hansen et al., turbances because it ignores the confusion between disturbance signals
2016; Pasquarella et al., 2017), enabling more detailed mapping of and seasonal defoliation.
forest change. Recently, the combination of several satellite platforms, An NRT monitoring of disturbance agents could be further con-
such as Harmonized Landsat and Sentinel (HLS) dataset (Hansen, 2024; strained by training data availability. A well-trained machine learning
Shang et al., 2022), has proven successful in reducing detection lags model, built on a sufficient number of high-quality training datasets, not
owing to the enhanced data density. While traditional NRT methods only ensures accurate mapping of disturbance agents but also improves
identified spectral anomalies from time-series datasets using a pre- the timeliness of detecting disturbance signals from various spectral
defined threshold for change magnitudes (Olsson et al., 2016; Pas- anomalies (Ye et al., 2024). Some existing studies manually interpreted
quarella et al., 2017; Shang et al., 2022; Tang et al., 2019; Verbesselt a set of disturbance agent samples and established a single classification
et al., 2012; Ye et al., 2021a), Ye et al. (2024)showed that the retro- model that is applied into the study area (Hermosilla et al., 2015; Ken-
spective analysis on early signals of historical disturbances through nedy et al., 2015; Shimizu et al., 2017; Slagter et al., 2023), while the
machine learning could considerably improve the timeliness for alerting performance might be compromised if the samples were not optimal for
disturbances in an NRT manner. Despite various datasets and algo- a local region. To fulfill a localized training sampling, historical
rithms, almost all existing NRT studies only targeted mapping locations disturbance dataset have been utilized to automate agent sample la-
and timing of generic forest disturbances, some of which additionally beling in United States (Pastick et al., 2019; Qiu et al., 2025) and in
provided disturbance probability map (Hansen et al., 2016). In a prac- Canada (Zhang et al., 2022), taking advantage of the abundance of
tical monitoring project, knowing why the disturbance occurs in a timely public disturbance products in these two countries. This approach en-
manner is equally important as being informed of where and when, ables the use of a local model built for a specific region, ultimately
because information on causal agents (e.g., wildfire, logging) is pre- enhancing map quality (Qiu et al., 2025). However, historical distur-
requisite for alert prioritization, actionable management and impact bance dataset covering comprehensive agents is often unavailable for
assessment (Slagter et al., 2023; Stahl et al., 2023). For example, Andela most regions worldwide, including China. To our knowledge, OPERA
et al. (2022)showcased separating wildfire disturbances from logging Land Surface Disturbance Product (Hansen, 2024) is the only global
and drought in Amazon holds great importance for wildfire suppression general disturbance dataset covering China's forest. The OPERA product
and air quality evaluation for this region. Particularly, given the detects recent spectral anomalies for indicating forest loss but lacks in-
increasing prevalence of forest disturbances globally, there is a clear formation on disturbance agents.
need for broadly applicable approaches that can map disturbance causal This study aims to develop a new NRT approach for mapping
agents in a timely manner. disturbance agents, with an application to monitoring forest distur-
The current challenges surrounding NRT disturbance agent mapping bances in China and potential transferability to other regions globally.
are primarily two-fold: methodological limitations and data constraints. To overcome the limitation of scarce local training data, we designed a
While numerous successful studies have mapped historical disturbance labor-saving workflow to generate local samples at a per-tile basis
agents (Hermosilla et al., 2015; Kennedy et al., 2015; Qiu et al., 2025; through a transfer mapping using disturbance samples from CONUS and
Stahl et al., 2023), the retrospective approaches may not be directly manual verification. Rich spectral-temporal features following distur-
applicable or could perform poorly in an NRT task. Most studies have bances were extracted from the Harmonized Landsat and Sentinel-2
utilized temporal segmentation on annual time series and then classified (HLS) dataset, which provides the densest moderate-resolution obser-
spectral breaks based upon spectral attributes of the breaks (Hermosilla vations to date. To enhance discrimination among disturbance agents,
et al., 2016; Hermosilla et al., 2015; Kennedy et al., 2015; Schroeder particularly during the early stages of disturbance, we constructed stage-
et al., 2017; Shimizu et al., 2017). A more advanced approach involved specific models informed by the number of consecutive anomalies
applying an end-to-end deep learning model on annual composite (Chen detected, and applied them for the NRT monitoring scenario. Consistent
et al., 2021; Perbet et al., 2024), instead of a two-step procedure for with previous studies (Hermosilla et al., 2015; Zhang et al., 2022), we
temporal segmentation and break classification. Both approaches adopted a three-agent classification system, consisting of wildfire, log-
generated agent maps annually at their fastest update rate, making them ging, and stress, with detailed definitions provided in Table 1.
insufficiently timely for an NRT monitoring task. Other approaches
chose dense time series as inputs from single-sensor or multi-sensor
Table 1
combination, often processing a long temporal window for post- Definition for three major disturbance agents in this study.
disturbance observations. As a result, while the estimated disturbance
Agents Description
dates can be close to reference dates, their operational timeliness in an
NRT context remains limited when disturbances need to be character- Wildfire Wildfire in forests or wooded land, including unplanned and prescribed
fires
ized within days to weeks. Zhang et al. (2022) required a synthetic
Logging The removal of forested vegetation by human activity such as timber
image from one year after the spectral break as one of machine-learning harvesting and construction, such as clear cutting, selective logging, etc.
inputs for classifying for boreal forest agents. Likewise, Qiu et al. (2025) Stress Biological or environmental press that undermines forest health, vigor, or
included harmonic coefficients of the post-disturbance segment (at least resilience without causing stand-replacing canopy damage, such as insect
infestation and drought.
one year) in their land agent classification model. Since these studies
2

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
2. Study sites and datasets observed in other subtropical regions of China. The Yangtze Plain (YP)
site, located in Zhejiang Province, is dominated by subtropical evergreen
2.1. Study sites broad-leaved forests and mixed deciduous–evergreen communities,
which together sustain a rich diversity of tree species. As one of China's
We chose the five study sites across a large geography of China, most developed regions, YP contains forests that are highly susceptible
representing a variety of forest types and disturbance agent patterns to human disturbances, particularly land-use conversion. The last study
(Fig. 1). Daxing'anling (“DX”), one of China's most wildfire-prone forest site, YunNan plateau (YN), hosts diverse forest ecosystems, ranging from
areas, is located in the northwestern Heilongjiang and northeastern tropical monsoon rainforest in the south to evergreen broadleaf forests
Inner Mongolia Province, which is cold-temperate deciduous coniferous in higher elevations. According to the past study (Lin et al., 2021), pine
forest dominated by Larix gemelini. The wildfire for this region mainly shoot beetles have caused extensive tree mortality, leading to consid-
occurred in spring and fall, mainly caused by lightning (Zhao et al., erable ecological impacts across the forests of this region. All sites
2020). It has been reported that frequency and severity of the lightning- include all three disturbance agents, with a summary of forest types and
induced wildfires are both increasing recently (Hu and Zhou, 2014). The primary disturbance agents provided in Table 2.
Sichuan Basin (SB) site, situated in southwestern China, is characterized
by evergreen broadleaf forests, mixed conifer–broadleaf stands, and 2.2. Datasets
extensive bamboo forests. These ecosystems often contain dense un-
derstory vegetation and substantial fuel loads. The accumulation of dry We used 2016 China Land Cover Dataset (CLCD) product (Yang and
branches, fallen leaves, and intertwined weeds further increases wildfire Huang, 2021) to define forest pixel population for NRT monitoring.
risk, making the region highly prone to wildfires. The Xiangzhong Basin CLCD, one of the most commonly used land cover products for China,
(XB), situated in central Hunan Province, falls within the subtropical was created by training a random forest with temporal metrics using
monsoon climate zone, characterized by warm, humid conditions and training samples from the public products, which reports to have an
abundant rainfall. Forest disturbances in this region are primarily driven overall accuracy of ~80% (Yang and Huang, 2021).
by logging and wildfire (Cao et al., 2025). In particular, timber har- We selected HLS time series datasets as the primary data source for
vesting and land conversion were largely driven by wood demand and performing the NRT task in China as well as extracting primary distur-
agricultural expansion, which follows patterns consistent with those bance features in CONUS. To create a seamless surface reflectance from
Fig. 1. Five study sites for testing an NRT forest disturbance monitoring in China. For each site, nine adjacent Harmonized Landsat and Sentinel (HLS) tiles were used
for testing the performance of the proposed approach (highlighted as yellow polygons). (For interpretation of the references to colour in this figure legend, the reader
is referred to the web version of this article.)
3

the Operational Land Imager (OLI) and Multi-Spectral Instrument (MSI)
aboard Landsat-8/9 and Sentinel-2 A/B satellites, the HLS dataset har-
monizes their products through radiometric calibration, common
gridding, bandpass alignment, and geometric co-registration (Claverie
et al., 2018; Ju et al., 2025). With four sensors currently in the virtual
constellation, HLS provides observations once every 2–3 days with 30-m
resolution, offering the highest temporal resolution available for moderate-resolution datasets. To guarantee the densest time series, we
hereafter focused on only six spectral bands present on both HLS Landsat
(L30) and Sentinel-2 (S30) products (Table S1 of the supplementary
material).
Similar to the previous work (Ye et al., 2024), we collected an
ensemble of annual CONUS-wide disturbance products from 2017 to
2021, which were used to build the CONUS sample archive for pre-
liminary mapping in China. These products include Landsat-based
Burned Area (BA) Science Product (Hawbaker et al., 2020) for wild-
fire, and Aerial Detection Survey (ADS) insect activity dataset (Johnson
and Wittwer, 2008) for stress disturbances. We also include Land
Change Monitoring, Assessment, and Projection (LCMAP) Primary Land
Cover maps (Xian et al., 2022) and LANDFIRE Annual Disturbance
Products (Ryan and Opperman, 2013) to indicate logging regions (see
Section 3.1).
3. Methodology
In this study, we adopted a two-level hierarchical framework to
define discontinuities detected in the time series: anomaly and break
levels. Their relationships with disturbance agents are illustrated in
Fig. 2. Spectral anomaly refers to any observation where the spectral
reflectance deviates from the expected patterns predicted by the his-
torical time series. Such anomalies are not always linked to distur-
bances; they may instead arise from processes such as succession,
phenological shifts, climate variability, or even data noise (Zhu et al.,
2022). We therefore categorized those anomalies not directly linked to
disturbances as “non-disturbance anomalies”. A “spectral break”, on the
other hand, represents a cluster of anomalies with large magnitudes and
extended durations, resulting in a structural change in the time series.
2
elbaT
.setis
yduts
evfi
rof
stesatad
dna
,ecnabrutsid
,tserof
ehT
seliT
)SLH(
lenitneS
dna
tasdnaL
dezinomraH
detceleS
stnega
ecnabrutsid
yramirP
seiceps
eert
yramirP
sepyt
tserof
yramirP
eman
etiS
,SWU15
,SVU15
,TXU15
,TWU15
,TVU15
,UXU15
,UVU15
gniggollaicremmoc，serfidliW
allyhpytalp
aluteB
,sirtsevlys
suniP
,inilemeg
xiraL
tserof
suorefinoc
suoudiced
etarepmet-dloC
)XD(
gnilna'gnixaD
UWU15
,SXU15
,TTR84
,MQR74
,MPR74
,NQR74
,NPR74
,PQR74
,PPR74
serfidliW
supracohtiL
,sisponatsaC
,sisponalabolcyC
stserof
devael-daorb
neergreve
laciportbuS
)BS(
nisaB
nauhciS
UTR84
,STR84
,KFR94
,KGR94
,HHR94
,HGR94
,HFR94
,JGR94
,JFR94
dnal
yb
nevird
gnittuc
raelC
supracohtiL
,sisponalabolcyC
,sisponatsaC
stserof
devael-daorb
neergreve
laciportbuS
)BX(
nisaB
gnohzgnaiX
QKR05
,JHR94
noisrevnoc
,NTR15
,PUR15
,PTR15
,TQR05
,SQR05
,UQR05
dnal
yb
nevird
gnittuc
raelC
,ataloecnal
aimahgninnuC
,abrepus
amihcS
oobmab
,stserof
devael-daorb
neergreve
laciportbuS
)PY(
nialP
eztgnaY
MUR15
,MTR15,NUR15
noisrevnoc
silude
syhcatsollyhP
stserof
,GNQ74
,HQR74
,HPR74
,HNR74
,JQR74
,JPR74
,JNR74
erfidliw
,secnabrutsid
tcesnI
sutanibrut
supracoretpiD
,sisnenannuy
suniP
laciport
,stserof
devael-daorb
neergreve
laciportbuS
)NY(
uaetalp
naNnuY
GQQ74
,GPQ74
stserof
niar
noosnom
R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Fig. 2. Spectral anomalies constitute a broad category encompassing all
irregular signals detected in satellite-based time-series datasets. A subset of
these anomalies emerges as spectral breaks, which represent pronounced and
persistent structural shifts in the spectral trajectory. While many spectral breaks
are typically associated with forest disturbance events such as wildfire or log-
ging, non-disturbance processes, including vegetation succession and climate
variability, can also produce break-like signals. Conversely, certain disturbance
events, such as drought stress or understory wildfires, may induce only subtle or
short-lived anomalies that do not evolve into detectable breaks. This study
aimed to detect and classify spectral anomalies into four categories (blue fonts
in the figure): wildfire, logging, stress, and non-disturbance anomalies. (For
interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)
4

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Fig. 3. The three-step workflow of the NRT forest disturbance agent mapping for this study.
Breaks are characterized by significant changes in statistical properties 3.1. CONUS sample preparation
(e.g., mean, variance) between pre- and post-change segments. When a
spectral break is detected, the time series model requires re-initialization 3.1.1. CONUS sample selection
using a CCDC-like approach, which necessitates at least 12 clear ob- We created a high-confidence agent sample archive from the
servations and a time span of one year (Zhu et al., 2022). This re- consensus between spectral anomaly detection and CONUS-wide
initialization complicates NRT monitoring, as the absence of a stable disturbance products. Fifty HLS grids were randomly sampled across
model in the new segment reduces temporal continuity, therefore a CONUS (Fig. S1 in the supplementary), covering a variety of geographic
stricter threshold is expected for break detection to minimize unnec- extent. The Stochastic Continuous Change Detection (S-CCD) algorithm
essary model reset. To address this challenge, we implemented a unified (Ye et al., 2021a) was implemented on all available HLS images of each
monitoring workflow with two detection levels following the previous tile (2016–2022) and produced a series of annual spectral anomaly maps
study (Ye et al., 2024): (1) the anomaly level, using a sensitive config- from 2017 to 2021. S-CCD (https://github.com/Remote-Sensing-of-Lan
uration (changethreshold =0.90,conse =3) to inclusively detect all types d-Resource-Lab/pyxccd), a short-memory adaptation of the CCDC al-
of spectral anomalies without triggering model re-initialization; and (2) gorithm that incorporates the Kalman filter, has two functionalities for
the break level, using a conservative configuration (changethreshold = this study: retrospective analysis for historical anomalies and NRT
0.9999,conse =8) to identify pronounced structural changes that justify monitoring for the most recent anomalies. This approach ensures the
model reset. Here, change threshold indicates the chi-square probability consistent feature generation between the retrospective and the NRT
for identifying spectral anomalies, while conse specifies the minimum scenario. The anomalies for the first (2016) and the last year (2022) of
consecutive number of anomalies required to confirm a break. Using this data range were excluded because the quality of spectral anomalies are
conservative break configuration, only 1.7% of forest pixels triggered a often unsatisfactory for CCDC-like algorithms.
break by the final weekly update (Table S2), indicating that model resets For open-access disturbance products, we first generated a general
were rare. The primary objective of this study is to classify spectral disturbance map at an annual step by combining Landsat-based BA
anomalies, rather than breaks, into disturbance agents in an NRT product, ADS dataset for stress samples, the category transition map
manner. from differencing LCMAP Primary Land Cover maps between two
Our workflow proceeds in three stages (Fig. 3). First, we generated neighbor years, and the annual LANDFIRE disturbance map. By over-
high-quality disturbance agent samples for CONUS by using the lapping the general disturbance map with its corresponding annual
consensus between break detection and multiple disturbance products. spectral anomaly map, we identified four distinct sample pools: one for
Next, the CONUS disturbance samples will be used to guide the local wildfire disturbances, defined by spectral anomalies within the Burned
sample selection and model construction for China. Finally, these Area (BA) region; one for stress disturbances, linked to spectral anom-
disturbance agent models, built from the local disturbance history, were alies overlapping the insect-impact region as indicated by the ADS map;
applied to direct NRT monitoring for recent disturbances. one for logging disturbances, consisting of spectral anomaly pixels
within forest transition regions identified by category changes in LCMAP
5

R. Liao et al.                                                                                                                                                                                         R  e  m  o  t e   S  e  n  s i n g    o  f   E  n  v i r o  n  m  e  n  t 342 (2026) 115461
cover maps or marked as “logging” in the LANDFIRE disturbance map;  ⎡ ⎤
0.30370.27930.47430.55850.50820.1863
and one for non-disturbance anomalies (e.g., phenological shifts, image
|     |     |     |     |     |     | B=⎣(cid:0) | 0.2941 (cid:0) 0.243 (cid:0) 0.54240.72760.0713 | (cid:0) 0.1608 | ⎦ (3)  |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------------------------------------- | -------------- | ------ |
noises), which are those spectral anomaly pixels outside the extent of
|     |     |     |     |     |     |     | 0.15110.19730.32790.3406 (cid:0) 0.7117 | (cid:0) 0.4559 |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | -------------- | --- |
general disturbances. We applied stratified sampling to collect 2000
samples from each sample pool per HLS tile for each year (2017 to  In addition, S-CCD preserves the eight multispectral observations
2021). For 50 CONUS tiles, we reached the final CONUS sample archive,  since the first anomaly observation signal. This enables the calculation
consisting of four PIXEL pools, i.e., logging (n =356,604), wildfire (n =
of each band-specific change magnitude at the xth post-anomaly
310,500), stress (n =76,500) and non-disturbance anomaly pool (n = observation (x =1,2,…,8) for the ith band (i =1,2,…,6):
386,594), after excluding non-forest pixels.
|     |     |     |     |     |     | CMi,x =̂ρ | i,x (cid:0) ρ |     | (4)  |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ---- |
i,x
| 3.1.2. | Disturbance agent feature extraction |     |     |     |     | Where ρ | and ̂ρ |     |     |
| ------ | ------------------------------------ | --- | --- | --- | --- | ------- | ------ | --- | --- |
i,x  i,x represents the actual and predicted reflectance for
We extracted 16 disturbance agent features for CONUS samples,
xth observation since the first anomaly signal at the ith band. Corre-
comprising three pre-disturbance features, nine trajectory-based change
spondingly, the TC-based change magnitudes were derived as linear
features, two general change features, one disturbance-date feature and
combinations of these band-wise change magnitude:
one data-density feature. Like other CCDC-type algorithms, S-CCD pro- ⎡ ⎤
CM1,x
duces temporal features (e.g., harmonic coefficients and break-based
|     |     |     |     |     |     | ⎡   | ⎤ ⎢ ⎢ C M ⎥ ⎥ |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
c h a n g e   m a g n i t u d e s )   f o r   e a c h   o r i g i n a l   b a n d .  A c c o r d i n g l y ,   t h e   p r e d i c t e d   C M , ⎢ 2 , x ⎥
|     |  ̂ρ |     |     |     |     | ⎣ b | r i x ⎦=B• ⎢ C M , ⎥ |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
r e fl e c t a n c e i ,x   f o r  x t h   o b s e r v a t i o n   s i n c e   t h e   fi r s t   a n o m a l y   s i g n a l   a t   t h e   C M , ⎢ 3 x ⎥ (5)
|     |     |     |     |     |     | g r | e x ⎢ C M , ⎥ |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
it h   H L S   b a n d   ( i = 1 , 2 , … , 6 )   i s   r e c o n s tr u c te d   f r o m   t h e   p r e - d i s t u r b a n c e   C M , ⎣ 4 x ⎦
|                         |     |     |     |     |     | w   | e t x C M , |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
| harmonic coefficients:  |     |     |     |     |     |     | 5 x         |     |     |
CM6,x
|     | (      | (   | )   | (   | ))  |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ∑n = 2 | πk  |     | πk  |     |     |     |     |     |
̂ρ =a0,i + 2 date(x) +bk,icos 2 date(x) W e   f u r t h e r   c o n st r u c t ed   sp e c t r a l  tr a j e c to r i e s   b y  t r a c k in g  ρ , ρ ,
| i,x | ak,icos |     |     |     |     |     |     |     | b ri, x g r,x |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | ------------- |
T T (1)  and  ρ a c r o s s   su c c e s si v e  p os t - a n o m a l y   o b s e r v a t io n s   ( x = 1 , 2 , … , 8 ).
|     | k= 1 |     |     |     |     | w   | et ,x   |     |     |
| --- | ---- | --- | --- | --- | --- | --- | ------- | --- | --- |
+c1,idate(x)
From each trajectory, a set of descriptors was derived in the two-
dimensional feature space (date, ρ). Specifically, Slope denotes Theil-
Where ak,i and bk,i are the harmonic coefficients, k is temporal fre-
Sen slope representing the general spectral trend after disturbance
quency of harmonic component, n is the number of harmonic pairs (note
occurrence. Intercept is the intersecting point between the first anomaly
that n=2 for S-CCD), T is the number of days per year (T=365.25).
date and the Theil-Sen trendline, which represents the initial post-
Following Zhang et al. (2022), we reduced the six HLS spectral bands
anomaly feature value. Because trajectories may deviate from line-
| into  | three  physically  | meaningful  | components,  | namely  | brightness,  |     |     |     |     |
| ----- | ------------------ | ----------- | ------------ | ------- | ------------ | --- | --- | --- | --- |
arity, skewness of the residuals is used to quantify asymmetric departures
greenness, and wetness, using the Tasseled-Cap (TC) transformation.  from the fitted linear trend:
This feature reduction effectively halved the dimensionality of the input
∑x ( (cid:0) )
s p a c e ,  t h e r e b y  a ll e v i a ti n g  p o t e n t ia l   o v e r fi t t i n g  a n d   p o o r  g e n e ra l iz a ti o n   = 1 ei e 3
|     |     |     |     |     |     | skewnessx |     |     | (6)  |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | ---- |
a ss o c i a t e d   w i th  a   h i g h - d im e n s i o n a l   fe a t u r e   i n p u t  ( V e r le y s e n  a n d  F r a n - x s
i
çois, 2005). The three pre-disturbance features, selected for disturbance
agent prediction in this study, were derived from the predicted reflec- Where x is the current number of successive anomalies since the first
̂
tance at the first post-anomaly observation (x =1):  anomaly signal, ei is the residual between the predicted C Mi by the
⎡ ⎤ Theil-Sen linear equation and the actual CMi, and s is the standard de-
̂ρ
⎢ 1 , 1 ⎥ v i a t i o n   o f   e .   A s   a   r e s u l t ,   f o r   e a c h   a n o m a l y   s e g m e n t ,   n i n e   t r a j e c t o r y -
| ⎡   | ⎤ ⎢ ̂ ρ | ⎥   |     |     |     |     | i   |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
̂ρ , ⎢ 2 , 1 ⎥ b a s e d   f e a t u r e s   w e r e   g e n e r a t e d   c o r r e s p o n d i n g   t o   t h r e e   t r a j e c t o r y   d e-
| ⎣ b r i | p r e ⎦=B• ⎢ ̂ ρ | , ⎥ |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
̂ρ , ⎢ 3 1 ⎥ (2)  s c r i p t o r s   ( s l o p e ,   i n t e r c e p t ,   a n d   s k e w n e s s )   f o r   e a c h   o f   t h e   t h r e e   T C   c o m -
| g r e | p r e ⎢ ̂ ρ | , ⎥   |     |     |     |     |     |     |     |
| ----- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| ̂ρ    | , ⎣ ̂       | 4 1 ⎦ |     |     |     |     |     |     |     |
w e t p r e ρ 5,1 p o n e n t s   ( b r i g h t n e s s ,   g r e e n n e s s ,   a n d  w e t n e s s ) .  W e   a s s i g n e d  z e r o s   t o   t h e m
̂ρ if x=1. Notably, trajectory-based features could differentiate distur-
6,1
bance agents to some degree (see Fig. S2), but are not assumed to exhibit
The matrix B represents the TC coefficient matrix for Landsat 8, as
a universal, globally consistent pattern across all regions. We used these
outlined in (Baig et al., 2014). Since the Sentinel-2 data in the HLS
features primarily for local discrimination, as our disturbance-agent
dataset was “spectrally adjusted to match Landsat 8/OLI spectral
classifiers were trained on a per-tile basis using locally verified sam-
bandpasses” (Claverie et al., 2018), it is appropriate to use the Landsat 8
ples, allowing the models to learn region-specific relationships between
TC coefficients for HLS. The coefficients are as follows:
trajectory descriptors and disturbance agents.
In addition, we incorporated two general change features from
Table 3
Definition of 16 disturbance agent features for this study. “Time-varying” means that the features are varying with post-anomaly observation collection in an NRT
scenario for a pixel.
| Predictor name |     |     |     |     | Description/Equation |     |     |     | Time-varying |
| -------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ------------ |
1. Pre-disturbance features ̂ρ bri,pre ,̂ρ gre,pre ,̂ρ wet,pre No
2. Spectral-trajectory descriptors slopebri ,slopegre ,slopewet , Yes
|                                |     |     |     |     | i n te r c e p t b r i , i nt | erc ept g re , in t e r c e p t )we t ,skewnessbri | ,skewnessgre ,skewnesswet |     |     |
| ------------------------------ | --- | --- | --- | --- | ----------------------------- | -------------------------------------------------- | ------------------------- | --- | --- |
|                                |     |     |     |     |                               | ∑ (                                                |                           |     |     |
| 3. Normalized change magnitude |     |     |     |     |                               | 6 C M i , x 2                                      |                           |     | Yes |
|                                |     |     |     |     | C M n o r m a li z e d , x    | =                                                  |                           |     |     |
|                                |     |     |     |     |                               | i = 2 r m s e i , x                                |                           |     |     |
1 ∑ (cid:0)
| 4. Spectral consistency angle |     |     |     |     | angle=   | n 1β         |     |     | Yes |
| ----------------------------- | --- | --- | --- | --- | -------- | ------------ | --- | --- | --- |
|                               |     |     |     |     | n(cid:0) | 1 j= 1 j,j+1 |     |     |     |
5. First anomaly day of year (DOY) DOY of the first anomaly observation No
| 6. Anomaly span |     |     |     |     | ndays=lastobsdat(cid:0) | distdat |     |     | Yes |
| --------------- | --- | --- | --- | --- | ----------------------- | ------- | --- | --- | --- |
Note: β j,j+1 is the change-vector angle from jth to j+1th anomaly; lastobs dat and dist dat are the last available observation date and the disturbance starting date.
6

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Then, we computed Mahalanobis distance between each U.S. sample (k)
and the multivariate distribution:
√̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
dx = (k(cid:0) μ)TS(cid:0)1(k(cid:0) μ) (7)
We ranked the samples in each of the four CONUS sample pools by
their Mahalanobis distance to the targeted China tile and selected the
top 30% as the initial sample set. To evaluate this strategy, we compared
the average Bhattacharyya distance (BD) between (1) the full CONUS
samples and the local China samples (derived from expert-verified
preliminary maps; Section 3.2.2), and (2) the selected CONUS samples
and the same local China samples, across 45 target tiles. BDs were
Fig. 4. Conceptual figure for transferring CONUS samples for a specific China's computed for the four most informative disturbance features, as iden-
HLS tile. A vegetation–topography feature space is constructed for all CONUS tified by random-forest Gini importance (Section 3.2.3). The results
samples. The target domain is defined by the feature distribution of the target (Fig. S3 of the supplementary material) show that BDs decreased after
tile. After similarity screening (top 30%) and equal interval sampling, a
selection for stress and wildfire, indicating that the distribution of
representative sample set matching the target domain is generated for subse-
transferred samples becomes more similar to the target-domain samples
quent local model training.
when guided by topographic and vegetation similarity. In contrast, BD
changes were more variable for logging, likely reflecting greater het-
COntinuous monitoring of Land Disturbances (Zhu et al., 2019a, 2019b),
erogeneity and region-specific management practices that are not rep-
i.e., normalized change magnitudes and spectral consistency angle,
resented during sample transfer. Overall, these results suggest that
which has shown effectiveness for distinguishing true disturbances from
topographic and vegetative matching can effectively improve cross-
noisy signals, especially when multiple consecutive anomalies are
region sample alignment, particularly for natural disturbances,
available. Finally, we added “first anomaly day of year” to account for
thereby strengthening subsequent disturbance mapping.
the occurrence date of a disturbance (e.g., wildfire disturbances occur
For the agent proportion, we first used an empirical equation from
more in April in China due to tomb-sweeping practices for Qingming
the previous study to determine the proportion for non-disturbance
Festival), and “anomaly span” to incorporate the effects of data density.
anomalies (Ye et al., 2024). The proportion was calculated as:
Collectively, we adopted 16 disturbance features for building agent
classification models (Table 3). Of note is that as a part of disturbance Prop nodisturb =0.9(cid:0) (CONSE(cid:0) x)*0.02 (8)
features are time-varying with more observation being collected (see
Where CONSE is the maximum number of consecutive anomalies, set
Table 3), we created a set of features for every possible number of
to 8, x is the number of consecutive anomalies to be investigated. We
consecutive anomalies from (x =1,2,…,8). used x =6, as six consecutive anomalies has been widely used for CCDC-
like approach as the default parameter (Xian et al., 2022; Zhu et al.,
2020; Zhu and Woodcock, 2014). Therefore, the proportion for non-
3.2. Local agent model construction for China
disturbance anomalies is 86% (i.e., 0.9 – (8–6) * 0.02). The remaining
sample number were equally distributed to three disturbance agents. A
For each targeted HLS tile in China, we first applied retrospective S-
total of 10,000 CONUS samples spanning from 2017 to 2021 was applied
CCD to all available HLS images from 2016 to 2023. This process yielded
for each tile, following the previous work (Ye et al., 2024). As a result,
segment-based harmonic coefficients at the per-pixel level, together
the sample numbers for non-disturbance anomalies, wildfire, logging,
with 16 disturbance-agent features for all identified anomalies. These
and stress were 8600, 467, 467, and 467, respectively. Equal prior
outputs served three purposes: (1) characterizing the vegetative condi-
probabilities were assumed for all disturbance agents, since their rela-
tions of each tile to guide the selection of the most appropriate CONUS
tive area proportions could not be estimated prior to the generation of
subsample; (2) providing spectral anomalies and their associated fea-
the classification map (Qiu et al., 2025).
tures for constructing preliminary historical disturbance maps; and (3)
From this set, we then applied an equal-interval sampling strategy to
supplying the initial data inputs for recursive updates in the NRT
construct CONUS samples per sample pool. For instance, within the
monitoring framework. A detailed description is provided below.
wildfire pool (310,500 samples), we retained the top 93,150 samples
(30%) and subsequently selected every 199th sample (93,150/467) in
3.2.1. Sample transfer
Building upon “similar geographic configurations lead to similar ascending order of Mahalanobis distance. The equal-interval sampling
geographic processes” (Zhu et al., 2018), which has been successfully approach minimizes redundancy from any single geographic region,
thereby enhancing the overall diversity of the selected samples.
applied in sample transferring (Cui et al., 2025; Hou et al., 2025; Zhu
et al., 2019a, 2019b), we proposed the hypothesis that “the more similar
3.2.2. Transferring-guided local samples
the topographic and vegetation conditions, the more similar the
disturbance spectral features are”. Based on this, we developed a method We collected 10,000 CONUS samples from the sample-transfer pro-
cedure and transfer 16 disturbance-agent features from CONUS
for selecting a subsample from the CONUS sample archive that most
(Table 2) derived from six consecutive anomalies (x = 6) to train an
closely matches the characteristics of a targeted HLS tile in China
initial random forest model for each tile. These features represent a
(Fig. 4). The topographic variables considered include the digital
multi-dimensional feature space that combines both pre-disturbance
elevation model (DEM) and slope, derived from Shuttle Radar Topog-
signatures and disturbance-process changes, improving separability
raphy Mission (SRTM) data (Yang et al., 2011). The vegetative variables
among disturbance agents. We note that we did not explicitly incorpo-
consist of pre-disturbance TC brightness, TC wetness, and TC greenness,
rate land management policies or other socio-economic features into the
which were calculated from synthetic surface reflectance images (dated
NRT agent classification framework, mainly because adequate high-
July 1, 2016) generated through segment-based harmonic coefficients,
resolution, spatially consistent socio-economic and policy datasets are
following the CCDC framework (Zhang et al., 2022; Zhu et al., 2015).
not readily available for our study regions. Nevertheless, regional dif-
Each targeted tile was characterized by constructing a multivariate
ferences in management intensity, land use pressure, accessibility, and
normal distribution based on these two topographic and the three
vegetative variables. Their mean vector (μ) and covariance matrix (S) enforcement can strongly influence both the frequency and composition
were computed from the “forest” pixels identified by the CLCD product. of disturbance agents, likely contributing to the spatial variability in
7

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Fig. 5. Manual verification example for a patch labeled as wildfire in the preliminary disturbance mapping (Latitude: 28.1524◦N; Longitude:120.1326◦E). (a) Time-
series trajectory showing a distinct temporal break characterized by a sharp decrease in NIR reflectance. (b) HLS image chips (true colour composite) acquired near
the disturbance date across three consecutive years. The observed burn scar and concurrent spectral decline confirmed that the preliminary wildfire label was
correctly assigned.
disturbance regimes observed across the five study sites. Accordingly, disturbance anomalies) within each HLS tile, evenly distributed to
our workflow was designed to be locally adaptive, because models and each year from 2019 to 2023. To address the uncertainties in the pre-
class proportions were constructed on a per-tile basis with local verifi- liminary mapping results, four experienced interpreters were recruited
cation, which helped accommodate regional differences in disturbance to manually verify the patch labels. The verification was based on pre-
regimes even when the underlying drivers differ. made figures that included both HLS time-series plot of the center
Subsequently, we applied S-CCD to all available HLS imagery to pixel and HLS image chips (see the example of Fig. 5). All interpreters
detect spectral anomalies for each forest pixel in the targeted tiles be- received training and testing prior to the labeling task to ensure
tween 2019 and 2023. The anomalies were then input into the tile- consistent interpretation criteria and efficient review. Only patches with
specific random forest model to produce a five-category map: wildfire, high confidence in their assigned labels were retained. To assess the
logging, stress, non-disturbance anomalies, and anomaly-free forest. The efficiency of this transferring-guided approach, we recorded the time
“anomaly-free forest” class includes forested pixels where no spectral with each interpreter required to complete their respective verification
anomalies were detected by S-CCD in history, indicating that these areas tasks. The verified patches were subsequently dissolved to the pixel level
have not experienced detectable spectral changes in the time period to establish four high-quality local sample pools. The verification out-
analyzed. For each annual disturbance map, we connected two neigh- comes and the corresponding time consumption are summarized in
borhood pixels with the same category and generated historical distur- Table S3 of the supplementary material. On average, for each HLS tile,
bance agent patch maps from 2019 to 2023, which consisted of three an interpreter required approximately 2.1 h to verify 4000 disturbance
types of disturbance agents as well as the non-disturbance anomaly patches from the preliminary mapping, of which 1697 patches (~42%)
category. Among them, we selected 1000 disturbance agent patches for were labeled as high-confidence disturbance agent patches, yielding a
each of the four categories (wildfire, logging, stress, and non- total of 38,286 sample pixels (Table S3). This high interpretation
8

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
efficiency is partially attributed to the fact that the interpreters were not frequency noise. In addition, our workflow further suppressed single-
required to determine the disturbance date, as this information had date artifacts through temporal persistence (consecutive anomalies
already been provided by the S-CCD-derived break date. and stage-based models), explicit inclusion of a non-disturbance
We set a total of 10,000 final local samples for each HLS tile to anomaly class during training, and a spatial sieving filter that removes
construct the final local machine learning model. These samples were very small isolated patches.
drawn from the pixel pool verified to be correct from preliminary Finally, we developed an NRT platform to implement the weekly
mapping. For categorical allocation, the proportion of non-disturbance updating procedure and to visualize the resulting disturbance-agent
anomalies was determined as a negative function of the number of maps. The website address is https://forestwatch.com.cn. The inter-
consecutive anomalies (x), following Eq. 8. This design increases the face of this website was displayed in Fig. S5 of the supplementary
relative proportion of disturbance samples when x is small, thereby material.
enhancing detection sensitivity during the early disturbance stage (Ye
et al., 2024). The remaining proportion was distributed among distur- 3.4. Accuracy and latency assessment
bance agents according to their relative pixel frequencies verified as
correct, ensuring that dominant disturbance types were assigned more We conducted accuracy assessments at the study-site level. For each
samples. The minimum sample number per category is set to 300 pixels, site, 1200 pixel-based samples were generated using stratified random
which guarantees that the minority category will not be under- sampling, with 300 samples assigned to each of the four categories:
represented. Accordingly, we prepared eight sets of local samples cor- wildfire, logging, stress, and non-disturbance forest (including non-
responding to the eight possible numbers of consecutive anomalies (x = disturbance anomalies and anomaly-free forest). The four strata were
1,2,…,8) for each tile. defined as all the pixels being labeled from an ensemble of 52 weekly
NRT disturbance agent maps. Across the five representative study sites,
3.2.3. Stage-based local models for China this yielded a total of 6000 samples for evaluating the overall model
We constructed stage-based disturbance agent models for each tile performance. Experienced interpreters manually determined the refer-
using the corresponding sample sets and their 16 agent-based features ence disturbance category and occurrence date for each sample pixel
(Table 3), with the disturbance stage indicated by the number of primarily using daily 3-m Planet imagery. Additionally, for stress vali-
consecutive anomalies. This stage-wise design allowed us to capture the dation, we relied on the HLS time-series interpretation for (1) a signif-
statistical relationships more acutely between the features and distur- icant SWIR2 increase with stable NIR band (e.g., bark borer) (Ye et al.,
bance agents, particularly during the early stage when a disturbance had 2021b) or (2) a pronounced NIR drop followed by rapid recovered (e.g.,
just begun (i.e., x = 1or2). As such, eight disturbance agent models defoliator) (Silva et al., 2013). The occurrence date was defined as the
(x =1,2,…,8) were trained from local samples for the NRT mapping. first day on which an anomaly signal could be visually identified from
We also assessed the average Gini-based feature importance across all the Planet image, enabling evaluation of the system's detection latency
tiles for these eight models (Fig. S4 in the supplementary material). The under operational conditions. Of note is that daily Planet imagery was
analysis reveals that (1) normalized change magnitude and spectral not guaranteed for all study sites (with approximately 30% of the days
consistency angle are consistently the most important features, and (2) missing), which could introduce some uncertainties when interpreting
spectral-trajectory descriptors, especially the greenness and brightness the reference disturbance dates. Despite this limitation, we believe that
intercepts, exerts a significant role in influencing the model performance using Planet imagery remains the most reliable method available for
across all stages. interpreting the reference dates.
We first used these samples to assess individual agent mapping ac-
3.3. Near-real-time mapping in China curacy across 52 weekly NRT agent maps in 2024. Following the sigmoid
framework proposed by Bullock et al. (2022), we generated lag-accuracy
We implemented NRT disturbance-agent monitoring for 2024 across curves for each agent to illustrate how accuracy varies with detection
the five study sites using a weekly updating frequency, which resulted lag. The lag was defined as the temporal difference between the map
into 52 weekly agent classification maps. In the NRT workflow, each production date (i.e., the weekly update date on our NRT platform) and
pixel was first evaluated for its current number of consecutive anoma- the reference disturbance date interpreted from Planet imagery. For
lies. This procedure generated eight NRT anomaly clusters, corre- each lag interval, we constructed a confusion matrix and calculated
sponding to disturbance stages ranging from one to eight consecutive user's accuracy (UA), producer's accuracy (PA), and, F1 score for each
anomalies. Each cluster was then classified by its corresponding random disturbance agent, thereby forming the lag-accuracy curves for inspec-
forest model into the four categories (logging, wildfire, stress, and non- tion. We then will derive two key lags: the first-alert and level-off lags.
disturbance anomalies), using 16 disturbance features extracted from The first-alert lag, also termed as Mean Time Lag for the First Alert
the current anomaly segment. The results were aggregated into a weekly (Reiche et al., 2018), is defined as the average time between the refer-
NRT disturbance-agent map, based on the spatial locations of the ence disturbance date and the first correct classification by the platform.
detected anomalies. To mitigate false positives, we applied a filtering This metric quantifies the system's responsiveness in issuing its earliest
rule that excluded “stress” pixels with only one consecutive anomaly, as correct alerts, considering only disturbances that were correctly iden-
the weak early-stage signals of stress disturbances are often indistin- tified (Bullock et al., 2022). The level-off lag (Bullock et al., 2022) will
guishable from phenological variability or data noise. In addition, we be employed to evaluate the latency and the model performance when
grouped adjacent pixels with the same disturbance agent labels into the NRT model accuracy plateaus. The level-off lag was determined as
disturbance patches using connected-component labeling and applied a the point of maximum vertical distance (y-value) between the curve and
sieving filter to remove small isolated detections. Specifically, patches a rotated virtual line (45◦around the straight line connecting the curve's
smaller than 0.3 ha (fewer than four 30 m HLS pixels) were removed to endpoints).
reduce salt-and-pepper noise. For the multi-agent assessment, we calculated the overall first-alert
Notably, despite the harmonization efforts in HLS, residual inter- and level-off lags as the weighted means across the three disturbance
sensor effects (e.g., subtle radiometric inconsistencies and occasional agents, using their total mapped area proportions by aggregating 52
sub-pixel misregistration) may still occur and could potentially trigger weekly resultant maps as weights. We reported the snapshot-based
spurious anomaly signals. To reduce these impacts, we applied the HLS confusion matrices and Overall Accuracy (OA) at the two overall lag
quality masks and detected anomalies normalized by multi-band resid- times. Because stratified sampling was employed for the reference data,
ual departures using a chi-square decision rule, which was less sensitive all accuracy metrics were adjusted by the mapped area proportions,
to small sensor-to-sensor biases that tended to manifest as high- following the recommended best practices outlined by Olofsson et al.
9

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Fig. 6. The average accuracy metrics for three disturbance agents at their first-alert and level-off lags across five study sites.
Fig. 7. The lag-accuracy curves for three individual disturbance agents. The first-alert and level-off lags were marked respectively as the light red and dark red
dashed line. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
(2014). We note that our accuracy assessment targets the end-to-end 4. Results
NRT outputs, and therefore the reported commission and omission er-
rors implicitly include uncertainties from both S-CCD anomaly detection 4.1. Individual disturbance assessments
and subsequent agent classification.
For benchmarking, we compared our NRT products with OPERA's Fig. 6shows the variations in the average lags and accuracies over
DIST-ALERT product (Hansen, 2024), which detects globally reductions the five study sites across three disturbance agents. The NRT mapping
in vegetation fraction whenever a new clear observation is acquired. By for wildfire disturbances achieved the shortest first-alert lag (8.2 days)
referencing a historical baseline for the same time of year, DIST-ALERT and the earliest level-off point (12.6 days) among the three agents, along
adjusts for seasonal vegetation dynamics and reduces false alerts. with the highest UA (82.6%, 88.8%), PA (59.2%, 74.5%), and F1 scores
Similar to our platform, DIST-ALERT is based on time-series analysis of (0.669, 0.81). This is likely attributable to the strong low-reflectance
the HLS dataset and is updated approximately weekly; however, it only signal of burn scars shortly after wildfire events, which enables rapid
identifies general disturbances without distinguishing among agents. and accurate detection. Logging disturbances exhibited intermediate
Accordingly, we limited our comparison to binary detection accuracy latency, with the first-alert lag of 11.7 days and the level-off lag of 15.4
and latency (i.e., disturbance vs. no disturbance). We reported the days. Stress disturbances required the longest time to be detected, with a
comparative lags, UA, PA, F1, and the level-off OA under the binary first-alert lag of 18.4 days and a level-off lag of 25.4 days. This longer
scenario (disturbances vs no disturbances), with the latter adjusted by latency can be explained by their more ambiguous spectral feature as
each category's area proportion respectively from the proposed and well as our definition that a stress pixel must show at least two
DIST-ALERT. consecutive anomalies. Stress disturbances also was reported to have the
lowest UA (33.6%, 51.9%), PA (33.1%, 55.4%), and F1 scores (0.305,
0.513) when the two key lags were reached, indicating greater
10

R. Liao et al.                                                                                                                                                                                         R  e  m  o  t e   S  e  n  s i n g    o  f   E  n  v i r o  n  m  e  n  t 342 (2026) 115461
Table 4
Snapshot-based confusion matrices at the overall first-alert lag (12 days).
Reference
| Map | Wildfire | Logging | Stress | Non-disturb. | Total |
| --- | -------- | ------- | ------ | ------------ | ----- |
Confusion matrix, sample counts
| Wildfire         | 691  | 23  | 3   | 65   | 782  |
| ---------------- | ---- | --- | --- | ---- | ---- |
| Logging          | 31   | 305 | 16  | 150  | 502  |
| Stress           | 8    | 9   | 85  | 295  | 397  |
| Non-dist. Forest | 418  | 237 | 318 | 3346 | 4319 |
| Total            | 1148 | 574 | 422 | 3856 | 6000 |
Confusion matrix, area proportion adjusted by mapped area proportion (Table S4)
| Wildfire         | 0.00013                                   | 0.00000 | 0.00000 | 0.00001 | 0.00015 |
| ---------------- | ----------------------------------------- | ------- | ------- | ------- | ------- |
| Logging          | 0.00008                                   | 0.00083 | 0.00004 | 0.00041 | 0.00136 |
| Stress           | 0.00000                                   | 0.00000 | 0.00001 | 0.00004 | 0.00006 |
| Non-dist. Forest | 0.09663                                   | 0.05479 | 0.07351 | 0.77350 | 0.99843 |
| Total            | 0.09685                                   | 0.05562 | 0.07357 | 0.77397 | 1.00000 |
| OA               | 0.00013 +0.00083 +0.00001 +0.77350 =77.5% |         |         |         |         |
Table 5
Snapshot-based confusion matrices at the overall level-off lag (16 days).
Reference
| Map | Wildfire | Logging | Stress | Non-disturb. | Total |
| --- | -------- | ------- | ------ | ------------ | ----- |
Confusion matrix, sample counts
| Wildfire         | 877  | 24  | 2   | 63   | 966  |
| ---------------- | ---- | --- | --- | ---- | ---- |
| Logging          | 32   | 339 | 17  | 174  | 562  |
| Stress           | 7    | 16  | 185 | 234  | 442  |
| Non-dist. Forest | 232  | 195 | 218 | 3385 | 4030 |
| Total            | 1148 | 574 | 422 | 3856 | 6000 |
Confusion matrix, area proportion adjusted by mapped area proportion (see Table S4)
| Wildfire         | 0.00014                                  | 0.00000 | 0.00000 | 0.00001 | 0.00015 |
| ---------------- | ---------------------------------------- | ------- | ------- | ------- | ------- |
| Logging          | 0.00008                                  | 0.00082 | 0.00004 | 0.00042 | 0.00136 |
| Stress           | 0.00000                                  | 0.00000 | 0.00003 | 0.00003 | 0.00006 |
| Non-dist. Forest | 0.05748                                  | 0.04831 | 0.05401 | 0.83863 | 0.99843 |
| Total            | 0.05769                                  | 0.04914 | 0.05408 | 0.83910 | 1.00000 |
| OA               | 0.00014 +0.00082 +0.00003+0.83863 =84.0% |         |         |         |         |
difficulties in distinguishing stress from other noisy factors such as  attributed to its fragmented landscape and humid subtropical climate,
phenological variation. Overall, disturbance agents that were detected  both of which obscure distinct wildfire signals. For logging, the lowest
earlier due to their stronger spectral separability (e.g., wildfire) tended  accuracy occurred in Daxing'anling, likely due to small-scale selective
to achieve higher mapping accuracy than those characterized by subtle  harvesting and strong seasonal variability that complicate disturbance
spectral changes (e.g., stress). identification. For stress, the Yangtze Plain uniquely exhibited an
illustrates the site-specific lag–accuracy curves. Most curves
Fig. 7 inverted-U pattern, where accuracy initially increased but declined with
exhibited an increasing trend with longer lags, as additional post-  longer observation windows, reflecting the rapid recovery of drought-
disturbance observations improved the extraction of trajectory-based  induced spectral anomalies typical of this region. Overall, consistent
features (e.g., slope and skewness) and the accumulation of consecu- with Fig. 6, both wildfire and logging exhibited shorter detection lags
tive anomalies helped suppress short-lived noise caused by phenological  than stress, except in the Yunnan Plateau, where the confirmation lag
fluctuations. The curves generally plateaued at larger lag values, indi- was relatively longer (exceeding 20 days) for both wildfire and logging
| cating that most disturbances had been detected by that stage. Fig. 7also  |     | events. |     |     |     |
| -------------------------------------------------------------------------- | --- | ------- | --- | --- | --- |
reveals pronounced regional differences in the performance of the pro-
posed approach. For wildfire, the Xiangzhong Basin exhibited relatively
lower UA, PA, and F1 score compared with the other four sites, while its  4.2. Overall latency and accuracy
first-alert and level-off lags were of intermediate length. This may be
The mapped area proportions for wildfire, logging, stress, and non-
Fig. 8. The lag-accuracy curves and the accuracy metrics associated with two key lags for the binary maps produced by the proposed and DIST-ALERT for the five
study sites.
11

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Fig. 9. Comparison between the proposed near-real-time (NRT) framework and the DIST-ALERT product across four representative study sites. The larger panels
present the 2024 yearly ensemble maps in which only confirmed disturbance polygons (defined as those with an average number of consecutive anomalies >5) are
retained. The smaller panels display weekly NRT results from the proposed framework for three consecutive weeks following disturbance onset (Weeks 1–3),
alongside the corresponding DIST-ALERT binary disturbance maps and HLS image (NIR-Red-Green composite) for Week 1. (A) Sichuan Basin wildfire (29.8612◦N,
101.5941◦E); (B) Yangtze Plain logging (28.1069◦N, 120.4240◦E); (C) Yunnan Plateau stress disturbance (25.8580◦N, 101.7880◦E); (D) Xiangzhong Basin logging
(26.0371◦N, 113.5437◦E). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
disturbance forest were 0.00015, 0.00136, 0.00006, and 0.99843, consecutive observations, as the correctly labeled “non-disturbance”
respectively, calculated by aggregating the number of pixels assigned to proportion increased from 0.763 to 0.834. It is worth noting that, for
each category across all weekly maps (see Table S4). Using these agent- simplicity, we used a consistent set of mapped area proportions derived
specific mapped area proportions as weights, the overall first-alert and as the average across all weekly maps, although the true area pro-
level-off lags were estimated to be 11.6 days and 15.5 days, respectively. portions might vary with lag. For the site-based accuracy (Table S5 – S9
We further constructed confusion matrices for the two key lags of the supplementary material), OA ranges from 68.5% (DX) to 83.2%
(Tables 4 and 5) and estimated the overall accuracy by weighting agent- (SB) for the first-alert lag, and from 81.5% (YP) to 86.6% (SB) for the
wise accuracy using the mapped area proportions. When the first alert level-off lag, which reflects that the accuracy for the level-off lag was
was correctly triggered, the overall accuracy of the NRT map reached more spatially robust than that for first-alert lag.
77.5%. Once the performance plateau was achieved, the overall accu-
racy increased to 84.0%. This accuracy gain was mainly attributed to the
reduction in commission errors for disturbance with the accumulation of
12

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
4.3. Comparison with DIST-ALERT total. This substantial improvement in efficiency arises from transferring
disturbance agent samples from CONUS to generate a preliminary
Fig. 8compares the lag-accuracy curves of binary disturbance maps disturbance patch map with accurately estimated anomaly dates,
(disturbance vs. no-disturbance) generated by the proposed framework thereby minimizing the need for exhaustive manual delineation and
with those from the DIST-ALERT product. Site-specific lag-accuracy temporal interpretation of historical disturbances. Interpreters were
curves are provided in Fig. S6 of the supplementary material. The pro- only required to record the sample IDs for which they had high confi-
posed approach shows a slightly longer first-alert lag than DIST-ALERT dence in the disturbance agent labels, based on time-series trajectories
(13.8 days vs. 10.1 days) but achieves substantially higher user's accu- and three-year HLS imagery. Consequently, the transferring-guided
racy (UA: 73.9% vs. 57.1%), leading to an improved F₁ score (0.680 vs. strategy combines the temporal and spatial scalability of automated
0.590). For the level-off lag, the proposed framework demonstrates a sample transfer with the accuracy of expert validation, enabling the
shorter lag (17.0 vs. 20.4 days) and consistently higher accuracy met- production of high-quality, representative local samples at a fraction of
rics, including UA (76.1% vs. 68.8%), producer's accuracy (PA: 72.0% the time and cost required by conventional manual annotation.
vs. 65.2%), and F₁ score (0.739 vs. 0.666). It should be noted that the lag The verified patches are subsequently converted into pixel-based
metrics derived from the binary maps differ slightly from the overall lags samples, ensuring sufficient sample numbers, and guaranteeing mini-
reported in Section 4.2, which were calculated as weighted means across mum representation even in regions where certain disturbance types are
the three disturbance agents, reflecting differences in computational relatively rare. Benefiting from random and spatially even sampling
procedures. In addition, using snapshot-based confusion matrices across the region, the verified pixel samples not only provide a pre-
adjusted by category area proportions at 21 lag days (when both liminary estimate of local cross-agent proportions but also support
methods had saturated accuracies, see Table S4 and S10), our approach proportional allocation across disturbance categories, thereby
still achieved a higher adjusted overall accuracy (86.26% vs. 81.74%, improving the representativeness of training datasets and enhancing the
see Table S11 and S12 of the supplementary material). It is noteworthy performance of machine-learning models (Zhu et al., 2016). This design
that DIST-ALERT is an unsupervised system that does not require is particularly advantageous for large-scale monitoring tasks, where
training-sample preparation, which improves operational flexibility but accurate class proportion and spatial distribution are critical for pre-
may partially explain its lower detection accuracy relative to our tile- venting model bias and ensuring robust generalization across different
calibrated, locally verified supervised framework. ecological and geographical contexts.
Fig. 9presents examples comparing the resultant disturbance maps It is noteworthy that manual verification of the preliminary distur-
generated by the proposed framework and the DIST-ALERT product. bance agent maps remains indispensable. We initially attempted to
Overall, both approaches exhibit highly similar spatial patterns during directly apply CONUS-based samples to train disturbance agent classi-
the first week following the disturbance (“W1-proposed” and “W1 DIST- fication models for China. However, the resultant map quality proved
ALERT”), particularly for wildfire and logging due to their pronounced unsatisfactory, even after strategically selecting the most representative
stand-removal signals. However, notable differences emerge for YN CONUS samples based on vegetation and topographic similarity. As
stress (Fig. 9C), where DIST-ALERT missed a considerable number of shown in Table S3 of the supplementary material, the high-confidence
affected pixels. This discrepancy is likely attributable to differences in rates for wildfire and stress categories were both below 10%. This lim-
baseline estimation. Specifically, DIST-ALERT estimates baseline con- itation likely arises from the large uncertainties embedded in post-
ditions using the minimum canopy loss observed within a ± 15-day disturbance spectral trajectories. Variations in forest management re-
temporal window over the preceding three years (Pickens et al., 2025), gimes, dominant vegetation species, and understory conditions between
which may introduce uncertainties associated with phenological China and United States can substantially modify the temporal and
changes. In contrast, the CCDC-like approach compares each observa- spectral patterns following disturbances. Additionally, differences in
tion with its modeled baseline reflectance predicted precisely for the climate regimes, disturbance intensity, and phenological cycles further
same calendar day, thereby minimizing seasonal bias. Additionally, exacerbate the mismatch, leading to reduced model transferability.
DIST-ALERT tends to produce salt-and-pepper disturbance identification These factors are inherently difficult to quantify and harmonize across
that are likely commission errors (see C) YN stress), whereas the pro- regions at large spatial scales, making direct sample transfer insufficient
posed supervised framework integrates non-disturbance anomaly sam- for accurate classification. Consequently, manual verification is a crit-
ples, effectively reducing false detections. ical safeguard to mitigate geographic bias by converting the transferred
priors into locally valid training data, which ultimately improves the
5. Discussion robustness of the final training dataset.
5.1. Transferring-guided local samples 5.2. Latency
High-quality local samples are essential for accurately estimating The lag time for mapping disturbance agents, influenced by both
category proportions and detecting region-specific disturbances. Ideally, algorithmic and logistical factors, critically determines the effectiveness
these samples would be generated entirely from the study regions using of an NRT monitoring system. In this study, we reported two key lag
local HLS time series. However, in regions where comprehensive his- metrics, namely first-alert and level-off lag, to evaluate latency and
torical disturbance products are scarce (e.g., much of China), building a model performance based on accuracy metrics at corresponding lag
representative training archive from scratch would require extensive times. The first-alert lag, representing the average time required to
manual interpretation over large areas and long time periods. A prag- produce a correct disturbance-agent classification, is particularly
matic alternative is to label only a small number of representative important for achieving rapid identification of disturbance type and
events, but this often leads to limited spatial and temporal coverage and extent. Although the NRT scenario was conducted under a weekly up-
can bias the training data toward a few disturbance episodes. To address date scheme, the reported lag times in this study are still underestimated
this limitation, we propose a transferring-guided sample generation by approximately two days in an operational context, due to the actual
strategy that leverages abundant disturbance products available in delay in NASA's preprocessing of Landsat and Sentinel-2 imagery into
CONUS to efficiently and consistently produce tile-specific local training HLS products.
datasets in China. Compared with the existing studies (e.g., Wang et al., In a standard CCDC workflow, monitoring typically relies on con-
2025), which reported an interpretation rate of approximately 18 firming a break and then re-initializing the model for the post-change
disturbance pixel samples per hour, our approach achieves a rate of segment, which can delay NRT alerts because break confirmation and
~850 sample patches per hour, yielding about 30,000 sample pixels in re-initialization require multiple clear post-disturbance observations. In
13

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
contrast, our framework decouples anomaly detection from break performance for anthropogenic disturbances (such as logging) and
confirmation and can issue disturbance alerts and agent attribution as enable expansion of the current disturbance feature set.
soon as the first clear post-disturbance observation is available (i.e., x = A second challenge in transferring to other regions is that locally
1). Break detection is applied conservatively only for persistent struc- dominant disturbance processes (e.g., shifting cultivation, selective
tural changes, preserving temporal continuity and reducing unnecessary logging, or mining) may require redefining the disturbance agent tax-
resets during NRT operation. However, compared with our similar onomy. For example, we currently aggregated timber harvest, con-
approach but for NRT binary disturbance mapping (Ye et al., 2024), the struction, and forest conversion into a single “logging” class because
overall first-alert lag increased from 7.1 to 11.6 days under the same these canopy-removal processes often exhibit similar early-stage spec-
assumption of ignoring data latency. Two factors likely contributed to tral responses in NRT optical observations. This aggregation can facili-
this increase. First, the previous evaluation was event-based (Ye et al., tate transfer to regions where fine-grained ancillary information is
2024), heavily influenced by several large disturbance events (e.g., limited, but it may constrain management-oriented interpretation when
Hurricane Ian and Mosquito Wildfire), whereas the validation in this more detailed attribution is needed. Future work will focus on devel-
study was time-uniformly sampled throughout the year rather than oping a dynamic classification strategy that leverages longer post-
concentrated around major events. Second, the four-class agent classi- disturbance observation windows to refine causal attribution and bet-
fication task addressed here (wildfire, logging, stress, and non- ter differentiate disturbance agents across both similar and contrasting
disturbance) is inherently more complex than the binary disturbance environments.
detection problem, reducing the model's discriminative capacity during
the early phase of disturbance development. For binary detection, our 5.4. Stress disturbances
framework reported a longer first-alert lag than DIST-ALERT, reflecting
a deliberate trade-off between timeliness and commission-error mini- Stress-related disturbances typically produce subtle and spatially
mization achieved by our incorporating non-disturbance anomaly heterogeneous spectral responses, which makes NRT detection inher-
samples. The level-off lag represents the minimum lag time required to ently more challenging than for abrupt stand-replacement events such as
achieve stable and satisfactory performance. The overall level-off lag fire or logging. Nevertheless, even when change magnitudes are small,
(15.5 days) was approximately four days longer than the first-alert lag, stress often exhibits a consistent spectral change direction (e.g., in-
accompanied by a ~ 7% increase in OA. Given the weekly update creases in SWIR2 associated with canopy moisture loss), suggesting that
scheme, these results indicate that our approach can identify most stress signals can still be detectable with a limited number of post-
disturbance agents by the second week following disturbance onset disturbance observations. In our results, the relatively low UA and PA
(first-alert lag) and achieve a satisfactory overall map quality by the for stress (both <60% at the level-off lag; Fig. 7) reflect this intrinsic
third week (level-off lag). These lag times could be further reduced by difficulty and are further compounded by the lack of independent field
increasing the update frequency to daily, which, as reported by Ye et al. datasets that can reliably define a precise onset date for gradual decline
(2024), could shorten the detection lags by approximately five days. processes. However, stress is critically relevant for timely management
Such daily updates are particularly recommended for emergent events, responses (e.g., prioritizing follow-up inspections or initiating suppres-
where timeliness is given the highest operational priority. sion in the case of pest outbreaks), especially given the increasing
Timeliness in an optical NRT monitoring system is also determined disturbance pressure under climate warming (Seidl et al., 2017). We
by the availability of clear observations, because a disturbance can only therefore retained stress in the monitoring scope, but positioned it
be detected after cloud free measurements are acquired. A recent global explicitly as an exploratory component aimed at providing early warn-
evaluation of HLS 2.0 cloud free coverage suggest that the mid latitude ing of canopy condition degradation. Future work will focus on
regions that include much of CONUS and our China study areas have improving robustness for this agent through integration of comple-
broadly comparable clear observation densities (Zhou et al., 2025). This mentary data streams and constraints, such as climate anomalies, tar-
similarity supports the feasibility of transferring disturbance samples geted field samples, and pest reports.
and applying an NRT framework originally developed and evaluated in
CONUS to China (Ye et al., 2024). Nevertheless, seasonal and regional 6. Conclusion
gaps in clear observations can still affect a CCDC-like algorithm by
reducing valid observations available for model updating and by This study presents a novel NRT framework for mapping disturbance
delaying the accumulation of consecutive anomalies. These effects can agents across China's forests using the Harmonized Landsat and
increase uncertainties in early-stage agent attribution and prolong Sentinel-2 (HLS) dataset. By integrating transferring-guided local sam-
detection lag. We note that future integration of complementary sensors, ple generation, stage-based model construction, and anomaly-level
such as Sentinel-1 and GF-2, could further mitigate temporal gaps detection, the proposed approach successfully identified major distur-
attributed to cloud. bance agents, i.e., wildfire, logging, and stress, within an average first-
alert lag of approximately 12 days. The framework effectively over-
5.3. Transferability to other regions comes the long-standing limitation of scarce local training data through
an efficient transferring–guided strategy, which substantially reduced
For regions whose vegetation and topography conditions are well manual labeling efforts while maintaining high sample reliability. The
represented in our CONUS archive, the sample-transfer step is expected stage-based models further enhanced the temporal sensitivity of agent
to be more effective because the transferred samples provide a strong classification, enabling early and accurate identification of disturbances
initialization for generating preliminary disturbance maps and effi- with diverse spectral trajectories. Comparative assessments demon-
ciently guiding local verification. Transferability may be reduced in strated that the approach achieved competitive latency and slightly
environments that differ substantially from CONUS, such as humid better accuracy relative to existing global products while providing
tropical regions, where persistent cloud cover and rapid vegetation re- more actionable insights through disturbance-agent attribution. These
covery can alter spectral–temporal trajectories and weaken agent findings highlight the feasibility of operationalizing fine-scale, NRT
separability in optical data. In such cases, the workflow remains feasible, disturbance-agent monitoring across large regions and underscore the
but it would likely require greater local verification effort and the potential for extending the framework to other forested regions globally.
incorporation of region-specific disturbance information (e.g., fire
products, concession boundaries, or national inventories) to build a CRediT authorship contribution statement
more representative initial sample pool. Moreover, incorporating man-
agement and social-economic datasets could further improve transfer Ronghua Liao: Writing – review & editing, Writing – original draft,
14

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Visualization, Validation, Software, Methodology, Investigation, Formal Hawbaker, T.J., Vanderhoof, M.K., Schmidt, G.L., Beal, Y.-J., Picotte, J.J., Takacs, J.D.,
analysis, Data curation, Conceptualization. Chengcheng Guo: Valida- Falgout, J.T., Dwyer, J.L., 2020. The Landsat burned area algorithm and products for
the conterminous United States. Remote Sens. Environ. 244, 111801.
tion, Data curation. Lingkun Chen: Visualization, Validation, Data Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., 2015. Regional
curation. Yulin Jiang: Validation, Data curation. Yuchen Tao: Visual- detection, characterization, and attribution of annual forest change from 1984 to
ization, Validation, Data curation. Jiani Liao: Data curation. Rui Lu: 2012 using Landsat-derived time-series metrics. Remote Sens. Environ. 170,
121–132.
Validation, Data curation. Huaguo Huang: Visualization, Validation,
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., Campbell, L.B.,
Methodology, Conceptualization. Zhou Shi: Methodology, Conceptu- 2016. Mass data processing of time series Landsat imagery: pixels to data products
alization. Su Ye: Writing – original draft, Visualization, Writing – review for forest monitoring. Int. J. Digit. Earth 9, 1035–1054.
& editing, Supervision, Methodology, Funding acquisition, Hou, G., Shen, X., Ge, S., Zhang, Y., Cao, L., 2025. A novel adaptive similarity-based
ecological niche model for the endangered Yunnan snub-nosed monkey
Conceptualization. (Rhinopithecus bieti) using UAV LiDAR data. Remote Sens. Environ. 326, 114804.
Hu, T., Zhou, G., 2014. Drivers of lightning-and human-caused fire regimes in the great
xing’an mountains. For. Ecol. Manag. 329, 49–58.
Declaration of competing interest Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust.
For. 71, 212–215.
The authors declare that they have no known competing financial Ju, J., Zhou, Q., Freitag, B., Roy, D.P., Zhang, H.K., Sridhar, M., Mandel, J., Arab, S.,
Schmidt, G., Crawford, C.J., Gascon, F., Strobl, P.A., Masek, J.G., Neigh, C.S.R.,
interests or personal relationships that could have appeared to influence 2025. The harmonized Landsat and Sentinel-2 version 2.0 surface reflectance
the work reported in this paper. dataset. Remote Sens. Environ. 324, 114723. https://doi.org/10.1016/j.
rse.2025.114723.
Kennedy, R.E., Yang, Z., Braaten, J., Copass, C., Antonova, N., Jordan, C., Nelson, P.,
Acknowledgements 2015. Attribution of disturbance change agent from Landsat time-series in support of
habitat monitoring in the Puget Sound region, USA. Remote Sens. Environ. 166,
The authors are grateful for the financial support provided by Na-
271–285.
Lin, Q., Huang, H., Chen, L., Wang, J., Huang, K., Liu, Y., 2021. Using the 3D model
tional Key R&D Program of China (2024YFF1306200;
RAPID to invert the shoot dieback ratio of vertically heterogeneous Yunnan pine
2024YFF1306201) and Fundamental and Interdisciplinary Disciplines forests to detect beetle damage. Remote Sens. Environ. 260, 112475.
Breakthrough Plan of the Ministry of Education of China Oddo, P.C., Bolten, J.D., 2019. The value of near real-time earth observations for
improved flood disaster response. Front. Environ. Sci. 7, 127.
(JYB2025XDXM909).
Olofsson, P., Foody, G.M., Herold, M., Stehman, S.V., Woodcock, C.E., Wulder, M.A.,
2014. Good practices for estimating area and assessing accuracy of land change.
Appendix A. Supplementary data Remote Sens. Environ. 148, 42–57.
Olsson, P.-O., Lindstro¨m, J., Eklundh, L., 2016. Near real-time monitoring of insect
induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote
Supplementary data to this article can be found online at https://doi. Sens. Environ. 181, 42–53. https://doi.org/10.1016/j.rse.2016.03.040.
org/10.1016/j.rse.2026.115461. Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect
defoliation using Landsat time series. Forests. https://doi.org/10.3390/f8080275.
Pastick, N.J., Jorgenson, M.T., Goetz, S.J., Jones, B.M., Wylie, B.K., Minsley, B.J.,
Data availability Genet, H., Knight, J.F., Swanson, D.K., Jorgenson, J.C., 2019. Spatiotemporal remote
sensing of ecosystem change and causation across Alaska. Glob. Chang. Biol. 25,
1171–1189.
Data will be made available on request. Perbet, P., Guindon, L., Coˆt´e, J.-F., B´eland, M., 2024. Evaluating deep learning methods
applied to Landsat time series subsequences to detect and classify boreal forest
References disturbances events: the challenge of partial and progressive disturbances. Remote
Sens. Environ. 306, 114107.
Pickens, A.H., Hansen, M.C., Song, Z., Poulson, A., Komarova, A., Baggett, A., Kerr, T.,
Andela, N., Morton, D.C., Schroeder, W., Chen, Y., Brando, P.M., Randerson, J.T., 2022.
Mikus, A., Ortiz Dominguez, C., Tyukavina, A., Lima, A., 2025. Rapid monitoring of
Tracking and classifying Amazon fire events in near real time. Sci. Adv. 8, eabd2713.
global land change. Nat. Commun. 16, 8948. https://doi.org/10.1038/s41467-025-
Baig, M.H.A., Zhang, L., Shuai, T., Tong, Q., 2014. Derivation of a tasselled cap
64014-9.
transformation based on Landsat 8 at-satellite reflectance. Remote Sens. Lett. 5,
423–431. Qiu, S., Zhu, Z., Yang, X., Woodcock, C.E., Fahey, R.T., Stehman, S., Zhang, Y.,
Cullerton, M., Grinstead, A., Hong, F., Song, K., Suh, J.W., Li, T., Ren, W., Nemani, R.
Bullock, E.L., Healey, S.P., Yang, Z., Houborg, R., Gorelick, N., Tang, X., Andrianirina, C.,
R., 2025. A shift from human-directed to undirected wild land disturbances in the
2022. Timeliness in forest change monitoring: a new assessment framework USA. Nat. Geosci. 18, 989–996. https://doi.org/10.1038/s41561-025-01792-3.
demonstrated using Sentinel-1 and a continuous change detection algorithm.
Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving
Remote Sens. Environ. 276, 113043.
near-real time deforestation monitoring in tropical dry forests by combining dense
Cao, P., Zang, Z., Zhang, M., Wang, X., Tang, X., Xiang, J., Tang, S., Wang, J., Zhang, Y.,
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
2025. Using LandTrendr to analyze forest disturbance, recovery, and attribution in 204, 147–161.
Hunan province from 2001 to 2024. Ecol. Indic. 176, 113712.
Reymondin, L., Jarvis, A., Perez-Uribe, A., Touval, J., Argote, K., Rebetez, J., Guevara, E.,
Chen, Xi, Zhao, W., Chen, J., Qu, Y., Wu, D., Chen, Xuehong, 2021. Mapping large-scale
Mulligan, M., 2012. Terra-I: A Methodology for near Real-Time Monitoring of
forest disturbance types with multi-temporal CNN framework. Remote Sens. 13,
Habitat Change at Continental Scales Using Modis-ndvi and trmm. CIAT-Terra-i.
5177. Ryan, K.C., Opperman, T.S., 2013. LANDFIRE–A national vegetation/fuels data base for
Cheng, K., Yang, H., Tao, S., Su, Y., Guan, H., Ren, Y., Hu, T., Li, W., Xu, G., Chen, M.,
2024. Carbon storage through China’s planted forest expansion. Nat. Commun. 15, u 20 se 8 – in 2 1 fu 6 e . ls treatment, restoration, and suppression planning. For. Ecol. Manag. 294,
4106.
Sarre, A., 2020. Global forest resources assessment, 2020: Main report. Food and
Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.-C., Skakun, S.V.,
Agriculture Organization of the United Nations.
Justice, C., 2018. The harmonized Landsat and Sentinel-2 surface reflectance data
set. Remote Sens. Environ. 219, 145–161. Schroeder, T.A., Schleeweis, K.G., Moisen, G.G., Toney, C., Cohen, W.B., Freeman, E.A.,
Yang, Z., Huang, C., 2017. Testing a Landsat-based approach for mapping
Cohen, W.B., Yang, Z., Stehman, S.V., Schroeder, T.A., Bell, D.M., Masek, J.G., Huang, C., disturbance causality in US forests. Remote Sens. Environ. 195, 230–243.
Meigs, G.W., 2016. Forest disturbance across the conterminous United States from
1985–2012: the emerging dominance of forest decline. For. Ecol. Manag. 360, Seidl, R., Schelhaas, M.-J., Rammer, W., Verkerk, P.J., 2014. Increasing forest
242–252. d
80
is
6
tu
–
r
8
b
1
a
0
n
.
ces in Europe and their impact on carbon storage. Nat. Clim. Chang. 4,
Cui, W., Yang, L., Zhang, L., Yang, C., Zhu, C., Zhou, C., 2025. A novel approach of
Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
generating pseudo revisited soil sample data based on environmental similarity for
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
space-time soil organic carbon modelling. Int. J. Appl. Earth Obs. Geoinf. 139, Nat. Clim. Chang. 7, 395–402.
104542.
Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time
Dee, L.E., Miller, S.J., Helmstedt, K.J., Boersma, K.S., Polasky, S., Reich, P.B., 2025. monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data.
Quantifying disturbance effects on ecosystem services in a changing climate. Nat.
Ecol. Evol. 1–12. Remote Sens. Environ. 278, 113073.
Shimizu, K., Ahmed, O.S., Ponce-Hernandez, R., Ota, T., Win, Z.C., Mizoue, N.,
Hansen, M.C., 2024. OPERA Land Surface Disturbance Annual from Harmonized Landsat
Yoshida, S., 2017. Attribution of disturbance agents to forest change using a Landsat
Sentinel-2 Product (Version 1) [Data Set] [WWW Document]. NASA EOSDIS L.
time series in tropical seasonal forests in the Bago Mountains, Myanmar. Forests 8,
Process. Distrib. Act. Arch. Cent. https://doi.org/10.5067/SNWG/OPERA_L3_DIST-
218.
ANN-HLS_V1.001 (accessed 3.12.25).
Silva, C.D.R., Olthoff, A.E., de la Mata, J.A.D., Alonso, A.P., 2013. Remote monitoring of
Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S., forest insect defoliation. A review. For. Syst. 22, 377–391.
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
using Landsat data. Environ. Res. Lett. 11, 34008.
15

R. Liao et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 342 (2026) 115461
Slagter, B., Reiche, J., Marcos, D., Mullissa, A., Lossou, E., Pen˜a-Claros, M., Herold, M., Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
2023. Monitoring direct drivers of small-scale tropical forest disturbance in near Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
real-time with Sentinel-1 and-2 data. Remote Sens. Environ. 295, 113655. dense Landsat time series: case studies of mountain pine beetle and spruce beetle
Stahl, A.T., Andrus, R., Hicke, J.A., Hudak, A.T., Bright, B.C., Meddens, A.J.H., 2023. disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2021.112560.
Automated attribution of forest disturbance types from remote sensing data: a Ye, S., Zhu, Z., Suh, J.W., 2024. Leveraging past information and machine learning to
synthesis. Remote Sens. Environ. 285, 113416. accelerate land disturbance monitoring. Remote Sens. Environ. 305, 114071.
Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time Zhang, Y., Woodcock, C.E., Chen, S., Wang, J.A., Sulla-Menashe, D., Zuo, Z., Olofsson, P.,
monitoring of tropical forest disturbance: new algorithms and assessment Wang, Y., Friedl, M.A., 2022. Mapping causal agents of disturbance in boreal and
framework. Remote Sens. Environ. 224, 202–218. arctic ecosystems of North America using time series of Landsat data. Remote Sens.
Tang, X., Bratley, K.H., Cho, K., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2023. Near Environ. 272, 112935.
real-time monitoring of tropical forest disturbance by fusion of Landsat, Sentinel-2, Zhang, B., Cai, D., Ai, S., Wang, H., Zuo, X., 2023. Research on the influencing factors
and Sentinel-1 data. Remote Sens. Environ. 294, 113626. and prevention measures of long-term forest fire risk in Northeast China. Ecol. Indic.
Thom, D., Seidl, R., 2016. Natural disturbance impacts on ecosystem services and 155, 110965.
biodiversity in temperate and boreal forests. Biol. Rev. 91, 760–781. Zhao, F., Liu, Y., Shu, L., 2020. Change in the fire season pattern from bimodal to
Tyukavina, A., Hansen, M.C., Potapov, P.V., Stehman, S.V., Smith-Rodriguez, K., unimodal under climate change: the case of Daxing’anling in Northeast China. Agric.
Okpa, C., Aguilar, R., 2017. Types and rates of forest disturbance in Brazilian legal For. Meteorol. 291, 108075.
Amazon, 2000–2013. Sci. Adv. 3, e1601047. Zhong, Z., He, B., Chen, Y., Yuan, W., Huang, L., Guo, L., Zhang, Y., Xie, X., 2021. Higher
Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using sensitivity of planted forests’ productivity than natural forests to droughts in China.
satellite image time series. Remote Sens. Environ. 123, 98–108. J. Geophys. Res. Biogeosci. 126, e2021JG006306.
Verleysen, M., François, D., 2005. The curse of dimensionality in data mining and time Zhou, Q., Neigh, C.S.R., Ju, J., Dabney, P., Cook, B., Zhu, Z., Crawford, C.J., Gascon, F.,
series prediction. In: International Work-Conference on Artificial Neural Networks. Strobl, P., Sridhar, M., 2025. Towards seamless global 30-meter terrestrial
Springer, pp. 758–770. monitoring: evaluating 2022 cloud free coverage of harmonized Landsat and
Wang, L., Liu, S., Song, W., Zhang, J., Ding, S., 2025. Global high-resolution forest Sentinel-2 (HLS) V2.0. IEEE Geosci. Remote Sens. Lett. 22, 1–5.
disturbance type dataset. Earth Syst. Sci. Data Discuss. 2025, 1–23. Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
Wheeler, D., Hammer, D., Kraft, R., Steele, A., 2014. Satellite-Based Forest Clearing cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
Detection in the Brazilian Amazon. Zhu, Z., Woodcock, C.E., Holden, C., Yang, Z., 2015. Generating synthetic Landsat
Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W., images based on all available Landsat data: predicting Landsat surface reflectance at
Gao, F., Goward, S.N., Helder, D., Helmer, E., 2008. Free access to Landsat imagery. any given time. Remote Sens. Environ. 162, 67–83.
Science 320, 1011. Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
Wu, Z., He, H.S., Keane, R.E., Zhu, Z., Wang, Y., Shan, Y., 2019. Current and future Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
patterns of forest fire occurrence in China. Int. J. Wildland Fire 29, 104–119. data for operational land cover classification for the LCMAP initiative. ISPRS J.
Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F., Photogramm. Remote Sens. 122, 206–221.
Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the Zhu, A., Lu, G., Liu, J., Qin, C., Zhou, C., 2018. Spatial prediction based on third law of
LCMAP collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14, geography. Ann. GIS 24, 225–240.
143–162. Zhu, A.-X., Miao, Y., Liu, J., Bai, S., Zeng, C., Ma, T., Hong, H., 2019a. A similarity-based
Xu, Q., Zhang, X., Li, J., Ren, J., Ren, L., Luo, Y., 2023. Pine wilt disease in northeast and approach to sampling absence data for landslide susceptibility mapping using data-
Northwest China: a comprehensive risk review. Forests 14, 174. driven methods. Catena 183, 104188.
Yang, J., Huang, X., 2021. 30 m annual land cover and its dynamics in China from 1990 Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2019b.
to 2019. Earth Syst. Sci. Data Discuss. 2021, 1–29. Continuous monitoring of land disturbance based on Landsat time series. Remote
Yang, L., Meng, X., Zhang, X., 2011. SRTM DEM and its application advances. Int. J. Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.
Remote Sens. 32, 3875–3896. Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.
Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring Continuous monitoring of land disturbance based on Landsat time series. Remote
forest disturbance using Landsat time series: stochastic continuous change detection. Sens. Environ. 238, 111116.
Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112167. Zhu, Z., Qiu, S., Ye, S., 2022. Remote sensing of land change: a multifaceted perspective.
Remote Sens. Environ. 282, 113266.
16