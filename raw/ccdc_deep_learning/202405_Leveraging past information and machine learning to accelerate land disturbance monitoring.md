---
title: "Leveraging past information and machine learning to accelerate land disturbance monitoring"
publication_date: "2024-05"
publication_date_precision: "month"
publication_date_basis: "journal_issue"
journal_issue_year: 2024
doi: "10.1016/j.rse.2024.114071"
source_pdf: "tmp/ccdc/Leveraging past information and machine learning to accelerate land disturbance monitoring.pdf"
source_pdf_pages: 15
converter: "MarkItDown 0.1.5 [pdf]"
date_note: "原 PDF 未标注首次在线发表日期；采用 Crossref 登记的 2024 年 5 月刊期，具体日未知。"
date_reference: "https://api.crossref.org/works/10.1016%2Fj.rse.2024.114071"
---

# Leveraging past information and machine learning to accelerate land disturbance monitoring

Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

Leveraging past information and machine learning to accelerate land
disturbance monitoring

Su Ye *, Zhe Zhu , Ji Won Suh

Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT, USA

A R T I C L E  I N F O

A B S T R A C T

Edited by Marie Weiss

Keywords:
Disturbance
Near real-time
Land change
Time-series
Latency
Machine learning

Near  real-time  (NRT)  monitoring  of  land  disturbances  holds  great  importance  for  delivering  emergency  aid,
mitigating negative social and ecological impacts, and distributing resources for disaster recovery. Many past
NRT  techniques  were  built  upon  examining  the  overall  change  magnitude  of  a  spectral  anomaly  with  a  pre-
defined threshold, namely the unsupervised approach. However, their lack of fully considering spectral change
direction, change date, and pre-disturbance conditions often led to low detection sensitivity and high commission
errors, especially when only a few satellite observations were available at the early disturbance stage, eventually
resulting in a longer lag to produce a reliable disturbance map. For this study, we developed a novel supervised
machine learning approach guided by historical disturbance datasets to accelerate land disturbance monitoring.
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
reach the plateau of its F1  curve (where most disturbance pixels are detected with high confidence), seven days
earlier  with  roughly  0.2  F1  score  improvement  compared  to  the  unsupervised  approach  (0.733  vs.  0.546  F1
score).  Further  analysis  showed  the  improvement  was  mainly  due  to  the  substantial  decrease  in  commission
errors (17.7% vs 44.4%). The latency component analysis illustrated that the supervised approach only took an
average of 4.1 days to yield the first disturbance alert at its fastest daily updating speed, owing to its decreased
sensitivity lag. This finding highlighted the importance of using past knowledge and machine learning to reduce
detection delays for an NRT monitoring task.

1. Introduction

1.1. Near real-time monitoring

Land  disturbance,  often  defined  as  any  discrete  event  that  occurs
outside  the  natural  variability  of  the  land  (Zhu  et  al.,  2020),  could
fundamentally  alter  land  surface  composition,  condition,  and  cover
types,  consequently  disrupting  ecosystem  functioning  such  as  biodi-
versity (Martínez-Ramos et al., 2016), productivity (Peters et al., 2013),

carbon storage (Liang et al., 2014; Seidl et al., 2014). Land disturbances
include natural hazards such as wildfire, flooding, tornado, and a variety
of land-use shifts led by anthropogenic activities (Thornton et al., 2024;
Zhu et al., 2020). There is a pressing need for mapping land disturbance
events  in  a  timely  manner,  which  will  hold  great  relevance  for  miti-
gating their social and ecological impacts (Verbesselt et al., 2012) and
delivering emergency aid to protect lives and infrastructure (Field et al.,
2012).

A large-scale Near Real-Time (NRT) monitoring of land disturbances

* Corresponding author.

E-mail address: remotesensingsuy@gmail.com (S. Ye).

https://doi.org/10.1016/j.rse.2024.114071
Received 24 October 2023; Received in revised form 20 January 2024; Accepted 18 February 2024

RemoteSensingofEnvironment305(2024)1140710034-4257/©2024ElsevierInc.Allrightsreserved.S. Ye et al.

has been long limited by a lack of timely satellite data acquisition until
multiple global  datasets became  publicly  available with reduced data
latency and improved delivery service (Woodcock et al., 2008; Wulder
et al., 2018). Earlier satellite-based NRT works were mainly based on
coarse-resolution  optical images  such  as  the  MODIS products,  DETER
project (Shimabukuro et al., 2006), the BFAST-monitor tool (Verbesselt
et  al.,  2012),  and  later  extended  to  the  medium-resolution  dataset
owning to the free access policy of Landsat datasets, such as the Global
Land  Analysis  and  Discovery  (GLAD)  alerting  system  (Hansen  et  al.,
2016), the Geobosques platform (Vargas et al., 2019) and Continuous
Change Detection and Classification (CCDC)-adapted approaches (Pas-
quarella et al., 2017; Ye et al., 2021b). The recent NRT studies incor-
porate the Synthetic Aperture Radar (SAR) dataset (Bullock et al., 2022;
Doblas et al., 2022; Eckerstorfer et al., 2019; Martinis et al., 2018) and 3-
m daily PlanetScope data (Francini et al., 2020), further reducing the
observation lag by incorporating more frequent acquisition of satellite
observations. On the other hand, some advanced approaches combined
multiple  sensors  to  shorten  the  time  interval  for  collecting  temporal
observations (Reiche et al., 2018; Shang et al., 2022; Tang et al., 2023).
For example, Shang et al. (2022) used the Harmonized Landsat Sentinel-
2  (HLS)  dataset  which  combines  four  satellite  sensors  (Landsat  8,
Landsat 9, Sentinel-2A, and Sentinel-2B) and successfully decreased the
confirmation latency of a land disturbance to 35 days.

Despite various input dataset types, NRT disturbance algorithms are
generally categorized into two broad groups: the cover-based and the
anomaly-based approaches. The cover-based approach was built on the
land cover classification and cover category change (or called land cover
conversion) (Andela et al., 2022; Diniz et al., 2015; Francini et al., 2020;
Giglio et al., 2009; Hansen et al., 2016; Reiche et al., 2018, 2021; Vargas
et al., 2019). This approach, typically the Global Land Analysis & Dis-
covery  (GLAD)  Alert  system  (Hansen  et  al.,  2016),  constructs  a  land-
cover  classification  model  based  on  historical  or  empirically  selected
samples, then applies the model to classify each newly collected image
and to detect new disturbance pixels if these pixels have been consis-
tently classified as altered land cover categories. The recent emerging
studies for NRT land cover mapping (Brown et al., 2022; Yu et al., 2022)
could be potentially leveraged for cover-based land disturbance moni-
toring as well. The cover-based approach often requires an additional
step for reducing data noise and normalizing input images (Reiche et al.,
2018, 2021) or simply assumes no seasonality for their targeted cover
(Hansen et al., 2016). If a disturbance only induces within-type surface
change (or named as cover condition change), such as insect disturbance
and  drought,  the  cover-based  approach  might  fail  to  alert  the  distur-
bance.  Some advanced cover-based methods  generated soft classifica-
tion outputs as a proxy, such as cover probabilities (Reiche et al., 2018,
2021) or cover fractions (Vargas et al., 2019), with an aim to address
subtle change as a “continuous” variable (e.g., forest loss). Nevertheless,
these methods were only successful in a relatively simple scenario for a
two-category classification scheme (e.g., forest vs. non-forest) so far.

The  anomaly-based  approach  detects  early  disturbance  signals  by
discriminating recent spectral anomalies from time-series dataset (Ols-
son et al., 2016; Pasquarella et al., 2017; Shang et al., 2022; Tang et al.,
2019;  Verbesselt  et  al.,  2012;  Ye  et  al.,  2021a).  The  anomaly-based
approach  was  often  achieved  without  the  necessity  of  tackling  land
cover information. This approach first builds a spectral baseline model
by fitting historical time-series datasets from a stable period, and then
continuously examines if the newly collected satellite observation rea-
ches a spectral difference over a predefined threshold against its pre-
dicted reflectance. The new disturbance event will be confirmed if the
minimum number of consecutive anomalies (namely “peek window”) is
satisfied. The anomaly-based approach could exclude such noises as data
seasonality and other natural variations by incorporating cyclic trends
and  long-term  trends  into  the  baseline  model.  Also,  benefiting  from
directly detecting change magnitudes, the anomaly-based approach is
capable of detecting subtle disturbances that do not directly alter land
cover types (Yang et al., 2022; Ye et al., 2021b).

Most cover-based or anomaly-based techniques require collecting a
minimum  number of consecutive  observations (conse)  for disturbance
confirmation  (e.g.,  conse = 6  in  most  CCDC-like  approaches),  as  the
temporal  stability of  a disturbance  signal aids  its differentiation  from
noisy signals. The setting of conse is practically controlled by the user
through algorithm configuration (Bullock et al., 2022). Arguably, it is
common  to  employ  less-than-required  satellite  observations  for  early
disturbance  alerting  (Shang  et  al.,  2022;  Ye  et  al.,  2021a),  yet  fewer
post-disturbance observations for decision-making come at the cost of
substantially increased commission errors. For example, Bullock et al.
(2022)  showcased  over  80%  commission  errors  in  the  initial  50  days
since  the  disturbance  occurrence  date  based  on  the  sample-based
agreement;  likewise,  Shang  et  al.  (2022)  reported  over  80%  commis-
sion errors when only one or two anomaly observations were identified.
This  was  because  these  techniques  discriminated  disturbance  signals
only relying on their relatively higher overall change magnitudes. When
the  post-disturbance  data  collection  is  short,  the  anomalies  are  more
likely  attributed  to  ephemeral  and  noisy  signals  (e.g.,  phenological
variation, short-term weather extremes, and even data noise), thereby
compromising the detection accuracy. Consequently, a long collection of
post-disturbance observations is still a must for most operational man-
agement tasks, if an NRT disturbance map with an acceptable commis-
sion rate is expected.

This  study  aims  to  develop  a  new  supervised  anomaly-based
approach  to  reduce  detection  latency  and  at  the  same  time  enhance
the detection accuracy. The new approach was inspired by Retrospective
Chart Review (RCR), a popular type of medical research design in which
pre-recorded,  patient-centered  datasets  are  used  to  examine  clinical
characteristics  (Gill  and  Kaplan,  2021;  Kaji  et  al.,  2014;  Vassar  and
Matthew,  2013). One  notable advantage  of RCR  is that it  is easier to
access conditions where there is a long latency from the initial exposure
and  the  patient’s  diagnosis  (Hess,  2004)  so  that  the  early  symptoms
could be retrospectively identified. The valuable information gathered
from  RCR  could  be  further  applied  to  guide  subsequent  prospective
studies. Similarly, the recent availability of numerous land cover data-
sets  and  disturbance  products  (Chuvieco  et  al.,  2019;  Johnson  and
Wittwer,  2008;  Latifovic  et  al., 2016;  Rollins,  2009)  as  well  as  freely
accessed historical satellite images have enabled us to gain insights into
early disturbance signals of a disturbance event whose occurrence might
be confirmed a lot later. Specifically, we are allowed to design methods
to effectively extract its early-stage spectral and temporal features from
historical time series, which can be further leveraged to construct ma-
chine  learning  models.  With  enhanced  model  specificity  and  better
capability  to  differentiate  noise  guided  by  well-recorded  disturbance
event information, it is expected that retrospective disturbance analysis
will improve both timeliness and accuracy against the current anomaly-
based approaches dominated by empirical thresholding. To our knowl-
edge,  historical  datasets  and  analyses  have  not  been  systematically
explored yet for the NRT disturbance mapping tasks. It is still unclear
what disturbance predictors are extracted from satellite time series and
how disturbance models are constructed for monitoring a variety of land
disturbances at their different lag stages.

1.2. Lag components

For  this  study,  the  monitoring  latency  is  viewed  as  an  intricacy
impacted  by  five  lag  components,  i.e.,  observation,  data,  sensitivity,
confirmation, and production lag, from input, algorithm, and produc-
tion  perspectives  (Fig.  1).  Assessing  different  proportions  of  lag  com-
ponents can provide potential treatments for accelerating disturbance
alerting. Note that compared to Fig. 1 of Bullock et al. (2022), the as-
sessments of sensitivity and production lags are newly proposed for this
study.

The input latency is mainly affected by observation and data lags. An
observation  lag  refers  to  the  time  interval  between  the  disturbance
occurrence  and  when  the  sensor  collects  the  first  clear  observation,

RemoteSensingofEnvironment305(2024)1140712S. Ye et al.

Fig. 1. Graphic explanations for the actual latency from an operational NRT disturbance task which is controlled by five lag components, i.e., observation, data,
sensitivity, confirmation, and production lag. Sensitivity and confirmation lag are newly proposed for this study, compared to the work done by Bullock et al. (2022).

which is often related to a satellite revisiting cycle and weather condi-
tions; a data lag is the delay between the first clear observation collec-
tion and this observation being preprocessed to a standard reflectance
product ready for analytics, which is often systematic and shorter than
one week (Bullock et al., 2022).

Algorithmic  latency  includes  sensitivity  and  confirmation  lags.  A
sensitivity lag refers to the day interval between the date for the first
available data product and the date for an algorithm first alerting this
disturbance. A sensitivity lag occurs where the disturbance signals are
spectrally unobvious at the first observations (e.g., insect disturbances,
selective  logging),  ranging  from  zero  day  (i.e.,  the  quickest  alert)  for
those  dramatic  disturbances,  to  infinity  when  the  algorithm  or  the
sensor  is  incapable  of  detecting  the  signal.  A  confirmation  lag,  also
named “algorithm latency” by Bullock et al. (2022), is a lag between the
first alert and the disturbance confirmation.

Lastly,  a  production  lag  is  the  operational  delay  caused  by  map
production and delivery, closely linked to the platform updating inter-
val. The production lag was not well discussed yet in past studies. For

each processing, an NRT platform will ingest the new images released,
map the latest disturbance, and publish the NRT product. These steps are
computationally expensive and time-consuming. Particularly for a large-
area monitoring system, it is often practically unfeasible to make a daily
update,  resulting  in  a  production  lag  brought  by  the  pre-defined
updating day interval.

The  remainder  of  the  paper  will  be  organized  as  follows:  we  first
introduce the study area and dataset used for this research (Section 2),
then describe the design of an operational NRT system (Section 3); we
will  thoroughly  compare  the  latency  and  accuracy  of  the  system
adopting supervised against the unsupervised anomaly-based approach
(Section 4.1), report their lag component assessment (Section 4.2), and
exhibit distinction of latency curves and lag components from different
disturbance events (Section 4.3); finally, we will discuss the comparative
performance against other existing NRT methods as well as the limita-
tions (Section 5).

Fig. 2. Five selected sites for NRT monitoring of land disturbance events for 2022 in this study. For each event, four adjacent HLS tiles were used for the test.

RemoteSensingofEnvironment305(2024)1140713S. Ye et al.

2. Study area and dataset

2.1. Study area

We  chose  the  five  most  influential  disturbance  events  across  the
Conterminous United States (CONUS) in 2022, including three natural
disasters,  one  forest  insect  infestation,  and  one  human-induced  land
surface modification (Fig. 2).

Mosquito fire:
Mosquito  fire  was  the  largest  wildfire  in  California  occurring  in
2022. The massive fire began on September 6 and was 90% contained on
October 4, burning a total area of 31,075 ha, mostly in forested regions
of  El  Dorado  and  Placer  counties;  more  than  half  of  the  fire  regions
(58%) experienced low soil burning severity (Teater, 2023). A total of
11,117  people  were  evacuated,  and  5848  houses  were  threatened  or
damaged (Teater, 2023).

Spongy moth:
The spongy moth, formerly known as  the gypsy moth, has been a
major forest disturbance type in New England since 2015 (Pasquarella
et  al.,  2017).  Sponge  moth  caterpillars  hatch  from  egg  mass  in  early
May, begin feeding on the leaves of hardwood trees since early June, and
reach peak defoliation by late June or early July as the larvae mature
(Pasquarella et al., 2017). Sponge moth defoliation is an ephemeral and
cyclic disturbance that occurs repeatedly every year in New England:
trees often re-foliate from spongy moth attacks in the summer, although
moth-induced repeated defoliation combined with other stressors may
lead to a long-term decline in forest health.

Hurricane Ian:
Hurricane  Ian,  which  happened  in  September  of  2022,  was  the
deadliest hurricane to strike Florida since 1935. It peaked as a Category
5 hurricane with 260 km/h winds on September 28 when attacking the
west  coast  of  Florida  (Karimiziarani  and  Moradkhani,  2023),  causing
major inland flooding and landfall in counties such as Lee and Charlotte.
The  hurricane  killed  149  people  across  Florida  and  produced  cata-
strophic damage with an estimated loss of 113 billion (NOAA National
Centers,  2023),  including  extensive  tree  and  building  damage  due  to
strong wind and floods.
Kentucky flooding:
Between July 26 and July 30, 2022, due to sustained record-breaking
rainfall, several devastating floods hit 15 counties in East Kentucky, such
as Hidman, Perry, and Prestonsburg counties. The floods resulted in the
death  of  45  people  and  displaced  thousands  more.  Entire  homes  and
some communities were swept away by flood water, causing extensive
damage to thousands of buildings, vehicles, and other infrastructures in
the  flooded  region,  with  an  estimated  cost  of  over  1.5  billion  dollars
(NOAA National Centers, 2023).

Construction:
Texas has been one of the hotspots for construction projects in the
past decade. Due to the lower cost of living and taxes, Texas, particularly
Austin and Houston, has become a big draw to businesses and companies
relocating from California and elsewhere. For example, Samsung started
construction on a semiconductor manufacturing campus in the suburbs
of Austin in 2022. Austin City ranked No.1 in the United States for the
housing demand in 2022 with numerous construction sites for real estate
developments (Salviati and Warnock, 2023), thereby being selected as
the testing site for studying construction events.

2.2. Datasets

greatly reduced data lag. Therefore, the HLS datasets were selected as
the time series inputs for this study. Each HLS tile has 3660 rows and
3660 columns with 30 m of pixel spacing in both directions, provided
over projected map coordinates aligned with the Military Grid Reference
System (MGRS). For each disturbance event, we chose four adjacent HLS
tiles  (2  by  2)  for  the  NRT  monitoring  and  the  accuracy  assessments
(Table 1), and a total of 20 tiles were used for the study. For each tile, we
downloaded all harmonized surface reflectance products from 2015 to
2021  for  the  retrospective  analysis;  during  the  later  NRT  monitoring
phase, we downloaded the HLS images of 2022 in an increment of one
week which is the predefined production interval for our test.

Besides, we collected four open-access annual CONUS disturbance
products  from  2016  to  2020,  which  were  used  for  labeling  historical
anomalies. They are 1) land cover transition map generated by differ-
encing Land Change Monitoring, Assessment, and Projection (LCMAP)
Primary  Land  Cover  maps  (Xian  et  al.,  2022)  between  two  neighbor
years; 2) LANDFIRE Disturbance Products (Ryan and Opperman, 2013);
3) Landsat Collection 1 Level-3 Burned Area Science Product (Hawbaker
et al., 2020); and 4) Aerial Detection Survey (ADS) insect activity dataset
which records polygonal forest health information generated by sketch
mapping (Johnson and Wittwer, 2008). All these products, except for
ADS insect dataset, are originally available at 30-m resolution. We ras-
terized the ADS dataset to 30-m binary maps (insect vs no-insect regions)
to keep aligned with the HLS satellite images.

The validation pixels were sampled by applying a stratified sampling
approach on the accumulated NRT land disturbance maps generated by
the supervised approach. The accumulated NRT maps were made from
merging all NRT detection maps within the assessment window for each
disturbance; the assessment window is defined as the disturbance period
with an extension of 15 days after a disturbance ends to take account of
most  delayed  detections.  We  randomly  sampled  300  pixels  from  the
“disturbance”  and  “no  disturbance”  regions,  respectively,  in  each
accumulated NRT map (600 samples for an event), forming 3000 sam-
ples in total for five disturbance events. For the response design, three
experienced  remote  sensing  experts  interpreted  the  reference  distur-
bance date for each sample pixel as the first date for their identifying
visible disturbance signals from Planet Explorer (https://www.planet.
com/explorer/). The Planet Explorer provides free access to 3-m daily
Planet  images.  As  such,  we  were  capable  of  determining  the  actual
disturbance date for the reference sample pixel, which was more accu-
rate than interpreting the first anomaly date from the time series (Shang
et al., 2022; Ye et al., 2021a, 2023) or using the date right in-between
the  first  anomaly  and  the  last  pre-disturbance  observation  date
(Bullock et al., 2022; Reiche et al., 2018). While the occasional cloud/
shadow  contamination  or  missing  datasets  in  PlanetScope  still  might
cause an inaccurate interpretation of the exact disturbance date, such
impacts  were  negligible  because  1)  PlanetScope  images  provided  the

Table 1
Location, disturbance periods, and selected HLS tiles for the disturbance events
to be tested for this study.

Impacted Region  HLS Tile IDs

Disturbance
Event

Mosquito fire

Spongy moth

Central
California
New England

Disturbance Period
(2022)

Sep. 6 – Oct. 22

Jun. 1 – Jul. 15

Sep. 26 – Sep. 28

Jul. 26 – Jul. 30

Feb. 15 – Jun. 15

10SFH, 10SFJ,
10SGH, 10SGJ
18TXM,
18TXN,
18TYM,
18TYN
17RLK, 17RLL,
17RMK,
17RML
17SKB, 17SKC,
17SLB, 17SLC
14RNU,
14RNV,
14RPU, 14RPV

Harmonized Landsat Sentinel-2 (HLS) dataset combines four satellite
sensors (Landsat 8, Landsat 9, Sentinel-2A, and Sentinel-2B satellites),
providing the highest temporal resolution of 2–3 days (Claverie et al.,
2018)  among  all  medium-resolution  (10–30  m)  satellite  datasets.
Notably, for the latest version of the HLS dataset (version 2.0), the Land
Processes Distributed Active Archive Center approximately takes only
two days of data lag to release the surface reflectance products, with

Hurricane Ian

Southwest
Florida

Kentucky flood

Construction

Eastern
Kentucky
Central Texas

RemoteSensingofEnvironment305(2024)1140714S. Ye et al.

densest optical images as daily observations; 2) the beginning dates for
some disturbance events (such as Hurricane Ian and Mosquito Fire) were
well  recorded  and  ascertained  so  that  the  recorded  disturbance  dates
could be directly adopted. The labeling process with PlanetScope images
was showcased in Section S1 of the supplementary material.

3. Methodology

A two-phase workflow was designed for this new approach (Fig. 3).
For the first phase “retrospective disturbance analysis”, we applied an
“over-detection” for time-series breakpoints from historical time series
to generate a comprehensive sample pool respectively for disturbance or
non-disturbance  anomalies,  under  the  guidance  of  the  disturbance
products; then we developed a specific sample set and built a machine-
learning model for each disturbance stage. For the second phase “Near
Real-time  Monitoring”,  we  implemented  a  NRT  disturbance  mapping
based  on  these  stage-based  disturbance  models  incrementally  with  a
step of one week for the year 2022, i.e., the system updating interval was
one week.

3.1. Phase 1: retrospective disturbance analysis

3.1.1. Anomaly generation

We first applied time-series-based breakpoint detection to generate
anomalies from historical HLS datasets (2015–2021) on a per-tile basis.
For  each  HLS  tile  to  be  monitored,  Stochastic  Continuous  Change
Detection  (S-CCD)  (Ye  et  al.,  2021a),  a  near  real-time  adaptation  of
Continuous  Change  Detection  and  Classification  (CCDC)  (Zhu  and
Woodcock,  2014),  was  applied.  S-CCD  incorporates  the  Kalman  filter
into the CCDC algorithm and recursively updates the anomaly records
(see Table S1 in the supplementary), instead of reconstructing the model
from scratch when new observations are available (Ye et al., 2021a). The
short-memory  nature  of  S-CCD  saves  disk  space  from  removing  the
historical images and speeds up the computation by skipping the step of
refitting  a  time-series  model,  thereby  improving  model  efficiency,
especially for large-area NRT monitoring. An improvement we made on
Ye  et  al.  (2021a)  is  to  let  S-CCD  produce  spectral  anomalies,  besides
structural breakpoints, for the processing of historical datasets. Spectral

anomalies, for this study, refer to the spectral breakpoints within a time
series produced by break over-detection. They are related to either real
disturbance  signals  or  non-disturbance  factors  (e.g.,  phenology  shifts
and ecosystem recovery). There are two key parameters for controlling
the break detection sensitivity for CCDC-like algorithms: change prob-
ability  threshold  (chg_t)  defines  the  minimum  change  magnitude  to
identify a single breakpoint (the default chg_t is 0.99), and conse is the
minimum  number  of  temporally  consecutive  anomalies  required  to
confirm a breakpoint (the default conse is 6). We used a lower change
probability threshold of 0.90 and a shorter conse as three observations,
ensuring  the  inclusion  of  the  most  subtle  disturbance  pixels  (Cohen
et al., 2017) as well as a variety of non-disturbance anomalies. Different
from the normal CCDC’s way of handling breakpoints, the S-CCD algo-
rithm  will  skip  the  model  initialization  but  only  update  the  current
anomaly record (see Table S1), considering that the Kalman filter can
self-adjust model coefficients for local fluctuations (Ye et al., 2021a).

Structural breakpoints refer to another type of breakpoints that leads
to an obvious structural change of the time series, where it is essential to
refit a new harmonic curve by using new observations of at least one
year  to  guarantee  the  model  predictability  (Zhu  et  al.,  2020).  We
adopted  a  more  conservative  parameter  set  to  generate  structural
breakpoints, chg_t = 0.9999, conse = 8. When the last observation of a
historical time series was processed, the anomaly records, which rep-
resented the current spectral status, were saved out to the disk for the
second phase (Fig. 3).

3.1.2. Anomaly labeling

We  combined  two  sources  of  disturbance  maps,  respectively  from
anomaly  generation  and  historical  disturbance  products,  to  develop
high-confidence spectral anomaly pools. An anomaly-based disturbance
map  was  produced  from  anomaly  records  based  on  the  disturbance-
extraction  strategy  proposed  in  Section  3.3.6  by  Zhu  et  al.  (2020).
This  post-processing  excluded  “greener”  breakpoints  identified  as
increased NIR, decreased Red and SWIR1 bands:

ΔRed < 0.02&ΔNIR > (cid:0) 0.02&ΔSWIR1 < 0.02

(1)

Where ΔRed, ΔNIR, and ΔSWIR1 are the spectral change magnitudes
of  the  RED,  NIR,  and  SWIR1  bands  for  the  breakpoint.  On  the  other

Fig. 3. A two-phase workflow of the supervised near real-time monitoring approach proposed for this study. For Phase 1, eight stage-based models were built for
each center tile using anomaly samples from a 3 by 3 moving window of neighbor tiles; the samples were labeled by combining historical disturbance datasets and
breakpoint  detection  from  the  HLS  time  series  (2015–2021).  For  Phase  2,  the  NRT  monitoring  was  implemented  using  the  stage-based  retrospective  models
incrementally for each week of 2022.

RemoteSensingofEnvironment305(2024)1140715S. Ye et al.

hand, we generated an annual product-based disturbance potential map
(2016–2020)  by  fusing  four  previously  mentioned  open  disturbance
products: the pixels were labeled as “disturbance” if this pixel fell within
the  disturbance  regions in  at least one  open disturbance  product. We
extracted  the  high-confidence  disturbance pixels  from  the overlapped
disturbance  regions  between  anomaly-based  and  product-based  maps
into a disturbance anomaly pool. Those pixels labeled as “disturbance”
only  in  anomaly-based  maps  were  spectral  anomalies  not  covered  by
historical disturbance regions, thereby representing noisy signals, so we
sort them into a non-disturbance anomaly pool.

For each HLS tile, we generated and labeled spectral anomalies on an
annual basis, and then combined labeled spectral anomalies from a 3 by
3 HLS tile window centered at the targeted tile (Brown et al., 2019) with
a temporal length of the middle five years (2016–2020, see “Phase 1” in
Fig. 3). We excluded the year 2015 and 2021 as the S-CCD might suffer
inaccuracies for detecting breakpoints at the starting and the ending of a
time series. There are two primary motivations for the 3 by 3 spatio-
temporal tile window design: 1) the machine learning model could be
developed  with  a  better  generalization  for  dealing  with  disturbance
variability using sample acquisition from a larger spatial extent and a
longer disturbance history; 2) 3 by 3 tile window considerably decreases
variation  of  local  models  between  two  neighborhood  tiles,  avoiding
artifacts on the boundaries of the two tiles (Brown et al., 2019).

3.1.3. Predictor extraction

We  extracted  17  disturbance-related  predictors  from  the  S-CCD
model  outputs  (not  from  the  disturbance  products),  which  could  be
categorized into the disturbance-process and the pre-disturbance group.
Fig.  4  illustrates  these  disturbance-related  predictors  using  a  sample
time series. Six HLS spectral bands, i.e., blue, green, red, NIR, SWIR1,
and  SWIR2 bands,  were  considered. We  retained  the  three  predictors
used in the COntinuous monitoring of Land Disturbance (COLD) algo-
rithm (Zhu et al., 2020) for the disturbance-related breakpoint decision,
i.e.,  1)  multispectral  change  magnitudes  to  take  account  of  spectral
change direction, 2) normalized change intensity, and 3) spectral con-
sistency  angle.  Besides,  we  also  included  4)  the  disturbance  date  to
incorporate seasonality, 5) the span of anomaly days for data temporal
density, and 6) multispectral pre-change reflectance to depict land-cover
spectral  features  prior  to  spectral  anomalies  being  detected.  The  for-
mulas for these predictors are given in Table 2.

3.1.4. Model construction

To  enhance  model  specificity  for  different  disturbance  stages,  we
individually established one sample set and one disturbance model for
each  consecutive  anomaly  number  condition  (nanom = 1, 2, 3, …, 8,
Fig. 5). Zhu et al. (2016) suggested a total of 20,000 samples for the
Landsat-based classification, and an HLS image (3660 * 3660) occupies
only a half of the total pixel number of the Landsat scene (5000 * 5000),
so  a  total number  of 10,000  training samples was  selected to  build  a
series  of  stage-based  models  for  each  tile.  To  evenly  distribute  these
10,000 samples across the sample years, we allocated 2000 samples for
each tile in each year, so for a center tile, a total of 90,000 samples (9
tiles  *  5  years  *  2000  samples)  were  used  to  build  each  stage-based
model  (see  Fig.  3).  A  proportional  random  sampling  was  chosen
because it has shown superiority over a balanced sampling for a classi-
fication scheme (Brown et al., 2019; Zhu et al., 2016). However, there
are far fewer disturbance anomalies compared to the non-disturbance
anomalies  in  practice,  causing  the  disturbance  category  to  be  easily
under-represented.  The  trickier  is  that  the  omission  and  commission
error  rates  are  often  both  increased  at  a  similar  degree  for  the  early
disturbance  stage  due  to  too  many  noisy  signals.  But  we  expected  to
suppress omission errors so that the potentially disturbed regions were
comprehensively provided for the possible subsequent high-resolution
damage mapping. As such, we designed a linear function with a nega-
tive  slope  to  control  disturbance  sample  proportion,  which  enabled
assigning a higher sample proportion to the disturbance category for the
shorter  nanom  (i.e.,  the  earlier  disturbance  stage).  For  each  nanom,  the
sample proportions are denoted as:

Pdist(nanom) = Pbase + (conse (cid:0) nanom)*slope

Pnondist(nanom) = 1 (cid:0) Pdist(nanom)

(2)

(3)

Where  Pdist(nanom) and  Pnondist(nanom) are  the  proportions  of  distur-
bance and non-disturbance categories for each nanom; conse is the con-
stant,  the  number  of  consecutive  anomaly  observations  to  detect  a
structural breakpoint (conse = 8); Pbase  is the baseline proportion when
the  nanom  reaches  the  maximum,  and  the  parameter  slope  controls
decreasing impacts of nanom  on Pdist. The parameter sensitivity test (see
Section S3 of the supplementary material) revealed that Pbase = 0.1 and
slope = 0.02 was the only group that keeps an acceptable overall accu-
racy while maintaining a low omission rate across all nanom.

For each nanom  (i.e., 1, 2, 3, …, 8), we trained a random-forest model
(ntrees = 100) for the binary classification scheme (disturbance vs. no

Fig. 4. Graphic illustration of the disturbance-related predictors used for this study (“n” means the number of variables).

RemoteSensingofEnvironment305(2024)1140716S. Ye et al.

Table 2
Definition of 17 predictors used for the NRT disturbance prediction.

Predictor name

Description

Number

Category

1. Multispectral change Magnitudes

2. Normalized change magnitude

3. Spectral consistency angle

4. Disturbance date

5. Anomaly span
6. Multispectral pre-disturbance reflectance

CMi = ρi,dist dat

CMnormalized =

(cid:0) ̂ρi,dist dat, i = 1, 2, 3, 4, 5, 6
)
∑
2
5
i=1

(

CMi
RMSEi

∑

n(cid:0) 1
j=1

βj,j+1
)

angle = 1
n (cid:0) 1
(
sindoy = sin

doydist dat

2π
T
2π
T
ndays = lastdist dat (cid:0) dist dat

(
cosdoy = cos

doydist dat

,
)

̂ρi,dist dat = a0,i +

∑
3
k=1

(cid:0)

ak,icos

)

(

x

+ bk,isin

2π
T

) )

x

+ c1,ix, i = 1, 2, 3, 4, 5, 6

(cid:0) 2π
T

6

1

1

2

1
6

Disturbance process

Pre-disturbance

Note: CMi  and RMSEi  are the individual change magnitude and Root Mean Square Error of the ith band; ρi,dist dat  and  ̂ρi,dist dat  are the actual and the predicted
reflectance of the ith band; n is the current consecutive anomaly number; βj,j+1  is the change-vector angle from jth to j + 1th anomaly; lastdist dat and dist dat are the
last disturbance date observed as a spectral anomaly and the disturbance starting date respectively; doy  is the date of the year; a0,i, ak,i, bk,i  and c1,i  are the harmonic
coefficients for the ith band; k is the temporal frequency of the harmonic components.

Fig. 5. Explanation for developing stage-based sample sets and disturbance models. The disturbance stages were characterized by the number of current consecutive
anomalies  (nanom).  We  used  the  stage-specific  sample  proportion,  Pdist(nanom) and  Pnondist (nanom),  to  make  samples  and  then  developed  a  machine-learning  model
individually for each stage.

disturbances)  using  each  corresponding  sample  set.  Hence,  a  total  of
eight  stage-based  retrospective  models  were  prepared  for  the  second
phase.

3.2. Stage 2: near real-time monitoring

Starting from January 1st, 2022, we iterated a workflow of near real-
time monitoring to process the newly collected images until the end of
2022. The workflow was operated incrementally at a step of one week.
The workflow ingested new images collected for each week, updated the
NRT anomaly records, and then extracted 17 disturbance-related pre-
dictors listed in Table 2. We tested and compared two ways for gener-
ating  disturbance  probability:  (1)  the  proposed  method  based  on  the
retrospective models (called supervised) and (2) the traditional anomaly
method based on an empirical change-magnitude threshold (called un-
supervised).  For  the  supervised  probability,  we  first  used  the  change
probability threshold of 0.9 to detect anomalies for each pixel (the same

chg_t  for  “anomaly  generation”  in Phase  2).  Then, 17  predictors  were
generated for each outputted anomaly. Finally, we input the predictors
into the corresponding stage-based model based on the current nanom,
and produced its NRT random-forest disturbance probability at a per-
pixel  level.  We  assigned  the  disturbance  probability  as  “0”  for  those
pixels without anomalies being detected. The unsupervised probability
applied the change probability threshold of 0.99 to detect disturbance
breakpoints, followed by eliminating the breakpoints attributed to the
greener trend using the rule of Eq. (1). The threshold as 0.99 is the most
commonly used change threshold for the CCDC-like approach, which,
for example, was adopted in the “Land Change Monitoring, Assessment,
and Projection”  project (Brown et al., 2019). We computed the unsu-
pervised  probability  as  the  ratio  of  the  current  consecutive  anomaly
number by the maximum anomaly number (conse = 8). For example, if
there  are  six  anomalies  at  the  end  of  the  current  time  series,  the
disturbance probability is 6 / 8 = 75%.

To  generate  spatially  complete  disturbance  patches  (i.e.,  a

RemoteSensingofEnvironment305(2024)1140717S. Ye et al.

continuous region affected by the change process), the Flood Fill algo-
rithm  was  first  applied  to  the  two  disturbance  probability  layers  (Ye
et al., 2023). Flood Fill is an algorithm to identify adjacent pixels as an
object in an image based on their similarity to an initial seed pixel (Van
der  Walt  et  al.,  2014).  The  Flood  Fill  algorithm  outperformed  other
segmentation algorithms such as SLIC and watershed in our previous test
(Ye et al., 2023), and hence was chosen for this study. For the supervised
probability layer, we retained the disturbance regions as the disturbance
patches  with  an  average  disturbance  probability  >50%;  for  the
unsupervised-probability layer, we labeled the patches as their average
probability ≥ 12.5%, so that the disturbance identification was possible
even when one anomaly observation was captured, as consistently as the
supervised-probability approach.

Finally, the identified disturbance patches were categorized into two
levels  of  the  NRT  products  based  on  the  current  patch-level  anomaly
number. We assigned the disturbance patches with an average of less
than  six  consecutive  anomalies  into  “detection  level”,  and  otherwise
“confirmation  level”.  We  used  the  confirmation  threshold  as  six
consecutive anomalies, considering most CCDC-like algorithms use six
observations as the minimum required anomaly number (Brown et al.,
2019;  Ye  et  al.,  2021a;  Zhu  et  al.,  2020).  When  one  workflow  was
completed for a monitoring interval, we saved two levels of the distur-
bance products with the disturbance attributes into the database. The
polygon-based attributes include the first anomaly date, the last anom-
aly date, and the production date (we set it as the last day of each week).
As our experiments were performed in early 2023, all HLS datasets for
2022 have been available for downloading, and hence the data lag was
zero. To keep close to the real latency for the operational monitoring, we
manually set the data lag as two days of HLS data lag and added it to all
production dates. The two-day data lag is the estimated average time
required  by  NASA  LP  DAAC  to  release  HLS2.0  surface  reflectance
products since their first collection, based on the user experience from
our NRT platform downloading over 90,000 HLS 2.0 images. It is worth
mentioning  that  our  comparative  evaluation  mainly  focused  on  the
detection-level products, though both the detection- and confirmation-
level  results were assessed  and reported. This  was because the detec-
tion level was practically more relevant for an NRT platform owing to its
enabling timelier monitoring (<10 days) and providing important po-
tential  disturbance  maps  for  further  high-resolution  applications.  We
developed an operational platform to update and to visualize the NRT
results  for  each  week  based  on  the  Google  Earth  Engine  platform
(https://gers.users.earthengine.app/view/nrt-conus).

3.3. Accuracy and latency assessment

We will use the sigmoid framework proposed by Bullock et al. (2022)
to comparatively assess the unsupervised and supervised approach. The
sigmoid  framework  incorporates  both  omission  and  commission  of
disturbance alerts as a function of lag. Hence, it could lead to a more
comprehensive assessment than other NRT assessment metrics that only
focused  on  the  disturbance  cases  being  correctly  identified  (Bullock
et al., 2022), such as Mean Time Lag (MTL) (Reiche et al., 2018). In this
study, we defined the omission error at a certain lag as when a distur-
bance sample was not hit by the disturbance patches from the recent
NRT  results  and  defined  the  commission  error  as  when  a  non-
disturbance sample was included in one disturbance patch.

Following  the  sigmoid  framework,  we  will  graph  omission,  com-
mission, and F1  score as sigmoid curves for incremental values of the
total lag (i.e., production date minus disturbance date), allowing for a
thorough comparison of detection effectiveness at a full range of latency.
F1  score is a harmonic mean of inverse omission and commission error
rate:

the primary tool to assess “lag-accuracy” performance: the Initial Delay
and Level Off Point. The Initial Delay is assigned to the date that 2% of
the total disturbance pixels are detected, representing the shortest time
of an algorithm for beginning to alert a disturbance event. The Level Off
Point, the time when F1  score is just stabilized, is computed as the date
that has the maximum y  for a virtual curve from rotating 45 degrees
around the line connecting the beginning and end points of the sigmoid
curve (Bullock et al., 2022). The x coordinate of Level Off Point indi-
cated the shortest lag to reach the maximum F1  score, and the y coor-
dinate points to the maximum overall performance.

Moreover, we will assess the individual contribution of the five lag
sources  given  in  Fig.  1.  We  will  generate  individual  lags  for  each
disturbance sample following the definitions given in Table 3, and then
compute the mean statistics of each lag component. We will also report
Mean Time Lag (MTL) and Mean Time Lag for the First Alert (MTLf ) for
comparison to other existing studies. The sum of all the lag sources is
equivalent  to  MTL,  a  lag  metric  commonly  used  in  previous  studies
(Shang et al., 2022; Ye et al., 2021a). The sum of all except the confir-
mation lag is equal to as MTLf  (Reiche et al., 2018), which is the average
time between the reference disturbance date and the date for capturing
the first anomaly.

4. Results

4.1. Unsupervised vs. supervised

Fig. 6 shows the sigmoid curves for the unsupervised (the traditional
method based on a predefined threshold) and the supervised (the pro-
posed) NRT approach based upon all evaluation samples from the five
testing sites (n = 3000, 50% are disturbance samples). Table 4 lists their
key lag metrics. Generally, F1  score curves for the two approaches both
began to increase around the Initial Delay (Fig. 6A); with time going
forward, F1  was gradually rising because more post-disturbance obser-
vations became available both temporally and spatially, and eventually
plateaued at the Level Off Point (Fig. 6A). The sigmoid curves of the two
approaches were almost fully overlapped before their Initial Delay (2
days for the detection level, and ~ 21 days for the confirmation level),
and became divergent afterward: the F1  sigmoid curve of the supervised
approach  (“blue”)  became  consistently  higher  than  that  of  the  unsu-
pervised  approach  (“yellow”).  Particularly  at  the  detection  level,  the
supervised approach only took 15 days to reach the Level Off Point with
0.733  F1  score,  which  had  seven  days  quicker  and  almost  0.2  F1
improvement than the unsupervised (the unsupervised: 22 days, 0.546
F1 score, see Table 4). The detection-level comparison reflects their large
performance distinction for mapping disturbances at their early stage.
Differently, the unsupervised and supervised approaches presented the
same lag days to reach their Level Off Points for the confirmation level
(35 days),  because the two approaches both applied  conse = 6 hence
similar confirmation lag (as Section 4.2 will show) that dominates their

Table 3
Definition of lag types to be assessed for this study. MTL: Mean Time Lag; MTLf :
Mean Time Lag for the First Alert.

Lag types

Definition

Observation Lag

Data Lag
Sensitivity Lag

Confirmation

Lag

Production Lag

Day interval between the reference disturbance date and the first
clear observation date
Constant value as two days
Day interval between the first clear observation date and the first
anomaly date detected
Day interval between the first and the last anomaly date detected
for a peek window
Day interval between the last anomaly date and the date being
officially confirmed by the platform
The sum for observation lag, data lag, sensitivity lag,
confirmation lag, and production Lag
The sum for observation lag, data lag, sensitivity lag, and
production Lag

F1 = 2*

(1 (cid:0) omission)*(1 (cid:0) commission)
(2 (cid:0) omission (cid:0) comission)

(4)

MTL

MTLf

Two lag metrics generated from the sigmoid curves will be used as

RemoteSensingofEnvironment305(2024)1140718S. Ye et al.

Fig. 6. Comparison of the unsupervised and supervised approaches on sigmoid curves at detection and confirmation levels based on a total of 3000 evaluation
samples from the five disturbance sites. The omission error, commission error, and F1  score are respectively plotted as a function of total lag (the sum of five lag
components)  within  a  tolerance  window  of  0  to  90  days.  Two  key  latency  metrics,  Initial  Delay  and  Level  Off  Points,  are  marked  on  the  curves  as  “circle”
and “triangle”.

Table 4
Comparison of the unsupervised and supervised approaches on lag, omission error, commission error and F1  score at the Initial Delay and Level Off Point of their
sigmoid curves. The bold font highlights the lag/accuracy difference between the two approaches.

Detection Level

Initial Delay

Lags (Days)
2
2
Confirmation Level
Initial Delay
Lags (Days)
22
21

Omission Error
68.8%
63.9%

Omission Error
89.9%
98.0%

Unsupervised
Supervised

Unsupervised
Supervised

Level Off Point

Commission Error
63.5%
58.5%

Commission Error
8.7%
0.6%

F1
0.336
0.386

F1
0.182
0.040

Lags (Days)
22
15

Omission Error
46.4%
34.0%

Commission Error
44.4%
17.7%

Level Off Point
Lags (Days)
35
35

Omission Error
75.2%
71.2%

Commission Error
14.9%
8.1%

F1
0.546
0.733

F1
0.384
0.439

total lag at the confirmation level (~77% of the total lag, see Section
4.2). Reducing consecutive observations for confirmation is out of the
scope for this study and was often determined by user settings (Bullock
et al., 2022). However, the supervised approach still achieved a rela-
tively  better  F1  score  at  the  confirmation  level  (supervised  vs.  unsu-
pervised: 0.439 vs. 0.384).

By  investigating  the  error  components,  the  supervised  presented
consistently  lower  omission  (Fig.  6B)  and  commission  rates  (Fig.  6C)
than  the  unsupervised  approach  over  time  after  the  Initial  Delay.
Particularly,  the supervised achieved a much  lower commission error
rate than the unsupervised by approximately 27 percent points at the
detection level (17.7% vs. 44.4%, Table 4). This revealed that the pri-
mary advantage of incorporating historical datasets was in alleviating
overdetection.  Fig.  7  showcased  a  sample  pixel  under  the  effects  of
climate variability that was misclassified as “disturbance” by the unsu-
pervised approach. Its NIR time series experienced a noticeable increase
at the breakpoint (Fig. 7A), which was related to the earlier leaf-on date
for the year 2022 (Fig. 7B). The unsupervised approach identified the
breakpoint as “disturbance” because the overall change magnitude was
larger than the predefined threshold (the change probability of 0.99),

while the supervised correctly ignored it (Fig. 7C) through a compre-
hensive  examination  on  change  magnitudes,  pre-change  features,
change season, and change direction using the retrospective models.

Fig. 8 is an example to show that the supervised approach also could
suppress  omission  errors.  The  sample  pixel  was  experiencing  spongy
moth damage with a medium-level NDVI drop in June of 2022 (Fig. 8A
and B). Unless a structural breakpoint was detected so that the S-CCD
model entered its initialization stage, the supervised approach inspected
the  outputted  consecutive  spectral  anomalies  (if  any)  and  predicted
disturbance  probability  for  each  new  observation.  Therefore,  the  su-
pervised approach was capable of delineating subtle change induced by
spongy  moth  (Fig.  8C)  even  with  low  change  magnitudes,  as  long  as
most  pixels  within  the  associated  anomaly  patch  were  identified  as
disturbance pixels by the machine-learning model. However, the unsu-
pervised  approach  missed  most  damage  at  the  confirmation  level
(Fig. 8C) as the spectral curve was quickly recovered (Fig. 8A), causing
the change magnitude to be lower than the threshold of 0.99 change
probability.

Comparing the detection and confirmation levels, the accuracies at
the detection level were higher than at the confirmation level for both

RemoteSensingofEnvironment305(2024)1140719S. Ye et al.

Fig. 7. An example site ((cid:0) 97.947, 30.339) for commission errors produced by the unsupervised approach. The HLS time series (A) shows a structural breakpoint
induced by increasing NIR which was possibly related to phenological shifts, while no obvious disturbance signal was found from inspecting the HLS images (B). The
supervised  approach  exhibited  superiority  in  suppressing  such  over-detection  by  modeling  disturbance  and  non-disturbance  anomalies  using  the  retrospective
datasets (C).

approaches.  This  finding  was  contrary  to  most  past  NRT  studies,  in
which the confirmation results achieved the better overall accuracies as
only enough consecutive anomalies could effectively exclude commis-
sion  errors.  The  outstanding  performance  for  the  detection  level  was
mainly  attributable  to  its  considerably  lower  omission  errors  (e.g.,
detection vs. confirmation = 34.0% vs. 71.2% for the supervised at its
Level  Off  Point).  Notably,  the  detection  level  was  advantageous  for
capturing the ephemeral disturbances (e.g., Hurricane Ian and Spongy
Moth) whose effects only lasted for one or two observations. As two out
of five study sites were ephemeral disturbances (344 / 830 disturbance
cases), the validation samples for this disturbance type might be over-
represented  for  this  study,  resulting  in  an  overestimation  of  the
detection-level  accuracy.  Note  that  the  unrealistic  sample  proportion
only  distorted  the  relative  accuracy  between  the  detection  and  the
confirmation  level  but  yielded  little  statistical  effects  on  comparative
performance  between  the  unsupervised  and  supervised  approaches.
Another  distinction between  the  detection and  the confirmation level
was  that  the  confirmation  level  required  a  much  longer  lag  to  reach
Initial Delay (22/21 days vs. 2 days) and Level Off Point (35 days vs. 22/
15 days) than the detection level for both unsupervised and supervised
approaches. Their difference reflects the minimum lag days (roughly 20

days)  required  to  collect  six  HLS  clear  observations  after  disturbance
occurrence.

4.2. Lag component evaluation

Fig. 9 displays assessments of different lag components of the two
approaches. Note that we made assessments based on only the distur-
bance samples that were successfully confirmed by each approach (un-
supervised: 287 cases; supervised: 370 cases). The total lags of the two
approaches,  MTLs,  are  close  (unsupervised  vs.  supervised  = 39.4  vs.
38.8 days), which is mainly due to 1) the ambiguity in reporting inde-
pendent  temporal  metrics  with  ignorance  on  spatial  accuracy  (i.e.,
omission and commission error rates) (Bullock et al., 2022); 2) the total
lags of the two approaches were dominated by their similar confirmation
lag (~77%) as their required anomaly numbers are both set as six. In
comparison, the supervised approach yielded lower sensitivity lags (0.1
vs 1.1 days), making its MTLf  shorter than the unsupervised by 10% (9.1
vs. 10.0 days). This revealed the advantage of the supervised approach
for the early alerting of the disturbance, especially when the signal was
not  pronounced.  The  observation  lags  were  both  averagely  2.0  days,
which  were  mainly  controlled  only  by  the  HLS  revisiting  cycle  and

RemoteSensingofEnvironment305(2024)11407110S. Ye et al.

Fig. 8. An example site ((cid:0) 73.377, 41.946) for omission errors produced by the unsupervised approach. The HLS time series (A) shows a time series impacted by
spongy moth damage, with the disturbance breakpoint detected by the supervised approach marked as “black circle” in (A). The damage has been verified by color
change (“white spots”) within HLS images (B). The NRT results (C) present that the unsupervised approach totally missed the disturbance patches at the confirmation
level due to the quick spectral recovery.

Fig. 9. An assessment of the unsupervised and supervised approach for their different lag components, with their correctly confirmed sample case number shown in
the y-axis labels. MTL: Mean Time Lag; MTLf : Mean Time Lag for the First Alert.

weather conditions. The average production lags of the two approaches
were almost the same (4.9 vs. 5.0 days). Their small numeric difference
was caused by the different sample sets that were successfully confirmed

(unsupervised  vs.  supervised  = 287:  370  cases)  and  involved  in  pro-
duction lag assessments. MTL  and MTLf  of the two approaches did not
present sufficient differences as their sigmoid curves showed (Fig. 6),

RemoteSensingofEnvironment305(2024)11407111S. Ye et al.

which echoed the viewpoint that these two metrics are problematic for
latency  assessment  because  they  were  calculated  based  on  their  own
correctly  identified  samples,  ignoring  their  omission  and  commission
errors (Bullock et al., 2022). A high rate of omission errors and com-
mission errors often caused incomplete patch detection and too many
noisy signals, which would eventually lead to a mapping delay.

4.3. Individual disturbance assessments

Fig. 10 shows that individual disturbance types presented different
sigmoid curves and lag metrics. For the detection level, “Kentucky flood”
(Fig. 10C) received the quickest alerting as its Level Off Point at (9 days,
0.94 F1  score); “Construction” had the longest latency as the Level Off
Point at (43 days, 0.68 F1 score), which was possibly due to the fact that
the  initial  stage  of  a  construction  project  (e.g.,  land  clearing)  often
yielded small-area and unobvious spectral signals; two ephemeral dis-
turbances, “Kentucky Flood” and “Hurricane Ian”, presented an inverted
U-shaped sigmoid curve while the other three were S-shaped. This in-
dicates  that  some  patches  affected  by  ephemeral  disturbances  experi-
enced  rapid  recovery.  For  the  confirmation  level,  F1  scores  for  two
ephemeral  disturbances dropped dramatically compared to the detec-
tion  level,  while  the  other  three  remained  similar  F1  scores  for  their
Level Off Point, which explained the noticeable performance difference
between the detection and the confirmation level in Table 4.

Fig.  11  demonstrates  the  dynamics  of  the  detection-  and  the
confirmation-level  products  over  time  since  a  disturbance.  For  “Mos-
quito Fire” (Fig. 11A) and “Spongy Moth” (Fig. 11B), most disturbance
regions  in  the  detection  level  were  confirmed (displayed  as  red  poly-
gons) since 5th week in the figure. Differently, the detected patches for
two ephemeral disturbances, “Hurricane Ian” (Fig. 11C) and “Kentucky
Flood”  (Fig.  11D),  were  not  converted  into  the  confirmation-level
patches  but  disappeared  after  the  5th  week,  as  these  disturbance
events did not last long enough to generate six consistent anomalies. The
NRT platform did not successfully map the Kentucky Flood in the 1st
week for this case, which might be lacking clear observations due to the
rainy/cloudy  weather  often  accompanying  the  flooding  event  (longer
data lag); once the first post-flood clear observation became available,
more flood-related signals  were captured, mainly  on housing damage
and  soil  change,  leading  to  an  F1  jump  at  the  9th  day  in  Fig.  10C
(“detection level”).

Table  5  exhibits  different  algorithmic  latency  (sensitivity  and

confirmation lags) among the five disturbance events. The other three
lag  components  (data,  observation,  and  product  lags)  were  only
contingent on data acquisition or platform operation, thereby generally
indifferent across various disturbance events. As a result of the subtle
change signals at their early stage, spongy moth and construction yiel-
ded  higher  sensitivity  lags  for  the  NRT  monitoring.  Compared  to  the
unsupervised, the supervised approach reached a lower average sensi-
tivity  lag,  enabling  an  earlier  alerting  for  these  two  events.  For  the
confirmation lag, Mosquito fire showed much shorter lags than the other
four disturbances, possibly owing to the frequent dry and sunny weather
for  North  California  providing  dense  post-fire  observations.  Different
from the sensitivity lag, confirmation lags were close between the su-
pervised  and  the  unsupervised  approaches,  indicating  that  the  retro-
spective  information  helped  little  in  reducing  the  confirmation  lag,
which should be controlled by the setting of conse and data density.

5. Discussion

5.1. Comparison to other NRT studies

Compared to the study using the closest evaluation method (Bullock
et  al.,  2022),  applying  CCDC  on  sentinel-1  time  series  (i.e.,  “P2”
configuration) reached a Level Off Point (203 days, 0.216 F1  score) at
the  confirmation  level  for  monitoring  tropical  deforestation,  much
worse  than  the  same  metric  result  for  the  supervised  approach  (38.8
days, 0.439 F1  score). Not to mention that we included the ephemeral
disturbances which were challenging and greatly impacted our F1  score
at the confirmation level. Reiche et al. (2018) combined observations
from  six  satellites,  Sentinel-1,  ALOS-2,  Landsat  7  and  8,  to  detect  a
specific land disturbance, deforestation, and reached a MTL as 31 days;
Shang et al. (2022) built a method based on HLS datasets with setting
four  minimum  consecutive  anomalies  for  confirmation,  reporting  a
resultant MTL as 35 days. The MTL of our supervised approach (38.8
days)  seems  to  be  a  little  longer  than  the  above  two  studies,  but  we
approached  more  diversified  land  disturbances  including  ephemeral
disturbances.  More  important  is  that  we  assessed  our  approach  in  an
operational platform by including observation, data, and production lag
assessments, which additionally increased approximately nine extra lag
days compared to the previous studies. It is noteworthy that for emer-
gency events, the updating interval of our NRT system could be manu-
ally  adjusted  to  a  one-day  interval  to  make  the  fastest  response  with

Fig. 10. Sigmoid accuracy curves for individual disturbance events being marked with the two key latency metrics at the detection and at the confirmation level.

RemoteSensingofEnvironment305(2024)11407112S. Ye et al.

Fig.  11. The  dynamics  of  detection-  and  confirmation-level  products  for  different  disturbance  events.  The  centroid  coordinates  for  the  sites  are  Mosquito  Fire
((cid:0) 120.752, 39.056), Spongy Moth ((cid:0) 73.684, 43.144), Hurricane Ian ((cid:0) 81.898, 26.652), and Kentucky Flood ((cid:0) 83.382, 37.553).

Table 5
Algorithmic latency comparison for the five disturbance events.

Sensitivity lag (days)

Mosquito Fire

Spongy Moth

Kentucky Flood

Hurricane Ian

Construction

Unsupervised
Supervised
Confirmation lag (days)

0.56
0.57

Unsupervised
Supervised

Mosquito Fire
18.08
17.22

4.29
2.18

Spongy Moth
31.08
31.80

0
0

Kentucky Flood
29.00
32.89

0
0

Hurricane Ian
35.27
35.36

6.40
4.75

Construction
34.70
35.13

zero-day  production  lag,  so  that  the  average  lag  for  alerting  the  first
anomaly for an event (MTLf ) would be further shortened to around half
of  a  week  (4.1  days).  It  will  be  even  faster  in  the  future,  with  more
medium-resolution  satellite  sensors  launched  and  quicker  release  of
reflectance products.

All  the  previous  studies  used  the  unsupervised  anomaly  approach
based  on  the  predefined  change  threshold,  mostly  focusing  on  forest
disturbances. To our knowledge, this study is the first attempt to build
up a sole NRT approach/system intended for various natural disasters
and human-induced terrestrial changes. To address the issue of distur-
bance variety, we designed multifaceted predictors, including the pre-
disturbance features that are indicative of background land cover, and
spectral change features for characterizing a disturbance process. With
the retrospective analysis of those historical disturbances, we were able
to  establish  machine  learning  models  using  these  predictors  to  better
analyze  ongoing  anomaly  signals.  Notably,  our  approach  built  an

explicit  model  for  each  anomaly  number  condition,  considerably
enhancing the capability of distinguishing early signals and decreasing
sensitivity lags, hence a timelier detection. For future research, the su-
pervised  approach  is  readily  expanded  to  provide  NRT  mapping  for
disturbance agents through the incorporation of agent samples.

5.2. Limitations

The relatively lower overall accuracy in the confirmation level sug-
gests the dilemma of disturbance confirmation. For this study, we used
the CCDC default minimum observations (conse = 6) for confirming a
disturbance patch, which was well verified in multiple past studies on
Landsat-based studies (Brown et al., 2019; Ye et al., 2021a; Zhu et al.,
2019). But the conse was not tested yet on a per-event basis. Especially, it
was still challenging to accurately confirm the impacted regions of those
short-lived  events.  The  two  ephemeral  events,  “Kentucky  Flood”  and

RemoteSensingofEnvironment305(2024)11407113S. Ye et al.

“Hurricane Ian”, did not lead to permanent land cover conversion, and
their  spectral  signals  only  lasted  for  one  to  three  observations.  As  a
result, their omission errors greatly increased after their Level Off Points
(Fig.  10C  and  Fig.  10D).  Even  with  a  decreased  minimum  anomaly
number such as conse = 4 in (Shang et al., 2022), it is still not likely to
accurately detect events such as flash flooding, which often induces only
one anomaly. In contrast, “Spongy Moth” (36 days, 0.76 F1  score) and
“Construction”  (43  days,  0.68  F1  score)  had  a  lag  for  their  Level  Off
Points close to the MTL of the supervised (38.8 days) using six anoma-
lies. It suggests that confirming a disturbance event with six anomalies
(conse = 6) is still workable for most non-ephemeral disturbance events.
The  varied  sigmoid  curves  and  Level  Off  Points  of  these  disturbance
events  indicate  a  future  direction  for  developing  agent-based  confir-
mation strategies instead of a universal confirmation rule.

The  present  methodology  predominantly  depends  on  U.S.  distur-
bance datasets to construct retrospective models, which introduces dif-
ficulties  in  deploying  the  supervised  approach  globally.  This  could
potentially be overcome by manual sample interpretation, but we pro-
pose  further  research  into  automating  the  transfer  of  U.S.  samples  to
other countries with a goal of enhancing the global applicability of this
supervised  model.  The  method’s  efficacy  is  confirmed  with  the  HLS
dataset due to its high temporal density. However, there is a lack of clear
observations  in  certain  areas,  such  as  tropical  regions,  or  the  distur-
bances  associated  with  frequent  cloud  cover,  like  floods.  For  future
improvements, we recommend integrating radar sensors like Sentinel-1.

6. Conclusion

We  proposed  a  novel  supervised  machine  learning  approach  to
analyze  spectral  anomalies  from  HLS  time  series.  The  retrospective
analysis extracted and modeled the early disturbance information from
the historical time-series datasets, combined with existing disturbance
products.  A  machine-learning  model  was  built  specifically  for  each
anomaly  number  condition  to  better  discriminate  early  disturbance
signals.  Compared  to  the  unsupervised  approach,  the  supervised
approach reduced sensitivity lag, especially for subtle disturbances, and
brought forward the Level Off point by seven days, with a 0.2 F1  score
improvement.  Besides,  the  supervised  approach  considerably  sup-
pressed  the  commission  error  rate  by  27  percent  points,  greatly
enhancing  the  NRT  capability  for  accurately  delineating  disturbance
regions.

CRediT authorship contribution statement

Su Ye: Conceptualization, Data curation, Formal analysis, Method-
ology, Software, Validation, Visualization, Writing – original draft. Zhe
Zhu:  Conceptualization,  Funding  acquisition,  Investigation,  Project
administration, Resources, Supervision, Writing – review & editing. Ji
Won Suh: Data curation, Visualization, Writing – review & editing.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Data availability

Data will be made available on request.

Acknowledgment

This work has been supported by the USGS-NASA Landsat Science
Team (LST) Program for Toward Near Real-time Monitoring and Char-
acterization  of  Land  Surface  Change  for  the  Conterminous  US
(140G0119C0008). The content of this document does not necessarily

represent the views or policies of the Department of the Interior, nor
does  mention  of  trade  names,  commercial  products,  or  organizations
imply endorsement by the U.S. Government.

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.

org/10.1016/j.rse.2024.114071.

References

Andela, N., Morton, D.C., Schroeder, W., Chen, Y., Brando, P.M., Randerson, J.T., 2022.
Tracking and classifying Amazon fire events in near real time. Sci. Adv. 8, eabd2713.

Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,

Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K.,
Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D.,
Reker, R.R., Rover, J., 2019. Lessons learned implementing an operational
continuous United States national land change monitoring capability: the land
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens.
Environ. https://doi.org/10.1016/j.rse.2019.111356.

Brown, C.F., Brumby, S.P., Guzder-Williams, B., Birch, T., Hyde, S.B., Mazzariello, J.,
Czerwinski, W., Pasquarella, V.J., Haertel, R., Ilyushchenko, S., 2022. Dynamic
world, near real-time global 10 m land use land cover mapping. Sci. Data 9, 1–17.
Bullock, E.L., Healey, S.P., Yang, Z., Houborg, R., Gorelick, N., Tang, X., Andrianirina, C.,

2022. Timeliness in forest change monitoring: a new assessment framework
demonstrated using Sentinel-1 and a continuous change detection algorithm.
Remote Sens. Environ. 276, 113043.

Centers, N.N., 2023. NOAA National Centers for Environmental Information (NCEI) U.S.
Billion-Dollar Weather and Climate Disasters (2023) [WWW Document]. https://doi.
org/10.25921/stkw-7w73.

Chuvieco, E., Mouillot, F., Van der Werf, G.R., San Miguel, J., Tanase, M., Koutsias, N.,
García, M., Yebra, M., Padilla, M., Gitas, I., 2019. Historical background and current
developments for mapping burned area from satellite earth observation. Remote
Sens. Environ. 225, 45–64.

Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.C., Skakun, S.V.,
Justice, C., 2018. The harmonized Landsat and Sentinel-2 surface reflectance data
set. Remote Sens. Environ. 219, 145–161. https://doi.org/10.1016/j.
rse.2018.09.002.

Cohen, W.B., Healey, S.P., Yang, Z., Stehman, S.V., Brewer, C.K., Brooks, E.B.,

Gorelick, N., Huang, C., Hughes, M.J., Kennedy, R.E., 2017. How similar are forest
disturbance maps derived from different landsat time series algorithms? For. Trees
Livelihoods 8, 98.

Diniz, C.G., de Almeida Souza, A.A., Santos, D.C., Dias, M.C., Da Luz, N.C., De Moraes, D.
R.V., Maia, J.S., Gomes, A.R., da Silva Narvaes, I., Valeriano, D.M., 2015. DETER-B:
the new Amazon near real-time deforestation detection system. IEEE J. Sel. Top.
Appl. earth Obs. Remote Sens. 8, 3619–3628.

Doblas, J., Reis, M.S., Belluzzo, A.P., Quadros, C.B., Moraes, D.R.V., Almeida, C.A.,
Maurano, L.E.P., Carvalho, A.F.A., Sant’Anna, S.J.S., Shimabukuro, Y.E., 2022.
DETER-R: an operational near-real time tropical forest disturbance warning system
based on Sentinel-1 time series analysis. Remote Sens. 14, 3658.

Eckerstorfer, M., Vickers, H., Malnes, E., Grahn, J., 2019. Near-real time automatic snow
avalanche activity monitoring system using Sentinel-1 SAR data in Norway. Remote
Sens. 11, 2863.

Field, C.B., Barros, V., Stocker, T.F., Dahe, Q., 2012. Managing the Risks of Extreme

Events and Disasters to Advance Climate Change Adaptation: Special Report of the
Intergovernmental Panel on Climate Change. Cambridge University Press.
Francini, S., McRoberts, R.E., Giannetti, F., Mencucci, M., Marchetti, M., Scarascia
Mugnozza, G., Chirici, G., 2020. Near-real time forest change detection using
PlanetScope imagery. Eur. J. Remote Sens. 53, 233–244.

Giglio, L., Loboda, T., Roy, D.P., Quayle, B., Justice, C.O., 2009. An active-fire based

burned area mapping algorithm for the MODIS sensor. Remote Sens. Environ. 113,
408–420.

Gill, S.K., Kaplan, A.S., 2021. A retrospective chart review study of symptom onset,

diagnosis, comorbidities, and treatment in patients with binge eating disorder in
Canadian clinical practice. Eat. Weight Disord. Anorexia, Bulim. Obes. 26,
1233–1242.

Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S.,
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
using Landsat data. Environ. Res. Lett. 11, 34008.

Hawbaker, T.J., Vanderhoof, M.K., Schmidt, G.L., Beal, Y.-J., Picotte, J.J., Takacs, J.D.,
Falgout, J.T., Dwyer, J.L., 2020. The Landsat burned area algorithm and products for
the conterminous United States. Remote Sens. Environ. 244, 111801.

Hess, D.R., 2004. Retrospective studies and chart reviews. Respir. Care 49, 1171–1174.
Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust.

For. https://doi.org/10.1080/00049158.2008.10675037.

Kaji, A.H., Schriger, D., Green, S., 2014. Looking through the retrospectoscope: reducing
bias in emergency medicine chart review studies. Ann. Emerg. Med. 64, 292–298.

Karimiziarani, M., Moradkhani, H., 2023. Social response and disaster management:

insights from twitter data assimilation on hurricane Ian. Int. J. Disaster Risk Reduct.
95, 103865.

Latifovic, R., Homer, C., Ressl, R., Pouliot, D., Hossain, S.N., Colditz, R.R., Olthof, I.,
Giri, C.P., Victoria, A., 2016. North American land-change monitoring system.
Remote Sens. L. Use L. Cover 303.

RemoteSensingofEnvironment305(2024)11407114S. Ye et al.

Liang, L., Chen, Y., Hawbaker, T.J., Zhu, Z., Gong, P., 2014. Mapping mountain pine

beetle mortality through growth trend analysis of time-series landsat data. Remote
Sens. https://doi.org/10.3390/rs6065696.

Martínez-Ramos, M., Ortiz-Rodríguez, I.A., Pi˜nero, D., Dirzo, R., Sarukh´an, J., 2016.
Anthropogenic disturbances jeopardize biodiversity conservation within tropical
rainforest reserves. Proc. Natl. Acad. Sci. USA. https://doi.org/10.1073/
pnas.1602893113.
´
Cwik, K., 2018. The use of Sentinel-1 time-series data to improve
Martinis, S., Plank, S.,

Maycock, T.K. (Eds.), Fifth National Climate Assessment. U.S. Global Change
Research Program, Washington, DC, USA. https://doi.org/10.7930/NCA5.2023.
CH6.

Van der Walt, S., Sch¨onberger, J.L., Nunez-Iglesias, J., Boulogne, F., Warner, J.D.,

Yager, N., Gouillart, E., Yu, T., 2014. scikit-image: image processing in Python. PeerJ
2, e453.

Vargas, C., Montalban, J., Leon, A.A., 2019. Early warning tropical forest loss alerts in

Peru using Landsat. Environ. Res. Commun. 1, 121002.

flood monitoring in arid areas. Remote Sens. 10, 583.

Olsson, P.-O., Lindstr¨om, J., Eklundh, L., 2016. Near real-time monitoring of insect

Vassar, M., Matthew, H., 2013. The retrospective chart review: important

methodological considerations. J. Educ. Eval. Health Prof. 10.

induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote
Sens. Environ. 181, 42–53. https://doi.org/10.1016/j.rse.2016.03.040.

Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using

satellite image time series. Remote Sens. Environ. 123, 98–108.

Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect
defoliation using landsat time series. Forests. https://doi.org/10.3390/f8080275.
Peters, E.B., Wythers, K.R., Bradford, J.B., Reich, P.B., 2013. Influence of disturbance on

temperate forest productivity. Ecosystems 16, 95–110.

Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving

near-real time deforestation monitoring in tropical dry forests by combining dense
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
204, 147–161.

Reiche, J., Mullissa, A., Slagter, B., Gou, Y., Tsendbazar, N.-E., Odongo-Braun, C.,

Vollrath, A., Weisse, M.J., Stolle, F., Pickens, A., 2021. Forest disturbance alerts for
the Congo Basin using Sentinel-1. Environ. Res. Lett. 16, 24005.

Rollins, M.G., 2009. LANDFIRE: a nationally consistent vegetation, wildland fire, and

fuel assessment. Int. J. Wildland Fire 18, 235–249.

Ryan, K.C., Opperman, T.S., 2013. LANDFIRE–A national vegetation/fuels data base for
use in fuels treatment, restoration, and suppression planning. For. Ecol. Manag. 294,
208–216.

Salviati, C., Warnock, R., 2023. Sun Belt metros lead apartment construction boom in

2023.

Seidl, R., Schelhaas, M.-J., Rammer, W., Verkerk, P.J., 2014. Increasing forest

disturbances in Europe and their impact on carbon storage. Nat. Clim. Chang. 4,
806–810.

Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time

monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data.
Remote Sens. Environ. 278, 113073.

Shimabukuro, Y., Duarte, V., Anderson, L., Valeriano, D., Arai, E., Freitas, R., Rudorff, B.
F., Moreira, M., 2006. Near real time detection of deforestation in the Brazilian
Amazon using MODIS imagery. Ambient. e Agua-An Interdiscip. J. Appl. Sci. 1,
37–47.

Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
monitoring of tropical forest disturbance: new algorithms and assessment
framework. Remote Sens. Environ. 224, 202–218.

Tang, X., Bratley, K.H., Cho, K., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2023. Near
real-time monitoring of tropical forest disturbance by fusion of Landsat, Sentinel-2,
and Sentinel-1 data. Remote Sens. Environ. 294, 113626.

Teater, D., 2023. Aquatics Specialist Report Mosquito Fire Burned Area Emergency

Response (BAER) Assessment Tahoe National Forest.

Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,

Gao, F., Goward, S.N., Helder, D., Helmer, E., Nemani, R., Oreopoulos, L., Schott, J.,
Thenkabail, P.S., Vermote, E.F., Vogelmann, J., Wulder, M.A., Wynne, R., 2008. Free
access to Landsat imagery. Science 320, 1011. https://doi.org/10.1126/
science.320.5879.1011a.

Wulder, M.A., Coops, N.C., Roy, D.P., White, J.C., Hermosilla, T., 2018. Land cover 2.0.

Int. J. Remote Sens. 39, 4254–4284. https://doi.org/10.1080/
01431161.2018.1452075.

Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
LCMAP collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
143–162.

Yang, X., Zhu, Zhe, Qiu, S., Kroeger, K.D., Zhu, Zhiliang, Covington, S., 2022. Detection

and characterization of coastal tidal wetland change in the northeastern US using
Landsat time series. Remote Sens. Environ. 276, 113047.

Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
forest disturbance using Landsat time series: stochastic continuous change detection.
Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112167.

Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
dense Landsat time series: case studies of mountain pine beetle and spruce beetle
disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2021.112560.
Ye, S., Zhu, Z., Cao, G., 2023. Object-based continuous monitoring of land disturbances

from dense Landsat time series. Remote Sens. Environ. 287, 113462.

Yu, L., Du, Z., Dong, R., Zheng, J., Tu, Y., Chen, X., Hao, P., Zhong, B., Peng, D., Zhao, J.,
2022. FROM-GLC plus: toward near real-time and multi-resolution land cover
mapping. GIScience Remote Sens. 59, 1026–1047.

Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
data for operational land cover classification for the LCMAP initiative. ISPRS J.
Photogramm. Remote Sens. 122, 206–221.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2019.

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.

Thornton, P.E., Reed, B.C., Xian, G.Z., Chini, L., East, A.E., Field, J.L., Hoover, C.M.,

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.

Poulter, B., Reed, S.C., Wang, G., Zhu, Z., 2024. Land cover and land-use change. In:
Crimmins, A.R., Avery, C.W., Easterling, D.R., Kunkel, K.E., Stewart, B.C.,

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.

RemoteSensingofEnvironment305(2024)11407115
