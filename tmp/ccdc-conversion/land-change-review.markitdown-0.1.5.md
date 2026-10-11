Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

Review

Remote sensing of land change: A multifaceted perspective

Zhe Zhu *, Shi Qiu *, Su Ye *

Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT 06269, USA

A R T I C L E  I N F O

A B S T R A C T

Edited by Dr Marie Weiss

Keywords:
Land change
Change agent
Change metric
Change target
Land cover change
Land disturbance
Climate variability
Climate change
Succession
Time series

1. Introduction

The discipline of land change science has been evolving rapidly in the past decades. Remote sensing played a
major role in one of the essential components of land change science, which includes observation, monitoring,
and characterization of land change. In this paper, we proposed a new framework of the multifaceted view of
land change through the lens of remote sensing and recommended five facets of land change including change
location, time, target, metric, and agent. We also evaluated the impacts of spatial, spectral, temporal, angular,
and  data-integration  domains  of  the  remotely  sensed  data  on  observing,  monitoring,  and  characterization  of
different facets of land change, as well as discussed some of the current land change products. We recommend
clarifying the specific land change facet being studied in remote sensing of land change, reporting multiple or all
facets of land change in remote sensing products, shifting the focus from land cover change to specific change
metric and agent, integrating social science data and multi-sensor datasets for a deeper and fuller understanding
of land change, and recognizing limitations and weaknesses of remote sensing in land change studies.

With  the  increasing  contemporary  concerns  on  climate  change,
global  environmental  change,  and  sustainability,  land  change  science
has  emerged  as  a  unique  science  direction  for  addressing  these  chal-
lenging issues (Gutman et al., 2004; Rindfuss et al., 2004; Turner et al.,
2007). Land change science, defined as “the interdisciplinary field [that]
seeks  to  understand  the  dynamics  of  land  cover  and  land  use  as  a
coupled  human-environment  system  to  address  theory,  concepts,
models, and applications relevant to environmental and societal prob-
lems, including the intersection of the two”  (Turner et al., 2007), has
many components, in which one of the most fundamental and critical
components is the observation, monitoring, and characterization of land
change.

The  terrestrial  surface  of  the  Earth  has  been  changing  at  an  un-
precedented rate. More than half of the Earth’s ice-free land surface has
been modified by humans (Ellis et al., 2010), and almost all land sur-
faces have been influenced by climate change and various kinds of land
disturbances (Dale, 1997; Potter et al., 2003). Remote sensing, partic-
ularly satellite remote sensing, that can provide synoptic and repeated
measurements  of the global land surface at different spectral, spatial,
and temporal resolutions, is of great importance for studying global land
change (Justice et al., 1998; Roy et al., 2014; Sellers et al., 1995). In the

past decades, big advancements have been made in large-scale mapping
of land change based on remote sensing data, due to the rapidly growing
amounts of earth observation satellites (Belward and Skøien, 2015; Ustin
and Middleton, 2021), the free and open data policy (Woodcock et al.,
2008;  Wulder  et  al.,  2012;  Zhu  et  al.,  2019),  the  analysis-ready  data
format  (Dwyer  et  al.,  2018;  Frantz,  2019),  the  state-of-art  cloud
computing platform that not only provides massive parallel computing
capability  but  also  a  huge  amount  of  online  datasets  (Gorelick  et  al.,
2017), and the improved capability of new algorithms for land change
detection  (Banskota  et  al.,  2014;  Kennedy  et  al.,  2014;  Zhu,  2017).
Recently, a paradigm shift from change detection of two points in time
to monitoring and tracking change continuously in time is observed in
the remote sensing community, where the use of dense time-series ob-
servations gain more popularity with a capability of retrieving new land
change  information,  such  as  subtle  changes  in  ecosystem  health  and
condition, and long-term trend of the vegetation productivity (Wood-
cock  et  al.,  2020).  Moreover,  land  change  information  can  now  be
monitored  in  near  real-time  (Shang  et  al.,  2022;  Tang  et  al.,  2020;
Verbesselt et al., 2012; Xin et al., 2013; Ye et al., 2021a), which greatly
improves its value to resource managers and policymakers. We have also
witnessed  a  proliferation  of  land  change  characterization  algorithms
(Zhu, 2017), mostly focusing on the “from-to” information, that is, land
cover and/or land use information before and after the change (Hansen

* Corresponding authors.

E-mail addresses: zhe@uconn.edu (Z. Zhu), shi.qiu@uconn.edu (S. Qiu), su.ye@uconn.edu (S. Ye).

https://doi.org/10.1016/j.rse.2022.113266
Received 26 February 2022; Received in revised form 28 August 2022; Accepted 7 September 2022

RemoteSensingofEnvironment282(2022)113266Availableonline7October20220034-4257/©2022TheAuthors.PublishedbyElsevierInc.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).Z. Zhu et al.

and Loveland, 2012; Pricope et al., 2019). It should be noted that though
“land cover” (the physical properties at the Earth’s surface) and “land
use” (the social, economic, and cultural utility of land) are quite distinct
(Turner,  1997),  they  are  often  grouped  together  in  remote  sensing
products,  and  “land  cover”  is  usually  used  as  a  surrogate  for  under-
standing “land use”, such as including cropland and developed land in
the categories of land cover (Anderson et al., 1976). Considering remote
sensing data provide information on land cover, rather than on land use,
we will mainly focus on land cover change hereafter.

In this paper, we propose the framework of a multifaceted perspec-
tive in remote sensing of land change, in which the change in land cover
is only one of the components viewed from one of the five facets of land
change - the target of change or what is changing. Basically, if we detect
change in satellite spectral bands, we can extract the land change in-
formation  to  answer  five  different  questions,  that  are,  when  (change
time),  where  (change  location),  what  (change  target),  how  (change
metric),  and  why  (change  agent)  the  change  happened.  Each  of  the
questions  will  occupy  one  facet  of  the  change  cube  that  contains  the
spectral change information derived from remotely sensed data (Fig. 1).
The facet on the top of the change cube is left empty on purpose, as there
may be other facets of land change that are not discussed in this paper.
The  two  facets  of  “Time”  and  “Location”  provide  information  on  the
detection and monitoring of land change, and the other three facets of
“Target”,  “Metric”, and  “Agent”  are related to  the characterization of
land  change.  Indeed,  the  topic  of  land  change  has  been  extensively
reviewed in the remote sensing community, but most focused on change
detection techniques (i.e., when and where) (Coppin et al., 2004; Hus-
sain et al., 2013; Lu et al., 2004; Singh, 1989; Zhu, 2017). Only very few
reviews  mentioned  other  facets  such  as  change  target  (Hansen  and
Loveland, 2012; Warner et al., 2009; Wulder et al., 2018), change metric
(G´omez et al., 2016; Kennedy et al., 2009; Vogelmann et al., 2016), and
change agent (Kennedy et al., 2015; Sebald et al., 2021; Shimizu et al.,

2019). Pouliot and Latifovic (2016) mapped the multifaceted nature of
land change, however, it was only a case study in the Athabasca oil sands
region of Canada and has not reviewed the multifaceted land change in a
systematic way. According to our knowledge, this paper is the first work
for synopsizing the detection and characterization of land change as a
five-facet task in a systematic manner, paving the way for operational-
izing  a  holistic  examination  of  land  change  as  well  as  accomplishing
efficient communication on related concepts - rather than a synthesis of
sensor or methodological comparison which has been widely touched in
previous works.

We will first discuss all five  facets of land change as well as their
relationship through the lens of remote sensing. Next, we will discuss the
remote sensing issues in spectral, spatial, temporal, angular, and data-
integration domains in observing, monitoring, and characterization of
different  facets  of  land  change.  Finally,  we  will  discuss  some  of  the
current  land  change  products  derived  from  remote  sensing  data  and
conclude  with  a  few  recommendations.  While  most  examples  of  this
paper were illustrated using time-series datasets given by our expertise
on this topic, we do appreciate the spatial and spectral merits of other
data types (e.g., LiDAR, Hyperspectral, and Unmanned Aerial Vehicle
(UAV)), which are equally important for characterizing land change. It
has been our recognition that the integration of multiple data sources
can provide a unique opportunity for the success of monitoring multi-
faced land change (will be discussed in Section 4.5).

2. The five facets of land change

If the remote sensing system is well designed for capturing the spe-
cific land change type, it is possible to extract land change information
for  five  different  facets  based  on  the  remotely  sensed  observations
collected before, during, and/or after the land change (Fig. 2).

Fig. 1. The five facets proposed for observation, monitoring, and characterization of land change using remotely sensed data. It is worth noting that not all land
change agents will lead to a change in change target or land cover in this case, and some of the change patches displayed in the other four facets are not shown (e.g.,
stress, flooding, and agriculture activity) or only partially shown (e.g., wind, construction, and regrowth) in the facet of change target.

RemoteSensingofEnvironment282(2022)1132662Z. Zhu et al.

2.1. Where - change location

2.2. When - change time

Fig. 2. Hierarchical classification system for the five facets of land change.

topography

The first facet of land change is to answer the question of where the
change has occurred or determine the change location. Theoretically, by
differencing two georeferenced remotely sensed images collected at a
different time from the same spectral band and same location, any kind
of land surface change that occurred between the two dates would have
larger difference values than places that have not changed. By using a
simple threshold, the location of change could be identified. The land
change  detected  in  this  way  is  sometimes  called  “spectral  change”
(Brown et al., 2020; Healey et al., 2018; Xian et al., 2022), as clearly
there is a spectral value change between the two dates of the remotely
sensed images, but this does not always correspond to the changes on the
land  surface.  Other  factors,  such  as  image  registration,  atmospheric
condition,  natural  soil  wetness  fluctuation,  vegetation  phenology,
sensor-solar-geometry,  and
illumination,  may  also
contribute  to  the  spectral  change  (Kennedy  et  al.,  2014;  Zhu,  2017).
Therefore, one of the most foundational steps before the remotely sensed
images  are  used  for  detecting  land  change  is  removing  or  at  least
reducing changes in spectral values that are not caused by land surface
change.  Advanced  algorithms  have  been  developed  to  provide  more
accurate image registration results (Gao et al., 2009; Yan et al., 2016),
perform  atmospheric  correction  and  cloud/cloud  shadow  detection
(Masek  et  al.,  2006;  Qiu  et  al.,  2019b;  Zhu  and  Woodcock,  2012),
include  precipitation  information  (Tollerud  et  al.,  2020),  model  and
exclude seasonality (Verbesselt et al., 2010; Zhu et al., 2020; Zhu and
Woodcock, 2014), apply Bidirectional Reflectance Distribution Function
(BRDF) to correct sensor-solar-geometry (Roy et al., 2016; Schaaf et al.,
2002),  remove  bandpass  difference  (Claverie  et  al.,  2018;  Shang  and
Zhu, 2019), and perform topographic correction (Buchner et al., 2020;
Tan et al., 2013). It is worth noting that though these algorithms have
the potential to reduce spectral changes that are not related to changes
on land surfaces, they may also introduce artifacts, and it is not always
necessary  to  apply  all  these  algorithms  before  conducting  change
detection (Qiu et al., 2019a; Song et al., 2001).

The second facet of land change is to answer the question of when the
change occurred or determine the change time. Basically, the closer the
two  images  are  selected  for  detecting  change,  the  more  accurate  the
change time can be determined. Compared to detecting change based on
real images, there are also new change detection methods that difference
the model predicted values with actual remote sensing observations to
identify land change (Verbesselt et al., 2012; Zhu and Woodcock, 2014)
and the detected change time is determined based on how soon the new
clear  observations  are  collected  for  each  pixel  location.  These  time-
series-based  approaches  do  not  need  to  wait  for  two  clear  remote
sensing  images  and  can  provide  more  rapid  change  detection  results.
The remote sensing community has shifted from using images collected
decades apart (Homer et al., 2007; Masek et al., 2008), to annual (Huang
et al., 2010; Kennedy et al., 2010), and is currently shifting all the way to
near-real-time change detection (Shang et al., 2022; Tang et al., 2019;
Verbesselt et al., 2012; Woodcock et al., 2020; Ye et al., 2021a). This is
particularly true with the successful launch of Sentinel-2 A/B (Drusch
et  al.,  2012),  Landsat  9  (Masek  et  al.,  2020),  and  the  hundreds  of
orbiting CubeSats (Huang and Roy, 2021), that could provide subweekly
or even daily land surface observations at medium to high spatial res-
olutions (Li and Roy, 2017; Roy et al., 2021).

2.3. What - change target

The third and probably the most studied facet of land change is to
answer  the  question  of  what  is  changing  or  determining  the  change
target. The change target is sometimes defined as changes in categorical
classes such as land cover type (e.g., forest, urban, water, grass, shrub,
snow/ice, agriculture, etc.), or defined as changes in continuous variables
of  biophysical/biochemical  parameters,  such  as  Impervious  Surface
Area (ISA), land surface temperature, Leaf Area Index (LAI), vegetation
height,  biomass,  leaf  moisture  content,  leaf  chlorophyll  content,  etc.
Remotely sensed data contain rich information on the characteristics of
the  land  surface.  A  feature  space  of  more  than  a  few  dozens  to  even
hundreds of dimensions could be created from the electromagnetic ra-
diation (EMR) that is recorded at different wavelengths, the texture of

RemoteSensingofEnvironment282(2022)1132663Z. Zhu et al.

the spectral bands, and the intra-annual/inter-annual temporal trajec-
tory from the time series observations, which could be further used to
determine the land cover based on image classification (G´omez et al.,
2016;  Pouliot  and  Latifovic,  2016)  or  to  estimate  the  biophysical/
biochemical parameters based on machine learning or regression from
empirical models (Garbulsky et al., 2011; Lin et al., 2020; Verrelst et al.,
2015).  Recently,  the  deep-learning-based  approaches,  particularly
Convolutional Neural Network (CNN), have shown better performance
in  land  cover  classification  compared  to  the  traditional  machine-
learning-based methods (Kussul et al., 2017; Liu et al., 2021b; Pouliot
et al., 2021), and are capable of incorporating the spatial domain of the
remote sensing data by automatically extracting a suitable representa-
tion of the remote sensing data through a hierarchy of spatial filters at
different sizes, which avoids the feature creation and selection processes
that most traditional machine learning methods require in advance for
preparation of the classification predictors (Molinier et al., 2021).

Theoretically, if we can create land cover or biophysical/biochem-
ical parameter maps accurately at different time points, we can compare
their maps to identify changes in different land cover or a specific bio-
physical/biochemical parameter. However, as land changes are usually
very small in size (e.g., 1–5% of the land surface) (Hansen et al., 2013;
Song  et  al.,  2018),  and  all  image  classification  and  biophysical/
biochemical parameter retrieval algorithms contain errors, comparing
maps of land cover or biophysical/biochemical parameters at different
time points to detect land change may lead to compounded errors in the
final change map at a magnitude way larger than the total change area
(Olofsson et al., 2013). Therefore, land change is usually better detected
based on the magnitude of spectral change and if a spectral change is
detected, we can then estimate land cover or biophysical/biochemical
parameters before and after the spectral change (Deng and Zhu, 2020;
Jin et al., 2019; Latifovic and Pouliot, 2005; Xian et al., 2009; Zhu and
Woodcock,  2014).  It  is  worth  noting  that  even  if  there  is  a  spectral
change detected, the classified categorical land cover type may still be
the same (Hermosilla et al., 2018), as the land change that occurred on
this land cover may not be dramatic enough to change the land cover
type,  and  we  usually  call  this  land  cover  modification  or  land  cover
condition change (Comber and Wulder, 2019; Rogan et al., 2008). For
example, if forest cover is defined as trees covering >10% of the pixel
following the U.S. Forest Service definition (Riemann et al., 2010), and if
selective logging is reducing forest cover from 90% to 30%, we are very
likely to detect a spectral change, but based on the definition, the land
cover is still forest before and after the spectral change. However, if the
forest harvest is reducing forest cover from 90% to 5%, then the land
cover  will  be  likely  changed  from  forest  to  barren  or  grass,  and  we
usually call this land cover conversion, which is corresponding to more
substantial land changes that cause land cover transitions from one to
another. In the remote sensing community, huge efforts have been given
to land cover conversions (Chowdhury et al., 2021; Colditz et al., 2014;
Homer et al., 2015, 2020; Pouliot et al., 2021, Pouliot et al., 2014), but
fewer studies were targeted on the land cover modification, which often
occur at a spatial scale similar to or even larger than land cover con-
version  (Asner  et  al.,  2005;  Qin  et  al.,  2021;  Rigge  et  al.,  2019).
Detecting  land  cover  modification  is  inherently  difficult  in  remote
sensing,  as  the  subtle  spectral  change  signal  may  be  at  a  change
magnitude  similar  to  other  background  noise.  Subpixel  analyzing
methods, such as spectral mixture analysis (Asner et al., 2009), contin-
uous  fields  (Hansen  and  DeFries,  2004),  fuzzy  (or  soft)  classification
(Foody  and  Doan,  2007),  and  the  continuous  subpixel  monitoring
approach  (Deng  and  Zhu,  2020),  have  shown  their  capability  in  the
detection of land cover modification at subpixel scales.

2.4. How - change metric

The fourth facet of land change is to answer the question of how it is
changing by  a number of change metrics,  such as  change magnitude,
change  duration,  and  change  direction  (G´omez  et  al., 2016;  Kennedy

et al., 2014; Petit et al., 2001). As remotely sensed data measure land
surface reflected or emitted EMR, any state transition can be reflected as
surface  reflectance  changes  from  the  spectral  bands,  making  remote
sensing data particularly useful for tracking the change trajectories and
characterizing  the  specific  change  process  based  on  different  change
metrics  (Comber  and  Wulder,  2019;  Kennedy  et  al.,  2014).  The  most
important remote sensing observations for calculating different change
metrics are the ones that are collected during the land change events.

According to the change duration metric (how long the change event
last),  land  change  can  be  divided  into  abrupt  change  and  gradual
change. Most remote sensing change detection algorithms were devel-
oped to detect abrupt changes that occur within a short time in response
to  a  punctuated  event,  as  these  changes  can  be  detected  directly  by
comparing two remotely sensed images collected at different time points
before and after the change event (Coppin and Bauer, 1996; Woodcock
et al., 2020). On the other hand, gradual changes usually last for a much
longer time as a result of a variety of causes such as damage to vege-
tation  from  disease  and  insects,  ecological  succession,  and  climate
change (Lawrence, 2005; Vogelmann et al., 2012, 2016). There are also
remote sensing methods developed to quantify gradual changes based
on long-term time series observations (e.g., > 10 years) with the capa-
bility  of  separating  co-existing  gradual  and  abrupt  changes  (De  Jong
et al., 2012; Vogelmann et al., 2016; Zhu et al., 2016a), enabling more
accurate estimation of gradual changes.

Based on the change magnitude metric (spectral distance between
the changed and unchanged observations), land change can be divided
into  subtle  change  and  dramatic  change.  Subtle  change  modifies  the
land cover, and the impact could be either short-lived, which is some-
times called ephemeral change (e.g., gypsy moth infestation and flood-
ing), or persistent at a much longer time (e.g., > 1 year), which is also
called  gradual  change.  Dramatic  change  is  mainly  caused  by  severe
disturbance events, which may lead to land cover conversion. Dramatic
change is relatively easy to identify as large differences will be observed
in remotely sensed imagery, but subtle change detection is much more
difficult  and  requires  change  agent-  or  land  cover-specific  algorithms
with  a  careful  model  parameter  calibration  (Ye  et  al.,  2021b).  The
change  direction,  measured  by  the  angularity  of  the  spectral  change
vector, indicates the nature of the change process (Lambin and Strahler,
1994) and has the potential of providing more accurate detection of land
change when used simultaneously with change magnitude (Zhu et al.,
2020). It is worth noting that other change metrics could also provide
valuable information for characterizing how the land surface is chang-
ing,  such  as  time  since  last  change,  spectral  stability  period,  and
occurrence change intensity (Brown et al., 2020; Pekel et al., 2016).

2.5. Why - change agent

The fifth facet of land change is to answer the question of why it is
changing or determine the change agent. Climate, land disturbance, and
succession  are  the  three  major  change  agents  that  occur  at  quite
different timescales (Fig. 3). Though the three change agents are quite
different conceptually, they interplay with various kinds of positive and
negative  feedbacks  (Dale  et  al.,  2001;  Guo  et  al.,  2018;  Johnson  and
Miyanishi, 2021; Laflower et al., 2016; Seidl et al., 2017).

Land disturbance has been defined in various ways (Clements, 1916;
Grime, 1977; Sousa, 1984; Turner, 2010; White and Pickett, 1985), and
one of the most commonly used definitions by ecologists is “any rela-
tively  discrete  event  in  time  that  disrupts  ecosystems,  community  or
population  structure  and  changes  resources,  substrate  availability,  or
the physical environment” (White and Pickett, 1985). Most of the time,
land disturbance occurs in a very short time ranging from hours to years
and  can  be  anthropogenic  or  natural.  Anthropogenic  disturbance,
sometimes  called  mechanical  change  or  land  use  change,  refers  to
human activity-related land change, such as forest management, agricul-
ture activity, construction, and prescribed fire. Natural disturbance can be
further  divided  into  abiotic  disturbance,  such  as  wildfire,  flooding,

RemoteSensingofEnvironment282(2022)1132664Z. Zhu et al.

Fig. 3. Timescales applicable to weather, climate variability, climate change, land disturbance, and succession.

tornado,  hurricane,  drought,  geological  hazard,  and  biotic  disturbance,
such as insect infestation, pathogens, and invasive species. It is worth noting
that there is a long debate on whether drought should be included as one
type of land disturbance, and it has only started to be considered as a
disturbance type over the past decade (Peters et al., 2011). Fire can be
both  natural  (wildfire)  and  anthropogenic  (prescribed  fire)  (Bowman
et al., 2011), and remote sensing can detect both burning fires and fire
burned  areas  (Justice  et  al.,  2002;  Lentile  et  al.,  2006).  Most  remote
sensing algorithms developed for detecting disturbance are only limited
to a single change target, such as forest disturbance (Healey et al., 2018;
Huang et al., 2010; Jin and Sader, 2005; Kennedy et al., 2007; Zhu et al.,
2012a), and only a few algorithms can provide more general disturbance
results, such as the MODIS Global Disturbance Index (MGDI) algorithm
(Mildrexler  et  al.,  2009),  the  Landsat-based  detection  of  Trends  in
Disturbance  and  Recovery  (LandTrendr)  algorithm  (Kennedy  et  al.,
2015),  and  the  COntinuous  monitoring  of  Land  Disturbance  (COLD)
algorithm (Zhu et al., 2020). As disturbance will create a spectral change
signal that deviates from the normal data fluctuation, it can be better
captured after the normal data fluctuation is well defined and modeled.
However, for certain disturbance types, such as selective logging and in-
sect  infestation,  they may  only  change  a  small  fraction  of  the  pixel  or
slightly  change  the  health  condition  of  the  ecosystem,  which  makes
these  kinds  of  disturbance  agents  extremely  difficult  to  detect  and
distinguish in remote sensing data (Asner et al., 2005; Senf et al., 2017;
Ye et al., 2021b).

Unlike weather that describes “snapshot-like” atmospheric condition
(e.g., rainstorms and tropical cyclones) that changes every hour, day,
and maybe months, the term “climate” depicts the mean and variability
of temperature, precipitation, or wind for a much longer time, ranging
from months to centuries. Climate variability refers to the short-term (e.
g., months, seasons, or years) variation in climate patterns such as El-
Ni˜no Southern Oscillation, and climate change refers to the long-term
changes  (e.g., decades  or centuries)  in climates  such as global  warm-
ing and sea-level rise. Climate variability can be detected using remotely
sensed vegetation indices by comparing a certain year with a baseline
computed  from  a  longer  satellite  time  series  (Saleska  et  al.,  2007;
Samanta et al., 2010), and climate change can be also evaluated based
on the long-term trend of remotely sensed vegetation indices (Myneni
et al., 1997; Zhu et al., 2016b). As both climate variability and distur-
bance will cause remote sensing observations to deviate abruptly from
their past trajectories with a change magnitude larger than a pre-defined
threshold,  climate  variability  is  sometimes  identified  as  one  kind  of
disturbance type in remote sensing (Huete, 2016), and will be particu-
larly noticeable in semiarid areas where the amount of precipitation will
have a large impact on the local ecosystems.

Climate  change  and  land  disturbance  initiate  succession  (e.g.,  pri-
mary  succession  and  secondary  succession),  which  is  defined  as  the
process that the structure of a biological community changes over time
(Huston  and  Smith,  1987).  The  process  of  succession  is  often  accom-
panied with a sequence of biotic community replacement, such as the

well-known  four-stage  Oliver  and  Larson  Model  (Oliver  and  Larson,
1996). Primary succession is the process that plants and animals colo-
nize a barren habitat for the first time, which could take hundreds of
years, while secondary succession begins after a major disturbance that
transformed the original landscape. As remote sensing has a relatively
short history, and the longest earth observation satellite, such as Land-
sat, only has a half-century record (Wulder et al., 2022), it is not ideal to
quantify primary succession, and there are only limited studies on this
topic  (e.g.,  Knoflach  et  al.,  2021;  Lawrence,  2005).  However,  remote
sensing data have been frequently used for quantifying secondary suc-
cession after disturbance with regards to its recovery rate or succession
stages.  The  post-disturbance  recovery  rate  was  often  estimated  via
spectral recovery rate as the proxy from the temporal trend analysis of
satellite time series (Bartels et al., 2016; Kennedy et al., 2010; P´erez-
Cabello et al., 2021; Senf et al., 2015; White et al., 2022; Zhao et al.,
2018). Combined with ground measurements (Huang et al., 2019; White
et al., 2019) and laser scanning data (Chirici et al., 2020; White et al.,
2018), the use of dense satellite time series has enabled a better evalu-
ation for re-establishment of forests over large areas (Chu et al., 2016;
White et al., 2017), offering new insights on forests resilience (Forzieri
et al., 2022; Senf and Seidl, 2022), recovery characterization (Bartels
et  al., 2016), and climate  effects  (Sulla-Menashe et  al., 2018). Differ-
ently, the succession stages were often characterized through a single-
date  species  mapping  based  on  optical  or  LiDAR  datasets  (Osi´nska-
Skotak et al., 2019; Raitsos et al., 2013; Rittenhouse et al., 2022), and
sometimes required to be linked to field observations (e.g., Hall et al.,
1991).

Observing  and  monitoring  places  where  disturbance,  climate,  and
succession occurred is important, but what is more critical is to identify
the  specific  change  agent,  and  this  effort  is  sometimes  called  change
agent  characterization  (or  attribution)  in  remote  sensing.  Among  the
variety of possible land change agents, we can divide them into direct or
proximate  causes  (e.g.,  agriculture  activity,  construction,  fire,  forest
management, etc.) and distal or underlying driving forces (e.g., human
population  dynamics, human  attitudes  and behavior,  economic  trans-
formation, climate change, etc.) (Geist and Lambin, 2002; Lambin et al.,
2001). A majority  of  the  remote  sensing  studies  are only  focusing on
creating change agent maps of the proximate causes, in which some of
them are more focused on anthropogenic agents (Kennedy et al., 2015;
Shimizu et al., 2019) and others are more of a natural agent focus (Oeser
et al., 2017; Schroeder et al., 2017). Most of the remotely sensed change
agent types are quite broad, and some of the typical categories include
agriculture activity, forest management, construction, insect, windstorm, fire,
flooding, and vegetation stress. Satellite time series observation collected
before, during, and/or after the disturbance events and supervised ma-
chine  learning  classifiers  are  usually  used  together  for  change  agent
classification (Shimizu et al., 2019), and the inclusion of spatial domain
of remote sensing data is frequently found helpful in improving sepa-
ration of different change agents (Kennedy et al., 2015; Sebald et al.,
2021; Shimizu et al., 2019). It should be noted that remote sensing of

RemoteSensingofEnvironment282(2022)1132665Z. Zhu et al.

change  agent  is  never  an  easy  task.  Changes  of  different  agents  can
happen simultaneously or in close proximity to each other, which makes
untangling  these  agents  extremely  hard  sometimes  (e.g.,  harvest
following  by  a  pest  infestation  in  forests).  Moreover,  different  distur-
bance agents may result in the same or similar change consequences (for
example, windstorms, wildfire, insect infestation, and drought will all
lead  to  defoliation),  which  makes  the  spectral  change  signature  very
similar among the different agents. Additionally, it is extremely chal-
lenging to collect high-quality change agent training data consistently
across a large geographic region at a national or global scale. Synthe-
sizing  all  the  land  change  agent  related  open  data,  such  as  the  Land
Change  Monitoring,  Assessment,  and  Projection  (LCMAP)  reference
sample (Pengra et al., 2020), LANDFIRE reference data (Rollins, 2009),
USGS Land Cover Trends data (Loveland et al., 2002), USFA National
Insect and Disease Survey database (Johnson and Wittwer, 2008), NASA
Cooperative Open Online Landslide Repository (COOLR) Landslide data
(Kirschbaum  et  al.,  2010),  NOAA  Severe  Weather  Data  Inventory
(SWDI) (NOAA, 2022), and Monitoring Trends in Burn Severity (MTBS)
data (Eidenshink et al., 2007), and refining training data based on prior
knowledge of change agent characteristics could be a potential solution.
Remote sensing can also help better understand the underlying driving
forces behind global land change based on qualifying and quantifying
human-environment interaction at a multitude of spatial and temporal
scales (Pricope et al., 2019). By integrating social science data and sta-
tistical methods such as fixed-effects models (Firebaugh et al., 2013), it
is possible to provide deeper understanding of the complex land change
transitions and teleconnection/telecoupling (Friis et al., 2016; Lambin
et al., 2001; NRC, 1998, 1999; Pricope et al., 2019; Seto et al., 2012).

3. Relationship of various kinds of change terminologies

A variety of change terminologies have been introduced and used for
remote  sensing  of  land  change.  Though  they  are  all  related  to  land
change,  their relationship  is  rather complicated  and  confusing. Fig. 4
illustrates the relationship of some widely used land change terminol-
ogies,  including  spectral  change,  land  surface  change,  land  cover
change,  land  cover  modification,  land  cover  conversion,  land  distur-
bance, climate variability, climate change, succession, and biophysical/
biochemical parameter change. Spectral change (the grey rectangle in
Fig. 4), defined as the temporal change in remote sensing spectral value,
has been widely used in many remote sensing change detection studies
(Cohen  and  Goward,  2004;  Coppin  and  Bauer,  1996;  Verstraete  and
Pinty, 1996). Spectral change is the broadest of all land change termi-
nologies  that  could  include  all  kinds  of  land  changes  (e.g.,  changes

Fig. 4. Relationship of some widely used land change terminologies, including
spectral change, land surface change, land cover change, land cover conversion,
land cover modification, land disturbance, climate variability, climate change,
succession, and biophysical/biochemical parameter change.

caused  by  vegetation  phenology  and  abrupt/gradual  land  surface
changes), as well as the spectral changes that have nothing to do with
land  change  on  the  ground,  such  as  atmospheric  influences  and  data
noise. On the other hand, land surface change (the region within red
dashed line in Fig. 4), which shared the same area as land cover change,
has also gained a lot of visibility in remote sensing studies of land change
(Brown et al., 2020; de Beurs et al., 2015; Sohl et al., 2004; Woodcock
et  al., 2020; Zhu  and Woodcock, 2014). Land  surface change  or land
cover  change  includes  all  land  change  (e.g.,  all  kinds  of  land  cover
conversions  and  modifications)  that  occurs  on  the  Earth’s  surface,
except for cyclic changes that are often caused by vegetation phenology
and  snow/ice  seasonality.  Biophysical/biochemical  parameter  change
(the purple rectangle in Fig. 4) includes land surface change (or land
cover change), that will inevitably lead to changes in certain biophysi-
cal/biochemical  parameters,  as  well  as  cyclic  changes  that  cause
changes  in  LAI  and  leaf  chlorophyll  contents.  Land  disturbances  (the
light red rectangle in Fig. 4) are discrete events that disrupts ecosystems,
and if they are severe enough, they can lead to land cover conversion,
and are sometimes overlapped with climate variability (e.g., drought).
Climate  variability  (the  light  yellow  rectangle  in  Fig.  4)  and  climate
change (the dark yellow rectangle in Fig. 4) are driven by the mean and
variability  of  temperature,  precipitation,  or  wind,  and  climate  vari-
ability  refers  to  the  short-term  variations  in  climate  patterns  (e.g.,
months, seasons, or years) while climate change refers to the long-term
changes (e.g., decades or centuries). Both can lead to land cover con-
version when it is persistent or have a significant impact on the land
surface. Succession (the green rectangle in Fig. 4), defined as the process
of the structure of a biological community changing over time can also
change the land cover categories (e.g., transitioned from grass to shrub,
and all the way to forest) with enough time and adequate recovery speed
(Brown  et  al.,  2020).  Note  that  land  disturbance,  climate  variability,
climate change, and succession may all lead to categorical land cover
change  -  land  cover  conversion  (the  rectangles  filled  with  stripes  in
Fig. 4), but most of the time they will only lead to within-state modifi-
cations or condition change - land cover modifications (the rectangles
filled  with  dots  in  Fig.  4),  such  as  changes  in  the  value  of  a  certain
biophysical/biochemical parameter.

4. The current issues for monitoring multifaceted land change

It would be ideal that the remote sensor was designed to detect all
land changes with the right spectral, spatial, temporal resolutions, and
viewing  angles.  However,  the  practical  issues  from  spectral,  spatial,
temporal,  angular,  and  data-integration  domains  have  hindered  the
remote  sensing  platform’s  capability  of  detecting  and  characterizing
land change.

4.1. The spectral issues

Visible,  Near  Infrared  (NIR),  Shortwave  Infrared  (SWIR),  thermal,
and  microwave  electromagnetic  radiation  is  absorbed,  reflected,  and
transmitted in different ways by terrestrial materials. Land changes, in
essence, are partial or complete changes of the terrestrial materials, and
hence  a  certain  type  of  land  changes  can  manifest  distinct  detection
performance at different wavelengths. In practice, if the spectral ranges
capable of separating the two different types of land surfaces  are not
included in the remote sensing bands, it is almost impossible to detect
change  location  and  time,  not  to  mention  accurate  identification  of
change target, metric, and agent. For example, when forests are burned,
the land-change signals are barely discernable from the visible Landsat
bands, such as blue, green, and red, and certain microwave bands (e.g.,
C-Band). In contrast, much larger spectral differences could be observed
between  before-  and  after-change  images  as  decreasing  NIR  and
increasing SWIR1, SWIR2, and thermal bands (Fig. 5) due to post-fire
char, reduced vegetation and water content, so these bands are critical
to  fire  damage  assessment.  Some  studies  also  reported  that  narrow

RemoteSensingofEnvironment282(2022)1132666Z. Zhu et al.

Fig. 5. Spectral change at different band wavelengths induced by a fire disturbance. The spectral differences are subtle in visible bands and the microwave band but
are substantial in NIR, SWIR, and thermal bands. Blue, green, red, NIR, SWIR1, SWIR2, and thermal bands were derived from Landsat 8 surface reflectance and
brightness temperature data, and microwave C-Band was selected from Sentinel-1C-Band synthetic aperture radar data with dual-band cross-polarization (Vertical
transmit/Horizontal receive) at descending orbit. All the remotely sensed images were acquired at central latitude/longitude (40.100 /(cid:0) 120.607) in June 2019 and
2020 and clipped to the same geographic extent (1001 pixels by 401 pixels) at 30 m spatial resolution. (For interpretation of the references to color in this figure
legend, the reader is referred to the web version of this article.)

spectral bands, such as red edge bands (680–730 nm), are particularly
useful for discriminating subtle/gradual vegetation changes which are
often unrecognizable from broadband remote sensing (Ortiz et al., 2013;
Xie et al., 2018). Generally, the selection of involved bands/indices is of
enormous  importance  to  the  effectiveness  of  such  change  detection
tasks, which necessitates more studies on target-based approaches for
determining optimal spectral inputs (Yang et al., 2022; Ye et al., 2021b).
Besides  change  detection,  the  spectral  selection  is  also  critical  to
characterizing change target, agent, and metric. The band selection is
known as the prerequisite for the success of a cover classification task to
identify  change  targets  such  as  before-change  and  after-change  cover
types (Guo et al., 2006). While given cover types may have similar and
indistinguishable spectral responses at specific points in time, in most
cases, the spectral behavior of different cover types varies over time, and
the combined ability to look both multi-spectrally and multi-temporally
may  provide new  insights for discriminating cover types (Fang et al.,
2020; Key et al., 2001; Pasquarella et al., 2018; Zhu et al., 2012b). The
multispectral change, also known as spectral change vector, often pre-
sents  diagnostic  attributes  such  as  change  direction  (Lambin  and
Strahler, 1994) and has been employed as the key variable for catego-
rizing change agents (Zhang et al., 2022). The change metrics, such as
“subtle  vs  dramatic”  in  the  change  magnitude,  are  also  spectrum
dependent. Furthermore, change magnitudes based on different remote

sensing  bands/indices  can  help  identify  biological  change  phases:  for
example, Red-Green Index (RGI) was often used to indicate the red stage
(i.e., the needles turn red) for a beetle-infestation process (Coops et al.,
2006),  while  a  substantial  drop  of  Normalized  Difference  Vegetation
Index (NDVI) could be treated as a sign of the grey stage (i.e., all foliage
drop)  (Hart  and  Veblen,  2015).  A  successful  change  characterization
requires careful investigation of the most relevant spectral inputs; more
important  might  be  recognizing  change  characterization  as  a  multi-
spectral problem for a thorough examination of a change process.

4.2. The spatial issues

The  spatial  resolution,  defined  as  the  dimension  in  meters  of  the
ground-projected  Instantaneous-Field-of-View  (IFOV),  determines  the
minimum mapping unit on the ground (e.g., a Landsat 8 pixel covers a
30 m × 30 m land area). Remotely sensed images from various kinds of
platforms  can  provide  a  wide  range  of  spatial  resolutions  from  sub-
meters  to  tens  of  kilometers  (Belward  and  Skøien,  2015).  The  choice
of spatial resolution also has important implications for the downstream
satellite-based  product  (Mascorro  et  al.,  2015).  Remote  sensing  data
with a higher spatial resolution are generally preferred as the input for
change  detection,  as  the  higher  the  spatial  resolution,  the  better  the
capability  in  detecting  small-scale  land  changes.  However,  when  the

RemoteSensingofEnvironment282(2022)1132667Z. Zhu et al.

spatial resolution is too high (e.g., < 1 m), the image quality may be
severely impacted by the shadow of land surface features (Bruzzone and
Bovolo, 2012). On the other hand, if the spatial resolution is too coarse,
small-sized land surface changes may not exhibit obvious spectral sig-
nals  (see  the  MODIS  images  in  Fig.  6),  and  the  large  difference  in
point-spread-function and BRDF impacts will lead to new data noise and
make  change  signals  even more diluted  (Xin et  al., 2013).  Therefore,
medium  resolution  satellites  with  resolution  between  10  and  100  m,
such as SPOT, Sentinel-2, and Landsat, are often more preferable than
the coarse resolution sensors for mapping cover type change (Martin and
Howarth, 1989; Szostak et al., 2018; Zhu, 2017), and the coarse reso-
lution  data,  such  as  MODIS  and  AVHRR,  are  mostly  used  to  extract
gradual  change  based  on  long  time  series  data  (Myneni  et  al.,  1997;
Pouliot et al., 2009; Zhu et al., 2016b). It is worth noting that the im-
pacts  of  spatial  resolution  of  the  remotely  sensed  imagery  may  differ
based on the specific image analyzing unit, such as pixel-based versus
object-based approaches (Baker et al., 2013).

When change units of interest are smaller than the resolution cells,
land change may only occur on a small fraction of a pixel (the fraction is
a continuous variable), which is also known as the L-resolution situation
(Strahler et al., 1986). To facilitate response design for reference sample
pixels, a thresholding strategy is often needed to determine whether a
pixel is considered as a “change pixel” from a ground view. For example,
in Hansen et al. (2013), forest change is defined as a pixel with >50%
change in forest cover within a pixel. On the other hand, the definition of

land cover also directly determines the scope of the change (mainly land
cover conversion) under investigation. For example, if a forest class is
defined as >10% of tree cover, and grassland is defined as a >10% of
grass cover, the pixel will be considered to have undergone land cover
conversion from the forest class to grass class only if >90% of the trees
are  removed  from  a  fully  forested  pixel  and  replaced  by  grassland
(Fig. 6). This is because the land cover definition is usually resource-
driven,  and  when  classes  meet  the  definition  of  more  than  one  cate-
gory,  classes  with  a  higher  priority  are  given  preference  in  assigning
labels  (e.g.,  urban  > forest  > grass).  Similarly,  if  some  proportion  of
forest is converted to built-up lands, it will be labeled as urban even if
the urban proportion of the pixel is small (but at least >10%) (Pengra
et al., 2020). For example, if >10% of trees were removed from a forest
pixel, and replaced by a new house, the pixel would still be considered to
have  undergone  land  cover  conversion  (from  forest  to  urban),  even
though the remaining forest cover is just slightly <90% (Fig. 6).

4.3. The temporal issues

The  temporal  resolution  of  a  remote  sensing  system  refers  to  the
revisiting period of a satellite sensor (e.g., Landsat 8 revisits the same
location  every  16  days).  A  variety  of  remote  sensing  systems  collect
observations every minute, hour, daily, weekly, monthly, or for a few
years  (Jensen,  2009).  Essentially,  more  accurate  detection  of  change
time  could  be  achieved  based  on  observations  of  higher  temporal

Fig. 6. The impacts of spatial resolution on mapping change location and change target between 2014 and 2018. All the remotely sensed images were acquired at
central latitude/longitude (41.781/(cid:0) 72.234) in the summer of 2014 and 2018 and reprojected into the WGS84 UTM Zone 19 N. The MODIS, Landsat, and Plan-
etScope images were collected at a coarse resolution (500 m), medium resolution (30 m), and high resolution (5 m), respectively. Two National Agriculture Imagery
Program (NAIP) aerial images (0.6 m) were classified into forest, urban, and grass which were used as the reference maps. To generate change location and change
target maps for each image type, we aggregated the reference maps at each resolution and labeled cover types and change pixels by investigating sub-pixel fraction:
forest is defined as pixels with >10% coverage of trees, and urban is defined as pixels with >10% coverage of built areas; changes were labeled when cover types for
>10% of the pixel changed. No change signals were present from MODIS images (500 m) under the definition but became detectable in the other remote sensing
images at 0.6–30 m spatial resolutions.

RemoteSensingofEnvironment282(2022)1132668Z. Zhu et al.

resolutions,  as  change  time  can  be  contained  within  a  narrower  time
interval, and this has been echoed by the fact that remote sensing change
detection  algorithms  are  using  denser  time  series  (Zhu,  2017).  The
choice of temporal resolution is particularly important when the short-
lived  phenomena  need  to  be  monitored  or  persistent  clouds  limit  a
clear view. For example, with two sensors working simultaneously, the
Landsat  time series can provide 8 days of revisit observations for the
same location if we do not consider observations contaminated by cloud,
cloud shadow, and snow/ice. For ephemeral change such as floods that
only last a few days, it is less likely to be observed based on Landsat time
series alone (Fig. 7a). In Fig. 7a, we serendipitously collected one clear
Landsat  image  located  during  the  flooding,  but  if  it  was  blocked  by
clouds,  it  would  be  impossible  for  detecting  this  kind  of  ephemeral
change  as  the  system  had  recovered  to  the  pre-change  state  before
acquisition of the next available observation unless other active sensors
such as radar were used. For grassland change (i.e., abrupt greenness
change)  caused  by  climatic  variability  and  forest  change  caused  by
beetle infestation, they can last for a year or multiple years, respectively,

and  are  usually  detectable  if  annual  Landsat  observations  are  used
(Fig.  7b-c).  Another  extreme  is  that  land  changes  relating  to  urban
expansion (Fig. 7d) that is often non-reversible and could be successfully
captured even by two Landsat images collected at an interval of 5 to 10
years.  Therefore,  the  minimum  temporal  resolution  required  for
different land change applications is usually quite different. Generally,
the  denser  the  time  series  observations  used,  the  more  accurate  the
detection of the time and location of change.

Even if all clear observations have remained for analysis, the time
series may have different temporal resolutions at different places and at
different times due to the overlap of adjacent swaths, the presence of
cloud  or  snow/ice,  and  the  data  acquisition  strategies  (Brown  et  al.,
2020; Zhu et al., 2018). For example, Gypsy Moth infestation usually
only lasts for one or two months, and if all available Landsat data are
used,  we can  have  around four  clear  observations  (without  using  ob-
servations from the neighboring path) in two months for most places
(assume cloud cover is 50%). In certain places where two Landsat paths
overlap with each other (the overlap areas), we could have around eight

Fig. 7. The impact of temporal resolution on land change detection. (a) A flood event that lasted for a few days at central latitude/longitude (41.103/(cid:0) 95.906). Of
all the available Landsat observations, only a single observation was observed during this ephemeral event. (b) Climatic variability over grassland that lasted almost a
year at central latitude/longitude (34.838/(cid:0) 117.460). (c) Beetle infestation related land change that lasted for several years at central latitude/longitude (40.226/
(cid:0) 106.064). (d) Urbanization over forested areas located at latitude/longitude (41.70/(cid:0) 71.57). In each figure, the time series plot in the upper panel was derived
from  all  available  Landsat  observations  at  the  center  of  the  smaller  red  square  of  the  false  color  composite  images  at  the  lower  panel.  The  change  period  was
highlighted by the red rectangles in the upper panel and the larger red rectangle surrounding the false color composite images in the lower panel. The false color
composite images were shown in Landsat SWIR1, NIR, and red bands at the same color stretch setting. Some of the images have black stripes due to the Landsat 7
Scan Line Corrector-off issue. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

RemoteSensingofEnvironment282(2022)1132669Z. Zhu et al.

Fig. 7. (continued).

clear  observations  which  increased  the  likelihood  of  detecting  these
short-lived changes if a fixed number of consecutive observations is used
to analyze change anomaly (Fig. 8). The use of overlap-path observa-
tions brings new science capability for Landsat data, but also result in
inconsistency to the final land change maps (between the overlap and
non-overlap  areas).  This  is  particularly  problematic  for  large-scale
remote  sensing  change  products,  as  large  differences  in  land  change
patterns will show up both spatially and temporally. Methods that select
data from the same path or adjust the number of observations to confirm
change based on data density could be possible solutions to alleviate this
issue, but it is at the sacrifice of losing the temporal density for certain
places, which may lead to omission errors (Fig. 8).

Temporal resolution is of critical relevance to detecting day-sensitive
changes such as vegetation phenology. The coarse resolution data, such
as MODIS and VIIRS, are capable of providing daily repeated observa-
tions  and  has  been  widely  used  for  land  surface  phenology  products
(Ganguly et al., 2010; Zhang et al., 2018, 2020). Practically, owing to
cloud  and  snow/ice  contamination,  multi-day  compositing  was  often
employed to produce clear observations at a temporal resolution lower
than  the  daily  frequency.  A  longer  compositing  interval  will  reduce
computational and data storage demand and also ensure the observation
inputs are of sufficient quality to be useful for model fitting, yet its low
temporal  resolution  comes  at  the  cost  of  hampering  accuracies  for
characterizing phenometrics. Fig. 9 depicts an example of phenological
transition date detection from daily (only clear observations remained),

eight-day, and 32-day MODIS-based (500 m) composite time series on a
cropland pixel (Indiana, USA). The daily and the eight-day composite
time  series  have  similar  predictions  on  green-up  and  dormancy  dates
(the  difference  ≤ 2  days),  while  a  significant  discrepancy  for  the
dormancy  date  (12  days  later  than  that  of  the  daily  time  series)  was
observed on the 32-day composite time series. This can be explained by
that lower data density often results in a poorer model fit, especially for
the  phenological  window  where  spectral  reflectance  often  changes
rapidly. A wide body of the literature supports that a moderately high
temporal resolution (three- to 16-day interval) is often necessitated to
accurately inform phenological dates (Cui et al., 2020; Henson et  al.,
2018; Zhang et al., 2009).

Additionally, the use of dense time series can create new information
or more accurate change detection/characterization that the traditional
two-date image difference method cannot provide. For example, we can
get to know how the change is occurring based on the change magni-
tude, the change direction, and the duration of the change. The infor-
mation embedded in the time series data provides important spectral-
temporal information about the pixel and we can extract this informa-
tion  based  on  estimated  time  series  model  coefficients  and  statistical
metrics to provide a more accurate classification of the change target
(Zhu, 2017). These derived spectral-temporal metrics could even revo-
lutionize the current land cover classification system and bring in new
land cover categories that are continuous in time and embedded with
changing conditions, such as greening urban, young forest, mature forest,

RemoteSensingofEnvironment282(2022)11326610Z. Zhu et al.

Fig. 8. A comparison of change detection results caused by Gypsy Moth damage using two Landsat paths (or swaths) data and a single path data. (a) Landsat NIR
surface reflectance observations at the center of the red square of the false color composite images on the right (c) at central latitude/longitude (41.996/(cid:0) 71.669).
The blue dots are from Landsat path #12 and the green dots are from path #13. The red line is the estimated time series model, and the red circle is the land surface
change captured by the COLD algorithm with six consecutive observations to confirm a change (Zhu et al., 2020). (b) A land disturbance map was created based on
the COLD algorithm using Landsat observations from two paths and a single path (#12). The darker the color, the more recent the land disturbance was detected. (c)
The false color composite Landsat images from path #12 (in blue outlines) and path #13 (in green outlines) were shown in SWIR1, NIR, and red bands, and they are
directly comparable because of the same stretch display. This figure demonstrated that for places with two Landsat path coverage, Gypsy Moth damage is possible to
detect by the COLD algorithm, but not possible for places with only a single Landsat path coverage. COLD: COntinuous monitoring of Land Disturbance.

and declining forest (Zhu and Woodcock, 2014). Finally, the time series
before, during, and after land change all contain rich spectral-temporal
information on the change agent and could be used as major inputs for
change agent classification.

In  addition  to  the  repeat  frequency,  the  time  of  day  the  remote
sensing  observations  are  collected  is  also  helpful  for  better  under-
standing different facets of land change. For example, most of the time
series we discussed are remotely sensed data collected during the day-
time (e.g., around 10 am), which relies on the reflected electromagnetic
radiation from the sun. There is also another type of satellite dataset for
imaging land surface at nighttime, which provide versatile data sources
for studying human activities, as most of the nighttime lights are arti-
ficial lights (Levin et al., 2020; Li et al., 2017; Zhao et al., 2019). Time-
series  nighttime  light  data  have  been  widely  used  to  monitor
anthropogenic-related land change and usually at a large scale. How-
ever, as there are also other sources of light at night, such as moonlight,
aurora, and lighting, the use of dense time series of nighttime light data
is still very rare (Wang et al., 2021), and the densest time series data ever
used is still the average monthly or yearly nighttime light observations
(Elvidge et al., 2021; Levin, 2017). Recently, NASA has created a Black
Marble  product  that  has  corrected  most  of  these  nonhuman-activity-
related  light  sources  and  has  provided  the  potential  of  using  daily
nighttime  light  observations  for  land  change  studies  (Rom´an  et  al.,
2018).

4.4. The angular issues

The  energy  acquired  by  the  remote  sensing  systems  contains  very
specific  angular  characteristics,  which  is  a  function  of  illumination
source (e.g., Sun for a passive system or the sensor itself for active sys-
tems) angles and the sensor viewing angles, known as the Bidirectional
Reflectance Distribution Function (BRDF) (Schaaf et al., 2002). This bi-
directional  nature  of  remote  sensing  systems  will  cause  inconsistency
among the radiance by the same sensor, as well as impact current surface
reflectance retrieval models, thereby limiting our capability for detect-
ing real change signals (Xin et al., 2013). Even for some of the sensors
that only collect near nadir observations, such as Landsat, the changes in
the  solar  angles  and  view  zenith  angles  (mostly  for  observations
collected in overlap swaths) will still cause large reflectance differences
(Qiu et al., 2019a; Zhang et al., 2018), and potentially lead to omission
or commission errors in change detection (Fig. 10a). Fortunately, with
enough remote sensing observations collected at the different view and
solar angles within a short time, this BRDF function can be modeled, and
local-noon nadir observation can be estimated for some coarse resolu-
tion satellites, such as MODIS and VIIRS (Liu et al., 2017; Schaaf et al.,
2002), and these BRDF parameters can help reduce BRDF effect in me-
dium  resolution  satellites,  such  as  Landsat  and  Sentinel-2  (Claverie
et al., 2018; Roy et al., 2016). Other solutions such as selecting obser-
vations within the same swath and creating time series models that es-
timate  the  solar  angle  difference  along  with  vegetation  phenology

RemoteSensingofEnvironment282(2022)11326611Z. Zhu et al.

Fig. 9. Cropland-based phenometrics predicted by different temporal resolutions at latitude/longitude (40.681/(cid:0) 86.912). The daily MODIS Enhanced Vegetation
Index (EVI) were generated from Nadir BRDF-Adjusted Reflectance (NBAR) daily dataset (MCD43A4) at 500-m resolution. The composite time series was further
produced using the maximum index. The phenological curve was modeled using Beck’s double logistic regression (Beck et al., 2006), and green-up and dormancy
dates were determined by using the rate of change in curvature (Zhang et al., 2003). The dormancy date for the 32-day composite time series (in the bold text) was
unrealistically 12 days later than the other two due to its poor model fit brought by inadequate observations. (For interpretation of the references to color in this
figure legend, the reader is referred to the web version of this article.)

Fig. 10. The impact of BRDF on land change detection. (a) Change detection using all observations collected in overlap paths. The BRDF effect, dominated by the
different sensor view angles from two adjacent paths, results in an omission error. (b) Change detection using all observations in a single path with minimum view
zenith angle. The land change can be successfully detected when the BRDF effect is reduced in time series observations collected from a single swath. (c) Landsat
Path/Row tiles. The blue and green polygons indicate Landsat paths #41 and #42, respectively. The center of the red square indicates the location of the time series
plots (a) and (b) at latitude/longitude (38.737/(cid:0) 117.880). This change detection example was generated from all available Landsat time series and a time-series-
based change detection method called COLD (Zhu et al., 2020). COLD: COntinuous monitoring of Land Disturbance. (For interpretation of the references to color in
this figure legend, the reader is referred to the web version of this article.)

changes  can  also  remove  or  at  least  reduce  the  BRDF  differences
embedded in the satellite data, and in this way, the change pixel can be
correctly identified (Fig. 10b) using a time-series based change detection
algorithm (Zhu et al., 2020). It is worth noting that the angular infor-
mation  can  be  useful  for  identifying  the  target  and  location  of  land
change, such as improving land cover classification (Jiao et al., 2011),
detecting moving objects such as clouds (Frantz et al., 2018), aircraft
(Liu et al., 2020b), and detection of newly built houses (Huang et al.,

2020), due to the inclusion of 3D information.

4.5. Data-integration issues

With  the  increased  availability  of  Earth  observation  satellites,  the
integration of multi-sensor datasets could offer complementary views on
spatial, temporal, and spectral dimensions, providing a unique oppor-
tunity for approaching a multifaceted land change problem (Dong et al.,

RemoteSensingofEnvironment282(2022)11326612Z. Zhu et al.

2009).  Methods  for  integrating  multi-sensor  datasets  for  multifaceted
land  change  studies  can  be  generally  categorized  into  observation
fusion, decision fusion, and information fusion. Observation fusion re-
fers to the strategy of combining multiple data sources into a consistent
blending observation set to create a finer temporal, spatial or spectral
resolution dataset as the algorithm’s inputs (Emelyanova et al., 2013;
Gao  et  al.,  2006;  Shang  et  al.,  2022).  Decision  fusion,  also  named
“competitive  integration”  (Schmitt  and  Zhu,  2016),  combines  similar
change facet information from different sensor-specific pipelines, aim-
ing at producing more reliable results for one single change facet (Car-
dille et al., 2022; Reiche et al., 2018). Information fusion, such as the
“complementary integration” (Schmitt and Zhu, 2016), is the fusion of
multi-sensor pipeline results targeted at different change facets, with a
goal  of  providing  complementary  change  information.  While  a
comprehensive  review  of  these  integration  techniques  is  beyond  the
scope of this article, it is important to recognize their conceptual dif-
ference in the context of multifaceted change analysis. Observation and
decision fusion have been widely applied to single-facet tasks such as
change  detection  or  land  cover  classification  to  answer  “when”,
“where”, and “what”, but much fewer were on change metrics or agents
(Fernandez-Manso  et  al.,  2019;  Meng  et  al.,  2018);comparatively,  a
paucity  of  information fusion  studies  on monitoring  land  change was
reported, partly due to a lack of recognizing change as a multifaceted
problem. Another challenge for information fusion is that different data
sources  may  have  different  geographic  coverage,  for  example,  LiDAR
and hyperspectral images are often unable to provide wall-to-wall land
change  information  similar  to  medium  or  coarse-resolution  images,
which implies that data interpolation is often required.

Beyond  remote  sensing  observations,  an  increasing  array  of  social
science data have shown their great promise for unveiling social/eco-
nomic processes that are not manifested on the landscape, pinpointing
the question of “why”  the land change happened. Social science data-
sets, such as population density, capital investment, poverty gap index,
were  often  manipulated  as  explanatory  variables  for  establishing
empirical  models  and  used  to  infer  causes  or  drivers  of  land  changes
observed from remote sensing images (NRC, 2013; Seto and Kaufmann,
2003; Wyman and Stein, 2010). While such applications for integrating
the remotely sensed (pixels) data with social science (people) data have
been  a  major  focus  in  land  change  science  (Lambin,  2004),  their
fundamental  differences  in  data  format  create  lots  of  challenges.  The
national Academy of Science volume “People and Pixels” (NRC, 1998)
and  Rindfuss  et  al.  (2012)  have  exemplified  several  data  integration
issues, such as different data presentations (e.g., “discrete” vs “contin-
uous”),  inconsistent  temporal  depth  and  data  complexities,  and
traversing  the  languages  and  terminology  from  different  disciplines.
Conventionally,  the  social  science  data  were  collected  based  on  field
observations, interviews with local people, and surveys, which is time
consuming,  labor  intensive,  and  usually  out-of-date.  The  Volunteered
Geographic Information (VGI) has been a paradigm shift that offers an
alternative mechanism for collecting and compilating the georeferenced
social science data (Goodchild, 2007). Through content retrieval, cate-
gorization and meta-data analysis (Daume et al., 2014), and georefer-
enced VGI data (such as from media reports or geotagged social media
posts)  can  be  integrated  at  decision  or  information  levels,  which  im-
proves insights not just on the disturbance agents from a “local view”,
but also uniquely uncovers the socioeconomic drivers underlying land
surface change, such as narcotrafficking (Sesnie et al., 2017; Tellman
et al., 2020) and population increase (Minale, 2013). Another notable
advantage of the VGI data is that their availability is usually more timely
(e.g., social media data), and by combining with other near real-time
satellite data sources, the social media datasets have showcased their
capacity for advancing those time-sensitive change detection tasks such
as rapid disaster mapping (Fohringer et al., 2015; Rosser et al., 2017;
Schnebele et al., 2014). Despite its great potential, several factors pre-
clude populating the VGI dataset of the present day for a wall-to-wall
land  change  mapping.  First  and  foremost,  the  data  quality  of  VGI  is

questionable due to their geolocation inaccuracy, participants’ bias, or
context  ambiguity;  trickier  might  be  that  data  uncertainty  accompa-
nying VGI data, unlike remote sensing datasets, are mostly unmeasur-
able and unmanageable (Goodchild and Li, 2012). The coverage of the
VGI dataset is also limited and cannot be extended to the same level as
remotely  sensed  images,  causing  a  grave  technical  challenge  for
enabling a geographically consistent mapping. Lastly, VGI data may not
uncover  some  change  agents  such  as  gradual  stress-related  changes.
Generally, the blending of VGI and remote sensing datasets is in infancy,
and  its  relevance  to  land  change  studies  is  still  inconclusive.  More
foundational  research  on  data  processing  protocols  and  well-verified,
localized study cases are both anticipated for the future, allowing for a
broader examination for incorporation of VGI datasets into the current
production workflow.

5. Current land change products

Lots  of  remote  sensing-based  land  change  products  have  been
created, and some of them have been widely used in a variety of fields,
such  as  environmental  sustainability,  land  management,  biodiversity
conservation, and ecosystem health assessment. However, most of these
land change products only focus on three facets of land change –  the
location, time, and target of change (mostly land cover), and very few
products are trying to provide some of the other facets of land change,
such as change agent or change metric (Table 1).

Most  of  the  current  large-scale  land  change  products  are  only
focusing on a single change target, such as changes in forest, urban, or
water  (Table  1).  For  instance,  Hansen  et  al.  (2013)  created  the
2000–2019 global 30-m forest cover and forest cover change (i.e., forest
loss and forest grain) products based on time series spectral metrics of
Landsat  data  and  a  supervised  classification  approach.  The  North
American Forest Dynamics (NAFD) project implemented the Vegetation
Change Tracker (VCT) algorithm (Huang et al., 2010) to produce annual
forest  disturbance  maps  for  the  conterminous  United  States  (CONUS)
from 1986 to 2010 based on annual Landsat time series data (Zhao et al.,
2018). Liu et al. (2020a) created 30-m Global Annual Urban Dynamics
(GAUD)  dataset  for  providing  information  on  urban  expansion  and
green recovery from 1985 to 2015 based on existing global urban extent
maps and Landsat time series data. European Space Agency (ESA) pro-
duced the Global Human Settlement Layer (GHSL) for multiple years,
which can provide new global spatial information, evidence-based an-
alytics, and knowledge describing the human presence such as built-up
area and population distribution on the Earth (Pesaresi et al., 2016). The
ESA Global Surface Water (GSW) dataset provides different facets of the
spatial and temporal distribution of surface water over long time periods
at a 30-m resolution based on 30+ years of Landsat data, such as water
occurrence for presenting overall water dynamics, water recurrence for
describing how frequently water returned from one year to another, and
water  seasonality  for  capturing  the  intra-annual  dynamics  of  water
surfaces (Pekel et al., 2016). This dataset also includes water occurrence
change intensity maps between two epochs (1984 to 1999, and 2000 to
2020), which can provide information on where surface water occur-
rence increased, decreased, or remained the same. In addition, products
of  single  change agent  are  available  as  well, particularly  for  fire.  For
example,  Giglio  et  al.  (2018)  applied  dynamic  thresholds  of  a  burn-
sensitive  vegetation  index  composite  data  (derived  from  daily  500  m
MODIS time series) to generate a global burned area product, in which
the date of the burned area will be provided within each MODIS tile with
10 degrees by 10 degrees.

Only  a  few  products  can  provide  information  on  land  change  on
different  kinds  of  land  surfaces.  The  National  Land  Cover  Database
(NLCD)  provides  multi-temporal  land  cover  and  land  cover  change
products for CONUS, Hawaii, Alaska, and Puerto Rico between 2001 and
2019 for every 2–3 year interval, based on decadal Landsat data as well
as other ancillary datasets (Jin et al., 2019). Using daily seamless data
cubes  generated  from  multi-source  remote  sensing  data,  Liu  et  al.

RemoteSensingofEnvironment282(2022)11326613Z. Zhu et al.

Table 1
A select list of current global and North America land change products. Only the most recent literature is listed here.

Change Metric

Change Agent

Satellite
Data

Landsat

Landsat

Citation

(Hansen et al.,
2013)
(Pekel et al., 2016)

MODIS

Landsat

Landsat

(Giglio et al.,
2018)
(Zhao et al., 2018)

(Pesaresi et al.,
2016)

Landsat

(Jin et al., 2019)

Fire, Mechanical,
Insect, Windthrow

Landsat

(Rollins, 2009)

N/A

Landsat

(Liu et al., 2020a)

N/A

Landsat

(Brown et al.,
2020)

Product Name

Coverage

Change
Location

Change Time
(Period)

Hansen forest
change map
Global Surface

Water

Global

30-m

Global

30-m

Annual
(2000–2019)
Intra-annual
Annual
(1984–2020)

MODIS burned

Global

500-m

area

NAFD-NEX

CONUS

30-m

GHSL

Global

NLCD

LANDFIRE

United
States

United
States

30-, 250-,
and 1000-
m
30-m

30-m

GAUD

Global

30-m

LCMAP

CONUS

30-m

iMap

Global

30-m

NALCMS

NTEMS

North
America
Canada

30- and
250-m
30-m

GLanCE

Global

30-m

GLCLUC2020

Global

30-m

Day of Year
(2000-Present)
Annual
(1986–2010)
Multiple years
(1975, 1990, 2000, and
2014)
2–3 years
(2001–2019)

Annual
Day of Year
(1999–2020)

Annual
(1985–2015)

Annual
Day of Year
(1985–2019)

Annual
Seasonal
(1985–2010)
5 years
(2001–2015)
Annual
(1984–2019 for land cover;
1985–2017 for recovery;
1985–2015 for disturbance
agent)
Annual
(2001(cid:0) 2020)
Annual (2000(cid:0) 2020)

Change
Target

Forest gain
Forest loss
Water
seasonality
Water
transitions
Annual water
recurrence
Burned area

Forest
disturbance
Built-up area

Land cover
change
Forest
disturbance
Vegetation
transition

Urban
expansion
Green
recovery
Land cover
change
Land spectral
change

Land cover
change

Land cover
change
Land cover
change

N/A

Water
occurrence
Change intensity

N/A

N/A

N/A

N/A

Disturbance
severity
Time since
disturbance
N/A

Change
magnitude
Spectral stability
period
Time since last
change
N/A

N/A

N/A

N/A

Fire

N/A

N/A

N/A

N/A

N/A

Landsat,
MODIS, and
AVHRR
Landsat and
MODIS
Landsat and
LiDAR

(Liu et al., 2021a)

(Latifovic et al.,
2016)
(Hermosilla et al.,
2022; White et al.,
2017, 2022)

Post-disturbance
recovery rate

Fire, Harvest, Road,
Non-stand replacing
disturbance

Land cover
change
Land cover
change

N/A

N/A

N/A

N/A

Landsat

Landsat

(Friedl et al.,
2022)
(Potapov et al.,
2022)

Notes: CONUS: COnterminous United States; NLCD: National Land Cover Database; LCMAP: Land Change Monitoring, Assessment, and Projection; GHSL: Global
Human Settlement Layer; GAUD: Global Annual Urban Dynamics; NAFD-NEX: North American Forest Dynamics - NASA Earth Exchange; NALCMS: North American
Land Cover Change Monitoring System; NTEMS: National Terrestrial Ecosystem Monitoring System; GLanCE: Global Land Cover Estimation; GLCLUC: Global Land
Cover and Land Use Change.

(2021a) generated 30 m resolution global land cover map data for 36
years by combining strategies of sample migration, machine learning,
and spatio-temporal adjustment, which can be used to study global land
change. Recently, Friedl et al. (2022) and Potapov et al. (2022) have also
created annual global land cover change maps between 2000 and 2020
based  on  the  Landsat  time  series.  Among  all  these  products,  Land
Change Monitoring, Assessment, and Projection (LCMAP) (Brown et al.,
2020), LANDFIRE (Rollins, 2009), and National Terrestrial Ecosystem
Monitoring System (NTEMS) (Hermosilla et al., 2022; White et al., 2017,
2022) are some of the few land change products that not only can pro-
vide  change  location  and  time,  change  target,  but  also  land  change
metrics, or even land change agent information.

6. Conclusion and recommendations

Land change science has made big advancements with the develop-
ment of remote sensing technology, and questions of where, when, what,

why, and how this change takes place can be fully evaluated and map-
ped. We proposed a new concept of the multifaceted view of land change
through  the  lens  of  remote  sensing  and  recommended  five  facets
including  change  location,  time,  target,  metric,  and  agent.  We  also
discussed the relationship of various kinds of land change terminologies
including spectral change,  land surface  change,  biophysical/biochem-
ical parameter change, land disturbance, climate change, climate vari-
ability, succession, land cover change, land cover conversion, and land
cover modifications, in which large differences were identified among
these  terminologies.  The  impacts  of  spatial,  spectral,  temporal,  and
angular  domains  of  the  remotely  sensed  data  on  observation,  moni-
toring,  and  characterization  of  land  change  were  also  evaluated.  We
emphasized the importance of selecting the “right” spectral bands and
spatial resolution  of  remote  sensing  data  for the  specific  land change
problem.  We  discussed  the  benefits  and  challenges  when  dense  time-
series  and  multi-angle  satellite  observations  are  used  for  observing
and characterizing land change. We also reviewed some of the current

RemoteSensingofEnvironment282(2022)11326614Z. Zhu et al.

land  change  products  and  observed the  lack of  products  that  provide
multiple,  or  all  land  change  facets,  particularly  for  the  facets  of  land
change agent and metric.

Therefore,  we  have  a  few  recommendations  on  remote  sensing  of
land change as follows. First, it is important to recognize the multifac-
eted nature of land change, and when remote sensing data are used to
study land change, specifying which land change facet is being studied,
is  usually  the  first  step.  Second,  remote  sensing-derived  land  change
products reported with all five facets are highly recommended, as land
change can only be fully understood if they are viewed from all different
angles. Third, we think a major shift in the focus from change target to
change metric and change agent is expected in future remote sensing
studies, as  these two  facets  are far  less studied in  the remote  sensing
community, and why and how global land is changing are some of the
most  difficult  and  important  science  questions.  Fourth,  land  change
science has transitioned into more complex systems such as land system
science (Turner et al., 2021), which requires deeper and more compre-
hensive  land  change  information.  For  example,  most  of  the  current
remote sensing change agent products are not detailed enough for social
sciences to answer the question of “why”, and the combined use of social
science  data  and  multiple  remote  sensing  data  sources  could  provide
new and deeper insights. Finally, we need to recognize that every remote
sensing system has limitations and weaknesses in land change studies,
and a thorough evaluation of all spectral, spatial, temporal, and angular
issues is highly recommended.

Declaration of Competing Interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Data availability

The remote sensing data used in this review were downloaded from

USGS, NASA, Copernicus, and Planet Labs.

Acknowledgment

This  research  was  supported  by  the  USGS-NASA  Landsat  Science
Team Program for Toward Near Real-time Monitoring and Character-
ization  of  Landsat  Surface  Change  for  the  Conterminous  US
(140G0119C0008). We would like to thank Billie Turner II and the five
anonymous reviewers for their insightful comments and suggestions for
this  manuscript.  The  content  of  this  document  does  not  necessarily
represent  the views or policies of the Department of the Interior, nor
does  mention  of  trade  names,  commercial  products,  or  organizations
imply endorsement by the U.S. Government.

References

Anderson, J.R., Hardy, E.E., Roach, J.T., Witmer, R.E., 1976. A land use and land cover
classification system for use with remote sensor data, Washington, DC: government
printing office (US geological survey. Professional Paper 964. https://doi.org/
10.3133/pp964.

Asner, G.P., Knapp, D.E., Balaji, A., P´aez-Acosta, G., 2009. Automated mapping of

tropical deforestation and forest degradation: CLASlite. J. Appl. Remote. Sens. 3,
33543. https://doi.org/10.1117/1.3223675.

Asner, G.P., Knapp, D.E., Broadbent, E.N., Oliveira, P.J.C., Keller, M., Silva, J.N., 2005.
Selective logging in the brazilian Amazon. Science 310, 480–482. https://doi.org/
10.1126/science.1118051.

Baker, B.A., Warner, T.A., Conley, J.F., McNeil, B.E., 2013. Does spatial resolution
matter? A multi-scale comparison of object-based and pixel-based methods for
detecting change associated with gas well drilling operations. Int. J. Remote Sens.
34, 1633–1651.

Banskota, A., Kayastha, N., Falkowski, M.J., Wulder, M.A., Froese, R.E., White, J.C.,

2014. Forest monitoring using landsat time series data: a review. Can. J. Remote.
Sens. 40, 362–384. https://doi.org/10.1080/07038992.2014.987376.

Bartels, S.F., Chen, H.Y.H., Wulder, M.A., White, J.C., 2016. Trends in post-disturbance
recovery rates of Canada’s forests following wildfire and harvest. For. Ecol. Manag.
361, 194–207. https://doi.org/10.1016/j.foreco.2015.11.015.

Beck, P.S.A., Atzberger, C., Høgda, K.A., Johansen, B., Skidmore, A.K., 2006. Improved
monitoring of vegetation dynamics at very high latitudes: a new method using
MODIS NDVI. Remote Sens. Environ. 100, 321–334.

Belward, A.S., Skøien, J.O., 2015. Who launched what, when and why; trends in global
land-cover observation capacity from civilian earth observation satellites. ISPRS J.
Photogramm. Remote Sens. 103, 115–128. https://doi.org/10.1016/j.
isprsjprs.2014.03.009.

Bowman, D.M.J.S., Balch, J., Artaxo, P., Bond, W.J., Cochrane, M.A., D’antonio, C.M.,
DeFries, R., Johnston, F.H., Keeley, J.E., Krawchuk, M.A., 2011. The human
dimension of fire regimes on earth. J. Biogeogr. 38, 2223–2236. https://doi.org/
10.1111/j.1365-2699.2011.02595.x.

Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,

Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., 2020. Lessons
learned implementing an operational continuous United States national land change
monitoring capability: the land change monitoring, assessment, and project
(LCMAP) approach. Remote Sens. Environ. 238, 111356 https://doi.org/10.1016/j.
rse.2019.111356.

Bruzzone, L., Bovolo, F., 2012. A novel framework for the design of change-detection

systems for very-high-resolution remote sensing images. Proceedings of the IEEE 101
(3), 609–630. https://doi.org/10.1109/JPROC.2012.2197169.

Buchner, J., Yin, H., Frantz, D., Kuemmerle, T., Askerov, E., Bakuradze, T., Bleyhl, B.,
Elizbarashvili, N., Komarova, A., Lewi´nska, K.E., 2020. Land-cover change in the
Caucasus Mountains since 1987 based on the topographic correction of multi-
temporal landsat composites. Remote Sens. Environ. 248, 111967 https://doi.org/
10.1016/j.rse.2020.111967.

Cardille, J.A., Perez, E., Crowley, M.A., Wulder, M.A., White, J.C., Hermosilla, T., 2022.

Multi-sensor change detection for within-year capture and labelling of forest
disturbance. Remote Sens. Environ. 268, 112741.

Chirici, G., Giannetti, F., Mazza, E., Francini, S., Travaglini, D., Pegna, R., White, J.C.,
2020. Monitoring clearcutting and subsequent rapid recovery in Mediterranean
coppice forests with landsat time series. Ann. For. Sci. 77, 1–14.

Chowdhury, S., Peddle, D.R., Wulder, M.A., Heckbert, S., Shipman, T.C., Chao, D.K.,

2021. Estimation of land-use/land-cover changes associated with energy footprints
and other disturbance agents in the upper peace region of Alberta Canada from 1985
to 2015 using landsat data. Int. J. Appl. Earth Obs. Geoinf. 94, 102224.
Chu, T., Guo, X., Takeda, K., 2016. Remote sensing approach to detect post-fire
vegetation regrowth in siberian boreal larch forest. Ecol. Indic. 62, 32–46.

Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.C., Skakun, S.V.,

Justice, C., 2018. The harmonized landsat and Sentinel-2 surface reflectance data
set. Remote Sens. Environ. 219, 145–161. https://doi.org/10.1016/j.
rse.2018.09.002.

Clements, F.E., 1916. Plant succession: an analysis of the development of vegetation.

Carnegie Institution of Washington.

Cohen, W.B., Goward, S.N., 2004. Landsat’s role in ecological applications of remote
sensing. Bioscience 54, 535–545. https://doi.org/10.1641/0006-3568(2004)054
[0535:LRIEAO]2.0.CO;2.

Colditz, R.R., Pouliot, D., Llamas, R.M., Homer, C., Latifovic, R., Ressl, R.A., Tovar, C.M.,
Hern´andez, A.V., Richardson, K., 2014. Detection of North American land cover
change between 2005 and 2010 with 250m MODIS data. PE&RS. Photogramm. Eng.
Remote Sens. 80, 918–924.

Comber, A., Wulder, M., 2019. Considering spatiotemporal processes in big data analysis:
Insights from remote sensing of land cover and land use. Trans. GIS 23, 879–891.
Coops, N.C., Johnson, M., Wulder, M.A., White, J.C., 2006. Assessment of QuickBird high
spatial resolution imagery to detect red attack damage due to mountain pine beetle
infestation. Remote Sens. Environ. 103, 67–80.

Coppin, P., Jonckheere, I., Nackaerts, K., Muys, B., Lambin, E., 2004. Digital change

detection methods in ecosystem monitoring: a review. Int. J. Remote Sens. 25,
1565–1596.

Coppin, P.R., Bauer, M.E., 1996. Digital change detection in forest ecosystems with

remote sensing imagery. Remote Sens. Rev. 13, 207–234. https://doi.org/10.1080/
02757259609532305.

Cui, T., Martz, L., Zhao, L., Guo, X., 2020. Investigating the impact of the temporal
resolution of MODIS data on measured phenology in the prairie grasslands.
GIScience Remote Sens. 57, 395–410.

Dale, V.H., 1997. The relationship between land-use change and climate change. Ecol.
Appl. 7, 753–769. https://doi.org/10.1890/1051-0761(1997)007[0753:TRBLUC]
2.0.CO;2.

Dale, V.H., Joyce, L.A., McNulty, S., Neilson, R.P., Ayres, M.P., Flannigan, M.D.,

Hanson, P.J., Irland, L.C., Lugo, A.E., Peterson, C.J., 2001. Climate change and forest
disturbances: climate change can affect forests by altering the frequency, intensity,
duration, and timing of fire, drought, introduced species, insect and pathogen
outbreaks, hurricanes, windstorms, ice storms, or landslides. Bioscience 51,
723–734. https://doi.org/10.1641/0006-3568(2001)051[0723:CCAFD]2.0.CO;2.

Daume, S., Albert, M., von Gadow, K., 2014. Forest monitoring and social

media–Complementary data sources for ecosystem surveillance? For. Ecol. Manag.
316, 9–20.

de Beurs, K.M., Henebry, G.M., Owsley, B.C., Sokolik, I., 2015. Using multiple remote

sensing perspectives to identify and attribute land surface dynamics in Central Asia
2001–2013. Remote Sens. Environ. 170, 48–61. https://doi.org/10.1016/j.
rse.2015.08.018.

De Jong, R., Verbesselt, J., Schaepman, M.E., De Bruin, S., 2012. Trend changes in global

greening and browning: Contribution of short-term trends to longer-term change.

RemoteSensingofEnvironment282(2022)11326615Z. Zhu et al.

Glob. Chang. Biol. 18, 642–655. https://doi.org/10.1111/j.1365-2486.2011.02578.
x.

Deng, C., Zhu, Z., 2020. Continuous subpixel monitoring of urban impervious surface
using Landsat time series. Remote Sens. Environ. 238, 110929 https://doi.org/
10.1016/j.rse.2018.10.011.

Dong, J., Zhuang, D., Huang, Y., Fu, J., 2009. Advances in multi-sensor data fusion:

Algorithms and applications. Sensors 9, 7771–7784.

Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., Hoersch, B.,
Isola, C., Laberinti, P., Martimort, P., Meygret, A., Spoto, F., Sy, O., Marchese, F.,
Bargellini, P., 2012. Sentinel-2: ESA’s Optical High-Resolution Mission for GMES
Operational Services. Remote Sens. Environ. 120, 25–36. https://doi.org/10.1016/j.
rse.2011.11.026.

Dwyer, J., Roy, D., Sauer, B., Jenkerson, C., Zhang, H., Lymburner, L., 2018. Analysis
Ready Data: Enabling Analysis of the Landsat Archive. Remote Sens. 10, 1363.
https://doi.org/10.3390/rs10091363.

Eidenshink, J., Schwind, B., Brewer, K., Zhu, Z., Quayle, B., Howard, S., Falls, S., Falls, S.,
2007. A Project for Monitoring Trends in Burn Severity. Fire Ecol. 3, 3–21. https://
doi.org/10.4996/fireecology.0301003.

Ellis, E.C., Klein Goldewijk, K., Siebert, S., Lightman, D., Ramankutty, N., 2010.

Anthropogenic transformation of the biomes, 1700 to 2000. Glob. Ecol. Biogeogr.
19, 589–606. https://doi.org/10.1111/j.1466-8238.2010.00540.x.

Elvidge, C.D., Zhizhin, M., Ghosh, T., Hsu, F.-C., Taneja, J., 2021. Annual time series of
global VIIRS nighttime lights derived from monthly averages: 2012 to 2019. Remote
Sens. 13, 922. https://doi.org/10.3390/rs13050922.

Emelyanova, I.V., McVicar, T.R., Van Niel, T.G., Li, L.T., Van Dijk, A.I.J.M., 2013.
Assessing the accuracy of blending Landsat–MODIS surface reflectances in two
landscapes with contrasting spatial and temporal dynamics: A framework for
algorithm selection. Remote Sens. Environ. 133, 193–209.

Fang, F., McNeil, B.E., Warner, T.A., Maxwell, A.E., Dahle, G.A., Eutsler, E., Li, J., 2020.
Discriminating tree species at different taxonomic levels using multi-temporal
WorldView-3 imagery in Washington DC, USA. Remote Sens. Environ. 246, 111811.

Fernandez-Manso, A., Quintano, C., Roberts, D.A., 2019. Burn severity analysis in

Mediterranean forests using maximum entropy model trained with EO-1 Hyperion
and LiDAR data. ISPRS J. Photogramm. Remote Sens. 155, 102–118.

Firebaugh, G., Warner, C., Massoglia, M., 2013. Fixed effects, random effects, and hybrid
models for causal analysis. In: Handbook of Causal Analysis for Social Research.
Springer, pp. 113–132.

Fohringer, J., Dransch, D., Kreibich, H., Schr¨oter, K., 2015. Social media as an

information source for rapid flood inundation mapping. Nat. Hazards Earth Syst. Sci.
15, 2725–2738.

Foody, G.M., Doan, H.T.X., 2007. Variability in soft classification prediction and its
implications for sub-pixel scale change detection and super resolution mapping.
Photogramm. Eng. Remote Sens. 73, 923–933. https://doi.org/10.14358/
PERS.73.8.923.

Forzieri, G., Dakos, V., McDowell, N.G., Ramdane, A., Cescatti, A., 2022. Emerging

signals of declining forest resilience under climate change. Nature 608, 534–539.
https://doi.org/10.1038/s41586-022-04959-9.

Frantz, D., 2019. FORCE—Landsat+ Sentinel-2 analysis ready data and beyond. Remote

Sens. 11, 1124. https://doi.org/10.3390/rs11091124.

Frantz, D., Haß, E., Uhl, A., Stoffels, J., Hill, J., 2018. Improvement of the Fmask

algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on
parallax effects. Remote Sens. Environ. 215, 471–481. https://doi.org/10.1016/j.
rse.2018.04.046.

Friedl, M.A., Woodcock, C.E., Olofsson, P., Zhu, Z., Loveland, T., Stanimirova, R.,

Arevalo, P., Bullock, E., Hu, K.-T., Zhang, Y., Turlej, K., Tarrio, K., McAvoy, K.,
Gorelick, N., Wang, J.A., Barber, C.P., Souza, C., 2022. Medium Spatial Resolution
Mapping of Global Land Cover and Land Cover Change Across Multiple Decades
From Landsat. Front. Remote Sens. 3 https://doi.org/10.3389/frsen.2022.894571.

Friis, C., Nielsen, J.Ø., Otero, I., Haberl, H., Niew¨ohner, J., Hostert, P., 2016. From
teleconnection to telecoupling: Taking stock of an emerging framework in land
system science. J. Land Use Sci. 11, 131–153. https://doi.org/10.1080/
1747423X.2015.1096423.

Ganguly, S., Friedl, M.A., Tan, B., Zhang, X., Verma, M., 2010. Land surface phenology
from MODIS: Characterization of the Collection 5 global land cover dynamics
product. Remote Sens. Environ. 114, 1805–1816.

Gao, F., Masek, J., Schwaller, M., Hall, F., 2006. On the blending of the Landsat and

MODIS surface reflectance: Predicting daily Landsat surface reflectance. IEEE Trans.
Geosci. Remote Sens. 44, 2207–2218.

Goodchild, M.F., 2007. Citizens as sensors: the world of volunteered geography.
GeoJournal 69, 211–221. https://doi.org/10.1007/s10708-007-9111-y.
Goodchild, M.F., Li, L., 2012. Assuring the quality of volunteered geographic

information. Spat Stat 1, 110–120. https://doi.org/10.1016/j.spasta.2012.03.002.

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., Moore, R., 2017.

Google Earth Engine: Planetary-scale geospatial analysis for everyone. Remote Sens.
Environ. 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031.

Grime, J.P., 1977. Evidence for the existence of three primary strategies in plants and its

relevance to ecological and evolutionary theory. Am. Nat. 111, 1169–1194.

Guo, B., Gunn, S.R., Damper, R.I., Nelson, J.D.B., 2006. Band selection for hyperspectral

image classification using mutual information. IEEE Geosci. Remote Sens. Lett. 3,
522–526.

Guo, X., Feng, J., Shi, Z., Zhou, X., Yuan, M., Tao, X., Hale, L., Yuan, T., Wang, J., Qin, Y.,

2018. Climate warming leads to divergent succession of grassland microbial
communities. Nat. Clim. Chang. 8, 813–818. https://doi.org/10.1038/s41558-018-
0254-2.

Gutman, G., Janetos, A.C., Justice, C.O., Moran, E.F., Mustard, J.F., Rindfuss, R.R.,

Skole, D., Turner II, B.L., Cochrane, M.A., 2004. Land change science: observing,
monitoring and understanding trajectories of change on the earth’s surface. Springer
Science & Business Media.

Hall, F.G., Botkin, D.B., Strebel, D.E., Woods, K.D., Goetz, S.J., 1991. Large-scale patterns

of forest succession as determined by remote sensing. Ecology 72, 628–640.
Hansen, M.C., DeFries, R.S., 2004. Detecting long-term global forest change using
continuous fields of tree-cover maps from 8-km advanced very high resolution
radiometer (AVHRR) data for the years 1982–99. Ecosystems 7, 695–716, 10.1007%
2Fs10021-004-0243.

Hansen, M.C., Loveland, T.R., 2012. A review of large area monitoring of land cover
change using Landsat data. Remote Sens. Environ. 122, 66–74. https://doi.org/
10.1016/j.rse.2011.08.024.

Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., Turubanova, S.A.A., Tyukavina, A.,
Thau, D., Stehman, S.V., Goetz, S.J., Loveland, T.R., Kommareddy, A., 2013. High-
resolution global maps of 21st-century forest cover change. Science 342, 850–853.
https://doi.org/10.1126/science.1244693.

Hart, S.J., Veblen, T.T., 2015. Detection of spruce beetle-induced tree mortality using

high- and medium-resolution remotely sensed imagery. Remote Sens. Environ. 168,
134–145. https://doi.org/10.1016/j.rse.2015.06.015.

Healey, S.P., Cohen, W.B., Yang, Z., Kenneth Brewer, C., Brooks, E.B., Gorelick, N.,
Hernandez, A.J., Huang, C., Joseph Hughes, M., Kennedy, R.E., Loveland, T.R.,
Moisen, G.G., Schroeder, T.A., Stehman, S.V., Vogelmann, J.E., Woodcock, C.E.,
Yang, L., Zhu, Z., 2018. Mapping forest change using stacked generalization: An
ensemble approach. Remote Sens. Environ. 204, 717–728. https://doi.org/10.1016/
j.rse.2017.09.029.

Henson, S.A., Cole, H.S., Hopkins, J., Martin, A.P., Yool, A., 2018. Detection of climate

change-driven trends in phytoplankton phenology. Glob. Chang. Biol. 24,
e101–e111.

Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2022. Land cover classification in
an era of big and open data: Optimizing localized implementation and training data
selection to improve mapping outcomes. Remote Sens. Environ. 268, 112780.
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., 2018. Disturbance-
Informed Annual Land Cover Classification Maps of Canada’s Forested Ecosystems
for a 29-Year Landsat Time Series. Can. J. Remote. Sens. 44, 67–87. https://doi.org/
10.1080/07038992.2018.1437719.

Homer, C., Dewitz, J., Fry, J., Coan, M., Hossain, N., Larson, C., Herold, N.,

McKerrow, A., VanDriel, J.N., Wickham, J., 2007. Completion of the 2001 national
land cover database for the counterminous United States. Photogramm. Eng. Remote
Sens. 337–341.

Homer, C., Dewitz, J., Jin, S., Xian, G., Costello, C., Danielson, P., Gass, L., Funk, M.,

Wickham, J., Stehman, S., 2020. Conterminous United States land cover change
patterns 2001–2016 from the 2016 national land cover database. ISPRS J.
Photogramm. Remote Sens. 162, 184–199.

Homer, C., Dewitz, J., Yang, L., Jin, S., Danielson, P., Xian, G., Coulston, J., Herold, N.,
Wickham, J., Megown, K., 2015. Completion of the 2011 National Land Cover
Database for the conterminous United States–representing a decade of land cover
change information. Photogramm. Eng. Remote Sens. 81, 345–354.

Huang, C., Goward, S.N., Masek, J.G., Thomas, N., Zhu, Z., Vogelmann, J.E., 2010. An
automated approach for reconstructing recent forest disturbance history using dense
Landsat time series stacks. Remote Sens. Environ. 114, 183–198. https://doi.org/
10.1016/j.rse.2009.08.017.

Gao, F., Masek, J.G., Wolfe, R.E., 2009. Automated registration and orthorectification

Huang, H., Roy, D.P., 2021. Characterization of Planetscope-0 Planetscope-1 surface

package for Landsat and Landsat-like data processing. J. Appl. Remote. Sens. 3,
033515 https://doi.org/10.1117/1.3104620.

Garbulsky, M.F., Pe˜nuelas, J., Gamon, J., Inoue, Y., Filella, I., 2011. The photochemical
reflectance index (PRI) and the remote sensing of leaf, canopy and ecosystem
radiation use efficiencies: A review and meta-analysis. Remote Sens. Environ. 115,
281–297. https://doi.org/10.1016/j.rse.2010.08.023.

Geist, H.J., Lambin, E.F., 2002. Proximate Causes and Underlying Driving Forces of
Tropical DeforestationTropical forests are disappearing as the result of many
pressures, both local and regional, acting in various combinations in different
geographical locations. Bioscience 52, 143–150. https://doi.org/10.1641/0006-
3568(2002)052[0143:PCAUDF]2.0.CO;2.

Giglio, L., Boschetti, L., Roy, D.P., Humber, M.L., Justice, C.O., 2018. The Collection 6
MODIS burned area mapping algorithm and product. Remote Sens. Environ. 217,
72–85. https://doi.org/10.1016/j.rse.2018.08.005.

G´omez, C., White, J.C., Wulder, M.A., 2016. Optical remotely sensed time series data for
land cover classification: A review. ISPRS J. Photogramm. Remote Sens. 116, 55–72.
https://doi.org/10.1016/j.isprsjprs.2016.03.008.

reflectance and normalized difference vegetation index continuity. Sci. Remote Sens.
3, 100014 https://doi.org/10.1016/j.srs.2021.100014.

Huang, S., Ramirez, C., McElhaney, M., Clark, C., Yao, Z., 2019. Quantifying

spatiotemporal post-disturbance recovery using field inventory, tree growth, and
remote sensing. Earth Sp. Sci. 6, 489–504.

Huang, X., Cao, Y., Li, J., 2020. An automatic change detection method for monitoring
newly constructed building areas using time-series multi-view high-resolution
optical satellite images. Remote Sens. Environ. 244, 111802 https://doi.org/
10.1016/j.rse.2020.111802.

Huete, A., 2016. Vegetation’s responses to climate variability. Nature 531, 181–182.

https://doi.org/10.1038/nature17301.

Hussain, M., Chen, D., Cheng, A., Wei, H., Stanley, D., 2013. Change detection from
remotely sensed images: From pixel-based to object-based approaches. ISPRS J.
Photogramm. Remote Sens. https://doi.org/10.1016/j.isprsjprs.2013.03.006.
Huston, M., Smith, T., 1987. Plant succession: life history and competition. Am. Nat. 130,

168–198. https://doi.org/10.1016/j.ecoleng.2021.106331.

RemoteSensingofEnvironment282(2022)11326616Z. Zhu et al.

Jensen, J.R., 2009. Remote Sensing of the Environment: An Earth Resource Perspective

2/e. Pearson Education India.

Jiao, Z., Woodcock, C., Schaaf, C.B., Tan, B., Liu, J., Gao, F., Strahler, A., Li, X., Wang, J.,
2011. Improving MODIS land cover classification by combining MODIS spectral and
angular signatures in a Canadian boreal forest. Can. J. Remote. Sens. 37, 184–203.
https://doi.org/10.5589/m11-030.

Jin, S., Homer, C., Yang, L., Danielson, P., Dewitz, J., Li, C., Zhu, Z., Xian, G., Howard, D.,
2019. Overall methodology design for the United States national land cover database
2016 products. Remote Sens. 11 https://doi.org/10.3390/rs11242971.

Jin, S., Sader, S.A., 2005. MODIS time-series imagery for forest disturbance detection and
quantification of patch size effects. Remote Sens. Environ. 99, 462–470. https://doi.
org/10.1016/j.rse.2005.09.017.

Johnson, E.A., Miyanishi, K., 2021. Disturbance and succession. In: Johnson, E.A.,
Miyanishi, K.B.T.-P.D.E. (Eds.), Plant Disturbance Ecology, Second edition.
Academic Press, San Diego, pp. 1–15. https://doi.org/10.1016/B978-0-12-818813-
2.00001-0.

active fire characteristics and post-fire effects. Int. J. Wildl. Fire 15, 319–345.
https://doi.org/10.1071/WF05097.

Levin, N., Kyba, C.C.M., Zhang, Q., de Miguel, A.S., Rom´an, M.O., Li, X., Portnov, B.A.,
Molthan, A.L., Jechow, A., Miller, S.D., 2020. Remote sensing of night lights: A
review and an outlook for the future. Remote Sens. Environ. 237, 111443.

Levin, Noam, 2017. The impact of seasonal changes on observed nighttime brightness

from 2014 to 2015 monthly VIIRS DNB composites. Remote Sens. Environ. 193,
150–164. https://doi.org/10.1016/j.rse.2017.03.003.

Li, J., Roy, D.P., 2017. A global analysis of Sentinel-2A, Sentinel-2B and Landsat-8 data
revisit intervals and implications for terrestrial monitoring. Remote Sens. 9, 902.
https://doi.org/10.3390/rs9090902.

Li, X., Elvidge, C., Zhou, Y., Cao, C., Warner, T., 2017. Remote sensing of night-time

light. Int. J. Remote Sens. 38, 5855–5859.

Lin, Y., Zhu, Z., Guo, W., Sun, Y., Yang, X., Kovalskyy, V., 2020. Continuous monitoring
of cotton stem water potential using Sentinel-2 imagery. Remote Sens. 12, 1176.
https://doi.org/10.3390/rs12071176.

Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust.

Liu, H., Gong, P., Wang, J., Wang, X., Ning, G., Xu, B., 2021a. Production of global daily

For. 71, 212–215. https://doi.org/10.1080/00049158.2008.10675037.

Justice, C.O., Giglio, L., Korontzi, S., Owens, J., Morisette, J.T., Roy, D., Descloitres, J.,

Alleaume, S., Petitcolin, F., Kaufman, Y., 2002. The MODIS fire products. Remote
Sens. Environ. 83, 244–262. https://doi.org/10.1016/S0034-4257(02)00076-7.

Justice, C.O., Vermote, E., Townshend, J.R.G., Defries, R., Roy, D.P., Hall, D.K.,
Salomonson, V.V., Privette, J.L., Riggs, G., Strahler, A., 1998. The Moderate
Resolution Imaging Spectroradiometer (MODIS): land remote sensing for global
change research. IEEE Trans. Geosci. Remote Sens. 36, 1228–1249.

Kennedy, R.E., Andr´efou¨et, S., Cohen, W.B., G´omez, C., Griffiths, P., Hais, M., Healey, S.
P., Helmer, E.H., Hostert, P., Lyons, M.B., 2014. Bringing an ecological view of
change to Landsat-based remote sensing. Front. Ecol. Environ. 12, 339–346. https://
doi.org/10.1890/130066.

Kennedy, R.E., Cohen, W.B., Schroeder, T.A., 2007. Trajectory-based change detection
for automated characterization of forest disturbance dynamics. Remote Sens.
Environ. 110, 370–386. https://doi.org/10.1016/j.rse.2007.03.010.

Kennedy, R.E., Townsend, P.A., Gross, J.E., Cohen, W.B., Bolstad, P., Wang, Y.Q.,
Adams, P., 2009. Remote sensing change detection tools for natural resource
managers: Understanding concepts and tradeoffs in the design of landscape
monitoring projects. Remote Sens. Environ. 113, 1382–1396. https://doi.org/
10.1016/j.rse.2008.07.018.

Kennedy, R.E., Yang, Z., Braaten, J., Copass, C., Antonova, N., Jordan, C., Nelson, P.,

2015. Attribution of disturbance change agent from Landsat time-series in support of
habitat monitoring in the Puget Sound region, USA. Remote Sens. Environ. 166,
271–285. https://doi.org/10.1016/j.rse.2015.05.005.

Kennedy, R.E., Yang, Z., Cohen, W.B., 2010. Detecting trends in forest disturbance and
recovery using yearly Landsat time series: 1. LandTrendr—Temporal segmentation
algorithms. Remote Sens. Environ. 114, 2897–2910. https://doi.org/10.1016/j.
rse.2010.07.008.

Key, T., Warner, T.A., McGraw, J.B., Fajvan, M.A., 2001. A comparison of multispectral
and multitemporal information in high spatial resolution imagery for classification
of individual tree species in a temperate hardwood forest. Remote Sens. Environ. 75,
100–112.

Kirschbaum, D.B., Adler, R., Hong, Y., Hill, S., Lerner-Lam, A., 2010. A global landslide
catalog for hazard applications: method, results, and limitations. Nat. Hazards 52,
561–575. https://doi.org/10.1007/s11069-009-9401-4.

Knoflach, B., Ramskogler, K., Talluto, M., Hofmeister, F., Haas, F., Heckmann, T.,

Pfeiffer, M., Piermattei, L., Ressl, C., Wimmer, M.H., 2021. Modelling of vegetation
dynamics from satellite time series to determine proglacial primary succession in the
course of global warming—a case study in the Upper Martell Valley (Eastern Italian
Alps). Remote Sens. 13, 4450.

Kussul, N., Lavreniuk, M., Skakun, S., Shelestov, A., 2017. Deep Learning Classification
of Land Cover and Crop Types Using Remote Sensing Data. IEEE Geosci. Remote
Sens. Lett. 14, 778–782. https://doi.org/10.1109/LGRS.2017.2681128.

Laflower, D.M., Hurteau, M.D., Koch, G.W., North, M.P., Hungate, B.A., 2016. Climate-
driven changes in forest succession and the influence of management on forest
carbon dynamics in the Puget Lowlands of Washington StateUSA. For. Ecol. Manage.
362, 194–204. https://doi.org/10.1016/j.foreco.2015.12.015.

Lambin, E.F., 2004. Linking socioeconomic and remote sensing data at the community or
at the household level. In: People and the Environment. Springer, pp. 223–240.
Lambin, E.F., Strahler, A.H., 1994. Change-vector analysis in multitemporal space: A tool
to detect and categorize land-cover change processes using high temporal-resolution
satellite data. Remote Sens. Environ. 48, 231–244. https://doi.org/10.1016/0034-
4257(94)90144-9.

Lambin, E.F., Turner, B.L., Geist, H.J., Agbola, S.B., Angelsen, A., Bruce, J.W.,

Coomes, O.T., Dirzo, R., Fischer, G., Folke, C., 2001. The causes of land-use and land-
cover change: Moving beyond the myths. Glob. Environ. Chang. 11, 261–269.
https://doi.org/10.1016/S0959-3780(01)00007-3.

Latifovic, R., Homer, C., Ressl, R., Pouliot, D., Hossain, S.N., Colditz, R.R., Olthof, I.,
Giri, C.P., Victoria, A., 2016. North American land-change monitoring system.
Remote Sens. 303. L. use L. Cover.

Latifovic, R., Pouliot, D., 2005. Multitemporal land cover mapping for Canada:

methodology and products. Can. J. Remote. Sens. 31, 347–363.

Lawrence, R., 2005. Remote sensing of vegetation responses during the first 20 years
following the 1980 eruption of Mount St. Helens: a spatially and temporally
stratified analysis. In: Ecological Responses to the 1980 Eruption of Mount St.
Helens. Springer, New York, NY, pp. 111–123. https://doi.org/10.1007/0-387-
28150-9_8.

Lentile, L.B., Holden, Z.A., Smith, A.M.S., Falkowski, M.J., Hudak, A.T., Morgan, P.,

Lewis, S.A., Gessler, P.E., Benson, N.C., 2006. Remote sensing techniques to assess

seamless data cubes and quantification of global land cover change from 1985 to
2020 - iMap World 1.0. Remote Sens. Environ. 258, 112364. https://doi.org/
10.1016/j.rse.2021.112364.

Liu, X., Huang, Y., Xu, X., Li, Xuecao, Li, Xia, Ciais, P., Lin, P., Gong, K., Ziegler, A.D.,
Chen, A., Gong, P., Chen, J., Hu, G., Chen, Y., Wang, S., Wu, Q., Huang, K., Estes, L.,
Zeng, Z., 2020a. High-spatiotemporal-resolution mapping of global urban change
from 1985 to 2015. Nat. Sustain. 3, 564–570. https://doi.org/10.1038/s41893-020-
0521-x.

Liu, Y., Wang, Z., Sun, Q., Erb, A.M., Li, Z., Schaaf, C.B., Zhang, X., Rom´an, M.O.,
Scott, R.L., Zhang, Q., Novick, K.A., Syndonia Bret-Harte, M., Petroy, S.,
SanClements, M., 2017. Evaluation of the VIIRS BRDF, Albedo and NBAR products
suite and an assessment of continuity with the long term MODIS record. Remote
Sens. Environ. 201, 256–274. https://doi.org/10.1016/j.rse.2017.09.020.

Liu, Y., Xu, B., Zhi, W., Hu, C., Dong, Y., Jin, S., Lu, Y., Chen, T., Xu, W., Liu, Yongchao,
Zhao, B., Lu, W., 2020b. Space eye on flying aircraft: From Sentinel-2 MSI parallax to
hybrid computing. Remote Sens. Environ. 246, 111867 https://doi.org/10.1016/j.
rse.2020.111867.

Liu, J., Yang, Z., Liu, Y., Mu, C., 2021b. Hyperspectral remote sensing images deep
feature extraction based on mixed feature and convolutional neural networks.
Remote Sens. 13 https://doi.org/10.3390/rs13132599.

Loveland, T.R., Sohl, T.L., Stehman, S.V., Gallant, A.L., Sayler, K.L., Napton, D.E., 2002.
A strategy for estimating the rates of recent United States land-cover changes.
Photogramm. Eng. Remote Sens. 68, 1091–1099.

Lu, D., Mausel, P., Brondizio, E., Moran, E., 2004. Change detection techniques. Int. J.

Remote Sens. 25, 2365–2401.

Martin, L., Howarth, P.J., 1989. Change-detection accuracy assessment using SPOT

multispectral imagery of the rural-urban fringe. Remote Sens. Environ. 30, 55–66.
https://doi.org/10.1016/0034-4257(89)90047-3.

Mascorro, V.S., Coops, N.C., Kurz, W.A., Olguín, M., 2015. Choice of satellite imagery

and attribution of changes to disturbance type strongly affects forest carbon balance
estimates. Carbon Balance Manag. 10, 1–15.

Masek, J.G., Huang, C., Wolfe, R., Cohen, W., Hall, F., Kutler, J., Nelson, P., 2008. North
American forest disturbance mapped from a decadal Landsat record. Remote Sens.
Environ. 112, 2914–2926. https://doi.org/10.1016/j.rse.2008.02.010.

Masek, J.G., Vermote, E.F., Saleous, N.E., Wolfe, R., Hall, F.G., Huemmrich, K.F., Gao, F.,
Kutler, J., Lim, T.-K., 2006. A Landsat surface reflectance dataset for North America,
1990–2000. IEEE Geosci. Remote Sens. Lett. 3, 68–72. https://doi.org/10.1109/
LGRS.2005.857030.

Masek, J.G., Wulder, M.A., Markham, B., McCorkel, J., Crawford, C.J., Storey, J.,

Jenstrom, D.T., 2020. Landsat 9: Empowering open science and applications through
continuity. Remote Sens. Environ. 248, 111968 https://doi.org/10.1016/j.
rse.2020.111968.

Meng, R., Dennison, P.E., Zhao, F., Shendryk, I., Rickert, A., Hanavan, R.P., Cook, B.D.,
Serbin, S.P., 2018. Mapping canopy defoliation by herbivorous insects at the
individual tree level using bi-temporal airborne imaging spectroscopy and LiDAR
measurements. Remote Sens. Environ. 215, 170–183.

Mildrexler, D.J., Zhao, M., Running, S.W., 2009. Testing a MODIS global disturbance
index across North America. Remote Sens. Environ. 113, 2103–2117. https://doi.
org/10.1016/j.rse.2009.05.016.

Minale, A.S., 2013. Retrospective analysis of land cover and use dynamics in Gilgel
Abbay Watershed by using GIS and remote sensing techniquesNorthwestern
Ethiopia. Int. J. Geosci. 4, 1003.

Molinier, M., Miettinen, J., Ienco, D., Qiu, S., Zhu, Z., 2021. Optical satellite image time
series analysis for environment applications: from classical methods to deep learning
and beyond. In: Change Detection and Image Time Series Analysis 2: Supervised
Methods. Wiley Online Library, pp. 109–154.

Myneni, R.B., Keeling, C.D., Tucker, C.J., Asrar, G., Nemani, R.R., 1997. Increased plant
growth in the northern high latitudes from 1981 to 1991. Nature 386, 698–702.
https://doi.org/10.1038/386698a0.

Noaa, 2022. Severe Weather Data Inventory [WWW Document]. NOAA (accessed
1.4.22). https://www.ncei.noaa.gov/products/severe-weather-data-inventory.

Nrc, 2013. Advancing Land Change Modeling: Opportunities and Research

Requirements. National Academies Press.

Nrc, 1999. Human Dimensions of Global Environmental Change: Research Pathways for

the Next Decade. National Academies Press.

Nrc, 1998. <book-title>People and Pixels: Linking Remote Sensing and Social </book-

title>Science. National Academies Press.

RemoteSensingofEnvironment282(2022)11326617Z. Zhu et al.

Oeser, J., Pflugmacher, D., Senf, C., Heurich, M., Hostert, P., 2017. Using intra-annual
Landsat time series for attributing forest disturbance agents in Central Europe.
Forests 8, 251. https://doi.org/10.3390/f8070251.

Oliver, C.D., Larson, B.C., 1996. Forest Stand Dynamics, Updated edition. John Wiley

and sons.

Olofsson, P., Foody, G.M., Stehman, S.V., Woodcock, C.E., 2013. Making better use of

accuracy data in land change studies: Estimating accuracy and area and quantifying
uncertainty using stratified estimation. Remote Sens. Environ. 129, 122–131.
https://doi.org/10.1016/j.rse.2012.10.031.

Ortiz, S.M., Breidenbach, J., K¨andler, G., 2013. Early detection of bark beetle green
attack using TerraSAR-X and RapidEye data. Remote Sens. 5, 1912–1931.
Osi´nska-Skotak, K., Radecka, A., Pi´orkowski, H., Michalska-Hejduk, D., Kope´c, D.,
Tokarska-Guzik, B., Ostrowski, W., Kania, A., Niedzielko, J., 2019. Mapping
succession in non-forest habitats by means of remote sensing: Is the data acquisition
time critical for species discrimination? Remote Sens. 11, 2629.

Pasquarella, V.J., Holden, C.E., Woodcock, C.E., 2018. Improved mapping of forest type
using spectral-temporal Landsat features. Remote Sens. Environ. 210, 193–207.
https://doi.org/10.1016/j.rse.2018.02.064.

Pekel, J.-F., Cottam, A., Gorelick, N., Belward, A.S., 2016. High-resolution mapping of
global surface water and its long-term changes. Nature 540, 418–422. https://doi.
org/10.1038/nature20584.

Pengra, B.W., Stehman, S.V., Horton, J.A., Dockter, D.J., Schroeder, T.A., Yang, Z.,

Cohen, W.B., Healey, S.P., Loveland, T.R., 2020. Quality control and assessment of
interpreter consistency of annual land cover reference data in an operational
national monitoring program. Remote Sens. Environ. 238, 111261 https://doi.org/
10.1016/j.rse.2019.111261.

P´erez-Cabello, F., Montorio, R., Alves, D.B., 2021. Remote sensing techniques to assess

post-fire vegetation recovery. Curr. Opin. Environ. Sci. Heal. 21, 100251.

Pesaresi, M., Ehrlich, D., Ferri, S., Florczyk, A., Freire, S., Halkia, M., Julea, A.,

Kemper, T., Soille, P., Syrris, V., 2016. Operating Procedure for the Production of the
Global Human Settlement Layer from Landsat Data of the Epochs 1975, 1990, 2000,
and 2014. Publications Office of the European Union, Luxembourg (Luxembourg).
https://doi.org/10.2788/656115.

Peters, D.P.C., Lugo, A.E., Chapin III, F.S., Pickett, S.T.A., Duniway, M., Rocha, A.V.,
Swanson, F.J., Laney, C., Jones, J., 2011. Cross-system comparisons elucidate
disturbance complexities and generalities. Ecosphere 2, 1–26. https://doi.org/
10.1890/ES11-00115.1.

Petit, C., Scudder, T., Lambin, E., 2001. Quantifying processes of land-cover change by
remote sensing: resettlement and rapid land-cover changes in south-eastern Zambia.
Int. J. Remote Sens. 22, 3435–3456. https://doi.org/10.1080/01431160010006881.

Potapov, P., Hansen, M.C., Pickens, A., Hernandez-Serna, A., Tyukavina, A.,

Turubanova, S., Zalles, V., Li, X., Khan, A., Stolle, F., Harris, N., Song, X.-P.,
Baggett, A., Kommareddy, I., Kommareddy, A., 2022. The Global 2000–2020 Land
Cover and Land Use Change Dataset Derived From the Landsat Archive: First Results.
Front. Remote Sens. 3 https://doi.org/10.3389/frsen.2022.856903.

Potter, C., Tan, P., Steinbach, M., Klooster, S., Kumar, V., Myneni, R., Genovese, V.,

2003. Major disturbance events in terrestrial ecosystems detected using global
satellite data sets. Glob. Chang. Biol. 9, 1005–1021. https://doi.org/10.1046/j.1365-
2486.2003.00648.x.

Pouliot, D., Alavi, N., Wilson, S., Duffe, J., Pasher, J., Davidson, A., Daneshfar, B.,

Lindsay, E., 2021. Assessment of Landsat Based Deep-Learning Membership Analysis
for Development of from–to Change Time Series in the Prairie Region of Canada
from 1984 to 2018. Remote Sens. 13, 634.

Pouliot, D., Latifovic, R., 2016. Land change attribution based on Landsat time series and
integration of ancillary disturbance data in the Athabasca oil sands region of Canada.
GIScience Remote Sens. 53, 382–401.

Pouliot, D., Latifovic, R., Olthof, I., 2009. Trends in vegetation NDVI from 1 km AVHRR
data over Canada for the period 1985–2006. Int. J. Remote Sens. 30, 149–168.
Pouliot, D., Latifovic, R., Zabcic, N., Guindon, L., Olthof, I., 2014. Development and

assessment of a 250 m spatial resolution MODIS annual land cover time series
(2000–2011) for the forest region of Canada derived from change-based updating.
Remote Sens. Environ. 140, 731–743.

Pricope, N.G., Mapes, K.L., Woodward, K.D., 2019. Remote sensing of

human–environment interactions in global change research: a review of advances,
challenges and future directions. Remote Sens. https://doi.org/10.3390/
rs11232783.

Qin, Y., Xiao, X., Wigneron, J.-P., Ciais, P., Brandt, M., Fan, L., Li, X., Crowell, S., Wu, X.,

Doughty, R., 2021. Carbon loss from forest degradation exceeds that from
deforestation in the Brazilian Amazon. Nat. Clim. Chang. 11, 442–448. https://doi.
org/10.1038/s41558-021-01026-5.

Qiu, S., Lin, Y., Shang, R., Zhang, J., Ma, L., Zhu, Z., Qiu, S., Lin, Y., Shang, R., Zhang, J.,
Ma, L., Zhu, Z., 2019a. Making landsat time series consistent: evaluating and
improving landsat analysis ready data. Remote Sens. 11 https://doi.org/10.3390/
RS11010051.

Qiu, S., Zhu, Z., He, B., 2019b. Fmask 4.0: Improved cloud and cloud shadow detection in
Landsats 4–8 and Sentinel-2 imagery. Remote Sens. Environ. 231, 111205 https://
doi.org/10.1016/j.rse.2019.05.024.

Raitsos, D.E., Pradhan, Y., Brewin, R.J.W., Stenchikov, G., Hoteit, I., 2013. Remote

sensing the phytoplankton seasonal succession of the Red Sea. PLoS One 8, e64909.

and Analysis (FIA) data. Remote Sens. Environ. 114, 2337–2352. https://doi.org/
10.1016/j.rse.2010.05.010.

Rigge, M., Shi, H., Homer, C., Danielson, P., Granneman, B., 2019. Long-term trajectories

of fractional component change in the Northern Great Basin, USA. Ecosphere 10,
e02762.

Rindfuss, R.R., Walsh, S.J., Turner, B.L., Fox, J., Mishra, V., 2004. Developing a science
of land change: challenges and methodological issues. Proc. Natl. Acad. Sci. 101,
13976–13981. https://doi.org/10.1073/pnas.0401545101.

Rindfuss, R.R., Walsh, S.J., Turner, B.L., Moran, E.F., Entwisle, B., 2012. Linking Pixels
and People. In: Gutman, G., Janetos, A.C., Justice, C.O., Moran, E.F., Mustard, J.F.,
Rindfuss, R.R., Skole, D., Turner, Billy Lee, Cochrane, M.A. (Eds.), Land Change
Science: Observing. Monitoring and Understanding Trajectories of Change on the
Earth’s Surface. Springer, Netherlands, Dordrecht, pp. 379–394. https://doi.org/
10.1007/978-1-4020-2562-4_22.

Rittenhouse, C.D., Berlin, E.H., Mikle, N., Qiu, S., Riordan, D., Zhu, Z., 2022. An Object-
Based Approach to Map Young Forest and Shrubland Vegetation Based on Multi-
Source Remote Sensing Data. Remote Sens. 14, 1091.

Rogan, J., Franklin, J., Stow, D., Miller, J., Woodcock, C., Roberts, D., 2008. Mapping
land-cover modifications over large areas: A comparison of machine learning
algorithms. Remote Sens. Environ. 112, 2272–2283.

Rollins, M.G., 2009. LANDFIRE: A nationally consistent vegetation, wildland fire, and

fuel assessment. Int. J. Wildl. Fire 18, 235–249. https://doi.org/10.1071/WF08088.
Rom´an, M.O., Wang, Z., Sun, Q., Kalb, V., Miller, S.D., Molthan, A., Schultz, L., Bell, J.,
Stokes, E.C., Pandey, B., 2018. NASA’s Black Marble nighttime lights product suite.
Remote Sens. Environ. 210, 113–143. https://doi.org/10.1016/j.rse.2018.03.017.
Rosser, J.F., Leibovici, D.G., Jackson, M.J., 2017. Rapid flood inundation mapping using
social media, remote sensing and topographic data. Nat. Hazards 87, 103–120.
Roy, D.P., Huang, H., Houborg, R., Martins, V.S., 2021. A global analysis of the temporal

availability of PlanetScope high spatial resolution multi-spectral imagery. Remote
Sens. Environ. 264, 112586 https://doi.org/10.1016/j.rse.2021.112586.

Roy, D.P., Wulder, M.A., Loveland, T.R., Ce, W., Allen, R.G., Anderson, M.C., Helder, D.,

Irons, J.R., Johnson, D.M., Kennedy, R., Scambos, T.A., Schaaf, C.B., Schott, J.R.,
Sheng, Y., Vermote, E.F., Belward, A.S., Bindschadler, R., Cohen, W.B., Gao, F.,
Hipple, J.D., Hostert, P., Huntington, J., Justice, C.O., Kilic, A., Kovalskyy, V., Lee, Z.
P., Lymburner, L., Masek, J.G., McCorkel, J., Shuai, Y., Trezza, R., Vogelmann, J.,
Wynne, R.H., Zhu, Z., 2014. Landsat-8: Science and product vision for terrestrial
global change research. Remote Sens. Environ. 145, 154–172. https://doi.org/
10.1016/j.rse.2014.02.001.

Roy, D.P., Zhang, H.K., Ju, J., Gomez-Dans, J.L., Lewis, P.E., Schaaf, C.B., Sun, Q., Li, J.,
Huang, H., Kovalskyy, V., 2016. A general method to normalize Landsat reflectance
data to nadir BRDF adjusted reflectance. Remote Sens. Environ. 176, 255–271.
https://doi.org/10.1016/j.rse.2016.01.023.

Saleska, S.R., Didan, K., Huete, A.R., Da Rocha, H.R., 2007. Amazon forests green-up

during 2005 drought. Science 318, 612. https://doi.org/10.1126/science.1146663.

Samanta, A., Ganguly, S., Hashimoto, H., Devadiga, S., Vermote, E., Knyazikhin, Y.,

Nemani, R.R., Myneni, R.B., 2010. Amazon forests did not green-up during the 2005
drought. Geophys. Res. Lett. 37 https://doi.org/10.1029/2009GL042154.
Schaaf, C.B., Gao, F., Strahler, A.H., Lucht, W., Li, X., Tsang, T., Strugnell, N.C.,

Zhang, X., Jin, Y., Muller, J.-P.P., Lewis, P., Barnsley, M., Hobson, P., Disney, M.,
Roberts, G., Dunderdale, M., Doll, C., D’Entremont, R.P., Hu, B., Liang, S.,
Privette, J.L., Roy, D., 2002. First operational BRDF, albedo nadir reflectance
products from MODIS. Remote Sens. Environ. 83, 135–148. https://doi.org/
10.1016/S0034-4257(02)00091-3.

Schmitt, M., Zhu, X.X., 2016. Data fusion and remote sensing: An ever-growing

relationship. IEEE Geosci. Remote Sens. Mag. 4, 6–23.

Schnebele, E., Cervone, G., Kumar, S., Waters, N., 2014. Real time estimation of the

Calgary floods using limited remote sensing data. Water 6, 381–398.

Schroeder, T.A., Schleeweis, K.G., Moisen, G.G., Toney, C., Cohen, W.B., Freeman, E.A.,

Yang, Z., Huang, C., 2017. Testing a Landsat-based approach for mapping
disturbance causality in US forests. Remote Sens. Environ. 195, 230–243. https://
doi.org/10.1016/j.rse.2017.03.033.

Sebald, J., Senf, C., Seidl, R., 2021. Human or natural? Landscape context improves the
attribution of forest disturbances mapped from Landsat in Central Europe. Remote
Sens. Environ. 262, 112502 https://doi.org/10.1016/j.rse.2021.112502.

Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Nat. Clim. Chang. 7, 395–402. https://doi.org/10.1038/nclimate3303.
Sellers, P.J., Meeson, B.W., Hall, F.G., Asrar, G., Murphy, R.E., Schiffer, R.A.,

Bretherton, F.P., Dickinson, R.E., Ellingson, R.G., Field, C.B., 1995. Remote sensing
of the land surface for studies of global change: Models—algorithms—experiments.
Remote Sens. Environ. 51, 3–26. https://doi.org/10.1016/0034-4257(94)00061-Q.

Senf, C., Pflugmacher, D., Wulder, M.A., Hostert, P., 2015. Characterizing

spectral–temporal patterns of defoliator and bark beetle disturbances using Landsat
time series. Remote Sens. Environ. 170, 166–177.

Senf, C., Seidl, R., 2022. Post-disturbance canopy recovery and the resilience of Europe’s

forests. Glob. Ecol. Biogeogr. 31, 25–36.

Senf, C., Seidl, R., Hostert, P., 2017. Remote sensing of forest insect disturbances: Current
state and future directions. Int. J. Appl. Earth Obs. Geoinf. 60, 49–60. https://doi.
org/10.1016/j.jag.2017.04.004.

Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving

Sesnie, S.E., Tellman, B., Wrathall, D., McSweeney, K., Nielsen, E., Benessaiah, K.,

near-real time deforestation monitoring in tropical dry forests by combining dense
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
204, 147–161. https://doi.org/10.1016/j.rse.2017.10.034.

Riemann, R., Wilson, B.T., Lister, A., Parks, S., 2010. An effective assessment protocol for
continuous geospatial datasets of forest characteristics using USFS Forest Inventory

Wang, O., Rey, L., 2017. A spatio-temporal analysis of forest loss related to cocaine
trafficking in Central America. Environ. Res. Lett. 12, 54015.

Seto, K.C., Kaufmann, R.K., 2003. Modeling the drivers of urban land use change in the
Pearl River Delta, China: Integrating remote sensing with socioeconomic data. Land
Econ. 79, 106–121.

RemoteSensingofEnvironment282(2022)11326618Z. Zhu et al.

Seto, K.C., Reenberg, A., Boone, C.G., Fragkias, M., Haase, D., Langanke, T.,

Wang, Z., Rom´an, M.O., Kalb, V.L., Miller, S.D., Zhang, J., Shrestha, R.M., 2021.

Marcotullio, P., Munroe, D.K., Olah, B., Simon, D., 2012. Urban land teleconnections
and sustainability. Proc. Natl. Acad. Sci. 109, 7687–7692. https://doi.org/10.1073/
pnas.1117622109.

Quantifying uncertainties in nighttime light retrievals from Suomi-NPP and NOAA-
20 VIIRS Day/Night Band data. Remote Sens. Environ. 263, 112557 https://doi.org/
10.1016/j.rse.2021.112557.

Shang, R., Zhu, Z., 2019. Harmonizing Landsat 8 and Sentinel-2: A time-series-based

Warner, T., Almutairi, A., Lee, J.Y., 2009. Remote Sensing of Land Cover Change. SAGE,

reflectance adjustment approach. Remote Sens. Environ. 235, 111439 https://doi.
org/10.1016/j.rse.2019.111439.

Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time

monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data.
Remote Sens. Environ. 278, 113073 https://doi.org/10.1016/j.rse.2022.113073.

Shimizu, K., Ota, T., Mizoue, N., Yoshida, S., 2019. A comprehensive evaluation of

disturbance agent classification approaches: Strengths of ensemble classification,
multiple indices, spatio-temporal variables, and direct prediction. ISPRS J.
Photogramm. Remote Sens. 158, 99–112. https://doi.org/10.1016/j.
isprsjprs.2019.10.004.

Singh, A., 1989. Digital change detection techniques using remotely-sensed data. Int. J.
Remote Sens. 10, 989–1003. https://doi.org/10.1080/01431168908903939.
Sohl, T.L., Gallant, A.L., Loveland, T.R., 2004. The characteristics and interpretability of
land surface change and implications for project design. Photogramm. Eng. Remote
Sensing 70, 439–448. https://doi.org/10.14358/PERS.70.4.439.

Song, C., Woodcock, C.E., Seto, K.C., Lenney, M.P., Macomber, S.A., 2001. Classification
and change detection using Landsat TM data: when and how to correct atmospheric
effects? Remote SensEnvironment 75, 230–244. https://doi.org/10.1016/S0034-
4257(00)00169-3.

Song, X.P., Hansen, M.C., Stehman, S.V., Potapov, P.V., Tyukavina, A., Vermote, E.F.,
Townshend, J.R., 2018. Global land change from 1982 to 2016. Nature 560,
639–643. https://doi.org/10.1038/s41586-018-0411-9.

Sousa, W.P., 1984. The role of disturbance in natural communities. Annu. Rev. Ecol. Syst.

15, 353–391.

London, UK.

White, J.C., Hermosilla, T., Wulder, M.A., Coops, N.C., 2022. Mapping, validating, and
interpreting spatio-temporal trends in post-disturbance forest recovery. Remote
Sens. Environ. 271, 112904.

White, J.C., Saarinen, N., Kankare, V., Wulder, M.A., Hermosilla, T., Coops, N.C.,

Pickell, P.D., Holopainen, M., Hyypp¨a, J., Vastaranta, M., 2018. Confirmation of
post-harvest spectral recovery from Landsat time series using measures of forest
cover and height derived from airborne laser scanning data. Remote Sens. Environ.
216, 262–275.

White, J.C., Saarinen, N., Wulder, M.A., Kankare, V., Hermosilla, T., Coops, N.C.,

Holopainen, M., Hyypp¨a, J., Vastaranta, M., 2019. Assessing spectral measures of
post-harvest forest recovery with field plot data. Int. J. Appl. Earth Obs. Geoinf. 80,
102–114.

White, J.C., Wulder, M.A., Hermosilla, T., Coops, N.C., Hobart, G.W., 2017. A nationwide
annual characterization of 25 years of forest disturbance and recovery for Canada
using Landsat time series. Remote Sens. Environ. 194, 303–321.

White, P.S., Pickett, S.T.A., 1985. Natural disturbance and patch dynamics: an
introduction. In: Pickett, S.T.A., White, P.S. (Eds.), The Ecology of Natural
Disturbance and Patch Dynamics. Academic Press, San Diego, pp. 3–13.

Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,

Gao, F., Goward, S.N., Helder, D., Helmer, E., Nemani, R., Oreopoulos, L., Schott, J.,
Thenkabail, P.S., Vermote, E.F., Vogelmann, J., Wulder, M.A., Wynne, R., 2008. Free
access to Landsat imagery. Science 320, 1011. https://doi.org/10.1126/
science.320.5879.1011a.

Strahler, A.H., Woodcock, C.E., Smith, J.A., 1986. On the nature of models in remote

Woodcock, C.E., Loveland, T.R., Herold, M., Bauer, M.E., 2020. Transitioning from

sensing. Remote Sens. Environ. 20, 121–139.

Sulla-Menashe, D., Woodcock, C.E., Friedl, M.A., 2018. Canadian boreal forest greening
and browning trends: an analysis of biogeographic patterns and the relative roles of
disturbance versus climate drivers. Environ. Res. Lett. 13, 14007.

Szostak, M., Hawryło, P., Piela, D., 2018. Using of Sentinel-2 images for automation of
the forest succession detection. Eur. J. Remote Sens. 51, 142–149. https://doi.org/
10.1080/22797254.2017.1412272.

Tan, B., Masek, J.G., Wolfe, R., Gao, F., Huang, C., Vermote, E.F., Sexton, J.O.,

Ederer, G., 2013. Improved forest change detection with terrain illumination
corrected Landsat images. Remote Sens. Environ. 136, 469–483. https://doi.org/
10.1016/j.rse.2013.05.013.

Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
monitoring of tropical forest disturbance: New algorithms and assessment
framework. Remote Sens. Environ. 224, 202–218. https://doi.org/10.1016/j.
rse.2019.02.003.

Tang, X., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2020. Can VIIRS continue the

legacy of MODIS for near real-time monitoring of tropical forest disturbance?
Remote Sens. Environ. 249, 112024.

Tellman, B., Sesnie, S.E., Magliocca, N.R., Nielsen, E.A., Devine, J.A., McSweeney, K.,
Jain, M., Wrathall, D.J., D´avila, A., Benessaiah, K., 2020. Illicit drivers of land use
change: Narcotrafficking and forest loss in Central America. Glob. Environ. Chang.
63, 102092.

Tollerud, H.J., Brown, J.F., Loveland, T.R., 2020. Investigating the effects of land use and
land cover on the relationship between moisture and reflectance using Landsat time
series. Remote Sens. 12, 1919. https://doi.org/10.3390/rs12121919.

Turner, B.L., 1997. The sustainability principle in global agendas: implications for

understanding land-use/cover change. Geogr. J. 163, 133–140.

Turner, B.L., Lambin, E.F., Verburg, P.H., 2021. From land-use/land-cover to land system
science. Ambio 50, 1291–1294. https://doi.org/10.1007/s13280-021-01510-4.
Turner, B.L., Lambin, E.F., Reenberg, A., 2007. The emergence of land change science for

global environmental change and sustainability. Proc. Natl. Acad. Sci. 104,
20666–20671. https://doi.org/10.1073/pnas.0704119104.

Turner, M.G., 2010. Disturbance and landscape dynamics in a changing world. Ecology

91, 2833–2849. https://doi.org/10.1890/10-0097.1.

Ustin, S.L., Middleton, E.M., 2021. Current and near-term advances in Earth observation
for ecological applications. Ecol. Process. 10, 1–57. https://doi.org/10.1186/
s13717-020-00255-4.

Verbesselt, J., Hyndman, R., Newnham, G., Culvenor, D., 2010. Detecting trend and

seasonal changes in satellite image time series. Remote Sens. Environ. 114, 106–115.
https://doi.org/10.1016/j.rse.2009.08.014.

Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using
satellite image time series. Remote Sens. Environ. 123, 98–108. https://doi.org/
10.1016/j.rse.2012.02.022.

Verrelst, J., Camps-Valls, G., Mu˜noz-Marí, J., Rivera, J.P., Veroustraete, F., Clevers, J.G.
P.W., Moreno, J., 2015. Optical remote sensing and the retrieval of terrestrial
vegetation bio-geophysical properties–A review. ISPRS J. Photogramm. Remote
Sens. 108, 273–290. https://doi.org/10.1016/j.isprsjprs.2015.05.005.

Verstraete, M.M., Pinty, B., 1996. Designing optimal spectral indexes for remote sensing

applications. IEEE Trans. Geosci. Remote Sens. 34, 1254–1265.

Vogelmann, J.E., Gallant, A.L., Shi, H., Zhu, Z., 2016. Perspectives on monitoring gradual
change across the continuity of Landsat sensors using time-series data. Remote Sens.
Environ. 185, 258–270.

Vogelmann, J.E., Xian, G., Homer, C., Tolk, B., 2012. Monitoring gradual ecosystem
change using Landsat time series analyses: Case studies in selected forest and
rangeland ecosystems. Remote Sens. Environ. 122, 92–105. https://doi.org/
10.1016/j.rse.2011.06.027.

change detection to monitoring with remote sensing: A paradigm shift. Remote Sens.
Environ. 238, 111558 https://doi.org/10.1016/j.rse.2019.111558.

Wulder, M.A., Coops, N.C., Roy, D.P., White, J.C., Hermosilla, T., 2018. Land cover 2.0.

Int. J. Remote Sens. 39, 4254–4284. https://doi.org/10.1080/
01431161.2018.1452075.

Wulder, M.A., Masek, J.G., Cohen, W.B., Loveland, T.R., Woodcock, C.E., 2012. Opening
the archive: How free data has enabled the science and monitoring promise of
Landsat. Remote Sens. Environ. 122, 2–10. https://doi.org/10.1016/j.
rse.2012.01.010.

Wulder, M.A., Roy, D.P., Radeloff, V.C., Loveland, T.R., Anderson, M.C., Johnson, D.M.,

Healey, S., Zhu, Z., Scambos, T.A., Pahlevan, N., Hansen, M., 2022. Fifty years of
Landsat science and impacts. Remote Sens. Environ. 280, 113195 https://doi.org/
10.1016/j.rse.2022.113195.

Wyman, M.S., Stein, T.V., 2010. Modeling social and land-use/land-cover change data to
assess drivers of smallholder deforestation in Belize. Appl. Geogr. 30, 329–342.
Xian, G., Homer, C., Fry, J., 2009. Updating the 2001 National Land Cover Database land

cover classification to 2006 by using Landsat imagery change detection methods.
Remote Sens. Environ. 113, 1133–1147.

Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
LCMAP Collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
143–162.

Xie, Q., Dash, J., Huang, W., Peng, D., Qin, Q., Mortimer, H., Casa, R., Pignatti, S.,

Laneve, G., Pascucci, S., 2018. Vegetation indices combining the red and red-edge
spectral information for leaf area index retrieval. IEEE J. Sel. Top. Appl. earth Obs.
Remote Sens. 11, 1482–1493.

Xin, Q.C., Olofsson, P., Zhu, Z., Tan, B., Woodcock, C.E., 2013. Toward near real-time
monitoring of forest disturbance by fusion of MODIS and Landsat data. Remote Sens.
Environ. 135, 234–247. https://doi.org/10.1016/J.Rse.2013.04.002.

Yan, L., Roy, D.P., Zhang, H., Li, J., Huang, H., 2016. An automated approach for sub-
pixel registration of Landsat-8 Operational Land Imager (OLI) and Sentinel-2 Multi
Spectral Instrument (MSI) imagery. Remote Sens. 8, 520. https://doi.org/10.3390/
rs8060520.

Yang, X., Zhu, Zhe, Qiu, S., Kroeger, K.D., Zhu, Zhiliang, Covington, S., 2022. Detection

and characterization of coastal tidal wetland change in the northeastern US using
Landsat time series. Remote Sens. Environ. 276, 113047 https://doi.org/10.1016/j.
rse.2022.113047.

Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
forest disturbance using Landsat time series: Stochastic continuous change detection.
Remote Sens. Environ. 252, 112167 https://doi.org/10.1016/j.rse.2020.112167.
Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
dense Landsat time series: Case studies of mountain pine beetle and spruce beetle
disturbance. Remote Sens. Environ. 263, 112560 https://doi.org/10.1016/j.
rse.2021.112560.

Zhang, X., Friedl, M.A., Schaaf, C.B., 2009. Sensitivity of vegetation phenology detection
to the temporal resolution of satellite data. Int. J. Remote Sens. 30, 2061–2074.
Zhang, X., Friedl, M.A., Schaaf, C.B., Strahler, A.H., Hodges, J.C.F., Gao, F., Reed, B.C.,
Huete, A., 2003. Monitoring vegetation phenology using MODIS. Remote Sens.
Environ. 84, 471–475.

Zhang, X., Liu, L., Liu, Y., Jayavelu, S., Wang, J., Moon, M., Henebry, G.M., Friedl, M.A.,
Schaaf, C.B., 2018. Generation and evaluation of the VIIRS land surface phenology
product. Remote Sens. Environ. 216, 212–229.

Zhang, X., Wang, J., Henebry, G.M., Gao, F., 2020. Development and evaluation of a new
algorithm for detecting 30 m land surface phenology from VIIRS and HLS time series.
ISPRS J. Photogramm. Remote Sens. 161, 37–51.

RemoteSensingofEnvironment282(2022)11326619Z. Zhu et al.

Zhang, Y., Woodcock, C.E., Chen, S., Wang, J.A., Sulla-Menashe, D., Zuo, Z., Olofsson, P.,

Wang, Y., Friedl, M.A., 2022. Mapping causal agents of disturbance in boreal and
arctic ecosystems of North America using time series of Landsat data. Remote Sens.
Environ. 272, 112935 https://doi.org/10.1016/j.rse.2022.112935.

Zhao, F., Huang, C., Goward, S.N., Schleeweis, K., Rishmawi, K., Lindsey, M.A.,

Denning, E., Keddell, L., Cohen, W.B., Yang, Z., Dungan, J.L., Michaelis, A., 2018.
Development of Landsat-based annual US forest disturbance history maps
(1986–2010) in support of the North American Carbon Program (NACP). Remote
Sens. Environ. 209, 312–326. https://doi.org/10.1016/j.rse.2018.02.035.

Zhao, M., Zhou, Y., Li, Xuecao, Cao, W., He, C., Yu, B., Li, Xi, Elvidge, C.D., Cheng, W.,

Zhou, C., 2019. Applications of satellite remote sensing of nighttime light
observations: Advances, challenges, and perspectives. Remote Sens. 11, 1971.

Zhu, Z., 2017. Change detection using landsat time series: A review of frequencies,

preprocessing, algorithms, and applications. ISPRS J. Photogramm. Remote Sens.
130, 370–384. https://doi.org/10.1016/j.isprsjprs.2017.06.013.

Zhu, Z., Fu, Y., Woodcock, C.E., Olofsson, P., Vogelmann, J.E., Holden, C., Wang, M.,
Dai, S., Yu, Y., 2016a. Including land cover change in analysis of greenness trends
using all available Landsat 5, 7, and 8 images: A case study from Guangzhou, China
(2000–2014). Remote Sens. Environ. 185, 243–257. https://doi.org/10.1016/j.
rse.2016.03.036.

Zhu, Z., Piao, S., Myneni, R.B., Huang, M., Zeng, Z., Canadell, J.G., Ciais, P., Sitch, S.,
Friedlingstein, P., Arneth, A., Cao, C., Cheng, L., Kato, E., Koven, C., Li, Y., Lian, X.,
Liu, Y., Liu, R., Mao, J., Pan, Y., Peng, S., Peuelas, J., Poulter, B., Pugh, T.A.M.,
Stocker, B.D., Viovy, N., Wang, X., Wang, Y., Xiao, Z., Yang, H., Zaehle, S., Zeng, N.,

2016b. Greening of the Earth and its drivers. Nat. Clim. Chang. 6, 791–795. https://
doi.org/10.1038/nclimate3004.

Zhu, Z., Qiu, S., He, B., Deng, C., 2018. Cloud and cloud shadow detection for Landsat
images : the fundamental basis for analyzing Landsat time series. Remote Sens. Time
Ser. Image Process. 3–24 https://doi.org/10.1201/9781315166636-10.

Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
cover using all available Landsat data. Remote Sens. Environ. 144, 152–171. https://
doi.org/10.1016/j.rse.2014.01.011.

Zhu, Z., Woodcock, C.E., 2012. Object-based cloud and cloud shadow detection in

Landsat imagery. Remote Sens. Environ. 118, 83–94. https://doi.org/10.1016/j.
rse.2011.10.028.

Zhu, Z., Woodcock, C.E., Olofsson, P., 2012a. Continuous monitoring of forest

disturbance using all available Landsat imagery. Remote Sens. Environ. 122, 75–91.
https://doi.org/10.1016/j.rse.2011.10.030.

Zhu, Z., Woodcock, C.E., Rogan, J., Kellndorfer, J., 2012b. Assessment of spectral,

polarimetric, temporal, and spatial dimensions for urban and peri-urban land cover
classification using Landsat and SAR data. Remote Sens. Environ. 117, 72–82.
https://doi.org/10.1016/j.rse.2011.07.020.

Zhu, Z., Wulder, M.A., Roy, D.P., Woodcock, C.E., Hansen, M.C., Radeloff, V.C.,
Healey, S.P., Schaaf, C., Hostert, P., Strobl, P., Pekel, J.F., Lymburner, L.,
Pahlevan, N., Scambos, T.A., 2019. Benefits of the free and open Landsat data policy.
Remote Sens. Environ. 224, 382–385. https://doi.org/10.1016/j.rse.2019.02.016.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. 238, 111116 https://doi.org/10.1016/j.rse.2019.03.009.

RemoteSensingofEnvironment282(2022)11326620