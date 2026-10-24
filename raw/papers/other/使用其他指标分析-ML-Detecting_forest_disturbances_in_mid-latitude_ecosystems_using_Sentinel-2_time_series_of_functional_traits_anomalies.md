Detecting forest disturbances in mid-latitude
ecosystems using Sentinel-2 time series of
functional traits anomalies
1st Erika Piaser 2nd Cinzia Panigada 3rd Beatrice Savinelli
Dep. of Earth and Environm. Sciences Dep. of Earth and Environm. Sciences Dep. of Earth and Environm. Sciences
University of Milano-Bicocca University of Milano-Bicocca University of Milano-Bicocca
Milano, Italy Milano, Italy Milano, Italy
erika.piaser1@unimib.it cinzia.panigada@unimib.it b.savinelli@campus.unimib.it
4th Giulia Tagliabue 5th Luigi Vignali 6th Fabian Ewald Fassnacht
Dep. of Earth and Environm. Sciences Dep. of Earth and Environm. Sciences Inst. of Remote Sens. and Geoinf.
University of Milano-Bicocca University of Milano-Bicocca Freie Universita¨t Berlin
Milano, Italy Milano, Italy Berlin, Germany
giulia.tagliabue@unimib.it luigi.vignali@unimib.it fabian.fassnacht@fu-berlin.de
7th Micol Rossini
Dep. of Earth and Environm. Sciences
University of Milano-Bicocca
Milano, Italy
micol.rossini@unimib.it
Abstract—Forest are facing increasing stress from climate- disturbancemapping,droughtandtreefall,multispectralsatellite
induced droughts and extreme weather events, threatening imagery
ecosystem function and resilience. Timely detection of these
disturbances is crucial for effective forest management. Remote I. INTRODUCTION
sensing offers scalable monitoring of forest condition and dy-
Covering nearly one-third of the Earth’s surface, forests
namics across large areas with consistent spatial and temporal
resolution. While most forest disturbance mapping approaches deliver key ecosystem services such as climate regulation,
rely on indirect proxies like vegetation indices, this study ex- biodiversityconservation,carbonsequestrationandsupportfor
plores the potential of Sentinel-2 derived plant traits, Canopy livelihoods through timber and food production [1]. However,
Chlorophyll Content (CCC) and Leaf Area Index (LAI), which
they are increasingly exposed to a range of disturbances
offermoredirectlinkstovegetationfunctionandstructure.Two
including droughts, storms, late frost, fires, and disease out-
documented disturbance types were analyzed: the 2022 summer
drought and 2023 windthrow. A rolling regression slope analysis breaks, which can significantly alter their structure, function
wasappliedtocumulativeanomaliesoffunctionaltraitstoassess andlong-termstability[2].Withtheintensificationofextreme
the timing, intensity, and persistence of the disturbances across climatic events, understanding their impacts on forest dynam-
ground-validated plots. Results show droughts generate isolated
ics has become critical for developing adaptive management
anomaly peaks during the event, with a stronger impact on leaf
strategies. In this context, remote sensing technologies play a
pigmentation(averagereductioninCCCof-41.53%vs.-31.93%
in LAI). In contrast, treefall produces a comparable reductions pivotalrolebyenablingcontinuousandlarge-scalemonitoring
in both traits (exceeding 30.00%), indicating both functional offorestconditionovertime[3].Overtheyears,multispectral
and structural canopy loss. In the year following the event, a sensors such as Landsat, MODIS and Sentinel-2 have been
prolonged plateau of anomalies is observed, with partial mid-
widely used to monitor forest structure, function, vitality and
seasonattenuationlinkedtounderstorydynamics.Thesefindings
loss dynamics [4]. Nevertheless, several challenges persist in
highlight the potential of the proposed approach to effectively
supportlong-termforestmonitoringandconservationstrategies. the detection and interpretation of forest disturbances. These
include the lack of high-quality reference data for validation,
IndexTerms—Plantfunctionaltraits,anomalydetection,forest the overlapping effects of multiple stressors in complex forest
environments, and the limited transferability of models across
This work was supported by the EO4Resilience project, funded by the different ecological zones and forest types [5]- [6]. Most
EuropeanSpaceAgencyundertheSentinelUsersPreparation(SUP)initiative
approaches for mapping forest disturbances rely on time
-[SUP-1]-ApplicationsPreparednesswithstakeholderandend-userspartic-
ipation,ContractNo.4000146103/24/I-DT-bgh. series of indirect proxies, employing temporal segmentation
173
979-8-3315-5486-6/25/$31.00 ©2025 IEEE
77421511.5202.32966roFirgAorteM/9011.01
:IOD
|
EEEI
5202©
00.13$/52/6-6845-5133-8-979
|
)roFirgAorteM(
yrtseroF
dna
erutlucirgA
rof
ygolorteM
no
pohskroW
lanoitanretnI
EEEI
5202
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore. Restrictions apply.

or multi-year deviations from expected phenological trends stress. In contrast, hygrophilic species like black alder, chest-
[5]- [7]- [8]. These methods often d epend on subjective nut, meso-hygrophylic oak associated with white hornbeam
thresholds, require identifying undisturbed baseline periods, showed minimal changes, suggesting higher resilience. In
andfrequentlyuseasingleannualobservationsorbi-temporal addition, during the summer 2023 severe convective storms,
differencing. Furthermore, most existing studies rely on time notably on July 23-27 and August 26, hit the region leading
series of vegetation indices or specific spectral bands [9]. to localized windthrow events. According to the regional
Although widely used, they often suffer from saturation in environmental protection agency ARPA Lombardia, extreme
densecanopies,sensitivity toatmosphericconditions,viewing weather events were characterized by wind gusts exceeding
geometry,andlimitedphysiologicalinterpretation.Incontrast, 100 km/h, contributing to blowdowns and treefalls throughout
| biophysical | canopy | traits | such  | as canopy     | chlorophyll |            | content | the park | [14]. |     |     |     |     |     |     |
| ----------- | ------ | ------ | ----- | ------------- | ----------- | ---------- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| (CCC) and   | Leaf   | Area   | Index | (LAI) provide | direct      | indicators |         |          |       |     |     |     |     |     |     |
of changes in vegetation structure and function, as they are B. Disturbance reference data
| closely | linked | to photosynthetic |     | activity, | and | overall | plant |           |       |      |             |     |        |            |      |
| ------- | ------ | ----------------- | --- | --------- | --- | ------- | ----- | --------- | ----- | ---- | ----------- | --- | ------ | ---------- | ---- |
|         |        |                   |     |           |     |         |       | Reference | data, | used | to validate | the | method | for forest | dis- |
health.Thismakesthemparticularlywell-suitedforcharacter-
turbanceassessment,werecollectedduringafieldcampaignin
izingstress-inducedresponses[10].Buildingonthisrationale,
summer2022fromhomogeneousforesttypeplots(30x30m),
| our analysis | serves | as  | an initial | step | towards | the | broader |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | ---------- | ---- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
followingprotocolsdescribedby[10]forplantdominanceand
| goals of          | the EO4Resilience |             | project, | funded       | by    | the European |     |             |                  |           |               |           |            |              |     |
| ----------------- | ----------------- | ----------- | -------- | ------------ | ----- | ------------ | --- | ----------- | ---------------- | --------- | ------------- | --------- | ---------- | ------------ | --- |
|                   |                   |             |          |              |       |              |     | species     | composition.     |           | Starting from | the       | location   | of reference |     |
| Space Agency      |                   | (ESA) under |          | the Sentinel | Users | Preparation  |     |             |                  |           |               |           |            |              |     |
|                   |                   |             |          |              |       |              |     | data, 2022  | drought-affected |           | areas         | were      | identified | according    |     |
| (SUP) initiative. |                   | The project | aims     | to advance   |       | development  | of  |             |                  |           |               |           |            |              |     |
|                   |                   |             |          |              |       |              |     | to observed | high             | anomalies | in            | validated | vegetation | traits       | in  |
innovativeEO-basedapproachesforassessingforestresilience
|                    |     |              |        |         |             |              |        | relation      | to meteorological |            | data | [10], while | zones  | impacted | by      |
| ------------------ | --- | ------------ | ------ | ------- | ----------- | ------------ | ------ | ------------- | ----------------- | ---------- | ---- | ----------- | ------ | -------- | ------- |
| to climate-induced |     | disturbances |        | such    | as drought, | with         | a par- |               |                   |            |      |             |        |          |         |
|                    |     |              |        |         |             |              |        | 2023 treefall | were              | determined |      | through     | direct | on-site  | inspec- |
| ticular emphasis   |     | on linking   | remote | sensing |             | observations |        | to            |                   |            |      |             |        |          |         |
tionscarriedoutbythepark’secologistsandbotanicalexperts,
| key functional |     | canopy | traits. | Within | this wider | context, | this |              |     |             |     |         |          |              |     |
| -------------- | --- | ------ | ------- | ------ | ---------- | -------- | ---- | ------------ | --- | ----------- | --- | ------- | -------- | ------------ | --- |
|                |     |        |         |        |            |          |      | who recorded |     | photographs | and | visible | evidence | of windthrow |     |
studyexploitsSentinel-2timeseriesofCCCandLAItraitsto
damage.
| provide    | an operational | case        | study  | on how      | biophysical |          | canopy |                 |     |           |     |            |        |     |     |
| ---------- | -------------- | ----------- | ------ | ----------- | ----------- | -------- | ------ | --------------- | --- | --------- | --- | ---------- | ------ | --- | --- |
| indicators | can be         | used detect | forest | disturbance |             | dynamics | and    |                 |     |           |     |            |        |     |     |
|            |                |             |        |             |             |          |        | C. Standardized |     | anomalies | of  | functional | traits |     |     |
evaluateposteventrecovery,basedondocumented2022-2023
stress events. Specifically, the objectives are to i) detect and Following the methodology presented in [10], the detection
distinguish drought- and treefall-induced disturbances, and ii) of forest traits anomalies was carried out from a total of 230
assessing post-disturbance recovery patterns to evaluate forest cloud-free Sentinel-2 multispectral images collected between
resilience associated with different stress types. 2017 and 2024. Functional vegetation traits of CCC and
|     |     |     |     |     |     |     |     | LAI were | extracted | using | the | biophysical |     | processor | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | --- | ----------- | --- | --------- | ------ |
II. MATERIALSANDMETHODS
|     |     |     |     |     |     |     |     | S2 toolbox | [15] | integrated | within | the | Sentinel | Application |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | ------ | --- | -------- | ----------- | --- |
A. Study area Platform (SNAP) software. This processor employs a hybrid
The study was conducted in the Ticino Regional Park retrievalalgorithmcombiningartificialneuralnetworks(ANN)
(45.4286 N, 8.8342 E), one of the largest remaining natural and radiative transfer models (PROSPECT for leaf-level and
|     | ◦   | ◦   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mixed temperate forests in the Po valley, northern Italy. Cov- SAIL for canopy simulations) to estimate trait values from
ering more than 900 km2, the park hosts fluvial ecosystems, reflectance data [15] - [16]. The processor has demonstrated
riparian woodlands and rare remnants of the primary plain strong agreement with reference data in the study area with
forest that once dominated the region [11]. The ecological CCCandLAIestimationsachievingnRMSEvaluesof13.56%
diversity makes the area a key reservoir of diverse habitat and 11.49%, respectively [10]. Raw time series of CCC and
and plant species [11] - [12]. The northern part is primarily LAI were extracted in 63 sampling plots from forest traits
composed of mesophylic mixed oak-hornbeam association, maps, and smoothed with a Savitzky-Golay filter [17] to
withQuercusroburandCarpinusbetulusasdominantspecies, reduce noise and low-quality observations. Then, a winter
sweet chestnut (Castanea sativa) and conifer species (Pinus baselineadjustmentwasappliedbyreplacingvaluesfromDay
silvestris and P. rigida). The southern part is commonly of Year (DOY) 335 to 56 with the 5th percentile of the entire
populated by poplar (Populus spp.) and black alder (Alnus smoothedtimeseries,tominimizenoisefromsnow,cloudand
glutinosa). In recent years, northern Italy was identified as a standardize seasonal dormancy. Finally, 5-days interpolation
hotspot of one of the most severe droughts across southern wasperformedusingasplinefunctiontoensurecontinuityand
Europe, which occurred in 2022 [13]. Hence, the Ticino produceregularlyspacedtimeseries.Anomaliesinforesttraits
RegionalParkexperiencedelevatedforeststressandmortality, were then identified using the Standardized Anomaly (SA),
which caused widespread canopy degradation and early leaf calculatedasthedeviationofeach5-dayobservationfromthe
senescence. Drought impacts were found uneven across forest correspondingmulti-year(2017–2024)average,normalizedby
types [10]: pine and black cherry showed the strongest and its standard deviation. This approach allowed the generation
most prolonged stress responses, while xerophilic oak and ofconsistent5-daytimeseriesforbothCCCandLAIforeach
| mixed deciduous |     | forests | also | indicated | moderate | to  | severe | plot. |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ---- | --------- | -------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
174
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore.  Restrictions apply.

D. Forest disturbance detection (drought-affected) exhibits clear deviations from the multi-
yearaverage(2017-2024)duringlatesummerof2022andthe
To assess forest disturbances associated with drought and
following spring, indicating marked disturbance characterized
treefall events, the Cumulative SA (CSA) was computed for
by a reduction in the forest trait value. Similarly, Fig. 1c
each sampling plot over the 2017-2024 period as the sum of
presents LAI time series for a plot affected by late summer
SA values up to time (1). Unlike instantaneous anomalies,
treefall disturbance in 2023 (FOR19), highlighting the impact
CSA captures the persistence and intensity of functional trait
on forest canopy structure and a consequent decline in the
deviations,highlightingperiodsofvegetationecologicalstress.
respective trait estimation. Notably, in the case of treefall
t (Fig. 1c), the trait anomaly persists into the following year
CSA = SA (1) (2024), as the physical absence of the affected tree prevents
t i
i=1 anystructuralrecoveryatthatlocation,resultinginasustained
X
deviation from the baseline value.
Furthermore, to characterize rapid deviations and potential
As shown in Fig. 2, rolling regression slope of CCC for
recoveryphases,therateofchangeofCSAwasassessedusing
drought-affected plot (FOR71) reaches its minimum value
arollingregressionslope.LinearregressionofeachCSAtime
with intensity around -1.99 during summer 2022, coinciding
serieswasappliedwithinafixed-sizemovingwindowofwidth
with the peak of the drought period. The slope subsequently
(w),generatingasequenceoflocalslopesthatquantifytherate
increases, turning positive in autumn, suggesting possible
anddirectionofchangeovertime.Negativeslopesindicatepe-
vegetation recovery. A second local minimum with intensity
riods of increasing stress accumulation, while positive slopes
around-1.95isobservedinMay2023,althoughitsattribution
suggest recovery or stabilization. The time window size was
remains uncertain and could potentially be linked to a late
empiricallysetto10weeks,basedonecologicalconsiderations
frost event. A third peak in June 2024 might be associated to
and sensitivity tests. This duration is long enough to capture
asecondary,lessseveredroughtepisodecomparedto2022.In
the typical progression of drought induced stress, yet short
contrast,rollingregressionslopeofLAIcalculatedfortreefall
enough to detect abrupt disturbances such as treefall. Testing
affected plot (FOR19) in the same figure (Fig. 2) reveals a
alternative window lengths (i.e. 5, 10, 15 and 20 weeks)
pronounced local minimum nearly aligned with the second
confirmed that 10 weeks provided a good balance between
recorded storm date in summer 2023, with an intensity peak
temporal sensitivity and noise reduction. The slope at each
of -1.57, reflecting immediate structural loss due to canopy
central time point t within the moving window is calculated
collapse.Thepersistenceofnegativeanomaliesfromthemulti-
as shown in (2),
year (2017-2024) average LAI time series is observed in the
following2024vegetativeperiodformingabroadplateauwith
RollingSlope =
w
i= − 0
1(t
i −
t¯)(CSA
i −
CS¯A)
(2) intensity around -2.30. A slight mid-season attenuation of the
t
P
w
i= − 0
1(t
i −
t¯)2 a
c
n
o
o
n
m
tri
a
b
l
u
y
ti
i
o
s
n
ob
o
s
f
e
u
rv
n
e
d
d
e
,
r
w
sto
h
r
ic
y
h
s
m
pe
a
c
y
ie
b
s
e
,
a
su
tt
c
ri
h
bu
a
t
s
ed
he
to
rb
t
a
h
c
e
eo
te
u
m
s
p
p
o
la
ra
n
r
t
y
s
where t
i
is the time index, CPSA
i
is the CSA at time t
i
,
and shrubs, that green up during summer and contribute
whilet¯andCS¯Aarethemeanvaluesinthetemporalwindow.
to the optical signal. As these species enter senescence in
Startingfromtherollingregressionslopetimeseries,segments
late summer and early autumn, the anomaly deepens again,
with negative slopes were selected, indicating a declining
reinforcing the overall negative peak.
trend in vegetation condition. Within each segment, the local
The rolling slope analysis for CCC and LAI forest traits
minimumslopefallingbelowadefinedthresholdwasselected
expanded to the 2020-2024 time range and across all sites is
as the point of peak disturbance intensity. The corresponding
reported in Fig. 3. A threshold of -1.0 in peak intensity was
date was then recorded as the moment of maximum stress
applied to identify meaningful disturbance events. In plots af-
experienced by the vegetation.
fected by 2022 drought (blue dots in Fig. 3), isolated negative
peaks in both CCC and LAI are visible (Fig. 3a and Fig. 3b),
III. RESULTS
reflecting sharp and temporally localized reduction in forest
Thisstudyfocusesonconfirmeddisturbanceevents,specif- function,moreaccentuatedforCCCthanLAI.Thesedrought-
ically the 2022 drought and 2023 treefall, to evaluate the related effects tend to occur at variable times across plots,
method’s ability to identify such events based on their effects indicating heterogeneous sensitivity and response dynamics
on forest condition. Fig. 1a shows selected plots within a amongsitesandspecies.After2022,otherpeaksareobserved
central area of the park, all of which were affected by the in summer 2023 and 2024, suggesting other drought-related
2022drought.Amongthese,someexperiencedtreefallin2023 effects. In contrast, treefall-affected plots (red dots in Fig. 3)
(FOR07, FOR16, FOR19, FOR21, FOR52, FOR53, FOR54, display a consistent temporal clustering of disturbance around
FOR57, FOR60, FOR74). These plots also represent a range summer2023stormevents,bothforCCCandLAI,confirming
of dominant vegetation species, including meso-hygrophilic the method to point timing of canopy loss. Furthermore,
oak or associated with white hornbeam, mixed deciduous, many of these points exhibit a prolonged negative anomaly
open xerophilic oak and hygrophilic black alder. As shown in throughout the 2024 growing season, forming a characteristic
Fig. 1b, the CCC reconstructed time series for plot FOR71 plateau in both CCC and LAI (Fig. 3a and Fig. 3b). Within
175
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 1. a) Map of the study area location within the central portion of the Ticino Regional Park, showing sampling plots predominandly affected by 2022
drought (blue) and 2023 treefall (red). Alongside blue lines for b) 5-day time series of canopy chlorophyll content (CCC) for FOR71 representative of the
2022 drought and c) 5-days time series of leaf area index (LAI) for FOR19 impacted by treefall events in 2023, compared to the corresponding CCC and
LAImulti-yearaverage(2017-2024)andstandarddeviationtimeseries(greenandredlines,respectively).Mapcoordinatereferencesystem:WGS84UTM
zone32N.
TABLEI
AVERAGEANDSTANDARDDEVIATIONOFTHEPERCENTAGEREDUCTION
INCCCANDLAIRELATIVETOTHEMULTI-YEARAVERAGECALCULATED
INTHEDISTURBANCEDATESORINTHESUBSEQUENTYEARS.
|     |     |     |     |              |                   |        | CCC          |           | LAI             |
| --- | --- | --- | --- | ------------ | ----------------- | ------ | ------------ | --------- | --------------- |
|     |     |     |     | Disturbance  | Year              |        | Reduction(%) |           | Reduction(%)    |
|     |     |     |     | Treefall     | 2023(eventyear)   |        | 32.56        | 10.80     | 33.76 8.04      |
|     |     |     |     |              |                   |        | − ±          |           | − ±             |
|     |     |     |     | Treefall     | 2024(1yearlater)  |        | 14.07        | 11.82     | 16.82 5.83      |
|     |     |     |     | Drought      | 2022(eventyear)   |        | − 41.53 ±    | 13.32     | − 31.93 ± 11.54 |
|     |     |     |     |              |                   |        | − ±          |           | − ±             |
|     |     |     |     | Drought      | 2023(1yearlater)  |        | 3.23         | 11.98     | 3.01 9.60       |
|     |     |     |     |              |                   |        | − ±          |           | − ±             |
|     |     |     |     | Drought      | 2024(2yearslater) |        | 5.59         | 13.93     | 4.39 10.46      |
|     |     |     |     |              |                   |        | − ±          |           | − ±             |
|     |     |     |     | years across | the selected      | plots. | Results      | show that | for treefall    |
Fig. 2. Example of rolling regression slopes of CSA (Cumulative sum of in the event year (2023) the average CCC reduction was -
StandardizedAnomalies)forCCCindrought-affectedplot(FOR71)andfor 32.56%,similartoLAI.Thisreflectshowadecreaseincanopy
| LAI in treefall-affected | plot (FOR19). | The 2022 drought | period and 2023 |          |                |         |             |         |          |
| ------------------------ | ------------- | ---------------- | --------------- | -------- | -------------- | ------- | ----------- | ------- | -------- |
|                          |               |                  |                 | coverage | simultaneously | affects | chlorophyll | content | and leaf |
summerstormeventsarehighlighted.
|     |     |     |     | area. One | year later | (2024), | reduction | in both | parameters |
| --- | --- | --- | --- | --------- | ---------- | ------- | --------- | ------- | ---------- |
wereconsiderablysmaller(around-15.00%),indicatingpartial
thisplateau,aslightmid-seasonattenuationisobserved,likely recovery, likely due to understory regrowth. The persistence
reflecting gap dynamics influenced by understory vegetation of a modest reduction suggests that full canopy recovery may
development. This temporal signature of peaks differentiates require multiple years. In contrast, drought event in 2022
treefall disturbances from drought, which generally produces caused a larger immediate average CCC reduction in the
mainly singular anomalies without prolonged responses. event year (2022), higher than LAI reduction (-41.53% vs.
To identify potential distinguishing patterns in CCC and -31.93%). This pattern is consistent with physiological stress
LAI dynamics associated with different disturbance types, responses, where color loss precedes actual leaf drops. In the
Table I reports the average percentage reduction in CCC and following two years (2023 and 2024), both CCC and LAI
LAI relative to the multi-year mean values, calculated at the showed substantial recovery, although a mild negative values
time of the disturbance event or at nearby dates in subsequent in 2024 may suggest either residual drought effects. Overall,
176
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore.  Restrictions apply.

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.3. Timingandintensityofvegetationdisturbanceeventsbasedonrollingslopeanalysisfora)CCCandb)LAI,acrossmonitoredforestplotsaffected
bydrought(bluedots)ortreefall(reddots).Eachpointrepresentalocalminimumintheslopetimeseries,withsizescaledbypeakintensity(onlyvalues
<-1.0shown).
the results highlight clear differences in recovery dynamics the effects of treefall persisted for a longer period. These
between the two types of disturbances: treefall causes abrupt resultspresentafirststeptowardsthedetectionofforeststress
proportionalreductionsinbothCCCandLAIthatdonotshow from biophysical traits across multiple disturbance and forest
clear recovery in the following year, while drought impacts types. Nevertheless, some limitations should be considered:
CCCmorestronglythanLAIintheeventyear,withrelatively the ANNs implemented in the Sentinel-2 Toolbox are trained
rapid recovery in the following years. on simulated data, so their accuracy depends on how well
|     |     |     |     |     |     |     |     | simulations | reflect real | leaves, | canopy | and | soil conditions. | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------- | ------ | --- | ---------------- | --- |
IV. CONCLUSION addition, retrievals are sensitive to input quality (i.e. Sentinel-
|                     |             |      |              |     |           |                   |     | 2 reflectance), | meaning            | that presence |     | of clouds,    | atmospheric |          |
| ------------------- | ----------- | ---- | ------------ | --- | --------- | ----------------- | --- | --------------- | ------------------ | ------------- | --- | ------------- | ----------- | -------- |
| These               | preliminary |      | results show | the | potential | of Sentinel-2     |     |                 |                    |               |     |               |             |          |
|                     |             |      |              |     |           |                   |     | effects, or     | sensor calibration | errors        |     | may propagate |             | into the |
| derived             | CCC and     | LAI  | time series  | to  | detect    | and differentiate |     |                 |                    |               |     |               |             |          |
|                     |             |      |              |     |           |                   |     | final outputs.  | Moreover,          | cloud cover   | and | variable      | atmospheric |          |
| forest disturbances |             | from | drought      | and | treefall  | in temperate      |     |                 |                    |               |     |               |             |          |
ecosystems. Rolling slope analysis of cumulative anomalies conditions can reduce the availability of observations, poten-
|     |     |     |     |     |     |     |     | tially introducing | gaps | or noise | that | may | affect time | series |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---- | -------- | ---- | --- | ----------- | ------ |
seemstoidentifywithgoodaccuracythetimingofdisturbance
|                |     |      |            |         |     |           |         | reconstruction | and anomaly | estimates. |     | Future | developments |     |
| -------------- | --- | ---- | ---------- | ------- | --- | --------- | ------- | -------------- | ----------- | ---------- | --- | ------ | ------------ | --- |
| peak, aligning |     | with | documented | drought |     | and storm | events. |                |             |            |     |        |              |     |
Droughtweremostlycharacterizedbyisolatednegativepeaks, could explore the generalization of the disturbance detection
|     |     |     |     |     |     |     |     | framework | across different | forest | types | and | geographic | re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | ------ | ----- | --- | ---------- | --- |
particularlyinCCC,reflectingshort-termphysiologicalstress.
In contrast, treefall led to a initial peak at the time of the gions. The CSA and rolling slope approach is conceptually
|                 |             |      |           |            |           |            |          | flexible, as   | it only relies | on temporal  |     | dynamics | of biophysical |           |
| --------------- | ----------- | ---- | --------- | ---------- | --------- | ---------- | -------- | -------------- | -------------- | ------------ | --- | -------- | -------------- | --------- |
| event, followed |             | by a | prolonged | plateau    | of        | anomalies, | with     |                |                |              |     |          |                |           |
|                 |             |      |           |            |           |            |          | traits, making | it potentially | transferable |     | to       | forest         | with con- |
| mid-season      | attenuation |      | due to    | understory | dynamics. |            | Percent- |                |                |              |     |          |                |           |
age reductions confirmed both CCC and LAI experienced trasting stuctures and phenologies. Nevertheless, adapting the
|             |              |            |        |             |          |             |          | methodology     | to diverse         | ecosystems | would     |               | require      | validation |
| ----------- | ------------ | ---------- | ------ | ----------- | -------- | ----------- | -------- | --------------- | ------------------ | ---------- | --------- | ------------- | ------------ | ---------- |
| significant | decline,     | with       | CCC    | more        | affected | by drought, | due      |                 |                    |            |           |               |              |            |
|             |              |            |        |             |          |             |          | against local   | ground measurement |            | and       | consideration |              | about      |
| to pigment  | degradation, |            | and    | both traits | equally  | impacted    | by       |                 |                    |            |           |               |              |            |
|             |              |            |        |             |          |             |          | region-specific | disturbances       | (e.g.      | fires,    | windthrow,    |              | cyclones). |
| treefall    | due to       | structural | canopy | damage.     |          | Recovery    | patterns |                 |                    |            |           |               |              |            |
|             |              |            |        |             |          |             |          | Another         | promising avenue   | is the     | extension |               | to a broader | set of     |
| showed      | a gradual    | return     | to     | baseline    | after    | drought,    | whereas  |                 |                    |            |           |               |              |            |
177
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore.  Restrictions apply.

functionaltraits,beyondthoseinvestigatedhere,byexploiting [13] K.P.Tripathy,andA.K.Mishra,“Howunusualisthe2022European
exist ing and upcoming hyperspectral s atellite missions (e.g. compound drought and heatwave event?,”. Geophysical Research Let-
ters,vol.50,pp.e2023GL105453,2023.
PRISMA,EnMAP,futureCHIME)thatprovidericherspectral
[14] M.Mauri,“Rinnovazionenaturalepostschiantoinunquerco-carpineto
informationforcanopychemistryandphysiology.Futurework di pianura nel Parco del Ticino,” Master thesis dissertation, University
could also extend the approach by integrating complementary ofPadua,Italy,2024.
data streams. For instance, existent and upcoming radar ob- [15] M. Weiss, F. Baret, and S. Jay, “S2ToolBox Level 2 products LAI,
|     |     |     |     |     |     |     |     |     | FAPAR, FCOVER,” | Doctoral | dissertation, |     | EMMAH-CAPTE, |     | INRAe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------------- | --- | ------------ | --- | ----- |
servations like Sentinel-1 and future ROSE-L may provide Avignon,2020.
robust information on canopy structure and soil moisture [16] Q.Xie,J.Dash,A.Huete,A.Jiang,G.Yin,Y.Ding,...andW.Huang,
“RetrievalofcropbiophysicalparametersfromSentinel-2remotesens-
| under frequent | cloud | cover, | while | LiDAR |     | data could | capture |     |               |               |         |            |       |             |     |
| -------------- | ----- | ------ | ----- | ----- | --- | ---------- | ------- | --- | ------------- | ------------- | ------- | ---------- | ----- | ----------- | --- |
|                |       |        |       |       |     |            |         |     | ing imagery,” | International | Journal | of Applied | Earth | Observation | and |
additionaldimensionsofforeststressandrecovery.Combining Geoinformation,vol.80,pp.187-195,2019.
Sentinel-2 with these sources would strengthen the resilience [17] A.Savitzky,andM.J.Golay,“Smoothinganddifferentiationofdataby
|                 |     |            |     |            |        |             |     |     | simplified | least squares | procedures,” | Analytical | chemistry, | vol. | 36, pp. |
| --------------- | --- | ---------- | --- | ---------- | ------ | ----------- | --- | --- | ---------- | ------------- | ------------ | ---------- | ---------- | ---- | ------- |
| and scalability | of  | the method |     | for global | forest | monitoring. |     |     |            |               |              |            |            |      |         |
1627-1639,1964.
V. ACKNOWLEDGMENT
| The author       | thanks       |                   | V. Parco    | and           | R.      | Castrovinci    | (Ticino      |      |     |     |     |     |     |     |     |
| ---------------- | ------------ | ----------------- | ----------- | ------------- | ------- | -------------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| Regional         | Park)        | for participating |             | in            | the     | 2022           | measurement  |      |     |     |     |     |     |     |     |
| campaigns        | and          | for their         | valuable    |               | support | with           | plot charac- |      |     |     |     |     |     |     |     |
| terization.      | The author   | also              | thanks      | V.            | Parco   | and F.         | Crozzoletto  |      |     |     |     |     |     |     |     |
| (Ticino Regional |              | Park)             | for their   | support       |         | and assistance |              | with |     |     |     |     |     |     |     |
| the in-situ      | verification |                   | of treefall | disturbances. |         |                |              |      |     |     |     |     |     |     |     |
REFERENCES
[1] G.B.Bonan,“Forestsandclimatechange:forcings,feedbacks,andthe
climatebenefitsofforests,”science,vol.320,pp.1444-1449,2008.
| [2] V. H. | Dale, L.   | A. Joyce, | S.    | McNulty, | R. P.    | Neilson, | M. P. | Ayres, |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | ----- | -------- | -------- | -------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| M. D      | Flannigan, | ... and   | B. M. | Wotton,  | “Climate | change   | and   | forest |     |     |     |     |     |     |     |
disturbances:climatechangecanaffectforestsbyalteringthefrequency,
| intensity, | duration,    | and        | timing | of fire,    | drought,    | introduced |             | species, |     |     |     |     |     |     |     |
| ---------- | ------------ | ---------- | ------ | ----------- | ----------- | ---------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| insect     | and pathogen | outbreaks, |        | hurricanes, | windstorms, |            | ice storms, | or       |     |     |     |     |     |     |     |
landslides,”BioScience,vol.51,pp.723-734,2001.
| [3] M. Wegler | and | C. Kuenzer, | “Potential |     | of earth | observation | to  | assess |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ---------- | --- | -------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
theimpactofclimatechangeandextremeweathereventsintemperate
forests—Areview,”RemoteSensing,vol.16,pp.2224,2024.
| [4] N. G.      | McDowell, | N.    | C. Coops, | P.      | S. Beck, | J. Q.          | Chambers, | C.        |     |     |     |     |     |     |     |
| -------------- | --------- | ----- | --------- | ------- | -------- | -------------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| Gangodagamage, |           | J. A. | Hicke,    | ... and | C. D.    | Allen, “Global |           | satellite |     |     |     |     |     |     |     |
monitoringofclimate-inducedvegetationdisturbances,”Trendsinplant
science,vol.20,pp.114-123,2015.
[5] A.GnilkeandT.G.Sanders,“Distinguishingabruptandgradualforest
disturbanceswithMODIS-basedphenologicalanomalyseries,”Frontiers
inPlantScience,vol.13,pp.863116,2022.
[6] J.B.Cannon,C.J.Peterson,J.J.O’BrienandJ.S.Brewer,“Areview
andclassificationofinteractionsbetweenforestdisturbancefromwind
andfire,”ForestEcologyandManagement,vol.406,pp.381-390,2017.
| [7] W. B.  | Cohen, | S. P. Healey, | Z.        | Yang,   | S. V. Stehman, | C.                 | K. Brewer, | E.   |     |     |     |     |     |     |     |
| ---------- | ------ | ------------- | --------- | ------- | -------------- | ------------------ | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| B. Brooks, | ...    | and Z.        | Zhu, “How | similar | are            | forest disturbance |            | maps |     |     |     |     |     |     |     |
derivedfromdifferentLandsattimeseriesalgorithms?,”Forests,vol.8,
pp.98,2017.
| [8] B. Putzenlechner, |     | P.  | Koal, M. | Kappas, | M.  | Lo¨w, P. | Mundhenk, | A.  |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------- | ------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Tischer,...andT.Koukal.“Towardsprecisionforestry:Droughtresponse
| from remote | sensing-based |     | disturbance |     | monitoring | and | fine-scale | soil |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ----------- | --- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
informationinCentralEurope,”ScienceofTheTotalEnvironment,vol.
880,pp.163114,2023.
| [9] P. Brun, | A. Psomas, |     | C. Ginzler, | W.  | Thuiller, | M. Zappa, | and | N. E. |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----------- | --- | --------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Zimmermann,“Large-scaleearly-wiltingresponseofCentralEuropean
| forests | to the | 2018 extreme | drought. |     | Global change | biology,” |     | vol. 26, |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | -------- | --- | ------------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
pp.7021-7035,2020.
| [10] B. Savinelli, | C.  | Panigada, | G.  | Tagliabue, | L. Vignali, | R.  | Gentili, | F. E. |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ---------- | ----------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Fassnacht,...andM.Rossini,“Monitoringfunctionaltraitsofcomplex
temperateforestsusingSentinel-2dataduringaseveredroughtperiod,”
ScienceofTheTotalEnvironment,vol.957,pp.177428,2024.
[11] C.Cerli,L.Celi,P.BoSIo,R.MoTTA,andG.Grassi,“Effectofland
| use change | on  | soil properties |     | and carbon | accumulation |     | in the | Ticino |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | ---------- | ------------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Park(NorthItaly),”StudiTrentSciNat,vol.85,pp.83-92,2009.
| [12] M. Boschetti, |         | L. Boschetti, | S.       | Oliveri,       | L. Casati, | and I. | Canova,   | “Tree  |     |     |     |     |     |     |     |
| ------------------ | ------- | ------------- | -------- | -------------- | ---------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| species            | mapping | with          | Airborne | hyper-spectral |            | MIVIS  | data: the | Ticino |     |     |     |     |     |     |     |
Parkstudycase,”InternationalJournalofRemoteSensing,vol.28,pp.
1251-1261,2007.
178
Authorized licensed use limited to: Zhejiang University. Downloaded on October 18,2026 at 05:41:14 UTC from IEEE Xplore.  Restrictions apply.