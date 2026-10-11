Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

Object-based continuous monitoring of land disturbances from dense
Landsat time series

Su Ye a,*, Zhe Zhu a, Guofeng Cao b
a Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT, USA
b Department of Geography, University of Colorado Boulder, Boulder, CO, USA

A R T I C L E  I N F O

A B S T R A C T

Edited by Marie Weiss

Keywords:
Land disturbance
Change detection
Time series
Object-based
Multiscale image analysis
Spatiotemporal

An accurate mapping of land disturbances with regard to their timing and locations is the prerequisite for the
success of downstream disturbance characterization. This study introduces and tests a novel approach that in-
tegrates  a  spatial  perspective  into  the  dense  Landsat  time  series  analysis,  called  “Object-Based  COntinuous
monitoring  of  Land  Disturbance”  (OB-COLD).  The  new  algorithm  is  based  on  the  recognition  that  the  pixels
under effects of the same disturbance event often present similar spectral change concurrently in a short time;
such pixels experiencing concurrent change could be grouped as an analytic spatial unit, namely “change object”.
OB-COLD first generates a change-magnitude snapshot every 60 days by applying per-pixel time series analysis to
measure  spectral  change  history.  Then,  an  object-based  change  analysis  is  applied  for  each  time-stamped
snapshot:  two  levels  of  change  objects  are  generated  through  over-segmentation  and  region  merging;  the
changing area is determined by examining three object-level properties derived at different scales: the average
change  magnitude,  the  pre-change  cover  type,  and  the  object  size.  Lastly,  OB-COLD  reconstructs  model  co-
efficients  for  each  temporal  segment  based  on  the  temporal  breaks  indicated  by  new  snapshot-based  change
maps. We tested the new algorithm using 3000 randomly selected reference sample plots and eight Landsat ARD
tiles  across  the  continental  United  States.  The  accuracy  assessment  suggests  that  OB-COLD  achieved  76.9%
producer’s  accuracy,  which  is  significantly  higher  than  the  per-pixel  time  series  algorithm  (i.e.,  COLD)  (16.3
percentage  increase)  while  keeping  a  comparable  user’s  accuracies  (58.7%  vs.  57.8%).  The  quantitative  and
qualitative evaluations both suggest that OB-COLD could significantly reduce omission errors, particularly for
stress disturbances. Most commission errors (73%) are attributed to agricultural practices and climate variability.
The  proposed  algorithm  is  computationally  scalable  to  large-scale  spatiotemporal  datasets  with  advanced
cyberinfrastructure resources, holding great potential as the base detection algorithm for the next generation of
land disturbance products.

1. Introduction

Land disturbance, not limited to forested regions, can be defined as
any event that is relatively discrete in time and space that disrupts the
structure of an ecosystem, community, or population (Newman, 2019;
White  and  Pickett,  1985).  Land  disturbances,  purportedly  driven  by
anthropogenic  activities  and  recent  climatic  warming,  have  been
documented over large parts of the globe with an increase in frequency
and severity (Dale et al., 2001; Seidl et al., 2017), yielding significant
impacts  on  the  carbon  cycle  (Liang  et  al.,  2014;  Seidl  et  al.,  2014),
biodiversity (Martínez-Ramos et al., 2016), water quality (Carey et al.,
2011)  and landscape composition  (Danneyrolles et  al., 2019). Timely

and  accurate  mapping  of  land  disturbance  events  is  of  enormous
importance  to  ecologists  and  forest  managers,  allowing  for  a  better
understanding  of  ecosystem-climate  interactions  and  improved  land
resource management (Cohen et al., 2016; Rogan and Miller, 2006; Senf
et al., 2017; Senf and Seidl, 2021). Remote sensing technology, typically
the  medium-resolution  time  series  analysis,  has  been  widely  used  for
detecting a variety of land disturbances by identifying a temporal span
of spectral anomaly relative to its natural variability (Coops et al., 2020;
Hermosilla et al., 2019; Schug et al., 2018; Villarreal et al., 2016; Yin
et al., 2020; Zhu et al., 2019). A satellite-based disturbance investigation
project  is  typically  comprised  of  two  components:  1)  mapping  of
disturbed region and timing (Cohen et al., 2018; Huang et al., 2010; Zhu

* Corresponding author.

E-mail address: remotesensingsuy@gmail.com (S. Ye).

https://doi.org/10.1016/j.rse.2023.113462
Received 19 July 2022; Received in revised form 13 January 2023; Accepted 16 January 2023

RemoteSensingofEnvironment287(2023)113462Availableonline27January20230034-4257/©2023ElsevierInc.Allrightsreserved.S. Ye et al.

et  al.,  2020);  2)  characterizing  disturbance  agents  (Baumann  et  al.,
2014; Kennedy et al., 2015; Zhang et al., 2022), severity (Rodman et al.,
2021), or recovery (White et al., 2022). This paper is concerned with the
first component, the process of detecting disturbances, which provides
essential base maps for downstream disturbance characterization.

To date, numerous algorithms have been developed to map distur-
bances  from  Landsat  time-series  dataset  (Zhu,  2017).  COntinuous
monitoring  of  Land  Disturbances  (COLD),  the  latest  version  of  the
Continuous  Change  Detection  and  Classification  (CCDC)  algorithm
tailored for land disturbance mapping, is a representative approach that
makes it feasible to detect a variety of land disturbances based upon all
available Landsats 4–8 data (herein named as “dense time series”, Zhu
et al., 2020). COLD or all CCDC-like algorithms successively compare
model  forecasts  and  actual  observations  and  identifies  breaks  if  the
discrepancies between new observations and model predictions persist
(Zhu et al., 2020; Zhu and Woodcock, 2014a), which have been widely
used for mapping coastal tidal wetland dynamics (Yang et al., 2022),
land disturbance agents (Qiu et al., 2022), nighttime light change (Li
et al., 2022) and forest dynamics (Healey et al., 2018).

While  COLD  and  other  popular  time-series  approaches,  such  as
LandTrendr (Kennedy et al., 2010), BFAST (Verbesselt et al., 2010), and
VCT (Huang et al., 2010), have greatly enhanced our ability for mapping
land  change,  these  methods  adhere  to  using  pixels  as  independent
spatial  units  for  analysis,  focusing  on  capturing  obvious  temporal
anomaly or breaks based upon single-pixel-based time series. The major
downside  for  such-like  approaches  is  that  they  often  suffer  a  high
omission error rate for the myriad of subtle disturbances (e.g., insect,
drought) that are characterized by insignificant spectral change lower
than their pre-defined magnitude threshold (Cohen et al., 2017; Ye et al.,
2021b; Zhu et al., 2019). Even for the dramatic disturbances that lead to
land cover conversion (e.g., agricultural expansion and urbanization),
per-pixel  approaches  may  fail  to  delineate  the  full  extent  of  a
disturbance-affected  region  that  often  presents  heterogeneous  change
owing to numerous geographically varying factors such as severity, pre-
disturbance  conditions,  and  topography.  Spatial-contextual  informa-
tion,  such  as  patch  size  and  change  adjacency,  could  provide  new
powerful  metrics  for  discriminating  subtle  disturbances  and  enhance
detection completeness through a consideration of spatial autocorrela-
tion  for  event-induced  spectral  change.  To  incorporate  spatial  infor-
mation into temporal analysis, several studies applied a simple spatial
filtering for post-processing disturbance maps (Pasquarella et al., 2017;
Ye et al., 2021b) but often only achieve a small degree of map refine-
ment (Ye et al., 2021b). More sophisticated is a group of spatial-window
techniques that uses a focal operation to preprocess each original sat-
ellite  image  and  then  applies  the  time-series  algorithm  to  the  pre-
processed  images  (Hamunyela  et  al.,  2016;  Meng  et  al.,  2021).  For
example, Hamunyela et al. (2016) normalized each pixel by the median
value of the neighboring pixels whose vegetation index values are above
the 90th percentile of all pixels within a spatial window; such spatial
normalization could significantly reduce signal noises from vegetation
phenology  for  the  subsequent  time  series  analysis  and  advance  the
timing of capturing deforestation signals (Hamunyela et al., 2016). This
study  was  targeted  at  forest  disturbance,  and  the  window  size  was
determined  through  sensitivity  analysis  (Hamunyela  et  al.,  2016);
however, a single predefined spatial window size may not be sufficient
for  modeling  generic  land  disturbances  at  a  national  or  continental
scales, which often manifests a diversity of cover types, spatial patterns
and extents.

Object-Based Image Analysis (OBIA) is an image processing frame-
work which divides an image into clusters of adjacent pixels based on
their spectral similarities, i.e., image objects (IOs), and then uses these
IOs  as  the  analytic  unit  (Blaschke,  2010)  for  the  tasks  such  as  image
classification  (Dronova  et  al.,  2015;  Gudex-Cross  et  al.,  2017;  Zhang
et  al.,  2014,  2018),  continuous  surface  parameter  estimate  (Laurent
et al., 2013; Roelfsema et al., 2014), and pansharpening (Zhang et al.,
2021).  IOs  can  be  used  to  represent  an  almost  unlimited  range  of

phenomena (Bian, 2007), from meaningful landscape entities to a lower-
level grouping of spectrally similar pixels such as superpixel (e.g., Csil-
lik, 2017), thereby leading to more flexibilities for modeling complex
geographic phenomenon than the spatial-window techniques. OBIA first
gained  its  popularity  among  the  fine-resolution  (< 5  m)  applications
under an H-resolution situation (Cleve et al., 2008; Holt et al., 2009),
where landscape units of interest are significantly larger than the reso-
lution  cells  (Strahler  et  al.,  1986).  Later  studies  utilized  OBIA  for
medium-resolution images such as Landsat (Duveiller et al., 2008; Jobin
et al., 2008; Vieira et al., 2012) and Sentinel-2 (Belgiu and Csillik, 2018;
Djerriri et al., 2020), owing to its superiority for incorporating spatial
properties  such  as  object  size  and  texture.  These  OBIA  studies  were
mainly employed for land cover classification tasks, defining their ob-
jects as landscape entities. Nevertheless, land disturbances not only alter
landscape units in terms of their biophysical properties, but also – and
more often  –  change their  spatial borders. Therefore,  it is  unlikely to
apply  an  object-oriented  paradigm  based  on  land  cover  objects  for
mapping  land  disturbances,  unless  targeted  landscape  boundaries
remain unchanged during the change process (e.g., Yin et al., 2018).

Alternatively, we could choose change objects as our analytic unit,
rather than land cover objects. The consequences of a disturbance event,
such  as  altering  land  condition,  composition,  soil  property,  or  cover
types, are often viewed as a spatial and temporal continuum (Kimmins,
2004).  If  a  pixel  is  experiencing  spectral  changes  related  to  a  distur-
bance,  it  is  reasonable  to  expect  that  its  neighboring  pixels  present
similar  spectral  changes  in  a  synchronized  manner,  constituting  a
change  object.  This  definition  resolves  the  issue  of  changing  object
boundaries over time and facilitates integration of object-level change
features,  such  as  change  object  size  and  pre-change  land  types,  for
improved disturbance detection.

Closing this gap, the change-object approach embarks on a similar
challenge  in  GIScience  concerning  the  representation  of  complex
spatiotemporal objects across multiple spatiotemporal scales (Blaschke
et al., 2014; Yuan, 2001). Particularly, enormous spectral details have
been  brought  by  within-event  change  heterogeneity,  as  well  as
increasing temporal  density and  spatial resolution  of satellite images,
calling  for  a  hierarchical,  multi-scale  framework  to  decompose  the
spatiotemporal complexity. Fig. 1 conceptualizes a three-level hierarchy
for perceiving a change process from a medium-resolution time-series
dataset typically with a revisiting cycle of 3–8 days. Change superpixels
(Level  III)  refer  to  a  grouping  of  pixels  that  share  common  spectral
change in a short interval (e.g., a month) under the effects of a process,
representing  the  most  detailed  spatiotemporal  object  representation.
The  adjacent  change  superpixels  within  the  same  time  intervals  are
further aggregated into a change patch (Level II), forming a continuous
region  affected  by  the  change  process  at  a  coarser  spatial  scale.  A
change-process object (Level I) is the total area affected by the change
process,  which  sometimes  necessitates  an  ensemble  of  change  infor-
mation from several time periods (such as one to several years). Change-
process  object  could  be  created  by  segmenting  intermediate  change
measurement maps at an interval of multiple years (G´omez et al., 2011)
or connecting adjacent pixels from annual pixel-based disturbance maps
(Hermosilla et al., 2015; Kennedy et al., 2015; Qiu et al., 2022), and was
commonly employed as the object unit for the disturbance character-
ization. On the contrary, change objects at a fine spatiotemporal scale
are more practically useful at the detection stage which aims at delin-
eating accurate spatial and temporal change boundaries, particularly to
the CCDC-like approaches that were established to provide intra-annual
change information. Besides, a fine temporal grain for monitoring can
help reduce the chance of misidentifying a mixed-disturbance object and
holds great promise for timely alerting in a near real-time monitoring
task. To our best knowledge, there are no established approaches yet for
analyzing change objects at a fine temporal scale (e.g., monthly). Spe-
cifically, two key impediments to such methodological development are:
1)  lacking  a  way  for  extracting  change  objects  from  a  time-series
perspective  of  perceiving  a  spectral  change  relative  to  its  historical

RemoteSensingofEnvironment287(2023)1134622S. Ye et al.

Fig. 1. A three-level hierarchy of land-change objects from a spatiotemporal domain.

variation;  2)  lacking  a  mechanism  for  intelligently  integrating  cross-
scale information into the change-decision process.

In this study, we will describe a novel spatial-temporal algorithm for
improved  detection  of  land  disturbances  from  Landsat  time  series
dataset,  called  Object-based  COntinuous  monitoring  of  Land  Distur-
bance  (OB-COLD).  The  basic  idea  of  OB-COLD  is  that  we  discretize
continuous time into a series of equal time intervals as the analytical
unit,  i.e.,  time  slices,  allowing  for  a  generation  of  image-like  change
snapshots  at  a  fine  temporal  scale;  then  apply  an  OBIA  procedure  to
delineate  change  regions  within  each  snapshot  by  combining  both
change-superpixel and change-patch information. In what follows, we
will introduce calibration and validation datasets (Section 2), provide
technical details for OB-COLD (Section 3), present both quantitative and
qualitative  evaluation  (Section  4),  and  finally  discuss  key  issues  in
incorporating spatial and thematic information, validation, downstream
disturbance characterization, etc. (Section 5).

2. Study area, datasets, and evaluation

2.1. Study area and datasets

Our algorithm tests were performed based on the CONUS (Conter-
minous  United  States)  region.  Two  openly  accessed  CONUS-wide
disturbance  plot  datasets,  i.e.,  Cohen’s  dataset  (Cohen  et  al.,  2016)
and LCMAP reference dataset (Pengra et al., 2020), were chosen as our
reference dataset for model calibration and evaluation, which were used
in  multiple  land  change  related studies  (Cohen et  al.,  2016; Stehman
et al., 2021; Ye et al., 2021a; Zhu et al., 2020).

In  this  study,  detectable  disturbances  are  defined  as  any  discrete
event  that  occurs  beyond  its  natural  variability  of  land  surfaces  on  a
decade scale; the spectral signals must be evident in both Landsat image
chips  or  Landsat-based  time  series.  Both  subtle  (e.g.,  stress)  and  dra-
matic disturbances (e.g., fire, harvest, and hydrology) are considered as
our detection targets; on the contrary, climate variability and agricul-
tural practice, which often induces ephemeral spectral fluctuation, are
not counted within our detection scope. Based upon the Land Change
Monitoring, Assessment and Projection (LCMAP) project and other past
land disturbance studies (Pengra et al., 2020; Qiu et al., 2022; Zhu et al.,
2020), the seven focused disturbance types in this paper were fire, har-
vest,  hydrology,  mechanical,  stress,  debris,  and  other.  For  a  detailed

definition  of  these  seven  disturbance  types,  we  refer  the  readers  to
Table 1 in Qiu et al. (2022).

Cohen’s  dataset  (Cohen  et  al.,  2016)  was  mainly  used  for  model
calibration in this study because this dataset adopted a forested-oriented
sampling strategy (forest occupy 40% of the sample pool) and hence had
less representativeness as a validation set for a generic land disturbance
mapping. Cohen’s dataset was generated from 180 Thiessen Scene Areas
(TSAs, designed  to provide non-overlapping Landsat-like frames  for a
convenient computation of unbiased estimator) polygons, which were
sampled  with  a  focus  on  the  forested  area  from  a  total  of  442  TSAs.
Within each of the 180 TSAs, 40 Landsat plots were selected based on a
simple random strategy, making up an initial sample set of 7200 Landsat
plots.  The  disturbance  years  ranging  from  1982  to  2012  were  inter-
preted  for  each  plot  using  a  visualization  software  called  TimeSync
(Cohen et al., 2010). For more processing details, we refer readers to
(Cohen et al., 2016; Zhu et al., 2020). A total of 6491 plots (blue dots in
Fig. 2) remained after eliminating those sample plots that did not have
enough clear sky observations (< 24) or were too difficult to interpret.
Admittedly, Cohen’s dataset was designed with a focus on the forested
area,  possibly  causing  the  resultant  model  to  yield  more  weights  on

Table 1
A summary of land cover types and major disturbance agents for pilot sites.

Evaluation site/tiles

New England
(h30v6)

Corn Belt Plains

(h21v8)

Dominant land cover
types

Tree cover, developed,
wetland
Cropland, developed

Mississippi River

Tree cover

Major disturbances

Gypsy moth outbreak, urban
expansion, hurricane
Urban expansion, agricultural
practice
Harvest, forest thinning

Lowlands (h21v15)
Western Great Plains

Grass, shrub, cropland

Drought

(h14v6)

Rocky Colorado

(h11v9)

Cascades Plateau

(h4v2)

West California

(h2v8)

South Florida
(h27v19)

Tree covers, cropland,
grass, shrub
Tree cover, grass,
shrub
Cropland, grass,
developed
Wetland (mangrove)

Beetle disturbances.
agricultural practices
Logging, forest fire

Wildfires, agricultural
practices
Tornado

RemoteSensingofEnvironment287(2023)1134623S. Ye et al.

Fig. 2. Locations of 6491 calibration plots, 2880 validation plots, and pilot testing tiles. Cover map source: 2001 Land Change Monitoring, Assessment and Projection
(LCMAP) primary land cover product (Version 1.2, Brown et al., 2019; Xian et al., 2022). (For interpretation of the references to color in this figure legend, the reader
is referred to the web version of this article.)

forest disturbance detection.  This problem could be alleviated by our
cover-specific  model  establishment  (see  section  3.2.3):  forest  distur-
bance sample plots were only used to tune the stable model for three
cover types with relatively small natural spectral variability (i.e., forest,
water, and developed), which did not affect the model calibration for the
other highly dynamic cover types (namely “fluctuated model”), such as
cropland and grass.

Quantitative evaluation was conducted based on land change refer-
ence sample plots from the LCMAP project (Pengra et al., 2020), which
were sampled from 30-m Landsat pixels in the CONUS ARD grid system.
The LCMAP sample plots were generated from cluster-based sampling,
in which each pixel was a cluster of 34 observation years of this pixel
(Stehman et al., 2021). We chose LCMAP reference dataset rather than
Cohen’s dataset for validation as LCMAP reference dataset have no bias
for specific land cover types, while Cohen’s dataset was mainly located
at  forest-dominated TSAs. While LCMAP reference dataset was  devel-
oped with a high quality following a rigorous protocol, we observed two
primary  issues  causing  its  discrepancies  with  our  detection  scope:  1)
disturbance omissions for ephemeral droughts that also induce a large-
area  spectral  change  from  Landsat  image  chips  as  well  as  temporal
break in the time-series profile (see the example of Fig. S1 in the sup-
plementary),  especially  in  semi-arid  regions;  2)  disturbance  commis-
sions caused by a spatial misalignment between the sample location and
the disturbance extent (often at the edge of a large disturbance patch),
where the sample pixels do not present an obvious change signal in the
time series but misidentified as disturbances in the LCMAP reference set
(see the example of Fig. S2 in the supplementary). Given these issues, we
randomly selected 3000 sample plots from the 24,971 total sample plots
and  manually  corrected  sample  plots  from  the  convergence  of  visual
evidence available in both temporal profiles and Landsat image chips,
backed up by referencing historical high-resolution Google imagery. We
excluded  120  sample  plots  (4.0%)  that  were  extremely  difficult  to
interpret  due  to  too  frequent  spectral  variation  (mostly  in  semi-arid

regions, see the example Fig. S3). As a result, 2880 time-series sample
plots were remained for the final model evaluation, resulting in a total of
97,920 validation cases for 34 years, which include 1230 disturbance
years  and  96,690  non-disturbance  years.  A  total  of  three  rounds  of
manual  inspection  were  given  to  all  validation  cases,  ensuring  their
correctness and consistency with the calibration dataset.

All Landsat ARD Collection 1 surface reflectance products between
1984 and 2021 (38 years) were downloaded for analysis. The Landsat
ARD products gridded all available Landsats 4–8 as tiled, georegistered,
and atmospherically corrected products defined in a common equal area
projection  (Dwyer  et  al.,  2018).  To  facilitate  model  calibration  and
evaluation,  we  cropped  a  smaller  time-series  chip  (53*53  pixels)  for
each reference plot. The width of 53 pixels was determined by covering
99% of patch-level change objects from running the default models for
four pilot tiles.

2.2. Model calibration and evaluation

F2  was chosen as the objective function for the model calibration.
Combining  the  producer’s  accuracy  (PA,  a.k.a.,  recall)  and  the  user’s
accuracy  (UA,  a.k.a.,  precision),  a  general  form  of  F-score  can  be
denoted as (Baeza-Yates and Ribeiro-Neto, 1999):

(cid:0)

1 + β2

Fβ =

)
*
β2

UA*PA
*UA + PA

(1)

F2  set β  = 2 such that PA is considered twice as important as UA,
motivated by that under-detection is more critical than over-detection
for the ensuing disturbance analysis. There is almost no effective way
for re-identifying a disturbance region if it is missed from the detection
stage, while it is often methodologically possible to eliminate commis-
sions through a spatial-contextual post processing such as sieving filter
(Ye  et  al.,  2021b)  or  through  disturbance  agent  classification  (Zhang
et al., 2022). The calculation of UA and PA for the cluster sampling is the

RemoteSensingofEnvironment287(2023)1134624S. Ye et al.

same as that from the random sampling strategy (Stehman et al., 2021).
For model evaluation, we chose the performance metrics that were
commonly  used  in  previous  disturbance  detection  studies  (Galbraith
et al., 2019; Sol´orzano and Gao, 2022; Ye et al., 2021a; Zhu et al., 2020)
concerning communication, i.e., F1 score, F2 score, user’s accuracy (UA)
and  producer’s  accuracies (PA).  To  our  knowledge,  COLD  is  the  only
algorithm  targeted  at  medium-resolution  generic  land  disturbance
detection and hence will be used as the primary baseline for comparative
analysis. The default COLD uses change probability P = 0.99 based on its
best-balanced  accuracy  (i.e.,  F1  score)  (Zhu  et  al.,  2020).  To  make  it
consistent with OB-COLD’s calibration manner, we will also report the
COLD  performance  with  P  = 0.95,  which  achieved  the  best  F2  score
based  on  the  same  calibration  dataset  (see  Table  S1  in  the
supplementary).

In  addition  to  quantitative  evaluation,  the  qualitative  assessment
was performed for eight pilot Landsat ARD tiles (see the black hollow
rectangle  in  Fig.  2),  representing  a  broad  range  of  ecoregions  and
disturbance  agent  types.  Major  land  cover  patterns  and  disturbance
agents for these eight tiles were summarized in Table 1. The evaluation
was accomplished by visually assessing OB-COLD disturbance maps in
conjunction  with  the  COLD  disturbance  maps  and  high-resolution
Google Earth imagery (Section 4.2).

3. Method

OB-COLD consisted of three steps (Fig. 3). First, OB-COLD applies
COLD  to  analyze  per-pixel  spectral  change  history  and  save  change
magnitudes at a regular temporal interval (i.e., time slice). Second, OB-
COLD reorganizes these per-pixel change magnitudes into a sequence of
image-like temporal snapshots and applies object-based change analysis
to  identify  change  regions  for  each  snapshot.  Finally,  OB-COLD  re-
produces temporal segment characterization as change records based on
the new spatially indicated breaks. It is worth mentioning that Steps 1
and 2 focus on the detection of general change processes including both
land  disturbances  and  other  ecological  processes  such  as  natural  re-
covery; land disturbance regions will be sorted out by applying a rule-
based strategy in Step 3.

3.1. Temporal change measurement

OB-COLD adapts COLD (Zhu et al., 2020), a well-established algo-
rithm for dense Landsat time-series, to analyze per-pixel spectral change
history  as  its  first  step.  Same  to  COLD,  OB-COLD  uses  the  Quality
Assessment  band  generated  by  the  Fmask  algorithm  (Zhu  and  Wood-
cock, 2012) to screen out the initial cloud, cloud shadow, and ice/snow,
and  then  applies  Tmask  (Zhu  and  Woodcock,  2014b),  a  time-series-
based outlier removal technique, to further remove remaining noises.
The only modification is that OB-COLD generates two extra outputs from
the COLD algorithm at a regular day interval, i.e., (1) the representative
change magnitude and (2) its associate change date. For a time series {xt,
t ∈ T} (T is the set of image acquisition dates), COLD identifies a spectral
break if 1) an observation xt  has a change magnitude (CMt), the mini-
mum squared norm of standardized change vectors (CV) among a peek
window (ψ) of k consecutive observations since a Julian date t, greater
than a change threshold from the chi-square distribution at a probability
of P (modified from Eq. 8 in (Zhu et al., 2020)):

CMt = min
x∈ψ

{

‖CV x‖2 }〉
χ2
P(5)

(2)

2) a mean included angle (βt) between the ith and (i + 1)th consec-
utive  observations  within  the  peek  window  is  lower  than  45
which
excludes the noisy signals that have a large variation of change direction
(Eq. 9 in (Zhu et al., 2020))

◦

βt =

1
k

∑k(cid:0) 1

i=1

βi,i+1 < 45◦

(2)

OB-COLD outputs a representative change magnitude for each time
slice at a per-pixel level to indicate the overall change likelihood for the
time  slice,  irrespective  of  break  detection.  Given  a  time  slice  ∅,  its
representative  change  magnitude  (CM∅)  combining  the  two  decision
intermediates, CMt and βt, is defined as:

CM∅ = max
tϵ∅

(CMt*F(βt) )

(3)

where F(βt) is a squashing function for penalizing those CMt that have βt
larger than the optimal mean included angle threshold given by (Zhu
◦
et al., 2020), i.e., 45

,

Fig. 3. The three-component workflow of OB-COLD. COLD: COntinuous monitoring of Land Disturbance; OB: Object-Based.

RemoteSensingofEnvironment287(2023)1134625S. Ye et al.

⎧
⎪⎪⎪⎨
⎪⎪⎪⎩

90 (cid:0)

45

F(IAt) =

1, βt < 45
IAt

0, βt > 90

◦

◦

3.2.1. Segmentation

, 45

◦ ≤ βt ≤ 90

◦

(4)

Besides,  the  ordinal  date  associated  with  each  CM∅  (i.e.,  change
date) is saved to the disk during this procedure as well, which will be an
essential component for the follow-up segmentation procedure as well as
the new break date retrieval. It is noteworthy that the OB-COLD also
looks  for  change  magnitudes  and  dates  in  a  look-backward  manner
during the process of detecting the start of a temporal segment after the
initialization stage is determined (see Fig. 4). The look-backward setting
could  improve  the  identification  of  secondary  disturbances  occurring
shortly after the first disturbance (see the example shown Fig. S4 of the
supplementary material) which are often missed for the detection during
the  normal  look-forward  detection  process  due  to  a  lack  of  an  estab-
lished time-series model.

The temporal interval of a time slice was empirically determined as
the  average days  needed for  accumulating five  observations. With  an
assumption of 50% cloud/shadow chance (Zhu et al., 2020), five tem-
poral observations ensure a probability of over 95% (i.e., 1 (cid:0) 0.55  =
96.88%) for acquiring at least one clear observation within this interval.
Landsat ARD dataset ideally has a temporal density of 8 days with two
sensors,  however,  the  overall  average  density  since  1984  is  between
eight to 16 days due to single-sensor operation before 2000 as well as the
Landsat 7 SLC-off issue. We chose a middle density, i.e., 12 days, and
thus the day interval for a time slice was defined as 12 days * 5 obser-
vations = 60 days.

Once  COLD  is  finished  and  regular-interval  change  measurements
are generated for all pixels, OB-COLD reorganizes these per-pixel change
magnitudes and dates into image-like snapshots indexed by time (see the
examples of Fig. 5A and B). Given that a change patch might be broken
into two consecutive snapshots due to a variety of factors such as cloud/
shadow  and  SLC-off  issues,  change  measurements  from  the  earlier
snapshot were used to fill “NA” values in the current change snapshot,
with a goal of generating more spatially contiguous patches. Hence, the
change dates in Fig. 5B also include the dates prior to the current pro-
cessing time slice.

3.2. Object-based change analysis

Object-based change analysis was applied to process time-stamped
change  magnitude  snapshots  following  a  pipeline  of  segmentation,
property extraction, and change decision.

This sub-step targets extracting two-level candidate change objects
from  each  change  measurement  snapshot.  It  is  practically  difficult  to
directly  extract  meaningful  change  objects  as  some  disturbance  sites
have  considerable  internal  variability,  therefore  we  applied  an  over-
segmentation to generate a lower level of the object representation as
change superpixels, pertaining the best boundary information. To derive
change superpixels, OB-COLD first applies a gaussian filter with a kernel
size  σ  = 1  on  a  change-magnitude  snapshot,  defines  the  initial  seed
pixels as the pixels with a change magnitude higher than χ0.90
(5), and
then  implements  a  mask-based  Flood  Fill  segmentation  (Bradski  and
Kaehler, 2000) to generate change superpixels. The pixel at (x, y) within
the 8-connectivity neighborhood is considered to belong to the super-
pixel of the seed pixel if its change magnitude (CM∅) and date (CD∅)
meet the below conditions:

2

(1 (cid:0) λ)*CM∅(xseed, yseed) ≤ CM∅(x, y) ≤ (1 + λ)*CM∅(xseed, yseed)

|CD∅(x, y) (cid:0) CD∅(xseed, yseed) |〈time slice interval

(5)

(6)

λ  is  a  factor  that determines  a  fixed range  centered at  the  change
magnitude of seed pixel to connect neighborhood pixels; λ = 0.4 and λ =
0.3 have the same F2 from the parameter sensitivity test (Table S1 in the
supplementary),  and  λ  = 0.4  was  chosen  due  to  its  better  efficiency
(higher λ means less oversegments). Eq. (6) aims to exclude those pixels
that have a change date interval longer than the time slice length with
seed  pixels,  which  were  brought  by  the  preprocessing  of  filling  NA
values using the earlier snapshot. Once a filling is finished, a mask will
be updated by adding the newly filled pixels to speed up the processing
for the next seed, until all seeds are processed. Admittedly, the Flood Fill
algorithm is not a typical superpixel segmentation approach; we chose
the Flood Fill because it exhibited the highest accuracy compared to the
other two popular superpixel algorithms, including Simple Linear Iter-
ative Clustering (SLIC) (Achanta et al., 2012) and watershed (Neubert
and  Protzel,  2014)  (Table  S1  in  the  supplementary).  This  might  be
because  SLIC  and  watershed  algorithms  were  originally  designed  for
high-resolution color images which are not optimal for segmenting 30-m
change snapshots.

After the Flood Fill segmentation is finished, change-patch objects at
a  broad  spatial  context  are  produced  by  merging  adjacent  change
superpixels, with a hypothesis that adjacent pixels presenting spectral
change within a short time are under the same change process regardless
of  their  distinct  inter-group  change  magnitudes  (see  the  example  of
Fig. 5D). The two levels of change objects will be used to extract object
properties. We tested detection performance under different scale stra-
tegies:  1)  change  superpixel  only;  2)  change  patch  only;  3)  change
superpixel and patch. The combination of change superpixel- and patch-

Fig. 4. Bidirectional change magnitude outputs and break identification in OB-COLD: OB-COLD saves intermediate change magnitudes from the COLD algorithm for
each time slice (i.e., a regular temporal interval) in both forward and backward direction, after an initialization window is established. COLD: COntinuous monitoring
of Land Disturbance; OB: Object-Based.

RemoteSensingofEnvironment287(2023)1134626S. Ye et al.

Fig. 5. An example site (Lat: 41.4761; Lon: (cid:0) 88.0881; ARD tile: H021V008) for illustrating several key steps within object-based change analysis for processing a
time slice (05/31/2003–07/30/2003), coupled with its related Landsat true color composite chips (the red rectangles highlight the images collected within the time
slice). A) the change magnitude snapshot and B) the change date snapshot; C) the change superpixel obtained by Flood Fill segmentation; D) the change patch
generated by merging adjacent superpixels; E) the final change map through object-based change decision which could eliminate the superpixels with extremely low
change  magnitudes.  ARD:  Analysis  Ready  Data.  (For  interpretation  of  the  references  to  color  in  this  figure  legend,  the  reader  is  referred  to  the  web  version  of
this article.)

information  showed  the  best  F2  (see  Table  S1

level
supplementary).

in  the

3.2.2. Object-level property extraction

OB-COLD  assigns  three  object-level  change  properties  to  each
candidate superpixel, relating to 1) spectral, 2) spatial, and 3) thematic
features. The spectral property for a candidate superpixel is calculated as
the average change magnitude of its membership pixels, indicating the
overall spectral change intensity for this superpixel.

The spatial property is derived as the size of the change patch that a
superpixel  belongs  to,  which  indicates  the  concurrent  change  area
occurring for a time slice. Rather than the superpixel-level objects that
are  not  meaningful  geographic  objects  due  to  the  over-segmentation
process,  patch-level  objects  can  provide  a  broad  view  for  concurrent
change as evidence for a real change process against noises which usu-
ally present a random speckle pattern in both space and time.

(6) wetland, (7) ice and snow, and (8) barren. OB-COLD generates a total
of  20,000  training  sample  pixels  is  generated  following  the  sampling
protocol provided in Zhu et al. (2016), applies the random-forest model
to predict yearly land cover maps, and finally extracts the dominant pre-
change cover type for each superpixel by overlaying the superpixel maps
with the classified land-cover map at one year prior to its time slice (∅),

3.2.3. Object-based change decision

To  a  superpixel  k  at  a  time  slice  ∅,  the  general  change  decision
function that adjusts the object-level change magnitude by the object
size is denoted as:

CMag∅,k*scale factor > χ2

P(5)

where

scale factor = 0.95 +

(cid:0)

log10N∅,k

)
*S

(8)

(9)

The thematic property, as an optional object-level property for OB-
COLD,  requires  a  pre-existing  land-cover  map  as  the  input  (see  the
dash line in Fig. 2). COLD change records from the first step “temporal
change  measurement”  define  an  intercept,  a  slope  and  three  sets  of
harmonic components for each temporal segment:
(
) }

{

)

(

∑3

̂ρi,t = a0,i +

ak,icos

k=1

2kπ
T

2kπ
T

t

+ bk,isin

t

+ c1,it

(7)

where ̂ρi,t  is the predicted reflectance for the ith Landsat Band at Julian
date t, a0, i is the intercept coefficient, ak, i and bk, i are kth order seasonal
harmonic coefficients, c1, i represents the slope coefficient. To speed up
processing, we selected 21 annual COLD predictors derived from COLD
change records as inputted features for classification, consisting of seven
overall predicted surface (a0,  i + c1,  it07(cid:0) 01(cid:0) year, i = 1, 2, …, 7th Bands)
and  14  intra-annual coefficients  of the  time segment  representing 1st
order seasonality (a1,  i,  year  and b1,  i,  year, i = 1, 2, …, 7th Bands). OB-
COLD  first  builds  a  localized  random-forest  model  by  coupling  a
single-year pre-existing map with the annual COLD predictors for the
year  of  the  map.  For  this  study,  we  used  2001  LCMAP  land-cover
product  as  the  seed  map,  following  the  LCMAP  classification  system
which defines eight primary land cover types (Brown et al., 2019), i.e.,
(1) tree cover, (2) developed, (3) wetland, (4) grass/shrub, (5) waterbodies,

CMag∅,k is the average change magnitude of a change superpixel. The
scale_factor is a function of the object size of its associated patch size (N∅,
k, unit: pixel number). The intercept “0.95” indicates that OB-COLD only
decreases the average change magnitude for the single-pixel change (N∅,
k  = 1) by 5%, which ensures a good performance in a heterogeneous
environment where a change entity is small-sized and even smaller than
Landsat  pixel  resolution  (i.e.,  L-resolution).  The  larger  change  patch
leads to a higher scale_factor, hence a lower average change magnitude is
needed to hit the change threshold. P and S are two key OB-COLD pa-
rameters  requiring  careful  calibration.  P  determines  the  chi-square
2(5)  (OB-COLD  and  COLD  both  use  five  spectral
change  threshold  χP
bands for calculating change magnitudes, so the degree of freedom is 5).
S is a size factor that controls the weight of change patch size (N∅, i) in
the decision function: when S = 0, only the average change magnitude is
considered; a larger S yields more weights to the concurrent change area
in the decision function.

This  study  will  examine  OB-COLD  under  two  parameterization
modes:  the  unimodal  and  the  bimodal  OB-COLD.  The  unimodel  OB-
COLD  is  implemented  in  the  absence  of  an  existing  land-cover  map,
which applies a single set of model parameters (P, S) to all superpixels.
Our  grid-searching  parameter  test  shows  that  the  parameter  set  (P  =

RemoteSensingofEnvironment287(2023)1134627S. Ye et al.

0.95, S = 0) is optimal under the unimodel situation given by its best F2
score (Fig. S5 in the supplementary).

The bimodel OB-COLD (the default option) additionally requires a
seed cover map for generating object-level thematic properties to guide
applying different model parameter specifications. The two-strata land
cover system (“fluctuated” vs “stable”) was designed to achieve a bal-
ance  between  adequate  per-stratum  sample  number  and  acceptable
model specificity based upon Disturbance-to-Noise Ratio (DNR). DNR is
defined  as  the  ratio  of  the  disturbance  superpixels  confirmed  by  the
reference sample plots to the noisy superpixels (i.e., superpixels in those
no-disturbance years). Noisy superpixels (or commission error objects)
are often associated with regional change processes that belong to nat-
ural variabilities, such as climate variability, and ideally, present lower
change magnitudes or smaller change patches in their attribute scatter
plot. The fluctuation model is designed for the superpixels whose major
pre-change  categories  have  relatively  low  DNR:  cropland,  grass/shrub,
water, ice/snow, and barren (Fig. 6D-E); the lower DNR indicates a higher
proportion  of  noisy  superpixels  and  therefore  higher  spectral  fluctua-
tion, suggesting a conservative model parameterization is necessitated
for keeping a low commission error rate. On the other hand, the stable
model  is  applied  to  identify  disturbances  occurring  on  the  rest  three
cover types, i.e., tree cover, developed, and wetland (Fig. 6A-C), which has
been also echoed by the past studies in forest regions (Ye et al., 2021b)
or  in  wetland  areas  (Yang  et  al.,  2022),  suggesting  a  more  sensitive
change parameterization for these cover types.

Under the bimodel OB-COLD, for a superpixel object k in a time slice
∅ with its known pre-change category LC∅,  k, OB-COLD identifies it as
the change superpixel when:
)〉

0.95 + log10N∅,k*Ss

χ2
Ps

(5), if LC∅,k ϵ stable stratum

(cid:0)
CMag∅,i*

(cid:0)
CMag∅,i*

0.95 + log10N∅,k*Sf

)〉

χ2
Pf

(5), if LC∅,k ϵ fluctuated stratum

(10)

(11)

where (Ps, Ss) and (Pf, Sf) are the two parameter sets respectively for the
stable and fluctuated models. To obtain the best parameter set for each
model, we separated our calibration change sample plots into these two
strata based on their pre-change categories predicted from the random-
forest model (Section 3.2.2) and performed a grid-searching parameter
test  for each  group. The grid-searching  results (Fig.  S5  in the  supple-
mentary) suggested the parameter set (Ps = 0.95, Ss = 0.1) was the best
for the stable model, while (Pf = 0.99, Sf = 0.05) was the optimal for the
fluctuated model due to its highest F2 score.

3.3. Change records reconstruction and disturbance extraction

For the final step, OB-COLD generates new change records that have
a consistent temporal variable set with the standard COLD (Zhu et al.,
2020). OB-COLD first produces new breaks at a per-pixel level by linking
resultant change maps from the second step with change date snapshots,
and then recursively selects the breaks that have a day interval of at least
365 days with the last break, concerning that each temporal segment
should have at least one-year interval for an efficient model fitting. As
followed, a two-step protocol is applied to eliminate outliers: 1) Tmask
(Zhu et al., 2019) and 2) non-consecutive outlier removal with a change-
probability  threshold  of  0.99999  based  on  LASSO  (Least  Absolute
Shrinkage and Selection Operator) model fitting. An 8-coefficient LASSO
regression is built using the remaining observations to produce the final
harmonic coefficients for each temporal segment.

The disturbance extraction in OB-COLD follows the same physical-
rule-based  approach  described  in  Zhu  et  al.  (2020).  Given  that  OB-
COLD additionally searches breaks in the looking-back procedure and
may  cause  commission  errors,  OB-COLD  introduces  the  second  non-
disturbance  break  type  called  “flipping  break”  besides  regrowth-
related breaks. Flipping breaks represent a type of break linked to the
end  of  a  disturbance  process,  which  has  an  opposite  spectral  change
direction from the previous disturbance. More details on flipping breaks

Fig. 6. Object-based attribute scatter plot and per-category Disturbance-to-Noise Ratio (DNR) based on calibration sample plots. Disturbance superpixels are those
superpixels  that  intersect  the  pixel  location  of  a  reference  sample  and  coincide  with  its  disturbance  year  (correct  objects),  while  noisy  superpixels  are  those
superpixels that intersect the sample pixel locations but occur in the no-disturbance years (commission error objects). DNR is the ratio of disturbance superpixel
number to noisy superpixel number. The number in the parathesis within each sub-title indicates the total number of candidate change superpixels.

RemoteSensingofEnvironment287(2023)1134628S. Ye et al.

will be given in Section S2 in the supplementary material.

4.2. Qualitative assessment

The COLD algorithm was written in the C language wrapped with
Python API, and other components for OB-COLD were written in python;
the  open-source  package  is  freely  downloadable  from  https://github.
com/GERSL/pycold.

4. Results

4.1. Quantitative assessment

The quantitative evaluation based on 2880 reference plots (Fig. 7)
illustrates that the bimodel OB-COLD achieved the best F1 (0.666) and F2
accuracy (0.724). While its UA was similar to the COLD with the default
change  probability  (COLD–t99)  (58.7%  vs.  57.8%),  the  bimodel  OB-
COLD  yielded  a  significantly  higher  PA  than  the  default  COLD  by
16.3% (76.9% vs. 60.6%), indicating that the primary enhancement of
the bimodel OB-COLD was at reducing omission errors compared to the
default COLD. Without considering pre-change cover types, the unim-
odel OB-COLD showed similar PAs with the bimodel (75.7% vs. 76.9%),
however, at an expense of a much lower UA (46.5% vs 58.7%). As both
were  calibrated  under  F2  objective,  the  unimodel  OB-COLD  achieved
12.2% F2  increase compared to COLD – 95, indicating that the object-
based components other than thematic components, such as segmenta-
tion procedure and object-level change decision, also greatly contribute
to  the  accuracy  improvement.  The  default  COLD  exhibited  the  best
balance on UA and PA because it was the only approach that was cali-
brated based on F1, though its F1  was still lower than the binary OB-
COLD. The COLD under the best F2, i.e., COLD–t95, had the lowest F1
and F2 partly due to its extremely high commission errors (UA = 31.5%).
Disturbance  detection  accuracies  on  the  individual  cover  type
(Fig. 8) shows a large performance variation among different pre-change
land status. Disturbance detection on tree cover (mostly relating to forest
disturbances) presented the highest performance among all cover types,
with  relatively  balanced  UA  and  PA:  the  binary  OB-COLD  achieved
>80%  on  both  PA  and  UA.  The  types  cropland  and  grass  &  barren
generally  showed  the  lowest  detection  performance  because  of  their
high disturbance commissions (no approaches could achieve >50% UA).
Water/ice  and  wetland  presented  high  PA  (~80%)  and  moderate  UA
(~60%) (except COLD-t99 on wetland, PA = 61.4% and UA = 77.3%).
For  cross-approach  comparison,  the  bimodel  OB-COLD  obtained  the
highest PA for developed (68.0%), tree cover (82.3%), water/ice (88.2%),
and wetland (88.0%), while the unimodel OB-COLD achieved the highest
for the rest two (cropland: 78.1%; grass & barren: 75.7%). COLD–t99 had
the highest UA for most cover types (developed: 60.3%; cropland: 44.1%;
grass  &  barren:  43.8%;  tree  cover:  86.7%;  wetland:  77.3%),  except  for
water/ice (the bimodal OB-COLD: 65.2%).

The qualitative assessment shows that the default COLD approach
(COLD–t99) presented under-detection for beetle outbreak, forest har-
vest,  construction,  and  cropland  conversion  (see  the  example  regions
Fig. 9A, D, E, and G). COLD-t99 missed the detection for some pixels of
the newly built solar panel site possibly because the transition from bare
land to solar panels did not always present significant spectral change
from  their  temporal  profile,  while  the  OBIA  procedure  in  OB-COLD
enabled  the  capture  of  a  more  complete  geometry  for  the  new  solar
panel  site  as  it  considers  spatially  concurrent  change.  The  COLD
approach under the F2  objective (COLD–t95) presented more commis-
sion errors and salt-and-pepper noise for semiarid regions (Fig. 9F, H),
and exhibited some omission errors/partial detection for wetland con-
dition change induced by the Irma hurricane (Fig. 9C). Compared to the
pixel-based approach, the unimodel and the bimodel OB-COLD gener-
ally  produced  more  complete  disturbance  patch geometry  with  fewer
omission  errors.  The  bimodel  OB-COLD  performed  better  than  the
unimodel for the subtle disturbances such as beetle outbreak (see Fig. 9
B).

4.3. Detection rates by disturbance agents

The detection rates (i.e., PA) were also evaluated against six primary
disturbance  agents  (Fig.  10).  Generally,  harvest  reached  higher  accu-
racies (COLD-t95, unimodel, the bimodel OB-COLD had over 80% PA),
while a lower detection rate was shown for fire and stress (all approach
obtained <70% PA) possibly due to their relatively higher proportion of
subtle-change  cases (such as  understory  fire  and insect  disturbances).
For cross-approach comparison, the default COLD (COLD–t99) exhibited
the lowest PA because the default COLD was calibrated for a balanced
accuracy.  The  unimodel  and  the  bimodel  OB-COLD  presented  similar
PAs (the largest difference is 3.4% in stress), but higher PAs than the
pixel-based  approaches  (COLD–t95  and  COLD–t99)  at  all  agents,
particularly for the stress category where the OB-COLD achieved 19.1%
accuracy gain compared to the default COLD approach.

5. Discussion

5.1. Novelty of OB-COLD

A  traditional  way  of  introducing  OBIA  into  the  time-series-based
approach is postprocessing pixel-based detection results by connecting
spatially and temporally adjacent break pixels into change-process ob-
jects (Hermosilla et al., 2015; Kennedy et al., 2015; Qiu et al., 2022),
which we called “objectifying detection”. This post-processing step for
labeling objects is performed after the detection is finished, and rarely

Fig. 7. Performance comparison among the pixel-based COLD algorithm under the threshold of 95% change probability (COLD-t95), the COLD algorithm with 99%
change probability (COLD-t99), the unimodel OB-COLD, and the bimodel OB-COLD. COLD: COntinuous monitoring of Land Disturbance; OB: Object-Based.

RemoteSensingofEnvironment287(2023)1134629S. Ye et al.

Fig. 8. Producer’s (PA) and user’s accuracy (UA) for six pre-change land cover categories. The number in the parathesis within each sub-title indicates the change
case number. The cover types were acquired by the annual land cover maps from the bimodel OB-COLD procedure. Note that COLD–95 and unimodel OB-COLD
achieved identical PA and UA in F) Water/Ice so that their scatter dots were overlapped. COLD: COntinuous monitoring of Land Disturbance; OB: Object-Based.

alters the general detected region, so the accuracy of the resultant map is
mostly  contingent  on  the  upstream  pixel-based  temporal  analysis.
Differently, OBIA/spatial information is employed as the key component
of  OB-COLD  to  delineate  and  identify  disturbance  regions  during  the
detection  process  (hereafter  named  “detecting  objects”).  The  spatial
information  was  exhaustively  analyzed  in  OB-COLD  mainly  by  two
steps: 1) segmenting a layer of soft change measurement from a tem-
poral domain (i.e., change magnitude) to generate potential disturbance
patch  boundaries,  ensuring  the  geometric  completeness  of  detected
patches regardless of the heterogeneity of within-patch spectral change;
2) leveraging the spatial (e.g., patch size) and the thematic object-level
features (e.g., pre-change cover types) to discriminate disturbance sig-
nals from a variety of data noise and climate-induced ephemeral change.
As a result, OB-COLD could possibly result in a very dissimilar distur-
bance map with the “objectifying detection” approach, which is exem-
plified  by  an  insect-affected  site  shown  in  Fig.  11:  the  disturbance
patches  derived  from  OB-COLD  (Fig.  11C)  presented  a  better  spatial
pattern for capturing spectral changes in Fig. 11A, while the COLD re-
sults (Fig. 11B) missed some parts of the insect-affected region where the
time-series  profile  showed  an  obvious  window  of  decreasing  NIR
(Fig.  11E),  even  though  the  same  model  parameterization  (change
probability = 0.95) was used for both. The accuracy improvement could
be also substantiated by our quantitative assessment which showed the
PA of COLD-t95 was lower than that of the two OB-COLD approaches by
at least 10%.

Of particular note is that object-level thematic information greatly
contributes  to  accuracy  improvement  by  enabling  multiple  cover-
specific model parameterizations to be applied for generic land distur-
bance mapping. Compared to the unimodel OB-COLD, the bimodel OB-
COLD  significantly  enhanced  UA  by  10.9%  (Fig.  7).  Specifically,  the
bimodel  OB-COLD  had  lower  disturbance  over-detection  for  cropland
and barren/grass cover types (see Fig. 8) because a more conservative
parameter set for the fluctuated group was applied to these two cover
types. Thematic information has been widely used as a cover mask layer
to guide cover-specific disturbance detection in previous studies (Tang
et al., 2019; Yang et al., 2022; Ye et al., 2021b). Assuming that the cover

type is static, most of these studies did not deal with new land covers
emerging  outside  the  mask  layer.  By  generating  and  applying  annual
cover maps from a seed map, OB-COLD provides an easy-to-use frame-
work for incorporating dynamic thematic information for mapping full-
category  or  cover-specific  disturbances.  OB-COLD  applies  a  robust
approach based on a pixel-level majority vote to determine the thematic
property for a change superpixel, which compensates for classification
accuracy degradation brought by a lack of accessory datasets compared
to LCMAP’s CCDC implementation (Zhu et al., 2016). In practice, OB-
COLD  can  be  implemented  under  an  unimodel,  bimodel  or  n-modal
setting (n≤ the total number of cover categories). Our python package
provides an interface for allowing users to define a customized n-modal
system: finer model stratification will enhance the overall accuracy, and
as  a  trade-off,  requires  a  more  sophisticated  calibration  for  increased
cover-specific parameter sets (P, S).

Lastly, OB-COLD provides a novel computationally scalable frame-
work for approaching the grand challenge of large-scale spatiotemporal
complexity: the steps of “temporal change measurement” and “change
record construction” can be paralleled at the per-pixel level, and the step
of “object-based change analysis” is performed on an image-based par-
allelization. Compared to the direct 3-D segmentation in a space-time
cube that is popular in video processing (e.g., Moscheni et al., 1998),
the  “time-space-time”  workflow  has  better  scalability,  because  each
parallelization  unit  in  each  step  is  completely  independent  without
communications overhead between CPUs. Our efficiency tests show that
the  binary  OB-COLD  costs  1.62  times  the  computing  hours  than  the
original COLD (see Section S4 of the supplementary material). For the
operational stage, the bimodal OB-COLD can use existing annual land
cover products such as LCMAP land cover products (Xian et al., 2022) to
save time for generating annual cover maps, which would result in the
same computing time as the unimodal OB-COLD (only 1.37 times than
the original COLD).

To summarize, OB-COLD innovates the traditional pixel-based time
series  analysis  and  other  spatiotemporal  change  detection  algorithms
mainly  from  three  perspectives:  1)  fully  integrating  OBIA  into  the
change-detection process rather than object labeling; 2) incorporating

RemoteSensingofEnvironment287(2023)11346210S. Ye et al.

Fig. 9. Map comparison of the default COLD (COLD-t95), the COLD under the F2 objective (COLD-t99), the unimodel OB-COLD, and the bimodel OB-COLD from the
pilot Landsat ARD tiles for this study. The site locations: beetle outbreak – Rocky Colorado (h011v009); hurricane – South Florida (h027v019); forest management –
Mississippi River Lowlands (h021v015); construction – New England (h030v006); agricultural practice – Corn Belt Plain (h021v008); drought– Western Great Plains
(h014v006). COLD: COntinuous monitoring of Land Disturbance; OB: Object-Based; ARD: Analysis Ready Data.

thematic  information;  3)  enabling  a  computationally  scalable  frame-
work to address spatiotemporal data complexity. On recognizing “land
change”  as  multiscale  objects  and  examining  their  change  properties
from  a  time-series  dataset,  OB-COLD  is  essentially  different  from  the
past  time-series  studies  which  segmented  static  landscape  objects  as
analytic  objects  (Hughes  et  al.,  2017;  Yin  et  al.,  2018)  and  various
object-based change detection techniques based on an image pair (e.g.,
Chen et al., 2012; Im et al., 2008; Liu et al., 2021; Wan et al., 2019;
Zheng et al., 2021). As a spatiotemporal algorithm that makes exhaus-
tive  use  of  spatial  information  for  generic  disturbance  mapping,  OB-
COLD distinguished itself from other CCDC-like improvements such as
temporal  segment  refinement  (Bullock  et  al.,  2020a)  and  spectral
unmixing integration (Bullock et al., 2020b; Chen et al., 2021), which
investigates spectral changes only from temporal domain and mainly set
focus on forest disturbances.

5.2. Limitation and future work

Generally, the accuracies reported in this study were lower than the
previous study targeting generic land disturbance (UA and PA > 70%,
Zhu  et  al., 2019),  which  was  primarily  due  to two  reasons.  First, the
validation in Zhu et al. (2019) was based on Cohen’s dataset generated
from  a  forest-oriented  sampling  strategy,  while  forest  cover  has  the
highest disturbance detection accuracy (see Fig. 8D). The use of a forest-
oriented  validation  set  would  result  in  higher  accuracy  than  using  a
purely  random  sampling  dataset.  Second,  we  incorporated  the  recent
updates on the COLD algorithm including a new single-path strategy: for
the overlapped region between two paths, only observations from the
path with the smaller view zenith angle (Qiu et al., 2022) remained as
the algorithm inputs. This strategy increased consistencies among wall-
to-wall  disturbance  mapping,  but  as  a  trade-off,  the  decreased  data
density negatively impacted detection accuracies, particularly for short-
interval disturbances such as gypsy moth (Zhu et al., 2022). Despite the
overall performance improvement,  the binary OB-COLD still only has

RemoteSensingofEnvironment287(2023)11346211S. Ye et al.

Fig.  10. Agent-specific  producer  accuracies  based  upon  an  assemblage  of  calibration  and  evaluation  set.  Note  that  we  reclassed  some  categories  due  to  in-
consistencies of agent systems between Cohen’s and LCMAP reference datasets: for LCMAP reference datasets, spectral decline and structural decline were combined
into the stress category; for Cohen’s reference datasets, wind was merged to other due to its small sample number (only 11 cases). LCMAP: Land Change Monitoring,
Assessment, and Projection.

“objectifying  detection”

Fig. 11. A sample pixel affected by west-
ern  spruce  budworm  (indicated  by  aerial
surveying  dataset)  from  the  center  Wash-
ington  (Lat:  47.3068;  Lon:  (cid:0) 120.6689;
Cascades  Plateau  -  H004V002)  for  exem-
plifying
vs
“detecting  objects”.  A)  depicts  a  spatial
pattern  of  contiguous  increased  change
magnitudes induced by spruce infestation
from  a  change  magnitude  snapshot  (04/
22/2011–06/21/2011);  B)
labels  con-
nected pixels of a yearly COLD disturbance
map  (the  year  of  2011,  0.95  change
probability)
into  multiple  disturbance
patches  (the  colors  represent  different
patches),  i.e.,  “objectifying  detection”;  C)
shows  disturbance  patch  map  generated
from  the  yearly  binary  OB-COLD  distur-
bance  map  (the  year  of  2011,  the  colors
represent different patches); E) and F) ex-
emplifies  the  time-series  profile  showing
that “objectifying detection”  missed some
insect-affected regions where the time se-
ries
shows  an  obvious  window  of
decreasing NIR. COLD: COntinuous moni-
toring  of  Land  Disturbance;  OB:  Object-
Based.

58.7% UA, meaning a high level of over-detection. This is partly because
we intentionally calibrated a biased model by F2, which put less weight
on commission than omission errors. Commission errors mainly occur
on the cover types cropland and grass/barren, accounting for 73% of the
total  commissions.  The  over-detections  were  mainly  attributed  to
climate  variability  and  intra-annual  variation  of  agricultural-practice
timing  which  often  leads to  a  large-area spatial pattern of  ephemeral
spectral reflectance change. Such change processes were excluded from
our  disturbance  definition,  following  the  most  common  disturbance
detection protocol (Pengra et al., 2020; Zhu et al., 2019). But agricul-
tural  practices  and  climate  variability  might  be  of  interest  to  other
domain-specific  studies  (e.g.,  Huete,  2016;  Seddon  et  al.,  2016),  and
could be potentially separated out by causal agent classification tech-
niques, such as in Zhang et al. (2022).

Different  from  traditional  change  detection  based  on  two  time
points, satellite time series provides a long span of land surface dynamic
history which uniquely allows for an examination of land change from
multiple spatiotemporal scales. In OB-COLD, a fine temporal grain (i.e.,
a two-month interval for deriving objects) is chosen for the detection
purpose so that we can accurately capture the change date as close to its
emergence  date.  The  temporal  interval  for  generating  change  objects
could be adjusted as needed by the monitoring tasks or based on the
temporal  resolution  of  the  original  dataset,  laying  a  solid  foundation
toward  near  real-time  monitoring  adaption  at  a  daily  or  weekly  tem-
poral scale in future. On the other hand, a broad temporal scale might be
preferable for the downstream disturbance characterization, especially
for those long-term change processes such as forest degradation (Med-
dens  and  Hicke,  2014)  and  urbanization  (Taubenb¨ock  et  al.,  2012).

RemoteSensingofEnvironment287(2023)11346212S. Ye et al.

While disturbance characterization is beyond the scope of this study, the
accurate  delineation  of  change  superpixel  and  patches  provide  a  pre-
requisite  for  generating  high-quality  change-process  objects,  which
could be further used for disturbance characterization. The future study
will be directed to establish a graph model that connects those spatially
and temporally adjacent change patches identified by OB-COLD, similar
as Wu et al. (2021) did. Compared to post-processing annual disturbance
detection maps, such graph models could remove the annual bounds for
defining a long-term change process and open a door for a plurality of
GIS-like  spatiotemporal  analysis  and  database  techniques,  revolution-
izing  current  disturbance  process  analytic  tools  and  database
management.

OB-COLD could be easily adapted for other Landsat-like time series
datasets,  such  as  10-m  Sentinel-2  or  Harmonized  Landsat  Sentinel-2
(HLS),  which  has  the  potential  for  further  enhancing  the  mapping
capability. For example, the Sentinel-2 dataset has been reported to be
superior to Landsat images for detecting small-scale disturbances such as
selective  logging  (Lima  et  al.,  2019);  same  as  COLD  and  the  LCMAP
products, OB-COLD uses a peek window of six consecutive Landsat ob-
servations  to  identify  a  disturbance  signal  and  thereby  likely  missed
detection for those short-lived disturbances such as flash floods, which
could be better detected using denser time series such as HLS dataset
(Tulbure et al., 2022).

Declaration of Competing Interest

None.

Data availability

Data will be made available on request.

Acknowledgment

This work has been supported by USGS-NASA Landsat Science Team
(LST) Program for Toward Near Real-time Monitoring and Character-
the  Conterminous  US
ization  of  Land  Surface  Change
(140G0119C0008). The content of this document does not necessarily
represent the views or policies of the Department of the Interior, nor
does  mention  of  trade  names,  commercial  products,  or  organizations
imply endorsement by the U.S. Government.

for

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.

org/10.1016/j.rse.2023.113462.

6. Conclusion

References

We developed a novel algorithm named “Object-Based COntinuous
monitoring of Land Disturbance” (OB-COLD) for detecting land distur-
bances which could make better use of spatial contexts – often neglected
- for the dense time-series analysis. OB-COLD is built upon the concept
“concurrent  change”,  a  group  of  spatially  adjacent  pixels  that  are
experiencing similar spectral changes within a short time interval. To
extract  and  analyze  concurrent  change,  OB-COLD  generates  change
snapshots stamped by a series of time slices, groups spectrally similar
change pixels into two levels of change objects, and then applies object-
level change decision for each snapshot. The benefits of a such workflow
are three-folded. First, OB-COLD inherits a temporal view from a well-
established  time-series  algorithm,  i.e.,  COLD,  which  measures  the
spectral changes relative to the historic natural variability and applies a
peek window of consecutive observations for robust change magnitude
calculation.  Second,  change  magnitude  snapshots,  as  a  soft  measure-
ment of concurrent change, are an effective proxy for spectral change
induced by a single change process, facilitating a spatial examination of
change regions. Lastly, object-level properties introduce new insights for
change detection and enhance detection accuracy, particularly for subtle
change  processes:  the  change  patch  size  reflects  concurrent  change
extent from a broad spatial context, as a strong indicator for real change
processes against data noises; the incorporation of object-level thematic
information  enhances  model  specificity  by  applying  cover-specific
model  parameterizations.  Compared  to  the  default  COLD  algorithm,
the new algorithm improves land disturbance detection accuracies by
significantly  increasing  PA  (+16%)  without  degraded  UA.  Despite
~40% of commission errors, most commission errors (73%) are attrib-
uted to agricultural practices and climate variability. The proposed al-
gorithm  owns  high  algorithmic  transparency  and  computationally
scalability for large-scale datasets with advanced computing resources,
holding  great  potential  as  the  base  detection  algorithm  for  the  next
generation of land disturbance products.

CRediT authorship contribution statement

Su Ye: Conceptualization, Methodology, Software, Writing – original
draft. Zhe Zhu: Conceptualization, Writing – review & editing. Guofeng
Cao: Writing – review & editing.

Achanta, R., Shaji, A., Smith, K., Lucchi, A., Fua, P., Süsstrunk, S., 2012. SLIC superpixels

compared to state-of-the-art superpixel methods. IEEE Trans. Pattern Anal. Mach.
Intell. 34, 2274–2282.

Baeza-Yates, R., Ribeiro-Neto, B., 1999. Modern information retrieval. ACM press, New

York.

Baumann, M., Ozdogan, M., Wolter, P.T., Krylov, A., Vladimirova, N., Radeloff, V.C.,

2014. Landsat remote sensing of forest windfall disturbance. Remote Sens. Environ.
143, 171–179.

Belgiu, M., Csillik, O., 2018. Sentinel-2 cropland mapping using pixel-based and object-
based time-weighted dynamic time warping analysis. Remote Sens. Environ. https://
doi.org/10.1016/j.rse.2017.10.005.

Bian, L., 2007. Object-oriented representation of environmental phenomena: is

everything best represented as an object? Ann. Assoc. Am. Geogr. https://doi.org/
10.1111/j.1467-8306.2007.00535.x.

Blaschke, T., 2010. Object based image analysis for remote sensing. ISPRS J.

Photogramm. Remote Sens. https://doi.org/10.1016/j.isprsjprs.2009.06.004.
Blaschke, T., Hay, G.J., Kelly, M., Lang, S., Hofmann, P., Addink, E., Feitosa, R.Q., Van
der Meer, F., Van der Werff, H., Van Coillie, F., 2014. Geographic object-based image
analysis–towards a new paradigm. ISPRS J. Photogramm. Remote Sens. 87,
180–191.

Bradski, G., Kaehler, A., 2000. OpenCV. Dr. Dobb’s J. Softw. Tools 3, 120.
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,

Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K.,
Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D.,
Reker, R.R., Rover, J., 2019. Lessons learned implementing an operational
continuous United States national land change monitoring capability: the land
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens.
Environ. https://doi.org/10.1016/j.rse.2019.111356.

Carey, R.O., Migliaccio, K.W., Li, Y., Schaffer, B., Kiker, G.A., Brown, M.T., 2011. Land

use disturbance indicators and water quality variability in the Biscayne Bay
Watershed, Florida. Ecol. Indic. 11, 1093–1104.

Chen, G., Hay, G.J., Carvalho, L.M.T., Wulder, M.A., 2012. Object-based change

detection. Int. J. Remote Sens. 33, 4434–4457.

Cleve, C., Kelly, M., Kearns, F.R., Moritz, M., 2008. Classification of the wildland–urban

interface: a comparison of pixel-and object-based classifications using high-
resolution aerial photography. Comput. Environ. Urban. Syst. 32, 317–326.
Cohen, W.B., Healey, S.P., Yang, Z., Stehman, S.V., Brewer, C.K., Brooks, E.B.,

Gorelick, N., Huang, C., Hughes, M.J., Kennedy, R.E., 2017. How similar are Forest
disturbance maps derived from different landsat time series Algorithms? For. Trees
Livelihoods 8, 98.

Cohen, W.B., Yang, Z., Healey, S.P., Kennedy, R.E., Gorelick, N., 2018. A LandTrendr

multispectral ensemble for forest disturbance detection. Remote Sens. Environ. 205,
131–140.

Cohen, W.B., Yang, Z., Kennedy, R., 2010. Detecting trends in forest disturbance and
recovery using yearly landsat time series: 2. TimeSync—Tools for calibration and
validation. Remote Sens. Environ. 114, 2911–2924.

Cohen, W.B., Yang, Z., Stehman, S.V., Schroeder, T.A., Bell, D.M., Masek, J.G., Huang, C.,
Meigs, G.W., 2016. Forest disturbance across the conterminous United States from
1985–2012: the emerging dominance of forest decline. For. Ecol. Manag. 360,
242–252. https://doi.org/10.1016/j.foreco.2015.10.042.

Coops, N.C., Shang, C., Wulder, M.A., White, J.C., Hermosilla, T., 2020. Change in forest
condition: characterizing non-stand replacing disturbances using time series satellite
imagery. For. Ecol. Manag. https://doi.org/10.1016/j.foreco.2020.118370.

RemoteSensingofEnvironment287(2023)11346213S. Ye et al.

Csillik, O., 2017. Fast segmentation and classification of very high resolution remote

sensing data using SLIC superpixels. Remote Sens. 9, 243.

Dale, V.H., Joyce, L.A., McNulty, S., Neilson, R.P., Ayres, M.P., Flannigan, M.D.,

Hanson, P.J., Irland, L.C., Lugo, A.E., Peterson, C.J., 2001. Climate change and forest
disturbances: climate change can affect forests by altering the frequency, intensity,
duration, and timing of fire, drought, introduced species, insect and pathogen
outbreaks, hurricanes, windstorms, ice storms, or landslides. Bioscience 51,
723–734.

Danneyrolles, V., Dupuis, S., Fortin, G., Leroyer, M., de R¨omer, A., Terrail, R.,

Vellend, M., Boucher, Y., Laflamme, J., Bergeron, Y., Arseneault, D., 2019. Stronger
influence of anthropogenic disturbance than climate change on century-scale
compositional changes in northern forests. Nat. Commun. https://doi.org/10.1038/
s41467-019-09265-z.

Djerriri, K., Safia, A., Adjoudj, R., 2020. Object-based classification of Sentinel-2 imagery
using compact texture unit descriptors through Google Earth Engine. In: 2020
Mediterr. Middle-East Geosci. Remote Sens. Symp. M2GARSS 2020 - Proc. https://
doi.org/10.1109/M2GARSS47143.2020.9105181.

Dronova, I., Gong, P., Wang, L., Zhong, L., 2015. Mapping dynamic cover types in a large
seasonally flooded wetland using extended principal component analysis and object-
based classification. Remote Sens. Environ. 158, 193–206.

Duveiller, G., Defourny, P., Descl´ee, B., Mayaux, P., 2008. Deforestation in Central

Africa: estimates at regional, national and landscape levels by advanced processing
of systematically-distributed landsat extracts. Remote Sens. Environ. https://doi.
org/10.1016/j.rse.2007.07.026.

Dwyer, J., Roy, D., Sauer, B., Jenkerson, C., Zhang, H., Lymburner, L., 2018. Analysis
ready data: enabling analysis of the landsat archive. Remote Sens. 10 https://doi.
org/10.20944/preprints201808.0029.v1.

Galbraith, S.M., Cane, J.H., Moldenke, A.R., Rivers, J.W., 2019. Salvage logging reduces
wild bee diversity, but not abundance, in severely burned mixed-conifer forest. For.
Ecol. Manag. 453, 117622.

G´omez, C., White, J.C., Wulder, M.A., 2011. Characterizing the state and processes of
change in a dynamic forest environment using hierarchical spatio-temporal
segmentation. Remote Sens. Environ. 115, 1665–1679.

Gudex-Cross, D., Pontius, J., Adams, A., 2017. Enhanced forest cover mapping using

spectral unmixing and object-based classification of multi-temporal landsat imagery.
Remote Sens. Environ. 196, 193–204.

Hamunyela, E., Verbesselt, J., Herold, M., 2016. Using spatial context to improve early
detection of deforestation from landsat time series. Remote Sens. Environ. 172,
126–138. https://doi.org/10.1016/j.rse.2015.11.006.

Healey, S.P., Cohen, W.B., Yang, Z., Kenneth Brewer, C., Brooks, E.B., Gorelick, N.,
Hernandez, A.J., Huang, C., Joseph Hughes, M., Kennedy, R.E., Loveland, T.R.,
Moisen, G.G., Schroeder, T.A., Stehman, S.V., Vogelmann, J.E., Woodcock, C.E.,
Yang, L., Zhu, Z., 2018. Mapping forest change using stacked generalization: an
ensemble approach. Remote Sens. Environ. 204, 717–728. https://doi.org/10.1016/
j.rse.2017.09.029.

Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2019. Prevalence of multiple
forest disturbances and impact on vegetation regrowth from interannual landsat
time series (1985–2015). Remote Sens. Environ. https://doi.org/10.1016/j.
rse.2019.111403.

Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., 2015. Regional
detection, characterization, and attribution of annual forest change from 1984 to
2012 using landsat-derived time-series metrics. Remote Sens. Environ. https://doi.
org/10.1016/j.rse.2015.09.004.

Lima, T.A., Beuchle, R., Langner, A., Grecchi, R.C., Griess, V.C., Achard, F., 2019.
Comparing Sentinel-2 MSI and landsat 8 OLI imagery for monitoring selective
logging in the brazilian Amazon. Remote Sens. 11, 961.

Liu, T., Yang, L., Lunga, D., 2021. Change detection using deep learning approach with

object-based image analysis. Remote Sens. Environ. 256, 112308.

Martínez-Ramos, M., Ortiz-Rodríguez, I.A., Pi˜nero, D., Dirzo, R., Sarukh´an, J., 2016.
Anthropogenic disturbances jeopardize biodiversity conservation within tropical
rainforest reserves. Proc. Natl. Acad. Sci. U. S. A. https://doi.org/10.1073/
pnas.1602893113.

Meddens, A.J.H., Hicke, J.A., 2014. Spatial and temporal patterns of Landsat-based

detection of tree mortality caused by a mountain pine beetle outbreak in Colorado,
USA. For. Ecol. Manage. 322, 78–88.

Meng, Y., Liu, X., Wang, Z., Ding, C., Zhu, L., 2021. How can spatial structural metrics
improve the accuracy of forest disturbance and recovery detection using dense
landsat time series? Ecol. Indic. 132, 108336.

Moscheni, F., Bhattacharjee, S., Kunt, M., 1998. Spatio-temporal segmentation based on

region merging. IEEE Trans. Pattern Anal. Mach. Intell. 20, 897–915.

Neubert, P., Protzel, P., 2014. Compact watershed and preemptive slic: On improving
trade-offs of superpixel segmentation algorithms. In: 2014 22nd International
Conference on Pattern Recognition. IEEE, pp. 996–1001.

Newman, E.A., 2019. Disturbance ecology in the anthropocene. Front. Ecol. Evol. 7

https://doi.org/10.3389/fevo.2019.00147.

Pasquarella, V.J., Bradley, B.A., Woodcock, C.E., 2017. Near-real-time monitoring of
insect defoliation using landsat time series. Forests 8. https://doi.org/10.3390/
f8080275.

Pengra, B.W., Stehman, S.V., Horton, J.A., Dockter, D.J., Schroeder, T.A., Yang, Z.,

Cohen, W.B., Healey, S.P., Loveland, T.R., 2020. Quality control and assessment of
interpreter consistency of annual land cover reference data in an operational
national monitoring program. Remote Sens. Environ. 238, 111261.

Qiu, S., Zhu, Z., Yang, X., 2022. Characterization of land disturbances based on Landsat

time series.

Rodman, K.C., Andrus, R.A., Veblen, T.T., Hart, S.J., 2021. Disturbance detection in

landsat time series is influenced by tree mortality agent and severity, not by prior
disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112244.

Roelfsema, C.M., Lyons, M., Kovacs, E.M., Maxwell, P., Saunders, M.I., Samper-

Villarreal, J., Phinn, S.R., 2014. Multi-temporal mapping of seagrass cover, species
and biomass: a semi-automated object based image analysis approach. Remote Sens.
Environ. 150, 172–187.

Rogan, J., Miller, J., 2006. Integrating GIS and remotely sensed data for mapping forest
disturbance and change. Underst. For. Disturb. Spat. Pattern. https://doi.org/
10.1201/9781420005189.ch6.

Schug, F., Okujeni, A., Hauer, J., Hostert, P., Nielsen, J.Ø., van der Linden, S., 2018.
Mapping patterns of urban development in Ouagadougou, Burkina Faso, using
machine learning regression modeling with bi-seasonal landsat time series. Remote
Sens. Environ. 210, 217–228.

Seddon, A.W.R., Macias-Fauria, M., Long, P.R., Benz, D., Willis, K.J., 2016. Sensitivity of

global terrestrial ecosystems to climate variability. Nature 531, 229–232.
Seidl, R., Schelhaas, M.-J., Rammer, W., Verkerk, P.J., 2014. Increasing forest

disturbances in Europe and their impact on carbon storage. Nat. Clim. Chang. 4,
806–810.

Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Nat. Clim. Chang. 7, 395–402.

Holt, A.C., Seto, E.Y.W., Rivard, T., Gong, P., 2009. Object-based detection and

Senf, C., Seidl, R., 2021. Mapping the forest disturbance regimes of Europe. Nat. Sustain.

classification of vehicles from high-resolution aerial photography. Photogramm.
Eng. Remote Sens. 75, 871–880.

Huang, C., Goward, S.N., Masek, J.G., Thomas, N., Zhu, Z., Vogelmann, J.E., 2010. An
automated approach for reconstructing recent forest disturbance history using dense
landsat time series stacks. Remote Sens. Environ. 114, 183–198.

Huete, A., 2016. Vegetation’s responses to climate variability. Nature 531, 181–182.
Im, J., Jensen, J.R., Tullis, J.A., 2008. Object-based change detection using correlation

image analysis and image segmentation. Int. J. Remote Sens. 29, 399–423.

Jobin, B., Labrecque, S., Grenier, M., Falardeau, G., 2008. Object-based classification as
an alternative approach to the traditional pixel-based classification to identify
potential habitat of the grasshopper sparrow. Environ. Manag. https://doi.org/
10.1007/s00267-007-9031-0.

Kennedy, R.E., Yang, Z., Braaten, J., Copass, C., Antonova, N., Jordan, C., Nelson, P.,

2015. Attribution of disturbance change agent from landsat time-series in support of
habitat monitoring in the Puget Sound region, USA. Remote Sens. Environ. 166,
271–285.

Kennedy, R.E., Yang, Z., Cohen, W.B., 2010. Detecting trends in forest disturbance and
recovery using yearly landsat time series: 1. LandTrendr—Temporal segmentation
algorithms. Remote Sens. Environ. 114, 2897–2910.

Kimmins, J., 2004. Forest Ecology – A Foundation for Sustainable Forest Management
and Environmental Ethics in Forestry. Prentice Hall, Up. Saddle Saddle River, New
Jersey.

Laurent, V.C.E., Verhoef, W., Damm, A., Schaepman, M.E., Clevers, J.G.P.W., 2013.
A bayesian object-based approach for estimating vegetation biophysical and
biochemical variables from APEX at-sensor radiance data. Remote Sens. Environ.
139, 6–17.

Li, T., Zhu, Z., Wang, Z., Rom´an, M.O., Kalb, V.L., Zhao, Y., 2022. Continuous monitoring
of nighttime light changes based on daily NASA’s black marble product suite.
Remote Sens. Environ. 282, 113269.

Liang, L., Chen, Y., Hawbaker, T.J., Zhu, Z., Gong, P., 2014. Mapping mountain pine

beetle mortality through growth trend analysis of time-series landsat data. Remote
Sens. https://doi.org/10.3390/rs6065696.

4, 63–70.

Senf, C., Seidl, R., Hostert, P., 2017. Remote sensing of forest insect disturbances: current

state and future directions. Int. J. Appl. Earth Obs. Geoinf. 60, 49–60.

Sol´orzano, J.V., Gao, Y., 2022. Forest disturbance detection with seasonal and trend
model components and machine learning algorithms. Remote Sens. 14, 803.

Stehman, S.V., Pengra, B.W., Horton, J.A., Wellington, D.F., 2021. Validation of the US
geological Survey’s land change monitoring, assessment and projection (LCMAP)
collection 1.0 annual land cover products 1985–2017. Remote Sens. Environ. 265,
112646.

Strahler, A.H., Woodcock, C.E., Smith, J.A., 1986. On the nature of models in remote

sensing. Remote Sens. Environ. 20 (2), 121–139.

Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
monitoring of tropical forest disturbance: new algorithms and assessment
framework. Remote Sens. Environ. 224, 202–218.

Taubenb¨ock, H., Esch, T., Felbier, A., Wiesner, M., Roth, A., Dech, S., 2012. Monitoring
urbanization in mega cities from space. Remote Sens. Environ. 117, 162–176.
Tulbure, M.G., Broich, M., Perin, V., Gaines, M., Ju, J., Stehman, S.V., Pavelsky, T.,

Masek, J.G., Yin, S., Mai, J., 2022. Can we detect more ephemeral floods with higher
density harmonized landsat sentinel 2 data compared to landsat 8 alone? ISPRS J.
Photogramm. Remote Sens. 185, 232–246.

Verbesselt, J., Hyndman, R., Newnham, G., Culvenor, D., 2010. Detecting trend and

seasonal changes in satellite image time series. Remote Sens. Environ. 114, 106–115.
https://doi.org/10.1016/j.rse.2009.08.014.

Vieira, M.A., Formaggio, A.R., Renn´o, C.D., Atzberger, C., Aguiar, D.A., Mello, M.P.,
2012. Object based image analysis and data mining applied to a remotely sensed
landsat time-series to map sugarcane over large areas. Remote Sens. Environ.
https://doi.org/10.1016/j.rse.2012.04.011.

Villarreal, M.L., Norman, L.M., Buckley, S., Wallace, C.S.A., Coe, M.A., 2016. Multi-index
time series monitoring of drought and fire effects on desert grasslands. Remote Sens.
Environ. 183, 186–197.

RemoteSensingofEnvironment287(2023)11346214S. Ye et al.

Wan, L., Xiang, Y., You, H., 2019. An object-based hierarchical compound classification
method for change detection in heterogeneous optical and SAR images. IEEE Trans.
Geosci. Remote Sens. 57, 9941–9959.

Zhang, C., Sargent, I., Pan, X., Li, H., Gardiner, A., Hare, J., Atkinson, P.M., 2018. An

object-based convolutional neural network (OCNN) for urban land use classification.
Remote Sens. Environ. 216, 57–70.

White, J.C., Hermosilla, T., Wulder, M.A., Coops, N.C., 2022. Mapping, validating, and
interpreting spatio-temporal trends in post-disturbance forest recovery. Remote
Sens. Environ. 271, 112904.

Zhang, Y., Atkinson, P.M., Ling, F., Foody, G.M., Wang, Q., Ge, Y., Li, X., Du, Y., 2021.
Object-based area-to-point regression kriging for pansharpening. IEEE Trans. Geosci.
Remote Sens. 59, 8599–8614.

White, P.S., Pickett, S.T.A., 1985. Natural disturbance and patch dynamics: an

Zhang, Y., Woodcock, C.E., Chen, S., Wang, J.A., Sulla-Menashe, D., Zuo, Z., Olofsson, P.,

introduction. Ecol. Nat. Disturb. Patch Dyn. https://doi.org/10.1016/b978-0-12-
554520-4.50006-x.

Wu, B., Yu, B., Shu, S., Wu, Q., Zhao, Y., Wu, J., 2021. A spatiotemporal structural graph

for characterizing land cover changes. Int. J. Geogr. Inf. Sci. 35, 397–425.

Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
LCMAP collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
143–162.

Yang, X., Zhu, Zhe, Qiu, S., Kroeger, K.D., Zhu, Zhiliang, Covington, S., 2022. Detection

and characterization of coastal tidal wetland change in the northeastern US using
landsat time series. Remote Sens. Environ. 276, 113047.

Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
forest disturbance using landsat time series: stochastic continuous change detection.
Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112167.

Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
dense landsat time series: case studies of mountain pine beetle and spruce beetle
disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2021.112560.

Yin, H., Brand˜ao Jr., A., Buchner, J., Helmers, D., Iuliano, B.G., Kimambo, N.E.,

Lewi´nska, K.E., Razenkova, E., Rizayeva, A., Rogova, N., 2020. Monitoring cropland
abandonment with landsat time series. Remote Sens. Environ. 246, 111873.

Yin, H., Prishchepov, A.V., Kuemmerle, T., Bleyhl, B., Buchner, J., Radeloff, V.C., 2018.
Mapping agricultural land abandonment from spatial and temporal segmentation of
landsat time series. Remote Sens. Environ. 210, 12–24.

Yuan, M., 2001. Representing complex geographic phenomena in GIS. Cartogr. Geogr.

Inf. Sci. 28, 83–96.

Wang, Y., Friedl, M.A., 2022. Mapping causal agents of disturbance in boreal and
arctic ecosystems of North America using time series of landsat data. Remote Sens.
Environ. 272, 112935.

Zheng, Z., Zhong, Y., Wang, J., Ma, A., Zhang, L., 2021. Building damage assessment for

rapid disaster response with a deep object-based semantic change detection
framework: from natural disasters to man-made disasters. Remote Sens. Environ.
265, 112636.

Zhu, Z., 2017. Change detection using landsat time series: a review of frequencies,

preprocessing, algorithms, and applications. ISPRS J. Photogramm. Remote Sens.
130, 370–384.

Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
data for operational land cover classification for the LCMAP initiative. ISPRS J.
Photogramm. Remote Sens. 122, 206–221.

Zhu, Z., Qiu, S., Ye, S., 2022. Remote sensing of land change: a multifaceted perspective.

Remote Sens. Environ. 282, 113266.

Zhu, Z., Woodcock, C.E., 2014a. Continuous change detection and classification of land

cover using all available landsat data. Remote Sens. Environ. 144, 152–171.

Zhu, Z., Woodcock, C.E., 2014b. Automated cloud, cloud shadow, and snow detection in
multitemporal landsat data: an algorithm designed specifically for monitoring land
cover change. Remote Sens. Environ. 152, 217–234.

Zhu, Z., Woodcock, C.E., 2012. Object-based cloud and cloud shadow detection in

landsat imagery. Remote Sens. Environ. 118, 83–94.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.

Continuous monitoring of land disturbance based on landsat time series. Remote
Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.

Zhang, C., Cooper, H., Selch, D., Meng, X., Qiu, F., Myint, S.W., Roberts, C., Xie, Z., 2014.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2019.

Mapping urban land cover types using object-based multiple endmember spectral
mixture analysis. Remote Sens. Lett. 5, 521–529.

Continuous monitoring of land disturbance based on landsat time series. Remote
Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.

RemoteSensingofEnvironment287(2023)11346215