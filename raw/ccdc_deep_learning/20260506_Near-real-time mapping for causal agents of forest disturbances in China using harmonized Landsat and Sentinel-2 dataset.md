---
title: "Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset"
publication_date: "2026-05-06"
publication_date_precision: "day"
publication_date_basis: "first_online"
journal_issue_year: 2026
doi: "10.1016/j.rse.2026.115461"
source_pdf: "tmp/ccdc/Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset.pdf"
source_pdf_pages: 16
converter: "MarkItDown 0.1.5 [pdf]"
date_reference: "原 PDF 首页 Available online"
---

# Near-real-time mapping for causal agents of forest disturbances in China using harmonized Landsat and Sentinel-2 dataset

Remote Sensing of Environment 342 (2026) 115461

Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

Near-real-time mapping for causal agents of forest disturbances in China
using harmonized Landsat and Sentinel-2 dataset

Ronghua Liao a,b, Chengcheng Guo b, Lingkun Chen a,b, Yulin Jiang a,b, Yuchen Tao a,b,
Jiani Liao a,b, Rui Lu a,b, Huaguo Huang c, Zhou Shi a,b, Su Ye a,b,*
a State Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China
b Zhejiang Key Laboratory of Agricultural Remote Sensing and Information Technology, Zhejiang University, Hangzhou 310058, China
c State Forestry and Grassland Administration Key Laboratory of Forest Resources and Environmental Management, Beijing Forestry University, Beijing 100083, China

A R T I C L E  I N F O

A B S T R A C T

Edited by Marie Weiss

Keywords:
Forest disturbance
Near-real-time
Disturbance agent
Time-series
Latency

Timely  identification  of  forest  disturbance  agents  is  essential  for  effective  ecosystem  management  and  rapid
response to natural and anthropogenic threats. However, most near-real-time (NRT) monitoring systems focus
solely on detecting disturbance locations and timing of generic disturbances, lacking attribution of causal agents
that is critical for operational decision making. This study presents a novel NRT framework to map major forest
disturbance agents—wildfire, logging, and stress—across China using the Harmonized  Landsat and Sentinel-2
(HLS)  dataset.  To  address  the  scarcity  of  local  training  data,  we  introduced  a  transferring-guided  sampling
strategy  that  efficiently  generated  tile-specific  local  samples  by  leveraging  disturbance  archives  from  the
conterminous United States and subsequent expert verification. Stage-based random forest models were subse-
quently  constructed  using  16  temporally  dynamic  features  derived  from  HLS  spectral  trajectories  to  classify
anomalies at varying disturbance stages. The system achieved an overall first-alert lag of 11.6 days and a level-off
lag of 15.5 days, with corresponding overall accuracies of 77.5% and 84.0%. Wildfire disturbances exhibited the
shortest detection lag and the highest accuracy, followed by logging and stress, reflecting differences in spectral
separability among agents. Compared with the global DIST-ALERT product, the proposed framework achieved
higher  accuracy  and  fewer  false  detections,  at  a  trade-off  of  a  3.7-day  longer  first-alert  lag,  while  providing
actionable  information  on  disturbance  causality.  These  results  demonstrate  the  feasibility  of  operationally
mapping disturbance agents in near real-time at a national scale. The proposed framework offers a transferable,
data-efficient solution for rapid forest disturbance attribution and provides a foundation for global-scale NRT
disturbance monitoring initiatives.

1. Introduction

2014).

Driven  by  climate  change  and  anthropogenic  factors,  a  growing
number  of  forest  disturbances  from  wildfires,  logging  and  insect  out-
breaks have emerged globally in recent years (Cohen et al., 2016; Seidl
et  al.,  2014;  Tyukavina  et  al.,  2017).  With  increasing  frequency  and
severity,  the  disturbance  events  disrupt  forest  structure  and  composi-
tion, causing severe ecological and economic consequences (Dee et al.,
2025; Thom and Seidl, 2016). Only with timely and detailed disturbance
maps  can  forest  managers  implement  mitigation  against  natural  di-
sasters (e.g., wildfire) through rapid damage assessment and evacuation
planning (Oddo and Bolten, 2019), or enact actions against illegal and
unsustainable  forest  harvesting  (Hansen  et  al.,  2016;  Wheeler  et  al.,

As of 2020, China's forest area reached approximately 220 million
hectares, making up about 5% of the world's total forest cover (Sarre,
2020). Given China's large forested areas and rapid economic expansion,
effective  monitoring  helps  address  forest  fragmentation,  habitat
destruction,  and  other  ecological  challenges.  Globally  exacerbated
climate warming also intensifies natural disturbances in China, such as
wildfires (Wu et al., 2019; Zhang et al., 2023) and pest outbreaks (Xu
et al., 2023). Particularly, China hosts the world's largest planted forest
area  (Cheng  et  al.,  2024),  and  these  planted  forests  might  be  more
vulnerable  to  climate-induced  disturbance  due  to  their  lower  species
richness  and  greater  structural  homogeneity  (Zhong  et  al.,  2021),
necessitating timely alerting and intervention.

* Corresponding author at: State Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China.

E-mail address: su.ye@zju.edu.cn (S. Ye).

https://doi.org/10.1016/j.rse.2026.115461
Received 23 October 2025; Received in revised form 7 April 2026; Accepted 26 April 2026
Available online 6 May 2026
0034-4257/© 2026 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Near-real-time (NRT) disturbance monitoring refers to performing a
disturbance mapping task with minimal delay between remotely sensed
image acquisition and decision making. The reported delay ranges from
several days (Tang et al., 2023; Ye et al., 2024) to two/three months
(Bullock et al., 2022; Reiche et al., 2018; Tang et al., 2019), depending
on the temporal resolution of the datasets and the chosen algorithm. The
earlier  NRT  disturbance-related  studies  focused  on  coarse-resolution
datasets  (> 30  m)  with  high  temporal  frequency,  such  as  the  MODIS
products (Reymondin et al., 2012; Verbesselt et al., 2012). Methods such
as  BFAST  Monitor  (Verbesselt  et  al.,  2012)  and  the  Terra-I  system
(Reymondin  et  al.,  2012)  have  been  widely  applied  to  MODIS  daily
observations to provide rapid disturbance alerts at global or continental
scales. With the open-access policy for Landsat (Woodcock et al., 2008),
the  NRT  monitoring  was  subsequently  extended  to  the  medium-
resolution  dataset  (10–30  m)  using  such  as  Landsat  (Hansen  et  al.,
2016;  Pasquarella  et  al.,  2017),  enabling  more  detailed  mapping  of
forest change. Recently, the combination of several satellite platforms,
such as Harmonized Landsat and Sentinel (HLS) dataset (Hansen, 2024;
Shang  et  al.,  2022),  has  proven  successful  in  reducing  detection  lags
owing  to  the  enhanced  data  density.  While  traditional  NRT  methods
identified  spectral  anomalies  from  time-series  datasets  using  a  pre-
defined  threshold  for  change  magnitudes  (Olsson  et  al.,  2016;  Pas-
quarella et al., 2017; Shang et al., 2022; Tang et al., 2019; Verbesselt
et al., 2012; Ye et al., 2021a), Ye et al. (2024) showed that the retro-
spective  analysis  on  early  signals  of  historical  disturbances  through
machine learning could considerably improve the timeliness for alerting
disturbances  in  an  NRT  manner.  Despite  various  datasets  and  algo-
rithms, almost all existing NRT studies only targeted mapping locations
and timing of generic forest disturbances, some of which additionally
provided disturbance probability map (Hansen et al., 2016). In a prac-
tical monitoring project, knowing why the disturbance occurs in a timely
manner  is  equally  important  as  being  informed  of  where  and  when,
because  information  on  causal  agents  (e.g.,  wildfire,  logging)  is  pre-
requisite  for  alert  prioritization,  actionable  management  and  impact
assessment (Slagter et al., 2023; Stahl et al., 2023). For example, Andela
et al. (2022) showcased separating wildfire disturbances from logging
and drought in Amazon holds great importance for wildfire suppression
and  air  quality  evaluation  for  this  region.  Particularly,  given  the
increasing  prevalence  of  forest  disturbances  globally,  there  is  a  clear
need for broadly applicable approaches that can map disturbance causal
agents in a timely manner.

The current challenges surrounding NRT disturbance agent mapping
are primarily two-fold: methodological limitations and data constraints.
While numerous successful studies have mapped historical disturbance
agents (Hermosilla et al., 2015; Kennedy et al., 2015; Qiu et al., 2025;
Stahl  et  al.,  2023),  the  retrospective  approaches  may  not  be  directly
applicable or could perform poorly in an NRT task. Most studies have
utilized temporal segmentation on annual time series and then classified
spectral breaks based upon spectral attributes of the breaks (Hermosilla
et al., 2016; Hermosilla et al., 2015; Kennedy et al., 2015; Schroeder
et al., 2017; Shimizu et al., 2017). A more advanced approach involved
applying an end-to-end deep learning model on annual composite (Chen
et  al.,  2021;  Perbet  et  al.,  2024),  instead  of  a  two-step  procedure  for
temporal  segmentation  and  break  classification.  Both  approaches
generated agent maps annually at their fastest update rate, making them
insufficiently  timely  for  an  NRT  monitoring  task.  Other  approaches
chose  dense  time  series  as  inputs  from  single-sensor  or  multi-sensor
combination,  often  processing  a  long  temporal  window  for  post-
disturbance observations. As a result, while the estimated disturbance
dates can be close to reference dates, their operational timeliness in an
NRT context remains limited when disturbances need to be character-
ized  within  days  to  weeks.  Zhang  et  al.  (2022) required  a  synthetic
image from one year after the spectral break as one of machine-learning
inputs for classifying for boreal forest agents. Likewise, Qiu et al. (2025)
included harmonic coefficients of the post-disturbance segment (at least
one year) in their land agent classification model. Since these studies

were originally designed for historical disturbance mapping, their per-
formance under a lack of long-term post-disturbance features remains
uncertain for the NRT scenario. To our knowledge, Slagter et al. (2023)
is the only study for addressing disturbance agent mapping in an NRT
scenario.  Slagter  et  al.  (2023) tested  Convolutional  Neural  Network
(CNN)  on  Sentinel-1  and  Sentinel-2  data  composited  over  a  period
ranging from 1 to 6 months after the disturbance for mapping the driver
for small-scale tropical forest disturbances (e.g., road development, se-
lective logging, and mining), reporting that the F1 score increased along
with the increasing post-disturbance period for compositing (1 month:
0.785; 6 months: 0.851). However, this approach suffers two primary
limitations when being operationalized for elsewhere in the world: 1) at
least one month of detection latency due to its contingency on cloud-free
monthly composite; 2) incapability of monitoring deciduous forest dis-
turbances because it ignores the confusion between disturbance signals
and seasonal defoliation.

An  NRT  monitoring  of  disturbance  agents  could  be  further  con-
strained by training data availability. A well-trained machine learning
model, built on a sufficient number of high-quality training datasets, not
only ensures accurate mapping of disturbance agents but also improves
the  timeliness  of  detecting  disturbance  signals  from  various  spectral
anomalies (Ye et al., 2024). Some existing studies manually interpreted
a set of disturbance agent samples and established a single classification
model that is applied into the study area (Hermosilla et al., 2015; Ken-
nedy et al., 2015; Shimizu et al., 2017; Slagter et al., 2023), while the
performance might be compromised if the samples were not optimal for
a  local  region.  To  fulfill  a  localized  training  sampling,  historical
disturbance  dataset  have  been  utilized  to  automate  agent  sample  la-
beling  in  United  States (Pastick  et  al.,  2019; Qiu  et  al.,  2025)  and  in
Canada  (Zhang  et  al.,  2022),  taking  advantage  of  the  abundance  of
public disturbance products in these two countries. This approach en-
ables  the  use  of  a  local  model  built  for  a  specific  region,  ultimately
enhancing  map  quality  (Qiu  et  al.,  2025). However,  historical  distur-
bance dataset covering comprehensive agents  is often unavailable for
most  regions  worldwide, including  China.  To  our  knowledge,  OPERA
Land  Surface  Disturbance  Product  (Hansen,  2024)  is  the  only  global
general disturbance dataset covering China's forest. The OPERA product
detects recent spectral anomalies for indicating forest loss but lacks in-
formation on disturbance agents.

This  study  aims  to  develop  a  new  NRT  approach  for  mapping
disturbance  agents,  with  an  application  to  monitoring  forest  distur-
bances in China and potential transferability to other regions globally.
To overcome the limitation of scarce local training data, we designed a
labor-saving  workflow  to  generate  local  samples  at  a  per-tile  basis
through a transfer mapping using disturbance samples from CONUS and
manual  verification.  Rich  spectral-temporal  features  following  distur-
bances  were  extracted  from  the  Harmonized  Landsat  and  Sentinel-2
(HLS)  dataset, which  provides the  densest  moderate-resolution obser-
vations to date. To enhance discrimination among disturbance agents,
particularly during the early stages of disturbance, we constructed stage-
specific  models  informed  by  the  number  of  consecutive  anomalies
detected, and applied them for the NRT monitoring scenario. Consistent
with previous studies (Hermosilla et al., 2015; Zhang et al., 2022), we
adopted a three-agent classification system, consisting of wildfire, log-
ging, and stress, with detailed definitions provided in Table 1.

Table 1
Definition for three major disturbance agents in this study.

Agents

Description

Wildfire Wildfire in forests or wooded land, including unplanned and prescribed

Logging

Stress

fires
The removal of forested vegetation by human activity such as timber
harvesting and construction, such as clear cutting, selective logging, etc.
Biological or environmental press that undermines forest health, vigor, or
resilience without causing stand-replacing canopy damage, such as insect
infestation and drought.

2

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

2. Study sites and datasets

2.1. Study sites

We  chose  the  five  study  sites  across  a  large  geography  of  China,
representing  a  variety  of  forest  types  and  disturbance  agent  patterns
(Fig. 1). Daxing'anling (“DX”), one of China's most wildfire-prone forest
areas,  is  located  in  the  northwestern  Heilongjiang  and  northeastern
Inner Mongolia Province, which is cold-temperate deciduous coniferous
forest dominated by Larix gemelini. The wildfire for this region mainly
occurred  in  spring  and  fall,  mainly  caused  by  lightning  (Zhao  et  al.,
2020). It has been reported that frequency and severity of the lightning-
induced wildfires are both increasing recently (Hu and Zhou, 2014). The
Sichuan Basin (SB) site, situated in southwestern China, is characterized
by  evergreen  broadleaf  forests,  mixed  conifer–broadleaf  stands,  and
extensive  bamboo  forests.  These  ecosystems  often  contain  dense  un-
derstory vegetation and substantial fuel loads. The accumulation of dry
branches, fallen leaves, and intertwined weeds further increases wildfire
risk, making the region highly prone to wildfires. The Xiangzhong Basin
(XB),  situated  in  central  Hunan  Province,  falls  within  the  subtropical
monsoon climate zone, characterized by warm, humid conditions and
abundant rainfall. Forest disturbances in this region are primarily driven
by  logging  and  wildfire  (Cao  et  al.,  2025).  In  particular,  timber  har-
vesting and land conversion were largely driven by wood demand and
agricultural  expansion,  which  follows  patterns  consistent  with  those

observed in other subtropical regions of China. The Yangtze Plain (YP)
site, located in Zhejiang Province, is dominated by subtropical evergreen
broad-leaved  forests  and  mixed  deciduous–evergreen  communities,
which together sustain a rich diversity of tree species. As one of China's
most developed regions, YP contains forests that are highly susceptible
to human disturbances, particularly land-use conversion. The last study
site, YunNan plateau (YN), hosts diverse forest ecosystems, ranging from
tropical monsoon rainforest in the south to evergreen broadleaf forests
in higher elevations. According to the past study (Lin et al., 2021), pine
shoot beetles have caused extensive tree mortality, leading to consid-
erable  ecological  impacts  across  the  forests  of  this  region.  All  sites
include all three disturbance agents, with a summary of forest types and
primary disturbance agents provided in Table 2.

2.2. Datasets

We used 2016 China Land Cover Dataset (CLCD) product (Yang and
Huang,  2021)  to  define  forest  pixel  population  for  NRT  monitoring.
CLCD, one of the most commonly used land cover products for China,
was  created  by  training  a  random  forest  with  temporal  metrics  using
training  samples  from  the  public  products,  which  reports  to  have  an
overall accuracy of ~80% (Yang and Huang, 2021).

We selected HLS time series datasets as the primary data source for
performing the NRT task in China as well as extracting primary distur-
bance features in CONUS. To create a seamless surface reflectance from

Fig. 1. Five study sites for testing an NRT forest disturbance monitoring in China. For each site, nine adjacent Harmonized Landsat and Sentinel (HLS) tiles were used
for testing the performance of the proposed approach (highlighted as yellow polygons). (For interpretation of the references to colour in this figure legend, the reader
is referred to the web version of this article.)

3

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

U
W
U
1
5

,
S
X
U
1
5

,
S
W
U
1
5

,
S
V
U
1
5

,

T
X
U
1
5

,

T
W
U
1
5

,

T
V
U
1
5

,

U
X
U
1
5

,

U
V
U
1
5

g
n
i
g
g
o
l
l
a
i
c
r
e
m
m
o
c
，

s
e
r
fi
d
l
i

W

a
l
l
y
h
p
y
t
a
l
p

a
l
u
t
e
B

,
s
i
r
t
s
e
v
l
y
s

s
u
n
i
P

,
i
n
i
l
e
m
e
g

x
i
r
a
L

t
s
e
r
o
f

s
u
o
r
e
f
i
n
o
c

s
u
o
u
d
i
c
e
d

e
t
a
r
e
p
m
e
t
-
d
l
o
C

)
X
D
(

'

g
n
i
l
n
a
g
n
i
x
a
D

s
e
l
i
T

)
S
L
H
(

l
e
n
i
t
n
e
S

d
n
a

t
a
s
d
n
a
L

d
e
z
i
n
o
m
r
a
H
d
e
t
c
e
l
e
S

s
t
n
e
g
a

e
c
n
a
b
r
u
t
s
i
d

y
r
a
m

i
r
P

s
e
i
c
e
p
s

e
e
r
t

y
r
a
m

i
r
P

s
e
p
y
t

t
s
e
r
o
f

y
r
a
m

i
r
P

e
m
a
n

e
t
i
S

,

T
T
R
8
4

,

M
Q
R
7
4

,

M
P
R
7
4

,

N
Q
R
7
4

,

N
P
R
7
4

,

P
Q
R
7
4

,

P
P
R
7
4

s
e
r
fi
d
l
i

W

s
u
p
r
a
c
o
h
t
i
L

,
s
i
s
p
o
n
a
t
s
a
C

,
s
i
s
p
o
n
a
l
a
b
o
l
c
y
C

s
t
s
e
r
o
f

d
e
v
a
e
l
-
d
a
o
r
b

n
e
e
r
g
r
e
v
e

l
a
c
i
p
o
r
t
b
u
S

)
B
S
(

n
i
s
a
B
n
a
u
h
c
i
S

U
T
R
8
4

,
S
T
R
8
4

Q
K
R
0
5

,
J
H
R
9
4

n
o
i
s
r
e
v
n
o
c

,

K
F
R
9
4

,

K
G
R
9
4

,

H
H
R
9
4

,

H
G
R
9
4

,

H
F
R
9
4

,
J
G
R
9
4

,
J
F
R
9
4

d
n
a
l

y
b

n
e
v
i
r
d

g
n
i
t
t
u
c

r
a
e
l
C

s
u
p
r
a
c
o
h
t
i
L

,
s
i
s
p
o
n
a
l
a
b
o
l
c
y
C

,
s
i
s
p
o
n
a
t
s
a
C

s
t
s
e
r
o
f

d
e
v
a
e
l
-
d
a
o
r
b

n
e
e
r
g
r
e
v
e

l
a
c
i
p
o
r
t
b
u
S

)
B
X
(

n
i
s
a
B
g
n
o
h
z
g
n
a
i
X

,

G
N
Q
7
4

,

H
Q
R
7
4

,

H
P
R
7
4

,

H
N
R
7
4

,
J
Q
R
7
4

,
J
P
R
7
4

,
J
N
R
7
4

e
r
fi
d
l
i

w

,
s
e
c
n
a
b
r
u
t
s
i
d

t
c
e
s
n
I

s
u
t
a
n
i
b
r
u
t

s
u
p
r
a
c
o
r
e
t
p
i
D

,
s
i
s
n
e
n
a
n
n
u
y

s
u
n
i
P

l
a
c
i
p
o
r
t

,
s
t
s
e
r
o
f

d
e
v
a
e
l
-
d
a
o
r
b

n
e
e
r
g
r
e
v
e

l
a
c
i
p
o
r
t
b
u
S

)
N
Y
(

u
a
e
t
a
l
p

n
a
N
n
u
Y

M
U
R
1
5

,

M
T
R
1
5
N
U
R
1
5

,

n
o
i
s
r
e
v
n
o
c

s
i
l
u
d
e

s
y
h
c
a
t
s
o
l
l
y
h
P

s
t
s
e
r
o
f

,

N
T
R
1
5

,

P
U
R
1
5

,

P
T
R
1
5

,

T
Q
R
0
5

,
S
Q
R
0
5

,

U
Q
R
0
5

d
n
a
l

y
b

n
e
v
i
r
d

g
n
i
t
t
u
c

r
a
e
l
C

,
a
t
a
l
o
e
c
n
a
l

a
i
m
a
h
g
n
i
n
n
u
C

,
a
b
r
e
p
u
s

a
m
i
h
c
S

o
o
b
m
a
b

,
s
t
s
e
r
o
f

d
e
v
a
e
l
-
d
a
o
r
b

n
e
e
r
g
r
e
v
e

l
a
c
i
p
o
r
t
b
u
S

)
P
Y
(

n
i
a
l
P

e
z
t
g
n
a
Y

G
Q
Q
7
4

,

G
P
Q
7
4

s
t
s
e
r
o
f

n
i
a
r

n
o
o
s
n
o
m

.
s
e
t
i
s

y
d
u
t
s

e
v
fi
r
o
f

s
t
e
s
a
t
a
d

d
n
a

,
e
c
n
a
b
r
u
t
s
i
d

,
t
s
e
r
o
f

e
h
T

2

e
l
b
a
T

Fig.  2. Spectral  anomalies  constitute  a  broad  category  encompassing  all
irregular  signals  detected  in  satellite-based  time-series  datasets.  A  subset  of
these anomalies emerges as spectral breaks, which represent pronounced and
persistent structural shifts in the spectral trajectory. While many spectral breaks
are typically associated with forest disturbance events such as wildfire or log-
ging,  non-disturbance  processes,  including  vegetation  succession  and  climate
variability, can also produce break-like signals. Conversely, certain disturbance
events, such as drought stress or understory wildfires, may induce only subtle or
short-lived  anomalies  that  do  not  evolve  into  detectable  breaks.  This  study
aimed to detect and classify spectral anomalies into four categories (blue fonts
in  the  figure):  wildfire,  logging,  stress,  and  non-disturbance  anomalies.  (For
interpretation  of  the  references  to  colour  in  this  figure  legend,  the  reader  is
referred to the web version of this article.)

the Operational Land Imager (OLI) and Multi-Spectral Instrument (MSI)
aboard Landsat-8/9 and Sentinel-2 A/B satellites, the HLS dataset har-
monizes  their  products  through  radiometric  calibration,  common
gridding, bandpass alignment, and geometric co-registration (Claverie
et al., 2018; Ju et al., 2025). With four sensors currently in the virtual
constellation, HLS provides observations once every 2–3 days with 30-m
resolution,  offering  the  highest  temporal  resolution  available  for
moderate-resolution datasets. To guarantee the densest time series, we
hereafter focused on only six spectral bands present on both HLS Landsat
(L30)  and  Sentinel-2  (S30)  products  (Table  S1  of  the  supplementary
material).

Similar  to  the  previous  work  (Ye  et  al.,  2024),  we  collected  an
ensemble  of  annual  CONUS-wide  disturbance  products  from  2017  to
2021,  which  were  used  to  build  the  CONUS  sample  archive  for  pre-
liminary  mapping  in  China.  These  products  include  Landsat-based
Burned  Area  (BA)  Science  Product  (Hawbaker  et  al.,  2020)  for  wild-
fire, and Aerial Detection Survey (ADS) insect activity dataset (Johnson
and  Wittwer,  2008)  for  stress  disturbances.  We  also  include  Land
Change Monitoring, Assessment, and Projection (LCMAP) Primary Land
Cover  maps  (Xian  et  al.,  2022)  and  LANDFIRE  Annual  Disturbance
Products (Ryan and Opperman, 2013) to indicate logging regions (see
Section 3.1).

3. Methodology

In  this  study,  we  adopted  a  two-level  hierarchical  framework  to
define  discontinuities  detected  in  the  time  series:  anomaly  and  break
levels.  Their  relationships  with  disturbance  agents  are  illustrated  in
Fig.  2.  Spectral  anomaly  refers  to  any  observation  where  the  spectral
reflectance  deviates  from  the  expected  patterns  predicted  by  the  his-
torical  time  series.  Such  anomalies  are  not  always  linked  to  distur-
bances;  they  may  instead  arise  from  processes  such  as  succession,
phenological shifts, climate variability, or even data noise (Zhu et al.,
2022). We therefore categorized those anomalies not directly linked to
disturbances as “non-disturbance anomalies”. A “spectral break”, on the
other hand, represents a cluster of anomalies with large magnitudes and
extended durations, resulting in a structural change in the time series.

4

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Fig. 3. The three-step workflow of the NRT forest disturbance agent mapping for this study.

Breaks are characterized by significant changes in statistical properties
(e.g., mean, variance) between pre- and post-change segments. When a
spectral break is detected, the time series model requires re-initialization
using  a  CCDC-like  approach,  which  necessitates  at  least  12  clear  ob-
servations  and  a  time  span  of  one  year  (Zhu  et  al.,  2022).  This  re-
initialization  complicates  NRT  monitoring,  as  the  absence  of  a  stable
model  in  the  new  segment  reduces  temporal  continuity,  therefore  a
stricter  threshold  is  expected  for  break  detection  to  minimize  unnec-
essary model reset. To address this challenge, we implemented a unified
monitoring workflow with two detection levels following the previous
study (Ye et al., 2024): (1) the anomaly level, using a sensitive config-
uration (changethreshold = 0.90, conse = 3) to inclusively detect all types
of spectral anomalies without triggering model re-initialization; and (2)
the  break  level,  using  a  conservative  configuration  (changethreshold =
0.9999,conse = 8) to identify pronounced structural changes that justify
model reset. Here, change threshold indicates the chi-square probability
for identifying spectral anomalies, while conse specifies the minimum
consecutive number of anomalies required to confirm a break. Using this
conservative break configuration, only 1.7% of forest pixels triggered a
break by the final weekly update (Table S2), indicating that model resets
were  rare.  The  primary  objective  of  this  study  is  to  classify  spectral
anomalies,  rather  than  breaks,  into  disturbance  agents  in  an  NRT
manner.

Our workflow proceeds in three stages (Fig. 3). First, we generated
high-quality  disturbance  agent  samples  for  CONUS  by  using  the
consensus between break detection and multiple disturbance products.
Next, the CONUS disturbance samples will be used to guide the local
sample  selection  and  model  construction  for  China.  Finally,  these
disturbance agent models, built from the local disturbance history, were
applied to direct NRT monitoring for recent disturbances.

3.1. CONUS sample preparation

3.1.1. CONUS sample selection

We  created  a  high-confidence  agent  sample  archive  from  the
consensus  between  spectral  anomaly  detection  and  CONUS-wide
disturbance  products.  Fifty  HLS  grids  were  randomly  sampled  across
CONUS (Fig. S1 in the supplementary), covering a variety of geographic
extent. The Stochastic Continuous Change Detection (S-CCD) algorithm
(Ye et al., 2021a) was implemented on all available HLS images of each
tile (2016–2022) and produced a series of annual spectral anomaly maps
from 2017 to 2021. S-CCD (https://github.com/Remote-Sensing-of-Lan
d-Resource-Lab/pyxccd),  a  short-memory  adaptation  of  the  CCDC  al-
gorithm that incorporates the Kalman filter, has two functionalities for
this  study:  retrospective  analysis  for  historical  anomalies  and  NRT
monitoring  for  the  most  recent  anomalies.  This  approach  ensures  the
consistent  feature  generation  between  the  retrospective  and  the  NRT
scenario. The anomalies for the first (2016) and the last year (2022) of
data range were excluded because the quality of spectral anomalies are
often unsatisfactory for CCDC-like algorithms.

For open-access disturbance products, we first generated a general
disturbance  map  at  an  annual  step  by  combining  Landsat-based  BA
product,  ADS  dataset  for  stress  samples,  the  category  transition  map
from  differencing  LCMAP  Primary  Land  Cover  maps  between  two
neighbor years, and the annual LANDFIRE disturbance map. By over-
lapping  the  general  disturbance  map  with  its  corresponding  annual
spectral anomaly map, we identified four distinct sample pools: one for
wildfire disturbances, defined by spectral anomalies within the Burned
Area (BA) region; one for stress disturbances, linked to spectral anom-
alies overlapping the insect-impact region as indicated by the ADS map;
one  for  logging  disturbances,  consisting  of  spectral  anomaly  pixels
within forest transition regions identified by category changes in LCMAP

5

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

cover maps or marked as “logging” in the LANDFIRE disturbance map;
and one for non-disturbance anomalies (e.g., phenological shifts, image
noises), which are those spectral anomaly pixels outside the extent of
general  disturbances.  We  applied  stratified  sampling  to  collect  2000
samples  from  each  sample  pool  per  HLS  tile  for  each  year  (2017  to
2021). For 50 CONUS tiles, we reached the final CONUS sample archive,
consisting of four PIXEL pools, i.e., logging (n = 356,604), wildfire (n =
310,500), stress (n = 76,500) and non-disturbance anomaly pool (n =
386,594), after excluding non-forest pixels.

3.1.2. Disturbance agent feature extraction

We  extracted  16  disturbance  agent  features  for  CONUS  samples,
comprising three pre-disturbance features, nine trajectory-based change
features, two general change features, one disturbance-date feature and
one data-density feature. Like other CCDC-type algorithms, S-CCD pro-
duces  temporal  features  (e.g.,  harmonic  coefficients  and  break-based
change magnitudes) for each original band. Accordingly, the predicted
reflectance ̂ρi,x  for xth observation since the first anomaly signal at the
ith HLS band (i = 1, 2, …, 6) is reconstructed from the pre-disturbance
harmonic coefficients:

̂ρi,x = a0,i +

(

∑n=2

k=1

(

2πk
T

ak,icos

)

(

date(x)

+ bk,icos

) )

2πk
T

date(x)

(1)

+ c1,idate(x)

Where ak,i  and bk,i  are the harmonic coefficients, k is temporal fre-
quency of harmonic component, n is the number of harmonic pairs (note
that  n=2  for  S-CCD),  T  is  the  number  of  days  per  year  (T=365.25).
Following Zhang et al. (2022), we reduced the six HLS spectral bands
into  three  physically  meaningful  components,  namely  brightness,
greenness,  and  wetness,  using  the  Tasseled-Cap  (TC)  transformation.
This feature reduction effectively halved the dimensionality of the input
space, thereby alleviating potential overfitting and poor generalization
associated with a high-dimensional feature input (Verleysen and Fran-
çois, 2005). The three pre-disturbance features, selected for disturbance
agent prediction in this study, were derived from the predicted reflec-
tance at the first post-anomaly observation (x = 1):

⎡

⎣

̂ρbri,pre
̂ρgre,pre
̂ρwet,pre

⎤
⎦ = B •

⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎦

⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎣

̂ρ1,1
̂ρ2,1
̂ρ3,1
̂ρ4,1
̂ρ5,1
̂ρ6,1

(2)

The matrix B represents the TC coefficient matrix for Landsat 8, as
outlined  in  (Baig  et  al.,  2014).  Since  the  Sentinel-2  data  in  the  HLS
dataset  was  “spectrally  adjusted  to  match  Landsat  8/OLI  spectral
bandpasses” (Claverie et al., 2018), it is appropriate to use the Landsat 8
TC coefficients for HLS. The coefficients are as follows:

⎡

⎣

B =

0.3037 0.2793 0.4743 0.5585 0.5082 0.1863
(cid:0) 0.2941 (cid:0) 0.243 (cid:0) 0.5424 0.7276 0.0713 (cid:0) 0.1608
0.1511 0.1973 0.3279 0.3406 (cid:0) 0.7117 (cid:0) 0.4559

⎤

⎦

(3)

In  addition,  S-CCD  preserves  the  eight  multispectral  observations
since the first anomaly observation signal. This enables the calculation
of  each  band-specific  change  magnitude  at  the  xth  post-anomaly
observation (x = 1, 2, …, 8) for the ith band (i = 1, 2, …, 6):

CMi,x = ̂ρi,x (cid:0) ρi,x

(4)

Where ρi,x  and ̂ρi,x  represents the actual and predicted reflectance for
xth  observation  since  the  first  anomaly  signal  at  the  ith  band.  Corre-
spondingly,  the  TC-based  change  magnitudes  were  derived  as  linear
combinations of these band-wise change magnitude:
⎤

⎡

⎡

⎣

CMbri,x
CMgre,x
CMwet,x

⎤

⎦ = B •

⎢
⎢
⎢
⎢
⎢
⎢
⎣

⎥
⎥
⎥
⎥
⎥
⎥
⎦

(5)

CM1,x
CM2,x
CM3,x
CM4,x
CM5,x
CM6,x

We  further  constructed  spectral  trajectories  by  tracking  ρbri,x,  ρgr,x,
and ρwet,x  across successive post-anomaly observations (x = 1, 2, …, 8).
From  each  trajectory,  a  set  of  descriptors  was  derived  in  the  two-
dimensional  feature  space  (date,  ρ).  Specifically,  Slope  denotes  Theil-
Sen  slope  representing  the  general  spectral  trend  after  disturbance
occurrence. Intercept is the intersecting point between the first anomaly
date  and  the  Theil-Sen  trendline,  which  represents  the  initial  post-
anomaly  feature  value.  Because  trajectories  may  deviate  from  line-
arity, skewness of the residuals is used to quantify asymmetric departures
from the fitted linear trend:

skewnessx = 1
x

∑x

i

)3

(
ei (cid:0) e
s

(6)

Where x is the current number of successive anomalies since the first

̂
anomaly  signal,  ei  is  the  residual  between  the  predicted
CMi  by  the
Theil-Sen linear equation and the actual CMi, and s is the standard de-
viation  of  ei.  As  a  result,  for  each  anomaly  segment,  nine  trajectory-
based  features  were  generated  corresponding  to  three  trajectory  de-
scriptors (slope, intercept, and skewness) for each of the three TC com-
ponents (brightness, greenness, and wetness). We assigned zeros to them
if  x=1.  Notably,  trajectory-based  features  could  differentiate  distur-
bance agents to some degree (see Fig. S2), but are not assumed to exhibit
a universal, globally consistent pattern across all regions. We used these
features  primarily  for  local  discrimination,  as  our  disturbance-agent
classifiers  were  trained  on  a  per-tile  basis  using  locally  verified  sam-
ples, allowing the models to learn region-specific relationships between
trajectory descriptors and disturbance agents.

In  addition,  we  incorporated  two  general  change  features  from

Table 3
Definition of 16 disturbance agent features for this study. “Time-varying” means that the features are varying with post-anomaly observation collection in an NRT
scenario for a pixel.

Predictor name

Description/Equation

Time-varying

1. Pre-disturbance features
2. Spectral-trajectory descriptors

3. Normalized change magnitude

4. Spectral consistency angle

5. First anomaly day of year (DOY)
6. Anomaly span

, skewnessbri, skewnessgre, skewnesswet

̂ρbri,pre, ̂ρgre,pre, ̂ρwet,pre
, slopegre
slopebri
interceptbri

, slopewet
, interceptgre

CMnormalized,x =

,
, interceptwet
)
(
2
CMi,x
rmsei,x

∑
6
i=2

∑

n (cid:0) 1

n(cid:0) 1
angle = 1
j=1
DOY of the first anomaly observation
ndays = lastobs dat (cid:0) dist dat

βj,j+1

No
Yes

Yes

Yes

No
Yes

Note: βj,j+1  is the change-vector angle from jth to j + 1th anomaly; lastobs dat and dist dat are the last available observation date and the disturbance starting date.

6

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Then, we computed Mahalanobis distance between each U.S. sample (k)
and the multivariate distribution:
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
(k (cid:0) μ)TS(cid:0) 1(k (cid:0) μ)

dx =

(7)

√

We ranked the samples in each of the four CONUS sample pools by
their Mahalanobis distance to the targeted China tile and selected the
top 30% as the initial sample set. To evaluate this strategy, we compared
the average Bhattacharyya distance (BD) between (1) the full CONUS
samples  and  the  local  China  samples  (derived  from  expert-verified
preliminary maps; Section 3.2.2), and (2) the selected CONUS samples
and  the  same  local  China  samples,  across  45  target  tiles.  BDs  were
computed for the four most informative disturbance features, as iden-
tified  by  random-forest  Gini  importance  (Section  3.2.3).  The  results
(Fig. S3 of the supplementary material) show that BDs decreased after
selection  for  stress  and  wildfire,  indicating  that  the  distribution  of
transferred samples becomes more similar to the target-domain samples
when guided by topographic and vegetation similarity. In contrast, BD
changes  were  more  variable  for  logging,  likely  reflecting  greater  het-
erogeneity and region-specific management practices that are not rep-
resented  during  sample  transfer.  Overall,  these  results  suggest  that
topographic  and  vegetative  matching  can  effectively  improve  cross-
region  sample  alignment,  particularly  for  natural  disturbances,
thereby strengthening subsequent disturbance mapping.

For the agent proportion, we first used an empirical equation from
the  previous  study  to  determine  the  proportion  for  non-disturbance
anomalies (Ye et al., 2024). The proportion was calculated as:

Propnodisturb

= 0.9 (cid:0) (CONSE (cid:0) x)*0.02

(8)

Where CONSE is the maximum number of consecutive anomalies, set
to 8, x is the number of consecutive anomalies to be investigated. We
used x = 6, as six consecutive anomalies has been widely used for CCDC-
like  approach  as  the  default  parameter  (Xian  et  al.,  2022;  Zhu  et  al.,
2020;  Zhu  and  Woodcock,  2014).  Therefore,  the  proportion  for  non-
disturbance anomalies is 86% (i.e., 0.9 – (8–6) * 0.02). The remaining
sample number were equally distributed to three disturbance agents. A
total of 10,000 CONUS samples spanning from 2017 to 2021 was applied
for each tile, following the previous work (Ye et al., 2024). As a result,
the sample numbers for non-disturbance anomalies, wildfire, logging,
and  stress  were  8600,  467,  467,  and  467,  respectively.  Equal  prior
probabilities were assumed for all disturbance agents, since their rela-
tive area proportions could not be estimated prior to the generation of
the classification map (Qiu et al., 2025).

From this set, we then applied an equal-interval sampling strategy to
construct  CONUS  samples  per  sample  pool.  For  instance,  within  the
wildfire pool  (310,500 samples),  we retained  the  top 93,150 samples
(30%) and subsequently selected every 199th sample (93,150/467) in
ascending order of Mahalanobis distance. The equal-interval sampling
approach  minimizes  redundancy  from  any  single  geographic  region,
thereby enhancing the overall diversity of the selected samples.

3.2.2. Transferring-guided local samples

We collected 10,000 CONUS samples from the sample-transfer pro-
cedure  and  transfer  16  disturbance-agent  features  from  CONUS
(Table  2)  derived  from  six  consecutive  anomalies  (x  = 6)  to  train  an
initial  random  forest  model  for  each  tile.  These  features  represent  a
multi-dimensional  feature  space  that  combines  both  pre-disturbance
signatures  and  disturbance-process  changes,  improving  separability
among disturbance agents. We note that we did not explicitly incorpo-
rate land management policies or other socio-economic features into the
NRT  agent  classification  framework,  mainly  because  adequate  high-
resolution, spatially consistent socio-economic and policy datasets are
not readily available for our study regions. Nevertheless, regional dif-
ferences in management intensity, land use pressure, accessibility, and
enforcement can strongly influence both the frequency and composition
of  disturbance  agents,  likely  contributing  to  the  spatial  variability  in

Fig. 4. Conceptual figure for transferring CONUS samples for a specific China's
HLS tile. A vegetation–topography feature space is constructed for all CONUS
samples. The target domain is defined by the feature distribution of the target
tile.  After  similarity  screening  (top  30%)  and  equal  interval  sampling,  a
representative sample set matching the target domain is generated for subse-
quent local model training.

COntinuous monitoring of Land Disturbances (Zhu et al., 2019a, 2019b),
i.e.,  normalized  change  magnitudes  and  spectral  consistency  angle,
which has shown effectiveness for distinguishing true disturbances from
noisy  signals,  especially  when  multiple  consecutive  anomalies  are
available. Finally, we added “first anomaly day of year” to account for
the occurrence date of a disturbance (e.g., wildfire disturbances occur
more in April in China  due to tomb-sweeping practices for Qingming
Festival), and “anomaly span” to incorporate the effects of data density.
Collectively,  we  adopted  16  disturbance  features  for  building  agent
classification models (Table 3). Of note is that as a part of disturbance
features  are  time-varying  with  more  observation  being  collected  (see
Table  3),  we  created  a  set  of  features  for  every  possible  number  of
consecutive anomalies from (x = 1, 2, …, 8).

3.2. Local agent model construction for China

For each targeted HLS tile in China, we first applied retrospective S-
CCD to all available HLS images from 2016 to 2023. This process yielded
segment-based  harmonic  coefficients  at  the  per-pixel  level,  together
with 16 disturbance-agent features for all identified anomalies. These
outputs served three purposes: (1) characterizing the vegetative condi-
tions of each tile to guide the selection of the most appropriate CONUS
subsample;  (2) providing  spectral anomalies  and  their  associated  fea-
tures for constructing preliminary historical disturbance maps; and (3)
supplying  the  initial  data  inputs  for  recursive  updates  in  the  NRT
monitoring framework. A detailed description is provided below.

3.2.1. Sample transfer

Building  upon  “similar  geographic  configurations  lead  to  similar
geographic processes”  (Zhu et al., 2018), which has been successfully
applied in sample transferring (Cui et al., 2025; Hou et al., 2025; Zhu
et al., 2019a, 2019b), we proposed the hypothesis that “the more similar
the  topographic  and  vegetation  conditions,  the  more  similar  the
disturbance spectral features are”. Based on this, we developed a method
for  selecting  a  subsample  from  the  CONUS  sample  archive  that  most
closely  matches  the  characteristics  of  a  targeted  HLS  tile  in  China
(Fig.  4).  The  topographic  variables  considered  include  the  digital
elevation model (DEM) and slope, derived from Shuttle Radar Topog-
raphy Mission (SRTM) data (Yang et al., 2011). The vegetative variables
consist of pre-disturbance TC brightness, TC wetness, and TC greenness,
which were calculated from synthetic surface reflectance images (dated
July 1, 2016) generated through segment-based harmonic coefficients,
following the CCDC framework (Zhang et al., 2022; Zhu et al., 2015).
Each  targeted  tile  was  characterized  by  constructing  a  multivariate
normal  distribution  based  on  these  two  topographic  and  the  three
vegetative variables. Their mean vector (μ) and covariance matrix (S)
were computed from the “forest” pixels identified by the CLCD product.

7

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Fig. 5. Manual verification example for a patch labeled as wildfire in the preliminary disturbance mapping (Latitude: 28.1524
E). (a) Time-
series trajectory showing a distinct temporal break characterized by a sharp decrease in NIR reflectance. (b) HLS image chips (true colour composite) acquired near
the  disturbance  date  across  three  consecutive  years.  The  observed  burn  scar  and  concurrent  spectral  decline  confirmed  that  the  preliminary  wildfire  label  was
correctly assigned.

◦

◦
N; Longitude:120.1326

disturbance regimes observed across the five study sites. Accordingly,
our workflow was designed to be locally adaptive, because models and
class proportions were constructed on a per-tile basis with local verifi-
cation, which helped accommodate regional differences in disturbance
regimes even when the underlying drivers differ.

Subsequently,  we  applied  S-CCD  to  all  available  HLS  imagery  to
detect spectral anomalies for each forest pixel in the targeted tiles be-
tween  2019  and  2023.  The  anomalies  were  then  input  into  the  tile-
specific random forest model to produce a five-category map: wildfire,
logging, stress, non-disturbance anomalies, and anomaly-free forest. The
“anomaly-free  forest”  class  includes  forested  pixels  where  no  spectral
anomalies were detected by S-CCD in history, indicating that these areas
have  not  experienced  detectable  spectral  changes  in  the  time  period
analyzed. For each annual disturbance map, we connected two neigh-
borhood pixels with the same category and generated historical distur-
bance agent patch maps from 2019 to 2023, which consisted of three
types  of  disturbance  agents  as  well  as  the  non-disturbance  anomaly
category. Among them, we selected 1000 disturbance agent patches for
each  of  the  four  categories  (wildfire,  logging,  stress,  and  non-

disturbance  anomalies)  within  each  HLS  tile,  evenly  distributed  to
each year from 2019 to 2023. To address the uncertainties in the pre-
liminary mapping results, four experienced interpreters were recruited
to manually verify the patch labels. The verification was based on pre-
made  figures  that  included  both  HLS  time-series  plot  of  the  center
pixel and HLS image chips (see the example of Fig. 5). All interpreters
received  training  and  testing  prior  to  the  labeling  task  to  ensure
consistent interpretation criteria and efficient review. Only patches with
high  confidence  in  their  assigned  labels  were  retained.  To  assess  the
efficiency  of  this  transferring-guided  approach,  we  recorded  the  time
with each interpreter required to complete their respective verification
tasks. The verified patches were subsequently dissolved to the pixel level
to establish four high-quality local sample pools. The verification out-
comes  and  the  corresponding  time  consumption  are  summarized  in
Table S3 of the supplementary material. On average, for each HLS tile,
an interpreter required approximately 2.1 h to verify 4000 disturbance
patches from the preliminary mapping, of which 1697 patches (~42%)
were labeled as high-confidence disturbance agent patches, yielding a
total  of  38,286  sample  pixels  (Table  S3).  This  high  interpretation

8

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

efficiency is partially attributed to the fact that the interpreters were not
required  to  determine  the  disturbance  date,  as  this  information  had
already been provided by the S-CCD-derived break date.

We  set  a  total  of  10,000  final  local  samples  for  each  HLS  tile  to
construct the final local machine learning model. These samples were
drawn  from  the  pixel  pool  verified  to  be  correct  from  preliminary
mapping. For categorical allocation, the proportion of non-disturbance
anomalies  was  determined  as  a  negative  function  of  the  number  of
consecutive  anomalies  (x),  following  Eq.  8.  This  design  increases  the
relative  proportion  of  disturbance  samples  when  x  is  small,  thereby
enhancing detection sensitivity during the early disturbance stage (Ye
et al., 2024). The remaining proportion was distributed among distur-
bance  agents  according  to  their  relative  pixel  frequencies  verified  as
correct, ensuring that dominant disturbance types were assigned more
samples. The minimum sample number per category is set to 300 pixels,
which  guarantees  that  the  minority  category  will  not  be  under-
represented. Accordingly, we prepared eight sets of local samples cor-
responding to the eight possible numbers of consecutive anomalies (x =
1, 2, …, 8) for each tile.

3.2.3. Stage-based local models for China

We constructed stage-based disturbance agent models for each tile
using the corresponding sample sets and their 16 agent-based features
(Table  3),  with  the  disturbance  stage  indicated  by  the  number  of
consecutive anomalies. This stage-wise design allowed us to capture the
statistical relationships more acutely between the features and distur-
bance agents, particularly during the early stage when a disturbance had
just  begun  (i.e.,  x = 1 or 2).  As  such,  eight  disturbance  agent models
(x = 1, 2, …, 8) were trained from local samples for the NRT mapping.
We also assessed the average Gini-based feature importance across all
tiles for these eight models (Fig. S4 in the supplementary material). The
analysis  reveals  that  (1)  normalized  change  magnitude  and  spectral
consistency angle are consistently the most important features, and (2)
spectral-trajectory descriptors, especially the greenness and brightness
intercepts, exerts a significant role in influencing the model performance
across all stages.

3.3. Near-real-time mapping in China

We implemented NRT disturbance-agent monitoring for 2024 across
the five study sites using a weekly updating frequency, which resulted
into  52 weekly  agent classification  maps.  In the  NRT workflow,  each
pixel was first evaluated for its current number of consecutive anoma-
lies.  This  procedure  generated  eight  NRT  anomaly  clusters,  corre-
sponding to disturbance stages ranging from one to eight consecutive
anomalies. Each cluster was then classified by its corresponding random
forest model into the four categories (logging, wildfire, stress, and non-
disturbance  anomalies),  using  16  disturbance  features  extracted  from
the current anomaly segment. The results were aggregated into a weekly
NRT  disturbance-agent  map,  based  on  the  spatial  locations  of  the
detected anomalies. To mitigate false positives, we applied a filtering
rule that excluded “stress” pixels with only one consecutive anomaly, as
the  weak  early-stage  signals  of  stress  disturbances  are  often  indistin-
guishable from phenological variability or data noise. In addition, we
grouped  adjacent  pixels  with  the  same  disturbance  agent  labels  into
disturbance patches using connected-component labeling and applied a
sieving filter to remove small isolated detections. Specifically, patches
smaller than 0.3 ha (fewer than four 30 m HLS pixels) were removed to
reduce salt-and-pepper noise.

Notably,  despite  the  harmonization  efforts  in  HLS,  residual  inter-
sensor  effects  (e.g.,  subtle  radiometric  inconsistencies  and  occasional
sub-pixel misregistration) may still occur and could potentially trigger
spurious anomaly signals. To reduce these impacts, we applied the HLS
quality masks and detected anomalies normalized by multi-band resid-
ual departures using a chi-square decision rule, which was less sensitive
to  small  sensor-to-sensor  biases  that  tended  to  manifest  as  high-

frequency  noise.  In  addition,  our  workflow further  suppressed  single-
date  artifacts  through  temporal  persistence  (consecutive  anomalies
and  stage-based  models),  explicit  inclusion  of  a  non-disturbance
anomaly class during training, and a spatial sieving filter that removes
very small isolated patches.

Finally,  we  developed  an  NRT  platform  to  implement  the  weekly
updating  procedure  and  to  visualize  the  resulting  disturbance-agent
maps.  The  website  address  is  https://forestwatch.com.cn.  The  inter-
face  of  this  website  was  displayed  in  Fig.  S5  of  the  supplementary
material.

3.4. Accuracy and latency assessment

We conducted accuracy assessments at the study-site level. For each
site, 1200 pixel-based samples were generated using stratified random
sampling,  with  300  samples  assigned  to  each  of  the  four  categories:
wildfire,  logging,  stress,  and  non-disturbance  forest  (including  non-
disturbance  anomalies and anomaly-free  forest). The four  strata  were
defined as all the pixels being labeled from an ensemble of 52 weekly
NRT disturbance agent maps. Across the five representative study sites,
this  yielded  a  total  of  6000  samples  for  evaluating  the  overall  model
performance. Experienced interpreters manually determined the refer-
ence  disturbance  category  and  occurrence  date  for  each  sample  pixel
primarily using daily 3-m Planet imagery. Additionally, for stress vali-
dation, we relied on the HLS time-series interpretation for (1) a signif-
icant SWIR2 increase with stable NIR band (e.g., bark borer) (Ye et al.,
2021b) or (2) a pronounced NIR drop followed by rapid recovered (e.g.,
defoliator) (Silva et al., 2013). The occurrence date was defined as the
first day on which an anomaly signal could be visually identified from
the Planet image, enabling evaluation of the system's detection latency
under operational conditions. Of note is that daily Planet imagery was
not guaranteed for all study sites (with approximately 30% of the days
missing), which could introduce some uncertainties when interpreting
the reference disturbance dates. Despite this limitation, we believe that
using  Planet  imagery  remains  the  most  reliable  method  available  for
interpreting the reference dates.

We first used these samples to assess individual agent mapping ac-
curacy across 52 weekly NRT agent maps in 2024. Following the sigmoid
framework proposed by Bullock et al. (2022), we generated lag-accuracy
curves for each agent to illustrate how accuracy varies with detection
lag. The lag was defined as the temporal difference between the map
production date (i.e., the weekly update date on our NRT platform) and
the  reference  disturbance  date  interpreted  from  Planet  imagery.  For
each  lag  interval,  we  constructed  a  confusion  matrix  and  calculated
user's accuracy (UA), producer's accuracy (PA), and, F1  score for each
disturbance agent, thereby forming the lag-accuracy curves for inspec-
tion. We then will derive two key lags: the first-alert and level-off lags.
The  first-alert  lag,  also  termed  as  Mean  Time  Lag  for  the  First  Alert
(Reiche et al., 2018), is defined as the average time between the refer-
ence disturbance date and the first correct classification by the platform.
This metric quantifies the system's responsiveness in issuing its earliest
correct alerts, considering only disturbances that were correctly iden-
tified (Bullock et al., 2022). The level-off lag (Bullock et al., 2022) will
be employed to evaluate the latency and the model performance when
the NRT model accuracy plateaus. The level-off lag was determined as
the point of maximum vertical distance (y-value) between the curve and
◦
a rotated virtual line (45
around the straight line connecting the curve's
endpoints).

For the multi-agent assessment, we calculated the overall first-alert
and level-off lags as the weighted means across the three disturbance
agents,  using  their  total  mapped  area  proportions  by  aggregating  52
weekly  resultant  maps  as  weights.  We  reported  the  snapshot-based
confusion  matrices  and  Overall  Accuracy  (OA)  at  the  two  overall  lag
times. Because stratified sampling was employed for the reference data,
all  accuracy  metrics  were  adjusted  by  the  mapped  area  proportions,
following the recommended best practices outlined by Olofsson et al.

9

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Fig. 6. The average accuracy metrics for three disturbance agents at their first-alert and level-off lags across five study sites.

Fig. 7. The lag-accuracy curves for three individual disturbance agents. The first-alert and level-off lags were marked respectively as the light red and dark red
dashed line. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

(2014).  We  note  that  our  accuracy  assessment  targets  the  end-to-end
NRT outputs, and therefore the reported commission and omission er-
rors implicitly include uncertainties from both S-CCD anomaly detection
and subsequent agent classification.

For  benchmarking,  we  compared our  NRT products  with  OPERA's
DIST-ALERT product (Hansen, 2024), which detects globally reductions
in vegetation fraction whenever a new clear observation is acquired. By
referencing a historical baseline for the same time of year, DIST-ALERT
adjusts  for  seasonal  vegetation  dynamics  and  reduces  false  alerts.
Similar to our platform, DIST-ALERT is based on time-series analysis of
the HLS dataset and is updated approximately weekly; however, it only
identifies  general  disturbances  without  distinguishing  among  agents.
Accordingly, we limited our comparison to binary detection accuracy
and  latency  (i.e.,  disturbance  vs.  no  disturbance).  We  reported  the
comparative  lags,  UA,  PA,  F1,  and  the  level-off  OA  under  the  binary
scenario (disturbances vs no disturbances), with the latter adjusted by
each  category's  area  proportion  respectively  from  the  proposed  and
DIST-ALERT.

4. Results

4.1. Individual disturbance assessments

Fig. 6 shows the variations in the average lags and accuracies over
the five study sites across three disturbance agents. The NRT mapping
for wildfire disturbances achieved the shortest first-alert lag (8.2 days)
and the earliest level-off point (12.6 days) among the three agents, along
with the highest UA (82.6%, 88.8%), PA (59.2%, 74.5%), and F1  scores
(0.669,  0.81).  This  is  likely  attributable  to  the  strong  low-reflectance
signal of burn scars shortly after wildfire events, which enables rapid
and  accurate  detection.  Logging  disturbances  exhibited  intermediate
latency, with the first-alert lag of 11.7 days and the level-off lag of 15.4
days. Stress disturbances required the longest time to be detected, with a
first-alert lag of 18.4 days and a level-off lag of 25.4 days. This longer
latency can be explained by their more ambiguous spectral feature as
well  as  our  definition  that  a  stress  pixel  must  show  at  least  two
consecutive anomalies. Stress disturbances also was reported to have the
lowest UA (33.6%, 51.9%), PA (33.1%, 55.4%), and F1  scores (0.305,
0.513)  when  the  two  key  lags  were  reached,  indicating  greater

10

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Table 4
Snapshot-based confusion matrices at the overall first-alert lag (12 days).

Reference

Map

Wildfire

Logging

Stress

Non-disturb.

Confusion matrix, sample counts
691
Wildfire
31
Logging
8
Stress
418
Non-dist. Forest
Total
1148
Confusion matrix, area proportion adjusted by mapped area proportion (Table S4)
Wildfire
Logging
Stress
Non-dist. Forest
Total
OA

0.00013
0.00008
0.00000
0.09663
0.09685
0.00013 + 0.00083 + 0.00001 + 0.77350 = 77.5%

0.00000
0.00083
0.00000
0.05479
0.05562

23
305
9
237
574

3
16
85
318
422

0.00000
0.00004
0.00001
0.07351
0.07357

65
150
295
3346
3856

0.00001
0.00041
0.00004
0.77350
0.77397

Table 5
Snapshot-based confusion matrices at the overall level-off lag (16 days).

Reference

Map

Wildfire

Logging

Stress

Non-disturb.

877
32
7
232
1148

Confusion matrix, sample counts
Wildfire
Logging
Stress
Non-dist. Forest
Total
Confusion matrix, area proportion adjusted by mapped area proportion (see Table S4)
0.00014
Wildfire
0.00008
Logging
0.00000
Stress
0.05748
Non-dist. Forest
0.05769
Total
0.00014 + 0.00082 + 0.00003+ 0.83863 = 84.0%
OA

0.00000
0.00082
0.00000
0.04831
0.04914

24
339
16
195
574

2
17
185
218
422

0.00000
0.00004
0.00003
0.05401
0.05408

63
174
234
3385
3856

0.00001
0.00042
0.00003
0.83863
0.83910

Total

782
502
397
4319
6000

0.00015
0.00136
0.00006
0.99843
1.00000

Total

966
562
442
4030
6000

0.00015
0.00136
0.00006
0.99843
1.00000

difficulties  in  distinguishing  stress  from  other  noisy  factors  such  as
phenological variation. Overall, disturbance agents that were detected
earlier due to their stronger spectral separability (e.g., wildfire) tended
to achieve higher mapping accuracy than those characterized by subtle
spectral changes (e.g., stress).

Fig. 7 illustrates the site-specific lag–accuracy curves. Most curves
exhibited  an  increasing  trend  with  longer  lags,  as  additional  post-
disturbance  observations  improved  the  extraction  of  trajectory-based
features  (e.g.,  slope  and  skewness)  and  the  accumulation  of  consecu-
tive anomalies helped suppress short-lived noise caused by phenological
fluctuations. The curves generally plateaued at larger lag values, indi-
cating that most disturbances had been detected by that stage. Fig. 7 also
reveals pronounced regional differences in the performance of the pro-
posed approach. For wildfire, the Xiangzhong Basin exhibited relatively
lower UA, PA, and F1  score compared with the other four sites, while its
first-alert and level-off lags were of intermediate length. This may be

attributed to its fragmented landscape and humid subtropical climate,
both of which obscure distinct wildfire signals. For logging, the lowest
accuracy occurred in Daxing'anling, likely due to small-scale selective
harvesting and strong seasonal variability that complicate disturbance
identification.  For  stress,  the  Yangtze  Plain  uniquely  exhibited  an
inverted-U pattern, where accuracy initially increased but declined with
longer observation windows, reflecting the rapid recovery of drought-
induced  spectral  anomalies  typical  of  this  region.  Overall,  consistent
with Fig. 6, both wildfire and logging exhibited shorter detection lags
than stress, except in the Yunnan Plateau, where the confirmation lag
was relatively longer (exceeding 20 days) for both wildfire and logging
events.

4.2. Overall latency and accuracy

The mapped area proportions for wildfire, logging, stress, and non-

Fig. 8. The lag-accuracy curves and the accuracy metrics associated with two key lags for the binary maps produced by the proposed and DIST-ALERT for the five
study sites.

11

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Fig. 9. Comparison between the proposed near-real-time (NRT) framework and the DIST-ALERT product across four representative study sites. The larger panels
present the 2024 yearly ensemble maps in which only confirmed disturbance polygons (defined as those with an average number of consecutive anomalies >5) are
retained.  The  smaller  panels  display  weekly  NRT  results  from  the  proposed  framework  for  three  consecutive  weeks  following  disturbance  onset  (Weeks  1–3),
◦
alongside the corresponding DIST-ALERT binary disturbance maps and HLS image (NIR-Red-Green composite) for Week 1. (A) Sichuan Basin wildfire (29.8612
N,
◦
101.5941
E); (D) Xiangzhong Basin logging
◦
(26.0371

◦
E); (C) Yunnan Plateau stress disturbance (25.8580
E). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

E); (B) Yangtze Plain logging (28.1069
◦
N, 113.5437

◦
N, 120.4240

◦
N, 101.7880

◦

disturbance  forest  were  0.00015,  0.00136,  0.00006,  and  0.99843,
respectively, calculated by aggregating the number of pixels assigned to
each category across all weekly maps (see Table S4). Using these agent-
specific mapped area proportions as weights, the overall first-alert and
level-off lags were estimated to be 11.6 days and 15.5 days, respectively.
We  further  constructed  confusion  matrices  for  the  two  key  lags
(Tables 4 and 5) and estimated the overall accuracy by weighting agent-
wise accuracy using the mapped area proportions. When the first alert
was correctly triggered, the overall accuracy of the NRT map reached
77.5%. Once the performance plateau was achieved, the overall accu-
racy increased to 84.0%. This accuracy gain was mainly attributed to the
reduction in commission errors for disturbance with the accumulation of

12

consecutive  observations,  as  the  correctly  labeled  “non-disturbance”
proportion increased from 0.763 to 0.834. It is worth noting that, for
simplicity, we used a consistent set of mapped area proportions derived
as  the  average  across  all  weekly  maps,  although  the  true  area  pro-
portions might vary with lag. For the site-based accuracy (Table S5 – S9
of the supplementary material), OA ranges from 68.5% (DX) to 83.2%
(SB) for the first-alert lag, and from 81.5% (YP) to 86.6% (SB) for the
level-off lag, which reflects that the accuracy for the level-off lag was
more spatially robust than that for first-alert lag.

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

4.3. Comparison with DIST-ALERT

Fig. 8 compares the lag-accuracy curves of binary disturbance maps
(disturbance vs. no-disturbance) generated by the proposed framework
with  those  from  the  DIST-ALERT  product.  Site-specific  lag-accuracy
curves are provided in Fig. S6 of the supplementary material. The pro-
posed approach shows a slightly longer first-alert lag than DIST-ALERT
(13.8 days vs. 10.1 days) but achieves substantially higher user's accu-
racy (UA: 73.9% vs. 57.1%), leading to an improved F₁ score (0.680 vs.
0.590).  For  the level-off  lag, the  proposed framework  demonstrates a
shorter lag (17.0 vs. 20.4 days) and consistently higher accuracy met-
rics, including UA (76.1% vs. 68.8%), producer's accuracy (PA: 72.0%
vs. 65.2%), and F₁ score (0.739 vs. 0.666). It should be noted that the lag
metrics derived from the binary maps differ slightly from the overall lags
reported in Section 4.2, which were calculated as weighted means across
the  three  disturbance  agents,  reflecting  differences  in  computational
procedures.  In  addition,  using  snapshot-based  confusion  matrices
adjusted  by  category  area  proportions  at  21  lag  days  (when  both
methods had saturated accuracies, see Table S4 and S10), our approach
still achieved a higher adjusted overall accuracy (86.26% vs. 81.74%,
see Table S11 and S12 of the supplementary material). It is noteworthy
that  DIST-ALERT  is  an  unsupervised  system  that  does  not  require
training-sample preparation, which improves operational flexibility but
may partially explain its lower detection accuracy relative to our tile-
calibrated, locally verified supervised framework.

Fig. 9 presents examples comparing the resultant disturbance maps
generated  by  the  proposed  framework  and  the  DIST-ALERT  product.
Overall, both approaches exhibit highly similar spatial patterns during
the first week following the disturbance (“W1-proposed” and “W1 DIST-
ALERT”), particularly for wildfire and logging due to their pronounced
stand-removal  signals.  However,  notable  differences  emerge  for  YN
stress  (Fig.  9C),  where  DIST-ALERT  missed  a  considerable  number  of
affected pixels. This discrepancy is likely attributable to differences in
baseline  estimation.  Specifically,  DIST-ALERT  estimates  baseline  con-
ditions  using  the  minimum  canopy  loss  observed  within  a  ± 15-day
temporal window over the preceding three years (Pickens et al., 2025),
which  may  introduce  uncertainties  associated  with  phenological
changes. In contrast, the CCDC-like approach compares each observa-
tion  with  its  modeled  baseline  reflectance  predicted  precisely  for  the
same  calendar  day,  thereby  minimizing  seasonal  bias.  Additionally,
DIST-ALERT tends to produce salt-and-pepper disturbance identification
that are likely commission errors (see C) YN stress), whereas the pro-
posed supervised framework integrates non-disturbance anomaly sam-
ples, effectively reducing false detections.

5. Discussion

total. This substantial improvement in efficiency arises from transferring
disturbance  agent  samples  from  CONUS  to  generate  a  preliminary
disturbance  patch  map  with  accurately  estimated  anomaly  dates,
thereby  minimizing  the  need  for  exhaustive  manual  delineation  and
temporal  interpretation  of  historical  disturbances.  Interpreters  were
only required to record the sample IDs for which they had high confi-
dence in the disturbance agent labels, based on time-series trajectories
and  three-year  HLS  imagery.  Consequently,  the  transferring-guided
strategy  combines  the  temporal  and  spatial  scalability  of  automated
sample  transfer  with  the  accuracy  of  expert  validation,  enabling  the
production of high-quality, representative local samples at a fraction of
the time and cost required by conventional manual annotation.

The  verified  patches  are  subsequently  converted  into  pixel-based
samples,  ensuring  sufficient  sample  numbers,  and  guaranteeing  mini-
mum representation even in regions where certain disturbance types are
relatively  rare.  Benefiting  from  random  and  spatially  even  sampling
across  the  region,  the  verified  pixel  samples  not  only  provide  a  pre-
liminary  estimate  of  local  cross-agent  proportions  but  also  support
proportional  allocation  across  disturbance  categories,
thereby
improving the representativeness of training datasets and enhancing the
performance of machine-learning models (Zhu et al., 2016). This design
is  particularly  advantageous  for  large-scale  monitoring  tasks,  where
accurate  class  proportion  and  spatial  distribution  are  critical  for  pre-
venting model bias and ensuring robust generalization across different
ecological and geographical contexts.

It is noteworthy that manual verification of the preliminary distur-
bance  agent  maps  remains  indispensable.  We  initially  attempted  to
directly apply CONUS-based samples to train disturbance agent classi-
fication models for China. However, the resultant map quality proved
unsatisfactory, even after strategically selecting the most representative
CONUS  samples  based  on  vegetation  and  topographic  similarity.  As
shown in Table S3 of the supplementary material, the high-confidence
rates for wildfire and stress categories were both below 10%. This lim-
itation  likely  arises  from  the  large  uncertainties  embedded  in  post-
disturbance  spectral  trajectories.  Variations  in  forest  management  re-
gimes, dominant vegetation species, and understory conditions between
China  and  United  States  can  substantially  modify  the  temporal  and
spectral  patterns  following  disturbances.  Additionally,  differences  in
climate regimes, disturbance intensity, and phenological cycles further
exacerbate  the  mismatch,  leading  to  reduced  model  transferability.
These factors are inherently difficult to quantify and harmonize across
regions at large spatial scales, making direct sample transfer insufficient
for accurate classification. Consequently, manual verification is a crit-
ical safeguard to mitigate geographic bias by converting the transferred
priors  into  locally  valid  training  data,  which  ultimately  improves  the
robustness of the final training dataset.

5.1. Transferring-guided local samples

5.2. Latency

High-quality  local  samples  are  essential  for  accurately  estimating
category proportions and detecting region-specific disturbances. Ideally,
these samples would be generated entirely from the study regions using
local  HLS time  series.  However,  in regions  where  comprehensive  his-
torical disturbance products are scarce (e.g., much of China), building a
representative  training  archive  from  scratch  would  require  extensive
manual interpretation over large areas and long time periods. A prag-
matic  alternative  is  to  label  only  a  small  number  of  representative
events, but this often leads to limited spatial and temporal coverage and
can bias the training data toward a few disturbance episodes. To address
this  limitation,  we  propose  a  transferring-guided  sample  generation
strategy  that  leverages  abundant  disturbance  products  available  in
CONUS to efficiently and consistently produce tile-specific local training
datasets in China. Compared with the existing studies (e.g., Wang et al.,
2025),  which  reported  an  interpretation  rate  of  approximately  18
disturbance  pixel  samples  per  hour,  our  approach  achieves  a  rate  of
~850 sample patches per hour, yielding about 30,000 sample pixels in

The  lag  time  for  mapping  disturbance  agents,  influenced  by  both
algorithmic and logistical factors, critically determines the effectiveness
of an NRT monitoring system. In this study, we reported two key lag
metrics,  namely  first-alert  and  level-off  lag,  to  evaluate  latency  and
model  performance  based  on  accuracy  metrics  at  corresponding  lag
times.  The  first-alert  lag,  representing  the  average  time  required  to
produce  a  correct  disturbance-agent  classification,  is  particularly
important  for  achieving  rapid  identification  of  disturbance  type  and
extent. Although the NRT scenario was conducted under a weekly up-
date scheme, the reported lag times in this study are still underestimated
by approximately two days in an operational context, due to the actual
delay in NASA's preprocessing of Landsat and Sentinel-2 imagery into
HLS products.

In  a  standard CCDC  workflow,  monitoring  typically  relies on  con-
firming a break and then re-initializing the model for the post-change
segment, which can delay NRT alerts because break confirmation and
re-initialization require multiple clear post-disturbance observations. In

13

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

contrast,  our  framework  decouples  anomaly  detection  from  break
confirmation and can issue disturbance alerts and agent attribution as
soon as the first clear post-disturbance observation is available (i.e., x =
1). Break detection is applied conservatively only for persistent struc-
tural changes, preserving temporal continuity and reducing unnecessary
resets  during  NRT  operation.  However,  compared  with  our  similar
approach but for NRT binary disturbance mapping (Ye et al., 2024), the
overall first-alert lag increased from 7.1 to 11.6 days under the same
assumption of ignoring data latency. Two factors likely contributed to
this increase. First, the previous evaluation was event-based (Ye et al.,
2024),  heavily  influenced  by  several  large  disturbance  events  (e.g.,
Hurricane  Ian  and  Mosquito  Wildfire),  whereas  the  validation  in  this
study  was  time-uniformly  sampled  throughout  the  year  rather  than
concentrated around major events. Second, the four-class agent classi-
fication  task  addressed  here  (wildfire,  logging,  stress,  and  non-
disturbance)  is  inherently  more  complex  than  the  binary  disturbance
detection problem, reducing the model's discriminative capacity during
the early phase of disturbance development. For binary detection, our
framework reported a longer first-alert lag than DIST-ALERT, reflecting
a  deliberate  trade-off  between  timeliness  and  commission-error  mini-
mization  achieved  by  our  incorporating  non-disturbance  anomaly
samples. The level-off lag represents the minimum lag time required to
achieve  stable  and  satisfactory  performance.  The  overall  level-off  lag
(15.5 days) was approximately four days longer than the first-alert lag,
accompanied  by  a  ~  7%  increase  in  OA.  Given  the  weekly  update
scheme,  these  results  indicate  that  our  approach  can  identify  most
disturbance  agents  by  the  second  week  following  disturbance  onset
(first-alert  lag)  and  achieve  a  satisfactory  overall  map  quality  by  the
third week (level-off lag). These lag times could be further reduced by
increasing the update frequency to daily, which, as reported by Ye et al.
(2024),  could  shorten  the  detection  lags  by  approximately  five  days.
Such daily updates are particularly recommended for emergent events,
where timeliness is given the highest operational priority.

Timeliness in an optical NRT monitoring system is also determined
by the availability of clear observations, because a disturbance can only
be detected after cloud free measurements are acquired. A recent global
evaluation of HLS 2.0 cloud free coverage suggest that the mid latitude
regions that include much of CONUS and our China study areas have
broadly comparable clear observation densities (Zhou et al., 2025). This
similarity  supports  the  feasibility  of  transferring  disturbance  samples
and applying an NRT framework originally developed and evaluated in
CONUS to China (Ye et al., 2024). Nevertheless, seasonal and regional
gaps  in  clear  observations  can  still  affect  a  CCDC-like  algorithm  by
reducing  valid  observations  available  for  model  updating  and  by
delaying the accumulation of consecutive anomalies. These effects can
increase  uncertainties  in  early-stage  agent  attribution  and  prolong
detection lag. We note that future integration of complementary sensors,
such  as  Sentinel-1  and  GF-2,  could  further  mitigate  temporal  gaps
attributed to cloud.

5.3. Transferability to other regions

For  regions  whose  vegetation  and  topography  conditions  are  well
represented in our CONUS archive, the sample-transfer step is expected
to be more effective because the transferred samples provide a strong
initialization  for  generating  preliminary  disturbance  maps  and  effi-
ciently  guiding  local  verification.  Transferability  may  be  reduced  in
environments  that  differ  substantially  from  CONUS,  such  as  humid
tropical regions, where persistent cloud cover and rapid vegetation re-
covery  can  alter  spectral–temporal  trajectories  and  weaken  agent
separability in optical data. In such cases, the workflow remains feasible,
but  it  would  likely  require  greater  local  verification  effort  and  the
incorporation  of  region-specific  disturbance  information  (e.g.,  fire
products,  concession  boundaries,  or  national  inventories)  to  build  a
more representative initial sample pool. Moreover, incorporating man-
agement  and  social-economic  datasets  could  further  improve  transfer

performance  for  anthropogenic  disturbances  (such  as  logging)  and
enable expansion of the current disturbance feature set.

A  second  challenge  in  transferring  to  other  regions  is  that  locally
dominant  disturbance  processes  (e.g.,  shifting  cultivation,  selective
logging, or mining) may require redefining the disturbance agent tax-
onomy.  For  example,  we  currently  aggregated  timber  harvest,  con-
struction,  and  forest  conversion  into  a  single  “logging”  class  because
these canopy-removal processes often exhibit similar early-stage spec-
tral responses in NRT optical observations. This aggregation can facili-
tate  transfer  to  regions  where  fine-grained  ancillary  information  is
limited, but it may constrain management-oriented interpretation when
more detailed attribution is needed. Future work will focus on devel-
oping  a  dynamic  classification  strategy  that  leverages  longer  post-
disturbance observation windows to refine causal attribution and bet-
ter differentiate disturbance agents across both similar and contrasting
environments.

5.4. Stress disturbances

Stress-related  disturbances  typically  produce  subtle  and  spatially
heterogeneous  spectral  responses,  which  makes  NRT  detection  inher-
ently more challenging than for abrupt stand-replacement events such as
fire or logging. Nevertheless, even when change magnitudes are small,
stress  often  exhibits  a  consistent  spectral  change  direction  (e.g.,  in-
creases in SWIR2 associated with canopy moisture loss), suggesting that
stress  signals  can  still  be  detectable  with  a  limited  number  of  post-
disturbance observations. In our results, the relatively low UA and PA
for stress (both <60% at the level-off lag; Fig. 7) reflect this intrinsic
difficulty and are further compounded by the lack of independent field
datasets that can reliably define a precise onset date for gradual decline
processes. However, stress is critically relevant for timely management
responses (e.g., prioritizing follow-up inspections or initiating suppres-
sion  in  the  case  of  pest  outbreaks),  especially  given  the  increasing
disturbance  pressure  under  climate  warming  (Seidl  et  al.,  2017).  We
therefore  retained  stress  in  the  monitoring  scope,  but  positioned  it
explicitly as an exploratory component aimed at providing early warn-
ing  of  canopy  condition  degradation.  Future  work  will  focus  on
improving  robustness  for  this  agent  through  integration  of  comple-
mentary data streams and constraints, such as climate anomalies, tar-
geted field samples, and pest reports.

6. Conclusion

This study presents a novel NRT framework for mapping disturbance
agents  across  China's  forests  using  the  Harmonized  Landsat  and
Sentinel-2 (HLS) dataset. By integrating transferring-guided local sam-
ple  generation,  stage-based  model  construction,  and  anomaly-level
detection, the proposed approach successfully identified major distur-
bance agents, i.e., wildfire, logging, and stress, within an average first-
alert  lag  of  approximately  12  days.  The  framework  effectively  over-
comes the long-standing limitation of scarce local training data through
an  efficient  transferring–guided  strategy,  which  substantially  reduced
manual labeling efforts while maintaining high sample reliability. The
stage-based models further enhanced the temporal sensitivity of agent
classification, enabling early and accurate identification of disturbances
with  diverse  spectral  trajectories.  Comparative  assessments  demon-
strated  that  the  approach  achieved  competitive  latency  and  slightly
better  accuracy  relative  to  existing  global  products  while  providing
more actionable insights through disturbance-agent attribution. These
findings  highlight  the  feasibility  of  operationalizing  fine-scale,  NRT
disturbance-agent monitoring across large regions and underscore the
potential for extending the framework to other forested regions globally.

CRediT authorship contribution statement

Ronghua Liao: Writing – review & editing, Writing – original draft,

14

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Visualization, Validation, Software, Methodology, Investigation, Formal
analysis, Data curation, Conceptualization. Chengcheng Guo: Valida-
tion,  Data  curation.  Lingkun  Chen:  Visualization,  Validation,  Data
curation. Yulin Jiang: Validation, Data curation. Yuchen Tao: Visual-
ization, Validation, Data curation. Jiani Liao: Data curation. Rui Lu:
Validation,  Data  curation.  Huaguo  Huang:  Visualization,  Validation,
Methodology,  Conceptualization.  Zhou  Shi:  Methodology,  Conceptu-
alization. Su Ye: Writing – original draft, Visualization, Writing – review
&
acquisition,

Supervision,  Methodology,

Funding

editing,
Conceptualization.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgements

The authors are grateful for the financial support provided by Na-
tional  Key  R&D
(2024YFF1306200;
of
2024YFF1306201)  and  Fundamental  and  Interdisciplinary  Disciplines
Breakthrough  Plan  of
the  Ministry  of  Education  of  China
(JYB2025XDXM909).

Program

China

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.

org/10.1016/j.rse.2026.115461.

Data availability

Data will be made available on request.

References

Andela, N., Morton, D.C., Schroeder, W., Chen, Y., Brando, P.M., Randerson, J.T., 2022.
Tracking and classifying Amazon fire events in near real time. Sci. Adv. 8, eabd2713.

Baig, M.H.A., Zhang, L., Shuai, T., Tong, Q., 2014. Derivation of a tasselled cap

transformation based on Landsat 8 at-satellite reflectance. Remote Sens. Lett. 5,
423–431.

Bullock, E.L., Healey, S.P., Yang, Z., Houborg, R., Gorelick, N., Tang, X., Andrianirina, C.,

2022. Timeliness in forest change monitoring: a new assessment framework
demonstrated using Sentinel-1 and a continuous change detection algorithm.
Remote Sens. Environ. 276, 113043.

Cao, P., Zang, Z., Zhang, M., Wang, X., Tang, X., Xiang, J., Tang, S., Wang, J., Zhang, Y.,
2025. Using LandTrendr to analyze forest disturbance, recovery, and attribution in
Hunan province from 2001 to 2024. Ecol. Indic. 176, 113712.

Chen, Xi, Zhao, W., Chen, J., Qu, Y., Wu, D., Chen, Xuehong, 2021. Mapping large-scale
forest disturbance types with multi-temporal CNN framework. Remote Sens. 13,
5177.

Cheng, K., Yang, H., Tao, S., Su, Y., Guan, H., Ren, Y., Hu, T., Li, W., Xu, G., Chen, M.,
2024. Carbon storage through China’s planted forest expansion. Nat. Commun. 15,
4106.

Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.-C., Skakun, S.V.,
Justice, C., 2018. The harmonized Landsat and Sentinel-2 surface reflectance data
set. Remote Sens. Environ. 219, 145–161.

Cohen, W.B., Yang, Z., Stehman, S.V., Schroeder, T.A., Bell, D.M., Masek, J.G., Huang, C.,
Meigs, G.W., 2016. Forest disturbance across the conterminous United States from
1985–2012: the emerging dominance of forest decline. For. Ecol. Manag. 360,
242–252.

Cui, W., Yang, L., Zhang, L., Yang, C., Zhu, C., Zhou, C., 2025. A novel approach of

generating pseudo revisited soil sample data based on environmental similarity for
space-time soil organic carbon modelling. Int. J. Appl. Earth Obs. Geoinf. 139,
104542.

Dee, L.E., Miller, S.J., Helmstedt, K.J., Boersma, K.S., Polasky, S., Reich, P.B., 2025.

Quantifying disturbance effects on ecosystem services in a changing climate. Nat.
Ecol. Evol. 1–12.

Hansen, M.C., 2024. OPERA Land Surface Disturbance Annual from Harmonized Landsat
Sentinel-2 Product (Version 1) [Data Set] [WWW Document]. NASA EOSDIS L.
Process. Distrib. Act. Arch. Cent. https://doi.org/10.5067/SNWG/OPERA_L3_DIST-
ANN-HLS_V1.001 (accessed 3.12.25).

Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S.,
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
using Landsat data. Environ. Res. Lett. 11, 34008.

15

Hawbaker, T.J., Vanderhoof, M.K., Schmidt, G.L., Beal, Y.-J., Picotte, J.J., Takacs, J.D.,
Falgout, J.T., Dwyer, J.L., 2020. The Landsat burned area algorithm and products for
the conterminous United States. Remote Sens. Environ. 244, 111801.

Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., 2015. Regional
detection, characterization, and attribution of annual forest change from 1984 to
2012 using Landsat-derived time-series metrics. Remote Sens. Environ. 170,
121–132.

Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., Campbell, L.B.,

2016. Mass data processing of time series Landsat imagery: pixels to data products
for forest monitoring. Int. J. Digit. Earth 9, 1035–1054.

Hou, G., Shen, X., Ge, S., Zhang, Y., Cao, L., 2025. A novel adaptive similarity-based

ecological niche model for the endangered Yunnan snub-nosed monkey
(Rhinopithecus bieti) using UAV LiDAR data. Remote Sens. Environ. 326, 114804.
Hu, T., Zhou, G., 2014. Drivers of lightning-and human-caused fire regimes in the great

xing’an mountains. For. Ecol. Manag. 329, 49–58.

Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust.

For. 71, 212–215.

Ju, J., Zhou, Q., Freitag, B., Roy, D.P., Zhang, H.K., Sridhar, M., Mandel, J., Arab, S.,

Schmidt, G., Crawford, C.J., Gascon, F., Strobl, P.A., Masek, J.G., Neigh, C.S.R.,
2025. The harmonized Landsat and Sentinel-2 version 2.0 surface reflectance
dataset. Remote Sens. Environ. 324, 114723. https://doi.org/10.1016/j.
rse.2025.114723.

Kennedy, R.E., Yang, Z., Braaten, J., Copass, C., Antonova, N., Jordan, C., Nelson, P.,

2015. Attribution of disturbance change agent from Landsat time-series in support of
habitat monitoring in the Puget Sound region, USA. Remote Sens. Environ. 166,
271–285.

Lin, Q., Huang, H., Chen, L., Wang, J., Huang, K., Liu, Y., 2021. Using the 3D model
RAPID to invert the shoot dieback ratio of vertically heterogeneous Yunnan pine
forests to detect beetle damage. Remote Sens. Environ. 260, 112475.

Oddo, P.C., Bolten, J.D., 2019. The value of near real-time earth observations for

improved flood disaster response. Front. Environ. Sci. 7, 127.

Olofsson, P., Foody, G.M., Herold, M., Stehman, S.V., Woodcock, C.E., Wulder, M.A.,
2014. Good practices for estimating area and assessing accuracy of land change.
Remote Sens. Environ. 148, 42–57.

Olsson, P.-O., Lindstr¨om, J., Eklundh, L., 2016. Near real-time monitoring of insect

induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote
Sens. Environ. 181, 42–53. https://doi.org/10.1016/j.rse.2016.03.040.

Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect
defoliation using Landsat time series. Forests. https://doi.org/10.3390/f8080275.

Pastick, N.J., Jorgenson, M.T., Goetz, S.J., Jones, B.M., Wylie, B.K., Minsley, B.J.,

Genet, H., Knight, J.F., Swanson, D.K., Jorgenson, J.C., 2019. Spatiotemporal remote
sensing of ecosystem change and causation across Alaska. Glob. Chang. Biol. 25,
1171–1189.

Perbet, P., Guindon, L., Cˆot´e, J.-F., B´eland, M., 2024. Evaluating deep learning methods
applied to Landsat time series subsequences to detect and classify boreal forest
disturbances events: the challenge of partial and progressive disturbances. Remote
Sens. Environ. 306, 114107.

Pickens, A.H., Hansen, M.C., Song, Z., Poulson, A., Komarova, A., Baggett, A., Kerr, T.,
Mikus, A., Ortiz Dominguez, C., Tyukavina, A., Lima, A., 2025. Rapid monitoring of
global land change. Nat. Commun. 16, 8948. https://doi.org/10.1038/s41467-025-
64014-9.

Qiu, S., Zhu, Z., Yang, X., Woodcock, C.E., Fahey, R.T., Stehman, S., Zhang, Y.,

Cullerton, M., Grinstead, A., Hong, F., Song, K., Suh, J.W., Li, T., Ren, W., Nemani, R.
R., 2025. A shift from human-directed to undirected wild land disturbances in the
USA. Nat. Geosci. 18, 989–996. https://doi.org/10.1038/s41561-025-01792-3.
Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving

near-real time deforestation monitoring in tropical dry forests by combining dense
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
204, 147–161.

Reymondin, L., Jarvis, A., Perez-Uribe, A., Touval, J., Argote, K., Rebetez, J., Guevara, E.,
Mulligan, M., 2012. Terra-I: A Methodology for near Real-Time Monitoring of
Habitat Change at Continental Scales Using Modis-ndvi and trmm. CIAT-Terra-i.
Ryan, K.C., Opperman, T.S., 2013. LANDFIRE–A national vegetation/fuels data base for
use in fuels treatment, restoration, and suppression planning. For. Ecol. Manag. 294,
208–216.

Sarre, A., 2020. Global forest resources assessment, 2020: Main report. Food and

Agriculture Organization of the United Nations.

Schroeder, T.A., Schleeweis, K.G., Moisen, G.G., Toney, C., Cohen, W.B., Freeman, E.A.,

Yang, Z., Huang, C., 2017. Testing a Landsat-based approach for mapping
disturbance causality in US forests. Remote Sens. Environ. 195, 230–243.
Seidl, R., Schelhaas, M.-J., Rammer, W., Verkerk, P.J., 2014. Increasing forest

disturbances in Europe and their impact on carbon storage. Nat. Clim. Chang. 4,
806–810.

Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Nat. Clim. Chang. 7, 395–402.

Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time

monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data.
Remote Sens. Environ. 278, 113073.

Shimizu, K., Ahmed, O.S., Ponce-Hernandez, R., Ota, T., Win, Z.C., Mizoue, N.,

Yoshida, S., 2017. Attribution of disturbance agents to forest change using a Landsat
time series in tropical seasonal forests in the Bago Mountains, Myanmar. Forests 8,
218.

Silva, C.D.R., Olthoff, A.E., de la Mata, J.A.D., Alonso, A.P., 2013. Remote monitoring of

forest insect defoliation. A review. For. Syst. 22, 377–391.

R. Liao et al.

Remote Sensing of Environment 342 (2026) 115461

Slagter, B., Reiche, J., Marcos, D., Mullissa, A., Lossou, E., Pe˜na-Claros, M., Herold, M.,
2023. Monitoring direct drivers of small-scale tropical forest disturbance in near
real-time with Sentinel-1 and-2 data. Remote Sens. Environ. 295, 113655.

Stahl, A.T., Andrus, R., Hicke, J.A., Hudak, A.T., Bright, B.C., Meddens, A.J.H., 2023.
Automated attribution of forest disturbance types from remote sensing data: a
synthesis. Remote Sens. Environ. 285, 113416.

Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
monitoring of tropical forest disturbance: new algorithms and assessment
framework. Remote Sens. Environ. 224, 202–218.

Tang, X., Bratley, K.H., Cho, K., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2023. Near
real-time monitoring of tropical forest disturbance by fusion of Landsat, Sentinel-2,
and Sentinel-1 data. Remote Sens. Environ. 294, 113626.

Thom, D., Seidl, R., 2016. Natural disturbance impacts on ecosystem services and

biodiversity in temperate and boreal forests. Biol. Rev. 91, 760–781.

Tyukavina, A., Hansen, M.C., Potapov, P.V., Stehman, S.V., Smith-Rodriguez, K.,

Okpa, C., Aguilar, R., 2017. Types and rates of forest disturbance in Brazilian legal
Amazon, 2000–2013. Sci. Adv. 3, e1601047.

Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using

satellite image time series. Remote Sens. Environ. 123, 98–108.

Verleysen, M., François, D., 2005. The curse of dimensionality in data mining and time
series prediction. In: International Work-Conference on Artificial Neural Networks.
Springer, pp. 758–770.

Wang, L., Liu, S., Song, W., Zhang, J., Ding, S., 2025. Global high-resolution forest

disturbance type dataset. Earth Syst. Sci. Data Discuss. 2025, 1–23.

Wheeler, D., Hammer, D., Kraft, R., Steele, A., 2014. Satellite-Based Forest Clearing

Detection in the Brazilian Amazon.

Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,

Gao, F., Goward, S.N., Helder, D., Helmer, E., 2008. Free access to Landsat imagery.
Science 320, 1011.

Wu, Z., He, H.S., Keane, R.E., Zhu, Z., Wang, Y., Shan, Y., 2019. Current and future
patterns of forest fire occurrence in China. Int. J. Wildland Fire 29, 104–119.
Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
LCMAP collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
143–162.

Xu, Q., Zhang, X., Li, J., Ren, J., Ren, L., Luo, Y., 2023. Pine wilt disease in northeast and

Northwest China: a comprehensive risk review. Forests 14, 174.

Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
dense Landsat time series: case studies of mountain pine beetle and spruce beetle
disturbance. Remote Sens. Environ. https://doi.org/10.1016/j.rse.2021.112560.
Ye, S., Zhu, Z., Suh, J.W., 2024. Leveraging past information and machine learning to
accelerate land disturbance monitoring. Remote Sens. Environ. 305, 114071.

Zhang, Y., Woodcock, C.E., Chen, S., Wang, J.A., Sulla-Menashe, D., Zuo, Z., Olofsson, P.,

Wang, Y., Friedl, M.A., 2022. Mapping causal agents of disturbance in boreal and
arctic ecosystems of North America using time series of Landsat data. Remote Sens.
Environ. 272, 112935.

Zhang, B., Cai, D., Ai, S., Wang, H., Zuo, X., 2023. Research on the influencing factors
and prevention measures of long-term forest fire risk in Northeast China. Ecol. Indic.
155, 110965.

Zhao, F., Liu, Y., Shu, L., 2020. Change in the fire season pattern from bimodal to

unimodal under climate change: the case of Daxing’anling in Northeast China. Agric.
For. Meteorol. 291, 108075.

Zhong, Z., He, B., Chen, Y., Yuan, W., Huang, L., Guo, L., Zhang, Y., Xie, X., 2021. Higher
sensitivity of planted forests’ productivity than natural forests to droughts in China.
J. Geophys. Res. Biogeosci. 126, e2021JG006306.

Zhou, Q., Neigh, C.S.R., Ju, J., Dabney, P., Cook, B., Zhu, Z., Crawford, C.J., Gascon, F.,

Strobl, P., Sridhar, M., 2025. Towards seamless global 30-meter terrestrial
monitoring: evaluating 2022 cloud free coverage of harmonized Landsat and
Sentinel-2 (HLS) V2.0. IEEE Geosci. Remote Sens. Lett. 22, 1–5.

Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
Zhu, Z., Woodcock, C.E., Holden, C., Yang, Z., 2015. Generating synthetic Landsat

images based on all available Landsat data: predicting Landsat surface reflectance at
any given time. Remote Sens. Environ. 162, 67–83.

Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
data for operational land cover classification for the LCMAP initiative. ISPRS J.
Photogramm. Remote Sens. 122, 206–221.

Zhu, A., Lu, G., Liu, J., Qin, C., Zhou, C., 2018. Spatial prediction based on third law of

geography. Ann. GIS 24, 225–240.

Zhu, A.-X., Miao, Y., Liu, J., Bai, S., Zeng, C., Ma, T., Hong, H., 2019a. A similarity-based
approach to sampling absence data for landslide susceptibility mapping using data-
driven methods. Catena 183, 104188.

Yang, J., Huang, X., 2021. 30 m annual land cover and its dynamics in China from 1990

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2019b.

to 2019. Earth Syst. Sci. Data Discuss. 2021, 1–29.

Yang, L., Meng, X., Zhang, X., 2011. SRTM DEM and its application advances. Int. J.

Remote Sens. 32, 3875–3896.

Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
forest disturbance using Landsat time series: stochastic continuous change detection.
Remote Sens. Environ. https://doi.org/10.1016/j.rse.2020.112167.

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. https://doi.org/10.1016/j.rse.2019.03.009.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. 238, 111116.

Zhu, Z., Qiu, S., Ye, S., 2022. Remote sensing of land change: a multifaceted perspective.

Remote Sens. Environ. 282, 113266.

16
