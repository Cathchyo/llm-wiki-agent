RemoteSensingofEnvironment305(2024)114071
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Leveraging past information and machine learning to accelerate land
disturbance monitoring
Su Ye*, Zhe Zhu, Ji Won Suh
Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT, USA
A R T I C L E I N F O A B S T R A C T
Edited by Marie Weiss Near real-time (NRT) monitoring of land disturbances holds great importance for delivering emergency aid,
mitigating negative social and ecological impacts, and distributing resources for disaster recovery. Many past
Keywords: NRT techniques were built upon examining the overall change magnitude of a spectral anomaly with a pre-
Disturbance defined threshold, namely the unsupervised approach. However, their lack of fully considering spectral change
Near real-time
direction, change date, and pre-disturbance conditions often led to low detection sensitivity and high commission
Land change
errors, especially when only a few satellite observations were available at the early disturbance stage, eventually
Time-series
resulting in a longer lag to produce a reliable disturbance map. For this study, we developed a novel supervised
Latency
Machine learning machine learning approach guided by historical disturbance datasets to accelerate land disturbance monitoring.
This new approach consisted of two phases. For the first phase, the supervised approach applied retrospective
analysis on historical Harmonized Landsat Sentinel-2 (HLS) datasets from 2015 to 2021, combined with several
open disturbance products. The disturbance model was constructed for each condition of consecutive anomaly
number, with the aim of enhancing the specificity for delineating early-stage disturbance regions. Then, these
stage-based models were applied for an NRT scenario to predict disturbance probabilities with 2022 HLS images
incrementally on a weekly basis. To demonstrate the capability of this new approach, we developed an opera-
tional NRT system incorporating both the unsupervised and supervised approach. Latency and accuracy were
evaluated against 3000 samples that were randomly selected from the five most influential disturbance events of
the United States in 2022, based on labels and disturbance dates interpreted from daily PlanetScope images. The
evaluation showed that the supervised approach required 15 days (since the start of the disturbance event) to
reach the plateau of its F1 curve (where most disturbance pixels are detected with high confidence), seven days
earlier with roughly 0.2 F1 score improvement compared to the unsupervised approach (0.733 vs. 0.546 F1
score). Further analysis showed the improvement was mainly due to the substantial decrease in commission
errors (17.7% vs 44.4%). The latency component analysis illustrated that the supervised approach only took an
average of 4.1 days to yield the first disturbance alert at its fastest daily updating speed, owing to its decreased
sensitivity lag. This finding highlighted the importance of using past knowledge and machine learning to reduce
detection delays for an NRT monitoring task.
1. Introduction carbon storage (Liang et al., 2014; Seidl et al., 2014). Land disturbances
include natural hazards such as wildfire, flooding, tornado, and a variety
1.1. Near real-time monitoring of land-use shifts led by anthropogenic activities (Thornton et al., 2024;
Zhu et al., 2020). There is a pressing need for mapping land disturbance
Land disturbance, often defined as any discrete event that occurs events in a timely manner, which will hold great relevance for miti-
outside the natural variability of the land (Zhu et al., 2020), could gating their social and ecological impacts (Verbesselt et al., 2012) and
fundamentally alter land surface composition, condition, and cover delivering emergency aid to protect lives and infrastructure (Field et al.,
types, consequently disrupting ecosystem functioning such as biodi- 2012).
versity (Martínez-Ramos et al., 2016), productivity (Peters et al., 2013), A large-scale Near Real-Time (NRT) monitoring of land disturbances
* Corresponding author.
E-mail address: remotesensingsuy@gmail.com (S. Ye).
https://doi.org/10.1016/j.rse.2024.114071
Received 24 October 2023; Received in revised form 20 January 2024; Accepted 18 February 2024
0034-4257/©2024ElsevierInc.Allrightsreserved.

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
has been long limited by a lack of timely satellite data acquisition until Most cover-based or anomaly-based techniques require collecting a
multiple global datasets became publicly available with reduced data minimum number of consecutive observations (conse) for disturbance
latency and improved delivery service (Woodcock et al., 2008; Wulder confirmation (e.g., conse=6 in most CCDC-like approaches), as the
et al., 2018). Earlier satellite-based NRT works were mainly based on temporal stability of a disturbance signal aids its differentiation from
coarse-resolution optical images such as the MODIS products, DETER noisy signals. The setting of conse is practically controlled by the user
project (Shimabukuro et al., 2006), the BFAST-monitor tool (Verbesselt through algorithm configuration (Bullock et al., 2022). Arguably, it is
et al., 2012), and later extended to the medium-resolution dataset common to employ less-than-required satellite observations for early
owning to the free access policy of Landsat datasets, such as the Global disturbance alerting (Shang et al., 2022; Ye et al., 2021a), yet fewer
Land Analysis and Discovery (GLAD) alerting system (Hansen et al., post-disturbance observations for decision-making come at the cost of
2016), the Geobosques platform (Vargas et al., 2019) and Continuous substantially increased commission errors. For example, Bullock et al.
Change Detection and Classification (CCDC)-adapted approaches (Pas- (2022) showcased over 80% commission errors in the initial 50 days
quarella et al., 2017; Ye et al., 2021b). The recent NRT studies incor- since the disturbance occurrence date based on the sample-based
porate the Synthetic Aperture Radar (SAR) dataset (Bullock et al., 2022; agreement; likewise, Shang et al. (2022) reported over 80% commis-
Doblas et al., 2022; Eckerstorfer et al., 2019; Martinis et al., 2018) and 3- sion errors when only one or two anomaly observations were identified.
m daily PlanetScope data (Francini et al., 2020), further reducing the This was because these techniques discriminated disturbance signals
observation lag by incorporating more frequent acquisition of satellite only relying on their relatively higher overall change magnitudes. When
observations. On the other hand, some advanced approaches combined the post-disturbance data collection is short, the anomalies are more
multiple sensors to shorten the time interval for collecting temporal likely attributed to ephemeral and noisy signals (e.g., phenological
observations (Reiche et al., 2018; Shang et al., 2022; Tang et al., 2023). variation, short-term weather extremes, and even data noise), thereby
For example, Shang et al. (2022) used the Harmonized Landsat Sentinel- compromising the detection accuracy. Consequently, a long collection of
2 (HLS) dataset which combines four satellite sensors (Landsat 8, post-disturbance observations is still a must for most operational man-
Landsat 9, Sentinel-2A, and Sentinel-2B) and successfully decreased the agement tasks, if an NRT disturbance map with an acceptable commis-
confirmation latency of a land disturbance to 35 days. sion rate is expected.
Despite various input dataset types, NRT disturbance algorithms are This study aims to develop a new supervised anomaly-based
generally categorized into two broad groups: the cover-based and the approach to reduce detection latency and at the same time enhance
anomaly-based approaches. The cover-based approach was built on the the detection accuracy. The new approach was inspired by Retrospective
land cover classification and cover category change (or called land cover Chart Review (RCR), a popular type of medical research design in which
conversion) (Andela et al., 2022; Diniz et al., 2015; Francini et al., 2020; pre-recorded, patient-centered datasets are used to examine clinical
Giglio et al., 2009; Hansen et al., 2016; Reiche et al., 2018, 2021; Vargas characteristics (Gill and Kaplan, 2021; Kaji et al., 2014; Vassar and
et al., 2019). This approach, typically the Global Land Analysis & Dis- Matthew, 2013). One notable advantage of RCR is that it is easier to
covery (GLAD) Alert system (Hansen et al., 2016), constructs a land- access conditions where there is a long latency from the initial exposure
cover classification model based on historical or empirically selected and the patient’s diagnosis (Hess, 2004) so that the early symptoms
samples, then applies the model to classify each newly collected image could be retrospectively identified. The valuable information gathered
and to detect new disturbance pixels if these pixels have been consis- from RCR could be further applied to guide subsequent prospective
tently classified as altered land cover categories. The recent emerging studies. Similarly, the recent availability of numerous land cover data-
studies for NRT land cover mapping (Brown et al., 2022; Yu et al., 2022) sets and disturbance products (Chuvieco et al., 2019; Johnson and
could be potentially leveraged for cover-based land disturbance moni- Wittwer, 2008; Latifovic et al., 2016; Rollins, 2009) as well as freely
toring as well. The cover-based approach often requires an additional accessed historical satellite images have enabled us to gain insights into
step for reducing data noise and normalizing input images (Reiche et al., early disturbance signals of a disturbance event whose occurrence might
2018, 2021) or simply assumes no seasonality for their targeted cover be confirmed a lot later. Specifically, we are allowed to design methods
(Hansen et al., 2016). If a disturbance only induces within-type surface to effectively extract its early-stage spectral and temporal features from
change (or named as cover condition change), such as insect disturbance historical time series, which can be further leveraged to construct ma-
and drought, the cover-based approach might fail to alert the distur- chine learning models. With enhanced model specificity and better
bance. Some advanced cover-based methods generated soft classifica- capability to differentiate noise guided by well-recorded disturbance
tion outputs as a proxy, such as cover probabilities (Reiche et al., 2018, event information, it is expected that retrospective disturbance analysis
2021) or cover fractions (Vargas et al., 2019), with an aim to address will improve both timeliness and accuracy against the current anomaly-
subtle change as a “continuous” variable (e.g., forest loss). Nevertheless, based approaches dominated by empirical thresholding. To our knowl-
these methods were only successful in a relatively simple scenario for a edge, historical datasets and analyses have not been systematically
two-category classification scheme (e.g., forest vs. non-forest) so far. explored yet for the NRT disturbance mapping tasks. It is still unclear
The anomaly-based approach detects early disturbance signals by what disturbance predictors are extracted from satellite time series and
discriminating recent spectral anomalies from time-series dataset (Ols- how disturbance models are constructed for monitoring a variety of land
son et al., 2016; Pasquarella et al., 2017; Shang et al., 2022; Tang et al., disturbances at their different lag stages.
2019; Verbesselt et al., 2012; Ye et al., 2021a). The anomaly-based
approach was often achieved without the necessity of tackling land 1.2. Lag components
cover information. This approach first builds a spectral baseline model
by fitting historical time-series datasets from a stable period, and then For this study, the monitoring latency is viewed as an intricacy
continuously examines if the newly collected satellite observation rea- impacted by five lag components, i.e., observation, data, sensitivity,
ches a spectral difference over a predefined threshold against its pre- confirmation, and production lag, from input, algorithm, and produc-
dicted reflectance. The new disturbance event will be confirmed if the tion perspectives (Fig. 1). Assessing different proportions of lag com-
minimum number of consecutive anomalies (namely “peek window”) is ponents can provide potential treatments for accelerating disturbance
satisfied. The anomaly-based approach could exclude such noises as data alerting. Note that compared to Fig. 1 of Bullock et al. (2022), the as-
seasonality and other natural variations by incorporating cyclic trends sessments of sensitivity and production lags are newly proposed for this
and long-term trends into the baseline model. Also, benefiting from study.
directly detecting change magnitudes, the anomaly-based approach is The input latency is mainly affected by observation and data lags. An
capable of detecting subtle disturbances that do not directly alter land observation lag refers to the time interval between the disturbance
cover types (Yang et al., 2022; Ye et al., 2021b). occurrence and when the sensor collects the first clear observation,
2

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Fig. 1. Graphic explanations for the actual latency from an operational NRT disturbance task which is controlled by five lag components, i.e., observation, data,
sensitivity, confirmation, and production lag. Sensitivity and confirmation lag are newly proposed for this study, compared to the work done by Bullock et al. (2022).
which is often related to a satellite revisiting cycle and weather condi- each processing, an NRT platform will ingest the new images released,
tions; a data lag is the delay between the first clear observation collec- map the latest disturbance, and publish the NRT product. These steps are
tion and this observation being preprocessed to a standard reflectance computationally expensive and time-consuming. Particularly for a large-
product ready for analytics, which is often systematic and shorter than area monitoring system, it is often practically unfeasible to make a daily
one week (Bullock et al., 2022). update, resulting in a production lag brought by the pre-defined
Algorithmic latency includes sensitivity and confirmation lags. A updating day interval.
sensitivity lag refers to the day interval between the date for the first The remainder of the paper will be organized as follows: we first
available data product and the date for an algorithm first alerting this introduce the study area and dataset used for this research (Section 2),
disturbance. A sensitivity lag occurs where the disturbance signals are then describe the design of an operational NRT system (Section 3); we
spectrally unobvious at the first observations (e.g., insect disturbances, will thoroughly compare the latency and accuracy of the system
selective logging), ranging from zero day (i.e., the quickest alert) for adopting supervised against the unsupervised anomaly-based approach
those dramatic disturbances, to infinity when the algorithm or the (Section 4.1), report their lag component assessment (Section 4.2), and
sensor is incapable of detecting the signal. A confirmation lag, also exhibit distinction of latency curves and lag components from different
named “algorithm latency” by Bullock et al. (2022), is a lag between the disturbance events (Section 4.3); finally, we will discuss the comparative
first alert and the disturbance confirmation. performance against other existing NRT methods as well as the limita-
Lastly, a production lag is the operational delay caused by map tions (Section 5).
production and delivery, closely linked to the platform updating inter-
val. The production lag was not well discussed yet in past studies. For
Fig. 2. Five selected sites for NRT monitoring of land disturbance events for 2022 in this study. For each event, four adjacent HLS tiles were used for the test.
3

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
2. Study area and dataset greatly reduced data lag. Therefore, the HLS datasets were selected as
the time series inputs for this study. Each HLS tile has 3660 rows and
2.1. Study area 3660 columns with 30 m of pixel spacing in both directions, provided
over projected map coordinates aligned with the Military Grid Reference
We chose the five most influential disturbance events across the System (MGRS). For each disturbance event, we chose four adjacent HLS
Conterminous United States (CONUS) in 2022, including three natural tiles (2 by 2) for the NRT monitoring and the accuracy assessments
disasters, one forest insect infestation, and one human-induced land (Table 1), and a total of 20 tiles were used for the study. For each tile, we
surface modification (Fig. 2). downloaded all harmonized surface reflectance products from 2015 to
Mosquito fire: 2021 for the retrospective analysis; during the later NRT monitoring
Mosquito fire was the largest wildfire in California occurring in phase, we downloaded the HLS images of 2022 in an increment of one
2022. The massive fire began on September 6 and was 90% contained on week which is the predefined production interval for our test.
October 4, burning a total area of 31,075 ha, mostly in forested regions Besides, we collected four open-access annual CONUS disturbance
of El Dorado and Placer counties; more than half of the fire regions products from 2016 to 2020, which were used for labeling historical
(58%) experienced low soil burning severity (Teater, 2023). A total of anomalies. They are 1) land cover transition map generated by differ-
11,117 people were evacuated, and 5848 houses were threatened or encing Land Change Monitoring, Assessment, and Projection (LCMAP)
damaged (Teater, 2023). Primary Land Cover maps (Xian et al., 2022) between two neighbor
Spongy moth: years; 2) LANDFIRE Disturbance Products (Ryan and Opperman, 2013);
The spongy moth, formerly known as the gypsy moth, has been a 3) Landsat Collection 1 Level-3 Burned Area Science Product (Hawbaker
major forest disturbance type in New England since 2015 (Pasquarella et al., 2020); and 4) Aerial Detection Survey (ADS) insect activity dataset
et al., 2017). Sponge moth caterpillars hatch from egg mass in early which records polygonal forest health information generated by sketch
May, begin feeding on the leaves of hardwood trees since early June, and mapping (Johnson and Wittwer, 2008). All these products, except for
reach peak defoliation by late June or early July as the larvae mature ADS insect dataset, are originally available at 30-m resolution. We ras-
(Pasquarella et al., 2017). Sponge moth defoliation is an ephemeral and terized the ADS dataset to 30-m binary maps (insect vs no-insect regions)
cyclic disturbance that occurs repeatedly every year in New England: to keep aligned with the HLS satellite images.
trees often re-foliate from spongy moth attacks in the summer, although The validation pixels were sampled by applying a stratified sampling
moth-induced repeated defoliation combined with other stressors may approach on the accumulated NRT land disturbance maps generated by
lead to a long-term decline in forest health. the supervised approach. The accumulated NRT maps were made from
Hurricane Ian: merging all NRT detection maps within the assessment window for each
Hurricane Ian, which happened in September of 2022, was the disturbance; the assessment window is defined as the disturbance period
deadliest hurricane to strike Florida since 1935. It peaked as a Category with an extension of 15 days after a disturbance ends to take account of
5 hurricane with 260 km/h winds on September 28 when attacking the most delayed detections. We randomly sampled 300 pixels from the
west coast of Florida (Karimiziarani and Moradkhani, 2023), causing “disturbance” and “no disturbance” regions, respectively, in each
major inland flooding and landfall in counties such as Lee and Charlotte. accumulated NRT map (600 samples for an event), forming 3000 sam-
The hurricane killed 149 people across Florida and produced cata- ples in total for five disturbance events. For the response design, three
strophic damage with an estimated loss of 113 billion (NOAA National experienced remote sensing experts interpreted the reference distur-
Centers, 2023), including extensive tree and building damage due to bance date for each sample pixel as the first date for their identifying
strong wind and floods. visible disturbance signals from Planet Explorer (https://www.planet.
Kentucky flooding: com/explorer/). The Planet Explorer provides free access to 3-m daily
Between July 26 and July 30, 2022, due to sustained record-breaking Planet images. As such, we were capable of determining the actual
rainfall, several devastating floods hit 15 counties in East Kentucky, such disturbance date for the reference sample pixel, which was more accu-
as Hidman, Perry, and Prestonsburg counties. The floods resulted in the rate than interpreting the first anomaly date from the time series (Shang
death of 45 people and displaced thousands more. Entire homes and et al., 2022; Ye et al., 2021a, 2023) or using the date right in-between
some communities were swept away by flood water, causing extensive the first anomaly and the last pre-disturbance observation date
damage to thousands of buildings, vehicles, and other infrastructures in (Bullock et al., 2022; Reiche et al., 2018). While the occasional cloud/
the flooded region, with an estimated cost of over 1.5 billion dollars shadow contamination or missing datasets in PlanetScope still might
(NOAA National Centers, 2023). cause an inaccurate interpretation of the exact disturbance date, such
Construction: impacts were negligible because 1) PlanetScope images provided the
Texas has been one of the hotspots for construction projects in the
past decade. Due to the lower cost of living and taxes, Texas, particularly
Austin and Houston, has become a big draw to businesses and companies Table 1
relocating from California and elsewhere. For example, Samsung started Location, disturbance periods, and selected HLS tiles for the disturbance events
to be tested for this study.
construction on a semiconductor manufacturing campus in the suburbs
of Austin in 2022. Austin City ranked No.1 in the United States for the Disturbance Impacted Region HLS Tile IDs Disturbance Period
housing demand in 2022 with numerous construction sites for real estate Event (2022)
developments (Salviati and Warnock, 2023), thereby being selected as Mosquito fire Central 10SFH, 10SFJ, Sep. 6 – Oct. 22
the testing site for studying construction events. California 10SGH, 10SGJ
Spongy moth New England 18TXM, Jun. 1 – Jul. 15
18TXN,
2.2. Datasets 18TYM,
18TYN
Harmonized Landsat Sentinel-2 (HLS) dataset combines four satellite Hurricane Ian Southwest 17RLK, 17RLL, Sep. 26 – Sep. 28
sensors (Landsat 8, Landsat 9, Sentinel-2A, and Sentinel-2B satellites), Florida 17RMK,
17RML
providing the highest temporal resolution of 2–3 days (Claverie et al., Kentucky flood Eastern 17SKB, 17SKC, Jul. 26 – Jul. 30
2018) among all medium-resolution (10–30 m) satellite datasets. Kentucky 17SLB, 17SLC
Notably, for the latest version of the HLS dataset (version 2.0), the Land Construction Central Texas 14RNU, Feb. 15 – Jun. 15
Processes Distributed Active Archive Center approximately takes only 14RNV,
14RPU, 14RPV
two days of data lag to release the surface reflectance products, with
4

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
densest optical images as daily observations; 2) the beginning dates for anomalies, for this study, refer to the spectral breakpoints within a time
some disturbance events (such as Hurricane Ian and Mosquito Fire) were series produced by break over-detection. They are related to either real
well recorded and ascertained so that the recorded disturbance dates disturbance signals or non-disturbance factors (e.g., phenology shifts
could be directly adopted. The labeling process with PlanetScope images and ecosystem recovery). There are two key parameters for controlling
was showcased in Section S1 of the supplementary material. the break detection sensitivity for CCDC-like algorithms: change prob-
ability threshold (chg_t) defines the minimum change magnitude to
3. Methodology identify a single breakpoint (the default chg_t is 0.99), and conse is the
minimum number of temporally consecutive anomalies required to
A two-phase workflow was designed for this new approach (Fig. 3). confirm a breakpoint (the default conse is 6). We used a lower change
For the first phase “retrospective disturbance analysis”, we applied an probability threshold of 0.90 and a shorter conse as three observations,
“over-detection” for time-series breakpoints from historical time series ensuring the inclusion of the most subtle disturbance pixels (Cohen
to generate a comprehensive sample pool respectively for disturbance or et al., 2017) as well as a variety of non-disturbance anomalies. Different
non-disturbance anomalies, under the guidance of the disturbance from the normal CCDC’s way of handling breakpoints, the S-CCD algo-
products; then we developed a specific sample set and built a machine- rithm will skip the model initialization but only update the current
learning model for each disturbance stage. For the second phase “Near anomaly record (see Table S1), considering that the Kalman filter can
Real-time Monitoring”, we implemented a NRT disturbance mapping self-adjust model coefficients for local fluctuations (Ye et al., 2021a).
based on these stage-based disturbance models incrementally with a Structural breakpoints refer to another type of breakpoints that leads
step of one week for the year 2022, i.e., the system updating interval was to an obvious structural change of the time series, where it is essential to
one week. refit a new harmonic curve by using new observations of at least one
year to guarantee the model predictability (Zhu et al., 2020). We
adopted a more conservative parameter set to generate structural
3.1. Phase 1: retrospective disturbance analysis
breakpoints, chg_t =0.9999, conse =8. When the last observation of a
historical time series was processed, the anomaly records, which rep-
3.1.1. Anomaly generation
resented the current spectral status, were saved out to the disk for the
We first applied time-series-based breakpoint detection to generate
second phase (Fig. 3).
anomalies from historical HLS datasets (2015–2021) on a per-tile basis.
For each HLS tile to be monitored, Stochastic Continuous Change
3.1.2. Anomaly labeling
Detection (S-CCD) (Ye et al., 2021a), a near real-time adaptation of
We combined two sources of disturbance maps, respectively from
Continuous Change Detection and Classification (CCDC) (Zhu and
anomaly generation and historical disturbance products, to develop
Woodcock, 2014), was applied. S-CCD incorporates the Kalman filter
high-confidence spectral anomaly pools. An anomaly-based disturbance
into the CCDC algorithm and recursively updates the anomaly records
map was produced from anomaly records based on the disturbance-
(see Table S1 in the supplementary), instead of reconstructing the model
extraction strategy proposed in Section 3.3.6 by Zhu et al. (2020).
from scratch when new observations are available (Ye et al., 2021a). The
This post-processing excluded “greener” breakpoints identified as
short-memory nature of S-CCD saves disk space from removing the
increased NIR, decreased Red and SWIR1 bands:
historical images and speeds up the computation by skipping the step of
refitting a time-series model, thereby improving model efficiency, ΔRed<0.02&ΔNIR> (cid:0) 0.02&ΔSWIR1<0.02 (1)
especially for large-area NRT monitoring. An improvement we made on
Where ΔRed, ΔNIR, and ΔSWIR1 are the spectral change magnitudes
Ye et al. (2021a) is to let S-CCD produce spectral anomalies, besides
of the RED, NIR, and SWIR1 bands for the breakpoint. On the other
structural breakpoints, for the processing of historical datasets. Spectral
Fig. 3. A two-phase workflow of the supervised near real-time monitoring approach proposed for this study. For Phase 1, eight stage-based models were built for
each center tile using anomaly samples from a 3 by 3 moving window of neighbor tiles; the samples were labeled by combining historical disturbance datasets and
breakpoint detection from the HLS time series (2015–2021). For Phase 2, the NRT monitoring was implemented using the stage-based retrospective models
incrementally for each week of 2022.
5

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
hand, we generated an annual product-based disturbance potential map 3.1.4. Model construction
(2016–2020) by fusing four previously mentioned open disturbance To enhance model specificity for different disturbance stages, we
products: the pixels were labeled as “disturbance” if this pixel fell within individually established one sample set and one disturbance model for
the disturbance regions in at least one open disturbance product. We each consecutive anomaly number condition (nanom = 1,2,3,…,8,
extracted the high-confidence disturbance pixels from the overlapped Fig. 5). Zhu et al. (2016) suggested a total of 20,000 samples for the
disturbance regions between anomaly-based and product-based maps Landsat-based classification, and an HLS image (3660 * 3660) occupies
into a disturbance anomaly pool. Those pixels labeled as “disturbance” only a half of the total pixel number of the Landsat scene (5000 * 5000),
only in anomaly-based maps were spectral anomalies not covered by so a total number of 10,000 training samples was selected to build a
historical disturbance regions, thereby representing noisy signals, so we series of stage-based models for each tile. To evenly distribute these
sort them into a non-disturbance anomaly pool. 10,000 samples across the sample years, we allocated 2000 samples for
For each HLS tile, we generated and labeled spectral anomalies on an each tile in each year, so for a center tile, a total of 90,000 samples (9
annual basis, and then combined labeled spectral anomalies from a 3 by tiles * 5 years * 2000 samples) were used to build each stage-based
3 HLS tile window centered at the targeted tile (Brown et al., 2019) with model (see Fig. 3). A proportional random sampling was chosen
a temporal length of the middle five years (2016–2020, see “Phase 1” in because it has shown superiority over a balanced sampling for a classi-
Fig. 3). We excluded the year 2015 and 2021 as the S-CCD might suffer fication scheme (Brown et al., 2019; Zhu et al., 2016). However, there
inaccuracies for detecting breakpoints at the starting and the ending of a are far fewer disturbance anomalies compared to the non-disturbance
time series. There are two primary motivations for the 3 by 3 spatio- anomalies in practice, causing the disturbance category to be easily
temporal tile window design: 1) the machine learning model could be under-represented. The trickier is that the omission and commission
developed with a better generalization for dealing with disturbance error rates are often both increased at a similar degree for the early
variability using sample acquisition from a larger spatial extent and a disturbance stage due to too many noisy signals. But we expected to
longer disturbance history; 2) 3 by 3 tile window considerably decreases suppress omission errors so that the potentially disturbed regions were
variation of local models between two neighborhood tiles, avoiding comprehensively provided for the possible subsequent high-resolution
artifacts on the boundaries of the two tiles (Brown et al., 2019). damage mapping. As such, we designed a linear function with a nega-
tive slope to control disturbance sample proportion, which enabled
3.1.3. Predictor extraction assigning a higher sample proportion to the disturbance category for the
We extracted 17 disturbance-related predictors from the S-CCD shorter nanom (i.e., the earlier disturbance stage). For each nanom, the
model outputs (not from the disturbance products), which could be sample proportions are denoted as:
categorized into the disturbance-process and the pre-disturbance group.
P dist (n anom )=P base +(conse(cid:0) n anom )*slope (2)
Fig. 4 illustrates these disturbance-related predictors using a sample
time series. Six HLS spectral bands, i.e., blue, green, red, NIR, SWIR1, P nondist (n anom )=1(cid:0) P dist (n anom ) (3)
and SWIR2 bands, were considered. We retained the three predictors
used in the COntinuous monitoring of Land Disturbance (COLD) algo- Where Pdist (nanom ) and Pnondist (nanom ) are the proportions of distur-
rithm (Zhu et al., 2020) for the disturbance-related breakpoint decision, bance and non-disturbance categories for each nanom; conse is the con-
i.e., 1) multispectral change magnitudes to take account of spectral stant, the number of consecutive anomaly observations to detect a
change direction, 2) normalized change intensity, and 3) spectral con- structural breakpoint (conse =8); Pbase is the baseline proportion when
sistency angle. Besides, we also included 4) the disturbance date to the nanom reaches the maximum, and the parameter slope controls
incorporate seasonality, 5) the span of anomaly days for data temporal decreasing impacts of nanom on Pdist. The parameter sensitivity test (see
density, and 6) multispectral pre-change reflectance to depict land-cover Section S3 of the supplementary material) revealed that Pbase =0.1 and
spectral features prior to spectral anomalies being detected. The for- slope=0.02 was the only group that keeps an acceptable overall accu-
mulas for these predictors are given in Table 2. racy while maintaining a low omission rate across all nanom.
For each nanom (i.e., 1, 2, 3, …, 8), we trained a random-forest model
(ntrees =100) for the binary classification scheme (disturbance vs. no
Fig. 4. Graphic illustration of the disturbance-related predictors used for this study (“n” means the number of variables).
6

S. Ye et al.                                                                                                                                                                                            R  e  m  o  t e  S  e  n s  i n g   o  f  E  n v  i r o  n  m  e  n t305(2024)114071
Table 2
Definition of 17 predictors used for the NRT disturbance prediction.
| Predictor name  |     | Description  |                           |     | Number  | Category  |
| --------------- | --- | ------------ | ------------------------- | --- | ------- | --------- |
|                 |     | = ρ          | (cid:0) ̂ρ = 1,2,3,4,5,6  |     |         |           |
1 .   M u l tis p e c t ra l  c h a n g e  M a g n it u d es  C M i i ,d i st dat i, di st d a t,  i 6
∑ ( ) 2
2 .   No r m a li z e d  c h a n g e   m ag n i tu d e   = 5 C M i 1
|     |     | C M no rma li z e d | i= 1 |     |     |     |
| --- | --- | ------------------- | ---- | --- | --- | --- |
R M S E i
3 .   S p e c t r a l  c o n s i st e n cy angle  1 ∑ n (cid:0) 1 1
|                        |                 | a n g l e =       | β , j+              |     |     |                      |
| ---------------------- | --------------- | ----------------- | ------------------- | --- | --- | -------------------- |
|                        |                 | n (cid:0) 1       | j = 1 j )1          |     |     | Disturbance process  |
| 4 .   D is t u r b a n | c e   d a t e   | (                 | 2 π                 |     | 2   |                      |
|                        |                 | si n = s i n      | d o y ,             |     |     |                      |
|                        |                 | d o y             | T d i s t d a t     |     |     |                      |
|                        |                 | (                 | )                   |     |     |                      |
|                        |                 | =                 | 2 π                 |     |     |                      |
|                        |                 | c o s d o y c o s | d o y d i s t d a t |     |     |                      |
T
| 5. Anomaly span  |     | ndays=lastdistdat(cid:0) | distdat  |     | 1   |     |
| ---------------- | --- | ------------------------ | -------- | --- | --- | --- |
) ( ))
6. Multispectral pre-disturbance reflectance  ∑ (cid:0) (cid:0)2 π 2 π 6  Pre-disturbance
|     |     | ̂ρ i,distdat =a0,i | + 3 k=1 ak,icos x +bk,isin | x +c1,ix, i=1,2,3,4,5,6  |     |     |
| --- | --- | ------------------ | -------------------------- | ------------------------ | --- | --- |
|     |     |                    | T                          | T                        |     |     |
Note: CMi and RMSEi are the individual change magnitude and Root Mean Square Error of the ith band; ρ and ̂ρ
i,dist dat  i,dist dat are the actual and the predicted
reflectance of the ith band; n is the current consecutive anomaly number; β j,j+1 is the change-vector angle from jth to j+1th anomaly; lastdist
dat and dist dat are the
last disturbance date observed as a spectral anomaly and the disturbance starting date respectively; doy is the date of the year; a0,i, ak,i, bk,i and c1,i are the harmonic
coefficients for theith band; k is the temporal frequency of the harmonic components.
Fig. 5. Explanation for developing stage-based sample sets and disturbance models. The disturbance stages were characterized by the number of current consecutive
anomalies (nanom). We used the stage-specific sample proportion, Pdist (nanom )and Pnondist (nanom ), to make samples and then developed a machine-learning model
individually for each stage.
disturbances) using each corresponding sample set. Hence, a total of  chg_t for “anomaly generation” in Phase 2). Then, 17 predictors were
eight stage-based retrospective models were prepared for the second  generated for each outputted anomaly. Finally, we input the predictors
phase.  into the corresponding stage-based model based on the current nanom,
and produced its NRT random-forest disturbance probability at a per-
pixel level. We assigned the disturbance probability as “0” for those
3.2. Stage 2: near real-time monitoring
pixels without anomalies being detected. The unsupervised probability
Starting from January 1st, 2022, we iterated a workflow of near real-  applied the change probability threshold of 0.99 to detect disturbance
breakpoints, followed by eliminating the breakpoints attributed to the
time monitoring to process the newly collected images until the end of
greener trend using the rule of Eq. (1). The threshold as 0.99 is the most
2022. The workflow was operated incrementally at a step of one week.
commonly used change threshold for the CCDC-like approach, which,
The workflow ingested new images collected for each week, updated the
for example, was adopted in the “Land Change Monitoring, Assessment,
NRT anomaly records, and then extracted 17 disturbance-related pre-
and Projection” project (Brown et al., 2019). We computed the unsu-
dictors listed in Table 2. We tested and compared two ways for gener-
pervised probability as the ratio of the current consecutive anomaly
ating disturbance probability: (1) the proposed method based on the
|     |     |     | number by the maximum anomaly number (conse |     |     | =8). For example, if  |
| --- | --- | --- | ------------------------------------------- | --- | --- | --------------------- |
retrospective models (called supervised) and (2) the traditional anomaly
there are six anomalies at the end of the current time series, the
method based on an empirical change-magnitude threshold (called un-
disturbance probability is 6 / 8 =75%.
supervised). For the supervised probability, we first used the change
probability threshold of 0.9 to detect anomalies for each pixel (the same  To  generate  spatially  complete  disturbance  patches  (i.e.,  a
7

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
continuous region affected by the change process), the Flood Fill algo- the primary tool to assess “lag-accuracy” performance: the Initial Delay
rithm was first applied to the two disturbance probability layers (Ye and Level Off Point. The Initial Delay is assigned to the date that 2% of
et al., 2023). Flood Fill is an algorithm to identify adjacent pixels as an the total disturbance pixels are detected, representing the shortest time
object in an image based on their similarity to an initial seed pixel (Van of an algorithm for beginning to alert a disturbance event. The Level Off
der Walt et al., 2014). The Flood Fill algorithm outperformed other Point, the time when F1 score is just stabilized, is computed as the date
segmentation algorithms such as SLIC and watershed in our previous test that has the maximum y for a virtual curve from rotating 45 degrees
(Ye et al., 2023), and hence was chosen for this study. For the supervised around the line connecting the beginning and end points of the sigmoid
probability layer, we retained the disturbance regions as the disturbance curve (Bullock et al., 2022). The x coordinate of Level Off Point indi-
patches with an average disturbance probability >50%; for the cated the shortest lag to reach the maximum F1 score, and the y coor-
unsupervised-probability layer, we labeled the patches as their average dinate points to the maximum overall performance.
probability ≥12.5%, so that the disturbance identification was possible Moreover, we will assess the individual contribution of the five lag
even when one anomaly observation was captured, as consistently as the sources given in Fig. 1. We will generate individual lags for each
supervised-probability approach. disturbance sample following the definitions given in Table 3, and then
Finally, the identified disturbance patches were categorized into two compute the mean statistics of each lag component. We will also report
levels of the NRT products based on the current patch-level anomaly Mean Time Lag (MTL) and Mean Time Lag for the First Alert (MTLf) for
number. We assigned the disturbance patches with an average of less comparison to other existing studies. The sum of all the lag sources is
than six consecutive anomalies into “detection level”, and otherwise equivalent to MTL, a lag metric commonly used in previous studies
“confirmation level”. We used the confirmation threshold as six (Shang et al., 2022; Ye et al., 2021a). The sum of all except the confir-
consecutive anomalies, considering most CCDC-like algorithms use six mation lag is equal to as MTLf (Reiche et al., 2018), which is the average
observations as the minimum required anomaly number (Brown et al., time between the reference disturbance date and the date for capturing
2019; Ye et al., 2021a; Zhu et al., 2020). When one workflow was the first anomaly.
completed for a monitoring interval, we saved two levels of the distur-
bance products with the disturbance attributes into the database. The 4. Results
polygon-based attributes include the first anomaly date, the last anom-
aly date, and the production date (we set it as the last day of each week). 4.1. Unsupervised vs. supervised
As our experiments were performed in early 2023, all HLS datasets for
2022 have been available for downloading, and hence the data lag was Fig. 6 shows the sigmoid curves for the unsupervised (the traditional
zero. To keep close to the real latency for the operational monitoring, we method based on a predefined threshold) and the supervised (the pro-
manually set the data lag as two days of HLS data lag and added it to all posed) NRT approach based upon all evaluation samples from the five
production dates. The two-day data lag is the estimated average time testing sites (n =3000, 50% are disturbance samples). Table 4 lists their
required by NASA LP DAAC to release HLS2.0 surface reflectance key lag metrics. Generally, F1 score curves for the two approaches both
products since their first collection, based on the user experience from began to increase around the Initial Delay (Fig. 6A); with time going
our NRT platform downloading over 90,000 HLS 2.0 images. It is worth forward, F1 was gradually rising because more post-disturbance obser-
mentioning that our comparative evaluation mainly focused on the vations became available both temporally and spatially, and eventually
detection-level products, though both the detection- and confirmation- plateaued at the Level Off Point (Fig. 6A). The sigmoid curves of the two
level results were assessed and reported. This was because the detec- approaches were almost fully overlapped before their Initial Delay (2
tion level was practically more relevant for an NRT platform owing to its days for the detection level, and ~ 21 days for the confirmation level),
enabling timelier monitoring (<10 days) and providing important po- and became divergent afterward: the F1 sigmoid curve of the supervised
tential disturbance maps for further high-resolution applications. We approach (“blue”) became consistently higher than that of the unsu-
developed an operational platform to update and to visualize the NRT pervised approach (“yellow”). Particularly at the detection level, the
results for each week based on the Google Earth Engine platform supervised approach only took 15 days to reach the Level Off Point with
(https://gers.users.earthengine.app/view/nrt-conus). 0.733 F1 score, which had seven days quicker and almost 0.2 F1
improvement than the unsupervised (the unsupervised: 22 days, 0.546
3.3. Accuracy and latency assessment F1 score, see Table 4). The detection-level comparison reflects their large
performance distinction for mapping disturbances at their early stage.
We will use the sigmoid framework proposed by Bullock et al. (2022) Differently, the unsupervised and supervised approaches presented the
to comparatively assess the unsupervised and supervised approach. The same lag days to reach their Level Off Points for the confirmation level
sigmoid framework incorporates both omission and commission of (35 days), because the two approaches both applied conse = 6 hence
disturbance alerts as a function of lag. Hence, it could lead to a more similar confirmation lag (as Section 4.2 will show) that dominates their
comprehensive assessment than other NRT assessment metrics that only
focused on the disturbance cases being correctly identified (Bullock
Table 3
et al., 2022), such as Mean Time Lag (MTL) (Reiche et al., 2018). In this
Definition of lag types to be assessed for this study. MTL: Mean Time Lag; MTLf:
study, we defined the omission error at a certain lag as when a distur-
Mean Time Lag for the First Alert.
bance sample was not hit by the disturbance patches from the recent
Lag types Definition
NRT results and defined the commission error as when a non-
disturbance sample was included in one disturbance patch. Observation Lag Day interval between the reference disturbance date and the first
clear observation date
Following the sigmoid framework, we will graph omission, com-
Data Lag Constant value as two days
mission, and F1 score as sigmoid curves for incremental values of the
Sensitivity Lag Day interval between the first clear observation date and the first
total lag (i.e., production date minus disturbance date), allowing for a anomaly date detected
thorough comparison of detection effectiveness at a full range of latency. Confirmation Day interval between the first and the last anomaly date detected
F1 score is a harmonic mean of inverse omission and commission error Lag for a peek window
Production Lag Day interval between the last anomaly date and the date being
rate:
officially confirmed by the platform
(1(cid:0) omission)*(1(cid:0) commission) MTL The sum for observation lag, data lag, sensitivity lag,
F 1 =2* (2(cid:0) omission(cid:0) comission) (4) confirmation lag, and production Lag
MTLf The sum for observation lag, data lag, sensitivity lag, and
production Lag
Two lag metrics generated from the sigmoid curves will be used as
8

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Fig. 6. Comparison of the unsupervised and supervised approaches on sigmoid curves at detection and confirmation levels based on a total of 3000 evaluation
samples from the five disturbance sites. The omission error, commission error, and F1 score are respectively plotted as a function of total lag (the sum of five lag
components) within a tolerance window of 0 to 90 days. Two key latency metrics, Initial Delay and Level Off Points, are marked on the curves as “circle”
and “triangle”.
Table 4
Comparison of the unsupervised and supervised approaches on lag, omission error, commission error and F1 score at the Initial Delay and Level Off Point of their
sigmoid curves. The bold font highlights the lag/accuracy difference between the two approaches.
Detection Level
Initial Delay Level Off Point
Lags (Days) Omission Error Commission Error F1 Lags (Days) Omission Error Commission Error F1
Unsupervised 2 68.8% 63.5% 0.336 22 46.4% 44.4% 0.546
Supervised 2 63.9% 58.5% 0.386 15 34.0% 17.7% 0.733
Confirmation Level
Initial Delay Level Off Point
Lags (Days) Omission Error Commission Error F1 Lags (Days) Omission Error Commission Error F1
Unsupervised 22 89.9% 8.7% 0.182 35 75.2% 14.9% 0.384
Supervised 21 98.0% 0.6% 0.040 35 71.2% 8.1% 0.439
total lag at the confirmation level (~77% of the total lag, see Section while the supervised correctly ignored it (Fig. 7C) through a compre-
4.2). Reducing consecutive observations for confirmation is out of the hensive examination on change magnitudes, pre-change features,
scope for this study and was often determined by user settings (Bullock change season, and change direction using the retrospective models.
et al., 2022). However, the supervised approach still achieved a rela- Fig. 8 is an example to show that the supervised approach also could
tively better F1 score at the confirmation level (supervised vs. unsu- suppress omission errors. The sample pixel was experiencing spongy
pervised: 0.439 vs. 0.384). moth damage with a medium-level NDVI drop in June of 2022 (Fig. 8A
By investigating the error components, the supervised presented and B). Unless a structural breakpoint was detected so that the S-CCD
consistently lower omission (Fig. 6B) and commission rates (Fig. 6C) model entered its initialization stage, the supervised approach inspected
than the unsupervised approach over time after the Initial Delay. the outputted consecutive spectral anomalies (if any) and predicted
Particularly, the supervised achieved a much lower commission error disturbance probability for each new observation. Therefore, the su-
rate than the unsupervised by approximately 27 percent points at the pervised approach was capable of delineating subtle change induced by
detection level (17.7% vs. 44.4%, Table 4). This revealed that the pri- spongy moth (Fig. 8C) even with low change magnitudes, as long as
mary advantage of incorporating historical datasets was in alleviating most pixels within the associated anomaly patch were identified as
overdetection. Fig. 7 showcased a sample pixel under the effects of disturbance pixels by the machine-learning model. However, the unsu-
climate variability that was misclassified as “disturbance” by the unsu- pervised approach missed most damage at the confirmation level
pervised approach. Its NIR time series experienced a noticeable increase (Fig. 8C) as the spectral curve was quickly recovered (Fig. 8A), causing
at the breakpoint (Fig. 7A), which was related to the earlier leaf-on date the change magnitude to be lower than the threshold of 0.99 change
for the year 2022 (Fig. 7B). The unsupervised approach identified the probability.
breakpoint as “disturbance” because the overall change magnitude was Comparing the detection and confirmation levels, the accuracies at
larger than the predefined threshold (the change probability of 0.99), the detection level were higher than at the confirmation level for both
9

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Fig. 7. An example site ((cid:0) 97.947, 30.339) for commission errors produced by the unsupervised approach. The HLS time series (A) shows a structural breakpoint
induced by increasing NIR which was possibly related to phenological shifts, while no obvious disturbance signal was found from inspecting the HLS images (B). The
supervised approach exhibited superiority in suppressing such over-detection by modeling disturbance and non-disturbance anomalies using the retrospective
datasets (C).
approaches. This finding was contrary to most past NRT studies, in days) required to collect six HLS clear observations after disturbance
which the confirmation results achieved the better overall accuracies as occurrence.
only enough consecutive anomalies could effectively exclude commis-
sion errors. The outstanding performance for the detection level was
4.2. Lag component evaluation
mainly attributable to its considerably lower omission errors (e.g.,
detection vs. confirmation =34.0% vs. 71.2% for the supervised at its
Fig. 9 displays assessments of different lag components of the two
Level Off Point). Notably, the detection level was advantageous for
approaches. Note that we made assessments based on only the distur-
capturing the ephemeral disturbances (e.g., Hurricane Ian and Spongy
bance samples that were successfully confirmed by each approach (un-
Moth) whose effects only lasted for one or two observations. As two out
supervised: 287 cases; supervised: 370 cases). The total lags of the two
of five study sites were ephemeral disturbances (344 / 830 disturbance
approaches, MTLs, are close (unsupervised vs. supervised = 39.4 vs.
cases), the validation samples for this disturbance type might be over-
38.8 days), which is mainly due to 1) the ambiguity in reporting inde-
represented for this study, resulting in an overestimation of the
pendent temporal metrics with ignorance on spatial accuracy (i.e.,
detection-level accuracy. Note that the unrealistic sample proportion
omission and commission error rates) (Bullock et al., 2022); 2) the total
only distorted the relative accuracy between the detection and the
lags of the two approaches were dominated by their similar confirmation
confirmation level but yielded little statistical effects on comparative
lag (~77%) as their required anomaly numbers are both set as six. In
performance between the unsupervised and supervised approaches.
comparison, the supervised approach yielded lower sensitivity lags (0.1
Another distinction between the detection and the confirmation level
was that the confirmation level required a much longer lag to reach
vs 1.1 days), making its MTLf shorter than the unsupervised by 10% (9.1
vs. 10.0 days). This revealed the advantage of the supervised approach
Initial Delay (22/21 days vs. 2 days) and Level Off Point (35 days vs. 22/
15 days) than the detection level for both unsupervised and supervised for the early alerting of the disturbance, especially when the signal was
not pronounced. The observation lags were both averagely 2.0 days,
approaches. Their difference reflects the minimum lag days (roughly 20
which were mainly controlled only by the HLS revisiting cycle and
10

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Fig. 8. An example site ((cid:0) 73.377, 41.946) for omission errors produced by the unsupervised approach. The HLS time series (A) shows a time series impacted by
spongy moth damage, with the disturbance breakpoint detected by the supervised approach marked as “black circle” in (A). The damage has been verified by color
change (“white spots”) within HLS images (B). The NRT results (C) present that the unsupervised approach totally missed the disturbance patches at the confirmation
level due to the quick spectral recovery.
Fig. 9. An assessment of the unsupervised and supervised approach for their different lag components, with their correctly confirmed sample case number shown in
the y-axis labels. MTL: Mean Time Lag; MTLf: Mean Time Lag for the First Alert.
weather conditions. The average production lags of the two approaches (unsupervised vs. supervised = 287: 370 cases) and involved in pro-
were almost the same (4.9 vs. 5.0 days). Their small numeric difference duction lag assessments. MTL and MTLf of the two approaches did not
was caused by the different sample sets that were successfully confirmed present sufficient differences as their sigmoid curves showed (Fig. 6),
11

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
which echoed the viewpoint that these two metrics are problematic for confirmation lags) among the five disturbance events. The other three
latency assessment because they were calculated based on their own lag components (data, observation, and product lags) were only
correctly identified samples, ignoring their omission and commission contingent on data acquisition or platform operation, thereby generally
errors (Bullock et al., 2022). A high rate of omission errors and com- indifferent across various disturbance events. As a result of the subtle
mission errors often caused incomplete patch detection and too many change signals at their early stage, spongy moth and construction yiel-
noisy signals, which would eventually lead to a mapping delay. ded higher sensitivity lags for the NRT monitoring. Compared to the
unsupervised, the supervised approach reached a lower average sensi-
tivity lag, enabling an earlier alerting for these two events. For the
4.3. Individual disturbance assessments
confirmation lag, Mosquito fire showed much shorter lags than the other
four disturbances, possibly owing to the frequent dry and sunny weather
Fig. 10 shows that individual disturbance types presented different
for North California providing dense post-fire observations. Different
sigmoid curves and lag metrics. For the detection level, “Kentucky flood”
from the sensitivity lag, confirmation lags were close between the su-
(Fig. 10C) received the quickest alerting as its Level Off Point at (9 days,
pervised and the unsupervised approaches, indicating that the retro-
0.94 F1 score); “Construction” had the longest latency as the Level Off
spective information helped little in reducing the confirmation lag,
Point at (43 days, 0.68 F1 score), which was possibly due to the fact that
which should be controlled by the setting of conse and data density.
the initial stage of a construction project (e.g., land clearing) often
yielded small-area and unobvious spectral signals; two ephemeral dis-
5. Discussion
turbances, “Kentucky Flood” and “Hurricane Ian”, presented an inverted
U-shaped sigmoid curve while the other three were S-shaped. This in-
5.1. Comparison to other NRT studies
dicates that some patches affected by ephemeral disturbances experi-
enced rapid recovery. For the confirmation level, F1 scores for two
Compared to the study using the closest evaluation method (Bullock
ephemeral disturbances dropped dramatically compared to the detec-
et al., 2022), applying CCDC on sentinel-1 time series (i.e., “P2”
t
L
i
e
o
v
n
e l
l e
O
v
f
e
f
l
P
,
o
w
in
h
t
i
,
l e
w
t
h
h
i
e
c h
o
e
th
x
e
p
r
la
t
i
h
n
r
e
e
d
e
t h
re
e
m
n
a
o
i
t
n
ic
e
e
d
a b
si
l
m
e p
il
e
a
r
r
f o
F
r
1
m
s
a
c
n
o
c
r
e
e s
d i
f
f
o
f
r
e r
t
e
h
n
e
c
i
e
r configuration) reached a Level Off Point (203 days, 0.216 F1 score) at
the confirmation level for monitoring tropical deforestation, much
between the detection and the confirmation level in Table 4.
worse than the same metric result for the supervised approach (38.8
Fig. 11 demonstrates the dynamics of the detection- and the
confirmation-level products over time since a disturbance. For “Mos-
days, 0.439 F1 score). Not to mention that we included the ephemeral
quito Fire” (Fig. 11A) and “Spongy Moth” (Fig. 11B), most disturbance
disturbances which were challenging and greatly impacted our F1 score
at the confirmation level. Reiche et al. (2018) combined observations
regions in the detection level were confirmed (displayed as red poly-
from six satellites, Sentinel-1, ALOS-2, Landsat 7 and 8, to detect a
gons) since 5th week in the figure. Differently, the detected patches for
specific land disturbance, deforestation, and reached a MTL as 31 days;
two ephemeral disturbances, “Hurricane Ian” (Fig. 11C) and “Kentucky
Shang et al. (2022) built a method based on HLS datasets with setting
Flood” (Fig. 11D), were not converted into the confirmation-level
four minimum consecutive anomalies for confirmation, reporting a
patches but disappeared after the 5th week, as these disturbance
resultant MTL as 35 days. The MTL of our supervised approach (38.8
events did not last long enough to generate six consistent anomalies. The
days) seems to be a little longer than the above two studies, but we
NRT platform did not successfully map the Kentucky Flood in the 1st
approached more diversified land disturbances including ephemeral
week for this case, which might be lacking clear observations due to the
disturbances. More important is that we assessed our approach in an
rainy/cloudy weather often accompanying the flooding event (longer
operational platform by including observation, data, and production lag
data lag); once the first post-flood clear observation became available,
assessments, which additionally increased approximately nine extra lag
more flood-related signals were captured, mainly on housing damage
days compared to the previous studies. It is noteworthy that for emer-
and soil change, leading to an F1 jump at the 9th day in Fig. 10C
gency events, the updating interval of our NRT system could be manu-
(“detection level”).
ally adjusted to a one-day interval to make the fastest response with
Table 5 exhibits different algorithmic latency (sensitivity and
Fig. 10. Sigmoid accuracy curves for individual disturbance events being marked with the two key latency metrics at the detection and at the confirmation level.
12

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Fig. 11. The dynamics of detection- and confirmation-level products for different disturbance events. The centroid coordinates for the sites are Mosquito Fire
((cid:0) 120.752, 39.056), Spongy Moth ((cid:0) 73.684, 43.144), Hurricane Ian ((cid:0) 81.898, 26.652), and Kentucky Flood ((cid:0) 83.382, 37.553).
Table 5
Algorithmic latency comparison for the five disturbance events.
Sensitivity lag (days)
Mosquito Fire Spongy Moth Kentucky Flood Hurricane Ian Construction
Unsupervised 0.56 4.29 0 0 6.40
Supervised 0.57 2.18 0 0 4.75
Confirmation lag (days)
Mosquito Fire Spongy Moth Kentucky Flood Hurricane Ian Construction
Unsupervised 18.08 31.08 29.00 35.27 34.70
Supervised 17.22 31.80 32.89 35.36 35.13
zero-day production lag, so that the average lag for alerting the first explicit model for each anomaly number condition, considerably
anomaly for an event (MTLf) would be further shortened to around half enhancing the capability of distinguishing early signals and decreasing
of a week (4.1 days). It will be even faster in the future, with more sensitivity lags, hence a timelier detection. For future research, the su-
medium-resolution satellite sensors launched and quicker release of pervised approach is readily expanded to provide NRT mapping for
reflectance products. disturbance agents through the incorporation of agent samples.
All the previous studies used the unsupervised anomaly approach
based on the predefined change threshold, mostly focusing on forest
disturbances. To our knowledge, this study is the first attempt to build 5.2. Limitations
up a sole NRT approach/system intended for various natural disasters
and human-induced terrestrial changes. To address the issue of distur- The relatively lower overall accuracy in the confirmation level sug-
bance variety, we designed multifaceted predictors, including the pre- gests the dilemma of disturbance confirmation. For this study, we used
disturbance features that are indicative of background land cover, and the CCDC default minimum observations (conse =6) for confirming a
spectral change features for characterizing a disturbance process. With disturbance patch, which was well verified in multiple past studies on
the retrospective analysis of those historical disturbances, we were able Landsat-based studies (Brown et al., 2019; Ye et al., 2021a; Zhu et al.,
to establish machine learning models using these predictors to better 2019). But the conse was not tested yet on a per-event basis. Especially, it
analyze ongoing anomaly signals. Notably, our approach built an was still challenging to accurately confirm the impacted regions of those
short-lived events. The two ephemeral events, “Kentucky Flood” and
13

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
“Hurricane Ian”, did not lead to permanent land cover conversion, and represent the views or policies of the Department of the Interior, nor
their spectral signals only lasted for one to three observations. As a does mention of trade names, commercial products, or organizations
result, their omission errors greatly increased after their Level Off Points imply endorsement by the U.S. Government.
(Fig. 10C and Fig. 10D). Even with a decreased minimum anomaly
number such as conse=4 in (Shang et al., 2022), it is still not likely to Appendix A. Supplementary data
accurately detect events such as flash flooding, which often induces only
one anomaly. In contrast, “Spongy Moth” (36 days, 0.76 F1 score) and Supplementary data to this article can be found online at https://doi.
“Construction” (43 days, 0.68 F1 score) had a lag for their Level Off org/10.1016/j.rse.2024.114071.
Points close to the MTL of the supervised (38.8 days) using six anoma-
lies. It suggests that confirming a disturbance event with six anomalies References
(conse =6) is still workable for most non-ephemeral disturbance events.
The varied sigmoid curves and Level Off Points of these disturbance Andela, N., Morton, D.C., Schroeder, W., Chen, Y., Brando, P.M., Randerson, J.T., 2022.
events indicate a future direction for developing agent-based confir- Tracking and classifying Amazon fire events in near real time. Sci. Adv. 8, eabd2713.
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,
mation strategies instead of a universal confirmation rule.
Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K.,
The present methodology predominantly depends on U.S. distur- Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D.,
bance datasets to construct retrospective models, which introduces dif- Reker, R.R., Rover, J., 2019. Lessons learned implementing an operational
continuous United States national land change monitoring capability: the land
ficulties in deploying the supervised approach globally. This could
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens.
potentially be overcome by manual sample interpretation, but we pro- Environ. https://doi.org/10.1016/j.rse.2019.111356.
pose further research into automating the transfer of U.S. samples to Brown, C.F., Brumby, S.P., Guzder-Williams, B., Birch, T., Hyde, S.B., Mazzariello, J.,
Czerwinski, W., Pasquarella, V.J., Haertel, R., Ilyushchenko, S., 2022. Dynamic
other countries with a goal of enhancing the global applicability of this
world, near real-time global 10 m land use land cover mapping. Sci. Data 9, 1–17.
supervised model. The method’s efficacy is confirmed with the HLS Bullock, E.L., Healey, S.P., Yang, Z., Houborg, R., Gorelick, N., Tang, X., Andrianirina, C.,
dataset due to its high temporal density. However, there is a lack of clear 2022. Timeliness in forest change monitoring: a new assessment framework
observations in certain areas, such as tropical regions, or the distur- demonstrated using Sentinel-1 and a continuous change detection algorithm.
Remote Sens. Environ. 276, 113043.
bances associated with frequent cloud cover, like floods. For future Centers, N.N., 2023. NOAA National Centers for Environmental Information (NCEI) U.S.
improvements, we recommend integrating radar sensors like Sentinel-1. Billion-Dollar Weather and Climate Disasters (2023) [WWW Document]. https://doi.
org/10.25921/stkw-7w73.
Chuvieco, E., Mouillot, F., Van der Werf, G.R., San Miguel, J., Tanase, M., Koutsias, N.,
6. Conclusion García, M., Yebra, M., Padilla, M., Gitas, I., 2019. Historical background and current
developments for mapping burned area from satellite earth observation. Remote
We proposed a novel supervised machine learning approach to Sens. Environ. 225, 45–64.
Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.C., Skakun, S.V.,
analyze spectral anomalies from HLS time series. The retrospective
Justice, C., 2018. The harmonized Landsat and Sentinel-2 surface reflectance data
analysis extracted and modeled the early disturbance information from set. Remote Sens. Environ. 219, 145–161. https://doi.org/10.1016/j.
the historical time-series datasets, combined with existing disturbance rse.2018.09.002.
Cohen, W.B., Healey, S.P., Yang, Z., Stehman, S.V., Brewer, C.K., Brooks, E.B.,
products. A machine-learning model was built specifically for each
Gorelick, N., Huang, C., Hughes, M.J., Kennedy, R.E., 2017. How similar are forest
anomaly number condition to better discriminate early disturbance disturbance maps derived from different landsat time series algorithms? For. Trees
signals. Compared to the unsupervised approach, the supervised Livelihoods 8, 98.
Diniz, C.G., de Almeida Souza, A.A., Santos, D.C., Dias, M.C., Da Luz, N.C., De Moraes, D.
approach reduced sensitivity lag, especially for subtle disturbances, and
R.V., Maia, J.S., Gomes, A.R., da Silva Narvaes, I., Valeriano, D.M., 2015. DETER-B:
brought forward the Level Off point by seven days, with a 0.2 F1 score the new Amazon near real-time deforestation detection system. IEEE J. Sel. Top.
improvement. Besides, the supervised approach considerably sup- Appl. earth Obs. Remote Sens. 8, 3619–3628.
Doblas, J., Reis, M.S., Belluzzo, A.P., Quadros, C.B., Moraes, D.R.V., Almeida, C.A.,
pressed the commission error rate by 27 percent points, greatly
Maurano, L.E.P., Carvalho, A.F.A., Sant’Anna, S.J.S., Shimabukuro, Y.E., 2022.
enhancing the NRT capability for accurately delineating disturbance DETER-R: an operational near-real time tropical forest disturbance warning system
regions. based on Sentinel-1 time series analysis. Remote Sens. 14, 3658.
Eckerstorfer, M., Vickers, H., Malnes, E., Grahn, J., 2019. Near-real time automatic snow
avalanche activity monitoring system using Sentinel-1 SAR data in Norway. Remote
CRediT authorship contribution statement Sens. 11, 2863.
Field, C.B., Barros, V., Stocker, T.F., Dahe, Q., 2012. Managing the Risks of Extreme
Su Ye: Conceptualization, Data curation, Formal analysis, Method- Events and Disasters to Advance Climate Change Adaptation: Special Report of the
Intergovernmental Panel on Climate Change. Cambridge University Press.
ology, Software, Validation, Visualization, Writing – original draft. Zhe
Francini, S., McRoberts, R.E., Giannetti, F., Mencucci, M., Marchetti, M., Scarascia
Zhu: Conceptualization, Funding acquisition, Investigation, Project Mugnozza, G., Chirici, G., 2020. Near-real time forest change detection using
administration, Resources, Supervision, Writing – review & editing. Ji PlanetScope imagery. Eur. J. Remote Sens. 53, 233–244.
Won Suh: Data curation, Visualization, Writing – review & editing. Giglio, L., Loboda, T., Roy, D.P., Quayle, B., Justice, C.O., 2009. An active-fire based
burned area mapping algorithm for the MODIS sensor. Remote Sens. Environ. 113,
408–420.
Declaration of competing interest Gill, S.K., Kaplan, A.S., 2021. A retrospective chart review study of symptom onset,
diagnosis, comorbidities, and treatment in patients with binge eating disorder in
Canadian clinical practice. Eat. Weight Disord. Anorexia, Bulim. Obes. 26,
The authors declare that they have no known competing financial 1233–1242.
interests or personal relationships that could have appeared to influence Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S.,
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
the work reported in this paper.
using Landsat data. Environ. Res. Lett. 11, 34008.
Hawbaker, T.J., Vanderhoof, M.K., Schmidt, G.L., Beal, Y.-J., Picotte, J.J., Takacs, J.D.,
Data availability Falgout, J.T., Dwyer, J.L., 2020. The Landsat burned area algorithm and products for
the conterminous United States. Remote Sens. Environ. 244, 111801.
Hess, D.R., 2004. Retrospective studies and chart reviews. Respir. Care 49, 1171–1174.
Data will be made available on request. Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust.
For. https://doi.org/10.1080/00049158.2008.10675037.
Acknowledgment Kaji, A.H., Schriger, D., Green, S., 2014. Looking through the retrospectoscope: reducing
bias in emergency medicine chart review studies. Ann. Emerg. Med. 64, 292–298.
Karimiziarani, M., Moradkhani, H., 2023. Social response and disaster management:
This work has been supported by the USGS-NASA Landsat Science insights from twitter data assimilation on hurricane Ian. Int. J. Disaster Risk Reduct.
Team (LST) Program for Toward Near Real-time Monitoring and Char- 95, 103865.
Latifovic, R., Homer, C., Ressl, R., Pouliot, D., Hossain, S.N., Colditz, R.R., Olthof, I.,
acterization of Land Surface Change for the Conterminous US
Giri, C.P., Victoria, A., 2016. North American land-change monitoring system.
(140G0119C0008). The content of this document does not necessarily Remote Sens. L. Use L. Cover 303.
14

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t305(2024)114071
Liang, L., Chen, Y., Hawbaker, T.J., Zhu, Z., Gong, P., 2014. Mapping mountain pine Maycock, T.K. (Eds.), Fifth National Climate Assessment. U.S. Global Change
beetle mortality through growth trend analysis of time-series landsat data. Remote Research Program, Washington, DC, USA. https://doi.org/10.7930/NCA5.2023.
Sens. https://doi.org/10.3390/rs6065696. CH6.
Martínez-Ramos, M., Ortiz-Rodríguez, I.A., Pin˜ero, D., Dirzo, R., Sarukh´an, J., 2016. Van der Walt, S., Scho¨nberger, J.L., Nunez-Iglesias, J., Boulogne, F., Warner, J.D.,
Anthropogenic disturbances jeopardize biodiversity conservation within tropical Yager, N., Gouillart, E., Yu, T., 2014. scikit-image: image processing in Python. PeerJ
rainforest reserves. Proc. Natl. Acad. Sci. USA. https://doi.org/10.1073/ 2, e453.
pnas.1602893113. Vargas, C., Montalban, J., Leon, A.A., 2019. Early warning tropical forest loss alerts in
´
Martinis, S., Plank, S., Cwik, K., 2018. The use of Sentinel-1 time-series data to improve Peru using Landsat. Environ. Res. Commun. 1, 121002.
flood monitoring in arid areas. Remote Sens. 10, 583. Vassar, M., Matthew, H., 2013. The retrospective chart review: important
Olsson, P.-O., Lindstro¨m, J., Eklundh, L., 2016. Near real-time monitoring of insect methodological considerations. J. Educ. Eval. Health Prof. 10.
induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using
Sens. Environ. 181, 42–53. https://doi.org/10.1016/j.rse.2016.03.040. satellite image time series. Remote Sens. Environ. 123, 98–108.
Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,
defoliation using landsat time series. Forests. https://doi.org/10.3390/f8080275. Gao, F., Goward, S.N., Helder, D., Helmer, E., Nemani, R., Oreopoulos, L., Schott, J.,
Peters, E.B., Wythers, K.R., Bradford, J.B., Reich, P.B., 2013. Influence of disturbance on Thenkabail, P.S., Vermote, E.F., Vogelmann, J., Wulder, M.A., Wynne, R., 2008. Free
temperate forest productivity. Ecosystems 16, 95–110. access to Landsat imagery. Science 320, 1011. https://doi.org/10.1126/
Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving science.320.5879.1011a.
near-real time deforestation monitoring in tropical dry forests by combining dense Wulder, M.A., Coops, N.C., Roy, D.P., White, J.C., Hermosilla, T., 2018. Land cover 2.0.
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ. Int. J. Remote Sens. 39, 4254–4284. https://doi.org/10.1080/
204, 147–161. 01431161.2018.1452075.
Reiche, J., Mullissa, A., Slagter, B., Gou, Y., Tsendbazar, N.-E., Odongo-Braun, C., Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Vollrath, A., Weisse, M.J., Stolle, F., Pickens, A., 2021. Forest disturbance alerts for Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
the Congo Basin using Sentinel-1. Environ. Res. Lett. 16, 24005. LCMAP collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
Rollins, M.G., 2009. LANDFIRE: a nationally consistent vegetation, wildland fire, and 143–162.
fuel assessment. Int. J. Wildland Fire 18, 235–249. Yang, X., Zhu, Zhe, Qiu, S., Kroeger, K.D., Zhu, Zhiliang, Covington, S., 2022. Detection
Ryan, K.C., Opperman, T.S., 2013. LANDFIRE–A national vegetation/fuels data base for and characterization of coastal tidal wetland change in the northeastern US using
use in fuels treatment, restoration, and suppression planning. For. Ecol. Manag. 294, Landsat time series. Remote Sens. Environ. 276, 113047.
208–216. Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
Salviati, C., Warnock, R., 2023. Sun Belt metros lead apartment construction boom in forest disturbance using Landsat time series: stochastic continuous change detection.
2023. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112167.
Seidl, R., Schelhaas, M.-J., Rammer, W., Verkerk, P.J., 2014. Increasing forest Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
disturbances in Europe and their impact on carbon storage. Nat. Clim. Chang. 4, Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
806–810. dense Landsat time series: case studies of mountain pine beetle and spruce beetle
Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2021.112560.
monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data. Ye, S., Zhu, Z., Cao, G., 2023. Object-based continuous monitoring of land disturbances
Remote Sens. Environ. 278, 113073. from dense Landsat time series. Remote Sens. Environ. 287, 113462.
Shimabukuro, Y., Duarte, V., Anderson, L., Valeriano, D., Arai, E., Freitas, R., Rudorff, B. Yu, L., Du, Z., Dong, R., Zheng, J., Tu, Y., Chen, X., Hao, P., Zhong, B., Peng, D., Zhao, J.,
F., Moreira, M., 2006. Near real time detection of deforestation in the Brazilian 2022. FROM-GLC plus: toward near real-time and multi-resolution land cover
Amazon using MODIS imagery. Ambient. e Agua-An Interdiscip. J. Appl. Sci. 1, mapping. GIScience Remote Sens. 59, 1026–1047.
37–47. Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
monitoring of tropical forest disturbance: new algorithms and assessment Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
framework. Remote Sens. Environ. 224, 202–218. Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
Tang, X., Bratley, K.H., Cho, K., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2023. Near data for operational land cover classification for the LCMAP initiative. ISPRS J.
real-time monitoring of tropical forest disturbance by fusion of Landsat, Sentinel-2, Photogramm. Remote Sens. 122, 206–221.
and Sentinel-1 data. Remote Sens. Environ. 294, 113626. Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2019.
Teater, D., 2023. Aquatics Specialist Report Mosquito Fire Burned Area Emergency Continuous monitoring of land disturbance based on Landsat time series. Remote
Response (BAER) Assessment Tahoe National Forest. Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.
Thornton, P.E., Reed, B.C., Xian, G.Z., Chini, L., East, A.E., Field, J.L., Hoover, C.M., Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.
Poulter, B., Reed, S.C., Wang, G., Zhu, Z., 2024. Land cover and land-use change. In: Continuous monitoring of land disturbance based on Landsat time series. Remote
Crimmins, A.R., Avery, C.W., Easterling, D.R., Kunkel, K.E., Stewart, B.C., Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.
15