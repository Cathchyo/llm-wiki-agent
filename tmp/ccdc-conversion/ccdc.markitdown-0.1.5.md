Remote Sensing of Environment 144 (2014) 152–171

Contents lists available at ScienceDirect

Remote Sensing of Environment

j o u r n a l h o m e p a g e : w w w . e l s e v i e r . c o m / l o c a t e / r s e

Continuous change detection and classiﬁcation of land cover using all
available Landsat data
Zhe Zhu ⁎, Curtis E. Woodcock

Center for Remote Sensing, Department of Earth and Environment, Boston University, 675 Commonwealth Avenue, Boston, MA 02215, USA

a r t i c l e

i n f o

a b s t r a c t

Article history:
Received 25 February 2013
Received in revised form 17 January 2014
Accepted 18 January 2014
Available online 11 February 2014

Keywords:
CCDC
Classiﬁcation
Change detection
Time series
Land cover
Continuous
Landsat
Random Forest

A new algorithm for Continuous Change Detection and Classiﬁcation (CCDC) of land cover using all available
Landsat data is developed. It is capable of detecting many kinds of land cover change continuously as new images
are collected and providing land cover maps for any given time. A two-step cloud, cloud shadow, and snow
masking algorithm is used for eliminating “noisy” observations. A time series model that has components of
seasonality, trend, and break estimates surface reﬂectance and brightness temperature. The time series model
is updated dynamically with newly acquired observations. Due to the differences in spectral response for various
kinds of land cover change, the CCDC algorithm uses a threshold derived from all seven Landsat bands. When the
difference between observed and predicted images exceeds a threshold three consecutive times, a pixel is iden-
tiﬁed as land surface change. Land cover classiﬁcation is done after change detection. Coefﬁcients from the time
series models and the Root Mean Square Error (RMSE) from model estimation are used as input to the Random
Forest Classiﬁer (RFC). We applied the CCDC algorithm to one Landsat scene in New England (WRS Path 12 and
Row 31). All available (a total of 519) Landsat images acquired between 1982 and 2011 were used. A random
stratiﬁed sample design was used for assessing the change detection accuracy, with 250 pixels selected within
areas of persistent land cover and 250 pixels selected within areas of change identiﬁed by the CCDC algorithm.
The accuracy assessment shows that CCDC results were accurate for detecting land surface change, with
producer's accuracy of 98% and user's accuracies of 86% in the spatial domain and temporal accuracy of 80%.
Land cover reference data were used as the basis for assessing the accuracy of the land cover classiﬁcation. The
land cover map with 16 categories resulting from the CCDC algorithm had an overall accuracy of 90%.

© 2014 Elsevier Inc. All rights reserved.

1. Introduction

1.1. Monitoring land cover change with remote sensing

Mapping and monitoring land cover have been widely recognized as
an important scientiﬁc goal (Anderson, 1976; Foody, 2002; Friedl et al.,
2002; Hansen, Defries, Townshend, & Sohlberg, 2000; Homer, Huang,
Yang, Wylie, & Coan, 2004; Loveland et al., 2000; Wulder et al., 2008).
Land cover inﬂuences the energy balance, carbon budget, and hydrolog-
ical cycle as many different physical characteristics change as a function
of land cover, such as albedo, emissivity, roughness, photosynthetic
capacity, and transpiration. Land cover change can be natural or anthro-
pogenic, but with human activity increasing, the Earth surface has been
modiﬁed signiﬁcantly in recent years by various kinds of land cover
change. Knowledge of land cover and land cover change is necessary
for modeling the climate and biogeochemistry of the Earth system and
for many kinds of management purposes. Satellite images have long
been used to assess the Earth surface because of repeated synoptic
collection of consistent measurements (Lambin & Strahler, 1994).

⁎ Corresponding author. Tel.: +1 617 233 6031.

E-mail address: zhuzhe@bu.edu (Z. Zhu).

0034-4257/$ – see front matter © 2014 Elsevier Inc. All rights reserved.
http://dx.doi.org/10.1016/j.rse.2014.01.011

Images from the Landsat series of satellites are one of the most im-
portant sources of data for studying different kinds of land cover change,
such as deforestation, agriculture expansion and intensiﬁcation, urban
growth, and wetland loss (Coppin & Bauer, 1996; Galford et al., 2008;
Jensen, Rutchey, Koch, & Narumalani, 1995; Seto et al., 2002; Woodcock,
Macomber, Pax-Lenney, & Cohen, 2001), due to their long record of con-
tinuous measurement, spatial resolution, and near nadir observations
(Pﬂugmacher, Cohen, & Kennedy, 2012; Woodcock & Strahler, 1987;
Wulder et al., 2008). One of the drawbacks of Landsat data is the rela-
tively low temporal frequency. For each Landsat sensor, overpasses of
the same location occur every 16 days, and data at this temporal
frequency are only common within the United States where the sensors
are turned on for every overpass. For other parts of the world, the fre-
quency of data collection is generally less, depending on many factors
such as cloud cover predictions and availability of international ground
stations (Arvidson, Goward, Gasch, & Williams, 2006). Even for images
that are collected, clouds reduce the amount of usable data (Zhang,
Rossow, Lacis, Oinas, & Mishchenko, 2004). Therefore, most change
detection algorithms using Landsat have used two dates of Landsat im-
ages (Collins & Woodcock, 1996; Coppin, Jonckheere, Nackaerts, Muys,

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

153

& Lambin, 2004; Healey, Cohen, Yang, & Krankina, 2005; Masek et al.,
2008; Singh, 1989). Though these kinds of algorithms are relatively sim-
ple to implement, they are not always applicable. It may take a few
years to ﬁnd an ideal pair of Landsat images that are free of clouds,
cloud shadows, and snow (hereafter referred to as “clear”) and acquired
at the same time of year.

To ﬁnd change over shorter time intervals, several new change
detection algorithms using many dates of Landsat images (typically
one image per year) are appearing in the literature (Goodwin et al.,
2008; Hostert, Röder, & Hill, 2003; Huang et al., 2010; Kennedy,
Cohen, & Schroeder, 2007; Vogelmann, Tolk, & Zhu, 2009). However,
these newly developed algorithms still have limitations related to selec-
tion of ideal Landsat images. For example, to minimize the inﬂuences of
phenology and sun angle differences, the ideal images should fall within
the same season. Moreover, though they can use images that are partly
covered by clouds, they still need most of the images to be cloud-free. To
satisfy all these requirements, the best these algorithms can typically
provide is annual or biennial change results (Huang et al., 2010;
Kennedy et al., 2007).

Recently, Moderate Resolution Imaging Spectroradiometer (MODIS)
time series data have been explored for monitoring various kinds of
land cover change (Eklundh, Johansson, & Solberg, 2009; Galford et al.,
2008; Jin & Sader, 2005; Lunetta, Knight, Ediriwickrema, Lyon, &
Worthy, 2006; Roy, Jin, Lewis, & Justice, 2005; Verbesselt, Hyndman,
Newnham, & Culvenor, 2010; Xin, Olofsson, Zhu, Tan, & Woodcock,
2012), because of its higher temporal frequency. The coarse spatial
resolution of the MODIS data limits its ability for detecting small
changes (Jin & Sader, 2005), which is common for anthropogenic chang-
es. Also, issues of Bidirectional Reﬂectance Distribution Function (BRDF)
effects (Schaaf et al., 2002), large differences in the projected Instanta-
neous Field of View (IFOV) (Xin et al., 2012), and gridding artifacts
(Tan et al., 2006) make comparison of multitemporal MODIS images dif-
ﬁcult. To monitor changes as they are occurring and to be able to iden-
tify changes small in size, the remote sensing community needs an
algorithm that uses ﬁne spatial resolution data such as Landsat and
uses as many observations as possible to detect land cover change accu-
rately and quickly.

1.2. Land cover classiﬁcation

Land cover classiﬁcation is one of the most studied topics in remote
sensing, and land cover maps provide the basis for many applications
like modeling of carbon budgets, management of forests, and estimation
of crop yield (Jung, Henkel, Herold, & Churkina, 2006; Lark & Stafford,
1997; Rogan et al., 2010; Wolter, Mladenoft, & Crow, 1995). While it is
relatively easy to generate a land cover map from remotely sensed
data, it is not easy to make it accurate. Using multitemporal images as
inputs is reported to help improve classiﬁcation accuracy (Carrao,
Goncalves, & Caetano, 2008; Guerschman, Paruelo, Bella, Giallorenzi, &
Pacin, 2003; Wolter et al., 1995; Zhu, Woodcock, Rogan, & Kellndorfer,
2012), especially for vegetation, because of the unique phenological
characteristics of different vegetation types. To achieve higher classiﬁca-
tion accuracy, most current land cover products are generated using
multitemporal images as their inputs (Friedl et al., 2010; Gopal,
Woodcock, & Strahler, 1999; Hansen et al., 2000; Homer et al., 2004;
Loveland et al., 2000; Tucker, Townshend, & Goff, 1985).

The use of multitemporal images also can cause problems for con-
ventional automated classiﬁcation algorithms. First, they need all
dates of images to be free of clouds to classify every pixel in the
image, which is often not possible, especially for sensors with relatively
low temporal frequency like Landsat. For some cloudy locations, it may
be necessary to wait a few years to get multiple Landsat images in the
same year without clouds and snow. Therefore, most Landsat-based
land cover maps are produced at the interval of ﬁve or ten years,
which greatly reduces their “currency”. Second, when making land
cover maps with multitemporal images, we typically assume there is

no land cover change in the time interval between the different images.
This assumption is not always valid, especially when images from long
time intervals are used, or for areas that are changing frequently
(Rogan, Franklin, & Roberts, 2002). Moreover, the land cover maps pro-
duced from conventional methods cannot be used directly for identify-
ing land cover change because frequently the magnitude of the error in
classiﬁcation is much larger than the amount of land cover change
(Friedl et al., 2010; Fuller, Smith, & Devereux, 2003). If we compare
land cover maps produced at different times for detecting change, the
errors from the classiﬁcation process will show up as change and this
causes serious problems for places where the sizes of changes are
small. Therefore, the remote sensing community needs a classiﬁcation
algorithm that: (1) increases the time period over which land cover
maps remain “current”; (2) works for areas where multiple kinds of
land cover change is common, and (3) makes land cover maps compa-
rable between times for identiﬁcation of change.

1.3. Introduction to the CCDC algorithm

The opening of the Landsat archive in 2008 (Woodcock et al., 2008)
has led to big changes in the way Landsat images are being used. Previ-
ously, a single Landsat image would cost hundreds of U.S. dollars. To
minimize costs, most researchers typically chose to use only a few
cloud-free Landsat images acquired during the growing season for
analysis. Following free access to the Landsat archive, studies using
lots of Landsat images are appearing (Brooks, Thomas, Wynne, &
Coulston, 2012; Goodwin et al., 2008; Hansen et al., 2013; Huang
et al., 2010; Kennedy, Yang, & Cohen, 2010; Melaas, Friedl, & Zhu,
2013; Vogelmann et al., 2009; Zhu, Woodcock, & Olofsson, 2012). In
this paper, we seek to improve monitoring of land cover and land
cover change for a region in coastal New England by developing an
approach that uses all available Landsat data. We use all available
Landsat data because there are many clear observations in Landsat im-
ages that have a high percentage of clouds. Fig. 1 is a cumulative histo-
gram of the percentage of clear observations in Landsat images as it
relates to cloud cover. The cloud cover estimates are derived from a
newly developed Fmask algorithm (Zhu & Woodcock, 2012) for Path
12 Row 31 between 1982 and 2011. Based on this information, if we
only use Landsat images with cloud cover less than 10%, as has been
common in the past, we would omit more than 50% of the total clear
observations. Even Landsat images with more than 40% cloud cover con-
tain almost 20% of the total clear observations. The use of all available
Landsat data has opened a door for many studies that could not be imag-
ined before, such as the study of phenology at Landsat scales (Melaas
et al., 2013) or detection of forest disturbance continuously at high

Fig. 1. Percent of total clear observations vs. cloud cover percent interval based on all avail-
able Landsat TM/ETM+ images from 1982 to 2011 for Path 12 Row 31 (New England).

154

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

spatial resolution and high temporal frequency (Zhu, Woodcock, &
Olofsson, 2012).

Using all available TM/ETM+ observations from Landsat 4, 5, and 7,
we developed a new Continuous Change Detection and Classiﬁcation
(CCDC) algorithm that helps minimize the issues that undermine the
more conventional change detection and classiﬁcation methods men-
tioned above. The use of the term “continuous” here refers to the capa-
bility to detect change detection every time a new image is collected. If it
is updated as new images are collected, then the approach begins to
approach near real-time change detection. The use of “continuous” in
the name of the algorithm also follows from the idea that a land cover
map can be produced for any given time within the time period covered
by images. One additional note is that this new algorithm is able to
detect many kinds of land cover change.

2. Data and study area

2.1. Study area

agricultural ﬁelds, and forest clearing; and (3) it is rare to ﬁnd a cloud-
free Landsat image in this study area, making it an outstanding place to
test the robustness of this new algorithm.

2.2. Landsat data

All available Level 1 Terrain (corrected) (L1T) Landsat TM/ETM+
images for Worldwide Reference System (WRS) Path 12 and Row 31
with cloud cover less than 80% (based on the Fmask results) were
used (Fig. 2). A total of 519 images from Landsat 4 TM (3 images),
Landsat 5 TM (331 images), and Landsat 7 ETM + (185 images)
between 1982 and 2011 were used. The images are fairly evenly distrib-
uted throughout the year (Table 1), the months during the growing sea-
son (July, August, and September) having slightly more images than the
other months.

2.3. Land cover reference data

The study area is located in coastal New England, United States
(Fig. 2). It includes all of Rhode Island, as well as much of Eastern
Massachusetts and parts of Eastern Connecticut. It has been selected
because: (1) it includes Boston making ﬁeld visits easy; (2) it includes
a wide variety of environments and land covers that provide examples
of many of the primary kinds of land cover change occurring in the
United States, including: extensive urbanization (three major metro-
politan areas—Boston, Providence, and Worcester), abandonment of

Land cover reference data collected at any given time (within the
time period covered by the Landsat images) will work for training the
CCDC algorithm. The land cover reference data used in this paper were
previously used to calibrate the HERO Massachusetts Forest Monitoring
Program (MaFoMP) 2000 land cover product (Rogan et al., 2010). They
were created with the aid of aerial photographs and many ﬁeld visits
between 2005 and 2007. All reference sites were 60 × 60 m in dimen-
sion, and were distributed throughout Massachusetts to capture the
variability in reﬂectance values within the study area. In the original

Fig. 2. Study area for testing the CCDC algorithm.

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

155

Table 1
Frequency by month of all available Landsat data for the study area at Path 12 Row 31.

Month

Number of images

Jan.

41

Feb.

41

Mar.

40

Apr.

41

May

43

Jun.

43

Jul.

52

Aug.

48

Sept.

52

Oct.

47

Nov.

40

Dec.

31

data, water is divided into two land cover classes (shallow water and
deep water). To simplify, we combined shallow water and deep water
into one land cover class—water. There are a total of 8220 reference
sites for 16 categories of land cover (Table 2).

method (DuMouchel & O'Brien, 1989; Holland & Welsch, 1977;
O'Leary, 1990; Street, Carroll, & Ruppert, 1988) is used for estimating
the time series model (Eq. 1). The robust feature of the RIRLS method
reduces the inﬂuence of ephemeral changes, or pixels affected by
clouds, shadows, or snow that were not identiﬁed by Fmask.

3. Methods

This study is a “prototype” for continuous change detection and
classiﬁcation using all available Landsat data. Testing this approach for
other regions with different environments will be a future research
direction. This CCDC algorithm has several components, including:
image preprocessing, continuous change detection, and continuous
land cover classiﬁcation.

3.1. Image preprocessing

3.1.1. Atmosphere correction

Geometric registration and atmospheric correction are critical to the
CCDC algorithm, as they facilitate comparison of images through time.
In this research, we only use Landsat L1T images as they are more pre-
cisely registered than the Level 1 Systematic (corrected) (L1G) images.
Atmospheric correction is performed using the Landsat Ecosystem
Disturbance Adaptive Processing System (LEDAPS) atmospheric cor-
rection tool (Masek et al., 2006; Vermote et al., 1997), in which the
raw DN values are converted into Surface Reﬂectance (SR) and Bright-
ness Temperature (BT).

3.1.2. Screening of cloud, cloud shadow, and snow

Clouds, cloud shadows, and snow were initially masked using a newly
developed object-based algorithm called Fmask (Zhu & Woodcock,
2012). Though the Fmask algorithm provides relatively accurate
masks for clouds, cloud shadows, and snow, it is not perfect. Moreover,
there are other ephemeral changes such as thick aerosols, smoke, or
ﬂooding that may also get confused with land cover change. Therefore,
the CCDC algorithm uses a second step to further screen outliers previ-
ously missed by the Fmask algorithm based on multitemporal analysis
of the Landsat data (Zhu & Woodcock, in preparation; Zhu, Woodcock,
& Olofsson, 2012). This approach ﬁrst estimates a time series model
based on the “clear” observations previously identiﬁed by Fmask and
then detects outliers by comparing model estimates and Landsat obser-
vations. The Robust Iteratively Reweighted Least Squares (RIRLS)

Table 2
16-categories land cover description.

^ρ i; xð
Þ

¼ a0;i

RIRLS

(cid:1)

2π
Τ x
(cid:3)

(cid:3)

(cid:1)

þ b1;i sin

(cid:3)
2π
Τ x

(cid:1)

þ a2;i cos

(cid:3)

2π
ΝΤ x

ð1Þ

þ a1;i cos
(cid:1)
2π
ΝΤ x

þ b2;i sin

where,

Julian date
x
the ith Landsat Band
I
number of days per year (T = 365)
T
number of years of Landsat data
N
coefﬁcient for overall values for the ith Landsat Band
a0,i
coefﬁcients for intra-annual change for the ith Landsat Band
a1,i,b1,i
coefﬁcients for inter-annual change for the ith Landsat Band
a2,i,b2,i
^ρ i; xð
Þ
RIRLS predicted value for the ith Landsat Band at Julian date x

based on RIRLS ﬁtting.

Due to the fact that clouds and snow make Band 2 brighter and cloud
shadows and snow make Band 5 darker, we estimate time series models
for Band 2 and Band 5. By comparing the actual Landsat observations
and the corresponding model predictions, it is comparatively easy to
identify any remaining clouds, cloud shadows, snow, and other
ephemeral changes (Fig. 3). If any of the conditions in Eq. (2) are
met, this observation is identiﬁed as an outlier and removed from
further analysis.

The model estimation starts when there are a total of 15 “clear”
determined by Fmask) observations. The ﬁrst 12 are compared between
observed and model predicted values to decide whether there are
outliers. The reason for picking the ﬁrst 12 clear observations is that
the time series model of the CCDC algorithm has 4 coefﬁcients (see
Section 3.2 for detail) and 12 clear observations (three times the num-
ber of coefﬁcients) help make model estimation robust and accurate.
We do not perform the multitemporal cloud, cloud shadow, and snow
screening algorithm for the last 3 clear observations because the CCDC
algorithm needs extra observations at the end of the time series to

Class

Orchards
Cranberry Bogs
Pasture/Row Crops
Deciduous Forest
Conifer Forest
Mixed Forest
Golf Course
Grassland
Low Density Residential
High Density Residential
Commercial/Industrial
Water
Wetland
Salt Marsh
Sand Quarry
Bare Soil

Number of sites

Description

234
265
541
570
582
702
486
502
511
466
613
1088
513
436
374
337

Managed plantation of fruit trees, primarily apples
Managed bog containing cranberry bushes, seasonally ﬂooded
Open and cultivated agricultural grasslands
Forested land ≥80% broadleaved deciduous canopy cover
Forested land ≥80% needleleaved evergreen canopy cover
Forest land N20% conifer and b80% deciduous canopy cover
Highly managed open grasslands
Grassland dominated open spaces
Residential land with equal parts impervious surface & vegetation
Residential land minimally vegetated, N60% impervious surface
Impervious surface
Standing water present N11 months
Vegetated lands with a high water table
Tidal saltwater rivers/mudﬂats & surrounding herbaceous cover
Sand & gravel mining pits
Bare land sparsely vegetated, N60% soil background

156

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

allow the model to respond to land surface change so that changes
that occur at the end of the initial model estimation will not be iden-
tiﬁed as outliers. The reason for picking 3 clear observations is that
the CCDC algorithm uses three consecutive observations to deter-
mine if a pixel is changed or not (see Section 3.3 for detail) and
three clear observations are enough for the time series model to re-
spond to land surface change. If any of the ﬁrst 12 pixels are found
to be possible cloud, cloud shadow, snow or other ephemeral changes,
it is removed from the clear pixel list. Due to computational limitations

and the requirement of continuous monitoring, the CCDC algorithm
only applies this multitemporal cloud, cloud shadow, and snow detec-
tion algorithm during the time of model initialization (see Section 3.2
for detail). For observations acquired after model initialization, only
the Fmask algorithm is used.

ð
ρ 2; x

Þ−^ρ 2; x
ð

Þ
RIRLS

where,

N0:04 OR ρ 5; x

ð

Þ−^ρ 5; x
ð

Þ
RIRLS

b−0:04

ð2Þ

x
Julian date
ρ(i,x)
Observed value for the ith Landsat Band at Julian date x.
^ρ i; xð
Þ
RIRLS Predicted value for the ith Landsat Band at Julian date x

based on RIRLS ﬁtting (Eq. 1).

Cloud observation

3.2. The CCDC time series model

Generally, land surface change can be divided into three categories:
(1) intra-annual change (Fig. 4A), caused by vegetation phenology
driven by seasonal patterns of environmental factors like temperature
and precipitation; (2) gradual inter-annual change (Fig. 4B), caused

A

B

C

Snow observation

Cloud shadow observation

D

Snow observation

A

B

C

Fig. 3. Illustration of multitemporal screening of cloud, cloud shadow, and snow. The
circles are pixels identiﬁed as “clear” by Fmask and those labeled are the ones found by
the multitemporal analysis to be clouds, cloud shadows, or snow. Because clouds and
snow make Band 2 brighter (Fig. 3A & B) while cloud shadows and snow make Band 5
darker (Fig. 3C & D), clouds, cloud shadows, and snow are easily identiﬁed by comparing
the actual Landsat observations with the model predictions.

Fig. 4. Three categories of land surface change shown in Band 5 surface reﬂectance:
(1) intra-annual change (or seasonality) (Fig. 4A); (2) inter-annual change (or trend)
(Fig. 4B); and (3) abrupt change (or break) (Fig. 4C).

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

157

by climate variability, vegetation growth or gradual change in land
management or land degradation; and (3) abrupt change (Fig. 4C),
caused by deforestation, ﬂoods, ﬁre, insects, urbanization and so on.
Therefore, we use a time series model that has components of seasonal-
ity, trend, and breaks that captures all three categories of surface change
(Eq. 3). The model coefﬁcients are estimated by the Ordinary Least
Squares (OLS) method based on the remaining clear Landsat observa-
tions. We use OLS instead of RIRLS simply because it is faster and
more accurate when all the signiﬁcant outliers have been excluded.

(cid:1)

(cid:3)

(cid:1)

þ b1;i sin

(cid:3)
2π
Τ x

þ c1;ix

ð3Þ

2π
Τ x

^ρ i; xð
Þ
OLS

¼ a0;i

þ a1;i cos

(cid:4)
τ(cid:2)
k−1

bx ≤τ(cid:2)

k

(cid:5)

where,

Julian date
the ith Landsat Band
number of days per year (T = 365)
coefﬁcient for overall value for the ith Landsat Band
coefﬁcients for intra-annual change for the ith Landsat Band
coefﬁcient for inter-annual change for the ith Landsat Band
the kth break points.

x
i
T
a0,i
a1,i,b1,i
c1,i
⁎
τk
^ρ i; xð
Þ
OLS predicted value for the ith Landsat Band at Julian date x.

In the time series model, the overall value, or mean, for the ith
Landsat Band is captured by a0,i. Coefﬁcients a1,i and b1,i are used to
estimate the intra-annual changes caused by phenology and sun angle
differences for the ith Landsat Band. The inter-annual change for the
ith Landsat Band is captured by c1,i. Ideally, the more the coefﬁcients
included, the more accurate the model will be. However, when there
are too many coefﬁcients, the model may start to ﬁt to noise. Fig. 5
shows the results of the model for the different components of the
time series model. If we only use a single constant coefﬁcient (a0,i), it
can only capture the overall reﬂectance and all the intra- and inter-
annual variability is lost (Fig. 5A). By adding the inter-annual trend
(c1,i), the time series model is able to capture the trends, however, los-
ing all intra-annual variability (Fig. 5B). The best result comes when all
three components are included (Fig. 5C).

3.3. Continuous change detection

A

B

C

Fig. 5. Illustration of the OLS ﬁtting results by including different components of the time
series model. Fig. 5A shows the results when only including a single constant. Fig. 5B
shows the results of using a constant and an inter-annual trend in the time series
model. Fig. 5C shows the results of using all three components.

The basis of our method is comparison of model predictions with
clear satellite observations to ﬁnd change. Ideally, a single date compar-
ison would be deﬁnitive for detecting change. However, there is sufﬁ-
cient noise in the system due to factors like undetected clouds, cloud
shadows, snow, atmospheric haze, smoke, and changes in soil wetness
that will lead to numerous false positive errors in change detection
when using a single date for comparison (Zhu, Woodcock, & Olofsson,
2012). While noise factors tend to be ephemeral in nature, land cover
change is more persistent through time. The CCDC algorithm minimizes
ephemeral effects by processing a set of dates together as a group for
identifying land cover change. That is, if a pixel is observed to change
in multiple consecutive images, it is more likely to be land cover change.
Based on previous studies (Zhu, Woodcock, & Olofsson, 2012), change
identiﬁed in three successive dates showed the best results. Therefore,
pixels showing change for one or two consecutive times will be ﬂagged
as “possible change” and if a third consecutive change is found, the pixel
is assigned to the “change” class.

To detect one kind of land cover change such as forest change, a sin-
gle change index with a ﬁxed threshold is sufﬁcient (Zhu, Woodcock, &
Olofsson, 2012). To ﬁnd many kinds of land cover change, we need to
use more spectral bands, as land cover change that is obvious in one

spectral band (or index), maybe difﬁcult to identify in other spectral
bands (or indices). Moreover, the threshold for deﬁning change may
also be different for different kinds of land cover change. Therefore,
the CCDC algorithm uses all Landsat spectral bands and a data-driven
threshold (adjusted for each individual pixel) to detect many kinds of
land cover change. The OLS method (Eq. 3) is applied to all seven
Landsat bands and the RMSE is computed for each spectral band. The
difference between observations and model predictions for each
Landsat band is normalized by three times the RMSE. We use three
times the RMSE due to the fact that the spectral signals usually deviate
from model prediction by more than three times the RMSE when land
cover change occurs. Fig. 6 illustrates how the “three times the RMSE”
criterion is used for detecting land cover change for a deforestation
pixel. When there is no land cover change, the next three clear observa-
tions are always within the model predicted ranges (± 3 × RMSE)
(Fig. 6A & C). Fig. 6B shows how change is initially detected by compar-
ing the next three consecutive clear observations with model predic-
tions. Fig. 6 only uses one Landsat band (Band 5) to illustrate the
algorithm, but all seven spectral bands are used to detect change. In
Fig. 7, the same deforestation pixel as Fig. 6 is shown and when defores-
tation occurred, all spectral bands changed signiﬁcantly. Therefore, the

158

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

A

B

C

Fig. 6. This ﬁgure illustrates the reason for using the threshold of three times the RMSE for continuous change detection. Fig. 6A shows the model prediction and three times the RMSE
before change occurred. Fig. 6B shows the model prediction and three times the RMSE when change occurred. Fig. 6C shows the model prediction and three times the RMSE after change
occurred.

CCDC algorithm averages the difference between observations and
model predictions that have been normalized by three times the
RMSE for all seven Landsat bands, and if the result is larger than 1 for
three consecutive clear observations, a change is identiﬁed (Eq. 4).
Otherwise, if the values for only one or two consecutive observations
are larger than 1, it will be regarded as an ephemeral change and the
observations will be ﬂagged as outliers. The CCDC algorithm updates
the time series model when new clear observations become available,
adding a dynamic character to the process that allows the time series
to adjust over time. Eq. (4) provides the details of the land cover change
algorithm. Note that the continuous change detection algorithm
assumes that the phenology is consistent for stable land covers,
which may not be true for some semi-arid environments due to the
variation of the inter-annual differences. Further studies may be neces-
sary if we want to expand the use of this algorithm to other parts of the
world.

(cid:6)
(cid:6)
ρ i; xð

Þ−^ρ i; xð
Þ
OLS
3 (cid:3) RMSEi

(cid:6)
(cid:6)

N1 three times consecutively

ð

Þ

ð4Þ

Julian date
the ith Landsat band
the number of Landsat bands
observed value for the ith Landsat Band at Julian date x

∑k

1
i¼1
k
where,

x
i
k
ρ(i,x)

^ρ i; xð
Þ
OLS predicted value for the ith Landsat Band at Julian date x based

on OLS ﬁtting (Eq. 3).

Land cover change that occurs within the time of model initialization
(start of the model estimation) can bias the time series model predictions.
Therefore, if there is land cover change during the process of model ini-
tialization, the CCDC algorithm will remove the ﬁrst clear observation
and add one more clear observation and this process will continue until
no possible change is detected within the initialization time period. As a
result, each pixel will have its own start date for model initialization
and this also leads to different start dates for the continuous change
detection and classiﬁcation process. Three approaches are used to detect
change that might have occurred during the time period covered by the
ﬁrst 12 clear observations used for model initialization: abnormal slope,
abnormal ﬁrst observation, and abnormal last observation.

For pixels of stable land cover, the magnitude of the slope of the time
series model will be relatively small. If land cover change occurs during
the time of model initialization (tmodel), the observation will usually
deviate more than three times the RMSE, making the slope of the time
series model larger than 3 × RMSEi/tmodel. Therefore, the slope of the
time series model for the ith Band is normalized by 3 × RMSEi/tmodel
(see Eq. 5 for details), and if the average value of the normalized slope
for all bands is larger than 1, it will be detected as an abnormal slope,
indicating a possible change within the model initialization time. On
the other hand, if land cover change occurs at the start or the end of
model initialization, there may not be enough observations affected by

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

159

the land cover change to signiﬁcantly inﬂuence the magnitude of the
slope, but they may still inﬂuence model estimation. In this case, the
CCDC algorithm compares Landsat observations with model predictions
for the ﬁrst and the last observations during model initialization. As a
few change observations at the very beginning or end of the model ini-
tialization period will not inﬂuence model prediction signiﬁcantly, they

can still be detected by comparing observations with model predictions.
Therefore, the CCDC algorithm also calculates the difference between
observations and model predictions for the ﬁrst and the last observa-
tions. Next, the difference between observed and predicted values for
each Landsat band is normalized by RMSEi (see Eq. 5 for details), and
if the average value of the normalized difference for all Landsat bands

A

B

C

D

E

Fig. 7. This ﬁgure illustrates how the seven Landsat spectral bands (Bands 1–7) deviate from their original trajectories when deforestation occurred.

160

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

F

G

Fig. 7. (continued).

is larger than 1 for the ﬁrst or the last observation, it will be identiﬁed as
an abnormal observation, indicating possible change within the model
initialization period. As soon as the model initialization is ﬁnished,
it will be used as the basis for continuous change detection and
classiﬁcation.

1
k

∑k

i¼1

(cid:6)
(cid:6)
(cid:6)
(cid:6)
c1;i xð Þ
3 (cid:3) RMSEi

=tmodel

N1 OR

OR

1
k

1
k

∑k

i¼1

∑k

i¼1

where,

(cid:6)
(cid:6)
ρ i; x1
ð

(cid:6)
(cid:6)
ρ i; xn
ð

Þ−^ρ i; x1
ð
3 (cid:3) RMSEi
Þ−^ρ i; xn
ð
3 (cid:3) RMSEi

Þ
OLS

(cid:6)
(cid:6)

N1

ð5Þ

(cid:6)
(cid:6)

Þ
OLS

N1

xn

x
x1

Julian date
the Julian date for theﬁ rst observation during model
initialization
the Julian date for the last observation during model
initialization
the ith Landsat Band
the number of Landsat bands (k = 7)
Root Mean Square Error for the ith Landsat Band (Eq. 3)
the total time used for model initialization
coefﬁcient for inter-annual change for the ith Landsat Band
(Eq. 3)
ρ(i,x)
observed value for the ith Landsat Band at Julian date x
^ρ i; xð
Þ
OLS predicted value for the ith Landsat Band at Julian date x based

i
k
RMSEi
Tmodel
C1,i

on OLS ﬁtting (Eq. 3).

3.4. Continuous land cover classiﬁcation

Finding land cover change is important, but it will be more beneﬁcial
if we know the land cover categories before and after change. Instead of
classifying the original Landsat images as conventional methods would,
the CCDC algorithm uses the coefﬁcients of time series models as the
inputs for land cover classiﬁcation. After the change detection process,
each pixel will have its own time series models before and after any
changes. By classifying the time series model coefﬁcients, this algorithm
can provide a land cover type for the entire time period for each time
series model. Time series observations from all seven Landsat bands

(including the thermal band) were used for the land cover classiﬁcation.
In general, it is usually not recommended to include thermal data in
land cover classiﬁcation due to its sensitivity to substantially different
physical phenomena. Including thermal data can cause more harm
than good in land cover classiﬁcation. However, the CCDC algorithm is
able to use the multitemporal thermal data in the form of the coefﬁ-
cients for overall temperature, trend in temperature, and intra-annual
variation in temperature. In this approach, most of the short-term vari-
ability in temperature is removed and the general patterns related to
surface characteristics remain, and they prove useful for improving
land cover classiﬁcation.

The main idea of the land cover classiﬁcation is that different land
cover classes will have different shapes for the estimated time series
models. Fig. 8 illustrates different estimated time series models for
four different kinds of land cover change that occurred in the study
area. Taking Fig. 8A for instance, by classifying the ﬁrst time series
model, the CCDC algorithm is capable of providing a land cover
class (forest) for this pixel between 2001 and 2003. Similarly, the classi-
ﬁcation results of the second time series model provide the land cover
class (developed) for this pixel between 2005 and 2006. The gaps
in the middle of two models are classiﬁed as “disturbed” in the land
cover maps, because the large variability in the data during the transi-
tion time prevents model initialization. Note that when forest is
changed to developed, the time series models show completely different
shapes, especially for Band 4 and Band 6 (Fig. 8A). The reduction of Band
4 reﬂectance is easy to understand: forest reﬂects strongly in Band 4
while developed areas do not. The increase in Band 6 is mostly due to
reduced evapotranspiration and urban heat island effects when forest
is converted to developed. When forest is changed to barren (Fig. 8B),
the most signiﬁcant changes are observed in Band 5 and Band 7, as forest
is usually low in SWIR bands but barren always has high reﬂectance in
these spectral bands. For a pixel that has undergone a change from forest
to grass (Fig. 8C), there is not much difference in the time series models
in the visible bands, but the SWIR and thermal bands are quite different.
For the pixel that changed from forest to agriculture (Fig. 8D), the time
series models of the NIR and SWIR bands show the biggest difference.
These examples illustrate that the information contained in the time
series model is helpful for land cover classiﬁcation and by using the
coefﬁcients of the time series model it is possible to provide a single
land cover class for the entire period when change is not speciﬁcally
identiﬁed.

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

161

A

Forest

Developed

B

Forest

Barren

C

Forest

Grass

D

Forest

Agriculture

Fig. 8. Examples of the estimated time series models for all seven Landsat bands for the four most common land cover change in the study area.

Five variables (ρ; a1; b1; c1; and RMSE) generated from time series
model estimation are used as inputs for land cover classiﬁcation. The
ﬁrst variable (ρ) represents the overall spectral value at the center of
each time series model for each Landsat band. This overall value is
calculated by adding a constant (a0) and a slope (c1) multiplied by
the time to the middle of the time series model (Eq. 6). The second
and the third variables (a1 & b1) provide temporal information
about intra-annual (or season) patterns. The fourth variable (c1)
measures inter-annual differences or trends. The last variable
(RMSE) is calculated during OLS ﬁtting in Eq. (3) and measures
how well the time series model ﬁts the data. Fig. 9 shows the average
from reference sites for the ﬁve different variables for different land
cover categories. It is clear that different land covers show quite
different shapes in the plots of the ﬁve variables, and this informa-
tion is helpful for discriminating land cover types. Considering
there are 7 spectral bands and each band has 5 variables, there are

35 variables used as the input for classiﬁcation. As the reference data
are collected between 2005 and 2007, the estimated coefﬁcients of the
reference pixels that were not detected to have land cover change
between 2005 and 2007 are used for training the classiﬁer. The Random
Forest Classiﬁer (RFC) is used to perform land cover classiﬁcation
because of its relatively high accuracy and computational efﬁciency
(Breiman, 2001).

ρ ið Þ ¼ a0;i

þ c1;i

(cid:3) tstart

þ tend
2

ð6Þ

where,

tstart
tend

the time (Julian date) when model initialization starts
the time (Julian date) when model initialization ends

162

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

C

D

A

B

E

Fig. 9. The value of the ﬁve variables, ρ; a1; b1; c1

ð

and RMSE) for different land cover classes based on reference sites for each land cover category.

i
a0,i
c0,i

ρ ið Þ

the ith Landsat Band
coefﬁcient for overall value for the ith Landsat Band (Eq. 3)
coefﬁcient inter-annual change for the ith Landsat Band
(Eq. 3)
overall spectral value at the center of each time series model
for the ith Landsat Band.

4. Results

4.1. Results of the CCDC algorithm

The CCDC algorithm is capable of providing land cover change
and classiﬁcation maps continuously as newly collected Landsat

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

163

Massachusetts

Connecticut

Rhode Island

Fig. 10. Two pieces of Landsat data used for illustration the CCDC results in the study area. The smaller one (left) is used for illustrating the CCDC results in Fig. 11 and the larger one (right)
is used for illustrating the CCDC results in Fig. 12.

images become available. We used a very small (5.6 km × 2.8 km)
and a relatively large (90 km × 45 km) area to illustrate the results
of the CCDC algorithm (Fig. 10).

Fig. 11 illustrates two “snapshots” of the CCDC results for the smaller
piece of Landsat image. Fig. 11A is the CCDC result for September 2nd,
1988 and Fig. 11B is the CCDC result for July 16th, 2011. For each time
period, the top three panels consist of a small piece of a newly collected
Landsat image (left), the most recent land cover change map at the cor-
responding time (middle), and a land cover classiﬁcation map at the
same time (right). The three graphs at the bottom are the time series
data (Band 4) for the three pixels located in sites 1, 2, and 3 that ulti-
mately underwent some kinds of land cover change. That change that
occurred at these pixels is obvious when viewed from the perspective
of the entire time series. This approach allows the identiﬁcation of the
timing of each change, as well as the kind of change. When the time se-
ries has been built for a pixel and analyzed for change, it is possible to
use the estimated time series models between the changes to identify
the land cover class for the pixel at different time periods. For the
pixel located at site 1, the estimated model preceding the change in
1988 can be used to classify the land cover for the entire time prior to
the change. Similarly the estimated model subsequent to the change
can be used to identify what land cover came after the change in
1988. The shape of the time series model can be very helpful in land
cover classiﬁcation which is evident in the time series graphs at the bot-
tom, as initially both pixels located at sites 1 and 3 were conifer forest
and pixel located at site 2 was a hardwood forest, and they are readily
distinguishable by the difference in the amplitude of their time series
in Band 4.

Fig. 12 illustrates the CCDC results for the larger piece of Landsat
data. The two images on the left (Fig. 12A & B) are two clear Landsat im-
ages at the beginning (September 17th, 1984) and at the end (July 16th,

2011) of the time series. The two images on the right (Fig. 12C & D) are
the most recent change detection and classiﬁcation maps at the end of
the time series generated by the CCDC algorithm. This comprehensive
analysis of land cover provides both the timing and nature of land
cover changes. To simplify for illustration purposes we collapsed the
16-categories land cover classes into 7-categories classes: forest, wet-
land, agriculture, barren, water, grass, and developed. For example, we
can easily derive information like in the past 30 years the largest loss
of forest is from forest to developed and the largest gain of forest is from
barren to forest for this area. It can also provide new kinds of information
about what kind of land cover change occurred on a yearly basis for the
entire scene. Fig. 13 illustrates the annual amounts (km2) of different
kinds of forest-related land cover change. Fig. 14 illustrates the amount
of forest loss on a yearly basis. Note that both Figs. 13 and 14 start in
1986 instead of 1982 when ﬁrst Landsat image is acquired. This is be-
cause the CCDC algorithm needs at least 15 clear observations to initial-
ize the time series model for continuous change detection and
classiﬁcation and before 1986 most of the pixels do not have more
than 15 clear observations.

4.2. Accuracy assessment

4.2.1. Accuracy assessment for change detection

As the CCDC algorithm is capable of detecting change at high tempo-
ral frequency, it is difﬁcult to ﬁnd reference data that can thoroughly
assess its accuracy both spatially and temporally. There simply are not
independent datasets available that have both ﬁner spatial resolution
and higher temporal frequency than Landsat images over the time peri-
od covered by Landsat. To know where and when land cover change
occurs, the primary source for reference data is the Landsat images
themselves (Cohen, Yang, & Kennedy, 2010). High spatial resolution

164

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

Landsat surface reflectance

Land cover change map

Land cover classification map

1

A

1

2

3

2

3

)
4
0
1
X

(

e
c
n
a
t
c
e

l
f
e
r
e
c
a
f
r
u
s
4
d
n
a
B

4000

2000

0

4000

2000

0

4000

2000

0

2009-08-15

2006-11-19

2004-02-23

2001-05-29

1998-09-02

1995-12-07

1993-03-12

1990-06-16

1987-09-20

1984-12-24

1982-03-30

Bare soil

Sand Quarry

Salt Marsh

Wetland

Water

Comm/Ind

High Den Res

Low Den Res

Grassland

Golf Course

Mixed Forest

Conif Forest

Decid Forest

Pasture/Crops

Cranb Bogs

Orchard

Disturbed

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

N

0

0.5

1

2

Kilometers

Landsat surface reflectance

Land cover change map

Land cover classification map

1

B

1

2

3

2

3

)
4
0
1
X

(

e
c
n
a
t
c
e
l
f
e
r

e
c
a
f
r
u
s

4
d
n
a
B

4000

2000

0

4000

2000

0

4000

2000

0

2009-08-15

2006-11-19

2004-02-23

2001-05-29

1998-09-02

1995-12-07

1993-03-12

1990-06-16

1987-09-20

1984-12-24

1982-03-30

Bare soil

Sand Quarry

Salt Marsh

Wetland

Water

Comm/Ind

High Den Res

Low Den Res

Grassland

Golf Course

Mixed Forest

Conif Forest

Decid Forest

Pasture/Crops

Cranb Bogs

Orchard

Disturbed

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

1985-01-01

1990-01-01

1995-01-01

2000-01-01

2005-01-01

2010-01-01

N

0

0.5

1

2

Kilometers

Fig. 11. Two “snapshots” of the smaller piece of Landsat data used for illustrating the CCDC results. Panel A is the CCDC results at the beginning (September 2nd, 1988) and panel B is the
CCDC results at the end (July 16th, 2011) of the almost 30 years of time series data. For each time period, the top three panels are a small piece of a newly collected Landsat image (left), a
map showing the timing and location of land cover change at the same time (middle), and the corresponding land cover map (right). The three graphs at the bottom are the time series of
Band 4 surface reﬂectance for the three pixels in sites 1, 2, and 3 located in the center of the white rectangles. Note that all three sites underwent land cover change (they started as forest)
and it is relatively easy to tell when they changed.

images from Google Earth (http://earth.google.com/) can help manual
interpretation of the land cover classes. Though the high spatial resolu-
tion images cannot provide the same temporal frequency as Landsat

data, their high spatial resolution is helpful in determining land cover
change at longer time intervals. A random stratiﬁed sample design
was used for assessing the change detection accuracy. A total of 500

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

165

Fig. 12. The larger piece of Landsat data used for illustrating the CCDC results. Panel A is from the September 17th, 1984 Landsat image. Panel B is from the July 16th, 2011 Landsat image.
Panel C is the most recent land cover change map. Panel D is the most recent land cover classiﬁcation map.

reference pixels were selected, in which 250 pixels were from areas
where land cover was persistent throughout the time of the analysis
(1982–2011) and 250 pixels were selected within areas where land
cover change was identiﬁed by the CCDC algorithm. By carefully

examining the time series data for all seven bands, it can be quite easy
to identify pixels that have changed and when the change occurred. If
there is confusion in determining a change or when it occurred, we
examined the Landsat images before and after the possible change

166

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

Table 3
The accuracy assessment of change detection in the spatial domain.

Reference data (spatial domain)

Changed pixels

Stable pixels

Total

User's (%)

Changed pixels
Stable pixels
Total
Producer's (%)

214
5
219

36
245
281

250
250

85.60
98.00

97.72

87.19

Overall (%)

91.80

more times consecutively; 3) low temporal frequency of the time series
data; and 4) very small RMSEs. Overﬁtting may cause serious problems.
Though we are using simple time series model, overﬁtting can still
happen if the data are always missing for a certain time of year because
of clouds and/or snow. In Fig. 17, overﬁtting occurred for Band 4 at the
beginning of model estimation, due to constant snow cover during the
winter and this led to a commission error marked by the red circle. On
the other hand, if clouds are missed three consecutive times, it will
also be falsely identiﬁed as change (Fig. 18). For pixels located at the
edges of Landsat images, the temporal frequency of the time series is
much lower, and this will reduce the accuracy of model estimation,
which may also lead to falsely identiﬁed change (Fig. 19). The last rea-
son for false detection of change is a very small RMSE. Since the CCDC
algorithm uses the RMSE value for deﬁning the threshold for land
cover change, when the RMSE value is small, a very slight change caused
by the atmosphere or other factors can be easily confused with land
cover change. This problem is common for pixels that are spectrally
dark, such as water (Fig. 20). Some of these problems can be overcome
by intelligent post-processing of the data. For example, if the land cover
class is the same before and after the change is identiﬁed, it is likely that
the identiﬁed change is an error.

The temporal accuracy of change detection was assessed for all
214 pixels in the accuracy assessment selected from areas where the
algorithm found land cover change, and are correctly identiﬁed in the
spatial domain. The proportion of the pixels that have the same change
time between the CCDC results and the reference data is referred to as
the “temporal accuracy”. The algorithm occasionally ﬁnds change later
than the reference data but it never found change earlier than the refer-
ence data. The proportion of the pixels that have the same time of
change between the algorithm results and reference data is 79.91%
(Table 4). The proportion of the pixels that are found to have changed
later than the reference data but are within 32 days of the ﬁrst date
when a change is observable is 13.08% which is 65.12% of the temporal
errors (Table 4). In other words, if we consider ﬁnding changes within a
month of the ﬁrst observable date is “correct”, the temporal accuracy is
as high as 92.99%.

The temporal errors are mostly due to the fact that at the very begin-
ning of the change, the pixel may have only partially changed, and this
spectral change is not large enough (less than three times the RMSE)
to be identiﬁed by the CCDC algorithm. However, this change may be
later identiﬁed by the CCDC algorithm when it is totally changed. In
Fig. 21, before the red circle (the change identiﬁed by the CCDC algo-
rithm), there is one observation that slightly deviates from model
prediction that was mainly caused by a partial forest cut (indicated by
the green circle), but this deviation is still relatively small compared to
the next clear observation in the red circle.

Table 4
The accuracy assessment of change detection in the temporal domain.

Reference data (temporal domain)

Changed pixels
Proportion (%)

Same

171

79.91

Late ≤ 32 days

Late N 32 days

Total

28
13.08

15

7.01

214
100.00

Fig. 13. Histogram of the annual amounts (km2) of different kinds of forest-related land
cover change between 1986 and 2010.

time or used high spatial resolution images from Google Earth to help
determine what was happening at that time for that speciﬁc location.
If there are multiple changes within one pixel, only the ﬁrst change is
used in the accuracy assessment.

The results of the accuracy assessment show producer's accuracy of
97.72% and user's accuracy of 85.60% for changed pixels, and overall
accuracy of 91.80% (Table 3). The relative lower user's accuracy indi-
cates more commission errors than omission errors in detected changes.
A higher threshold or more consecutive observations may better bal-
ance the commission and omission errors.

The omission errors are mostly due to the following reasons: 1) par-
tially changed pixels; and 2) change occurs too early, before the model
is initialized. The partially changed pixels are always difﬁcult to detect,
as the magnitude of change is mostly dependent on the proportion of
change within that pixel. In Fig. 15, there was a partial forest cut around
1998 and it is evident that after that point in time the Band 5 variability
changed signiﬁcantly, but the magnitude of this change is relatively
small. On the other hand, if change occurred at the beginning of
model initialization, the CCDC algorithm was unable to detect any
kind of change as there are not enough observations to initialize the
time series model (Fig. 16).

The commission errors mostly result from the following reasons:
1) overﬁtting of the time series model; 2) clouds missed three or

Fig. 14. Histogram of the annual amounts (km2) of net forest loss between 1986 and 2010.

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

167

.

e
s
U

.

5
9
6
8

.

8
0
9
9

.

0
4
9
8

7
3
1
9

.

.

1
0
9
8

5
0
5
8

.

.

2
4
2
9

9
9
7
8

.

9
3
8
7

.

.

2
3
7
8

.

7
0
8
8

.

9
4
8
9

.

3
7
2
9

.

4
9
8
9

6
8
4
8

.

.

7
8
5
8

0
2
0
9

.

2

3
3

6
0
1

0

4
1

9
3

4
2

6
4

0
5

0

9
5

0

9

0

9
5
1

7
2
3
2

0

0

7
1

0

0

5
1

0

7
1

2

0

0

5

0

4
1
1

7
8

5
3
6
2

0

0

0

0

0

4
1

0

0

8

0

7

3

0

0

2
4

7
8
9
2

0

0

2
1

1
2

0

2
4

0

0

6
1

0

0

5
6

0

1

1
2

1
3
4
3

0

5

0

0

1

0

0

0

0

0

0
2

0

3
1

2
1

2
1
1

1
1
3
8

0

0

0

9

0

3
7

0

0
2

9
1

6
6
2

8
0
1
3

0

8

0

1
5

5
6
1

0

0

0

0

0

0

0

0

1
0
1

6
3
1

4
9
4
1

0

0

0

0

6
1

0

2
2

4
1

6
2

8

9
3

3

1
9

4
4

1
5

1
1

6

5

9
3

5
8
1

0
8
8
2

0

1
7

3
9

5

0

2
1

3
8

7
1
1

7
6
9
2

3
1

1
6

0

0

0

4
3

6
6

8

3
4

9
3

4
3

0
1

3
2

4
2

9
0
1

0
5
4
2

0

0

8

1

3

0

0

0

3

0

9
0
2

1
3
4

6
8
6
4

0

2
4

1
2

0

0

0

2
1

0

2
3

0

0

0

0

1
1

9
7
3

3
4
6
3

0

0

4
3

0

0

0

2

0

0

3

1

0

3

0

6
3
1

9
1
6
3

0

0

0

0

0

0

0

0
3

6
4

4
2

S
B

Q
S

M
S

T
W

W

I
C

D
H

D
L

G

C
G

F
M

F
C

F
D

2

8
2
1

0
5
5
3

C
P

0

0
1

3
2

7
3

0
6

0
1
1

0

0

0

0

0

6
3

2
7

4
1
1
8

.

1
1
1
9

.

8
5
7
9

.

.

7
0
5
9

.

8
0
8
9

.

7
5
3
8

2
5
5
8

.

1
1
4
8

.

4
2
4
8

.

3
0
9
8

.

0
2
6
8

.

6
4
9
8

.

.

8
7
3
9

.

3
1
8
8

0

2
5
1
2

B
C

2

0

0

8

0

1
1

3
1

0

0

0

1

0

0

2
4
7
9

.

2
2

0

5
3
1

6
8
9
1

O

3

0

1

2
1

1
5

2
3

0

0

0

0

2

0

6

4
1
9
8

.

B
C

C
P

F
D

F
C

O

F
M

C
G

G

D
L

D
H

I
C

W
D

W

M
S

Q
S

S
B

.

o
r
P

/
l
a
i
c
r
e
m
m
o
C
=

I
C

,
l
a
i
t
n
e
d
i
s
e
R
y
t
i
s
n
e
D
h
g
i
H
=
D
H

,
l
a
i
t
n
e
d
i
s
e
R
y
t
i
s
n
e
D
w
o
L

=
D
L

,

d
n
a
l
s
s
a
r
G
=
G

,

e
s
r
u
o
C
f
l
o
G
=
C
G

,
t
s
e
r
o
F
d
e
x
i
M
=
F
M

,
t
s
e
r
o
F

r
e
f
i
n
o
C
=
F
C

,

t
s
e
r
o
F

s
u
o
u
d
i
c
e
D
=

F
D

,
s
p
o
r
C
w
o
R
/
e
r
u
t
s
a
P
=
C
P

,
s
g
o
B
y
r
r
e
b
n
a
r
C
=
B
C

,
s
d
r
a
h
c
r
O
=
O

:
e
t
o
N

.

n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

f
o
t
n
e
m

s
s
e
s
s
a
y
c
a
r
u
c
c
a
e
h
T

5
e
l
b
a
T

.
l
i
o
S

e
r
a
B
=
S
B

,

y
r
r
a
u
Q
d
n
a
S

=
Q
S

,

h
s
r
a
M

t
l
a
S

=
M
S

,

d
n
a
l
t
e

W
=
T
W

,
r
e
t
a
W
=
W

,
l
a
i
r
t
s
u
d
n
I

4.2.2. Accuracy assessment for classiﬁcation

The land cover reference data previously used for continuous land
cover classiﬁcation (introduced in Section 2.3) were used as the basis
for assessing the accuracy of classiﬁcation for the CCDC algorithm. As
the land cover reference data were collected between 2005 and 2007,
we will only assess the accuracy of land cover classiﬁcation at this
speciﬁc time interval. A total of 80% of the land cover reference data
were randomly selected to train the classiﬁer, and the remaining 20%
were used to assess map accuracy (Fielding & Bell, 1997). This process
was repeated 50 times and the average user's accuracy, average
producer's accuracy, and average overall classiﬁcation accuracy were
used to assess the land cover classiﬁcation accuracy for the CCDC algo-
rithm. In this approach, each reference pixel is used many times for
both training and accuracy assessment, but never both for a single trial.
The average of the overall accuracy of the land cover classiﬁcation with
16-categories is 90.20% (Table 5), which is almost the same accuracy as
another study of the same place using all available dimensions (spectral,
temporal, and spatial) of Landsat data (Zhu, Woodcock, Rogan, et al.,
2012). The average producer's and user's accuracies for the different
land cover types are also quite high, with mostly being approximately
90% (Table 5). The largest confusions are between Mixed Forest and Co-
nifer Forest, Deciduous Forest and Mixed Forest, Low Density Residential
and High Density Residential, and Low Density Residential and Commer-
cial/Industrial (Table 5).

5. Discussion and conclusions

Detection of land cover change and classiﬁcation are difﬁcult prob-
lems in remote sensing. Better use of the temporal domain of Landsat
data can improve both change detection and land cover classiﬁcation.
In this study, we developed a new algorithm for continuous change
detection and classiﬁcation at high temporal frequency. By using all
available Landsat data, this approach allows reconstruction of the
history of the Earth surface in the Landsat TM and ETM+ era. Models
estimated by sines and cosines can predict Landsat observations at
any date assuming there is no land cover change. The CCDC algorithm
ﬂags land cover change by differencing the predicted and observed
Landsat data. It determines a pixel has experienced a land cover change
if it shows “change” for three consecutive times. The estimated time
series coefﬁcients (also including the RMSEs) were used for land cover
classiﬁcation. The reference data revealed that the CCDC results were
accurate for detecting land cover change, with producer's accuracy of
97.72% and user's accuracies of 85.60% in the spatial domain, and tem-
poral accuracy of 79.91%. The CCDC classiﬁcation results also showed
high overall accuracy of 90.20%.

The CCDC algorithm has many advantages. It is fully automated and
is capable of monitoring many kinds of land cover change as soon as
new images become available. Moreover, there are no empirical or glob-
al thresholds used in detecting change. The thresholds are generated
through the original observations and model estimation which are
done separately for each individual pixel. In this study, three times the
RMSE is recommended for thresholding, but more subtle changes can
be captured if two times the RMSE is used, which also result in more
false detection of land cover change. The continuous character of the
monitoring makes the algorithm capable of using as many images as
possible. Therefore, how fast the CCDC algorithm is able to ﬁnd change
and its corresponding land cover type is primarily dependent on the
frequency of available clear observations. This algorithm will improve
as the frequency of images from sensors like Landsat increases
(Arvidson et al., 2006). The opening of the archive from Earth Resources
Observation and Science (EROS) Data Center is the ﬁrst major step. Data
from the Landsat 8 should further increase the frequency of available
observations considering the much larger duty cycle for Landsat 8
compared with previous Landsat satellites. The two Sentinel 2A/2B
satellites are very similar to Landsat (Drusch et al., 2012). They have a
Sun-synchronous orbit at 786 km and a 10:30 a.m. descending node,

168

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

Partial forest cut

Fig. 15. Omission error in change detection for CCDC: partial forest cut illustrated by time series Band 5 surface reﬂectance.

Early change

Fig. 16. Omission error in change detection for CCDC: change occurred too early illustrated by time series Band 5 surface reﬂectance.

which is close to the Landsat local overpass time. The 13 spectral bands
span from the visible and the NIR to the SWIR and include all six Landsat
bands and at similar spatial resolution. Though there are some differ-
ences in widths and locations of the spectral bands and spatial resolu-
tions between Landsat and Sentinel 2A/2B (Drusch et al., 2012), with
some modiﬁcations or adjustments of the algorithm, it will be possible

to combine observations from Sentinel 2A/2B with Landsat observations
in the CCDC algorithm. With Sentinel 2A planned for launch in 2014 and
the second (2B) planed for launch 18 month later, there will be 5 days
repeat time for observations at the Equator and 2–3 days at mid-
latitudes (Berger, Moreno, Johannessen, Levelt, & Hanssen, 2012).
More importantly, the Sentinel data policy is free and open access to

Fig. 17. Commission error in change detection for CCDC: overﬁtting of time series model illustrated by time series Band 4 surface reﬂectance. The red circle indicates the incorrect
assignment of change.

Fig. 18. Commission error in change detection for CCDC: clouds missed three times consecutively illustrated by time series Band 2 surface reﬂectance. The red circle indicates the incorrect
assignment of change.

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

169

Fig. 19. Commission error in change detection for CCDC: low temporal frequency of the time series data illustrated by time series Band 5 surface reﬂectance. The red circle indicates the
incorrect assignment of change.

Fig. 20. Commission error in change detection for CCDC: small RMSE illustrated by time series Band 5 surface reﬂectance. The red circle indicates the incorrect assignment of change.

users. In principle, anybody can access acquired Sentinel data and there
is no difference between public, commercial and scientiﬁc use and be-
tween European and non-European users (Aschbacher & Milagro-
Pérez, 2012). By combining combined with Landsat 7 and 8, and two
Sentinel 2A and 2B, there would be typically 10 high resolution observa-
tions per month, greatly improving the availability of Landsat-like

observations such that we will be able to begin to monitor change in
near real-time at Landsat scales.

By using all available observations and considering each pixel sepa-
rately, the CCDC algorithm can overcome limitations like the failure of
the Scan Line Corrector (SLC) in Landsat 7 as the scan line gaps are
treated like clouds, cloud shadows, or snow and only the available

Fig. 21. Temporal error in change detection for CCDC: ﬁnding change later than it is observed in the reference data. The red circle is the “ﬁrst” changed observation identiﬁed by the CCDC
algorithm and the green circle is the ﬁrst time the change (a partial forest cut) can be observed in close examination of the images.

Fig. 22. Clear observations (Band 5) from Jun. to Sept. and model predictions for Aug. 1st every year between 1984 and 2011. Forest clearing occurred in 2005 for this pixel.

170

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

clear observations are used. This approach allows use of images from all
times of year or that are partially cloudy. It also can work in very hetero-
geneous areas that are reported to be problematic for some methods
(Huang et al., 2010; Masek et al., 2008). Moreover, the CCDC algorithm
does not need to perform relative normalization for each image like
many methods (Huang et al., 2010; Kennedy et al., 2007), as the time se-
ries model already includes the effects of phenology and sun angle dif-
ferences. By using many observations for model estimation, this
algorithm is not adversely affected by noise and the predicted data
form a more stable basis for comparison with new observations.
Fig. 22 illustrates the model-predicted Landsat observations at the
same time of year and the original clear Landsat observations during
growing season (from June to September) through the TM and ETM+
era for a deforestation pixel. It is clear that the model predicted observa-
tions are much more stable compared to the original observations and
this feature should signiﬁcantly reduce false positive errors in change
detection.

Additionally, land cover maps from any time period in the history of
the Landsat 4–8 era can be generated. More speciﬁcally, this algorithm
can also generate maps of land cover change over any speciﬁed time
period and provide information about the land cover categories before
and after change occurs by simply differencing the two land cover
maps generated by CCDC at different time. Usually, it is very dangerous
to compare two land cover maps from two different time to ﬁnd change,
as the areas of land cover change are relatively small compared to the
magnitude of errors in land cover classiﬁcation maps. This algorithm
avoids this problem when comparing two land cover maps to ﬁnd
change, as the land cover classiﬁcation algorithm is based on the
results of change detection. Moreover, this algorithm can also provide
information about inter-annual changes via the trend coefﬁcients. It is
possible to provide new land cover categories that are unique temporal-
ly, for example, the forest class can be separated into growing forest,
mature forest, and declining forest. This kind of information is important
for the study of vegetation health conditions and for carbon modeling,
but difﬁcult to derive from the conventional land cover classiﬁcation
methods.

The CCDC algorithm also has limitations. First of all, this algorithm is
computationally expensive and needs lots of data storage. Just the surface
reﬂectance and brightness temperature data takes more than 500 giga-
bytes for a total of 519 Landsat images. The algorithm updates the time se-
ries model every time new observations are available, which has the
beneﬁt of more accurate model estimation, but also greatly increases
the computational load. Second, this algorithm requires high temporal
frequency of clear observations. For places of persistent snow or clouds,
the model estimation may not be accurate as there are not enough obser-
vations to estimate the time series model. For extreme cases, if there are
less than 15 clear observations, the CCDC algorithm will not be able to ini-
tialize the time series model. For places outside of the United States this
problem will be more common. Third, we assume that the simple sinusoi-
dal model is able to estimate all kinds of land cover types, which may not
be valid for land cover types that have more intra-annual variation, such
as agriculture. A more complex time series model is needed if we want
to apply it to other parts of the world. Finally, though the data-driven
threshold used in this algorithm is able to handle many kinds of land
cover change for the Boston scene, it may have problems for places that
have large inter-annual variations. For example semi-arid regions that ex-
hibit high variability in the timing of phenological processes may prove
particularly challenging, as the data will ﬂuctuate more at some times of
the year and at this time a higher threshold is needed. Thresholds able
to change temporally may provide better accuracy.

Acknowledgments

We gratefully acknowledge the supports of the USGS Landsat
Science Team Program for Better Use of the Landsat Temporal Domain:
Monitoring Land Cover Type, Condition, and Change.

References

Anderson, J. R. (1976). A land use and land cover classiﬁcation system for use with remote

sensor data, Vol. 964. US Government Printing Ofﬁce.

Arvidson, T., Goward, S., Gasch, J., & Williams, D. (2006). Landsat-7 long-term acquisition
plan: Development and validation. Photogrammetric Engineering & Remote Sensing,
72(10), 1137–1146.

Aschbacher, J., & Milagro-Pérez, M. P. (2012). The European Earth monitoring (GMES)
programme: Status and perspectives. Remote Sensing of Environment, 120, 3–8.
Berger, M., Moreno, J., Johannessen, J. A., Levelt, P. F., & Hanssen, R. F. (2012). ESA's senti-
nel missions in support of Earth system science. Remote Sensing of Environment, 120,
84–90.

Breiman, L. (2001). Random forests. Machine Learning, 45, 5–32.
Brooks, E. B., Thomas, V. A., Wynne, R. H., & Coulston, J. W. (2012). Fitting the
multitemporal curve: A fourier series approach to the missing data problem in
remote sensing analysis. Geoscience and Remote Sensing, 50(9), 3340–3353.
Carrao, H., Goncalves, P., & Caetano, M. (2008). Contribution of multispectral and
multitemporal information from MODIS images to land cover classiﬁcation. Remote
Sensing of Environment, 112(3), 986–997.

Cohen, W. B., Yang, Z., & Kennedy, R. (2010). Detecting trends in forest disturbance and
recovery using yearly Landsat time series: 2. TimeSync—Tools for calibration and
validation. Remote Sensing of Environment, 114(12), 2911–2924.

Collins, J. B., & Woodcock, C. E. (1996). An assessment of several linear change detection
techniques for mapping forest mortality using multitemporal Landsat TM data.
Remote Sensing of Environment, 56, 66–77.

Coppin, P. R., & Bauer, M. E. (1996). Digital change detection in forest ecosystems with

remote sensing imagery. Remote Sensing Reviews, 13(3–4), 207–234.

Coppin, P., Jonckheere, I., Nackaerts, K., Muys, B., & Lambin, E. (2004). Digital change
detection methods in ecosystem monitoring: A review. International Journal of
Remote Sensing, 25(9), 1565–1596.

Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., et al. (2012).
Sentinel-2: ESA's optical high-resolution mission for GMES operational services.
Remote Sensing of Environment, 120, 25–36.

DuMouchel, W. H., & O'Brien, F. L. (1989). Integrating a robust option into a multiple
regression computing environment. Computer Science and Statistics: Proceedings
of the 21st Symposium on the Interface. Alexandria, VA American Statistical
Association.

Eklundh, L., Johansson, T., & Solberg, S. (2009). Mapping insect defoliation in Scots pine
with MODIS time-series data. Remote Sensing of Environment, 113(7), 1566–1573.
Fielding, A. H., & Bell, A. J. F. (1997). A review of methods for the assessment of prediction
errors in conservation presence/absence models. Environmental Conservation, 24(1),
38–49.

Foody, G. M. (2002). Status of land cover classiﬁcation accuracy assessment. Remote

Sensing of Environment, 80(1), 185–201.

Friedl, M.A., McIver, D. K., Hodges, J. C. F., Zhang, X. Y., Muchoney, D., Strahler, A. H., et al.
(2002). Global land cover mapping from MODIS: Algorithms and early results.
Remote Sensing of Environment, 83(1), 287–302.

Friedl, M.A., Menashe, D. S., Tan, B., Schneider, A., Ramankutty, N., Sibley, A., et al. (2010).
MODIS collection 5 global land cover: Algorithm reﬁnements and characterization of
new datasets. Remote Sensing of Environment, 114, 168–182.

Fuller, R. M., Smith, G. M., & Devereux, B. J. (2003). The characterisation and measurement
of land cover change through remote sensing: Problems in operational applications?
International Journal of Applied Earth Observation and Geoinformation, 4(3), 243–253.
Galford, G. L., Mustard, J. F., Melillo, J., Gendrin, A., Cerri, C. C., & Cerri, C. E. P. (2008).
Wavelet analysis of MODIS time series to detect expansion and intensiﬁcation of
row-crop agriculture in Brazil. Remote Sensing of Environment, 112(2), 576–587.
Goodwin, N. R., Coops, N. C., Wulder, M.A., Gillanders, Schroeder, T. A., & Nelson, T. (2008).
Estimation of insect infestation dynamics using a temporal sequence of Landsat data.
Remote Sensing of Environment, 112, 3680–3689.

Gopal, S., Woodcock, C. E., & Strahler, A. (1999). Fuzzy neural classiﬁcation of global land
cover from a 1 degree AVHRR Data Set. Remote Sensing of Environment, 67, 230–243.
Guerschman, J. P., Paruelo, J. M., Bella, C. D. I., Giallorenzi, M. C., & Pacin, F. (2003). Land
cover classiﬁcation in the Argentine Pampas using multi-temporal Landsat TM data.
International Journal of Remote Sensing, 24(17), 3381–3402.

Hansen, M. C., Defries, R. S., Townshend, J. R. G., & Sohlberg, R. (2000). Global land cover
classiﬁcation at 1 km spatial resolution using a classiﬁcation tree approach.
International Journal of Remote Sensing, 21(6 & 7), 1331–1364.

Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A., et al.
(2013). High-resolution global maps of 21st-century forest cover change. Science,
342(6160), 850–853.

Healey, S. P., Cohen, W. B., Yang, Z., & Krankina, O. N. (2005). Comparison of Tasseled
Cap-based Landsat data structure for use in forest disturbance detection. Remote
Sensing of Environment, 97, 301–310.

Holland, P. W., & Welsch, R. E. (1977). Robust regression using iteratively reweighted

least-squares. Theory and Methods, 813–827.

Homer, C., Huang, C., Yang, L., Wylie, B., & Coan, M. (2004). Development of a 2001
national land-cover database for the United States. Photogrammetric Engineering &
Remote Sensing, 70(7), 829–840.

Hostert, P., Röder, Achim, & Hill, J. (2003). Coupling spectral unmixing and trend analysis
for monitoring of long-term vegetation dynamics in Mediterranean rangelands.
Remote Sensing of Environment, 87, 183–197.

Huang, C., Goward, S. N., Masek, J. G., Thomas, N., Zhu, Z., & Vogelmann, J. E. (2010). An
automated approach for reconstructing recent forest disturbance history using
dense Landsat time series stacks. Remote Sensing of Environment, 114, 183–198.
Jensen, J. R., Rutchey, K., Koch, M. S., & Narumalani (1995). Inland wetland change
detection in the everglades water conservation area 2A using a time series of

Z. Zhu, C.E. Woodcock / Remote Sensing of Environment 144 (2014) 152–171

171

normalized remotely sensed data. Photogrammetric Engineering & Remote
Sensing, 61(2), 199–209.

Jin, S., & Sader, S. A. (2005). MODIS time-series imagery for forest disturbance detection
and quantiﬁcation of patch size effects. Remote Sensing of Environment, 99(4),
462–470.

Seto, K. C., Woodcock, C. E., Song, C., Huang, X., Lu, J., & Kaufmann, R. K. (2002). Monitor-
ing land-use change in the Pearl River Delta using Landsat TM. International Journal of
Remote Sensing, 23(10), 1985–2004.

Singh, A. (1989). Review Article Digital change detection techniques using remotely-

sensed data. International Journal of Remote Sensing, 10(6), 989–1003.

Jung, M., Henkel, K., Herold, M., & Churkina, G. (2006). Exploiting synergies of global land
cover products for carbon cycle modeling. Remote Sensing of Environment, 101(4),
534–553.

Street, J. O., Carroll, R. J., & Ruppert, D. (1988). A note on computing robust regression
estimates via iteratively reweighted least squares. American Statistical Association,
42(2), 152–154.

Kennedy, R. E., Cohen, W. B., & Schroeder, T. A. (2007). Trajectory-based change detection
for automated characterization of forest disturbance dynamics. Remote Sensing of
Environment, 110, 370–386.

Kennedy, R. E., Yang, Z., & Cohen, W. B. (2010). Detecting trends in forest disturbance and
recovery using yearly Landsat time series: 1. LandTrendr—Temporal segmentation
algorithms. Remote Sensing of Environment, 114(12), 2897–2910.

Lambin, E. F., & Strahler, A. H. (1994). Change-vector analysis in multitemporal space: A
tool to detect and categorize land-cover change processes using high temporal-
resolution satellite data. Remote Sensing of Environment, 48, 231–244.

Lark, R. M., & Stafford, J. V. (1997). Classiﬁcation as a ﬁrst step in the interpretation of
temporal and spatial variation of crop yield. Annals of Applied Biology, 130(1),
111–121.

Loveland, T. R., Reed, B. C., Brown, J. F., Ohlen, D. O., Zhu, Z., Yang, L. W. M. J., & Merchant, J.
W. (2000). Development of a global land cover characteristics database and IGBP
DISCover from 1 km AVHRR data. International Journal of Remote Sensing, 21(6–7),
1303–1330.

Lunetta, R. S., Knight, J. F., Ediriwickrema, J., Lyon, J. G., & Worthy, L. D. (2006). Land-cover
change detection using multi-temporal MODIS NDVI data. Remote Sensing of
Environment, 105(2), 142–154.

Masek, J. G., Huang, C., Wolfe, R., Cohen, W., Hall, F., Kutler, J., et al. (2008). North
American forest disturbance mapped from decadal Landsat record. Remote Sensing
of Environment, 112, 2914–2926.

Masek, J. G., Vermote, E. F., Saleous, N., Wolfe, R., Hall, E. F., Huemmrich, F., et al. (2006). A
Landsat surface reﬂectance data set for North America, 1990–2000. Geoscience and
Remote Sensing Letters, 3, 68–72.

Melaas, E. K., Friedl, M.A., & Zhu, Z. (2013). Detecting interannual variation in deciduous
broadleaf forest phenology using Landsat TM/ETM + data. Remote Sensing of
Environment, 132, 176–185.

O'Leary, D. P. (1990). Robust regression computation using iteratively reweighted least

squares. Society for Industrial and Applied Mathematics, 11(3), 466–480.

Pﬂugmacher, D., Cohen, W. B., & E Kennedy, R. (2012). Using Landsat-derived disturbance
history (1972–2010) to predict current forest structure. Remote Sensing of
Environment, 122, 146–165.

Rogan, J., Bumbarger, N., Kulakowski, D., Christman, Z. J., Runfola, D.M., & Blanchard, S. D.
(2010). Improving forest type discrimination with mixed lifeform classes using fuzzy
classiﬁcation thresholds informed by ﬁeld observations. Canadian Journal of Remote
Sensing, 36(6), 699–708.

Rogan, J., Franklin, J., & Roberts, D. A. (2002). A comparison of methods for monitoring
multitemporal vegetation change using Thematic Mapper imagery. Remote Sensing
of Environment, 80, 143–156.

Roy, D. P., Jin, Y., Lewis, P. E., & Justice, C. O. (2005). Prototyping a global algorithm for
systematic ﬁre-affected area mapping using MODIS time series data. Remote Sensing
of Environment, 97(2), 137–162.

Tan, B., Woodcock, C. E., Hu, J., Zhang, P., Ozdogan, M., Huang, D., et al. (2006). The impact
of gridding artifacts on the local spatial properties of MODIS data: Implications for
validation, compositing, and band-to-band registration across resolution. Remote
Sensing of Environment, 105(2), 98–114.

Tucker, C. J., Townshend, J. R. G., & Goff, T. E. (1985). African land-cover classiﬁcation using

satellite data. Science, 227(4685), 369–375.

Verbesselt, J., Hyndman, R., Newnham, G., & Culvenor, D. (2010). Detecting trend and sea-
sonal changes in satellite image time series. Remote Sensing of Environment, 114(1),
106–115.

Vermote, E. F., El Saleous, N., Justice, C. O., Kaufman, Y. J., Privette, J. L., et al. (1997). Atmo-
spheric correction of visible to middle-infrared EOS-MODIS data over land surfaces:
Background, operational algorithm, and validation. Journal of Geophysical Research,
102, 17131–17141.

Vogelmann, J. E., Tolk, B., & Zhu, Z. (2009). Monitoring forest changes in the southwestern
United States using multitemporal Landsat data. Remote Sensing of Environment, 113,
1739–1748.

Wolter, P. I., Mladenoft, D. S., & Crow, T. R. (1995). Improved forest classiﬁcation in the
northern lake states using multi-temporal Landsat imagery. Photogrammetry
Engineering & Remote Sensing, 61(9), 1129–1143.

Woodcock, C. E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W., et al.

(2008). Free access to Landsat imagery. Science, 320(5879), 1011.

Woodcock, C. E., Macomber, S. A., Pax-Lenney, M., & Cohen, W. B. (2001). Large area mon-
itoring of temperate forest change using Landsat data: Generalization across sensors,
time and space. Remote Sensing of Environment, 78(1–2), 194–203.

Woodcock, C. E., & Strahler, A. H. (1987). The factor of scale in remote sensing. Remote

Sensing of Environment, 21(3), 311–332.

Wulder, M.A., White, J. C., Goward, S. N., Masek, J. G., Irons, J. R., Herold, M., et al. (2008).
Landsat continuity: Issues and opportunities for land cover monitoring. Remote
Sensing of Environment, 112(3), 955–969.

Xin, Q., Olofsson, P., Zhu, Z., Tan, B., & Woodcock, C. E. (2012). Towards near real-time
monitoring of forest disturbance by fusion of MODIS and Landsat data. Remote
Sensing of Environment, 135, 234–247.

Zhang, Y., Rossow, W. B., Lacis, A. A., Oinas, V., & Mishchenko, M. I. (2004). Calculation of
radiative ﬂuxes from the surface to top of atmosphere based on ISCCP and other
global data sets: Reﬁnements of the radiative transfer model and the input data.
Journal of Geophysical Research, 109(19), 19105.

Zhu, Z., & Woodcock, C. E. (2012). Object-based cloud and cloud shadow detection in

Landsat imagery. Remote Sensing of Environment, 118(15), 83–94.

Zhu, Z., & Woodcock, C. E. (2014). Automated cloud, cloud shadow, and snow detection
based on multitemporal Landsat data: An algorithm designed speciﬁcally for monitoring
surface change, submitted to Remote Sensing of Environment.

Zhu, Z., Woodcock, C. E., & Olofsson, P. (2012). Continuous monitoring of forest disturbance

using all available Landsat imagery. Remote Sensing of Environment, 122, 75–91.

Schaaf, C. B., Gao, F., Strahler, A. H., Lucht, W., Li, X., Tsang, T., et al. (2002). First oper-
ational BRDF, albedo nadir reﬂectance products from MODIS. Remote Sensing of
Environment, 83(1), 135–148.

Zhu, Z., Woodcock, C. E., Rogan, J., & Kellndorfer, J. (2012). Assessment of spectral, polarimet-
ric, temporal, and spatial dimensions for urban and peri-urban land cover classiﬁcation
using Landsat and SAR data. Remote Sensing of Environment, 117, 72–82.

