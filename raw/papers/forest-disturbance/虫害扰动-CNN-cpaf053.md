Forestry: An International Journal of Forest Research, 2026, 99, 1–14

https://doi.org/10.1093/forestry/cpaf053
Advance access publication date 11 September 2025
Original Article

Early detection of bark beetle infestations in Central
Europe using deep learning–based reconstructions of
irregular Sentinel-2 time series

Christopher Schiller

1,*, Johannes May2, Randolf Klinke3, Fabian Ewald Fassnacht1

1Remote Sensing and Geoinformatics, Institute of Geographical Sciences, Freie Universität Berlin, Malteserstrasse 74-100, 12249 Berlin, Germany
2State Enterprise for Forestry and Timber North Rhine-Westphalia, Albrecht-Thaer-Straße 34, 48147 Münster, Germany
3LUP - Luftbild Umwelt Planung GmbH, Große Weinmeisterstraße 3a, 14469 Potsdam, Germany

*Corresponding author. Remote Sensing and Geoinformatics, Institute of Geographical Sciences, Freie Universität Berlin, Malteserstrasse 74-100, 12249 Berlin,
Germany. E-mail: christopher.schiller@fu-berlin.de

Abstract

Norway spruce (Picea abies) is among the most abundant tree species in Central Europe. Due to climate change-induced extreme weather
events, spruce trees are increasingly stressed and therefore threatened by European spruce bark beetle (Ips typographus) infestations.
Recent mass outbreaks led to severe ecological and economic damage in Central European forests. After an infestation, the filial
generation of the beetles swarms out within 6 to 10 weeks to infest new trees. Consequently, an efficient bark beetle management needs
to remove infested trees within 10 weeks to prevent further dispersal. While remote sensing allows for large-scale monitoring of forests,
the detection of bark beetle infestations remains challenging, as many trees show no visible signs of the infestation within the 10-week
detection period. Here, we try to achieve early detections by adjusting a state-of-the-art Deep Learning model to be able to cope with
irregular Sentinel-2 satellite time series for reconstruction-based anomaly detection. The model is trained on >300 000 time series of
undisturbed coniferous forest and the threshold denoting an anomaly is derived independently, i.e. not from the test dataset. We test the
model on a geographically independent dataset with known infestation dates. It achieves moderate performance for detections within
10 weeks after the infestation with a producer’s accuracy (PA) of 11.8% ± 8.4% and user’s accuracy (UA) of 43.5% ± 24.5% across three
model runs, but yields very good results when extending the detection period to 13 weeks (UA = 84.5% ± 7.6%, PA = 81.5% ± 1%). Since
the model responds immediately to an anomaly, we conclude that area-wide bark beetle detections within 10 weeks after infestation
are likely impossible using Sentinel-2 alone. Still, our approach can readily be used as a near real-time monitoring system for coniferous
forest, be applied on any forest disturbance detection task, and may complement terrestrial surveys in the future.

Keywords: remote sensing; anomaly detection; deep learning; bark beetle; disturbance; early detection

Introduction

One of the most abundant tree species in Central European
forests is Norway spruce (Picea abies L.) (Caudullo et al. 2016),
which is often planted in monocultures for timber production.
Norway spruce is regularly subject to insect infestations, par-
ticularly by the European spruce bark beetle (Ips typographus
L., in the following: “bark beetle”). Bark beetles benefit from
warm and dry weather conditions, allowing them to complete
their life cycles more rapidly. As the frequency and intensity
of extreme weather events is increasing due to climate change
(García-Herrera et al. 2019, Grillakis 2019, Ionita and Nagavciuc
2021), trees are increasingly stressed and their defense mecha-
nisms are weakened. This further promotes bark beetle outbreaks,
which are currently becoming more frequent and severe (Senf
et al. 2017, Netherer et al. 2019, Patacca et al. 2022). Severe bark
beetle infestations have led to mass dieback events (e.g. Harz
National Park and Saxon Switzerland National Park in Germany)
with significant ecological and economic consequences (Schiefer

et al. 2024), which also induced a shift in the species composition
in some parts of Central Europe. For instance, the area stocked
with spruce in Germany has decreased by ∼17% between 2012
and 2022, much of which is attributed to bark beetle outbreaks
(Federal Ministry of Food and Agriculture (BMEL) 2024).

During the first few months after an initial bark beetle infesta-
tion, the crowns of spruce trees usually remain green (green attack
stage) (Ortiz et al. 2013, Kautz 2014). In the green attack stage, the
bark beetles establish maternal and brood galleries in the phloem
of the tree. The boring beetles also enable wood-degrading fungi to
penetrate into the tree (Künniger et al. 2024), which then colonize
the sapwood within a few weeks (Solheim 1992). The fungal
growth disrupts the water transport through the xylem of the
tree (Kirisits and Offenthaler 2002), impairing the tree’s defense
mechanism of resin production and water transport capabilities.
Meanwhile, the beetles lay eggs, which evolve as larvae, pupae and
finally beetles, continuously feeding on the phloem of the trees.
This leads to a disruption of the nutrient transport in the phloem
and consecutively to further breakdown of the tree’s defense

Handling editor: Prof. Teja Kattenborn
Received 12 March 2025; revised 25 June 2025; accepted 15 August 2025
© The Author(s) 2025. Published by Oxford University Press on behalf of the Institute of Chartered Foresters. All rights reserved. For commercial re-use, please
contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the
Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com.

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

2 | Schiller et al.

mechanisms, followed by fine root mortality, which reduces the
ability of the tree to provide water and nutrients to its organs.
Consequently, the conditions for conducting photosynthesis no
longer occur, and the tree dies. After the green attack stage, the
needles turn red (red attack) and are finally shed (gray attack).

The subdivision into green, red, and gray attack, however, is
not necessarily relevant for forest managers. Since the new filial
generation swarms out to infest new trees ∼6 to 10 weeks after
the initial infestation (depending on environmental conditions,
tree health, etc.) (Kautz et al. 2024), an early detection (before
the emergence of the new beetle generation) is crucial to apply
efficient mitigation measures such as sanitation felling and log
removal. Thus, the time frame for a successful early detection
in the sense of forest management usually ends 10 weeks after
infestation, while the trees are typically still in the green attack
stage.

The urgently needed monitoring of early bark beetle infesta-
tions has been relying on regular field visits, but also remote
sensing approaches have been explored. On the ground, sniffer
dogs can be trained to smell the pheromones excreted by the bee-
tles during tree colonization (Voˇsvrdová et al. 2023). Additionally,
trained human observers can identify infested trees by observing
boring dust, entrance holes, woodpecker-caused loosened bark
patches, and the beetles themselves (Kautz et al. 2023). While
these ground observations achieve satisfactory performance in
experiments (Kautz et al. 2023), this method is labor-intense and
hardly feasible to be applied systematically across wide areas.

As opposed to that, remote sensing is a good option to monitor
large areas efficiently. As stated above, the trees are deprived of
water supply during the green attack stage (Kautz et al. 2024). This
inevitably leads to water stress symptoms such as a reduced leaf
water content and is followed by deterioration of the cell structure
(Kautz et al. 2024). While early symptoms usually do not show
a strong spectral response in the human-visible wavelengths
(hence the term green attack), they are often detectable in wave-
lengths captured by multi- or hyperspectral sensors (Abdullah
et al. 2018) such as multispectral satellites (Abdullah et al. 2019).
For instance, satellite bands in the shortwave infrared (SWIR)
wavelength range are usually sensitive to water content of the
vegetation’s leaf tissue (Ustin et al. 2004, Kokaly et al. 2009)
and wavelengths in the red-edge and near infrared (NIR) range
respond to changes in leaf cell structure.

Consequently, many remote sensing studies have shown the
spectral separability between undisturbed and infested (green
attack) spruce trees. For instance, Ortiz et al. (2013) use data from
the multispectral RapidEye satellite with a spatial resolution of
6.5 m to distinguish between undisturbed and green attack spruce
trees ∼8 weeks after infestation. Another study uses WorldView-
2 with a spatial resolution of 2 m to classify undisturbed and
green attack trees (Immitzer and Atzberger 2014). Many studies
also tested the capability of Sentinel-2 (S2) for early detections
of bark beetle infestations (e.g. Bárta et al. 2021, Huo et al. 2021,
Dalponte et al. 2022, and Mandl and Lang 2023).

While most of these studies indicate measurable spectral dif-
ferences between green attack and undisturbed trees, the model
performances achieved so far are not yet sufficient for an efficient
monitoring (Kautz et al. 2024). On top of that, most studies so
far focused on small study areas (e.g. Abdullah et al. 2019, Bárta
et al. 2021, Mandl and Lang 2023), sometimes a single forest stand
and a single image acquisition (e.g. Ortiz et al. 2013, Minaˇrík et al.
2021). Therefore, it is unclear if the obtained results can be gener-
alized across larger regions for a large-area application. Addition-
ally, most of these studies use data from commercial satellites

(e.g. RapidEye in Ortiz et al. 2013, WorldView-2 in Immitzer and
Atzberger 2014), which are associated with costs, or exploit UAV
acquisitions (e.g. Minaˇrík et al. 2021), which are laborious to
collect. Regarding freely available multispectral satellite imagery,
the best current option is S2 from the European Space Agency due
to its high spatial resolution of 10 m and a revisit time of ∼5 days.
The temporal resolution of satellite systems such as S2 allows
for a monitoring approach using time series anomaly detection.
Yet, the temporal trends of satellite time series of forests can
be complex due to diverse physiological responses of the trees
to a multitude of environmental inf luences (e.g. disturbances,
meteorological anomalies, environmental conditions, and stand
properties), which in turn manifest in different spectral responses.
On top of that, satellite time series are often noisy, e.g. due to
atmospherical effects, which can lead to false detections. Conse-
quently, a simple threshold ref lectance value for anomaly detec-
tion cannot distinguish undisturbed from disturbed forest. There-
fore, more advanced methods have been developed for anomaly
detection using satellite time series, e.g. CCDC (Zhu and Woodcock
2014), its successor for near real-time (NRT) monitoring S-CCD
(Ye et al. 2021), and BFAST Monitor (Verbesselt et al. 2012). While
having shown promising results in land cover change monitor-
ing, these methods rely on predefined functions or statistical
assumptions about the time series. For instance, they assume that
the processes affecting the spectral time series can be described
by linear and/or seasonal trends. Consequently, they might not
fully capture the complex, nonlinear relationships characteristic
of ecological processes.

Studies specifically focusing on early detection of bark beetle
infestations using S2 time series suggest that it is possible to some
extent. However, their results cannot be directly applied in an
operational system. Some studies, for instance, use information
from the end of the study period to investigate detection capa-
bilities in retrospect (Dalponte et al. 2022, Mandl and Lang 2023),
which prevents NRT monitoring. Other studies investigating the
early detection of bark beetle infestations on satellite time series
use advanced Machine Learning (ML) techniques to improve clas-
sification of undisturbed and infested pixels (Bárta et al. 2021,
Huo et al. 2021, Dalponte et al. 2022). While these models, e.g.
Random Forest (RF) or Support Vector Machines, are generally
capable of processing feature vectors derived from multitempo-
ral observations, they do not inherently capture the temporal
dependencies and long-range temporal dynamics of satellite time
series. In other terms, they treat each feature independently and
are not designed to capture that an observation at timestep t
chronologically follows the observation of timestep t − 1.

Deep Learning (DL), a sub-class of ML, has evolved as a promis-
ing tool in remote sensing of forests (e.g. Schiefer et al. 2020,
Minaˇrík et al. 2021, Schwarz et al. 2024). Recent studies also
indicate its high potential in time series analysis, e.g. by for-
est disturbance classification (Du et al. 2023, Perbet et al. 2024,
Schiller et al. 2024) and standing deadwood estimation (Schiefer
et al. 2023). However, NRT monitoring that aims at early detec-
tion of disturbances in forest remote sensing using DL models
has still not been tested widely. One NRT approach is anomaly
detection using time series reconstructions. Here, we propose a
model to reconstruct time series of S2 pixels representing undis-
turbed forest exclusively. Being fitted on undisturbed forest’s time
series only, the model is unable to reconstruct a time series of
a disturbed forest’s pixel, which leads to a difference between
reconstruction and observation. This anomaly can be interpreted
as a deviation from the undisturbed state, meaning that it must
be a disturbed forest’s pixel. While this approach has been tested

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Table 1. Meta information about the datasets used in this study

Dataset

Region

Training/
test

Labels

Number of
samples

Undisturbed/
infested

Max. time
frame

Early detection of bark beetle infestations in Central Europe | 3

Own work: AUS
Own work: BB
Own work: SAX
Own work: THU Thuringia, Germany
Own work: RLP

Tyrol, Austria
Brandenburg, Germany
Saxony, Germany

FNEWS LoSa
FNEWS Sax
FNEWS BW1

FNEWS BW2

Lux
AF (Arnsberg
Forest)

Rhineland-Palatinate,
Germany
Lower Saxony, Germany
Saxony, Germany
Baden-Württemberg,
Germany
Baden-Württemberg,
Germany
Luxembourg
North Rhine-Westphalia,
Germany

Training
Training
Training
Training
Training

Training
Training
Training

Visual interpretation of orthophoto
Visual interpretation of orthophoto
Visual interpretation of orthophoto
Visual interpretation of orthophoto
Visual interpretation of orthophoto

Visual interpretation of orthophoto
Visual interpretation of orthophoto
Visual interpretation of orthophoto

5051
13 041
13 760
11 712
963

22 186
12 073
95 560

Undisturbed
Undisturbed
Undisturbed
Undisturbed
Undisturbed

Undisturbed
Undisturbed
Undisturbed

[2018, 2021]
[2018, 2021]
[2018, 2021]
[2018, 2021]
[2017, 2020]

[2016, 2018]
[2016, 2019]
[2016, 2017]

Training

Visual interpretation of orthophoto

61 448

Undisturbed

[2016, 2019]

Training
Test

Visual interpretation of orthophoto
Ground observation

96 159
4939
(undisturbed) 351
(infested)

Undisturbed
Undisturbed,
infested

[2016, 2019]
[2017, 2021]

Max. time frame refers to the years of Sentinel-2 data contained in the time series of the corresponding dataset.

successfully in anomaly detection in other fields of research (Wu
et al. 2023), it is still novel in remote sensing to the best of our
knowledge.

Accordingly, in this study we tested a reconstruction-based DL
anomaly detection method on S2 time series for its capability
of early detections of bark beetle outbreaks in spruce forest in
Central Europe. To this aim, we adjusted a state-of-the-art model
architecture to be able to cope with irregular time series and thus
avoid interpolation and resampling. We acquired >300 000 S2 time
series of undisturbed forest in Germany, Austria, and Luxembourg
for model training. We trained our model on training sites located
far away from the test study site in order to investigate if the
approach can be generalized across regions. The latter is still an
open challenge and a strong limitation of most former studies
on early bark beetle infestation detection (Marvasti-Zadeh et al.
2023). Additionally, most other studies focus on detecting the
green attack stage after infestation, which is not relevant for
forest management (see above). Here, we explicitly investigate
how many weeks after infestation are needed to detect a bark
beetle infestation. In case of adequate performance, such a model
could readily be applied to Central European spruce forests using
the freely available S2 data to finally enable an operational NRT
monitoring system of early bark beetle infestations.

Methods
Training dataset preparation
In this study, we use pixels representing undisturbed forest for
training and pixels representing both undisturbed as well as bark
beetle–infested forest for testing (for an overview, see Table 1 and
Fig. 1). We compiled multiple datasets from different publica-
tions and sources for model training. These comprise data from
Langner et al. (2023) (in the following “FNEWS”), from Schwarz
et al. (2024) (in the following “Lux”), and from Schiller et al.
(2024) (in the following “own work”: RLP, BB, THU, SAX). The first
author of the present paper additionally labeled one study site
in Austria (“own work”: AUS). All of these datasets contain forest
disturbance information. In case of our own work (RLP, BB, THU,
SAX, AUS), we removed the forest disturbance areas (dieback and
logging) including a buffer of 15 m from all forested areas. Lux
contains visually interpreted dieback areas and no forest mask.

Here, we utilized the official forest land use as well as dieback
and logging information from the Cadastral and Topographic
Administration (Administration du cadastre et de la topographie,
ACT; www.geoportail.lu) of Luxembourg including a buffer of 15 m
to remove non-forest as well as disturbed (logging and dieback)
areas. FNEWS comprised only forest areas, so a forest mask was
not necessary. Here, we discarded all but the polygons denoted as
undisturbed. We further discarded all but the coniferous forest
pixels from all datasets as determined by the forest type charac-
terization of the Copernicus Land Monitoring Service or, in case
of Lux, by the official forest type information from the Cadastral
and Topographic Administration of Luxembourg. All S2 pixels
located entirely within the remaining coniferous forest areas were
assumed to show time series of undisturbed forest and, thus, their
time series were sampled as training data from the S2 datacube
as described in Section Time Series Acquisition.

Test dataset preparation
For model testing, we needed spatially and temporally explicit
data about bark beetle infestations as well as a control group
(undisturbed areas). The former was obtained from Wald und Holz
NRW (North Rhine-Westphalia; in the following “AF”; data collec-
tor: J.M.) in or near Arnsberg Forest in North Rhine-Westphalia,
Germany, within the scope of the FirSt 2.0 project. AF contains
both undisturbed and infestation information, all infested and
undisturbed data being located within a range of 45 km from the
city of Arnsberg (Fig. 2).

The 78 undisturbed polygons consist of monocultural stands
of Norway spruce that have been confirmed to be undisturbed
and green by 14 June 2021 by the local foresters. For the infested
polygons, ground observations were conducted every 2 weeks
within the study period in the Arnsberg Forest in an area of
∼2.5 × 2.5 km. In this area, only a few spruce stands were still alive
and uninfested in 2021. Thus, it was feasible to scan every single
spruce tree for signs of bark beetle infestations in the study period.
After detection of these signs (e.g. saw dust, bore holes, devel-
opmental stage under bark, beetles themselves), areas of similar
developmental stage of the bark beetles were determined by
screening each tree. The polygons delineating the canopy areas of
the infested trees were derived using in-field GPS measurements
and delineated and checked using GIS software. The infestation

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

4 | Schiller et al.

Figure 1. Spatial distribution of datasets used in this study, spanning the countries Luxembourg (Lux), Austria (own work), and Germany (own work,
FNEWS, AF). Center point of each circle on the map is located at the centroid of the corresponding dataset. Training datasets are indicated by solid,
test dataset by dotted outline. Map on the top right shows an overview of the study countries (Lux: Luxembourg; Ger: Germany; Aus: Austria). Point
sizes are scaled proportionally to the square root of the number of samples to accurately represent data magnitude while accounting for perceptual
bias. Coordinate reference system EPSG:3035.

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Figure 2. Overview of test area (A) and detailed map of infestation monitoring area (B) of the test dataset AF. For orientation, larger cities are shown by
star symbols and nature parks are visualized by polygons (Arnsberg Forest in the north and Sauerland-Rothaargebirge in the south). Coordinate
reference system: EPSG:3035. Digital orthophotos courtesy of open.NRW (dl-zero-de/2.0).

date could then either be inferred directly (e.g. when the bark
beetles were freshly boring into the bark; 6 polygons) or estimated
depending on the detected developmental stage of the bark bee-
tles for certain areas (5 polygons). Thus, the temporal information
of the bark beetle infestations could be inferred precisely, likely
achieving an uncertainty of only a few days. In the following, we
assume the day inferred by this procedure based on the field visits
as the infestation date. For this study, we used only those polygons
that have not been harvested until 14 weeks after the presumed
infestation date, as including clearings would likely lead to an
overestimation of model performance. We also excluded all S2
pixels that were not fully covered by the disturbance polygons.
Details about the undisturbed and infested datasets of AF are
provided in Table 2. As visible in Fig. 1, training and test data

do not overlap and are far away from each other, enabling an
external validation that investigates the model’s capability of
generalization across regions.

Time series acquisition
For each S2 pixel sampled as described in the previous sections,
we acquired a time series from an S2 datacube preprocessed
with the Framework for Operational Radiometric Correction for
Environmental Monitoring (FORCE; Frantz 2019). The Level 2A
data derived from FORCE have been atmospherically and topo-
graphically corrected and the two S2 satellites S2A and S2B have
been co-registered. The latter is crucial for time-series analysis
as it is necessary to ensure that the ref lectance of the same
geolocation is sampled at each timestep. Otherwise, the concept of

Early detection of bark beetle infestations in Central Europe | 5

Table 2. Information on AF dataset used for testing, including number of polygons and pixel count of both undisturbed and infested
datasets as well as infestation date range of infested dataset

Subset

Undisturbed
Infested

Number of
polygons

78
11

Number of pixels per polygon
(min; mean; median; max)

Infestation date range

1; 63; 29; 603
1; 32; 19; 155

28 May 2021 to 3 August 2021

change detection would not be feasible. Furthermore, the FORCE
Level 2A product has been cleared of clouds, cloud shadows, snow,
and other potential artifacts. All S2 bands have been resampled to
10 m spatial resolution using the ImproPhe algorithm implemented
in FORCE. The datacube for Germany was readily available on
the platform www.eo-lab.org, while the datacubes for Austria and
Luxembourg were processed using the same FORCE parameters
using our own computational resources.

As we pursue NRT monitoring, high-quality data are of utmost
importance since any low-quality observation such as a cloud that
has been missed by the cloud masking algorithm could poten-
tially lead to an anomaly, which then triggers a false warning.
Prioritizing quality over quantity, we used the quality assurance
information from FORCE to further exclude observations from
analysis when f lagged as cloud (opaque, cirrus), cloud shadow,
snow, water, high or unknown aerosol optical depth, and others.
FORCE uses an improved fmask algorithm to detect clouds (Frantz
et al. 2018).

The model was provided with univariate time series of the
CRSWIR (continuum removal shortwave infrared) VI as input. It is
computed using the narrow NIR (B8a), SWIR1 (B11), and SWIR2
(B12) bands of S2. The equation to compute CRSWIR is

CRSWIR =

(cid:2)

B11
(cid:3)

B8a +

B12−B8a
λB12−λB8a

× (λB11 − λB8a)

(1)

where λBn denotes the S2 wavelength of the corresponding band
in nanometers and Bn represents the observed ref lectance of the
corresponding S2 band. Using this equation, a straight line (the
continuum) is drawn between the NIR and SWIR2 band. Next, the
SWIR1 ref lectance is compared to the continuum value at the
SWIR1 wavelength. Thus, the deviation of SWIR1 to this contin-
uum is measured, specifically highlighting the ref lectance of the
forest in the SWIR1 spectral range, which is sensitive to changes
in water content of the vegetation (Ustin et al. 2004, Kokaly et al.
2009). Since reduced leaf water content is an early symptom of
bark beetle infestations in spruce trees and SWIR1 is sensitive to
vegetation moisture and bark beetle green attacks (Abdullah et al.
2018), the CRSWIR index is particularly suitable for early detection
of bark beetle infestations (Dutrieux et al. 2021). We also tested
other VIs suggested by, for instance, Abdullah et al. (2019), König
et al. (2023), and Mandl and Lang (2023). As they resulted in much
lower model performance, we do not report their results in this
study.

All datasets used in this study are temporally explicit, meaning
that the date of image acquisition and the date of ground obser-
vation of the bark beetle status of the trees were both known for
the training and validation data, respectively. This was necessary
to allow the acquisition of undisturbed (and non–green attacked)
time series in training and validation, and to enable measuring
the detection delay. The time series were acquired according to
the following scheme: for undisturbed pixels, the end date was
defined as 31 December of the year prior to the observation date,

while for infested pixels, the end date was set to 31 December of
the same year. As infested spruce trees usually express mortality
within 1 year, this guaranteed that the time series did not contain
an early stage of bark beetle infestations that was not yet visible in
the orthophoto (green attack). The dates of image acquisition for
the training data can be inferred from the original publications,
see Schiller et al. (2024) and Langner et al. (2023). The maximum
length of the time series was set to four years and only full years
were used, meaning that the time series always started at the
first observation of the corresponding Gregorian calendar year.
The earliest start date was set to 1 January 2016, as 2016 is the
first year with S2 coverage from the beginning of the calendar
year. Thus, the resulting time series exhibited a length between
two and four years (cp. Table 1).

Reconstruction-based time series anomaly
detection
There are multiple ways to approach NRT change detection in
time series using DL, e.g. short-term forecasting, meaning that the
model predicts future observations, which are then compared to
real observations once the latter are acquired. In this study, we
tried a reconstruction-based approach that works as follows: the
model is trained to reconstruct a given (here: univariate) time
series, i.e. it attempts to learn the patterns underlying each of
the time series and then reproduces them as close as possible,
optimized by a loss function (here: mean squared error between
observations and reconstructions). Therefore, the input and out-
put of the model is a time series: input are the observations,
output are the reconstructions/predictions.

During the training phase, the model is only exposed to non-
anomalous time series, derived from pixels of fully undisturbed
forest in our case. Thereby, the model learns patterns (represen-
tations) of undisturbed time series. As opposed to that, during
the test phase the model receives both anomalous and non-
anomalous time series as input. As the model learned only pat-
terns from S2 time series of undisturbed forest, it would be unable
to reconstruct disturbed (anomalous) time series. Consequently,
the reconstructions and the observations diverge beginning at
the timestep at which the anomaly starts. This discrepancy can
be measured and classified as an anomaly if exceeding a user-
defined threshold.

TimesNet model
In this study, we used the anomaly detection module of the Times-
Net model (Wu et al. 2023) to reconstruct the input time series.
TimesNet has shown state-of-the-art performance on benchmark
datasets across all time series analysis tasks, including anomaly
detection (Wu et al. 2023). The principle of this model architecture,
which uses the concept of Convolutional Neural Networks (CNNs)
as main building block, along with our adjustments to it are
explained in the following.

First, the input time series are embedded into a latent space by
two embedding modules: a 1D-convolutional layer provides links
between the input channels, i.e. across the channel dimension

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

6 | Schiller et al.

and ignoring the time dimension (Input Embeddings). In our case,
the only input channel is a time series of CRSWIR. Therefore, the
1D kernels translate the CRSWIR observations into the latent space
of the model, learning representations relevant to the under-
standing of the undisturbed time-series patterns. In the case of
multivariate time series, the kernels would additionally model
input channel combinations relevant for the understanding of
the time series. Additionally, Temporal Embeddings (also called
Positional Encodings; PE) are derived as learnable sine and cosine
representations from the day-of-the-year (DOY) information of
the observations and summed to the Input Embeddings. The
anomaly detection module of the TimesNet architecture is only
designed for and tested on regular time series (with equidistant
timesteps), and thus uses the position of the observation within
the sequences (the index) for PE. Since S2 time series are usually
irregular (due to pixels affected by clouds, cloud shadows, etc.),
we adjusted the PE to take as input the DOY values of the input
time series. Former research has shown that DL models can learn
PE on DOY values that support understanding the notion of time
of each observation (Yuan and Lin 2021, Wu et al. 2023, Schiller
et al. 2024).

The idea of the TimesNet model is to learn representations
across and within temporal subsets of the input time series (inter-
and intra-period variations; Fig. 3 (1) and (2)) by splitting them
into sub-sequences of repeating temporal patterns (periods) deter-
mined by Fourier transform. In our case of highly irregular time
series, however, a Fourier transform is not applicable. To mitigate
this, we use domain knowledge to replace it: the most relevant
period in forest remote sensing covering several years is the yearly
cycle of growing season and non-growing season. Thus, we can
define the period as one year. Technically, our input time series
(of two to four years’ length) is split by years and concatenated
next to each other instead of being analyzed as one single time
series of two to four years’ length (Fig. 3 (2)). With this setup,
however, the convolutional kernels (the main building blocks of
CNNs) running across the years (inter-period variation) would still
have to compare observations of potentially very different time
steps, as these kernels technically stride over index positions of
the sequences (Fig. 3 (3)). The abovementioned PE mitigate, but do
not solve, this problem, as e.g. the first observation of each single
year from the multi-year time series can be >2 months apart.
For instance, the observation date of the first index position of
a year (the first observation of this year) might be 1 January 2016,
whereas the observation date of the succeeding year’s first index
might be 20 March 2017. Since PE technically alters the value of
the observation in the latent space of the model given the day-of-
the-year value, but do not consider the temporal context of each
observation with respect to its preceding and succeeding observa-
tions (which is exactly what convolutional kernels are supposed to
do), a more f lexible approach that considers temporal context of
the utilized convolutional kernels is needed. Therefore, we adopt
the concept of Time-Parameterized Convolutional Neural Networks
(TPCNNs) (Kosma et al. 2023) by introducing “time-aware” kernels
with learnable parameters dynamically derived from the DOY val-
ues of the corresponding observations (Fig. 3 (4)). Technically, the
learnable weights of the convolutional kernels are multiplied by
the time tensor. Other than in the TPCNN study, we use absolute
(and not relative) parameterization. Relative parameterization
means that the center weight of the convolutional kernel is not
altered by the temporal value (the timestamp), while the others
are adjusted in relation to the center value. This, for instance,
might be reasonable for tracking the spread of a wildfire captured
by a sequence of satellite images, where the absolute timestamp

(e.g. the date) is irrelevant. In our case, however, the absolute
DOY contains essential information, e.g. the temporal position in
the vegetation season (summer, autumn . . . ) of the observation.
Consequently, we use the DOY of each embedded observation to
introduce dynamic time-aware convolutional kernels. Instead of
the DOY itself, we use the sine value of the DOY to model the
seasonal cycle. This allows the model to understand that while
DOY 1 and DOY 365 are mathematically the farthest apart in
the sequence, they are almost identical in terms of the seasonal
cycle. The convolutional kernels used in TimesNet always cover
all sequences at once, meaning that their width is equal to the
maximum number of parallel sequences, which is four years
(Fig. 3 (3)). In case the time series contains less than four years, the
years without observations are padded with zeros for technical
reasons. The kernels vary in their temporal coverage from one
until 15 time steps (this number was determined to be best in
preliminary training runs). Thus, these dynamic kernels enable
modeling the intra-period variation (see above) as well. Using
the representations learned as described above, the model then
reconstructs the input time series using a multi-layer perceptron
(also called dense layer; Fig. 3 (5)), which is the most basic layer
in DL.

For details about the model parameters and exact imple-
mentation, refer to the code repository on https://github.com/
ChrSchiller/TimesNet_RSAD.

Training and test procedure
We trained the model on all univariate CRSWIR time series from
the training datasets (Table 1; Fig. 1) of two to four years’ length.
We used data augmentation to inf late the training dataset during
training in order to prevent overfitting of the model to its specific
characteristics. In this approach, we applied DOY jitter, which ran-
domly adjusts the DOY values of the observations by ±3 days, and
observation jitter, which modifies the satellite observations by up
to 2% of the standard deviation of the corresponding time series.
The jitter was intentionally small since our aim in this study
was to identify even small diversions from normal patterns. Thus,
the noise level should be as low as possible in the time series.
As an additional data augmentation procedure, we shuff led the
order of the years in the time series randomly. This ensured e.g.
that there is no unintended bias from the more limited time
series of 2016 and 2017 (when S2B was either unavailable or only
partly available), which would otherwise always be the earliest
years in the time series. We stopped the training procedure if the
model performance (loss determined as mean squared error) did
not improve for three consecutive training cycles (epochs). This
procedure is called Early Stopping with a patience of three and
further prevents overfitting.

We split the training dataset randomly by a ratio of 4:1 into
training (used for adjusting the model parameters during training)
and validation. Mean and SD of the training dataset were used to
normalize the validation and test data. We repeated the random
training data split three times to assess whether the model’s
performance is consistent across different training datasets. Note
that when referring to the validation dataset here, we do not mean
the dataset used for validation of the model. While the latter is
referred to as the test dataset, the validation dataset is used to
track the progress of the training process in DL.

Analyses
The predictions of the final model on the validation dataset were
used for automatic thresholding for the classification on the test
dataset by determining the background noise level of the model.

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Early detection of bark beetle infestations in Central Europe | 7

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Figure 3. Processing chain of our adjusted version of the TimesNet (Wu et al. 2023) model architecture. (1) The input time series of the CRSWIR index of
up to 4 years’ length are (2) reshaped by splitting them by years. Afterwards, (3) convolutional kernels stride over the time series to learn
representations across sequences (inter-period variation) and timesteps (intra-period variation). The convolutional kernels are (4) dynamically
parameterized by a time tensor (Kosma et al. 2023) consisting of adjusted day-of-the-year values of the corresponding observations. (5) The learned
representations are used to reconstruct the input time series as close as possible.

The decision threshold for a bark beetle infestation detection was
defined as

threshold = meanval_error

+ f ×

(cid:4)

q99val_error

− q01val_error

(cid:5)

(2)

where meanval_error, q99val_error, and q01val_error denote the mean,
99th, and 1st percentile of all the model errors (squared error
between normalized observation and reconstruction) of the val-
idation dataset, respectively, and f is a threshold factor. The inter-
percentile range was preferred over the standard deviation here
to prevent rare extreme outliers from inf luencing the threshold.
Three threshold factors were tested in this study: 0.5, 1, and 1.5.
An anomaly was detected if the squared error between recon-
struction and corresponding normalized observation exceeded
the determined threshold for two consecutive observations. We
removed non-growing season observations (between 15 Novem-
ber and 15 March) from analysis since bark beetle infestation
detections are not possible in this time due to the inactivity
of the beetles in winter and might lead to unintended false
warnings.

We evaluated the model performance on undisturbed time
series of the AF dataset between 1 January 2018 and 31 Decem-
ber 2020 and on infested time series between 1 January 2019
until 10 to 14 weeks after the infestation event in 2021. Using
this approach, the time series of both groups had a length of

exactly three years for the undisturbed class and almost three
years for the infested class. A detection was considered a true
positive only if a warning was triggered according to the above-
mentioned scheme within the time frame of 4 weeks before and 10
to 14 weeks after the infestation (in the following called “detection
period”). We analyzed the early detection capabilities of the model
by consecutively increasing the detection period by 1 week from
10 to 14 weeks after the infestation. If a warning was triggered
before the detection period in the infested time series (meaning
between 1 January 2019 and the corresponding infestation date in
2021), we added a false positive to the confusion matrix for each
warning issued too early by the model. Regarding the undisturbed
time series, we decreased the number of true negatives and
increased the number of false positives by one for the first (false)
warning, and added a false positive to the confusion matrix for
any further false detection per pixel. The confusion matrix was
used to compute producer’s accuracy (PA, syn. recall), user’s accu-
racy (UA, syn. precision), and F1-score (harmonic mean between
PA and UA). These metrics were used to assess the performance
of the model.

We used R programming language (R Core Team 2023, v4.4.2)
including the packages terra (Hijmans 2023, v1.7-83) and sf
(Pebesma 2018, v1.0-19) for preprocessing and result analysis
and Python (Van Rossum and Drake 2009, v3.8) including PyTorch
(Paszke et al. 2019, v2.2.2) for model training and inference.

8 | Schiller et al.

Figure 4. Mean and standard deviation of user’s accuracy (precision) and producer’s accuracy (recall) for threshold factors (symbols) of decision
threshold (for details see section Methods) and weeks after infestation allowed for detection (colors) of three random splits of training and validation
datasets for model training. Dashed (dotted) black line indicates value of 0.8 (0.9) for reference.

Results

Discussion

Using a threshold factor of 1, the model achieves a PA of
11.8% ± 8.4% and a UA of 43.5% ± 24.5% (Fig. 4, Supplementary
Tables S1 and S2) in the early detection scenario (detection
within 10 weeks of estimated/observed infestation). This results
in an F1-score of 0.18 ± 0.12. When allowing for a detec-
tion within 13 weeks, both PA and UA increase notably to
PA = 81.5% ± 1%, UA = 84.5% ± 7.6%, and F1-score = 0.83 ± 0.04
(Fig. 4; Supplementary Tables S1 and S3). For detailed results on
the detection performance after 11, 12, and 14 weeks and the other
threshold factors, see Supplementary Tables S1, S4, S5, and S6. In
case of a threshold factor of 0.5 in the early detection scenario,
the UA is strongly reduced with UA = 34.5% ± 8.4%, whereas the
PA is clearly increased with PA = 25.4% ± 9.4%. Here, the F1-score
is 0.29 ± 0.14.

Among the 351 time series labeled as infested, 60 are detected
in the 6th week after infestation in case of a threshold factor
of 1 and the best model resulting from the three training data
splits (Fig. 5), whereas 59 are not detected within the detection
period. Most of the detections occur in week 11 (n = 123) and week
13 (n = 65). As visible in Fig. 6, detections with a similar delay
in weeks after infestation cluster spatially (another example is
shown in Supplementary Fig. S1). In this example, the center of the
disturbance polygon gets detected first (maximum 10 weeks after
infestation), and those pixels located more toward the edges of the
polygon get detected later (later than 10 weeks after infestation).
An example time series of the abovementioned polygon’s pixels
shows that the anomaly score rarely supersedes the detection
threshold in case of a threshold factor of 1 (Fig. 7). In this example,
it occurs only once before the infestation date. This occurrence
would not trigger a warning since the detection threshold is
only superseded once. Apart from that, the model reconstructs
the time series accurately. Shortly after the infestation, however,
the observed CRSWIR time series deviates from normal, which
manifests in a strong and rapid increase of the anomaly score.
In this case, subtle deviations from the non-anomalous pattern
result in an early detection.

In this study, we used >300 000 Sentinel-2 (S2) time series derived
from pixels of undisturbed coniferous forest in Central Europe
(Germany, Luxembourg, Austria) to train a reconstruction-based
Deep Learning (DL) model for anomaly detection with the goal of
early detection of bark beetle infestations.

We quantified differences between observations and recon-
structions (which are our predictions) of the CRSWIR index to detect
spectral anomalies resulting from bark beetle infestations. While
our model showed only a few detections within 10 weeks after
infestation (early detection scenario), which would have been
preferred by forest managers to prevent the spread of the next
beetle generation, it achieved high performance metrics within
13 weeks after infestation (PA = 81.5% ± 1%, UA = 84.5% ± 7.6%, F1-
score = 0.83 ± 0.04). In the following, we discuss the model perfor-
mance and the model’s potential in operational monitoring.

Model performance
Using a threshold factor of 0.5 resulted in many false positives
(Fig. 4), showing that this decision threshold is not clearly
exceeding the background error of the reconstructions. Even
using this threshold, however, the PA, which is a measure of
the ability of the model to detect positive cases (infestations),
was only 34.5% ± 21.1% in case of the early detection scenario.
The high standard deviation of UA and PA in the early detection
setup independent of the threshold factors also indicates that the
results are not robust for early detection. In any case, the model
clearly failed to reach a PA of 80% or higher, which was stated to
be supportive of an operational system aiming at controlling the
number of bark beetle infestations (Pietzsch et al. 2023). Figure 7
illustrates why the early detection results might be unstable:
while the model detects a subtle anomaly as the CRSWIR value
decreases unexpectedly in July 2021 in this example, the observed
CRSWIR strongly increases afterwards, leading to a clear anomaly.
The latter spectral response is expected once the trees are
deprived of water supply, which is a typical early symptom of bark
beetle infestations (Kirisits and Offenthaler 2002, Kautz et al. 2024,

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Early detection of bark beetle infestations in Central Europe | 9

Figure 5. Histogram showing the number of pixels of infested polygons with respect to the relative week of detection after estimated/observed bark
beetle infestation using the best among the three random training sample splits and a threshold factor of 1 (see section Methods). Last bin (“never
detected”) are those pixels that were not classified as anomalous until 14 weeks after infestation.

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Figure 6. Example polygon of infested class and time of detection in
weeks after infestation for all Sentinel-2 pixels completely covered by
the polygon for the best model resulting from the three random training
sample splits and a threshold factor of 1 (see section Methods). Circle:
time series shown in Fig. 7. Coordinate reference system EPSG:3035.

Marx et al. 2024). The former, however,
is more likely an
uncommon spectral f luctuation than an indicator of a typical
physiological response of the trees, as this spectral behavior is, to
the best of our knowledge, not described in literature. Moreover,
this is inconsistent with other time-series examples (not shown
for brevity). In week 11 and again in week 13, the detection rate
suddenly and strongly improves (Fig. 4). From week 13 onward, the
results are stable across random training data splits, indicating

Figure 7. Example time series of observed and predicted normalized
CRSWIR (upper panel) of an infested forest stand’s pixel and
corresponding anomaly scores (lower panel) of the best model among
the three random training sample splits. Vertical dashed line: date of
infestation (11 June 2021); vertical dotted line: date of detection using a
threshold factor of 1 (23 July 2021); horizontal dashed line: decision
threshold of an anomaly score of 1.138 (threshold factor = 1; see section
Methods). The plot shows the time series of the highlighted pixel in
Fig. 6.

that our approach is robust and the model is performing well
when given more time to detect the disturbance. This might be
the transition from green to red attack, when the trees show a
clear physiological and thus spectral response. This is in line with

10 | Schiller et al.

Huo et al. (2021), who found that the spectral response of S2
only shows significant differences between undisturbed and
infested trees for severely infested plots (>10 trees) and only
after ∼3 months, at the end or after the green attack stage.

Accordingly, it is unlikely that the correct disturbance detec-
tions in weeks ≤0 and 2 after the infestation (Fig. 5) were actually
caused by the targeted bark beetle infestation. While potential
reasons for these early detections could have been errors in deter-
mining the infestation date or an overseen tree infested earlier
during ground sampling, it seems more likely that the bark beetle
disturbance constitutes a secondary disturbance on an already
declining tree. In the latter case, the detected disturbances would
either be a delayed symptom of the severe hot drought of the pre-
ceding years (2018–2020) or caused by an unknown disturbance
agent, whereas the bark beetle infestation itself might have fol-
lowed, rather than initiated, the tree’s mortality. Delayed mortal-
ity occurring after the end of a drought has been reported before
(Bigler et al. 2007, Haberstroh et al. 2022). Secondary disturbance
as a reason for pre-infestation detections is also supported by the
fact that false warnings are much more abundant in the infested
than in the undisturbed time series (cp. Supplementary Fig. S2).
The figure also shows that these false warnings are accumulated
by a very small amount of pixels, some of them reaching up
to 16 warnings for a single pixel that was infested much later
and potentially disturbed already at the time the anomaly was
detected by the model (also cp. Supplementary Fig. S3). The partic-
ular example of Supplementary Fig. S3, which returned three false
warnings, shows a pixel located at the boundary of the test poly-
gon, and the neighboring forest stand has been cleared due to bark
beetles in the previous year (also confirmed for most other pixels
expressing more than five false warnings). Thus, it is possible that
the reason for the (seemingly false and too early) warnings of such
pixels is a spatial inaccuracy of the polygon delineation. Since
these few pixels expressing early warnings had a large impact on
our current analyses, although they might be correct detections
(except that they detect another disturbance event), we propose
an alternative performance assessment that defines “anomalous
phases” instead of counting each two consecutive anomalous
observations as a false positive in the Supplementary Material
(see also Supplementary Fig. S4, Supplementary Table S7). An
anomalous phase starts with the first detection and ends only if
two consecutive observations do not exceed the anomaly thresh-
old. In any case, the detections within a few weeks after infesta-
tion illustrate that the model, as all other remote sensing–based
near real-time (NRT) monitoring systems we are currently aware
of (e.g. Verbesselt et al. 2012, Puhm et al. 2020, Dutrieux et al.
2021, and Ye et al. 2021), is not able to differentiate between
disturbance agents. One option to partly differentiate between
disturbance agents would be a post hoc assessment investigating
the date of detection and the shape of disturbance patches. For
instance, windstorms and harvesting usually occur in winter in
Central Europe, whereas fires usually occur in summer.

Once a disturbance is detected by the model, the anomaly
often manifests unambiguously. The difference in both UA and
PA is rather small for the threshold factors of 1 and 1.5, which
illustrates that both decision thresholds are well above the recon-
struction error of the undisturbed time series. This is supported
by Fig. 7, which shows a clear distinction between anomaly scores
before the infestation and when the deviation of the observations
from the undisturbed pattern starts. Consequently, most false
positives can be avoided by our approach by selecting a threshold
factor of ≥1. Thus, we do not need to apply a minimum mapping
unit of multiple pixels to avoid falsely detected anomalies of

single pixels, as it is sometimes required in other NRT monitoring
approaches (e.g. Puhm et al. 2020 and Reinosch et al. 2024).
Additionally, the model should be able to reconstruct nonfatal
drought stress and thus not trigger a (false) warning in most cases.
As the spectral trajectories of trees during the hot drought of 2018
until 2020 in Central Europe have been included in the training
dataset, the mentioned nonfatal stress was indeed part of the
training. Thus, these severe stress events—when not leading to
mortality of the dominant trees—should mostly not be considered
anomalous by the model.

All in all, our study design along with the results suggest
that our method can safely be generalized and thus utilized in
locations other than those used for training purposes. As seen
in Fig. 7 (among others), the model responds immediately once
the spectral trajectory deviates from the pattern of the preceding
years. Thus, the model appears to generalize well across different
locations.

Operational bark beetle monitoring
Given that the model shows an immediate response once the
spectral trajectory deviates from the normal pattern (visible in
Fig. 7), it is questionable if a timely bark beetle infestation detec-
tion (within 10 weeks after infestation) can at all be realized
with S2 time series using any model, especially in a large-area
approach as we try here.

Many studies on early detection of bark beetle (mostly Ips
typographus L.) infestations have already been conducted. They
exploited S2 and other sensors such as uncrewed aerial vehicles
(UAVs) or other satellites (e.g. WorldView, RapidEye). The most
promising results with PA and UA >70% were achieved on indi-
vidual tree level using high-resolution imagery, e.g. UAV (Minaˇrík
et al. 2021; spatial resolution 6 cm), WorldView-2 (Immitzer and
Atzberger 2014; 2 m) or RapidEye (Ortiz et al. 2013; 6.5 m). Model
performances using S2 are generally lower, e.g. 53%/67% (PA/UA;
Abdullah et al. 2019), 76%/61% (Mandl and Lang 2023), 76%/53%
(Dalponte et al. 2022), and 79%/57% (Bárta et al. 2021). This might
be attributed to the lower spatial resolution of this sensor, making
an analysis on individual tree level challenging (for an attempt see
Dalponte et al. 2022). When counting a true positive only within
10 weeks after infestation in our analysis, all of these studies
outperformed ours since it did not show a consistent response
within this period (exceptions are discussed in Section Model
Performance and visible in Fig. 6). However, if using a less strict
criterion, e.g. detection within 13 weeks, our model outperformed
all S2-based studies and most of the other studies. A direct
comparison is challenging, however, as the term “early detection”
is often defined as green attack detection (infested trees that are
still green), ignoring the exact time after infestation (probably due
to the lack of reliable reference datasets).

The green attack, however, can last from a few weeks (Huo
et al. 2022) up to a few months after the infestation (Bárta et al.
2021, Huo et al. 2021), depending on environmental conditions,
for instance. Independent of that, the bark beetle brood swarms
out ∼6 to 10 weeks after the infestation (Kautz et al. 2024).
Accordingly, forest managers are primarily interested in an early
detection in terms of a maximum of 10 weeks after the infestation,
regardless of whether the tree is still green or already red. Two
studies are more explicit with respect to the temporal dimen-
sion. First, Mandl and Lang (2023) reported the detection date
and performance relative to ground observations on 4-weekly
surveys determining the infested trees as “freshly infested and
still green”. Most of the detected infestations in this study were
between 3 weeks before or after the ground observation. While

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

this might imply an early detection among the correctly classified
infestations, the study used post hoc information from the end of
the study period for its detections (see below). This impairs direct
applicability of the approach as a monitoring system. Second,
Ortiz et al. (2013) used data from a pheromone attraction exper-
iment set up at a specific date, and used single RapidEye (opti-
cal satellite) and TerraSAR-X (Radar) scenes acquired ∼7 weeks
after starting the experiment. Thus, these results imply an early
detection, as long as there were no infestations before starting
the experiment. However, besides the higher spatial resolution
of the sensors used in this study, the training and test site was
also limited to a single small forest stand in this study. This
further facilitates successful classification, as the model did not
have to deal with additional variability introduced by differing site
conditions and forest structures.

The problem of limited extent of study areas applies to many
earlier studies (e.g. Ortiz et al. 2013, Minaˇrík et al. 2021, Dalponte
et al. 2022, and Mandl and Lang 2023). Studies focusing on larger
regions such as the Bavarian Forest National Park in Germany
also did not test the spatial transferability of the model (Abdullah
et al. 2019). Working with small study areas likely decreases the
variability of both undisturbed and infested time series and image
features (sun angle, etc.), which in turn provides much better
conditions for separation of the classes and thus probably leads
to an increase of model performance (cp. Kattenborn et al. 2022)
as compared to an operational setting where large areas have to
be monitored. To the best of our knowledge, Marx et al. (2024) is
the only publication about early detection in the European spruce
bark beetle versus Norway spruce system that used a training
dataset far away from the test dataset (here: 436 km). The latter
study achieved good results on early detection between 13 and
70 days after infestation using a hyperspectral sensor mounted on
a UAV with spatial resolution of 5 cm. Therefore, this is the only
study that suggests that early detections are feasible across large
areas with the same model. Besides that, our study appears to be
the only one which uses a spatial hold-out as test data, which
provides a more pessimistic assessment, since environmental
conditions (e.g. temperature, understory composition) and sensor
effects (sun angle, etc.) may both differ.

Another drawback of former early detection studies is the use
of information from the end of the detection period to distin-
guish between undisturbed and infested trees during the detec-
tion period for model or data calibration. For instance, Mandl
and Lang (2023) retrospectively analyzed S2 scenes from 2020,
using gray attack areas determined in September 2020 in aerial
imagery to derive vegetation index (VI) thresholds and show the
post hoc separability of green attack and undisturbed trees in the
same year. Dalponte et al. (2022) used VI values from the last S2
scene of their study period as a baseline to calculate temporal
changes in VI values, which were then used for classification.
While these approaches demonstrate the potential of S2 for early
or green attack detection, they are not ready for NRT monitoring.
As opposed to that, our approach used automated thresholding on
data from different areas and partly different years to infer a suit-
able decision threshold. This threshold demonstrated robustness,
as anomalies clearly stand out against non-anomalous sequences
in the time series (cp. Fig. 4 and Fig. 7).

Accordingly, to the best of our knowledge, this is the first
study that applied an early bark beetle infestation detection
approach readily applicable for NRT monitoring on free-of-charge
S2 time series with spatially clearly distinct training and test areas
and temporally very accurate infestation data. An operational
remote sensing–based system successfully confining bark beetle

Early detection of bark beetle infestations in Central Europe | 11

outbreaks was estimated to require the timely removal of at least
80% of the infested trees (Pietzsch et al. 2023) while minimizing
the labor needed to achieve this. Consequently, in light of our
results and those from other studies discussed herein, this goal
seems to be almost unachievable at the moment. Laborious ter-
restrial observations, as opposed to that, have shown UA of 91%
and PA of 93% (Kautz et al. 2023), clearly meeting the accuracy
requirement.

One reason that hinders early detection in an NRT large-area
approach is likely the noise in the S2 time series. Despite a strict
quality assurance (see section Methods), single timestep outliers
may occur as point anomalies (cp. Fig. 7). Thus, we needed to
allow for two consecutive anomalous observations to trigger a
warning, which delays the detection time by at least one revisit
cycle (two consecutive clear sky observations). In most cases, this
leads to a delay of at least 5 days. Note, however, that the S2A
and S2B orbits partly overlap, which leads to improved revisit
times in the overlapping areas. Thus, the probability of clear
sky observations is higher in these cases. Since the model has
been trained on data covering large areas, the training dataset
contains both overlapping and non-overlapping parts of the orbits.
Therefore, the model should be able to cope with both enhanced
and reduced sampling frequencies.

Apart from this general challenge of optical satellites in NRT
monitoring, the spatial resolution might be one main drawback
of S2 in early bark beetle detections. The best results in literature
were achieved using satellites or UAV allowing for analysis on
individual tree crown level, e.g. Ortiz et al. (2013), Immitzer and
Atzberger (2014), and Minaˇrík et al. (2021). Individual tree analysis
ensures that the background signal, e.g. coming from soil, other
vegetation, or undisturbed trees, does not overlap the spectral
signal of the trees. Accordingly, the findings of Huo et al. (2022)
suggest that 5 to 10 disturbed trees in a 15-m plot of ∼30–50
trees are necessary to show any spectral response in S2. For most
plots in this study, significant changes in S2 bands occurred only
after ∼3 months and only in severely infested plots (>10 disturbed
trees).

While our anomaly detection approach bears great potential
in early detection tasks, it requires a manual selection of the
most suitable S2 bands or combinations thereof. One of the main
advantages of most DL models over other modeling approaches,
including other Machine Learning algorithms, is that manual
feature engineering is not necessary. These DL models inher-
ently engineer relevant features automatically from raw data and
extract relevant representations of those features, often followed
by a classification or regression (e.g. Yuan and Lin 2021, Schiefer
et al. 2023, and Schiller et al. 2024). In our case, however, the
approach was to reconstruct the input, meaning that automatic
feature engineering can only take place internally, whereas the
output was a reproduction of the input features. Thus, we needed
to provide an input that is optimally suited for the bark beetle
detection task. While many VIs have been developed and tested
for this task, there is no agreement in literature about a specific
index. Promising VIs are designed either to detect changes in cell
structure and chlorophyll content (Abdullah et al. 2019, Marx et al.
2024) or leaf water content (Abdullah et al. 2019, Mandl and Lang
2023). The raw SWIR1 band can also be used for forest disturbance
detection (Grabska et al. 2020) and has been shown to be sensitive
to bark beetle infestations in many studies (Abdullah et al. 2019,
Huo et al. 2021, Huo et al. 2022). Since preliminary tests indicated
best performance of CRSWIR, we used it here. The CRSWIR index,
which has not been used frequently in literature yet, amplifies
subtle changes in vegetation water content compared to SWIR1

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

12 | Schiller et al.

alone. This has shown to be optimal for this disturbance detec-
tion task. For instance, FORDEAD (Dutrieux et al. 2021), an NRT
disturbance detection approach using S2 time series, detected
68% of green attacks on spruce stands (Dutrieux et al. 2021). The
CRSWIR index has also been used to achieve a drought disturbance
detection in oak trees using S2 time series (Mouret et al. 2024).

The mentioned FORDEAD approach fits a harmonic model
to the S2 time series of the pixel of interest during a training
period and compares observations to model predictions in the
consecutive detection period. A potential advantage of FORDEAD
might be that the model only has to account for the variabil-
ity within a single pixel, whereas our model has to internalize
the spectral variability of all of the training time series across
Central Europe. Consequently, our model might be less sensitive
to subtle changes in the spectral trajectory which might consti-
tute normal spectral patterns considering large areas, but are
a sign of bark beetle infestation for a time series at a specific
location.

Considering that local/regional studies tend to achieve better
results (see above), it might be necessary to add local information
to the model to reduce the variability of what constitutes an
undisturbed time series. In the current model, regional differ-
ences, e.g. in the phenology, were largely ignored. One option to
improve upon this is to use thermal temporal encoding (Nyborg
et al. 2022), e.g. the cumulative soil temperature across the year
as observed by and extrapolated from ground-based local weather
station records, instead of our day-of-the-year encoding. Mete-
orological conditions strongly inf luence the phenology of trees,
e.g. by shortening the growing season at higher altitudes. Using
extrapolated or modeled temperature information from weather
station records, the variability of the features of an undisturbed
time series could be constrained. Such local cues might support
an earlier detection of bark beetle infestations.

A further option would be to couple the results of the presented
model with a predisposition approach. There is evidence that
the susceptibility of spruce trees to bark beetle infestations can
be modeled using various environmental factors. These include
stand characteristics such as age and density, site conditions like
drought stress, and climate variables such as temperature and
precipitation (Overbeck and Schmidt 2012, Netherer et al. 2019,
Xu et al. 2024). For the determined predisposed stands, a lower
anomaly threshold could be used to achieve an earlier detection,
or they could be prioritized in case of limited resources for ground
observations.

Conclusion

In this study, we used DL-based reconstructions of S2 time series
to detect anomalies in the CRSWIR index as an attempt for early
detections of bark beetle infestations in Central Europe. For model
training, the approach requires only undisturbed forest as refer-
ence data, which are generally easier to acquire, as most of the
forest in Central Europe remains intact despite numerous distur-
bances. While a satisfactory amount of early detections appears
impossible with our approach, the model seems well suited for for-
est disturbance detection in general. We provide trained models
and code at https://github.com/ChrSchiller/TimesNet_RSAD also
including all other forest types (broadleaved, mixed, coniferous)
and the 10 S2 bands with 10- and 20-m spatial resolution for the
scientific community to apply in following studies. All trained
models, however, should be evaluated on a broader scale and
scope (e.g. different disturbance agents) to verify a comprehensive
applicability since the current test dataset was confined to a small
area and a short time period of disturbance events.

Upcoming improved NRT monitoring approaches might need
information
to use regional models or additional regional
to reduce the spectral variability of non-infested trees for a
better separability of subtle changes in the spectral trajectory.
Additionally, the model performance could be enhanced by
additional
information from a predisposition approach that
models the susceptibility of the spruce trees in each pixel based
upon environmental variables. Moreover, sensors with higher
spatial resolution might be used, as they can be applied at
individual tree crown level, generally achieving better results
(Ortiz et al. 2013, Immitzer and Atzberger 2014, Minaˇrík et al.
2021). Data from these sensors, however, are usually cost-
intensive and thus not yet readily available for an area-wide
monitoring across large areas.

All in all, our approach did not achieve a sufficient accuracy
to replace terrestrial bark beetle surveys for early detection, but
appears very promising when given more time for the detection
(e.g. 13 weeks). As we provide the trained model for a ready-to-use
NRT bark beetle monitoring system, it may support ground obser-
vations by giving hints at specific locations that might have been
missed by human observers. Consequently, it may complement
terrestrial surveys in future operational use.

Acknowledgements

We thank Selina Schwarz from Karlsruhe Institute of Technology
(KIT) for providing the forest dieback dataset of Luxembourg and
Berthold Mertens from Wald und Holz NRW for approving the use
of the test dataset. We are generally thankful for any efforts to
publish datasets that can be used by other researchers, e.g. the
FNEWS dataset from Thünen Institute in Eberswalde, Germany.
We thank any institution that offers publicly available data, such
as some of the German federal states and the state of Luxem-
bourg. We greatly appreciate the provision of the S2 datacube of
Germany preprocessed with the FORCE software on the platform
www.eo-lab.org. Next to the data, code of the model architectures
are needed to try newly developed approaches. Hence, we thank
anyone who publishes the code along with their research. In case
of this study, we dedicate our gratitude to the developers of the
TimesNet model, which is the backbone of our approach. The
editors and reviewers who commented on the manuscript greatly
helped to improve it—thank you for that.

Author contributions

Christopher Schiller (Conceptualization, Data curation, Formal
analysis,
Investigation, Methodology, Visualization, Writing—
original draft), Johannes May (Data curation, Writing—review &
editing), Randolf Klinke (Writing—review & editing), and Fabian
Ewald Fassnacht (Funding acquisition, Project administration,
Supervision, Writing—review & editing)

Supplementary data

Supplementary data are available at Forestry online.

Conf lict of interest: None declared.

Funding

This work was supported by the German Federal Ministry
for Environment, Nature Conservation, Nuclear Safety and
Consumer Protection in the Future Forest project under grant
number 67KI21002C.

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

/

f

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

Data availability

The test dataset can be made available upon request to the cor-
responding author, co-author J.M., or at the following data repos-
itory: https://zenodo.org/records/10495412. Most of the training
data are available either openly (FNEWS: https://www.openagrar.
de/receive/openagrar_mods_00093065) or upon request to the cor-
responding author (own work datasets), e.g. via the following data
repository: https://zenodo.org/records/8397141. The Sentinel-2
datacubes of Austria and Luxembourg can be made available
upon request.

References

Abdullah H, Darvishzadeh R, Skidmore AK. et al. European spruce
bark beetle (Ips typographus, L.) green attack affects foliar
reflectance and biochemical properties. Int J Appl Earth Observ
Geoinform 2018;64:199–209. https://doi.org/10.1016/j.jag.2017.
09.009.

Abdullah H, Skidmore AK, Darvishzadeh R. et al. Sentinel-2 accu-
rately maps green-attack stage of European spruce bark beetle
(Ips typographus, L.) compared with Landsat-8. Remote Sens Ecol
Conserv 2019;5:87–106. https://doi.org/10.1002/rse2.93.

Bárta V, Lukeˇs P, Homolová L. Early detection of bark beetle infesta-
tion in Norway spruce forests of Central Europe using Sentinel-
2. Int J Appl Earth Observ Geoinform 2021;100:102335. https://doi.
org/10.1016/j.jag.2021.102335.

Bigler C, Gavin DG, Gunning C.

induces
lagged tree mortality in a subalpine Forest in the Rocky
Mountains. Oikos 2007;116:1983–94. https://doi.org/10.1111/
j.2007.0030-1299.16034.x.

al. Drought

et

Caudullo G, Tinner W, de Rigo D. Picea abies in Europe: distribution,
habitat, usage and threats. In: San-Miguel-Ayanz J, de Rigo D,
Caudullo G, Houston Durrant T, Mauri A (eds), European Atlas of
Forest Tree Species. Luxembourg: Publications Office of the Euro-
pean Union, 2016.

Dalponte M, Solano-Correa YT, Frizzera L. et al. Mapping a Euro-
pean spruce bark beetle outbreak using Sentinel-2 remote
sensing data. Remote Sens 2022;14:3135. https://doi.org/10.3390/
rs14133135.

Du B, Yuan Z, Bo Y. et al. A combined deep learning and prior
knowledge constraint approach for large-scale forest disturbance
detection using time series remote sensing data. Remote Sens
2023;15:2963. https://doi.org/10.3390/rs15122963.

Dutrieux R, Féret J-B, Ose K. Mise au point d’une méthode repro-
ductible pour le suivi généralisé des dégats de scolytes par télédé-
tection satellitaire. ONF Rend Techn 2021;69-70:37–44.
Dutrieux R, Féret J-B, Ose K. et al. Package Fordead. 2021.
Federal Ministry of Food and Agriculture (BMEL). Der Wald in Deutsch-
land - Ergebnisse der Vierten Bundeswaldinventur (the Forest in Ger-
many - Results of the Fourth National Forest Inventory). Bonn, Ger-
many: Federal Ministry of Food and Agriculture, 2024.

Frantz D. FORCE—Landsat + Sentinel-2 analysis ready data
and beyond. Remote Sens 2019;11:1124. https://doi.org/10.3390/
rs11091124.

Early detection of bark beetle infestations in Central Europe | 13

Sentinel-2 time series. Remote Sens 2020;12:1298. https://doi.
org/10.3390/rs12081298.

Grillakis MG. Increase in severe and extreme soil moisture droughts
for Europe under climate change. Sci Total Environ 2019;660:
1245–55. https://doi.org/10.1016/j.scitotenv.2019.01.001.

Haberstroh S, Werner C, Grün M. et al. Central European 2018 hot
drought shifts Scots pine forest to its tipping point. Plant Biol J
2022;24:1186–97. https://doi.org/10.1111/plb.13455.

Hijmans RJ. terra: Spatial Data Analysis. 2023.
Huo L, Lindberg E, Fransson JES. et al. Comparing spectral differences
between healthy and early infested spruce forests caused by bark
beetle attacks using satellite images. In: IGARSS 2022–2022 IEEE
International Geoscience and Remote Sensing Symposium, edited by
IEEE. Kuala Lumpur, Malaysia: IEEE, 2022, 7709–12.

Huo L, Persson HJ, Lindberg E. Early detection of forest stress from
European spruce bark beetle attack, and a new vegetation index:
normalized distance red & SWIR (NDRS). Remote Sens Environ
2021;255:112240. https://doi.org/10.1016/j.rse.2020.112240.

Immitzer M, Atzberger C. Early detection of bark beetle infestation
in Norway spruce (Picea abies, L.) using WorldView-2 data. PFG
2014;2014:351–67. https://doi.org/10.1127/1432-8364/2014/0229.
Ionita M, Nagavciuc V. Changes in drought features at the European
level over the last 120 years. Nat Hazards Earth Syst Sci 2021;21:
1685–701. https://doi.org/10.5194/nhess-21-1685-2021.

Kattenborn T, Schiefer F, Frey J. et al. Spatially autocorrelated training
and validation samples inflate performance assessment of con-
volutional neural networks. ISPRS Open J Photogramm Remote Sens
2022;5:100018. https://doi.org/10.1016/j.ophoto.2022.100018.
Kautz M. On correcting the time-lag bias in aerial-surveyed bark
beetle infestation data. For Ecol Manage 2014;326:157–62. https://
doi.org/10.1016/j.foreco.2014.04.010.

Kautz M, Feurer J, Adler P. Early detection of bark beetle (Ips
typographus) infestations by remote sensing – a critical review
of recent research. For Ecol Manage 2024;556:121595. https://doi.
org/10.1016/j.foreco.2023.121595.

Kautz M, Peter FJ, Harms L. et al. Patterns, drivers and detectability of
infestation symptoms following attacks by the European spruce
bark beetle. J Pest Sci 2023;96:403–14. https://doi.org/10.1007/
s10340-022-01490-8.

Kirisits T, Offenthaler I. Xylem sap flow of Norway spruce
after
inoculation with the blue-stain fungus Ceratocystis
polonica. Plant Pathol 2002;51:359–64. https://doi.org/10.1046/
j.1365-3059.2002.00722.x.

Kokaly RF, Asner GP, Ollinger SV. et al. Characterizing canopy bio-
chemistry from imaging spectroscopy and its application to
ecosystem studies. Remote Sens Environ 2009;113:S78–91. https://
doi.org/10.1016/j.rse.2008.10.018.

König S, Thonfeld F, Förster M. et al. Assessing combinations of Land-
sat, Sentinel-2 and Sentinel-1 time series for detecting bark beetle
infestations. GIScience Remote Sens 2023;60:2226515. https://doi.
org/10.1080/15481603.2023.2226515.

Kosma C, Nikolentzos G, Vazirgiannis M. Time-parameterized
convolutional neural networks for irregularly sampled time
series.
2023. https://doi.org/10.48550/
Preprint
arXiv.2308.03210.

on arXiv.

Frantz D, Haß E, Uhl A. et al. Improvement of the Fmask algorithm for
Sentinel-2 images: separating clouds from bright surfaces based
on parallax effects. Remote Sens Environ 2018;215:471–81. https://
doi.org/10.1016/j.rse.2018.04.046.

Künniger T, Elsener R, Heeb M. et al. Mechanical properties of
Norway spruce (Picea abies) infested by the bark beetle (Ips
typographus). Wood Mater Sci Eng 2024;19:85–91. https://doi.
org/10.1080/17480272.2023.2226644.

García-Herrera R, Garrido-Perez JM, Barriopedro D. et al. The Euro-
pean 2016/17 drought. J Climate 2019;32:3169–87. https://doi.
org/10.1175/JCLI-D-18-0331.1.

Langner N, Puhm M, Deutscher J. et al. FNEWS-Jahresprodukte 2018
bis 2022. Eberswalde, Germany: Thünen-Institut, 2023. Available
from OpenAgrar.

Grabska E, Hawryło P, Socha J. Continuous detection of small-
scale changes in Scots pine dominated stands using dense

Mandl L, Lang S. Uncovering early traces of bark beetle induced
forest stress via semantically enriched Sentinel-2 data and

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

14 | Schiller et al.

spectral
s41064-023-00240-4.

indices. PFG 2023;91:211–31. https://doi.org/10.1007/

Marvasti-Zadeh SM, Goodsman D, Ray N. et al. Early detection of
bark beetle attack using remote sensing and machine learning:
a review. ACM Computing Surveys 2024;56:Article 97.

Marx A, Clasen A, May J. et al. Imaging spectroscopy for bark beetle
detection in Norway spruce and the relevance of the red-edge
spectral range. Int J Appl Earth Observ Geoinform 2024;133:104100.
https://doi.org/10.1016/j.jag.2024.104100.

Minaˇrík R, Langhammer J, Lendzioch T. Detection of bark beetle
disturbance at tree level using UAS multispectral imagery and
deep learning. Remote Sens 2021;13:4768. https://doi.org/10.3390/
rs13234768.

Mouret F, Morin D, Martin H. et al. Toward an operational monitoring
of oak dieback with multispectral satellite time series: a case
study in Centre-val De Loire region of France. IEEE J Sel Top Appl
Earth Observ Remote Sens 2024;17:643–59. https://doi.org/10.1109/
JSTARS.2023.3332420.

Netherer S, Panassiti B, Pennerstorfer J. et al. Acute drought is
an important driver of bark beetle infestation in Austrian Nor-
way spruce stands. Front For Glob Change 2019;2:39. https://doi.
org/10.3389/ffgc.2019.00039.

Nyborg J, Pelletier C, Assent I. Generalized classification of satellite
image time series with thermal positional encoding. In: 2022
IEEE/CVF Conference on Computer Vision and Pattern Recognition Work-
shops (CVPRW), edited by IEEE. New Orleans, LA, USA: IEEE, 2022,
1391–401.

Reinosch E, Backa J, Adler P. et al. Detailed validation of large-
scale Sentinel-2-based forest disturbance maps across Germany.
Forestry 2025;98:437–453.

Schiefer F, Kattenborn T, Frick A. et al. Mapping forest tree species
in high resolution UAV-based RGB-imagery by means of convolu-
tional neural networks. ISPRS J Photogramm Remote Sens 2020;170:
205–15. https://doi.org/10.1016/j.isprsjprs.2020.10.015.

Schiefer F, Schmidtlein S, Frick A. et al. UAV-based reference data
for the prediction of fractional cover of standing deadwood
from Sentinel time series. ISPRS Open J Photogramm Remote Sens
2023;8:100034. https://doi.org/10.1016/j.ophoto.2023.100034.
Schiefer F, Schmidtlein S, Hartmann H. et al. Large-scale remote
sensing reveals that tree mortality in Germany appears to be
greater than previously expected. Forestry 2024;98:535–549.

Schiller C, Költzow J, Schwarz S. et al. Forest disturbance detection
in Central Europe using transformers and Sentinel-2 time series.
Remote Sens Environ 2024;315:114475. https://doi.org/10.1016/j.
rse.2024.114475.

Schwarz S, Werner C, Fassnacht FE. et al. Forest canopy mortal-
ity during the 2018-2020 summer drought years in Central
Europe: the application of a deep learning approach on aerial
images across Luxembourg. Forestry 2024;97:376–87. https://doi.
org/10.1093/forestry/cpad049.

Senf C, Seidl R, Hostert P. Remote sensing of

insect
disturbances: current state and future directions. Int J Appl
Earth Observ Geoinform 2017;60:49–60. https://doi.org/10.1016/j.
jag.2017.04.004.

forest

Ortiz S, Breidenbach J, Kändler G. Early detection of bark beetle green
attack using TerraSAR-X and RapidEye data. Remote Sens 2013;5:
1912–31. https://doi.org/10.3390/rs5041912.

Solheim H. Fungal succession in sapwood of Norway spruce infested
by the bark beetle Ips typographus. Eur J Forest Pathol 1992;22:
136–48. https://doi.org/10.1111/j.1439-0329.1992.tb01440.x.

Overbeck M, Schmidt M. Modelling infestation risk of Norway spruce
by Ips typographus (L.) in the Lower Saxon Harz Mountains (Ger-
many). For Ecol Manage 2012;266:115–25. https://doi.org/10.1016/
j.foreco.2011.11.011.

Paszke A, Gross S, Massa F. et al. PyTorch: an imperative style.
In: Advances in Neural Information Processing Systems. Vancou-
ver, Canada: High-Performance Deep Learning Library; 2019;32:
8024–35.

Patacca M, Lindner M, Lucas-Borja ME. et al. Significant increase
in natural disturbance impacts on European forests since 1950.
Glob Chang Biol 2022;29:1359–76. https://doi.org/10.1111/gcb.
16531.

Pebesma E. Simple features for R: standardized support for spa-
tial vector data. R J 2018;10:439–46. https://doi.org/10.32614/
RJ-2018-009.

Perbet P, Guindon L, Côté J-F. et al. Evaluating deep learning meth-
ods applied to Landsat time series subsequences to detect
and classify boreal forest disturbances events: the challenge
of partial and progressive disturbances. Remote Sens Environ
2024;306:114107. https://doi.org/10.1016/j.rse.2024.114107.

Pietzsch BW, Wudel C, Berger U. Nonparametric upscaling of bark
beetle infestations and management from plot to landscape
level by combining individual-based with Markov chain mod-
els. Eur J Forest Res 2023;142:129–44. https://doi.org/10.1007/
s10342-022-01512-1.

Puhm M, Deutscher J, Hirschmugl M. et al. A near real-time method
for forest change detection based on a structural time series
model and the Kalman filter. Remote Sens 2020;12:3135. https://
doi.org/10.3390/rs12193135.

R Core Team. R: A Language and Environment for Statistical

Computing. 2023.

Ustin SL, Roberts DA, Gamon JA.

imaging
spectroscopy to study ecosystem processes and properties.
BioScience 2004;54:523. https://doi.org/10.1641/0006-3568(2004)
054[0523:UISTSE]2.0.CO;2.

al. Using

et

Van Rossum G, Drake FL. Python 3 Reference Manual. Beaverton, OR:

Python Software Foundation, 2009.

Verbesselt J, Zeileis A, Herold M. Near real-time disturbance detec-
tion using satellite image time series. Remote Sens Environ
2012;123:98–108. https://doi.org/10.1016/j.rse.2012.02.022.

Voˇsvrdová N, Johansson A, Turˇcáni M. et al. Dogs trained to recognise
a bark beetle pheromone locate recently attacked spruces better
than human experts. For Ecol Manage 2023;528:120626. https://
doi.org/10.1016/j.foreco.2022.120626.

Wu H, Hu T, Liu Y et al. TimesNet: Temporal 2D-Variation Modeling for
General Time Series Analysis. Preprint on arXiv, 2023. https://doi.
org/10.48550/arXiv.2210.02186.

Xu C, Förster M, Gränzig T. et al. Relating soil moisture and Sentinel-2
vegetation index patterns to spruce bark beetle infestations prior
to outbreak. Forestry 2024;97:728–738.

Ye S, Rogan J, Zhu Z. et al. A near-real-time approach for monitoring
forest disturbance using Landsat time series: stochastic con-
tinuous change detection. Remote Sens Environ 2021;252:112167.
https://doi.org/10.1016/j.rse.2020.112167.

Yuan Y, Lin L. Self-supervised pretraining of transformers for
satellite image time series classification. IEEE J Sel Top Appl
Earth Observ Remote Sens 2021;14:474–87. https://doi.org/10.1109/
JSTARS.2020.3036602.

Zhu Z, Woodcock CE. Continuous change detection and clas-
sification of
land cover using all available Landsat data.
Remote Sens Environ 2014;144:152–71. https://doi.org/10.1016/j.
rse.2014.01.011.

© The Author(s) 2025. Published by Oxford University Press on behalf of the Institute of Chartered Foresters. All rights reserved. For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be
obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com.
Forestry: An International Journal of Forest Research, 2026, 99, 1–14
https://doi.org/10.1093/forestry/cpaf053
Original Article

l

D
o
w
n
o
a
d
e
d

f
r
o
m
a
c
a
d
e
m
c
.
o
u
p
.
c
o
m

i

/
f

l

/

/

o
r
e
s
t
r
y
/
a
r
t
i
c
e
9
9
2
/
c
p
a
0
5
3
8
2
5
0
8
3
6
b
y
g
u
e
s
t

f

/

o
n
1
8
O
c
t
o
b
e
r
2
0
2
6

