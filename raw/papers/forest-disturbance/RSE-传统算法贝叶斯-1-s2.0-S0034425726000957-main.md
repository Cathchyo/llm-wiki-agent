Remote Sensing of Environment 337 (2026) 115325
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
☆
European forest disturbance alerting using Sentinel-1
Sietse van der Woudea,*, Johannes Reichea,*, Johannes Ballinga, Gert-Jan Nabuursb,c,
Frank Sterckb, Anne-Juul Welsinka, Bart Slagtera, Martin Herolda,d
aWageningen University & Research, Laboratory of Geo-information Science and Remote Sensing, Droevendaalsesteeg 3, 6708 PB Wageningen, the Netherlands
bForest Ecology and Forest Management, Wageningen University and Research, Droevendaalsesteeg 3, 6708 PB Wageningen, the Netherlands
cWageningen Environmental Research, Droevendaalsesteeg 3, 6708 PB Wageningen, the Netherlands
dGFZ German Research Centre for Geosciences, Remote Sensing and Geoinformatics Section, Telegrafenberg, 14473 Potsdam, Germany
A R T I C L E I N F O A B S T R A C T
Edited by Marie Weiss We demonstrate a near-real time forest disturbance alerting system for Europe using Sentinel-1 radar data.
Sentinel-1 radar can penetrate clouds and offers high spatial (~20 m) and temporal (3- to 6-day) detail. We
Keywords: directly integrated near-real time ERA5-Land temperature and Copernicus forest type data into the disturbance
Forest detection framework to address freezing temperatures and seasonal phenology, both of which influence the
Disturbance
Sentinel-1 backscatter signal and thus need to be accounted for. This facilitates year-round monitoring across a
Radar
range of environmental conditions (sub-zero, wet and dry) and forest types (coniferous, deciduous) throughout
Europe
the boreal, temperate, and Mediterranean forests of Europe. Validation across Europe showed high accuracy,
Near-real time
Seasonality with a user accuracy of 91.2% (±1.3%) and producer accuracy of 74.5% (±6.0%). User accuracy increased to
99% (±0.4%) when excluding errors in the European-scale forest cover mask primarily caused by local over-
estimation of forest height and density. Disturbances were detected with a median delay of 27 days relative to the
first high-resolution optical Planet reference image, which can further be reduced to 1 day through retrospective
event-based correction of late detection bias. Compared to existing annual optical-based products, our method
improves the detection of small-scale disturbances such as group fellings in Romania. We generated European-
scale estimates of intra-annual disturbance seasonality, capturing variation in forest management practices and
disturbance regimes such as winter harvesting in northern Europe, spring sanitation cutting in central Europe,
and summer wildfires in southern Europe. Overall, this alerting system provides timely and detailed forest
disturbance information in support of sustainable forest management, biodiversity conservation, carbon ac-
counting, and law enforcement efforts across Europe. The alerts are available at https://wurnrt-raddeurope.
projects.earthengine.app/view/radd-europe.
1. Introduction Strategy (European Commission, 2021b) and to reaching the climate
mitigation targets set in the certification framework for carbon removals
Accurate and timely estimates of where and when forest across (European Commission, 2022). These policies have resulted in a
Europe are being disturbed are important for forest management, law growing need for consistent and timely information on the state of the
enforcement, carbon accounting, and biodiversity conservation. Forests forests to balance the multiple demands imposed upon them.
occupy an increasingly central role in achieving sustainable policy goals This need has been fueled by the realization that forests are at risk,
such as those outlined in the 2030 Forest Strategy (European Commis- potentially impeding the realization of European policy goals related to
sion, 2021a). These policies promote wood as a sustainable building climate and nature restoration targets. These risks are linked to slow-
material and as a fuel source for biomass power plants, both of which are moving processes such as climate change-related droughts and excess
expected to increase the harvesting pressure on forests (Bell et al., 2018). nutrient deposition (FOREST EUROPE, 2020), as well as sudden events
Simultaneously, forests are expected to contribute to reaching biodi- leading to a loss of forest cover and biomass. These include forest fires,
versity targets, such as described in the European 2030 Biodiversity windthrows, and pest infestations (Patacca et al., 2023). Studies have
☆ This article is part of a Special issue entitled: ‘Ten years of Sentinel-1 in space (Invitation Only)’ published in Remote Sensing of Environment.
* Corresponding authors.
E-mail addresses: sietse.vanderwoude@wur.nl(S. van der Woude), Johannes.reiche@wur.nl(J. Reiche).
https://doi.org/10.1016/j.rse.2026.115325
Received 16 April 2025; Received in revised form 19 December 2025; Accepted 15 February 2026
Available online 27 February 2026
0034-4257/© 2026 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
estimated that canopy mortality has doubled in European forests be- scales (Reiche et al., 2018a). Signal-based inference alone remains
tween 1984 and 2016 (Senf et al., 2018), while the spatial dispersion of highly uncertain unless external covariates are incorporated, especially
disturbances has become increasingly scattered (Senf and Seidl, 2018). considering increases in weather extremes due to climate change
As a result, traditional sources of information such as the sample-based (Cassou and Cattiaux, 2016; Menzel et al., 2006). Previous efforts have
5- to 10-year ground-based forest inventory data cycles alone can no been made to incorporate climatic data, but these have been limited to
longer meet increasing forest monitoring demands. filtering out observations affected by freezing temperatures (Mullissa
Satellite-based optical and radar remote sensing offers extensive and et al., 2024) and snow cover (Mermoz et al., 2024).
consistent observations and has become key in estimating the extent and In this study, we expand our near-real time Sentinel-1 forest distur-
severity of forest disturbances. Large-scale forest disturbance products bance detection method originally developed for the humid tropics
such as Global Forest Change (Hansen et al., 2013), European Forest (Reiche et al., 2021) to the seasonal boreal, temperate, and Mediterra-
Disturbance Atlas (EFDA) (Viana-Soto and Senf, 2025), and Tree Canopy nean forests of Europe. By directly integrating temperature data from
Height Change (Turubanova et al., 2023) have been developed using 30 ERA5-Land (Mun˜oz-Sabater et al., 2021) and Copernicus forest type
m resolution Landsat data and provide disturbance area estimates for data, we explicitly account for the effect of freezing conditions and
multi-decadal time spans. However, they incur a minimum one-year seasonal shifts in leaf phenology on the Sentinel-1 backscatter signal. We
data delivery lag due to their reliance on cloud-free observations, demonstrate this approach by generating spatially detailed (10 m ×10
limiting their application for rapid response applications such as law m) weekly forest disturbance alerts over a four-year period
enforcement and emergency management after windstorms or fires. (2020–2023). We evaluate their spatial accuracy and timeliness and
In contrast, synthetic aperture radar (SAR) offers year-round obser- compare our results with currently available optically-based European
vations unaffected by cloud cover and illumination conditions. The disturbance products (Hansen et al., 2013; Viana-Soto and Senf, 2025).
Sentinel-1C-band SAR satellite constellation has increased the avail- Furthermore, we analyze seasonal disturbance regimes across Europe to
ability of high-resolution (~20 m) radar data since its launch in 2014, highlight the benefits of intra-annual disturbance detection.
offering revisit intervals of up to 6 days at the equator and up to 3 days at
higher latitudes in Europe, along with open data distribution (European 2. Study area and definitions
Space Agency, 2026). This has enabled the development of operational,
near-real time forest disturbance detection systems in the tropics such as 2.1. Study area
the pan-tropical Radar for Detection of Deforestation (RADD) alerts
(Reiche et al., 2021), TropiSCO (Mermoz et al., 2021) and the Real Time Our study area covered all EU member states except Cyprus and
Deforestation Detection System (DETER-R) (Doblas et al., 2022). These overseas territories, and included the following non-EU countries:
SAR-based systems have proven to be highly complementary to optical Albania, Andorra, Bosnia and Herzegovina, Guernsey, Isle of Man, Jer-
near-real time detection systems (Doblas et al., 2023; Reiche et al., sey, Kosovo, Liechtenstein, Monaco, Montenegro, North Macedonia,
2024). Norway, San Marino, Serbia, Switzerland and United Kingdom. We
Despite successful implementation in the tropics, the use of C-band defined four geographic regions for statistical analysis: North, East,
SAR backscatter data for detecting disturbances in temperate and boreal South, and West Europe (Fig. 1).
zones is limited by its strong sensitivity to freezing conditions (Benninga
et al., 2019; Cohen et al., 2021; Lemmetyinen et al., 2022), and to a 2.2. Definitions
lesser degree, shifts in seasonal leaf phenology (Ahern et al., 1993;
Frison et al., 2018; Rüetschi et al., 2017; Soudani et al., 2021). The We created a forest cover mask for 2019 to restrict disturbance
sensitivity to freezing temperatures is primarily linked to changes in
moisture content: freezing conditions decrease the liquid moisture
content in the canopy, thereby reducing the dielectric constant of the
scatterers. This reduces the interaction with the radar waves, and de-
creases backscatter (Rignot et al., 1994). Other related factors can also
decrease backscatter, such as frost protection mechanisms in needle-leaf
trees (Ahern et al., 1993; Chang et al., 2021), signal penetration to
frozen ground in sparse canopies (Cohen et al., 2024, 2021), and wet
snow cover (Koskinen et al., 2010; Naderpour et al., 2022).
The sensitivity of C-band SAR to shifts in seasonal leaf phenology is
related to changes in structure: In leaf-on conditions, leaves are the
dominant scatterers and mask woody components like twigs and
branches. During transition to leaf-off conditions, these become
increasingly exposed and act as volume scatterers, increasing cross-
polarized backscatter (Ahern et al., 1993; Rüetschi et al., 2017). Sea-
sonal leaf phenology is largely dependent on temperature and varies
annually. High spring temperatures can induce early leaf senescence
(Vitasse et al., 2009a, 2009b), thereby decreasing volume scattering and
reducing backscatter (Frison et al., 2018; Rüetschi et al., 2017; Soudani
et al., 2021).
These factors must be accounted for to avoid confusion between
seasonal variation and actual forest disturbances. Signal-based inference
methods such as harmonic modelling (Shimizu et al., 2019), cumulative
Fig. 1. Forest cover mask for 2019 with subdivision into geographic regions
sum (Ruiz-Ramos et al., 2020), and Kalman filtering (Puhm et al., 2020)
(North, East, South, and West Europe). Maps A-C show three examples of local
have been applied in Sentinel-1-based forest monitoring for this pur-
inaccuracies in the forest cover mask (Google imagery used as basemap): (A)
pose. These methods are limited because they model the seasonal pat- pre-2020 canopy cover removals in Wales (52.577311◦N, (cid:0) 3.656523◦E), (B)
terns in the backscatter timeseries itself, rather than the environmental overestimation of forest height in Northern Italy (45.863691◦ N, 11.278484◦
conditions driving these patterns. They struggle to capture shifts in E), (C) overestimation of forest density in sparse forest in the Romanian Car-
seasonality and stochastic weather fluctuations at daily and weekly time pathians (47.116965◦N, 25.298427◦E).
2

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
detections to undisturbed forest present at the beginning of the moni- Average (Savg) as additional Sentinel-1 features (VVSavg and VHSavg)
toring period in 2020 (Fig. 1). We defined forest as areas of non- besides the VV and VH backscatter (VVBS and VHBS) using a 5-pixel
agricultural and non-urban canopy cover of at least 50% with a mini- window size (Balling et al., 2023; Hall-Beyer, 2017; Haralick et al.,
mum canopy height of 6 m. The forest cover mask for 2019 was derived 1973). Compared to backscatter, GLCM Savg has demonstrated
by (i) intersecting the Copernicus Forest Type and Tree Cover products increased detection sensitivity for fire events and large-scale clearings
for 2018 (Buchhorn et al., 2020) and (ii) excluding areas with canopy with remaining structure such as stumps and slash (Balling et al., 2023;
removals before 2020 and canopy height < 6 m (Turubanova et al., Gibson et al., 2023).
2023). 6 m canopy height was used rather than the more commonly used
5 m due to the lower accuracy of canopy cover extent (overestimation of 3.2. ERA5-Land
canopy height) in the underlying product below 6 m (Turubanova et al.,
2023). We further excluded remaining forest fragments smaller than 0.1 We employed ERA5-Land 2 m modelled surface air temperature data
ha. available in the Google Earth Engine catalog (Gorelick et al., 2017). This
The continental scale of the input datasets (Buchhorn et al., 2020; dataset provides near-real time global coverage (with ~1 week delay) at
Turubanova et al., 2023) occasionally resulted in local inaccuracies. a spatial resolution of ~11 km (Mun˜oz-Sabater et al., 2021). We per-
This included inclusion of areas where forest cover had already been formed two pre-processing steps: (i) we addressed missing temperature
removed prior to 2020 (Fig. 1A), overestimation of forest height data in coastal areas by buffering and extrapolating edge pixels using a 4
(Fig. 1B), and overestimation of forest density (Fig. 1C). Common to ×4-pixel gaussian kernel and (ii) we modified temperatures using the
Landsat-based forest change products, some pre-2020 disturbance Copernicus GLO-30 DEM to account for the general decrease in air
events were not captured by the algorithm used to generate the canopy temperature with elevation. We used lapse rates linearly interpolated
removal data, primarily due to a lack of cloud-free Landsat data at the between 5 ◦C/km on December 31st and 6.5 ◦C/km on June 30th. These
end of 2019 (Verhelst et al., 2021). are consistent with observed seasonal patterns where greater lapse rates
Forest disturbance was defined as removal of at least 50% canopy occur during warmer months (Rolland, 2003).
cover within a 10 ×10 m Sentinel-1 pixel (~0.01 ha), consistent with
definitions of stand-replacing disturbances in other forest disturbance 4. Methods
products (Hansen et al., 2013; Reiche et al., 2021; Senf and Seidl, 2021).
Non-stand-replacing disturbances, such as individual tree breakage, 4.1. European forest disturbance alerting
defoliation or low-intensity thinning were not taken into consideration.
We did not distinguish between disturbance agents, such as harvesting, Our forest disturbance detection methodology is based on an
pests, fires and storms. approach originally developed for the tropics (Reiche et al., 2015b,
2018a, 2021). A new forest disturbance is flagged by comparing new
3. Data Sentinel-1 observations with historical stable forest metrics. Subsequent
images are used to increase confidence, resulting in low- or high-
3.1. Sentinel-1 confidence alerts. We modified this method for European forest condi-
tions by directly integrating Sentinel-1 data with ERA5-Land tempera-
We used dual polarization (VV and VH) Sentinel-1 Ground Range ture data to account for the effects of freezing temperatures and with
Detected (GRD) products acquired in Interferometric Wide (IW) swath Copernicus forest type data (Buchhorn et al., 2020) to address seasonal
mode, as available in the Google Earth Engine catalog (Gorelick et al., variations in leaf phenology (Sections 3.1.1 and 3.1.2). We validated the
2017). Data from both ascending and descending orbits were used. The spatial accuracy and detection timeliness (Sections 3.2.1 and 3.2.2) of
revisit interval of the available data was approximately 3 days with two high-confidence alerts and compared detected disturbance area with
operational satellites (Sentinel-1A and -1B; pre-December 2021), and annual optically-based disturbance products (Section 3.3). Finally, we
approximately 6 days with a single satellite (Sentinel-1A after the failure performed an Europe-wide analysis of disturbance seasonality, for
of Sentinel-1B, post-December 2021). The imagery is multi-looked using which we applied event-based bias correction as additional processing
a 5 ×1 window resulting in a resolution of approximately 20 m ×22 m step retrospectively to improve detection timeliness (Section 3.4).
and is provided at a 10 m pixel spacing to preserve maximum spatial
detail. The pre-processing performed by Google include thermal noise, 4.1.1. Temperature-based forest metrics
GRD border noise correction, radiometric calibration, and range- We calculated pixel-based historical temperature-based metrics to
Doppler terrain correction (Google Developers, 2026). describe the derived distribution of stable forest (F) and non-forest (NF)
We applied additional pre-processing steps to the Sentinel-1 GRD backscatter within temperature intervals for each orbit direction sepa-
imagery. First, we performed radiometric slope correction using the rately. This was performed in five steps. First, for the three year his-
Copernicus GLO-30 Digital Elevation Model (DEM) (Airbus, 2022). torical period from 2017 to 2019, 800 Sentinel-1 images were sampled
Second, we applied supplementary border noise corrections as described per 2◦x 2◦tile (or fewer, depending on availability), resulting in 138 to
in Mullissa et al. (2021) to obtain gamma nought backscatter values, 342 observations per pixel. Second, VVBS and VHBS and VVSavg and
followed by conversion to decibels. Third, we applied incidence angle- VHSavg observations were temporally matched to ERA5-Land tempera-
specific masking to address variations in backscatter values caused by ture data and grouped into three temperature intervals (i1-i3): frozen
overlapping orbit paths. This was done by selecting the relative orbit (<(cid:0) 5 ◦C), transitional ((cid:0) 5 ◦C to 5 ◦C), and non-frozen (>5 ◦C). This
path per pixel and per orbit direction in which the incidence angle per accounts for lower values in the frozen interval and higher values in the
pixel was closest to the average incidence angle (~37.9◦) of an image. non-frozen interval in coniferous forest pixels, and the inverse in de-
This resulted in a decrease in effective revisit interval (6 days with two ciduous forest pixels (Ahern et al., 1993; Rüetschi et al., 2017). The
operational satellites and 12 days with one), but it ensured consistent transitional interval captures the high uncertainty in backscatter
backscatter values and temporal coverage independent of latitude. We response around 0 ◦C, which arises from variations in snow cover dy-
did not apply additional speckle filtering in order to preserve the namics (Cohen et al., 2024, 2021; Lemmetyinen et al., 2022), variations
greatest possible spatial detail in the imagery (Bottani et al., 2024). This in leaf emergence and falling (Vitasse et al., 2009b, 2009a), and un-
offers advantages in the detection of small disturbances and distur- certainty in the modelled temperature data itself (Mun˜oz-Sabater et al.,
bances with irregular or narrow shapes such as roads, but may also 2021). Third, we defined the derived F distribution per temperature
introduce commission errors. interval as a gaussian distribution Ni(x̃ i,2σ i), where x̃ i denotes the
We calculated Grey Level Co-Occurrence Matrix (GLCM) Sum expectation (median) and 2σ i the standard deviation at temperature
3

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
interval i. Fourth, we defined the derived NF distribution as a gaussian well (Appendix A).
distribution Ni(x̃ i-4σ i,2σ i), where we assumed that the x̃ i of the NF dis-
tribution would be 4σ i lower than the x̃ i of F. Although this general 4.1.2. Disturbance detection
assumption was originally made for wet and dry tropical forests (Reiche Our disturbance detection method consisted of five steps (I-V) and
et al., 2018b), we found that this was applicable to European forests as was applied to each newly acquired Sentinel-1 backscatter image
Fig. 2. Flowchart depicting the Sentinel-1-based forest disturbance alerting methodology. The roman numerals correspond to the steps described in Section 3.1.2.
4

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
(Fig. 2). previous iteration's DP as prior P(Dt|PNFt+j-1). PNF values from both
orbit directions were used to update DP, except where doing so would
I. Preprocessing and GLCM calculation have halted iterative updating. In that case, the observation was
ignored. Iterative updating (Eq. (2)) was halted if DP dropped below 0.5
Preprocessing (border noise, incidence angle-specific masking and or when high-confidence alerts were issued.
slope correction; Mullissa et al., 2021) was applied to each dual-
polarized backscatter (BS) image (VVBS and VHBS) followed by the V. Low- and high confidence alerts
calculation of GLCM Savg (VVSavg and VHSavg) features.
Low- and high confidence alerts were issued by applying pre-defined
II. Image normalization thresholds to disturbance probabilities DPBS and DPSavg with spatial and
temporal constraints. An inverse buffer of half the GLCM kernel size (3
Image normalization was performed to mitigate local backscatter pixels) was applied to DPSavg to remove overestimation of patch edges
changes caused by climatic variability and the different responses of (Balling et al., 2023). Low-confidence alerts were issued when DPBS or
forest type and densities (Hamunyela et al., 2016; Reiche et al., 2018a). DPSavg exceeded 0.875 within 180 days. High-confidence alerts were
Precipitation and temperature can vary locally due to factors like issued when the DPBS exceeded 0.975 within a 30 to 180 day window.
elevation differences which are not captured adequately by the low The 30-day minimum confirmation period was introduced in order to
resolution of the ERA5 temperature data. We clustered all backscatter mitigate commissions related to temporary flooding and snowmelt
and GLCM observations within the image using matching temperature events in low-density forest, which can incur sharp changes in the
intervals (frozen, transitional, non-frozen), forest types (deciduous and backscatter signal that endure longer than daily fluctuations induced by
coniferous) and forest densities (high; ≥80% and low; <80%). For each temperature (DeVries et al., 2020; Koskinen et al., 2010). High-
cluster we calculated the mean of the historic medians (Section 3.1.1) confidence alerts were also issued when the DPSavg exceeded 0.975
and the mean of the current values. If the mean of current values at that within a 30 to 180 day window, where at least 10% of the change patch
timestep was lower than the mean of the historic values, we added the overlapped with existing high-confidence (DPBS-derived) alerts of which
difference to each pixel value, resulting in normalized backscatter and the mean date was within 180 days. This was done to reduce commission
GLCM values. error during summer and autumn in deciduous forests of southern
Europe to mitigate opposing geometric effects (shadow, layover) on
III. Probabilistic disturbance detection algorithm backscatter at disturbance patch edges (van der Woude et al., 2024).
High-confidence detection dates were filtered using two subsequent
New forest disturbances were detected using a probabilistic distur- spatial filters: (i) a 3 ×3-pixel modal kernel in order to smooth radar
bance detection algorithm (Reiche et al., 2018b). The normalized speckle-related patterns; and (ii) a 3 × 3-pixel plus-shaped kernel to
backscatter (VVBS and VHBS) and GLCM Savg (VVSavg and VHSavg) ob- smooth patch edges, removing pixels with only one direct neighbor.
servations (collectively denoted as S) were converted separately into Finally, we applied a minimum mapping unit, removing patches smaller
conditional forest and non-forest probabilities p(Si|Fi) and p(Si|NFi) at than 0.1 ha (10 4-connected pixels).
temperature interval i. This was done by extracting the coinciding
observed ERA5 temperature and applying the corresponding 4.1.2.1. Detection example. Fig. 3depicts an example of the disturbance
temperature-specific F and NF probability density functions derived detection methodology in Northern Sweden, where heavy snow cover
from observations in the historic period (Section 3.1.1). Then, condi- and freezing temperatures are commonplace. Drops in backscatter over
tional non-forest probabilities (PNF) were calculated used Bayes stable forest during freezing temperatures are visible, as well as the high
theorem: variance of backscatter in the transitional temperature interval during
PNF=P(NFiSi )= p(SiN p F (S i ) iN + F p i ) (SiFi ) (1) s w re n h s o u i w l l e t m ed i e n l i t n t a h h n e i d g h tr s a P n n N o s w F it i v a o a c n l c u a u e l m s i . n u A t l e f a t r t e i v o r a n s l, e . v I s e n i r n a c p l e o o i b n th s t e e B r v , l o a a t w io c n h b s a a n i c n g k e s w c a h w t i a t c e s h r fl D v a P a g l w g u e a e d s s
Similarly to Reiche et al. (2018b), we employed a block weighting iteratively updated, the 0.975 threshold was exceeded and the change
function (0.05, 0.95) to remove extreme probabilities. The highest non- was identified as a high-confidence alert. Point A was correctly identi-
forest probability was selected for the backscatter (PNFBS) and GLCM fied as non-disturbed, since the backscatter values were more likely
Savg observations (PNFSavg) separately, and potential alerts were flag- within the range of the temperature-specific derived F distributions,
ged when a threshold of 0.6 was exceeded for PNFBS or PNFSavg. rather than the derived NF distributions.
IV. Iterative updating of disturbance probabilities
4.2. Validation
Iterative Bayesian updating (Reiche et al., 2015a) was initiated for
flagged alerts to calculate the disturbance probability (DP) separately 4.2.1. Assessing spatial accuracy
for backscatter (DPBS) and GLCM Savg (DPSavg) using the past (t-1), We validated the European Sentinel-1-based forest disturbance high-
current (t), and future observations (t + j) of non-forest probability confidence alert product for a 4-year period (2020-2023) in a near-real
(PNFBS or PNFSavg): time monitoring scenario through visual inspection using monthly
(cid:0) ) (cid:0) ) composites of very-high-resolution multispectral PlanetScope data
DP=P
(cid:0)
Dt PNFt+j
)
=
P PNFt+jD
(cid:0)
P DtP
)
NFt+j(cid:0)1
(2) (~4.7 m) (Boshuizen et al., 2014). The alerting method was initiated in
P PNFt+j
January 2019, but alerts occurring before 2020 were removed to avoid
Here DP or P(Dt|PNFt+j) denotes the posterior, representing the attributing erroneously unaccounted disturbances in the 2019 forest
probability of disturbance at time t (Dt), given new evidence PNFt+j. P cover mask to early 2020 (Section 2.1, Fig. 1). We continued disturbance
(PNFt+j) represents the total probability of PNF. j indexes the future detection through June 2024 in order to allow low-confidence alerts
observations (j =0, …, n). At the first timestep (j =0), DP P(Dt|PNFt) detected near the end of the validation period (2023) to reach high
was calculated using the PNF at the current step PNFt as new evidence, confidence, but we removed new alerts after 2023.
and PNFt-1 as the prior. Afterwards, DP P(Dt|PNFt+j) was updated at each A probability sampling design was applied (Stehman et al., 2003)
timestep using incoming PNF values (PNFt+j) as new evidence, and the using two stable forest and two forest disturbance strata (Appendix B).
To better capture omission errors, which are more likely to occur near
5

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. 3. Example of the disturbance detection methodology in Northern Sweden. The ERA5-Land temperature values at the time of observation are shown in the top
time series plot. Below this are Sentinel-1 VH backscatter time series in ascending orbit for a non-disturbed pixel (A) and a disturbed pixel (B). The temperature-
specific derived distributions of backscatter for forest (F, solid lines) and non-forest (NF, dotted lines) are depicted on the right and were derived from the obser-
vations in the historical period (in grey). The maps show the last available pre-disturbance optical image (left) and first available post-disturbance optical image
(right) available from Planet Labs.
existing forest disturbances (Olofsson et al., 2020), one stable forest inaccuracies were not regarded as errors in order to avoid penalizing the
stratum was defined within a 200 m buffer surrounding detected dis- alert system, see Appendix Cfor full details.
turbances (F < 200 m), while the second stratum included all areas The accuracy of forest disturbance detection was estimated while
outside of the buffer (F >200 m). Both stable forest strata were derived correcting for unequal inclusion probabilities between strata, reflecting
from all pixels within the 2019 forest cover mask. To avoid bias towards the disproportionate allocation of sample points to strata areas
large disturbance events, the two forest disturbance strata were defined (Stehman et al., 2003). The 2019 forest cover mask and the mapped
by event size: the first included disturbances smaller than 2 ha (D <2 forest disturbances were used to generate the strata samples and
ha), and the second included those larger than 2 ha (D >2 ha). calculate area statistics and inclusion probabilities for each stratum
We calculated potential sample sizes for a range of target standard (Stehman et al., 2003). A weighted confusion matrix was created using
errors (seT =0.10, 0.25, 0.50%), with expected user accuracies (F <200 estimation weights derived from the inclusion probabilities (Appendix
m: 99%, F >200 m: 99%, D <2 ha: 90%, D >2 ha: 90%) using Eq. (13) B), and area-adjusted user accuracy (UA; 100-commission error), pro-
in Olofsson et al. (2020), resulting in sample sizes of 10,922, 1747 and ducer accuracy (PA; 100-omission error) and F1 (2 * (PA * UA) / (PA +
436 respectively. We chose to use 1000 samples (seT = 0.33%), split UA)) were calculated (Stehman, 2014). To avoid penalizing our distur-
equally into 250 samples per stratum similar to previous disturbance bance detection methodology for remaining errors in the forest cover
mapping efforts (Balling et al., 2023; Hansen et al., 2016, 2013; Reiche mask (Fig. 1), we also calculated accuracies separately after excluding
et al., 2021; Turubanova et al., 2023) while taking sampling costs into 45 affected validation samples in the disturbance strata (Table 1).
consideration. Both the sampling and population unit corresponded to a UA, PA and F1 were calculated for entire Europe, as well as sepa-
10 m × 10 m Sentinel-1 pixel. Disturbance patch boundary-related rately for the four defined geographic regions: North, East, South, and
ambiguities related to partial tree cover, radar geometry and location West Europe (Fig. 1). Post-stratification was applied and we recalculated
6

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Table 1 commission and omission bias.
Estimated overall and region-specific user accuracy (UA: 100-comission error)
and producer accuracy (PA: 100-omission error) and F1 scores for all high- 4.4. Analyzing seasonal European disturbance regimes
confidence alerts, with and without the exclusion of forest cover mask errors
[%] (±standard errors [%]). Samples [n] overall and per region. We investigated disturbance seasonality for the 2020–2023 period
All detected disturbances Excluding forest cover mask errors by performing an additional postprocessing step on high-confidence
UA PA F1 n UA PA F1 n alerts to correct for late detection bias, i.e. a systematic shift between
the detected disturbance date and the reference optically-derived date.
Overall 91.2 74.5 82.0 1000 99.1 76.0 86.0 955
Late detection bias is related to remaining canopy structure in the core of
(1.3) (6.0) (0.4) (5.8)
North 94.7 75.9 84.2 407 100 76.8 86.9 393 large disturbance events which reduces contrast between forest and non-
(1.5) (8.3) (0.0) (8.1) forest in the C-band radar signal (Balling et al., 2024, 2023; Mitchell
East 88.0 82.6 85.2 190 97.8 84.1 90.4 179 et al., 2014). During autumn, large fluctuations in temperature and high
(3.3) (14.4) (1.5) (13.4)
precipitation levels lead to high variability in historical forest condi-
South 90.7 51.7 65.9 167 98.6 53.8 69.6 161
(3.4) (14.0) (1.4) (13.9) tions, while in winter, freezing conditions lower overall backscatter.
West 85.7 84.6 85.2 236 98.0 86.3 91.8 222 Disturbance event edges are typically rapidly detected due to radar
(3.3) (13.0) (1.4) (11.8) shadowing effects (Bouvet et al., 2018), which cause a strong drop in
backscatter year-round.
We leveraged this by applying event-based bias correction to adjust
the inclusion probabilities based on the updated area statistics
disturbance dates in the event core using earlier dates at event edges. We
(Appendix B) and sample sizes (Table 1) for each region (Tsendbazar
adapted the method used by Kennedy et al. (2012). First, we defined the
et al., 2021).
bias-corrected detection date as the 5th percentile of all detection dates
within each four-connected cluster. This threshold was chosen instead of
4.2.2. Assessing detection timeliness
the earliest detection date to reduce the influence of false early de-
We assessed the detection timeliness by measuring the delay be-
tections. Second, bias-corrected dates were assigned only to clustered
tween the detection date of high-confidence alert and a reference date,
detections occurring within a 275-day temporal window (~9 months);
visually determined as the first day Planet daily imagery showed
these were considered as discrete events. The underlying assumption is
disturbance with canopy cover loss greater than 50% within the
that spatially connected but temporally separate events occur at rela-
Sentinel-1 pixel area. The disturbance timeliness is therefore relative to
tively fixed times of the year, such as such as large fires during the dry
the earliest available optical image of disturbance, rather than the true
periods or forest management in winter (Sebald et al., 2021; Wohlge-
date. We excluded samples where the time difference between the last
muth et al., 2022). The choice of 9 months rather than one year allows
visible stable forest phase and the first observed disturbance exceeded
for some variation in disturbance seasonality between years. For
31 days (80 samples removed) to minimize large uncertainties in the
example, this prevents directly adjacent clearcuts occurring in January
reference date. The resulting median time between pre- and post-
and December of the same year from both being attributed the bias-
disturbance Planet image pairs was 6.5 days. Only valid disturbance
corrected date of the earliest clearcut. Finally, the process was
samples were included, excluding commission and omission errors as
repeated until no further improvement was found (three times), in
well as errors related to the forest cover mask. We reported the median,
25th and 75th percentile for all remaining samples (n = 370) across which each iteration was applied only to the remaining uncorrected
pixels. We reported the improvement in timeliness compared to the
Europe and within each of the four validation regions (Fig. 1).
timeliness of the near-real time monitoring scenario in Section 4.2.
We also assessed the time required to move from low- to high-
confidence alerts (Reiche et al., 2018b). We reported the median delay
5. Results
and the percentage of alerts moved from low- to high-confidence from
36 days (the 30-day minimum confirmation window plus one observa-
5.1. European forest disturbance alerts
tion) to 90 days after first detection, using the average of the
backscatter-based and GLCM-based values.
We generated weekly European disturbance alerts from 2020 to
2023 (Fig. 4). The product demonstrates the ability to detect a wide
4.3. Comparison with annual optical disturbance products range of spatiotemporally varying disturbances across Europe. Examples
include clearings following bark beetle damage in South Tyrol, Italy (A),
We compared the mapped area of high-confidence disturbance alerts intensive large-scale clearcuts in Rapla, Estonia (B), harvesting (in 2020
with the Global Forest Change (GFC) (Hansen et al., 2013) and European and 2021) followed by a large fire (2022) in Landes, France (C) and
Forest Disturbance Atlas (EFDA) (Viana-Soto and Senf, 2025) products small-scale group fellings in Suceava, Romania (D). The disturbance
for the 4-year 2020–2023 period. This allows for the evaluation of alerts highlight localized areas with high relative disturbance pressure
relative differences in the spatial and temporal trends, but it does not (~7.5% to ~30%), including large fire events in Portugal, Sicily, and
provide an unbiased comparison of the true area of disturbances. Both Greece; bark beetle damage in Germany and Czechia; and harvesting in
GFC and EFDA are Landsat-based and provide annual forest disturbance France, Scotland, Hungary, Serbia, and Romania. In addition, wide areas
estimates for entire Europe with a 30 m pixel size. Hansen et al. (2013) of moderate disturbance pressure (~2.5% to 7.5%), primarily related to
do not use a minimum mapping unit (MMU), while Viana-Soto and Senf forest management practices, were observed in Poland, Ireland, and
(2025) use a three pixel (0.27 ha) MMU. Two comparisons were per- across northern Europe.
formed: First, we resampled the optical products to 10 m pixel spacing Performance was improved compared to the baseline method
and masking them using the same forest cover mask as this study in developed for the tropics (Reiche et al., 2021), demonstrating the
order to mitigate differences in product resolutions and forest cover advantage of integrating temperature and forest type data into the
definitions. Second, we used the native resolution of each product and detection method (Fig. 5). Commission errors were in reduced in
their original forest masks. For both comparisons, we summarized the northern Sweden related to freezing temperatures (A) and in Southern
disturbed area and number of disturbance events using 4-connected Italy related to shifts in seasonal leaf phenology (B). An example is
pixels for very small (≤0.27 ha; 3 Landsat pixels), small (0.27–1 ha), shown in (C) of simultaneous reduction of commission error and
medium (1–5 ha) and large (≥5 ha) disturbance events. The area esti- improvement of detection timeliness in Estonia, where the clearcut areas
mates produced are based on simple pixel counts and not corrected for could be more reliably attributed to late 2020 than early 2021.
7

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. 4. Detected forest disturbances from January 2020 to December 2023, summarized as percentage of disturbed forest area within ~50 km hexagonal grid cells.
Insert maps show disturbance alerts within the 2019 forest cover mask for four regions with distinct disturbance regimes (Google Earth imagery used as basemap):
(A) Bark beetle damage and clearing in South Tyrol, Italy, (B) clearcuts in Rapla, Estonia, (C) mixed harvesting and fire in Landes, France, and (D) small-scale group
fellings in Suceava, Romania.
Fig. 5. Comparison between the baseline method used in the humid tropics (Reiche et al., 2021) and the improved method developed for Europe (this paper). Alert
dates are shown within the 2019 forest cover mask for three example locations (Planet-Labs imagery used as base maps): (A) reduction of commission error in sparse
peatland conifer forest in northern Sweden, (B) in dense deciduous forest in southern Italy, and (C) improvement of detection timeliness in dense conifer forest
in Estonia.
8

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
5.2. Spatial accuracy and timeliness to (cid:0) 9 days). However, some negative detection delays were introduced,
particularly in eastern and western Europe during summer ((cid:0) 27 and (cid:0)
Spatial validation of forest disturbance alerts revealed high overall 11 days, respectively).
accuracies (Table 1). The user accuracy (UA; 100 - commission error) The analysis of the time delay between issuance of low- and high-
was 91.2% (±1.3%), while producer accuracy (PA; 100 – omission confidence alerts revealed that 66% of low-confidence alerts achieved
error) reached 74.5% (±6.0%). The highest UA of 94.7% (±1.5%) was high-confidence within 36 days, 80% within 48 days, and 95% within
found in northern Europe. The PA was similar across all regions (ranging 90 days.
from 75% to 84.6%) with exception of southern Europe, where PA was
low: 51.7% (±14.0%). This lower PA in southern Europe was driven by
just 3 forest samples classified as omission error (Appendix B). In total, 5.3. Comparison with annual optical disturbance products
ten stable forest samples were classified as omission errors, all stemming
from the within-200 m buffer stratum (Appendix B). With forest dis- Our method resulted in a greater detection capability of small dis-
turbances associated with remaining forest cover mask errors excluded, turbances (≤0.27 ha, equaling 3 Landsat pixels), but a lower total
overall UA improved to 99.1% (±0.4%) with consistently high accu- detected disturbed area in the 4-year 2020–2023 period compared to the
racies across all regions, resulting in near-zero commission error across optical-based products within our 2019 forest cover mask. We detected
all regions (ranging from 97.8% to 100%). PA also improved slightly, 332 kha (2.1 M events) in the ≤0.27 ha class compared to 253 kha (1.6
reaching 76.0% (±5.8%) across all regions. M) and 207 kha (1.2 M) for Viana-Soto & Senf and Hansen et al.
The detection timeliness of the disturbance alerts showed an overall respectively (Fig. 7). The same increased capacity to detect small dis-
median detection delay of 27 days (p75 =109; p25 =5) (Fig. 6). The turbances was found using the native resolutions and original forest
shortest median delay occurred in spring (38 to 14 days) and summer masks of the optically-based products (Appendix D.1 and D.2). Fig. 8A
(23 to 10 days), while longer delays were observed during winter (57 to depicts a visual example from Romania, in which the high spatial detail
20 days), particularly in northern Europe. Autumn detections exhibited allowed for the detection of small-scale group felling pattern with a clear
the longest delays and the highest variability (156 to 24 days), especially delineation of disturbance patch borders. However, we found a lower
in northern and western Europe. total disturbed area of 3174 kha compared to 5037 kha in Viana-Soto
Applying event-based bias-correction substantially reduced late and Senf (2025)and 5290 kha in Hansen et al. (2013)(Fig. 7). This was
detection bias. The overall median detection delay across all seasons and primarily driven by missed detections in the large (≥5 ha) disturbance
regions was reduced to 1 day (p75 =17; p25 =(cid:0) 17.5). The greatest class, in which we detected 985 kha compared to 2079 kha and 2461 kha
improvements were observed in winter (9 to (cid:0) 8 days) and autumn (10 for Viana-Soto & Senf and Hansen et al. respectively (Fig. 7), related to
large and low-intensity disturbances such as thinning (Fig. 8B) and fire
Fig. 6. Detection delay (in days) relative to the first visible disturbance in optical (Planet Labs) imagery, shown per geographic region and three-month season.
Delays are reported for both pixel-based (using the near-real time alerting product) and event-based (using bias correction) results. Positive values indicate detection
later than optical imagery, while negative values indicate earlier detection.
9

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. 7. Disturbed area in Kha (top) and disturbance event counts (bottom) by disturbance size class comparison for the 2020–2023 period, comparing results from
this study with two Landsat-based annual disturbance products: Viana-Soto and Senf (2025)and Hansen et al. (2013), masked using the forest cover mask in this
study. The smallest size class (≤0.27 ha) represents disturbances equal to or smaller than three 30 m Landsat pixels, the minimum mapping unit used in Viana-Soto &
Senf. Note the different scales for the left and right plots.
(Fig. 8C). The high spatial detail of the Sentinel-1 system allowed for the
detection of small disturbances and accurate determination of distur-
5.4. Seasonal patterns in European disturbance regimes bance event borders. This methodological framework is scalable and
applicable to operational settings, enabling the provision of near-real
We uncovered large seasonal variation in the timing and spatial time disturbance alerts similar to those currently available for the tro-
distribution of disturbances across Europe on a ~ 50 km hexagonal grid pics (Reiche et al., 2018a). Consistent with previous alerting products
(Fig. 9). Disturbance regimes often showed one or two recurring sea- (Hansen et al., 2016; Reiche et al., 2021), our alerts provide timely
sonal peaks, revealing distinct spring-, winter-, or summer-dominated detection of new forest disturbances without quantifying their exact
patterns. Winter-dominated disturbance regimes were prominent in area, but enable the assessment of relative spatial and temporal trends.
parts of central and eastern Europe, as shown in Fig. 9A, which depicts
harvesting activity in northern Finland with secondary peaks in spring 6.1. Accurate and consistent forest disturbance alerting
and summer. High spring disturbance pressures (>40% of total distur-
bance area for the 4-year 2020–2023 period) were observed across Our radar-based forest disturbance alerting method demonstrated
western Europe, Italy, the British Isles and southern Scandinavia. For high accuracy, characterized by a user accuracy (UA) of 91.2% (±1.3%)
example, Fig. 9B illustrates an early-spring peak associated with forest and a producer accuracy (PA) of 74.5% (±6.0%). When excluding errors
management in southern Belgium. Summer disturbances were most associated with local inaccuracies of the European-scale forest cover
concentrated in Sicily, Greece and the Balkan. Fig. 9D shows an example mask applied here (e.g. overestimation of forest height and density), the
from southern Serbia, where harvesting activity is centered around the UA improved to 99.1% (±1.3%). This highlights the benefits of using
summer months. In contrast, some areas lacked a clear seasonal pattern refined national or local-scale forest cover products tailored to specific
due to irregular disturbance timing. This was evident in regions with low user needs.
forest cover and fire-driven disturbance regimes, such as parts of Spain, The relatively low PA indicates a conservative approach that prior-
Portugal, Italy and Greece. Fig. 9E depicts an extreme case from itizes minimizing commission errors, which is essential for reliable
Portugal, where a single wildfire in summer 2022 accounted for 20% of alerting systems (Reiche et al., 2024, 2021; Woodcock et al., 2020).
the total disturbed area over the entire 4-year period. Areas like alpine Some commission errors persisted, primarily resulting from local inac-
Switzerland (Fig. 9C) exhibited a relatively uniform distribution of curacies in the underlying forest cover mask (Fig. 1). Particularly in
disturbance events, showing no distinct seasonal pattern. areas with sparse or low-canopy forests such as alpine and Mediterra-
nean regions, backscatter variability due to soil moisture and snow cover
6. Discussion fluctuations was more pronounced and difficult to mitigate solely with
temperature adjustments (Pulliainen et al., 1996). Some omission errors
Detecting forest disturbances at high temporal and spatial resolution also remained, especially in the fire-driven disturbance regime of
is important for our understanding of the mixed anthropogenic and Southern Europe (PA =51.7%). Out of three omission errors in Southern
natural disturbance regimes of Europe, as well as for supporting law Europe, two were events larger than 2 ha, suggesting the sensitivity of
enforcement agencies and policymakers (Senf and Seidl, 2021; Wood- the alerting methodology to large, low intensity fires is relatively low. C-
cock et al., 2020). In this study we presented a novel adaptation to a band radar is not only sensitive to structural changes in the canopy (van
Sentinel-1 based tropical forest monitoring method (Reiche et al., 2021), der Woude et al., 2024), but also to post-disturbance moisture fluctua-
which has allowed us to produce the first year-round European radar- tions and remaining structure which have been shown to affect detection
based forest disturbance alerting product. of large disturbances such as fires (Balling et al., 2023, 2021; Bouvet
10

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. 8. Visual comparison at different scales between the forest disturbance product from this study, Viana-Soto and Senf (2025), and Hansen et al. (2013), for (A)
small-scale group felling in Romania, (B) clearcuts and thinning in northern Sweden (Note: thinning — highlighted in white — was omitted in our method because
the Sentinel-1C-band radar signal is not sensitive to low-intensity forest disturbances) and (C) large-scale fire in Portugal. No additional forest cover masking was
applied. The forest cover mask for 2019 is shown in green. A May 2024 Planet Labs composite image is used as a basemap. Note that the scale used for this paper is
continuous, while the annual products are shown with discrete scales. (For interpretation of the references to colour in this figure legend, the reader is referred to the
web version of this article.)
et al., 2018; Gibson et al., 2023). lower omission errors in France, in line with expectations for a locally-
Compared to other radar-based disturbance products, our method parameterized model. However, both removed observations in the
displayed roughly similar spatial accuracies. Mermoz et al. (2024) winter due to freezing temperatures (Mullissa et al., 2024) and/or snow
achieved similarly high UA (99.4%) and PA (80.9%) for clearcuts in cover (Mermoz et al., 2024; Mullissa et al., 2024). This can lead to late or
France, while Mullissa et al. (2024) reported lower accuracies (UA of non-existent winter detections, especially in areas which regularly
78%, PA of 40%) across Europe. A simple analysis of disturbed area experience these conditions. Our methodology addressed these limita-
between Mermoz et al. (2024)and this study in France revealed that our tions by allowing the detections to continue uninterrupted despite sea-
method detected ~26% lower disturbed area within our 2019 forest sonal and daily weather-induced fluctuations.
cover mask (Appendix E). This indicates Mermoz et al. likely exhibits
11

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. 9. Seasonal proportion of disturbed area in a ~ 50 km hexagonal grid. Five selected grid cells (A-E) are highlighted in red on the map and correspond to time
series plots of monthly proportion of disturbed area per cell with a three-month moving window applied. Grey bars in the background indicate the monthly values per
year. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
6.2. Detection timeliness particularly during summer months in Eastern Europe. We found that
this overcorrection was mostly driven by samples located in bark beetle-
We achieved a low overall detection delay of 27 days relative to the affected disturbance patches in Czechia which spanned very large areas,
earliest visible disturbance in Planet imagery, with particularly good and were therefore more prone to being assigned excessively early
performance in spring and summer (Fig. 5). In some cases, negative detection dates in some areas. This suggests further refinement of the
detection delays were found, indicating earlier detection than the first simple event-based timing correction method could reduce early
optical reference image in which a disturbance was visible. This was detection bias in large multi-event disturbance events.
possible because detections can occur in the time period between pre-
and post-disturbance optical image pairs (median of 6.5 days). A greater
6.3. Comparison with annual optical disturbance products
detection delay was found in autumn and winter months in northern and
western Europe, related to remaining structure after disturbance events
The map comparison between our radar-based alerting method and
and climatic effects. In addition, natural disturbances such as bark
annual optical-based disturbance products revealed the greater spatial
beetle, wind, and fire events are known to often result in minimal de-
detail of our product compared to the Global Forest Loss (GFC) and
creases in backscatter (Balling et al., 2021; Hechtl et al., 2025; Tanase
European Forest Disturbance Atlas (EFDA) products, visible in a greater
et al., 2018), or even increased backscatter (Rüetschi et al., 2019). The
detected disturbance area and number of detections for fine-scale (≤
detection timeliness of natural disturbances is therefore likely lower
0.27 ha) disturbances (Fig. 7). This indicates that small forest distur-
than indicated in the overall assessment of timeliness, as these events are
bance events are not well-detected in available Landsat-based moni-
often only fully detected when post-disturbance salvage logging is
toring products (Hansen et al., 2013; Viana-Soto and Senf, 2025). Our
performed.
overall detected area was significantly lower, as the relative disturbance
Analysis of disturbance seasonality benefited from bias-corrected,
area detected in our product decreased with disturbance size compared
event-based assessment to overcome late detections in autumn and
to the optical products (Fig. 7). The large omission in the ≥5 ha class
winter. Applying event-based late detection bias corrections (Kennedy
compared to the optical products (Viana-Soto and Senf, 2024) likely
et al., 2012) significantly reduced the overall median late detection bias
stems from the lower sensitivity of the Sentinel-1C-band backscatter
to 1 day relative to the earliest available optical image. However, this
signal to detect low intensity non-stand replacing forest disturbances
correction introduced minor early detection bias in some cases,
(Balling et al., 2023, 2021; van der Woude et al., 2024).
12

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
While a direct comparison of accuracy figures is challenging due to forest monitoring. The operationalization of Sentinel-1C and Sentinel-
differences in validation strategies, forest masks, and spatial & temporal 1D and the launch of Sentinel Next Generation in 2033 will ensure the
scales, the general pattern is consistent with our findings: our method consistent and rapid availability of data beyond 2030. Special attention
exhibited fewer commission errors and more omission errors than should be given to the varying impacts which different natural distur-
existing annual optical-based forest disturbance products, while bances can have on C-band radar backscatter in order to improve
providing higher spatial and temporal detail. Viana-Soto and Senf detection accuracy and timeliness. Integrating radar-based disturbance
(2025)reported 89.4% UA and 79.5% PA for detected disturbances in detection with optical remote sensing has proven to be highly comple-
the period 2001–2023. Turubanova et al. (2023)reported 81.7% (±1.9) mentary (Doblas et al., 2023; Reiche et al., 2024) and could substantially
UA and 95.0% (±1.9) PA for their tree canopy removal product, and improve the detection accuracy of disturbances and characterization of
59.5% (±4.3) UA and 71.4% (±2.5) PA for the GFC product (Hansen disturbance drivers (Sebald et al., 2021; Viana-Soto and Senf, 2025). L-
et al., 2013) using the same validation samples for the 2001–2021 band radar missions, such as the recently launched NISAR and upcoming
period. The high spatial detail and consistent year-round detection ca- ROSE-L, are expected to provide greater detection capabilities and
pabilities of radar-based monitoring and the sensitivity of optical reduced detection delay by means of their increased sensitivity to
products to large, low-intensity disturbances highlights their structural changes in the forest (Balling et al., 2024). This will mitigate
complementarity. some of the current limitations in the use of C-band radar posed by
seasonal variations, freezing conditions, and post-disturbance remaining
6.4. Seasonality in European disturbance regimes structure (Balling et al., 2024; Cohen et al., 2024, 2021).
Advancements in near-real time weather and climate data integra-
The assessment of seasonality in European disturbance regimes tion such as improved and high-resolution temperature, precipitation,
demonstrated that disturbance regimes vary not only spatially, but also and snow-cover datasets could further reduce commission errors as a
seasonally throughout Europe. The overall patterns found here appear to result of signal variations due to drought, freezing temperatures and
relate largely to the presence and degree of forest management rather snowmelt. This could also reduce omission error and increase detection
than natural disturbances (Sebald et al., 2021; Wohlgemuth et al., timeliness particularly in mountainous and low-density forests (Cohen
2022). The effect of varying forest management styles is strongly visible et al., 2021; Koskinen et al., 2010). This will be especially crucial when
in differences in seasonal patterns along country borders, such as be- expanding this detection methodology beyond the currently used forest
tween Poland and Germany, or between Serbia, North Macedonia and cover mask to lower density forests where the increased ground
Kosovo (Fig. 9). Large scale managed forestry in northern Europe is contribution of the radar signal (Magagi et al., 2002) requires a better
characterized by winter and late spring harvest, since heavy harvesting characterization of moisture-induced fluctuations such as drought and
machinery requires either dry or frozen conditions to avoid causing snow melt. The availability of global near-real time climate data calls for
damage to access roads and forest plots (Lehtonen et al., 2019). Sani- the expansion of this methodology to boreal, temperate and dry forests
tation felling of bark-beetle affected spruce stands often occurs in early outside of Europe.
spring to avoid further spreading (Hl´asny et al., 2019), as we found to be
the case in western and central Europe. Summer fires are known to be 7. Conclusion
common in Greece and the Balkan peninsula, while fires in the interior
of Spain also occur independent of season (Galizia et al., 2021). Remote This study demonstrated a radar-based approach for near-real time
and inaccessible forests like those in alpine Switzerland show relatively monitoring of forest disturbances across Europe by integrating Sentinel-
little variation in seasonality, as they are affected by a wide range of 1 radar data with ERA5-Land temperature and Copernicus forest type
natural disturbances throughout the year (Bebi et al., 2017). Only a 4- datasets. The resulting alerts enhance geographic coverage and tempo-
year period was analyzed, so these patterns were likely driven by ral consistency of forest disturbances compared to existing Europe-wide
large environmental and societal events, such as the 2018–2020 radar-based near-real time products and complement available annual
droughts which led to widespread bark beetle outbreaks in central Landsat-based products. These alerts offer timely forest disturbance in-
Europe (Thonfeld et al., 2022) and the 2019–2023 Covid-19 pandemic formation which can contribute to more effective forest management,
(Hlava´ˇckova´ et al., 2024; Kronholm, 2023). biodiversity conservation, and more accurate carbon accounting, in
particular when combined with expert knowledge on disturbance
6.5. Implications and outlook sources. The high temporal detail of the data allowed for the first year-
round European-scale assessment of intra-annual disturbance season-
The radar-based forest disturbance alerting methodology presented ality. Additionally, combining radar-based systems with existing optical
here expands our ability to monitor European forests by providing alerts products will provide highly complementary insights, further enriching
with enhanced temporal and spatial detail and with a low data delivery the understanding and management of forest disturbance dynamics.
lag compared to annual products. This has implications for forest Future uptake of new L-band radar missions, improved climate data
management and conservation strategies, aligning their efforts closely integration, and integration of monitoring systems represent immense
with objectives outlined in the European 2030 Biodiversity Strategy and opportunities for the enhancement of forest disturbance management.
the 2030 Forest Strategy (European Commission, 2021b, 2021a). The
rapid provisioning of disturbance data, in combination with local expert CRediT authorship contribution statement
knowledge, provides actionable information that can strengthen law
enforcement capabilities in detecting and responding to illegal logging Sietse van der Woude: Writing – review & editing, Writing – orig-
(Thompson and Magrath, 2021), and refine national forest inventories inal draft, Visualization, Validation, Software, Methodology, Investiga-
(Coops et al., 2022). The high temporal detail can enable further studies tion, Formal analysis, Conceptualization. Johannes Reiche: Writing –
into intra-annual dynamics of disturbance events, which are not possible review & editing, Writing – original draft, Validation, Supervision,
with annual-scale monitoring approaches and multi-annual national Methodology, Funding acquisition, Conceptualization. Johannes Ball-
forest inventory cycles (Senf and Seidl, 2018; Wohlgemuth et al., 2022). ing: Writing – review & editing, Writing – original draft, Validation,
In addition, the ability to identify fine-scale patterns in time and space Investigation, Formal analysis. Gert-Jan Nabuurs: Writing – review &
could lead to better classification of disturbance agents and their im- editing, Supervision, Funding acquisition, Conceptualization. Frank
pacts (Belenguer-Plomer et al., 2019; Rüetschi et al., 2019; Slagter et al., Sterck: Writing – review & editing, Supervision, Funding acquisition,
2023). Conceptualization. Anne-Juul Welsink: Writing – review & editing,
There are many opportunities to further improve near-real time Methodology, Conceptualization. Bart Slagter: Writing – review &
13

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
editing, Methodology, Conceptualization. Martin Herold: Writing – interests or personal relationships that could have appeared to influence
review & editing, Supervision, Methodology, Funding acquisition, the work reported in this paper.
Conceptualization.
Acknowledgements
Declaration of generative AI and AI-assisted technologies in the
writing process This research was funded by the Open-Earth-Monitor Cyberinfras-
tructure project (grant agreement No. 101059548), The ForestWard
During the preparation of this work the authors used Open AI's Observatory to Secure Resilience of European Forests (FORWARDS)
ChatGPT in order to aid in the generation of code for simple data sum- project (101084481). Additional support was provided by the Next-
marization and visualization tasks, as well as improving readability, genCarbon project (101184989) and the Monifun project (101134991).
grammar and spelling. After using this tool, the authors reviewed and Modified Copernicus Sentinel data [2017–2024] were accessed and pre-
edited the content as needed and take full responsibility for the content processed on the Google Earth Engine Platform. We thank the Google
of the published article. Earth Engine team for providing cloud-computing resources to perform
this research. We thank the anonymous reviewers for their constructive
Declaration of competing interest feedback and contributions to this study.
The authors declare that they have no known competing financial
Appendix A
14

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Fig. A.1. Time series and Sentinel-1 backscatter distribution examples from two locations (single S1 pixel) in the tropics detected by RADD (Reiche et al., 2021) (A:
Brazil; B: Gabon) and two locations in Europe (C: France; D: Romania) detected as change in this paper. Maps A1-D1 depict stable forest (F) conditions, while maps
A2-D2 depict non-forest (NF) conditions. In A3-D3 time series of VH backscatter for one orbit direction are shown. The vertical red line depicts the date of detection.
A4-D4 show the measured F and NF backscatter distributions in grey, and the derived NF (x̃-4σ, 2σ) in red, which is based on the measured observations during F
conditions. All imagery are Planet Labs monthly composites
In Fig. A.1, we depict several examples from the tropics and Europe of forest disturbances and the corresponding Sentinel-1 backscatter time series.
We did not use the temperature intervals here to maintain comparability. In both the tropics and Europe, the measured NF values do not always reach
the derived NF median (in red). However, due to the probabilistic nature of the detection method, a change can be detected given enough observations
where the NF probability is greater than the F probability.
Appendix B
Table B.1
Overview of strata area proportions (Area [%]), correctly classified samples out of total samples per strata (Correct/Total) for four strata: stable forest within 200 m
buffer around change (F <200 m), stable forest outside 200 m buffer around change (F >200 m), disturbance smaller than 2 ha (D <2 ha) and disturbance larger than
2 ha (D >2 ha). Also shown are commission (Com.) and omission (Om.) errors by region
F <200 m F >200 m D <2 ha D >2 ha Com. Om.
Area [%] 75.96 21.54 1.11 1.39
All regions 49 10
Correct/Total 250/250 240/250 223/250 228/250
(continued on next page)
15

S. van der Woude et al.                                                                                                                                                                          R  e m   o  t e   S  e n  s i n  g    o f   E  n  v  i r o  n m   e  n t   337 (2026) 115325
Table B.1 (continued)
|                 |               | F <200 m  | F >200 m  | D <2 ha  | D >2 ha  |       |     |
| --------------- | ------------- | --------- | --------- | -------- | -------- | ----- | --- |
|                 |               |           |           |          |          | Com.  | Om. |
|                 | Area [%]      | 73.42     | 23.25     | 1.23     | 2.10     |       |     |
| Northern Europe |               |           |           |          |          | 14    | 5   |
|                 | Correct/Total | 88/88     | 90/95     | 94/98    | 116/126  |       |     |
|                 | Area [%]      | 74.59     | 23.13     | 1.13     | 1.15     |       |     |
| Eastern Europe  |               |           |           |          |          | 12    | 1   |
|                 | Correct/Total | 40/40     | 54/55     | 44/53    | 39/42    |       |     |
|                 | Area [%]      | 84.57     | 13.93     | 0.80     | 0.70     |       |     |
| Southern Europe |               |           |           |          |          | 7     | 3   |
|                 | Correct/Total | 65/65     | 30/33     | 36/42    | 26/27    |       |     |
|                 | Area [%]      | 74.39     | 23.37     | 1.16     | 1.08     |       |     |
| Western Europe  | Correct/Total | 57/57     | 66/67     | 49/57    | 47/55    | 16    | 1   |
Table B.2
See Table B.1., but excluding forest cover mask errors from the forest disturbance strata D <2 ha and D >2 ha.
|                 |               | F <200 m | F >200 m | D <2 ha | D >2 ha | Com. | Om. |
| --------------- | ------------- | -------- | -------- | ------- | ------- | ---- | --- |
| All regions     | Area [%]      | 75.96    | 21.54    | 1.11    | 1.39    | 5    | 10  |
|                 | Correct/Total | 250/250  | 240/250  | 222/226 | 228/229 |      |     |
|                 | Area [%]      | 73.42    | 23.25    | 1.23    | 2.10    |      |     |
| Northern Europe |               |          |          |         |         | 0    | 5   |
|                 | Correct/Total | 88/88    | 90/95    | 94/94   | 116/116 |      |     |
|                 | Area [%]      | 74.59    | 23.13    | 1.13    | 1.15    |      |     |
| Eastern Europe  |               |          |          |         |         | 2    | 1   |
|                 | Correct/Total | 40/40    | 54/55    | 43/45   | 39/39   |      |     |
|                 | Area [%]      | 84.57    | 13.93    | 0.80    | 0.70    |      |     |
| Southern Europe |               |          |          |         |         | 1    | 3   |
|                 | Correct/Total | 65/65    | 30/33    | 36/37   | 26/26   |      |     |
|                 | Area [%]      | 74.39    | 23.37    | 1.16    | 1.08    |      |     |
| Western Europe  |               |          |          |         |         | 2    | 1   |
|                 | Correct/Total | 57/57    | 66/67    | 49/50   | 47/48   |      |     |
Appendix C
Fig. C.1. Example of a boundary pixel. The validation sample (in red) is located on the boundary of an alert patch (orange, semi-transparent). There is a clear
disturbance visible in the Planet Imagery related to the alert patch, however it is difficult to unambiguously determine if the canopy at the location of the pixel was
>50% removed
Boundary pixels typically reflect partial tree cover at the edges of larger disturbances, making validation challenging (Hansen et al., 2016),
particularly with high-resolution Sentinel-1 data (Reiche et al., 2021). Besides the side-looking radar geometry, sub-optimal terrain correction in GEE
could further introduce location inaccuracies (Flores-Anderson et al., 2023). Ambiguous pixels located on disturbance boundaries clearly visible in
Planet imagery were labeled as ‘boundary pixels’ (Fig. C.1) rather than false detections (commission errors). In total 70 such cases were found.
Similarly, disturbance events in the Planet imagery clearly related to alert pixels which appeared to be shifted due to side-looking radar geometry or
location inaccuracies (Bouvet et al., 2018; Carstairs et al., 2022; Flores-Anderson et al., 2023), were labeled as ‘edge case’ rather than missed de-
tections (omission errors), of which 3 were found. We did this to avoid penalizing the alert system, of which the main purpose is to detect disturbances
rather than precisely estimate their area (Tang et al., 2019).
16

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Appendix D
Fig. D.1. Disturbed area in Kha (top) and disturbance event counts (bottom) by disturbance size class comparison for the 2020–2023 period, comparing results from
this study with Viana-Soto and Senf (2025)and Hansen et al. (2013)using each product's original forest mask. The smallest size class (≤0.27 ha) represents dis-
turbances equal to or smaller than three 30 m Landsat pixels, the minimum mapping unit used in Viana-Soto & Senf. Note the different scales for the left and
right plots
Fig. D.2. Total area in Kha covered by the forest masks used in this paper, Viana-Soto and Senf (2025), and Hansen et al. (2013). Note: areas of cover loss as detected
by Hansen et al. pre-2020 were removed from the Hansen et al. forest cover mask. This was not done for Viana-Soto & Senf, since it is an estimate of forest land use,
rather than forest cover.
17

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Appendix E
Fig. E.1. Disturbed area for France in Kha for the 2020–2023 period in this paper, Mermoz et al. (2024)masked using our 2019 forest cover mask, and Mermoz et al.
(2024). Our 2019 forest cover mask yielded a 2020 forest area of 13,437 Kha in France, compared to 17,017 Kha in the forest cover mask of Mermoz et al. (2024)
(after removal of pre-2020 detected areas).
Data availability Remote. Sens. Spat. Inf. Sci. XLVIII-3–2024, 43–49. https://doi.org/10.5194/isprs-
archives-XLVIII-3-2024-43-2024.
Bouvet, A., Mermoz, S., Ball`ere, M., Koleck, T., Le Toan, T., 2018. Use of the SAR
Data will be made available on request. shadowing effect for deforestation detection with Sentinel-1 time series. Remote
Sens. 10, 1250. https://doi.org/10.3390/rs10081250.
References Buchhorn, M., Lesiv, M., Tsendbazar, N.E., Herold, M., Bertels, L., Smets, B., 2020.
Copernicus global land cover layers-collection 2. Remote Sens. 12, 1–14. https://doi.
org/10.3390/rs12061044.
Ahern, F.J., Leckie, D.J., Drieman, J.A., 1993. Seasonal changes in relative C-band Carstairs, H., Mitchard, E.T.A., McNicol, I., Aquino, C., Chezeaux, E., Ebanega, M.O.,
backscatter of northern forest cover types. IEEE Trans. Geosci. Remote Sens. 31, Dikongo, A.M., Disney, M., 2022. Sentinel-1 shadows used to quantify canopy loss
668–680. https://doi.org/10.1109/36.225533. from selective logging in Gabon. Remote Sens. 14, 4233. https://doi.org/10.3390/
Airbus, 2022. Copernicus DEM Copernicus Digital Elevation Model Product Handbook. rs14174233.
Balling, J., Verbesselt, J., De Sy, V., Herold, M., Reiche, J., 2021. Exploring archetypes of Cassou, C., Cattiaux, J., 2016. Disruption of the European climate seasonal clock in a
tropical fire-related forest disturbances based on dense optical and radar satellite warming world. Nat. Clim. Chang. 6, 589–594. https://doi.org/10.1038/
data and active fire alerts. Forests 12, 456. https://doi.org/10.3390/f12040456. nclimate2969.
Balling, J., Herold, M., Reiche, J., 2023. How textural features can improve SAR-based Chang, C.Y., Br¨autigam, K., Hüner, N.P.A., Ensminger, I., 2021. Champions of winter
tropical forest disturbance mapping. Int. J. Appl. Earth Obs. Geoinf. 124, 103492. survival: cold acclimation and molecular regulation of cold hardiness in evergreen
https://doi.org/10.1016/j.jag.2023.103492. conifers. New Phytol. 229, 675–691. https://doi.org/10.1111/nph.16904.
Balling, J., Slagter, B., van der Woude, S., Herold, M., Reiche, J., 2024. ALOS-2 PALSAR- Cohen, J., Rautiainen, K., Lemmetyinen, J., Smolander, T., Vehvila¨inen, J., Pulliainen, J.,
2 ScanSAR and Sentinel-1 data for timely tropical forest disturbance mapping: a case 2021. Sentinel-1 based soil freeze/thaw estimation in boreal forest environments.
study for Sumatra, Indonesia. Int. J. Appl. Earth Obs. Geoinf. 132, 103994. https:// Remote Sens. Environ. 254, 112267. https://doi.org/10.1016/j.rse.2020.112267.
doi.org/10.1016/j.jag.2024.103994. Cohen, J., Lemmetyinen, J., Jorge Ruiz, J., Rautiainen, K., Ikonen, J., Kontu, A.,
Bebi, P., Seidl, R., Motta, R., Fuhr, M., Firm, D., Krumm, F., Conedera, M., Ginzler, C., Pulliainen, J., 2024. Detection of soil and canopy freeze/thaw state in the boreal
Wohlgemuth, T., Kulakowski, D., 2017. Changes of forest cover and disturbance region with L and C band synthetic aperture radar. Remote Sens. Environ. 305,
regimes in the mountain forests of the Alps. For. Ecol. Manag. 388, 43–56. https:// 114102. https://doi.org/10.1016/j.rse.2024.114102.
doi.org/10.1016/j.foreco.2016.10.028. Coops, N.C., Tompalski, P., Goodbody, T.R.H., Achim, A., Mulverhill, C., 2022.
Belenguer-Plomer, M.A., Tanase, M.A., Fernandez-Carrillo, A., Chuvieco, E., 2019. Framework for near real-time forest inventory using multi source remote sensing
Burned area detection and mapping using Sentinel-1 backscatter coefficient and data. Forestry. https://doi.org/10.1093/forestry/cpac015 cpac015.
thermal anomalies. Remote Sens. Environ. 233, 111345. https://doi.org/10.1016/j. DeVries, B., Huang, C., Armston, J., Huang, W., Jones, J.W., Lang, M.W., 2020. Rapid
rse.2019.111345. and robust monitoring of flood events using Sentinel-1 and Landsat data on the
Bell, J., Paula, L., Dodd, T., N´emeth, S., Nanou, C., Mega, V., Campos, P., 2018. EU Google earth engine. Remote Sens. Environ. 240, 111664. https://doi.org/10.1016/
ambition to build the world’s leading bioeconomy—uncertain times demand j.rse.2020.111664.
innovative and sustainable solutions. New Biotechnol. 40, 25–30. https://doi.org/ Doblas, J., Reis, M.S., Belluzzo, A.P., Quadros, C.B., Moraes, D.R.V., Almeida, C.A.,
10.1016/j.nbt.2017.06.010. Maurano, L.E.P., Carvalho, A.F.A., Sant’Anna, S.J.S., Shimabukuro, Y.E., 2022.
Benninga, H.-J., van der Velde, R., Su, Z., 2019. Impacts of radiometric uncertainty and DETER-R: an operational near-real time tropical forest disturbance warning system
weather-related surface conditions on soil moisture retrievals with Sentinel-1. based on Sentinel-1 time series analysis. Remote Sens. 14, 3658. https://doi.org/
Remote Sens. 11, 2025. https://doi.org/10.3390/rs11172025. 10.3390/rs14153658.
Boshuizen, C.R., Mason, J., Klupar, P., Spanhake, S., 2014. Results from the planet labs Doblas, J., Lima, L., Mermoz, S., Bouvet, A., Reiche, J., Watanabe, M., Sant Anna, S.,
flock constellation. In: Presented at the 28th Annual AIAA/USU Conference on Small Shimabukuro, Y., 2023. Inter-comparison of optical and SAR-based forest
Satellites. disturbance warning systems in the Amazon shows the potential of combined SAR-
Bottani, M., Ferro-Famil, L., Doblas, J., Mermoz, S., Bouvet, A., Koleck, T., 2024. optical monitoring. Int. J. Remote Sens. 44, 59–77. https://doi.org/10.1080/
Advanced Bayesian method for timely small-scale forest loss detection in the 01431161.2022.2157684.
Brazilian Amazon and Cerrado with Sentinel-1 time-series. Int. Arch. Photogramm. European Commission, 2021a. New EU Forest Strategy for 2030. Brussels.
18

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
European Commission, 2021b. EU Biodiversity Strategy for 2030: Bringing Nature Back Mermoz, S., Bouvet, A., Koleck, T., Ball`ere, M., Le Toan, T., 2021. Continuous detection
into our Lives. Publications Office, LU. of Forest loss in Vietnam, Laos, and Cambodia using Sentinel-1 data. Remote Sens.
European Commission, 2022. Proposal for a Regulation of the European Parliament and 13, 4877. https://doi.org/10.3390/rs13234877.
of the Council Establishing a Union Certification Framework for Carbon Removals. Mermoz, S., Prieto, J.D., Planells, M., Morin, D., Koleck, T., Mouret, F., Bouvet, A., Le
European Space Agency, 2026. Revisit and Coverage [WWW Document]. Sentinel Toan, T., Sheeren, D., Hamrouni, Y., B´elouard, T., Paillassa, E ´ ., Carme, M.,
Online. URL. https://sentinels.copernicus.eu/web/sentinel/user-guides/sentine Chartier, M., Martel, S., F´eret, J.-B., 2024. Submonthly assessment of temperate
l-1-sar/revisit-and-coverage(accessed 2.15.23). forest clear-cuts in mainland France. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens.
Flores-Anderson, A.I., Parache, H.B., Martin-Arias, V., Jim´enez, S.A., Herndon, K., 17, 13743–13764. https://doi.org/10.1109/JSTARS.2024.3429012.
Mehlich, S., Meyer, F.J., Agarwal, S., Ilyushchenko, S., Agarwal, M., Nicolau, A., Mitchell, A.L., Tapley, I., Milne, A.K., Williams, M.L., Zhou, Z.-S., Lehmann, E.,
Markert, A., Saah, D., Cherrington, E., 2023. Evaluating SAR radiometric terrain Caccetta, P., Lowell, K., Held, A., 2014. C- and L-band SAR interoperability: filling
correction products: analysis-ready data for users. Remote Sens. 15, 5110. https:// the gaps in continuous forest cover mapping in Tasmania. Remote Sens. Environ.
doi.org/10.3390/rs15215110. 155, 58–68. https://doi.org/10.1016/j.rse.2014.02.020.
FOREST EUROPE, 2020. State of Europe’s forests 2020. In: Ministerial Conference on the Mullissa, A., Vollrath, A., Odongo-Braun, C., Slagter, B., Balling, J., Gou, Y., Gorelick, N.,
Protection of Forests in Europe. FOREST EUROPE. Reiche, J., 2021. Sentinel-1 SAR backscatter analysis ready data preparation in
Frison, P.-L., Fruneau, B., Kmiha, S., Soudani, K., Dufrˆene, E., Le Toan, T., Koleck, T., Google earth engine. Remote Sens. 13, 1954. https://doi.org/10.3390/rs13101954.
Villard, L., Mougin, E., Rudant, J.-P., 2018. Potential of Sentinel-1 data for Mullissa, A., Saatchi, S., Dalagnol, R., Erickson, T., Provost, N., Osborn, F., Ashary, A.,
monitoring temperate mixed forest phenology. Remote Sens. 10, 2049. https://doi. Moon, V., Melling, D., 2024. LUCA: a Sentinel-1 SAR-based global forest land use
org/10.3390/rs10122049. change alert. Remote Sens. 16, 2151. https://doi.org/10.3390/rs16122151.
Galizia, L.F., Curt, T., Barbero, R., Rodrigues, M., 2021. Understanding fire regimes in Mun˜oz-Sabater, J., Dutra, E., Agustí-Panareda, A., Albergel, C., Arduini, G., Balsamo, G.,
Europe. Int. J. Wildland Fire 31, 56–66. https://doi.org/10.1071/WF21081. Boussetta, S., Choulga, M., Harrigan, S., Hersbach, H., Martens, B., Miralles, D.G.,
Gibson, R.K., Mitchell, A., Chang, H.-C., 2023. Image texture analysis enhances Piles, M., Rodríguez-Fern´andez, N.J., Zsoter, E., Buontempo, C., Th´epaut, J.-N.,
classification of fire extent and severity using sentinel 1 and 2 satellite imagery. 2021. ERA5-land: a state-of-the-art global reanalysis dataset for land applications.
Remote Sens. 15, 3512. https://doi.org/10.3390/rs15143512. Earth Syst. Sci. Data 13, 4349–4383. https://doi.org/10.5194/essd-13-4349-2021.
Google Developers, 2026. Sentinel-1 Algorithms [WWW Document]. Google Earh Naderpour, R., Schwank, M., Houtz, D., Werner, C., Matzler, C., 2022. Wideband
Engine. URL. https://developers.google.com/earth-engine/guides/sentinel1 backscattering from Alpine snow cover: a full-season study. IEEE Trans. Geosci.
(accessed 4.1.24). Remote Sens. 60, 1–15. https://doi.org/10.1109/TGRS.2021.3112772.
Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., Moore, R., 2017. Olofsson, P., Ar´evalo, P., Espejo, A.B., Green, C., Lindquist, E., McRoberts, R.E., Sanz, M.
Google earth engine: planetary-scale geospatial analysis for everyone. Remote Sens. J., 2020. Mitigating the effects of omission errors on area and area change estimates.
Environ. 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031. Remote Sens. Environ. 236, 111492. https://doi.org/10.1016/j.rse.2019.111492.
Hall-Beyer, M., 2017. Practical guidelines for choosing GLCM textures to use in Patacca, M., Lindner, M., Lucas-Borja, M.E., Cordonnier, T., Fidej, G., Gardiner, B.,
landscape classification tasks over a range of moderate spatial scales. Int. J. Remote Hauf, Y., Jasineviˇcius, G., Labonne, S., Linkeviˇcius, E., Mahnken, M., Milanovic, S.,
Sens. 38, 1312–1338. https://doi.org/10.1080/01431161.2016.1278314. Nabuurs, G., Nagel, T.A., Nikinmaa, L., Panyatov, M., Bercak, R., Seidl, R.,
Hamunyela, E., Verbesselt, J., Herold, M., 2016. Using spatial context to improve early Ostrogovi´c Sever, M.Z., Socha, J., Thom, D., Vuletic, D., Zudin, S., Schelhaas, M.,
detection of deforestation from Landsat time series. Remote Sens. Environ. 172, 2023. Significant increase in natural disturbance impacts on European forests since
126–138. https://doi.org/10.1016/j.rse.2015.11.006. 1950. Glob. Chang. Biol. 29, 1359–1376. https://doi.org/10.1111/gcb.16531.
Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., Turubanova, S.A., Tyukavina, A., Puhm, M., Deutscher, J., Hirschmugl, M., Wimmer, A., Schmitt, U., Schardt, M., 2020.
Thau, D., Stehman, S.V., Goetz, S.J., Loveland, T.R., Kommareddy, A., Egorov, A., A near real-time method for forest change detection based on a structural time series
Chini, L., Justice, C.O., Townshend, J.R.G., 2013. High-resolution global maps of model and the Kalman filter. Remote Sens. 12, 3135. https://doi.org/10.3390/
21st-century forest cover change. Science 342, 850–853. https://doi.org/10.1126/ rs12193135.
science.1244693. Pulliainen, J.T., Mikhela, P.J., Hallikainen, M.T., Ikonen, J.-P., 1996. Seasonal dynamics
Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S., of C-band backscatter of boreal forests with applications to biomass and soil
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts moisture estimation. IEEE Trans. Geosci. Remote Sens. 34, 758–770. https://doi.
using Landsat data. Environ. Res. Lett. 11, 034008. https://doi.org/10.1088/1748- org/10.1109/36.499781.
9326/11/3/034008. Reiche, J., De Bruin, S., Hoekman, D., Verbesselt, J., Herold, M., 2015a. A Bayesian
Haralick, R.M., Shanmugam, K., Dinstein, I., 1973. Textural features for image approach to combine Landsat and ALOS PALSAR time series for near real-time
classification. IEEE Trans. Syst. Man Cybern. SMC-3, 610–621. https://doi.org/ deforestation detection. Remote Sens. 7, 4973–4996. https://doi.org/10.3390/
10.1109/TSMC.1973.4309314. rs70504973.
Hechtl, C., Hauser, S., Schmitt, A., Heurich, M., Wendleder, A., 2025. Kennaugh elements Reiche, J., Verbesselt, J., Hoekman, D., Herold, M., 2015b. Fusing Landsat and SAR time
allow early detection of bark beetle infestation in temperate forests using Sentinel-1 series to detect deforestation in the tropics. Remote Sens. Environ. 156, 276–293.
data. Forests 16, 1272. https://doi.org/10.3390/f16081272. https://doi.org/10.1016/j.rse.2014.10.001.
Hla´sny, T., Krokene, P., Liebhold, A., Montagn´e-Huck, C., Müller, J., Qin, H., Raffa, K., Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018a. Improving
Schelhaas, M.-J., Seidl, R., Svoboda, M., Viiri, H., European Forest Institute, 2019. near-real time deforestation monitoring in tropical dry forests by combining dense
Living with Bark Beetles: Impacts, Outlook and Management Options (from Science Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
to Policy), From Science to Policy. European Forest Institute. https://doi.org/ 204, 147–161. https://doi.org/10.1016/j.rse.2017.10.034.
10.36333/fs08. Reiche, J., Verhoeven, R., Verbesselt, J., Hamunyela, E., Wielaard, N., Herold, M., 2018b.
Hlava´ˇckova´, P., Bana´s, J., Utnik-Bana´s, K., 2024. Intervention analysis of COVID-19 Characterizing tropical forest cover loss using dense Sentinel-1 data and active fire
pandemic impact on timber price in selected markets. Forest Policy Econ. 159, alerts. Remote Sens. 10, 777. https://doi.org/10.3390/rs10050777.
103123. https://doi.org/10.1016/j.forpol.2023.103123. Reiche, J., Mullissa, A., Slagter, B., Gou, Y., Tsendbazar, N.E., Odongo-Braun, C.,
Kennedy, R.E., Yang, Z., Cohen, W.B., Pfaff, E., Braaten, J., Nelson, P., 2012. Spatial and Vollrath, A., Weisse, M.J., Stolle, F., Pickens, A., Donchyts, G., Clinton, N.,
temporal patterns of forest disturbance and regrowth within the area of the Gorelick, N., Herold, M., 2021. Forest disturbance alerts for the Congo basin using
northwest forest plan. Remote Sens. Environ. 122, 117–133. https://doi.org/ Sentinel-1. Environ. Res. Lett. 16. https://doi.org/10.1088/1748-9326/abd0a8.
10.1016/j.rse.2011.09.024. Reiche, J., Balling, J., Pickens, A.H., Masolele, R.N., Berger, A., Weisse, M.J.,
Koskinen, J.T., Pulliainen, J.T., Luojus, K.P., Takala, M., 2010. Monitoring of snow-cover Mannarino, D., Gou, Y., Slagter, B., Donchyts, G., Carter, S., 2024. Integrating
properties during the spring melting period in forested areas. IEEE Trans. Geosci. satellite-based forest disturbance alerts improves detection timeliness and
Remote Sens. 48, 50–58. https://doi.org/10.1109/TGRS.2009.2024755. confidence. Environ. Res. Lett. 19, 054011. https://doi.org/10.1088/1748-9326/
Kronholm, T., 2023. Effects of the COVID-19 pandemic on logging contractors in ad2d82.
Sweden: a survey on personnel absenteeism, safety measures and economic impacts. Rignot, E., Way, J.B., McDonald, K., Viereck, L., Williams, C., Adams, P., Payne, C.,
Forests 14, 2173. https://doi.org/10.3390/f14112173. Wood, W., Shi, J., 1994. Monitoring of environmental conditions in taiga forests
Lehtonen, I., Vena¨l¨ainen, A., K¨ama¨r¨ainen, M., Asikainen, A., Laitila, J., Anttila, P., using ERS-1 SAR. Remote Sens. Environ. 49, 145–154. https://doi.org/10.1016/
Peltola, H., 2019. Projected decrease in wintertime bearing capacity on different 0034-4257(94)90051-5.
forest and soil types in Finland under a warming climate. Hydrol. Earth Syst. Sci. 23, Rolland, C., 2003. Spatial and seasonal variations of air temperature lapse rates in Alpine
1611–1631. https://doi.org/10.5194/hess-23-1611-2019. regions. J. Clim. 16, 1032–1046. https://doi.org/10.1175/1520-0442(2003)
Lemmetyinen, J., Ruiz, J.J., Cohen, J., Haapamaa, J., Kontu, A., Pulliainen, J., Praks, J., 016<1032:SASVOA>2.0.CO;2.
2022. Attenuation of radar signal by a boreal forest canopy in winter. IEEE Geosci. Rüetschi, M., Schaepman, M., Small, D., 2017. Using multitemporal Sentinel-1 C-band
Remote Sens. Lett. 19, 1–5. https://doi.org/10.1109/LGRS.2022.3187295. backscatter to monitor phenology and classify deciduous and coniferous forests in
Magagi, R., Bernier, M., Ung, Chhun-Huor, 2002. Quantitative analysis of RADARSAT northern Switzerland. Remote Sens. 10, 55. https://doi.org/10.3390/rs10010055.
SAR data over a sparse forest canopy. IEEE Trans. Geosci. Remote Sens. 40, Rüetschi, M., Small, D., Waser, L.T., 2019. Rapid detection of windthrows using Sentinel-
1301–1313. https://doi.org/10.1109/TGRS.2002.800235. 1 C-band SAR data. Remote Sens. 11, 115. https://doi.org/10.3390/rs11020115.
Menzel, A., Sparks, T.H., Estrella, N., Koch, E., Aasa, A., Ahas, R., Alm-Kübler, K., Ruiz-Ramos, J., Marino, A., Boardman, C., Suarez, J., 2020. Continuous Forest
Bissolli, P., Braslavska´, O., Briede, A., Chmielewski, F.M., Crepinsek, Z., Curnel, Y., monitoring using cumulative sums of Sentinel-1 Timeseries. Remote Sens. 12, 3061.
Dahl, Å., Defila, C., Donnelly, A., Filella, Y., Jatczak, K., Måge, F., Mestre, A., https://doi.org/10.3390/rs12183061.
Nordli, Ø., Pen˜uelas, J., Pirinen, P., Remiˇsova´, V., Scheifinger, H., Striz, M., Sebald, J., Senf, C., Seidl, R., 2021. Human or natural? Landscape context improves the
Susnik, A., Van Vliet, A.J.H., Wielgolaski, F., Zach, S., Zust, A., 2006. European attribution of forest disturbances mapped from Landsat in Central Europe. Remote
phenological response to climate change matches the warming pattern. Glob. Chang. Sens. Environ. 262, 112502. https://doi.org/10.1016/j.rse.2021.112502.
Biol. 12, 1969–1976. https://doi.org/10.1111/j.1365-2486.2006.01193.x.
19

S. van der Woude et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 337 (2026) 115325
Senf, C., Seidl, R., 2018. Natural disturbances are spatially diverse but temporally 2018–2020 drought years. Remote Sens. 14, 562. https://doi.org/10.3390/
synchronized across temperate forest landscapes in Europe. Glob. Chang. Biol. 24, rs14030562.
1201–1211. https://doi.org/10.1111/gcb.13897. Tsendbazar, N., Herold, M., Li, L., Tarko, A., de Bruin, S., Masiliunas, D., Lesiv, M.,
Senf, C., Seidl, R., 2021. Mapping the forest disturbance regimes of Europe. Nat. Fritz, S., Buchhorn, M., Smets, B., Van De Kerchove, R., Duerauer, M., 2021. Towards
Sustainability 4, 63–70. https://doi.org/10.1038/s41893-020-00609-y. operational validation of annual global land cover maps. Remote Sens. Environ. 266,
Senf, C., Pflugmacher, D., Zhiqiang, Y., Sebald, J., Knorn, J., Neumann, M., Hostert, P., 112686. https://doi.org/10.1016/j.rse.2021.112686.
Seidl, R., 2018. Canopy mortality has doubled in Europe’s temperate forests over the Turubanova, S., Potapov, P., Hansen, M.C., Li, X., Tyukavina, A., Pickens, A.H.,
last three decades. Nat. Commun. 9, 4978. https://doi.org/10.1038/s41467-018- Hernandez-Serna, A., Arranz, A.P., Guerra-Hernandez, J., Senf, C., Ha¨me, T.,
07539-6. Valbuena, R., Eklundh, L., Brovkina, O., Navra´tilov´a, B., Novotný, J., Harris, N.,
Shimizu, K., Ota, T., Mizoue, N., 2019. Detecting Forest changes using dense Landsat 8 Stolle, F., 2023. Tree canopy extent and height change in Europe, 2001–2021,
and Sentinel-1 time series data in tropical seasonal forests. Remote Sens. 11, 1899. quantified using Landsat data archive. Remote Sens. Environ. 298, 113797. https://
https://doi.org/10.3390/rs11161899. doi.org/10.1016/j.rse.2023.113797.
Slagter, B., Reiche, J., Marcos, D., Mullissa, A., Lossou, E., Pen˜a-Claros, M., Herold, M., van der Woude, S., Reiche, J., Sterck, F., Nabuurs, G.-J., Vos, M., Herold, M., 2024.
2023. Monitoring direct drivers of small-scale tropical forest disturbance in near Sensitivity of Sentinel-1 backscatter to management-related disturbances in
real-time with Sentinel-1 and -2 data. Remote Sens. Environ. 295, 113655. https:// temperate forests. Remote Sens. 16, 1553. https://doi.org/10.3390/rs16091553.
doi.org/10.1016/j.rse.2023.113655. Verhelst, K., Gou, Y., Herold, M., Reiche, J., 2021. Improving Forest baseline maps in
Soudani, K., Delpierre, N., Berveiller, D., Hmimina, G., Vincent, G., Morfin, A., tropical wetlands using GEDI-based forest height information and Sentinel-1. Forests
Dufrˆene, E ´ ., 2021. Potential of C-band synthetic aperture radar Sentinel-1 time-series 12, 1374. https://doi.org/10.3390/f12101374.
for the monitoring of phenological cycles in a deciduous forest. Int. J. Appl. Earth Viana-Soto, A., Senf, C., 2024. The European Forest Disturbance Atlas: A Forest
Obs. Geoinf. 104, 102505. https://doi.org/10.1016/j.jag.2021.102505. Disturbance Monitoring System Using the Landsat Archive. https://doi.org/
Stehman, S.V., 2014. Estimating area and map accuracy for stratified random sampling 10.5194/essd-2024-361.
when the strata are different from the map classes. Int. J. Remote Sens. 35, Viana-Soto, A., Senf, C., 2025. The European Forest Disturbance Atlas: A Forest
4923–4939. https://doi.org/10.1080/01431161.2014.930207. Disturbance Monitoring System Using the Landsat Archive. https://doi.org/
Stehman, S.V., Sohl, T.L., Loveland, T.R., 2003. Statistical sampling to characterize 10.5194/essd-17-2373-2025.
recent United States land-cover change. Remote Sens. Environ. 86, 517–529. https:// Vitasse, Y., Delzon, S., Dufrˆene, E., Pontailler, J.-Y., Louvet, J.-M., Kremer, A.,
doi.org/10.1016/S0034-4257(03)00129-9. Michalet, R., 2009a. Leaf phenology sensitivity to temperature in European trees: do
Tanase, M.A., Aponte, C., Mermoz, S., Bouvet, A., Le Toan, T., Heurich, M., 2018. within-species populations exhibit similar responses? Agric. For. Meteorol. 149,
Detection of windthrows and insect outbreaks by L-band SAR: a case study in the 735–744. https://doi.org/10.1016/j.agrformet.2008.10.019.
Bavarian Forest National Park. Remote Sens. Environ. 209, 700–711. https://doi. Vitasse, Y., Port´e, A.J., Kremer, A., Michalet, R., Delzon, S., 2009b. Responses of canopy
org/10.1016/j.rse.2018.03.009. duration to temperature changes in four temperate tree species: relative
Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time contributions of spring and autumn leaf phenology. Oecologia 161, 187–198.
monitoring of tropical forest disturbance: new algorithms and assessment https://doi.org/10.1007/s00442-009-1363-4.
framework. Remote Sens. Environ. 224, 202–218. https://doi.org/10.1016/j. Wohlgemuth, T., Jentsch, A., Seidl, R., 2022. Disturbance Ecology, Landscape Series.
rse.2019.02.003. Springer International Publishing, Cham. https://doi.org/10.1007/978-3-030-
Thompson, S.T., Magrath, W.B., 2021. Preventing illegal logging. Forest Policy Econ. 98756-5.
128, 102479. https://doi.org/10.1016/j.forpol.2021.102479. Woodcock, C.E., Loveland, T.R., Herold, M., Bauer, M.E., 2020. Transitioning from
Thonfeld, F., Gessner, U., Holzwarth, S., Kriese, J., da Ponte, E., Huth, J., Kuenzer, C., change detection to monitoring with remote sensing: a paradigm shift. Remote Sens.
2022. A first assessment of canopy cover loss in Germany’s forests after the Environ. 238, 111558. https://doi.org/10.1016/j.rse.2019.111558.
20