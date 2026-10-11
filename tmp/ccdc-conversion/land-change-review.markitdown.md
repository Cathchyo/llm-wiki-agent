RemoteSensingofEnvironment282(2022)113266
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Review
Remote sensing of land change: A multifaceted perspective
Zhe Zhu*, Shi Qiu*, Su Ye*
Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT 06269, USA
A R T I C L E I N F O A B S T R A C T
Edited by Dr Marie Weiss The discipline of land change science has been evolving rapidly in the past decades. Remote sensing played a
major role in one of the essential components of land change science, which includes observation, monitoring,
Keywords: and characterization of land change. In this paper, we proposed a new framework of the multifaceted view of
Land change land change through the lens of remote sensing and recommended five facets of land change including change
Change agent
location, time, target, metric, and agent. We also evaluated the impacts of spatial, spectral, temporal, angular,
Change metric
and data-integration domains of the remotely sensed data on observing, monitoring, and characterization of
Change target
different facets of land change, as well as discussed some of the current land change products. We recommend
Land cover change
Land disturbance clarifying the specific land change facet being studied in remote sensing of land change, reporting multiple or all
Climate variability facets of land change in remote sensing products, shifting the focus from land cover change to specific change
Climate change metric and agent, integrating social science data and multi-sensor datasets for a deeper and fuller understanding
Succession of land change, and recognizing limitations and weaknesses of remote sensing in land change studies.
Time series
1. Introduction past decades, big advancements have been made in large-scale mapping
of land change based on remote sensing data, due to the rapidly growing
With the increasing contemporary concerns on climate change, amounts of earth observation satellites (Belward and Skøien, 2015; Ustin
global environmental change, and sustainability, land change science and Middleton, 2021), the free and open data policy (Woodcock et al.,
has emerged as a unique science direction for addressing these chal- 2008; Wulder et al., 2012; Zhu et al., 2019), the analysis-ready data
lenging issues (Gutman et al., 2004; Rindfuss et al., 2004; Turner et al., format (Dwyer et al., 2018; Frantz, 2019), the state-of-art cloud
2007). Land change science, defined as “the interdisciplinary field [that] computing platform that not only provides massive parallel computing
seeks to understand the dynamics of land cover and land use as a capability but also a huge amount of online datasets (Gorelick et al.,
coupled human-environment system to address theory, concepts, 2017), and the improved capability of new algorithms for land change
models, and applications relevant to environmental and societal prob- detection (Banskota et al., 2014; Kennedy et al., 2014; Zhu, 2017).
lems, including the intersection of the two” (Turner et al., 2007), has Recently, a paradigm shift from change detection of two points in time
many components, in which one of the most fundamental and critical to monitoring and tracking change continuously in time is observed in
components is the observation, monitoring, and characterization of land the remote sensing community, where the use of dense time-series ob-
change. servations gain more popularity with a capability of retrieving new land
The terrestrial surface of the Earth has been changing at an un- change information, such as subtle changes in ecosystem health and
precedented rate. More than half of the Earth’s ice-free land surface has condition, and long-term trend of the vegetation productivity (Wood-
been modified by humans (Ellis et al., 2010), and almost all land sur- cock et al., 2020). Moreover, land change information can now be
faces have been influenced by climate change and various kinds of land monitored in near real-time (Shang et al., 2022; Tang et al., 2020;
disturbances (Dale, 1997; Potter et al., 2003). Remote sensing, partic- Verbesselt et al., 2012; Xin et al., 2013; Ye et al., 2021a), which greatly
ularly satellite remote sensing, that can provide synoptic and repeated improves its value to resource managers and policymakers. We have also
measurements of the global land surface at different spectral, spatial, witnessed a proliferation of land change characterization algorithms
and temporal resolutions, is of great importance for studying global land (Zhu, 2017), mostly focusing on the “from-to” information, that is, land
change (Justice et al., 1998; Roy et al., 2014; Sellers et al., 1995). In the cover and/or land use information before and after the change (Hansen
* Corresponding authors.
E-mail addresses: zhe@uconn.edu (Z. Zhu), shi.qiu@uconn.edu (S. Qiu), su.ye@uconn.edu (S. Ye).
https://doi.org/10.1016/j.rse.2022.113266
Received 26 February 2022; Received in revised form 28 August 2022; Accepted 7 September 2022
Availableonline7October2022
0034-4257/©2022TheAuthors.PublishedbyElsevierInc.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
and Loveland, 2012; Pricope et al., 2019). It should be noted that though 2019). Pouliot and Latifovic (2016) mapped the multifaceted nature of
“land cover” (the physical properties at the Earth’s surface) and “land land change, however, it was only a case study in the Athabasca oil sands
use” (the social, economic, and cultural utility of land) are quite distinct region of Canada and has not reviewed the multifaceted land change in a
(Turner, 1997), they are often grouped together in remote sensing systematic way. According to our knowledge, this paper is the first work
products, and “land cover” is usually used as a surrogate for under- for synopsizing the detection and characterization of land change as a
standing “land use”, such as including cropland and developed land in five-facet task in a systematic manner, paving the way for operational-
the categories of land cover (Anderson et al., 1976). Considering remote izing a holistic examination of land change as well as accomplishing
sensing data provide information on land cover, rather than on land use, efficient communication on related concepts - rather than a synthesis of
we will mainly focus on land cover change hereafter. sensor or methodological comparison which has been widely touched in
In this paper, we propose the framework of a multifaceted perspec- previous works.
tive in remote sensing of land change, in which the change in land cover We will first discuss all five facets of land change as well as their
is only one of the components viewed from one of the five facets of land relationship through the lens of remote sensing. Next, we will discuss the
change - the target of change or what is changing. Basically, if we detect remote sensing issues in spectral, spatial, temporal, angular, and data-
change in satellite spectral bands, we can extract the land change in- integration domains in observing, monitoring, and characterization of
formation to answer five different questions, that are, when (change different facets of land change. Finally, we will discuss some of the
time), where (change location), what (change target), how (change current land change products derived from remote sensing data and
metric), and why (change agent) the change happened. Each of the conclude with a few recommendations. While most examples of this
questions will occupy one facet of the change cube that contains the paper were illustrated using time-series datasets given by our expertise
spectral change information derived from remotely sensed data (Fig. 1). on this topic, we do appreciate the spatial and spectral merits of other
The facet on the top of the change cube is left empty on purpose, as there data types (e.g., LiDAR, Hyperspectral, and Unmanned Aerial Vehicle
may be other facets of land change that are not discussed in this paper. (UAV)), which are equally important for characterizing land change. It
The two facets of “Time” and “Location” provide information on the has been our recognition that the integration of multiple data sources
detection and monitoring of land change, and the other three facets of can provide a unique opportunity for the success of monitoring multi-
“Target”, “Metric”, and “Agent” are related to the characterization of faced land change (will be discussed in Section 4.5).
land change. Indeed, the topic of land change has been extensively
reviewed in the remote sensing community, but most focused on change 2. The five facets of land change
detection techniques (i.e., when and where) (Coppin et al., 2004; Hus-
sain et al., 2013; Lu et al., 2004; Singh, 1989; Zhu, 2017). Only very few If the remote sensing system is well designed for capturing the spe-
reviews mentioned other facets such as change target (Hansen and cific land change type, it is possible to extract land change information
Loveland, 2012; Warner et al., 2009; Wulder et al., 2018), change metric for five different facets based on the remotely sensed observations
(Go´mez et al., 2016; Kennedy et al., 2009; Vogelmann et al., 2016), and collected before, during, and/or after the land change (Fig. 2).
change agent (Kennedy et al., 2015; Sebald et al., 2021; Shimizu et al.,
Fig. 1. The five facets proposed for observation, monitoring, and characterization of land change using remotely sensed data. It is worth noting that not all land
change agents will lead to a change in change target or land cover in this case, and some of the change patches displayed in the other four facets are not shown (e.g.,
stress, flooding, and agriculture activity) or only partially shown (e.g., wind, construction, and regrowth) in the facet of change target.
2

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Fig. 2. Hierarchical classification system for the five facets of land change.
2.1. Where - change location 2.2. When - change time
The first facet of land change is to answer the question of where the The second facet of land change is to answer the question of when the
change has occurred or determine the change location. Theoretically, by change occurred or determine the change time. Basically, the closer the
differencing two georeferenced remotely sensed images collected at a two images are selected for detecting change, the more accurate the
different time from the same spectral band and same location, any kind change time can be determined. Compared to detecting change based on
of land surface change that occurred between the two dates would have real images, there are also new change detection methods that difference
larger difference values than places that have not changed. By using a the model predicted values with actual remote sensing observations to
simple threshold, the location of change could be identified. The land identify land change (Verbesselt et al., 2012; Zhu and Woodcock, 2014)
change detected in this way is sometimes called “spectral change” and the detected change time is determined based on how soon the new
(Brown et al., 2020; Healey et al., 2018; Xian et al., 2022), as clearly clear observations are collected for each pixel location. These time-
there is a spectral value change between the two dates of the remotely series-based approaches do not need to wait for two clear remote
sensed images, but this does not always correspond to the changes on the sensing images and can provide more rapid change detection results.
land surface. Other factors, such as image registration, atmospheric The remote sensing community has shifted from using images collected
condition, natural soil wetness fluctuation, vegetation phenology, decades apart (Homer et al., 2007; Masek et al., 2008), to annual (Huang
sensor-solar-geometry, and topography illumination, may also et al., 2010; Kennedy et al., 2010), and is currently shifting all the way to
contribute to the spectral change (Kennedy et al., 2014; Zhu, 2017). near-real-time change detection (Shang et al., 2022; Tang et al., 2019;
Therefore, one of the most foundational steps before the remotely sensed Verbesselt et al., 2012; Woodcock et al., 2020; Ye et al., 2021a). This is
images are used for detecting land change is removing or at least particularly true with the successful launch of Sentinel-2 A/B (Drusch
reducing changes in spectral values that are not caused by land surface et al., 2012), Landsat 9 (Masek et al., 2020), and the hundreds of
change. Advanced algorithms have been developed to provide more orbiting CubeSats (Huang and Roy, 2021), that could provide subweekly
accurate image registration results (Gao et al., 2009; Yan et al., 2016), or even daily land surface observations at medium to high spatial res-
perform atmospheric correction and cloud/cloud shadow detection olutions (Li and Roy, 2017; Roy et al., 2021).
(Masek et al., 2006; Qiu et al., 2019b; Zhu and Woodcock, 2012),
include precipitation information (Tollerud et al., 2020), model and 2.3. What - change target
exclude seasonality (Verbesselt et al., 2010; Zhu et al., 2020; Zhu and
Woodcock, 2014), apply Bidirectional Reflectance Distribution Function The third and probably the most studied facet of land change is to
(BRDF) to correct sensor-solar-geometry (Roy et al., 2016; Schaaf et al., answer the question of what is changing or determining the change
2002), remove bandpass difference (Claverie et al., 2018; Shang and target. The change target is sometimes defined as changes in categorical
Zhu, 2019), and perform topographic correction (Buchner et al., 2020; classes such as land cover type (e.g., forest, urban, water, grass, shrub,
Tan et al., 2013). It is worth noting that though these algorithms have snow/ice, agriculture, etc.), or defined as changes in continuous variables
the potential to reduce spectral changes that are not related to changes of biophysical/biochemical parameters, such as Impervious Surface
on land surfaces, they may also introduce artifacts, and it is not always Area (ISA), land surface temperature, Leaf Area Index (LAI), vegetation
necessary to apply all these algorithms before conducting change height, biomass, leaf moisture content, leaf chlorophyll content, etc.
detection (Qiu et al., 2019a; Song et al., 2001). Remotely sensed data contain rich information on the characteristics of
the land surface. A feature space of more than a few dozens to even
hundreds of dimensions could be created from the electromagnetic ra-
diation (EMR) that is recorded at different wavelengths, the texture of
3

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
the spectral bands, and the intra-annual/inter-annual temporal trajec- et al., 2014; Petit et al., 2001). As remotely sensed data measure land
tory from the time series observations, which could be further used to surface reflected or emitted EMR, any state transition can be reflected as
determine the land cover based on image classification (Go´mez et al., surface reflectance changes from the spectral bands, making remote
2016; Pouliot and Latifovic, 2016) or to estimate the biophysical/ sensing data particularly useful for tracking the change trajectories and
biochemical parameters based on machine learning or regression from characterizing the specific change process based on different change
empirical models (Garbulsky et al., 2011; Lin et al., 2020; Verrelst et al., metrics (Comber and Wulder, 2019; Kennedy et al., 2014). The most
2015). Recently, the deep-learning-based approaches, particularly important remote sensing observations for calculating different change
Convolutional Neural Network (CNN), have shown better performance metrics are the ones that are collected during the land change events.
in land cover classification compared to the traditional machine- According to the change duration metric (how long the change event
learning-based methods (Kussul et al., 2017; Liu et al., 2021b; Pouliot last), land change can be divided into abrupt change and gradual
et al., 2021), and are capable of incorporating the spatial domain of the change. Most remote sensing change detection algorithms were devel-
remote sensing data by automatically extracting a suitable representa- oped to detect abrupt changes that occur within a short time in response
tion of the remote sensing data through a hierarchy of spatial filters at to a punctuated event, as these changes can be detected directly by
different sizes, which avoids the feature creation and selection processes comparing two remotely sensed images collected at different time points
that most traditional machine learning methods require in advance for before and after the change event (Coppin and Bauer, 1996; Woodcock
preparation of the classification predictors (Molinier et al., 2021). et al., 2020). On the other hand, gradual changes usually last for a much
Theoretically, if we can create land cover or biophysical/biochem- longer time as a result of a variety of causes such as damage to vege-
ical parameter maps accurately at different time points, we can compare tation from disease and insects, ecological succession, and climate
their maps to identify changes in different land cover or a specific bio- change (Lawrence, 2005; Vogelmann et al., 2012, 2016). There are also
physical/biochemical parameter. However, as land changes are usually remote sensing methods developed to quantify gradual changes based
very small in size (e.g., 1–5% of the land surface) (Hansen et al., 2013; on long-term time series observations (e.g., >10 years) with the capa-
Song et al., 2018), and all image classification and biophysical/ bility of separating co-existing gradual and abrupt changes (De Jong
biochemical parameter retrieval algorithms contain errors, comparing et al., 2012; Vogelmann et al., 2016; Zhu et al., 2016a), enabling more
maps of land cover or biophysical/biochemical parameters at different accurate estimation of gradual changes.
time points to detect land change may lead to compounded errors in the Based on the change magnitude metric (spectral distance between
final change map at a magnitude way larger than the total change area the changed and unchanged observations), land change can be divided
(Olofsson et al., 2013). Therefore, land change is usually better detected into subtle change and dramatic change. Subtle change modifies the
based on the magnitude of spectral change and if a spectral change is land cover, and the impact could be either short-lived, which is some-
detected, we can then estimate land cover or biophysical/biochemical times called ephemeral change (e.g., gypsy moth infestation and flood-
parameters before and after the spectral change (Deng and Zhu, 2020; ing), or persistent at a much longer time (e.g., >1 year), which is also
Jin et al., 2019; Latifovic and Pouliot, 2005; Xian et al., 2009; Zhu and called gradual change. Dramatic change is mainly caused by severe
Woodcock, 2014). It is worth noting that even if there is a spectral disturbance events, which may lead to land cover conversion. Dramatic
change detected, the classified categorical land cover type may still be change is relatively easy to identify as large differences will be observed
the same (Hermosilla et al., 2018), as the land change that occurred on in remotely sensed imagery, but subtle change detection is much more
this land cover may not be dramatic enough to change the land cover difficult and requires change agent- or land cover-specific algorithms
type, and we usually call this land cover modification or land cover with a careful model parameter calibration (Ye et al., 2021b). The
condition change (Comber and Wulder, 2019; Rogan et al., 2008). For change direction, measured by the angularity of the spectral change
example, if forest cover is defined as trees covering >10% of the pixel vector, indicates the nature of the change process (Lambin and Strahler,
following the U.S. Forest Service definition (Riemann et al., 2010), and if 1994) and has the potential of providing more accurate detection of land
selective logging is reducing forest cover from 90% to 30%, we are very change when used simultaneously with change magnitude (Zhu et al.,
likely to detect a spectral change, but based on the definition, the land 2020). It is worth noting that other change metrics could also provide
cover is still forest before and after the spectral change. However, if the valuable information for characterizing how the land surface is chang-
forest harvest is reducing forest cover from 90% to 5%, then the land ing, such as time since last change, spectral stability period, and
cover will be likely changed from forest to barren or grass, and we occurrence change intensity (Brown et al., 2020; Pekel et al., 2016).
usually call this land cover conversion, which is corresponding to more
substantial land changes that cause land cover transitions from one to 2.5. Why - change agent
another. In the remote sensing community, huge efforts have been given
to land cover conversions (Chowdhury et al., 2021; Colditz et al., 2014; The fifth facet of land change is to answer the question of why it is
Homer et al., 2015, 2020; Pouliot et al., 2021, Pouliot et al., 2014), but changing or determine the change agent. Climate, land disturbance, and
fewer studies were targeted on the land cover modification, which often succession are the three major change agents that occur at quite
occur at a spatial scale similar to or even larger than land cover con- different timescales (Fig. 3). Though the three change agents are quite
version (Asner et al., 2005; Qin et al., 2021; Rigge et al., 2019). different conceptually, they interplay with various kinds of positive and
Detecting land cover modification is inherently difficult in remote negative feedbacks (Dale et al., 2001; Guo et al., 2018; Johnson and
sensing, as the subtle spectral change signal may be at a change Miyanishi, 2021; Laflower et al., 2016; Seidl et al., 2017).
magnitude similar to other background noise. Subpixel analyzing Land disturbance has been defined in various ways (Clements, 1916;
methods, such as spectral mixture analysis (Asner et al., 2009), contin- Grime, 1977; Sousa, 1984; Turner, 2010; White and Pickett, 1985), and
uous fields (Hansen and DeFries, 2004), fuzzy (or soft) classification one of the most commonly used definitions by ecologists is “any rela-
(Foody and Doan, 2007), and the continuous subpixel monitoring tively discrete event in time that disrupts ecosystems, community or
approach (Deng and Zhu, 2020), have shown their capability in the population structure and changes resources, substrate availability, or
detection of land cover modification at subpixel scales. the physical environment” (White and Pickett, 1985). Most of the time,
land disturbance occurs in a very short time ranging from hours to years
2.4. How - change metric and can be anthropogenic or natural. Anthropogenic disturbance,
sometimes called mechanical change or land use change, refers to
The fourth facet of land change is to answer the question of how it is human activity-related land change, such as forest management, agricul-
changing by a number of change metrics, such as change magnitude, ture activity, construction, and prescribed fire. Natural disturbance can be
change duration, and change direction (Go´mez et al., 2016; Kennedy further divided into abiotic disturbance, such as wildfire, flooding,
4

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Fig. 3. Timescales applicable to weather, climate variability, climate change, land disturbance, and succession.
tornado, hurricane, drought, geological hazard, and biotic disturbance, well-known four-stage Oliver and Larson Model (Oliver and Larson,
such as insect infestation, pathogens, and invasive species. It is worth noting 1996). Primary succession is the process that plants and animals colo-
that there is a long debate on whether drought should be included as one nize a barren habitat for the first time, which could take hundreds of
type of land disturbance, and it has only started to be considered as a years, while secondary succession begins after a major disturbance that
disturbance type over the past decade (Peters et al., 2011). Fire can be transformed the original landscape. As remote sensing has a relatively
both natural (wildfire) and anthropogenic (prescribed fire) (Bowman short history, and the longest earth observation satellite, such as Land-
et al., 2011), and remote sensing can detect both burning fires and fire sat, only has a half-century record (Wulder et al., 2022), it is not ideal to
burned areas (Justice et al., 2002; Lentile et al., 2006). Most remote quantify primary succession, and there are only limited studies on this
sensing algorithms developed for detecting disturbance are only limited topic (e.g., Knoflach et al., 2021; Lawrence, 2005). However, remote
to a single change target, such as forest disturbance (Healey et al., 2018; sensing data have been frequently used for quantifying secondary suc-
Huang et al., 2010; Jin and Sader, 2005; Kennedy et al., 2007; Zhu et al., cession after disturbance with regards to its recovery rate or succession
2012a), and only a few algorithms can provide more general disturbance stages. The post-disturbance recovery rate was often estimated via
results, such as the MODIS Global Disturbance Index (MGDI) algorithm spectral recovery rate as the proxy from the temporal trend analysis of
(Mildrexler et al., 2009), the Landsat-based detection of Trends in satellite time series (Bartels et al., 2016; Kennedy et al., 2010; P´erez-
Disturbance and Recovery (LandTrendr) algorithm (Kennedy et al., Cabello et al., 2021; Senf et al., 2015; White et al., 2022; Zhao et al.,
2015), and the COntinuous monitoring of Land Disturbance (COLD) 2018). Combined with ground measurements (Huang et al., 2019; White
algorithm (Zhu et al., 2020). As disturbance will create a spectral change et al., 2019) and laser scanning data (Chirici et al., 2020; White et al.,
signal that deviates from the normal data fluctuation, it can be better 2018), the use of dense satellite time series has enabled a better evalu-
captured after the normal data fluctuation is well defined and modeled. ation for re-establishment of forests over large areas (Chu et al., 2016;
However, for certain disturbance types, such as selective logging and in- White et al., 2017), offering new insights on forests resilience (Forzieri
sect infestation, they may only change a small fraction of the pixel or et al., 2022; Senf and Seidl, 2022), recovery characterization (Bartels
slightly change the health condition of the ecosystem, which makes et al., 2016), and climate effects (Sulla-Menashe et al., 2018). Differ-
these kinds of disturbance agents extremely difficult to detect and ently, the succession stages were often characterized through a single-
distinguish in remote sensing data (Asner et al., 2005; Senf et al., 2017; date species mapping based on optical or LiDAR datasets (Osin´ska-
Ye et al., 2021b). Skotak et al., 2019; Raitsos et al., 2013; Rittenhouse et al., 2022), and
Unlike weather that describes “snapshot-like” atmospheric condition sometimes required to be linked to field observations (e.g., Hall et al.,
(e.g., rainstorms and tropical cyclones) that changes every hour, day, 1991).
and maybe months, the term “climate” depicts the mean and variability Observing and monitoring places where disturbance, climate, and
of temperature, precipitation, or wind for a much longer time, ranging succession occurred is important, but what is more critical is to identify
from months to centuries. Climate variability refers to the short-term (e. the specific change agent, and this effort is sometimes called change
g., months, seasons, or years) variation in climate patterns such as El- agent characterization (or attribution) in remote sensing. Among the
Nin˜o Southern Oscillation, and climate change refers to the long-term variety of possible land change agents, we can divide them into direct or
changes (e.g., decades or centuries) in climates such as global warm- proximate causes (e.g., agriculture activity, construction, fire, forest
ing and sea-level rise. Climate variability can be detected using remotely management, etc.) and distal or underlying driving forces (e.g., human
sensed vegetation indices by comparing a certain year with a baseline population dynamics, human attitudes and behavior, economic trans-
computed from a longer satellite time series (Saleska et al., 2007; formation, climate change, etc.) (Geist and Lambin, 2002; Lambin et al.,
Samanta et al., 2010), and climate change can be also evaluated based 2001). A majority of the remote sensing studies are only focusing on
on the long-term trend of remotely sensed vegetation indices (Myneni creating change agent maps of the proximate causes, in which some of
et al., 1997; Zhu et al., 2016b). As both climate variability and distur- them are more focused on anthropogenic agents (Kennedy et al., 2015;
bance will cause remote sensing observations to deviate abruptly from Shimizu et al., 2019) and others are more of a natural agent focus (Oeser
their past trajectories with a change magnitude larger than a pre-defined et al., 2017; Schroeder et al., 2017). Most of the remotely sensed change
threshold, climate variability is sometimes identified as one kind of agent types are quite broad, and some of the typical categories include
disturbance type in remote sensing (Huete, 2016), and will be particu- agriculture activity, forest management, construction, insect, windstorm, fire,
larly noticeable in semiarid areas where the amount of precipitation will flooding, and vegetation stress. Satellite time series observation collected
have a large impact on the local ecosystems. before, during, and/or after the disturbance events and supervised ma-
Climate change and land disturbance initiate succession (e.g., pri- chine learning classifiers are usually used together for change agent
mary succession and secondary succession), which is defined as the classification (Shimizu et al., 2019), and the inclusion of spatial domain
process that the structure of a biological community changes over time of remote sensing data is frequently found helpful in improving sepa-
(Huston and Smith, 1987). The process of succession is often accom- ration of different change agents (Kennedy et al., 2015; Sebald et al.,
panied with a sequence of biotic community replacement, such as the 2021; Shimizu et al., 2019). It should be noted that remote sensing of
5

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
change agent is never an easy task. Changes of different agents can caused by vegetation phenology and abrupt/gradual land surface
happen simultaneously or in close proximity to each other, which makes changes), as well as the spectral changes that have nothing to do with
untangling these agents extremely hard sometimes (e.g., harvest land change on the ground, such as atmospheric influences and data
following by a pest infestation in forests). Moreover, different distur- noise. On the other hand, land surface change (the region within red
bance agents may result in the same or similar change consequences (for dashed line in Fig. 4), which shared the same area as land cover change,
example, windstorms, wildfire, insect infestation, and drought will all has also gained a lot of visibility in remote sensing studies of land change
lead to defoliation), which makes the spectral change signature very (Brown et al., 2020; de Beurs et al., 2015; Sohl et al., 2004; Woodcock
similar among the different agents. Additionally, it is extremely chal- et al., 2020; Zhu and Woodcock, 2014). Land surface change or land
lenging to collect high-quality change agent training data consistently cover change includes all land change (e.g., all kinds of land cover
across a large geographic region at a national or global scale. Synthe- conversions and modifications) that occurs on the Earth’s surface,
sizing all the land change agent related open data, such as the Land except for cyclic changes that are often caused by vegetation phenology
Change Monitoring, Assessment, and Projection (LCMAP) reference and snow/ice seasonality. Biophysical/biochemical parameter change
sample (Pengra et al., 2020), LANDFIRE reference data (Rollins, 2009), (the purple rectangle in Fig. 4) includes land surface change (or land
USGS Land Cover Trends data (Loveland et al., 2002), USFA National cover change), that will inevitably lead to changes in certain biophysi-
Insect and Disease Survey database (Johnson and Wittwer, 2008), NASA cal/biochemical parameters, as well as cyclic changes that cause
Cooperative Open Online Landslide Repository (COOLR) Landslide data changes in LAI and leaf chlorophyll contents. Land disturbances (the
(Kirschbaum et al., 2010), NOAA Severe Weather Data Inventory light red rectangle in Fig. 4) are discrete events that disrupts ecosystems,
(SWDI) (NOAA, 2022), and Monitoring Trends in Burn Severity (MTBS) and if they are severe enough, they can lead to land cover conversion,
data (Eidenshink et al., 2007), and refining training data based on prior and are sometimes overlapped with climate variability (e.g., drought).
knowledge of change agent characteristics could be a potential solution. Climate variability (the light yellow rectangle in Fig. 4) and climate
Remote sensing can also help better understand the underlying driving change (the dark yellow rectangle in Fig. 4) are driven by the mean and
forces behind global land change based on qualifying and quantifying variability of temperature, precipitation, or wind, and climate vari-
human-environment interaction at a multitude of spatial and temporal ability refers to the short-term variations in climate patterns (e.g.,
scales (Pricope et al., 2019). By integrating social science data and sta- months, seasons, or years) while climate change refers to the long-term
tistical methods such as fixed-effects models (Firebaugh et al., 2013), it changes (e.g., decades or centuries). Both can lead to land cover con-
is possible to provide deeper understanding of the complex land change version when it is persistent or have a significant impact on the land
transitions and teleconnection/telecoupling (Friis et al., 2016; Lambin surface. Succession (the green rectangle in Fig. 4), defined as the process
et al., 2001; NRC, 1998, 1999; Pricope et al., 2019; Seto et al., 2012). of the structure of a biological community changing over time can also
change the land cover categories (e.g., transitioned from grass to shrub,
3. Relationship of various kinds of change terminologies and all the way to forest) with enough time and adequate recovery speed
(Brown et al., 2020). Note that land disturbance, climate variability,
A variety of change terminologies have been introduced and used for climate change, and succession may all lead to categorical land cover
remote sensing of land change. Though they are all related to land change - land cover conversion (the rectangles filled with stripes in
change, their relationship is rather complicated and confusing. Fig. 4 Fig. 4), but most of the time they will only lead to within-state modifi-
illustrates the relationship of some widely used land change terminol- cations or condition change - land cover modifications (the rectangles
ogies, including spectral change, land surface change, land cover filled with dots in Fig. 4), such as changes in the value of a certain
change, land cover modification, land cover conversion, land distur- biophysical/biochemical parameter.
bance, climate variability, climate change, succession, and biophysical/
biochemical parameter change. Spectral change (the grey rectangle in 4. The current issues for monitoring multifaceted land change
Fig. 4), defined as the temporal change in remote sensing spectral value,
has been widely used in many remote sensing change detection studies It would be ideal that the remote sensor was designed to detect all
(Cohen and Goward, 2004; Coppin and Bauer, 1996; Verstraete and land changes with the right spectral, spatial, temporal resolutions, and
Pinty, 1996). Spectral change is the broadest of all land change termi- viewing angles. However, the practical issues from spectral, spatial,
nologies that could include all kinds of land changes (e.g., changes temporal, angular, and data-integration domains have hindered the
remote sensing platform’s capability of detecting and characterizing
land change.
4.1. The spectral issues
Visible, Near Infrared (NIR), Shortwave Infrared (SWIR), thermal,
and microwave electromagnetic radiation is absorbed, reflected, and
transmitted in different ways by terrestrial materials. Land changes, in
essence, are partial or complete changes of the terrestrial materials, and
hence a certain type of land changes can manifest distinct detection
performance at different wavelengths. In practice, if the spectral ranges
capable of separating the two different types of land surfaces are not
included in the remote sensing bands, it is almost impossible to detect
change location and time, not to mention accurate identification of
change target, metric, and agent. For example, when forests are burned,
the land-change signals are barely discernable from the visible Landsat
bands, such as blue, green, and red, and certain microwave bands (e.g.,
C-Band). In contrast, much larger spectral differences could be observed
between before- and after-change images as decreasing NIR and
Fig. 4. Relationship of some widely used land change terminologies, including
spectral change, land surface change, land cover change, land cover conversion, increasing SWIR1, SWIR2, and thermal bands (Fig. 5) due to post-fire
land cover modification, land disturbance, climate variability, climate change, char, reduced vegetation and water content, so these bands are critical
succession, and biophysical/biochemical parameter change. to fire damage assessment. Some studies also reported that narrow
6

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Fig. 5. Spectral change at different band wavelengths induced by a fire disturbance. The spectral differences are subtle in visible bands and the microwave band but
are substantial in NIR, SWIR, and thermal bands. Blue, green, red, NIR, SWIR1, SWIR2, and thermal bands were derived from Landsat 8 surface reflectance and
brightness temperature data, and microwave C-Band was selected from Sentinel-1C-Band synthetic aperture radar data with dual-band cross-polarization (Vertical
transmit/Horizontal receive) at descending orbit. All the remotely sensed images were acquired at central latitude/longitude (40.100 /(cid:0) 120.607) in June 2019 and
2020 and clipped to the same geographic extent (1001 pixels by 401 pixels) at 30 m spatial resolution. (For interpretation of the references to color in this figure
legend, the reader is referred to the web version of this article.)
spectral bands, such as red edge bands (680–730 nm), are particularly sensing bands/indices can help identify biological change phases: for
useful for discriminating subtle/gradual vegetation changes which are example, Red-Green Index (RGI) was often used to indicate the red stage
often unrecognizable from broadband remote sensing (Ortiz et al., 2013; (i.e., the needles turn red) for a beetle-infestation process (Coops et al.,
Xie et al., 2018). Generally, the selection of involved bands/indices is of 2006), while a substantial drop of Normalized Difference Vegetation
enormous importance to the effectiveness of such change detection Index (NDVI) could be treated as a sign of the grey stage (i.e., all foliage
tasks, which necessitates more studies on target-based approaches for drop) (Hart and Veblen, 2015). A successful change characterization
determining optimal spectral inputs (Yang et al., 2022; Ye et al., 2021b). requires careful investigation of the most relevant spectral inputs; more
Besides change detection, the spectral selection is also critical to important might be recognizing change characterization as a multi-
characterizing change target, agent, and metric. The band selection is spectral problem for a thorough examination of a change process.
known as the prerequisite for the success of a cover classification task to
identify change targets such as before-change and after-change cover
4.2. The spatial issues
types (Guo et al., 2006). While given cover types may have similar and
indistinguishable spectral responses at specific points in time, in most
The spatial resolution, defined as the dimension in meters of the
cases, the spectral behavior of different cover types varies over time, and
ground-projected Instantaneous-Field-of-View (IFOV), determines the
the combined ability to look both multi-spectrally and multi-temporally
minimum mapping unit on the ground (e.g., a Landsat 8 pixel covers a
may provide new insights for discriminating cover types (Fang et al., 30 m ×30 m land area). Remotely sensed images from various kinds of
2020; Key et al., 2001; Pasquarella et al., 2018; Zhu et al., 2012b). The
platforms can provide a wide range of spatial resolutions from sub-
multispectral change, also known as spectral change vector, often pre- meters to tens of kilometers (Belward and Skøien, 2015). The choice
sents diagnostic attributes such as change direction (Lambin and
of spatial resolution also has important implications for the downstream
Strahler, 1994) and has been employed as the key variable for catego-
satellite-based product (Mascorro et al., 2015). Remote sensing data
rizing change agents (Zhang et al., 2022). The change metrics, such as
with a higher spatial resolution are generally preferred as the input for
“subtle vs dramatic” in the change magnitude, are also spectrum
change detection, as the higher the spatial resolution, the better the
dependent. Furthermore, change magnitudes based on different remote
capability in detecting small-scale land changes. However, when the
7

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
spatial resolution is too high (e.g., <1 m), the image quality may be land cover also directly determines the scope of the change (mainly land
severely impacted by the shadow of land surface features (Bruzzone and cover conversion) under investigation. For example, if a forest class is
Bovolo, 2012). On the other hand, if the spatial resolution is too coarse, defined as >10% of tree cover, and grassland is defined as a >10% of
small-sized land surface changes may not exhibit obvious spectral sig- grass cover, the pixel will be considered to have undergone land cover
nals (see the MODIS images in Fig. 6), and the large difference in conversion from the forest class to grass class only if >90% of the trees
point-spread-function and BRDF impacts will lead to new data noise and are removed from a fully forested pixel and replaced by grassland
make change signals even more diluted (Xin et al., 2013). Therefore, (Fig. 6). This is because the land cover definition is usually resource-
medium resolution satellites with resolution between 10 and 100 m, driven, and when classes meet the definition of more than one cate-
such as SPOT, Sentinel-2, and Landsat, are often more preferable than gory, classes with a higher priority are given preference in assigning
the coarse resolution sensors for mapping cover type change (Martin and labels (e.g., urban > forest > grass). Similarly, if some proportion of
Howarth, 1989; Szostak et al., 2018; Zhu, 2017), and the coarse reso- forest is converted to built-up lands, it will be labeled as urban even if
lution data, such as MODIS and AVHRR, are mostly used to extract the urban proportion of the pixel is small (but at least >10%) (Pengra
gradual change based on long time series data (Myneni et al., 1997; et al., 2020). For example, if >10% of trees were removed from a forest
Pouliot et al., 2009; Zhu et al., 2016b). It is worth noting that the im- pixel, and replaced by a new house, the pixel would still be considered to
pacts of spatial resolution of the remotely sensed imagery may differ have undergone land cover conversion (from forest to urban), even
based on the specific image analyzing unit, such as pixel-based versus though the remaining forest cover is just slightly <90% (Fig. 6).
object-based approaches (Baker et al., 2013).
When change units of interest are smaller than the resolution cells,
land change may only occur on a small fraction of a pixel (the fraction is 4.3. The temporal issues
a continuous variable), which is also known as the L-resolution situation
(Strahler et al., 1986). To facilitate response design for reference sample The temporal resolution of a remote sensing system refers to the
pixels, a thresholding strategy is often needed to determine whether a revisiting period of a satellite sensor (e.g., Landsat 8 revisits the same
pixel is considered as a “change pixel” from a ground view. For example, location every 16 days). A variety of remote sensing systems collect
in Hansen et al. (2013), forest change is defined as a pixel with >50% observations every minute, hour, daily, weekly, monthly, or for a few
change in forest cover within a pixel. On the other hand, the definition of years (Jensen, 2009). Essentially, more accurate detection of change
time could be achieved based on observations of higher temporal
Fig. 6. The impacts of spatial resolution on mapping change location and change target between 2014 and 2018. All the remotely sensed images were acquired at
central latitude/longitude (41.781/(cid:0) 72.234) in the summer of 2014 and 2018 and reprojected into the WGS84 UTM Zone 19 N. The MODIS, Landsat, and Plan-
etScope images were collected at a coarse resolution (500 m), medium resolution (30 m), and high resolution (5 m), respectively. Two National Agriculture Imagery
Program (NAIP) aerial images (0.6 m) were classified into forest, urban, and grass which were used as the reference maps. To generate change location and change
target maps for each image type, we aggregated the reference maps at each resolution and labeled cover types and change pixels by investigating sub-pixel fraction:
forest is defined as pixels with >10% coverage of trees, and urban is defined as pixels with >10% coverage of built areas; changes were labeled when cover types for
>10% of the pixel changed. No change signals were present from MODIS images (500 m) under the definition but became detectable in the other remote sensing
images at 0.6–30 m spatial resolutions.
8

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
resolutions, as change time can be contained within a narrower time and are usually detectable if annual Landsat observations are used
interval, and this has been echoed by the fact that remote sensing change (Fig. 7b-c). Another extreme is that land changes relating to urban
detection algorithms are using denser time series (Zhu, 2017). The expansion (Fig. 7d) that is often non-reversible and could be successfully
choice of temporal resolution is particularly important when the short- captured even by two Landsat images collected at an interval of 5 to 10
lived phenomena need to be monitored or persistent clouds limit a years. Therefore, the minimum temporal resolution required for
clear view. For example, with two sensors working simultaneously, the different land change applications is usually quite different. Generally,
Landsat time series can provide 8 days of revisit observations for the the denser the time series observations used, the more accurate the
same location if we do not consider observations contaminated by cloud, detection of the time and location of change.
cloud shadow, and snow/ice. For ephemeral change such as floods that Even if all clear observations have remained for analysis, the time
only last a few days, it is less likely to be observed based on Landsat time series may have different temporal resolutions at different places and at
series alone (Fig. 7a). In Fig. 7a, we serendipitously collected one clear different times due to the overlap of adjacent swaths, the presence of
Landsat image located during the flooding, but if it was blocked by cloud or snow/ice, and the data acquisition strategies (Brown et al.,
clouds, it would be impossible for detecting this kind of ephemeral 2020; Zhu et al., 2018). For example, Gypsy Moth infestation usually
change as the system had recovered to the pre-change state before only lasts for one or two months, and if all available Landsat data are
acquisition of the next available observation unless other active sensors used, we can have around four clear observations (without using ob-
such as radar were used. For grassland change (i.e., abrupt greenness servations from the neighboring path) in two months for most places
change) caused by climatic variability and forest change caused by (assume cloud cover is 50%). In certain places where two Landsat paths
beetle infestation, they can last for a year or multiple years, respectively, overlap with each other (the overlap areas), we could have around eight
Fig. 7. The impact of temporal resolution on land change detection. (a) A flood event that lasted for a few days at central latitude/longitude (41.103/(cid:0) 95.906). Of
all the available Landsat observations, only a single observation was observed during this ephemeral event. (b) Climatic variability over grassland that lasted almost a
year at central latitude/longitude (34.838/(cid:0) 117.460). (c) Beetle infestation related land change that lasted for several years at central latitude/longitude (40.226/
(cid:0) 106.064). (d) Urbanization over forested areas located at latitude/longitude (41.70/(cid:0) 71.57). In each figure, the time series plot in the upper panel was derived
from all available Landsat observations at the center of the smaller red square of the false color composite images at the lower panel. The change period was
highlighted by the red rectangles in the upper panel and the larger red rectangle surrounding the false color composite images in the lower panel. The false color
composite images were shown in Landsat SWIR1, NIR, and red bands at the same color stretch setting. Some of the images have black stripes due to the Landsat 7
Scan Line Corrector-off issue. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
9

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Fig. 7. (continued).
clear observations which increased the likelihood of detecting these eight-day, and 32-day MODIS-based (500 m) composite time series on a
short-lived changes if a fixed number of consecutive observations is used cropland pixel (Indiana, USA). The daily and the eight-day composite
to analyze change anomaly (Fig. 8). The use of overlap-path observa- time series have similar predictions on green-up and dormancy dates
tions brings new science capability for Landsat data, but also result in (the difference ≤ 2 days), while a significant discrepancy for the
inconsistency to the final land change maps (between the overlap and dormancy date (12 days later than that of the daily time series) was
non-overlap areas). This is particularly problematic for large-scale observed on the 32-day composite time series. This can be explained by
remote sensing change products, as large differences in land change that lower data density often results in a poorer model fit, especially for
patterns will show up both spatially and temporally. Methods that select the phenological window where spectral reflectance often changes
data from the same path or adjust the number of observations to confirm rapidly. A wide body of the literature supports that a moderately high
change based on data density could be possible solutions to alleviate this temporal resolution (three- to 16-day interval) is often necessitated to
issue, but it is at the sacrifice of losing the temporal density for certain accurately inform phenological dates (Cui et al., 2020; Henson et al.,
places, which may lead to omission errors (Fig. 8). 2018; Zhang et al., 2009).
Temporal resolution is of critical relevance to detecting day-sensitive Additionally, the use of dense time series can create new information
changes such as vegetation phenology. The coarse resolution data, such or more accurate change detection/characterization that the traditional
as MODIS and VIIRS, are capable of providing daily repeated observa- two-date image difference method cannot provide. For example, we can
tions and has been widely used for land surface phenology products get to know how the change is occurring based on the change magni-
(Ganguly et al., 2010; Zhang et al., 2018, 2020). Practically, owing to tude, the change direction, and the duration of the change. The infor-
cloud and snow/ice contamination, multi-day compositing was often mation embedded in the time series data provides important spectral-
employed to produce clear observations at a temporal resolution lower temporal information about the pixel and we can extract this informa-
than the daily frequency. A longer compositing interval will reduce tion based on estimated time series model coefficients and statistical
computational and data storage demand and also ensure the observation metrics to provide a more accurate classification of the change target
inputs are of sufficient quality to be useful for model fitting, yet its low (Zhu, 2017). These derived spectral-temporal metrics could even revo-
temporal resolution comes at the cost of hampering accuracies for lutionize the current land cover classification system and bring in new
characterizing phenometrics. Fig. 9 depicts an example of phenological land cover categories that are continuous in time and embedded with
transition date detection from daily (only clear observations remained), changing conditions, such as greening urban, young forest, mature forest,
10

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Fig. 8. A comparison of change detection results caused by Gypsy Moth damage using two Landsat paths (or swaths) data and a single path data. (a) Landsat NIR
surface reflectance observations at the center of the red square of the false color composite images on the right (c) at central latitude/longitude (41.996/(cid:0) 71.669).
The blue dots are from Landsat path #12 and the green dots are from path #13. The red line is the estimated time series model, and the red circle is the land surface
change captured by the COLD algorithm with six consecutive observations to confirm a change (Zhu et al., 2020). (b) A land disturbance map was created based on
the COLD algorithm using Landsat observations from two paths and a single path (#12). The darker the color, the more recent the land disturbance was detected. (c)
The false color composite Landsat images from path #12 (in blue outlines) and path #13 (in green outlines) were shown in SWIR1, NIR, and red bands, and they are
directly comparable because of the same stretch display. This figure demonstrated that for places with two Landsat path coverage, Gypsy Moth damage is possible to
detect by the COLD algorithm, but not possible for places with only a single Landsat path coverage. COLD: COntinuous monitoring of Land Disturbance.
and declining forest (Zhu and Woodcock, 2014). Finally, the time series 4.4. The angular issues
before, during, and after land change all contain rich spectral-temporal
information on the change agent and could be used as major inputs for The energy acquired by the remote sensing systems contains very
change agent classification. specific angular characteristics, which is a function of illumination
In addition to the repeat frequency, the time of day the remote source (e.g., Sun for a passive system or the sensor itself for active sys-
sensing observations are collected is also helpful for better under- tems) angles and the sensor viewing angles, known as the Bidirectional
standing different facets of land change. For example, most of the time Reflectance Distribution Function (BRDF) (Schaaf et al., 2002). This bi-
series we discussed are remotely sensed data collected during the day- directional nature of remote sensing systems will cause inconsistency
time (e.g., around 10 am), which relies on the reflected electromagnetic among the radiance by the same sensor, as well as impact current surface
radiation from the sun. There is also another type of satellite dataset for reflectance retrieval models, thereby limiting our capability for detect-
imaging land surface at nighttime, which provide versatile data sources ing real change signals (Xin et al., 2013). Even for some of the sensors
for studying human activities, as most of the nighttime lights are arti- that only collect near nadir observations, such as Landsat, the changes in
ficial lights (Levin et al., 2020; Li et al., 2017; Zhao et al., 2019). Time- the solar angles and view zenith angles (mostly for observations
series nighttime light data have been widely used to monitor collected in overlap swaths) will still cause large reflectance differences
anthropogenic-related land change and usually at a large scale. How- (Qiu et al., 2019a; Zhang et al., 2018), and potentially lead to omission
ever, as there are also other sources of light at night, such as moonlight, or commission errors in change detection (Fig. 10a). Fortunately, with
aurora, and lighting, the use of dense time series of nighttime light data enough remote sensing observations collected at the different view and
is still very rare (Wang et al., 2021), and the densest time series data ever solar angles within a short time, this BRDF function can be modeled, and
used is still the average monthly or yearly nighttime light observations local-noon nadir observation can be estimated for some coarse resolu-
(Elvidge et al., 2021; Levin, 2017). Recently, NASA has created a Black tion satellites, such as MODIS and VIIRS (Liu et al., 2017; Schaaf et al.,
Marble product that has corrected most of these nonhuman-activity- 2002), and these BRDF parameters can help reduce BRDF effect in me-
related light sources and has provided the potential of using daily dium resolution satellites, such as Landsat and Sentinel-2 (Claverie
nighttime light observations for land change studies (Rom´an et al., et al., 2018; Roy et al., 2016). Other solutions such as selecting obser-
2018). vations within the same swath and creating time series models that es-
timate the solar angle difference along with vegetation phenology
11

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
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
changes can also remove or at least reduce the BRDF differences 2020), due to the inclusion of 3D information.
embedded in the satellite data, and in this way, the change pixel can be
correctly identified (Fig. 10b) using a time-series based change detection
4.5. Data-integration issues
algorithm (Zhu et al., 2020). It is worth noting that the angular infor-
mation can be useful for identifying the target and location of land
With the increased availability of Earth observation satellites, the
change, such as improving land cover classification (Jiao et al., 2011),
integration of multi-sensor datasets could offer complementary views on
detecting moving objects such as clouds (Frantz et al., 2018), aircraft
spatial, temporal, and spectral dimensions, providing a unique oppor-
(Liu et al., 2020b), and detection of newly built houses (Huang et al.,
tunity for approaching a multifaceted land change problem (Dong et al.,
12

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
2009). Methods for integrating multi-sensor datasets for multifaceted questionable due to their geolocation inaccuracy, participants’ bias, or
land change studies can be generally categorized into observation context ambiguity; trickier might be that data uncertainty accompa-
fusion, decision fusion, and information fusion. Observation fusion re- nying VGI data, unlike remote sensing datasets, are mostly unmeasur-
fers to the strategy of combining multiple data sources into a consistent able and unmanageable (Goodchild and Li, 2012). The coverage of the
blending observation set to create a finer temporal, spatial or spectral VGI dataset is also limited and cannot be extended to the same level as
resolution dataset as the algorithm’s inputs (Emelyanova et al., 2013; remotely sensed images, causing a grave technical challenge for
Gao et al., 2006; Shang et al., 2022). Decision fusion, also named enabling a geographically consistent mapping. Lastly, VGI data may not
“competitive integration” (Schmitt and Zhu, 2016), combines similar uncover some change agents such as gradual stress-related changes.
change facet information from different sensor-specific pipelines, aim- Generally, the blending of VGI and remote sensing datasets is in infancy,
ing at producing more reliable results for one single change facet (Car- and its relevance to land change studies is still inconclusive. More
dille et al., 2022; Reiche et al., 2018). Information fusion, such as the foundational research on data processing protocols and well-verified,
“complementary integration” (Schmitt and Zhu, 2016), is the fusion of localized study cases are both anticipated for the future, allowing for a
multi-sensor pipeline results targeted at different change facets, with a broader examination for incorporation of VGI datasets into the current
goal of providing complementary change information. While a production workflow.
comprehensive review of these integration techniques is beyond the
scope of this article, it is important to recognize their conceptual dif- 5. Current land change products
ference in the context of multifaceted change analysis. Observation and
decision fusion have been widely applied to single-facet tasks such as Lots of remote sensing-based land change products have been
change detection or land cover classification to answer “when”, created, and some of them have been widely used in a variety of fields,
“where”, and “what”, but much fewer were on change metrics or agents such as environmental sustainability, land management, biodiversity
(Fernandez-Manso et al., 2019; Meng et al., 2018);comparatively, a conservation, and ecosystem health assessment. However, most of these
paucity of information fusion studies on monitoring land change was land change products only focus on three facets of land change – the
reported, partly due to a lack of recognizing change as a multifaceted location, time, and target of change (mostly land cover), and very few
problem. Another challenge for information fusion is that different data products are trying to provide some of the other facets of land change,
sources may have different geographic coverage, for example, LiDAR such as change agent or change metric (Table 1).
and hyperspectral images are often unable to provide wall-to-wall land Most of the current large-scale land change products are only
change information similar to medium or coarse-resolution images, focusing on a single change target, such as changes in forest, urban, or
which implies that data interpolation is often required. water (Table 1). For instance, Hansen et al. (2013) created the
Beyond remote sensing observations, an increasing array of social 2000–2019 global 30-m forest cover and forest cover change (i.e., forest
science data have shown their great promise for unveiling social/eco- loss and forest grain) products based on time series spectral metrics of
nomic processes that are not manifested on the landscape, pinpointing Landsat data and a supervised classification approach. The North
the question of “why” the land change happened. Social science data- American Forest Dynamics (NAFD) project implemented the Vegetation
sets, such as population density, capital investment, poverty gap index, Change Tracker (VCT) algorithm (Huang et al., 2010) to produce annual
were often manipulated as explanatory variables for establishing forest disturbance maps for the conterminous United States (CONUS)
empirical models and used to infer causes or drivers of land changes from 1986 to 2010 based on annual Landsat time series data (Zhao et al.,
observed from remote sensing images (NRC, 2013; Seto and Kaufmann, 2018). Liu et al. (2020a) created 30-m Global Annual Urban Dynamics
2003; Wyman and Stein, 2010). While such applications for integrating (GAUD) dataset for providing information on urban expansion and
the remotely sensed (pixels) data with social science (people) data have green recovery from 1985 to 2015 based on existing global urban extent
been a major focus in land change science (Lambin, 2004), their maps and Landsat time series data. European Space Agency (ESA) pro-
fundamental differences in data format create lots of challenges. The duced the Global Human Settlement Layer (GHSL) for multiple years,
national Academy of Science volume “People and Pixels” (NRC, 1998) which can provide new global spatial information, evidence-based an-
and Rindfuss et al. (2012) have exemplified several data integration alytics, and knowledge describing the human presence such as built-up
issues, such as different data presentations (e.g., “discrete” vs “contin- area and population distribution on the Earth (Pesaresi et al., 2016). The
uous”), inconsistent temporal depth and data complexities, and ESA Global Surface Water (GSW) dataset provides different facets of the
traversing the languages and terminology from different disciplines. spatial and temporal distribution of surface water over long time periods
Conventionally, the social science data were collected based on field at a 30-m resolution based on 30+years of Landsat data, such as water
observations, interviews with local people, and surveys, which is time occurrence for presenting overall water dynamics, water recurrence for
consuming, labor intensive, and usually out-of-date. The Volunteered describing how frequently water returned from one year to another, and
Geographic Information (VGI) has been a paradigm shift that offers an water seasonality for capturing the intra-annual dynamics of water
alternative mechanism for collecting and compilating the georeferenced surfaces (Pekel et al., 2016). This dataset also includes water occurrence
social science data (Goodchild, 2007). Through content retrieval, cate- change intensity maps between two epochs (1984 to 1999, and 2000 to
gorization and meta-data analysis (Daume et al., 2014), and georefer- 2020), which can provide information on where surface water occur-
enced VGI data (such as from media reports or geotagged social media rence increased, decreased, or remained the same. In addition, products
posts) can be integrated at decision or information levels, which im- of single change agent are available as well, particularly for fire. For
proves insights not just on the disturbance agents from a “local view”, example, Giglio et al. (2018) applied dynamic thresholds of a burn-
but also uniquely uncovers the socioeconomic drivers underlying land sensitive vegetation index composite data (derived from daily 500 m
surface change, such as narcotrafficking (Sesnie et al., 2017; Tellman MODIS time series) to generate a global burned area product, in which
et al., 2020) and population increase (Minale, 2013). Another notable the date of the burned area will be provided within each MODIS tile with
advantage of the VGI data is that their availability is usually more timely 10 degrees by 10 degrees.
(e.g., social media data), and by combining with other near real-time Only a few products can provide information on land change on
satellite data sources, the social media datasets have showcased their different kinds of land surfaces. The National Land Cover Database
capacity for advancing those time-sensitive change detection tasks such (NLCD) provides multi-temporal land cover and land cover change
as rapid disaster mapping (Fohringer et al., 2015; Rosser et al., 2017; products for CONUS, Hawaii, Alaska, and Puerto Rico between 2001 and
Schnebele et al., 2014). Despite its great potential, several factors pre- 2019 for every 2–3 year interval, based on decadal Landsat data as well
clude populating the VGI dataset of the present day for a wall-to-wall as other ancillary datasets (Jin et al., 2019). Using daily seamless data
land change mapping. First and foremost, the data quality of VGI is cubes generated from multi-source remote sensing data, Liu et al.
13

Z. Zhu et al.                                                                                                                                                                                          R  e  m  o  t e  S  e  n s  i n g   o  f  E  n v  i r o  n  m  e  n  t282(2022)113266
Table 1
A select list of current global and North America land change products. Only the most recent literature is listed here.
Product Name  Coverage  Change  Change Time  Change  Change Metric  Change Agent  Satellite  Citation
|     | Location  | (Period)  | Target  |     |     | Data  |
| --- | --------- | --------- | ------- | --- | --- | ----- |
Hansen forest  Global  30-m  Annual  Forest gain  N/A  N/A  Landsat  (Hansen et al.,
| change map  |     | (2000–2019)  | Forest loss  |     |     | 2013)  |
| ----------- | --- | ------------ | ------------ | --- | --- | ------ |
Global Surface  Global  30-m  Intra-annual  Water  Water  N/A  Landsat  (Pekel et al., 2016)
| Water  |     | Annual       | seasonality  | occurrence        |     |     |
| ------ | --- | ------------ | ------------ | ----------------- | --- | --- |
|        |     | (1984–2020)  | Water        | Change intensity  |     |     |
transitions
Annual water
recurrence
MODIS burned  Global  500-m  Day of Year  Burned area  N/A  Fire  MODIS  (Giglio et al.,
| area  |     | (2000-Present)  |     |     |     | 2018)  |
| ----- | --- | --------------- | --- | --- | --- | ------ |
NAFD-NEX  CONUS  30-m  Annual  Forest  N/A  N/A  Landsat  (Zhao et al., 2018)
|     |     | (1986–2010)  | disturbance  |     |     |     |
| --- | --- | ------------ | ------------ | --- | --- | --- |
GHSL  Global  30-, 250-,  Multiple years  Built-up area  N/A  N/A  Landsat  (Pesaresi et al.,
and 1000-  (1975, 1990, 2000, and  2016)
m  2014)
NLCD  United  30-m  2–3 years  Land cover  N/A  N/A  Landsat  (Jin et al., 2019)
|     | States  | (2001–2019)  | change  |     |     |     |
| --- | ------- | ------------ | ------- | --- | --- | --- |
Forest
disturbance
LANDFIRE  United  30-m  Annual  Vegetation  Disturbance  Fire, Mechanical,  Landsat  (Rollins, 2009)
States  Day of Year  transition  severity  Insect, Windthrow
|     |     | (1999–2020)  |     | Time since  |     |     |
| --- | --- | ------------ | --- | ----------- | --- | --- |
disturbance
GAUD  Global  30-m  Annual  Urban  N/A  N/A  Landsat  (Liu et al., 2020a)
(1985–2015)
expansion
Green
recovery
LCMAP  CONUS  30-m  Annual  Land cover  Change  N/A  Landsat  (Brown et al.,
|     |     | Day of Year  | change         | magnitude           |     | 2020)  |
| --- | --- | ------------ | -------------- | ------------------- | --- | ------ |
|     |     | (1985–2019)  | Land spectral  | Spectral stability  |     |        |
|     |     |              | change         | period              |     |        |
Time since last
change
iMap  Global  30-m  Annual  Land cover  N/A  N/A  Landsat,  (Liu et al., 2021a)
|     |     | Seasonal     | change  |     |     | MODIS, and  |
| --- | --- | ------------ | ------- | --- | --- | ----------- |
|     |     | (1985–2010)  |         |     |     | AVHRR       |
NALCMS  North  30- and  5 years  Land cover  N/A  N/A  Landsat and  (Latifovic et al.,
|     | America  250-m  | (2001–2015)  | change  |     |     | MODIS  2016)  |
| --- | --------------- | ------------ | ------- | --- | --- | ------------- |
NTEMS  Canada  30-m  Annual  Land cover  Post-disturbance  Fire, Harvest, Road,  Landsat and  (Hermosilla et al.,
(1984–2019 for land cover;  change  recovery rate  Non-stand replacing  LiDAR  2022; White et al.,
|     |     | 1985–2017 for recovery;  |     |     | disturbance  | 2017, 2022)  |
| --- | --- | ------------------------ | --- | --- | ------------ | ------------ |
1985–2015 for disturbance
agent)
GLanCE  Global  30-m  Annual  Land cover  N/A  N/A  Landsat  (Friedl et al.,
(2001(cid:0)
|     |     | 2020)  | change  |     |     | 2022)  |
| --- | --- | ------ | ------- | --- | --- | ------ |
Annual (2000(cid:0)
GLCLUC2020  Global  30-m  2020)  Land cover  N/A  N/A  Landsat  (Potapov et al.,
change  2022)
Notes: CONUS: COnterminous United States; NLCD: National Land Cover Database; LCMAP: Land Change Monitoring, Assessment, and Projection; GHSL: Global
Human Settlement Layer; GAUD: Global Annual Urban Dynamics; NAFD-NEX: North American Forest Dynamics - NASA Earth Exchange; NALCMS: North American
Land Cover Change Monitoring System; NTEMS: National Terrestrial Ecosystem Monitoring System; GLanCE: Global Land Cover Estimation; GLCLUC: Global Land
Cover and Land Use Change.
(2021a) generated 30 m resolution global land cover map data for 36  why, and how this change takes place can be fully evaluated and map-
years by combining strategies of sample migration, machine learning,  ped. We proposed a new concept of the multifaceted view of land change
and spatio-temporal adjustment, which can be used to study global land  through the lens of remote sensing and recommended five facets
change. Recently, Friedl et al. (2022) and Potapov et al. (2022) have also  including change location, time, target, metric, and agent. We also
created annual global land cover change maps between 2000 and 2020  discussed the relationship of various kinds of land change terminologies
based on the Landsat time series. Among all these products, Land  including spectral change, land surface change, biophysical/biochem-
Change Monitoring, Assessment, and Projection (LCMAP) (Brown et al.,  ical parameter change, land disturbance, climate change, climate vari-
2020), LANDFIRE (Rollins, 2009), and National Terrestrial Ecosystem  ability, succession, land cover change, land cover conversion, and land
Monitoring System (NTEMS) (Hermosilla et al., 2022; White et al., 2017,  cover modifications, in which large differences were identified among
2022) are some of the few land change products that not only can pro- these terminologies. The impacts of spatial, spectral, temporal, and
vide change location and time, change target, but also land change  angular domains of the remotely sensed data on observation, moni-
metrics, or even land change agent information.  toring, and characterization of land change were also evaluated. We
emphasized the importance of selecting the “right” spectral bands and
6. Conclusion and recommendations  spatial resolution of remote sensing data for the specific land change
problem. We discussed the benefits and challenges when dense time-
Land change science has made big advancements with the develop- series and multi-angle satellite observations are used for observing
ment of remote sensing technology, and questions of where, when, what,  and characterizing land change. We also reviewed some of the current
14

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
land change products and observed the lack of products that provide Bartels, S.F., Chen, H.Y.H., Wulder, M.A., White, J.C., 2016. Trends in post-disturbance
multiple, or all land change facets, particularly for the facets of land recovery rates of Canada’s forests following wildfire and harvest. For. Ecol. Manag.
361, 194–207. https://doi.org/10.1016/j.foreco.2015.11.015.
change agent and metric. Beck, P.S.A., Atzberger, C., Høgda, K.A., Johansen, B., Skidmore, A.K., 2006. Improved
Therefore, we have a few recommendations on remote sensing of monitoring of vegetation dynamics at very high latitudes: a new method using
land change as follows. First, it is important to recognize the multifac- MODIS NDVI. Remote Sens. Environ. 100, 321–334.
Belward, A.S., Skøien, J.O., 2015. Who launched what, when and why; trends in global
eted nature of land change, and when remote sensing data are used to
land-cover observation capacity from civilian earth observation satellites. ISPRS J.
study land change, specifying which land change facet is being studied, Photogramm. Remote Sens. 103, 115–128. https://doi.org/10.1016/j.
is usually the first step. Second, remote sensing-derived land change isprsjprs.2014.03.009.
Bowman, D.M.J.S., Balch, J., Artaxo, P., Bond, W.J., Cochrane, M.A., D’antonio, C.M.,
products reported with all five facets are highly recommended, as land
DeFries, R., Johnston, F.H., Keeley, J.E., Krawchuk, M.A., 2011. The human
change can only be fully understood if they are viewed from all different dimension of fire regimes on earth. J. Biogeogr. 38, 2223–2236. https://doi.org/
angles. Third, we think a major shift in the focus from change target to 10.1111/j.1365-2699.2011.02595.x.
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,
change metric and change agent is expected in future remote sensing
Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., 2020. Lessons
studies, as these two facets are far less studied in the remote sensing learned implementing an operational continuous United States national land change
community, and why and how global land is changing are some of the monitoring capability: the land change monitoring, assessment, and project
(LCMAP) approach. Remote Sens. Environ. 238, 111356 https://doi.org/10.1016/j.
most difficult and important science questions. Fourth, land change
rse.2019.111356.
science has transitioned into more complex systems such as land system Bruzzone, L., Bovolo, F., 2012. A novel framework for the design of change-detection
science (Turner et al., 2021), which requires deeper and more compre- systems for very-high-resolution remote sensing images. Proceedings of the IEEE 101
hensive land change information. For example, most of the current (3), 609–630. https://doi.org/10.1109/JPROC.2012.2197169.
Buchner, J., Yin, H., Frantz, D., Kuemmerle, T., Askerov, E., Bakuradze, T., Bleyhl, B.,
remote sensing change agent products are not detailed enough for social Elizbarashvili, N., Komarova, A., Lewin´ska, K.E., 2020. Land-cover change in the
sciences to answer the question of “why”, and the combined use of social Caucasus Mountains since 1987 based on the topographic correction of multi-
science data and multiple remote sensing data sources could provide temporal landsat composites. Remote Sens. Environ. 248, 111967 https://doi.org/
10.1016/j.rse.2020.111967.
new and deeper insights. Finally, we need to recognize that every remote
Cardille, J.A., Perez, E., Crowley, M.A., Wulder, M.A., White, J.C., Hermosilla, T., 2022.
sensing system has limitations and weaknesses in land change studies, Multi-sensor change detection for within-year capture and labelling of forest
and a thorough evaluation of all spectral, spatial, temporal, and angular disturbance. Remote Sens. Environ. 268, 112741.
Chirici, G., Giannetti, F., Mazza, E., Francini, S., Travaglini, D., Pegna, R., White, J.C.,
issues is highly recommended.
2020. Monitoring clearcutting and subsequent rapid recovery in Mediterranean
coppice forests with landsat time series. Ann. For. Sci. 77, 1–14.
Declaration of Competing Interest Chowdhury, S., Peddle, D.R., Wulder, M.A., Heckbert, S., Shipman, T.C., Chao, D.K.,
2021. Estimation of land-use/land-cover changes associated with energy footprints
and other disturbance agents in the upper peace region of Alberta Canada from 1985
The authors declare that they have no known competing financial to 2015 using landsat data. Int. J. Appl. Earth Obs. Geoinf. 94, 102224.
interests or personal relationships that could have appeared to influence Chu, T., Guo, X., Takeda, K., 2016. Remote sensing approach to detect post-fire
vegetation regrowth in siberian boreal larch forest. Ecol. Indic. 62, 32–46.
the work reported in this paper.
Claverie, M., Ju, J., Masek, J.G., Dungan, J.L., Vermote, E.F., Roger, J.C., Skakun, S.V.,
Justice, C., 2018. The harmonized landsat and Sentinel-2 surface reflectance data
Data availability set. Remote Sens. Environ. 219, 145–161. https://doi.org/10.1016/j.
rse.2018.09.002.
Clements, F.E., 1916. Plant succession: an analysis of the development of vegetation.
The remote sensing data used in this review were downloaded from Carnegie Institution of Washington.
USGS, NASA, Copernicus, and Planet Labs. Cohen, W.B., Goward, S.N., 2004. Landsat’s role in ecological applications of remote
sensing. Bioscience 54, 535–545. https://doi.org/10.1641/0006-3568(2004)054
[0535:LRIEAO]2.0.CO;2.
Acknowledgment
Colditz, R.R., Pouliot, D., Llamas, R.M., Homer, C., Latifovic, R., Ressl, R.A., Tovar, C.M.,
Herna´ndez, A.V., Richardson, K., 2014. Detection of North American land cover
This research was supported by the USGS-NASA Landsat Science change between 2005 and 2010 with 250m MODIS data. PE&RS. Photogramm. Eng.
Remote Sens. 80, 918–924.
Team Program for Toward Near Real-time Monitoring and Character-
Comber, A., Wulder, M., 2019. Considering spatiotemporal processes in big data analysis:
ization of Landsat Surface Change for the Conterminous US Insights from remote sensing of land cover and land use. Trans. GIS 23, 879–891.
(140G0119C0008). We would like to thank Billie Turner II and the five Coops, N.C., Johnson, M., Wulder, M.A., White, J.C., 2006. Assessment of QuickBird high
spatial resolution imagery to detect red attack damage due to mountain pine beetle
anonymous reviewers for their insightful comments and suggestions for
infestation. Remote Sens. Environ. 103, 67–80.
this manuscript. The content of this document does not necessarily Coppin, P., Jonckheere, I., Nackaerts, K., Muys, B., Lambin, E., 2004. Digital change
represent the views or policies of the Department of the Interior, nor detection methods in ecosystem monitoring: a review. Int. J. Remote Sens. 25,
1565–1596.
does mention of trade names, commercial products, or organizations
Coppin, P.R., Bauer, M.E., 1996. Digital change detection in forest ecosystems with
imply endorsement by the U.S. Government. remote sensing imagery. Remote Sens. Rev. 13, 207–234. https://doi.org/10.1080/
02757259609532305.
References Cui, T., Martz, L., Zhao, L., Guo, X., 2020. Investigating the impact of the temporal
resolution of MODIS data on measured phenology in the prairie grasslands.
GIScience Remote Sens. 57, 395–410.
Anderson, J.R., Hardy, E.E., Roach, J.T., Witmer, R.E., 1976. A land use and land cover Dale, V.H., 1997. The relationship between land-use change and climate change. Ecol.
classification system for use with remote sensor data, Washington, DC: government Appl. 7, 753–769. https://doi.org/10.1890/1051-0761(1997)007[0753:TRBLUC]
printing office (US geological survey. Professional Paper 964. https://doi.org/ 2.0.CO;2.
10.3133/pp964. Dale, V.H., Joyce, L.A., McNulty, S., Neilson, R.P., Ayres, M.P., Flannigan, M.D.,
Asner, G.P., Knapp, D.E., Balaji, A., Pa´ez-Acosta, G., 2009. Automated mapping of Hanson, P.J., Irland, L.C., Lugo, A.E., Peterson, C.J., 2001. Climate change and forest
tropical deforestation and forest degradation: CLASlite. J. Appl. Remote. Sens. 3, disturbances: climate change can affect forests by altering the frequency, intensity,
33543. https://doi.org/10.1117/1.3223675. duration, and timing of fire, drought, introduced species, insect and pathogen
Asner, G.P., Knapp, D.E., Broadbent, E.N., Oliveira, P.J.C., Keller, M., Silva, J.N., 2005. outbreaks, hurricanes, windstorms, ice storms, or landslides. Bioscience 51,
Selective logging in the brazilian Amazon. Science 310, 480–482. https://doi.org/ 723–734. https://doi.org/10.1641/0006-3568(2001)051[0723:CCAFD]2.0.CO;2.
10.1126/science.1118051. Daume, S., Albert, M., von Gadow, K., 2014. Forest monitoring and social
Baker, B.A., Warner, T.A., Conley, J.F., McNeil, B.E., 2013. Does spatial resolution media–Complementary data sources for ecosystem surveillance? For. Ecol. Manag.
matter? A multi-scale comparison of object-based and pixel-based methods for 316, 9–20.
detecting change associated with gas well drilling operations. Int. J. Remote Sens. de Beurs, K.M., Henebry, G.M., Owsley, B.C., Sokolik, I., 2015. Using multiple remote
34, 1633–1651. sensing perspectives to identify and attribute land surface dynamics in Central Asia
Banskota, A., Kayastha, N., Falkowski, M.J., Wulder, M.A., Froese, R.E., White, J.C., 2001–2013. Remote Sens. Environ. 170, 48–61. https://doi.org/10.1016/j.
2014. Forest monitoring using landsat time series data: a review. Can. J. Remote. rse.2015.08.018.
Sens. 40, 362–384. https://doi.org/10.1080/07038992.2014.987376. De Jong, R., Verbesselt, J., Schaepman, M.E., De Bruin, S., 2012. Trend changes in global
greening and browning: Contribution of short-term trends to longer-term change.
15

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Glob. Chang. Biol. 18, 642–655. https://doi.org/10.1111/j.1365-2486.2011.02578. Goodchild, M.F., 2007. Citizens as sensors: the world of volunteered geography.
x. GeoJournal 69, 211–221. https://doi.org/10.1007/s10708-007-9111-y.
Deng, C., Zhu, Z., 2020. Continuous subpixel monitoring of urban impervious surface Goodchild, M.F., Li, L., 2012. Assuring the quality of volunteered geographic
using Landsat time series. Remote Sens. Environ. 238, 110929 https://doi.org/ information. Spat Stat 1, 110–120. https://doi.org/10.1016/j.spasta.2012.03.002.
10.1016/j.rse.2018.10.011. Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., Moore, R., 2017.
Dong, J., Zhuang, D., Huang, Y., Fu, J., 2009. Advances in multi-sensor data fusion: Google Earth Engine: Planetary-scale geospatial analysis for everyone. Remote Sens.
Algorithms and applications. Sensors 9, 7771–7784. Environ. 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031.
Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., Hoersch, B., Grime, J.P., 1977. Evidence for the existence of three primary strategies in plants and its
Isola, C., Laberinti, P., Martimort, P., Meygret, A., Spoto, F., Sy, O., Marchese, F., relevance to ecological and evolutionary theory. Am. Nat. 111, 1169–1194.
Bargellini, P., 2012. Sentinel-2: ESA’s Optical High-Resolution Mission for GMES Guo, B., Gunn, S.R., Damper, R.I., Nelson, J.D.B., 2006. Band selection for hyperspectral
Operational Services. Remote Sens. Environ. 120, 25–36. https://doi.org/10.1016/j. image classification using mutual information. IEEE Geosci. Remote Sens. Lett. 3,
rse.2011.11.026. 522–526.
Dwyer, J., Roy, D., Sauer, B., Jenkerson, C., Zhang, H., Lymburner, L., 2018. Analysis Guo, X., Feng, J., Shi, Z., Zhou, X., Yuan, M., Tao, X., Hale, L., Yuan, T., Wang, J., Qin, Y.,
Ready Data: Enabling Analysis of the Landsat Archive. Remote Sens. 10, 1363. 2018. Climate warming leads to divergent succession of grassland microbial
https://doi.org/10.3390/rs10091363. communities. Nat. Clim. Chang. 8, 813–818. https://doi.org/10.1038/s41558-018-
Eidenshink, J., Schwind, B., Brewer, K., Zhu, Z., Quayle, B., Howard, S., Falls, S., Falls, S., 0254-2.
2007. A Project for Monitoring Trends in Burn Severity. Fire Ecol. 3, 3–21. https:// Gutman, G., Janetos, A.C., Justice, C.O., Moran, E.F., Mustard, J.F., Rindfuss, R.R.,
doi.org/10.4996/fireecology.0301003. Skole, D., Turner II, B.L., Cochrane, M.A., 2004. Land change science: observing,
Ellis, E.C., Klein Goldewijk, K., Siebert, S., Lightman, D., Ramankutty, N., 2010. monitoring and understanding trajectories of change on the earth’s surface. Springer
Anthropogenic transformation of the biomes, 1700 to 2000. Glob. Ecol. Biogeogr. Science & Business Media.
19, 589–606. https://doi.org/10.1111/j.1466-8238.2010.00540.x. Hall, F.G., Botkin, D.B., Strebel, D.E., Woods, K.D., Goetz, S.J., 1991. Large-scale patterns
Elvidge, C.D., Zhizhin, M., Ghosh, T., Hsu, F.-C., Taneja, J., 2021. Annual time series of of forest succession as determined by remote sensing. Ecology 72, 628–640.
global VIIRS nighttime lights derived from monthly averages: 2012 to 2019. Remote Hansen, M.C., DeFries, R.S., 2004. Detecting long-term global forest change using
Sens. 13, 922. https://doi.org/10.3390/rs13050922. continuous fields of tree-cover maps from 8-km advanced very high resolution
Emelyanova, I.V., McVicar, T.R., Van Niel, T.G., Li, L.T., Van Dijk, A.I.J.M., 2013. radiometer (AVHRR) data for the years 1982–99. Ecosystems 7, 695–716, 10.1007%
Assessing the accuracy of blending Landsat–MODIS surface reflectances in two 2Fs10021-004-0243.
landscapes with contrasting spatial and temporal dynamics: A framework for Hansen, M.C., Loveland, T.R., 2012. A review of large area monitoring of land cover
algorithm selection. Remote Sens. Environ. 133, 193–209. change using Landsat data. Remote Sens. Environ. 122, 66–74. https://doi.org/
Fang, F., McNeil, B.E., Warner, T.A., Maxwell, A.E., Dahle, G.A., Eutsler, E., Li, J., 2020. 10.1016/j.rse.2011.08.024.
Discriminating tree species at different taxonomic levels using multi-temporal Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., Turubanova, S.A.A., Tyukavina, A.,
WorldView-3 imagery in Washington DC, USA. Remote Sens. Environ. 246, 111811. Thau, D., Stehman, S.V., Goetz, S.J., Loveland, T.R., Kommareddy, A., 2013. High-
Fernandez-Manso, A., Quintano, C., Roberts, D.A., 2019. Burn severity analysis in resolution global maps of 21st-century forest cover change. Science 342, 850–853.
Mediterranean forests using maximum entropy model trained with EO-1 Hyperion https://doi.org/10.1126/science.1244693.
and LiDAR data. ISPRS J. Photogramm. Remote Sens. 155, 102–118. Hart, S.J., Veblen, T.T., 2015. Detection of spruce beetle-induced tree mortality using
Firebaugh, G., Warner, C., Massoglia, M., 2013. Fixed effects, random effects, and hybrid high- and medium-resolution remotely sensed imagery. Remote Sens. Environ. 168,
models for causal analysis. In: Handbook of Causal Analysis for Social Research. 134–145. https://doi.org/10.1016/j.rse.2015.06.015.
Springer, pp. 113–132. Healey, S.P., Cohen, W.B., Yang, Z., Kenneth Brewer, C., Brooks, E.B., Gorelick, N.,
Fohringer, J., Dransch, D., Kreibich, H., Schro¨ter, K., 2015. Social media as an Hernandez, A.J., Huang, C., Joseph Hughes, M., Kennedy, R.E., Loveland, T.R.,
information source for rapid flood inundation mapping. Nat. Hazards Earth Syst. Sci. Moisen, G.G., Schroeder, T.A., Stehman, S.V., Vogelmann, J.E., Woodcock, C.E.,
15, 2725–2738. Yang, L., Zhu, Z., 2018. Mapping forest change using stacked generalization: An
Foody, G.M., Doan, H.T.X., 2007. Variability in soft classification prediction and its ensemble approach. Remote Sens. Environ. 204, 717–728. https://doi.org/10.1016/
implications for sub-pixel scale change detection and super resolution mapping. j.rse.2017.09.029.
Photogramm. Eng. Remote Sens. 73, 923–933. https://doi.org/10.14358/ Henson, S.A., Cole, H.S., Hopkins, J., Martin, A.P., Yool, A., 2018. Detection of climate
PERS.73.8.923. change-driven trends in phytoplankton phenology. Glob. Chang. Biol. 24,
Forzieri, G., Dakos, V., McDowell, N.G., Ramdane, A., Cescatti, A., 2022. Emerging e101–e111.
signals of declining forest resilience under climate change. Nature 608, 534–539. Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2022. Land cover classification in
https://doi.org/10.1038/s41586-022-04959-9. an era of big and open data: Optimizing localized implementation and training data
Frantz, D., 2019. FORCE—Landsat+Sentinel-2 analysis ready data and beyond. Remote selection to improve mapping outcomes. Remote Sens. Environ. 268, 112780.
Sens. 11, 1124. https://doi.org/10.3390/rs11091124. Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., 2018. Disturbance-
Frantz, D., Haß, E., Uhl, A., Stoffels, J., Hill, J., 2018. Improvement of the Fmask Informed Annual Land Cover Classification Maps of Canada’s Forested Ecosystems
algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on for a 29-Year Landsat Time Series. Can. J. Remote. Sens. 44, 67–87. https://doi.org/
parallax effects. Remote Sens. Environ. 215, 471–481. https://doi.org/10.1016/j. 10.1080/07038992.2018.1437719.
rse.2018.04.046. Homer, C., Dewitz, J., Fry, J., Coan, M., Hossain, N., Larson, C., Herold, N.,
Friedl, M.A., Woodcock, C.E., Olofsson, P., Zhu, Z., Loveland, T., Stanimirova, R., McKerrow, A., VanDriel, J.N., Wickham, J., 2007. Completion of the 2001 national
Arevalo, P., Bullock, E., Hu, K.-T., Zhang, Y., Turlej, K., Tarrio, K., McAvoy, K., land cover database for the counterminous United States. Photogramm. Eng. Remote
Gorelick, N., Wang, J.A., Barber, C.P., Souza, C., 2022. Medium Spatial Resolution Sens. 337–341.
Mapping of Global Land Cover and Land Cover Change Across Multiple Decades Homer, C., Dewitz, J., Jin, S., Xian, G., Costello, C., Danielson, P., Gass, L., Funk, M.,
From Landsat. Front. Remote Sens. 3 https://doi.org/10.3389/frsen.2022.894571. Wickham, J., Stehman, S., 2020. Conterminous United States land cover change
Friis, C., Nielsen, J.Ø., Otero, I., Haberl, H., Niewo¨hner, J., Hostert, P., 2016. From patterns 2001–2016 from the 2016 national land cover database. ISPRS J.
teleconnection to telecoupling: Taking stock of an emerging framework in land Photogramm. Remote Sens. 162, 184–199.
system science. J. Land Use Sci. 11, 131–153. https://doi.org/10.1080/ Homer, C., Dewitz, J., Yang, L., Jin, S., Danielson, P., Xian, G., Coulston, J., Herold, N.,
1747423X.2015.1096423. Wickham, J., Megown, K., 2015. Completion of the 2011 National Land Cover
Ganguly, S., Friedl, M.A., Tan, B., Zhang, X., Verma, M., 2010. Land surface phenology Database for the conterminous United States–representing a decade of land cover
from MODIS: Characterization of the Collection 5 global land cover dynamics change information. Photogramm. Eng. Remote Sens. 81, 345–354.
product. Remote Sens. Environ. 114, 1805–1816. Huang, C., Goward, S.N., Masek, J.G., Thomas, N., Zhu, Z., Vogelmann, J.E., 2010. An
Gao, F., Masek, J., Schwaller, M., Hall, F., 2006. On the blending of the Landsat and automated approach for reconstructing recent forest disturbance history using dense
MODIS surface reflectance: Predicting daily Landsat surface reflectance. IEEE Trans. Landsat time series stacks. Remote Sens. Environ. 114, 183–198. https://doi.org/
Geosci. Remote Sens. 44, 2207–2218. 10.1016/j.rse.2009.08.017.
Gao, F., Masek, J.G., Wolfe, R.E., 2009. Automated registration and orthorectification Huang, H., Roy, D.P., 2021. Characterization of Planetscope-0 Planetscope-1 surface
package for Landsat and Landsat-like data processing. J. Appl. Remote. Sens. 3, reflectance and normalized difference vegetation index continuity. Sci. Remote Sens.
033515 https://doi.org/10.1117/1.3104620. 3, 100014 https://doi.org/10.1016/j.srs.2021.100014.
Garbulsky, M.F., Pen˜uelas, J., Gamon, J., Inoue, Y., Filella, I., 2011. The photochemical Huang, S., Ramirez, C., McElhaney, M., Clark, C., Yao, Z., 2019. Quantifying
reflectance index (PRI) and the remote sensing of leaf, canopy and ecosystem spatiotemporal post-disturbance recovery using field inventory, tree growth, and
radiation use efficiencies: A review and meta-analysis. Remote Sens. Environ. 115, remote sensing. Earth Sp. Sci. 6, 489–504.
281–297. https://doi.org/10.1016/j.rse.2010.08.023. Huang, X., Cao, Y., Li, J., 2020. An automatic change detection method for monitoring
Geist, H.J., Lambin, E.F., 2002. Proximate Causes and Underlying Driving Forces of newly constructed building areas using time-series multi-view high-resolution
Tropical DeforestationTropical forests are disappearing as the result of many optical satellite images. Remote Sens. Environ. 244, 111802 https://doi.org/
pressures, both local and regional, acting in various combinations in different 10.1016/j.rse.2020.111802.
geographical locations. Bioscience 52, 143–150. https://doi.org/10.1641/0006- Huete, A., 2016. Vegetation’s responses to climate variability. Nature 531, 181–182.
3568(2002)052[0143:PCAUDF]2.0.CO;2. https://doi.org/10.1038/nature17301.
Giglio, L., Boschetti, L., Roy, D.P., Humber, M.L., Justice, C.O., 2018. The Collection 6 Hussain, M., Chen, D., Cheng, A., Wei, H., Stanley, D., 2013. Change detection from
MODIS burned area mapping algorithm and product. Remote Sens. Environ. 217, remotely sensed images: From pixel-based to object-based approaches. ISPRS J.
72–85. https://doi.org/10.1016/j.rse.2018.08.005. Photogramm. Remote Sens. https://doi.org/10.1016/j.isprsjprs.2013.03.006.
Go´mez, C., White, J.C., Wulder, M.A., 2016. Optical remotely sensed time series data for Huston, M., Smith, T., 1987. Plant succession: life history and competition. Am. Nat. 130,
land cover classification: A review. ISPRS J. Photogramm. Remote Sens. 116, 55–72. 168–198. https://doi.org/10.1016/j.ecoleng.2021.106331.
https://doi.org/10.1016/j.isprsjprs.2016.03.008.
16

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Jensen, J.R., 2009. Remote Sensing of the Environment: An Earth Resource Perspective active fire characteristics and post-fire effects. Int. J. Wildl. Fire 15, 319–345.
2/e. Pearson Education India. https://doi.org/10.1071/WF05097.
Jiao, Z., Woodcock, C., Schaaf, C.B., Tan, B., Liu, J., Gao, F., Strahler, A., Li, X., Wang, J., Levin, N., Kyba, C.C.M., Zhang, Q., de Miguel, A.S., Roma´n, M.O., Li, X., Portnov, B.A.,
2011. Improving MODIS land cover classification by combining MODIS spectral and Molthan, A.L., Jechow, A., Miller, S.D., 2020. Remote sensing of night lights: A
angular signatures in a Canadian boreal forest. Can. J. Remote. Sens. 37, 184–203. review and an outlook for the future. Remote Sens. Environ. 237, 111443.
https://doi.org/10.5589/m11-030. Levin, Noam, 2017. The impact of seasonal changes on observed nighttime brightness
Jin, S., Homer, C., Yang, L., Danielson, P., Dewitz, J., Li, C., Zhu, Z., Xian, G., Howard, D., from 2014 to 2015 monthly VIIRS DNB composites. Remote Sens. Environ. 193,
2019. Overall methodology design for the United States national land cover database 150–164. https://doi.org/10.1016/j.rse.2017.03.003.
2016 products. Remote Sens. 11 https://doi.org/10.3390/rs11242971. Li, J., Roy, D.P., 2017. A global analysis of Sentinel-2A, Sentinel-2B and Landsat-8 data
Jin, S., Sader, S.A., 2005. MODIS time-series imagery for forest disturbance detection and revisit intervals and implications for terrestrial monitoring. Remote Sens. 9, 902.
quantification of patch size effects. Remote Sens. Environ. 99, 462–470. https://doi. https://doi.org/10.3390/rs9090902.
org/10.1016/j.rse.2005.09.017. Li, X., Elvidge, C., Zhou, Y., Cao, C., Warner, T., 2017. Remote sensing of night-time
Johnson, E.A., Miyanishi, K., 2021. Disturbance and succession. In: Johnson, E.A., light. Int. J. Remote Sens. 38, 5855–5859.
Miyanishi, K.B.T.-P.D.E. (Eds.), Plant Disturbance Ecology, Second edition. Lin, Y., Zhu, Z., Guo, W., Sun, Y., Yang, X., Kovalskyy, V., 2020. Continuous monitoring
Academic Press, San Diego, pp. 1–15. https://doi.org/10.1016/B978-0-12-818813- of cotton stem water potential using Sentinel-2 imagery. Remote Sens. 12, 1176.
2.00001-0. https://doi.org/10.3390/rs12071176.
Johnson, E.W., Wittwer, D., 2008. Aerial detection surveys in the United States. Aust. Liu, H., Gong, P., Wang, J., Wang, X., Ning, G., Xu, B., 2021a. Production of global daily
For. 71, 212–215. https://doi.org/10.1080/00049158.2008.10675037. seamless data cubes and quantification of global land cover change from 1985 to
Justice, C.O., Giglio, L., Korontzi, S., Owens, J., Morisette, J.T., Roy, D., Descloitres, J., 2020 - iMap World 1.0. Remote Sens. Environ. 258, 112364. https://doi.org/
Alleaume, S., Petitcolin, F., Kaufman, Y., 2002. The MODIS fire products. Remote 10.1016/j.rse.2021.112364.
Sens. Environ. 83, 244–262. https://doi.org/10.1016/S0034-4257(02)00076-7. Liu, X., Huang, Y., Xu, X., Li, Xuecao, Li, Xia, Ciais, P., Lin, P., Gong, K., Ziegler, A.D.,
Justice, C.O., Vermote, E., Townshend, J.R.G., Defries, R., Roy, D.P., Hall, D.K., Chen, A., Gong, P., Chen, J., Hu, G., Chen, Y., Wang, S., Wu, Q., Huang, K., Estes, L.,
Salomonson, V.V., Privette, J.L., Riggs, G., Strahler, A., 1998. The Moderate Zeng, Z., 2020a. High-spatiotemporal-resolution mapping of global urban change
Resolution Imaging Spectroradiometer (MODIS): land remote sensing for global from 1985 to 2015. Nat. Sustain. 3, 564–570. https://doi.org/10.1038/s41893-020-
change research. IEEE Trans. Geosci. Remote Sens. 36, 1228–1249. 0521-x.
Kennedy, R.E., Andr´efou¨et, S., Cohen, W.B., Go´mez, C., Griffiths, P., Hais, M., Healey, S. Liu, Y., Wang, Z., Sun, Q., Erb, A.M., Li, Z., Schaaf, C.B., Zhang, X., Rom´an, M.O.,
P., Helmer, E.H., Hostert, P., Lyons, M.B., 2014. Bringing an ecological view of Scott, R.L., Zhang, Q., Novick, K.A., Syndonia Bret-Harte, M., Petroy, S.,
change to Landsat-based remote sensing. Front. Ecol. Environ. 12, 339–346. https:// SanClements, M., 2017. Evaluation of the VIIRS BRDF, Albedo and NBAR products
doi.org/10.1890/130066. suite and an assessment of continuity with the long term MODIS record. Remote
Kennedy, R.E., Cohen, W.B., Schroeder, T.A., 2007. Trajectory-based change detection Sens. Environ. 201, 256–274. https://doi.org/10.1016/j.rse.2017.09.020.
for automated characterization of forest disturbance dynamics. Remote Sens. Liu, Y., Xu, B., Zhi, W., Hu, C., Dong, Y., Jin, S., Lu, Y., Chen, T., Xu, W., Liu, Yongchao,
Environ. 110, 370–386. https://doi.org/10.1016/j.rse.2007.03.010. Zhao, B., Lu, W., 2020b. Space eye on flying aircraft: From Sentinel-2 MSI parallax to
Kennedy, R.E., Townsend, P.A., Gross, J.E., Cohen, W.B., Bolstad, P., Wang, Y.Q., hybrid computing. Remote Sens. Environ. 246, 111867 https://doi.org/10.1016/j.
Adams, P., 2009. Remote sensing change detection tools for natural resource rse.2020.111867.
managers: Understanding concepts and tradeoffs in the design of landscape Liu, J., Yang, Z., Liu, Y., Mu, C., 2021b. Hyperspectral remote sensing images deep
monitoring projects. Remote Sens. Environ. 113, 1382–1396. https://doi.org/ feature extraction based on mixed feature and convolutional neural networks.
10.1016/j.rse.2008.07.018. Remote Sens. 13 https://doi.org/10.3390/rs13132599.
Kennedy, R.E., Yang, Z., Braaten, J., Copass, C., Antonova, N., Jordan, C., Nelson, P., Loveland, T.R., Sohl, T.L., Stehman, S.V., Gallant, A.L., Sayler, K.L., Napton, D.E., 2002.
2015. Attribution of disturbance change agent from Landsat time-series in support of A strategy for estimating the rates of recent United States land-cover changes.
habitat monitoring in the Puget Sound region, USA. Remote Sens. Environ. 166, Photogramm. Eng. Remote Sens. 68, 1091–1099.
271–285. https://doi.org/10.1016/j.rse.2015.05.005. Lu, D., Mausel, P., Brondizio, E., Moran, E., 2004. Change detection techniques. Int. J.
Kennedy, R.E., Yang, Z., Cohen, W.B., 2010. Detecting trends in forest disturbance and Remote Sens. 25, 2365–2401.
recovery using yearly Landsat time series: 1. LandTrendr—Temporal segmentation Martin, L., Howarth, P.J., 1989. Change-detection accuracy assessment using SPOT
algorithms. Remote Sens. Environ. 114, 2897–2910. https://doi.org/10.1016/j. multispectral imagery of the rural-urban fringe. Remote Sens. Environ. 30, 55–66.
rse.2010.07.008. https://doi.org/10.1016/0034-4257(89)90047-3.
Key, T., Warner, T.A., McGraw, J.B., Fajvan, M.A., 2001. A comparison of multispectral Mascorro, V.S., Coops, N.C., Kurz, W.A., Olguín, M., 2015. Choice of satellite imagery
and multitemporal information in high spatial resolution imagery for classification and attribution of changes to disturbance type strongly affects forest carbon balance
of individual tree species in a temperate hardwood forest. Remote Sens. Environ. 75, estimates. Carbon Balance Manag. 10, 1–15.
100–112. Masek, J.G., Huang, C., Wolfe, R., Cohen, W., Hall, F., Kutler, J., Nelson, P., 2008. North
Kirschbaum, D.B., Adler, R., Hong, Y., Hill, S., Lerner-Lam, A., 2010. A global landslide American forest disturbance mapped from a decadal Landsat record. Remote Sens.
catalog for hazard applications: method, results, and limitations. Nat. Hazards 52, Environ. 112, 2914–2926. https://doi.org/10.1016/j.rse.2008.02.010.
561–575. https://doi.org/10.1007/s11069-009-9401-4. Masek, J.G., Vermote, E.F., Saleous, N.E., Wolfe, R., Hall, F.G., Huemmrich, K.F., Gao, F.,
Knoflach, B., Ramskogler, K., Talluto, M., Hofmeister, F., Haas, F., Heckmann, T., Kutler, J., Lim, T.-K., 2006. A Landsat surface reflectance dataset for North America,
Pfeiffer, M., Piermattei, L., Ressl, C., Wimmer, M.H., 2021. Modelling of vegetation 1990–2000. IEEE Geosci. Remote Sens. Lett. 3, 68–72. https://doi.org/10.1109/
dynamics from satellite time series to determine proglacial primary succession in the LGRS.2005.857030.
course of global warming—a case study in the Upper Martell Valley (Eastern Italian Masek, J.G., Wulder, M.A., Markham, B., McCorkel, J., Crawford, C.J., Storey, J.,
Alps). Remote Sens. 13, 4450. Jenstrom, D.T., 2020. Landsat 9: Empowering open science and applications through
Kussul, N., Lavreniuk, M., Skakun, S., Shelestov, A., 2017. Deep Learning Classification continuity. Remote Sens. Environ. 248, 111968 https://doi.org/10.1016/j.
of Land Cover and Crop Types Using Remote Sensing Data. IEEE Geosci. Remote rse.2020.111968.
Sens. Lett. 14, 778–782. https://doi.org/10.1109/LGRS.2017.2681128. Meng, R., Dennison, P.E., Zhao, F., Shendryk, I., Rickert, A., Hanavan, R.P., Cook, B.D.,
Laflower, D.M., Hurteau, M.D., Koch, G.W., North, M.P., Hungate, B.A., 2016. Climate- Serbin, S.P., 2018. Mapping canopy defoliation by herbivorous insects at the
driven changes in forest succession and the influence of management on forest individual tree level using bi-temporal airborne imaging spectroscopy and LiDAR
carbon dynamics in the Puget Lowlands of Washington StateUSA. For. Ecol. Manage. measurements. Remote Sens. Environ. 215, 170–183.
362, 194–204. https://doi.org/10.1016/j.foreco.2015.12.015. Mildrexler, D.J., Zhao, M., Running, S.W., 2009. Testing a MODIS global disturbance
Lambin, E.F., 2004. Linking socioeconomic and remote sensing data at the community or index across North America. Remote Sens. Environ. 113, 2103–2117. https://doi.
at the household level. In: People and the Environment. Springer, pp. 223–240. org/10.1016/j.rse.2009.05.016.
Lambin, E.F., Strahler, A.H., 1994. Change-vector analysis in multitemporal space: A tool Minale, A.S., 2013. Retrospective analysis of land cover and use dynamics in Gilgel
to detect and categorize land-cover change processes using high temporal-resolution Abbay Watershed by using GIS and remote sensing techniquesNorthwestern
satellite data. Remote Sens. Environ. 48, 231–244. https://doi.org/10.1016/0034- Ethiopia. Int. J. Geosci. 4, 1003.
4257(94)90144-9. Molinier, M., Miettinen, J., Ienco, D., Qiu, S., Zhu, Z., 2021. Optical satellite image time
Lambin, E.F., Turner, B.L., Geist, H.J., Agbola, S.B., Angelsen, A., Bruce, J.W., series analysis for environment applications: from classical methods to deep learning
Coomes, O.T., Dirzo, R., Fischer, G., Folke, C., 2001. The causes of land-use and land- and beyond. In: Change Detection and Image Time Series Analysis 2: Supervised
cover change: Moving beyond the myths. Glob. Environ. Chang. 11, 261–269. Methods. Wiley Online Library, pp. 109–154.
https://doi.org/10.1016/S0959-3780(01)00007-3. Myneni, R.B., Keeling, C.D., Tucker, C.J., Asrar, G., Nemani, R.R., 1997. Increased plant
Latifovic, R., Homer, C., Ressl, R., Pouliot, D., Hossain, S.N., Colditz, R.R., Olthof, I., growth in the northern high latitudes from 1981 to 1991. Nature 386, 698–702.
Giri, C.P., Victoria, A., 2016. North American land-change monitoring system. https://doi.org/10.1038/386698a0.
Remote Sens. 303. L. use L. Cover. Noaa, 2022. Severe Weather Data Inventory [WWW Document]. NOAA (accessed
Latifovic, R., Pouliot, D., 2005. Multitemporal land cover mapping for Canada: 1.4.22). https://www.ncei.noaa.gov/products/severe-weather-data-inventory.
methodology and products. Can. J. Remote. Sens. 31, 347–363. Nrc, 2013. Advancing Land Change Modeling: Opportunities and Research
Lawrence, R., 2005. Remote sensing of vegetation responses during the first 20 years Requirements. National Academies Press.
following the 1980 eruption of Mount St. Helens: a spatially and temporally Nrc, 1999. Human Dimensions of Global Environmental Change: Research Pathways for
stratified analysis. In: Ecological Responses to the 1980 Eruption of Mount St. the Next Decade. National Academies Press.
Helens. Springer, New York, NY, pp. 111–123. https://doi.org/10.1007/0-387- Nrc, 1998. <book-title>People and Pixels: Linking Remote Sensing and Social </book-
28150-9_8. title>Science. National Academies Press.
Lentile, L.B., Holden, Z.A., Smith, A.M.S., Falkowski, M.J., Hudak, A.T., Morgan, P.,
Lewis, S.A., Gessler, P.E., Benson, N.C., 2006. Remote sensing techniques to assess
17

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Oeser, J., Pflugmacher, D., Senf, C., Heurich, M., Hostert, P., 2017. Using intra-annual and Analysis (FIA) data. Remote Sens. Environ. 114, 2337–2352. https://doi.org/
Landsat time series for attributing forest disturbance agents in Central Europe. 10.1016/j.rse.2010.05.010.
Forests 8, 251. https://doi.org/10.3390/f8070251. Rigge, M., Shi, H., Homer, C., Danielson, P., Granneman, B., 2019. Long-term trajectories
Oliver, C.D., Larson, B.C., 1996. Forest Stand Dynamics, Updated edition. John Wiley of fractional component change in the Northern Great Basin, USA. Ecosphere 10,
and sons. e02762.
Olofsson, P., Foody, G.M., Stehman, S.V., Woodcock, C.E., 2013. Making better use of Rindfuss, R.R., Walsh, S.J., Turner, B.L., Fox, J., Mishra, V., 2004. Developing a science
accuracy data in land change studies: Estimating accuracy and area and quantifying of land change: challenges and methodological issues. Proc. Natl. Acad. Sci. 101,
uncertainty using stratified estimation. Remote Sens. Environ. 129, 122–131. 13976–13981. https://doi.org/10.1073/pnas.0401545101.
https://doi.org/10.1016/j.rse.2012.10.031. Rindfuss, R.R., Walsh, S.J., Turner, B.L., Moran, E.F., Entwisle, B., 2012. Linking Pixels
Ortiz, S.M., Breidenbach, J., K¨andler, G., 2013. Early detection of bark beetle green and People. In: Gutman, G., Janetos, A.C., Justice, C.O., Moran, E.F., Mustard, J.F.,
attack using TerraSAR-X and RapidEye data. Remote Sens. 5, 1912–1931. Rindfuss, R.R., Skole, D., Turner, Billy Lee, Cochrane, M.A. (Eds.), Land Change
Osin´ska-Skotak, K., Radecka, A., Pio´rkowski, H., Michalska-Hejduk, D., Kope´c, D., Science: Observing. Monitoring and Understanding Trajectories of Change on the
Tokarska-Guzik, B., Ostrowski, W., Kania, A., Niedzielko, J., 2019. Mapping Earth’s Surface. Springer, Netherlands, Dordrecht, pp. 379–394. https://doi.org/
succession in non-forest habitats by means of remote sensing: Is the data acquisition 10.1007/978-1-4020-2562-4_22.
time critical for species discrimination? Remote Sens. 11, 2629. Rittenhouse, C.D., Berlin, E.H., Mikle, N., Qiu, S., Riordan, D., Zhu, Z., 2022. An Object-
Pasquarella, V.J., Holden, C.E., Woodcock, C.E., 2018. Improved mapping of forest type Based Approach to Map Young Forest and Shrubland Vegetation Based on Multi-
using spectral-temporal Landsat features. Remote Sens. Environ. 210, 193–207. Source Remote Sensing Data. Remote Sens. 14, 1091.
https://doi.org/10.1016/j.rse.2018.02.064. Rogan, J., Franklin, J., Stow, D., Miller, J., Woodcock, C., Roberts, D., 2008. Mapping
Pekel, J.-F., Cottam, A., Gorelick, N., Belward, A.S., 2016. High-resolution mapping of land-cover modifications over large areas: A comparison of machine learning
global surface water and its long-term changes. Nature 540, 418–422. https://doi. algorithms. Remote Sens. Environ. 112, 2272–2283.
org/10.1038/nature20584. Rollins, M.G., 2009. LANDFIRE: A nationally consistent vegetation, wildland fire, and
Pengra, B.W., Stehman, S.V., Horton, J.A., Dockter, D.J., Schroeder, T.A., Yang, Z., fuel assessment. Int. J. Wildl. Fire 18, 235–249. https://doi.org/10.1071/WF08088.
Cohen, W.B., Healey, S.P., Loveland, T.R., 2020. Quality control and assessment of Rom´an, M.O., Wang, Z., Sun, Q., Kalb, V., Miller, S.D., Molthan, A., Schultz, L., Bell, J.,
interpreter consistency of annual land cover reference data in an operational Stokes, E.C., Pandey, B., 2018. NASA’s Black Marble nighttime lights product suite.
national monitoring program. Remote Sens. Environ. 238, 111261 https://doi.org/ Remote Sens. Environ. 210, 113–143. https://doi.org/10.1016/j.rse.2018.03.017.
10.1016/j.rse.2019.111261. Rosser, J.F., Leibovici, D.G., Jackson, M.J., 2017. Rapid flood inundation mapping using
P´erez-Cabello, F., Montorio, R., Alves, D.B., 2021. Remote sensing techniques to assess social media, remote sensing and topographic data. Nat. Hazards 87, 103–120.
post-fire vegetation recovery. Curr. Opin. Environ. Sci. Heal. 21, 100251. Roy, D.P., Huang, H., Houborg, R., Martins, V.S., 2021. A global analysis of the temporal
Pesaresi, M., Ehrlich, D., Ferri, S., Florczyk, A., Freire, S., Halkia, M., Julea, A., availability of PlanetScope high spatial resolution multi-spectral imagery. Remote
Kemper, T., Soille, P., Syrris, V., 2016. Operating Procedure for the Production of the Sens. Environ. 264, 112586 https://doi.org/10.1016/j.rse.2021.112586.
Global Human Settlement Layer from Landsat Data of the Epochs 1975, 1990, 2000, Roy, D.P., Wulder, M.A., Loveland, T.R., Ce, W., Allen, R.G., Anderson, M.C., Helder, D.,
and 2014. Publications Office of the European Union, Luxembourg (Luxembourg). Irons, J.R., Johnson, D.M., Kennedy, R., Scambos, T.A., Schaaf, C.B., Schott, J.R.,
https://doi.org/10.2788/656115. Sheng, Y., Vermote, E.F., Belward, A.S., Bindschadler, R., Cohen, W.B., Gao, F.,
Peters, D.P.C., Lugo, A.E., Chapin III, F.S., Pickett, S.T.A., Duniway, M., Rocha, A.V., Hipple, J.D., Hostert, P., Huntington, J., Justice, C.O., Kilic, A., Kovalskyy, V., Lee, Z.
Swanson, F.J., Laney, C., Jones, J., 2011. Cross-system comparisons elucidate P., Lymburner, L., Masek, J.G., McCorkel, J., Shuai, Y., Trezza, R., Vogelmann, J.,
disturbance complexities and generalities. Ecosphere 2, 1–26. https://doi.org/ Wynne, R.H., Zhu, Z., 2014. Landsat-8: Science and product vision for terrestrial
10.1890/ES11-00115.1. global change research. Remote Sens. Environ. 145, 154–172. https://doi.org/
Petit, C., Scudder, T., Lambin, E., 2001. Quantifying processes of land-cover change by 10.1016/j.rse.2014.02.001.
remote sensing: resettlement and rapid land-cover changes in south-eastern Zambia. Roy, D.P., Zhang, H.K., Ju, J., Gomez-Dans, J.L., Lewis, P.E., Schaaf, C.B., Sun, Q., Li, J.,
Int. J. Remote Sens. 22, 3435–3456. https://doi.org/10.1080/01431160010006881. Huang, H., Kovalskyy, V., 2016. A general method to normalize Landsat reflectance
Potapov, P., Hansen, M.C., Pickens, A., Hernandez-Serna, A., Tyukavina, A., data to nadir BRDF adjusted reflectance. Remote Sens. Environ. 176, 255–271.
Turubanova, S., Zalles, V., Li, X., Khan, A., Stolle, F., Harris, N., Song, X.-P., https://doi.org/10.1016/j.rse.2016.01.023.
Baggett, A., Kommareddy, I., Kommareddy, A., 2022. The Global 2000–2020 Land Saleska, S.R., Didan, K., Huete, A.R., Da Rocha, H.R., 2007. Amazon forests green-up
Cover and Land Use Change Dataset Derived From the Landsat Archive: First Results. during 2005 drought. Science 318, 612. https://doi.org/10.1126/science.1146663.
Front. Remote Sens. 3 https://doi.org/10.3389/frsen.2022.856903. Samanta, A., Ganguly, S., Hashimoto, H., Devadiga, S., Vermote, E., Knyazikhin, Y.,
Potter, C., Tan, P., Steinbach, M., Klooster, S., Kumar, V., Myneni, R., Genovese, V., Nemani, R.R., Myneni, R.B., 2010. Amazon forests did not green-up during the 2005
2003. Major disturbance events in terrestrial ecosystems detected using global drought. Geophys. Res. Lett. 37 https://doi.org/10.1029/2009GL042154.
satellite data sets. Glob. Chang. Biol. 9, 1005–1021. https://doi.org/10.1046/j.1365- Schaaf, C.B., Gao, F., Strahler, A.H., Lucht, W., Li, X., Tsang, T., Strugnell, N.C.,
2486.2003.00648.x. Zhang, X., Jin, Y., Muller, J.-P.P., Lewis, P., Barnsley, M., Hobson, P., Disney, M.,
Pouliot, D., Alavi, N., Wilson, S., Duffe, J., Pasher, J., Davidson, A., Daneshfar, B., Roberts, G., Dunderdale, M., Doll, C., D’Entremont, R.P., Hu, B., Liang, S.,
Lindsay, E., 2021. Assessment of Landsat Based Deep-Learning Membership Analysis Privette, J.L., Roy, D., 2002. First operational BRDF, albedo nadir reflectance
for Development of from–to Change Time Series in the Prairie Region of Canada products from MODIS. Remote Sens. Environ. 83, 135–148. https://doi.org/
from 1984 to 2018. Remote Sens. 13, 634. 10.1016/S0034-4257(02)00091-3.
Pouliot, D., Latifovic, R., 2016. Land change attribution based on Landsat time series and Schmitt, M., Zhu, X.X., 2016. Data fusion and remote sensing: An ever-growing
integration of ancillary disturbance data in the Athabasca oil sands region of Canada. relationship. IEEE Geosci. Remote Sens. Mag. 4, 6–23.
GIScience Remote Sens. 53, 382–401. Schnebele, E., Cervone, G., Kumar, S., Waters, N., 2014. Real time estimation of the
Pouliot, D., Latifovic, R., Olthof, I., 2009. Trends in vegetation NDVI from 1 km AVHRR Calgary floods using limited remote sensing data. Water 6, 381–398.
data over Canada for the period 1985–2006. Int. J. Remote Sens. 30, 149–168. Schroeder, T.A., Schleeweis, K.G., Moisen, G.G., Toney, C., Cohen, W.B., Freeman, E.A.,
Pouliot, D., Latifovic, R., Zabcic, N., Guindon, L., Olthof, I., 2014. Development and Yang, Z., Huang, C., 2017. Testing a Landsat-based approach for mapping
assessment of a 250 m spatial resolution MODIS annual land cover time series disturbance causality in US forests. Remote Sens. Environ. 195, 230–243. https://
(2000–2011) for the forest region of Canada derived from change-based updating. doi.org/10.1016/j.rse.2017.03.033.
Remote Sens. Environ. 140, 731–743. Sebald, J., Senf, C., Seidl, R., 2021. Human or natural? Landscape context improves the
Pricope, N.G., Mapes, K.L., Woodward, K.D., 2019. Remote sensing of attribution of forest disturbances mapped from Landsat in Central Europe. Remote
human–environment interactions in global change research: a review of advances, Sens. Environ. 262, 112502 https://doi.org/10.1016/j.rse.2021.112502.
challenges and future directions. Remote Sens. https://doi.org/10.3390/ Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
rs11232783. Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Qin, Y., Xiao, X., Wigneron, J.-P., Ciais, P., Brandt, M., Fan, L., Li, X., Crowell, S., Wu, X., Nat. Clim. Chang. 7, 395–402. https://doi.org/10.1038/nclimate3303.
Doughty, R., 2021. Carbon loss from forest degradation exceeds that from Sellers, P.J., Meeson, B.W., Hall, F.G., Asrar, G., Murphy, R.E., Schiffer, R.A.,
deforestation in the Brazilian Amazon. Nat. Clim. Chang. 11, 442–448. https://doi. Bretherton, F.P., Dickinson, R.E., Ellingson, R.G., Field, C.B., 1995. Remote sensing
org/10.1038/s41558-021-01026-5. of the land surface for studies of global change: Models—algorithms—experiments.
Qiu, S., Lin, Y., Shang, R., Zhang, J., Ma, L., Zhu, Z., Qiu, S., Lin, Y., Shang, R., Zhang, J., Remote Sens. Environ. 51, 3–26. https://doi.org/10.1016/0034-4257(94)00061-Q.
Ma, L., Zhu, Z., 2019a. Making landsat time series consistent: evaluating and Senf, C., Pflugmacher, D., Wulder, M.A., Hostert, P., 2015. Characterizing
improving landsat analysis ready data. Remote Sens. 11 https://doi.org/10.3390/ spectral–temporal patterns of defoliator and bark beetle disturbances using Landsat
RS11010051. time series. Remote Sens. Environ. 170, 166–177.
Qiu, S., Zhu, Z., He, B., 2019b. Fmask 4.0: Improved cloud and cloud shadow detection in Senf, C., Seidl, R., 2022. Post-disturbance canopy recovery and the resilience of Europe’s
Landsats 4–8 and Sentinel-2 imagery. Remote Sens. Environ. 231, 111205 https:// forests. Glob. Ecol. Biogeogr. 31, 25–36.
doi.org/10.1016/j.rse.2019.05.024. Senf, C., Seidl, R., Hostert, P., 2017. Remote sensing of forest insect disturbances: Current
Raitsos, D.E., Pradhan, Y., Brewin, R.J.W., Stenchikov, G., Hoteit, I., 2013. Remote state and future directions. Int. J. Appl. Earth Obs. Geoinf. 60, 49–60. https://doi.
sensing the phytoplankton seasonal succession of the Red Sea. PLoS One 8, e64909. org/10.1016/j.jag.2017.04.004.
Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving Sesnie, S.E., Tellman, B., Wrathall, D., McSweeney, K., Nielsen, E., Benessaiah, K.,
near-real time deforestation monitoring in tropical dry forests by combining dense Wang, O., Rey, L., 2017. A spatio-temporal analysis of forest loss related to cocaine
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ. trafficking in Central America. Environ. Res. Lett. 12, 54015.
204, 147–161. https://doi.org/10.1016/j.rse.2017.10.034. Seto, K.C., Kaufmann, R.K., 2003. Modeling the drivers of urban land use change in the
Riemann, R., Wilson, B.T., Lister, A., Parks, S., 2010. An effective assessment protocol for Pearl River Delta, China: Integrating remote sensing with socioeconomic data. Land
continuous geospatial datasets of forest characteristics using USFS Forest Inventory Econ. 79, 106–121.
18

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Seto, K.C., Reenberg, A., Boone, C.G., Fragkias, M., Haase, D., Langanke, T., Wang, Z., Rom´an, M.O., Kalb, V.L., Miller, S.D., Zhang, J., Shrestha, R.M., 2021.
Marcotullio, P., Munroe, D.K., Olah, B., Simon, D., 2012. Urban land teleconnections Quantifying uncertainties in nighttime light retrievals from Suomi-NPP and NOAA-
and sustainability. Proc. Natl. Acad. Sci. 109, 7687–7692. https://doi.org/10.1073/ 20 VIIRS Day/Night Band data. Remote Sens. Environ. 263, 112557 https://doi.org/
pnas.1117622109. 10.1016/j.rse.2021.112557.
Shang, R., Zhu, Z., 2019. Harmonizing Landsat 8 and Sentinel-2: A time-series-based Warner, T., Almutairi, A., Lee, J.Y., 2009. Remote Sensing of Land Cover Change. SAGE,
reflectance adjustment approach. Remote Sens. Environ. 235, 111439 https://doi. London, UK.
org/10.1016/j.rse.2019.111439. White, J.C., Hermosilla, T., Wulder, M.A., Coops, N.C., 2022. Mapping, validating, and
Shang, R., Zhu, Z., Zhang, J., Qiu, S., Yang, Z., Li, T., Yang, X., 2022. Near-real-time interpreting spatio-temporal trends in post-disturbance forest recovery. Remote
monitoring of land disturbance with harmonized Landsats 7–8 and Sentinel-2 data. Sens. Environ. 271, 112904.
Remote Sens. Environ. 278, 113073 https://doi.org/10.1016/j.rse.2022.113073. White, J.C., Saarinen, N., Kankare, V., Wulder, M.A., Hermosilla, T., Coops, N.C.,
Shimizu, K., Ota, T., Mizoue, N., Yoshida, S., 2019. A comprehensive evaluation of Pickell, P.D., Holopainen, M., Hyyppa¨, J., Vastaranta, M., 2018. Confirmation of
disturbance agent classification approaches: Strengths of ensemble classification, post-harvest spectral recovery from Landsat time series using measures of forest
multiple indices, spatio-temporal variables, and direct prediction. ISPRS J. cover and height derived from airborne laser scanning data. Remote Sens. Environ.
Photogramm. Remote Sens. 158, 99–112. https://doi.org/10.1016/j. 216, 262–275.
isprsjprs.2019.10.004. White, J.C., Saarinen, N., Wulder, M.A., Kankare, V., Hermosilla, T., Coops, N.C.,
Singh, A., 1989. Digital change detection techniques using remotely-sensed data. Int. J. Holopainen, M., Hyypp¨a, J., Vastaranta, M., 2019. Assessing spectral measures of
Remote Sens. 10, 989–1003. https://doi.org/10.1080/01431168908903939. post-harvest forest recovery with field plot data. Int. J. Appl. Earth Obs. Geoinf. 80,
Sohl, T.L., Gallant, A.L., Loveland, T.R., 2004. The characteristics and interpretability of 102–114.
land surface change and implications for project design. Photogramm. Eng. Remote White, J.C., Wulder, M.A., Hermosilla, T., Coops, N.C., Hobart, G.W., 2017. A nationwide
Sensing 70, 439–448. https://doi.org/10.14358/PERS.70.4.439. annual characterization of 25 years of forest disturbance and recovery for Canada
Song, C., Woodcock, C.E., Seto, K.C., Lenney, M.P., Macomber, S.A., 2001. Classification using Landsat time series. Remote Sens. Environ. 194, 303–321.
and change detection using Landsat TM data: when and how to correct atmospheric White, P.S., Pickett, S.T.A., 1985. Natural disturbance and patch dynamics: an
effects? Remote SensEnvironment 75, 230–244. https://doi.org/10.1016/S0034- introduction. In: Pickett, S.T.A., White, P.S. (Eds.), The Ecology of Natural
4257(00)00169-3. Disturbance and Patch Dynamics. Academic Press, San Diego, pp. 3–13.
Song, X.P., Hansen, M.C., Stehman, S.V., Potapov, P.V., Tyukavina, A., Vermote, E.F., Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,
Townshend, J.R., 2018. Global land change from 1982 to 2016. Nature 560, Gao, F., Goward, S.N., Helder, D., Helmer, E., Nemani, R., Oreopoulos, L., Schott, J.,
639–643. https://doi.org/10.1038/s41586-018-0411-9. Thenkabail, P.S., Vermote, E.F., Vogelmann, J., Wulder, M.A., Wynne, R., 2008. Free
Sousa, W.P., 1984. The role of disturbance in natural communities. Annu. Rev. Ecol. Syst. access to Landsat imagery. Science 320, 1011. https://doi.org/10.1126/
15, 353–391. science.320.5879.1011a.
Strahler, A.H., Woodcock, C.E., Smith, J.A., 1986. On the nature of models in remote Woodcock, C.E., Loveland, T.R., Herold, M., Bauer, M.E., 2020. Transitioning from
sensing. Remote Sens. Environ. 20, 121–139. change detection to monitoring with remote sensing: A paradigm shift. Remote Sens.
Sulla-Menashe, D., Woodcock, C.E., Friedl, M.A., 2018. Canadian boreal forest greening Environ. 238, 111558 https://doi.org/10.1016/j.rse.2019.111558.
and browning trends: an analysis of biogeographic patterns and the relative roles of Wulder, M.A., Coops, N.C., Roy, D.P., White, J.C., Hermosilla, T., 2018. Land cover 2.0.
disturbance versus climate drivers. Environ. Res. Lett. 13, 14007. Int. J. Remote Sens. 39, 4254–4284. https://doi.org/10.1080/
Szostak, M., Hawryło, P., Piela, D., 2018. Using of Sentinel-2 images for automation of 01431161.2018.1452075.
the forest succession detection. Eur. J. Remote Sens. 51, 142–149. https://doi.org/ Wulder, M.A., Masek, J.G., Cohen, W.B., Loveland, T.R., Woodcock, C.E., 2012. Opening
10.1080/22797254.2017.1412272. the archive: How free data has enabled the science and monitoring promise of
Tan, B., Masek, J.G., Wolfe, R., Gao, F., Huang, C., Vermote, E.F., Sexton, J.O., Landsat. Remote Sens. Environ. 122, 2–10. https://doi.org/10.1016/j.
Ederer, G., 2013. Improved forest change detection with terrain illumination rse.2012.01.010.
corrected Landsat images. Remote Sens. Environ. 136, 469–483. https://doi.org/ Wulder, M.A., Roy, D.P., Radeloff, V.C., Loveland, T.R., Anderson, M.C., Johnson, D.M.,
10.1016/j.rse.2013.05.013. Healey, S., Zhu, Z., Scambos, T.A., Pahlevan, N., Hansen, M., 2022. Fifty years of
Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time Landsat science and impacts. Remote Sens. Environ. 280, 113195 https://doi.org/
monitoring of tropical forest disturbance: New algorithms and assessment 10.1016/j.rse.2022.113195.
framework. Remote Sens. Environ. 224, 202–218. https://doi.org/10.1016/j. Wyman, M.S., Stein, T.V., 2010. Modeling social and land-use/land-cover change data to
rse.2019.02.003. assess drivers of smallholder deforestation in Belize. Appl. Geogr. 30, 329–342.
Tang, X., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2020. Can VIIRS continue the Xian, G., Homer, C., Fry, J., 2009. Updating the 2001 National Land Cover Database land
legacy of MODIS for near real-time monitoring of tropical forest disturbance? cover classification to 2006 by using Landsat imagery change detection methods.
Remote Sens. Environ. 249, 112024. Remote Sens. Environ. 113, 1133–1147.
Tellman, B., Sesnie, S.E., Magliocca, N.R., Nielsen, E.A., Devine, J.A., McSweeney, K., Xian, G.Z., Smith, K., Wellington, D., Horton, J., Zhou, Q., Li, C., Auch, R., Brown, J.F.,
Jain, M., Wrathall, D.J., Da´vila, A., Benessaiah, K., 2020. Illicit drivers of land use Zhu, Z., Reker, R.R., 2022. Implementation of the CCDC algorithm to produce the
change: Narcotrafficking and forest loss in Central America. Glob. Environ. Chang. LCMAP Collection 1.0 annual land surface change product. Earth Syst. Sci. Data 14,
63, 102092. 143–162.
Tollerud, H.J., Brown, J.F., Loveland, T.R., 2020. Investigating the effects of land use and Xie, Q., Dash, J., Huang, W., Peng, D., Qin, Q., Mortimer, H., Casa, R., Pignatti, S.,
land cover on the relationship between moisture and reflectance using Landsat time Laneve, G., Pascucci, S., 2018. Vegetation indices combining the red and red-edge
series. Remote Sens. 12, 1919. https://doi.org/10.3390/rs12121919. spectral information for leaf area index retrieval. IEEE J. Sel. Top. Appl. earth Obs.
Turner, B.L., 1997. The sustainability principle in global agendas: implications for Remote Sens. 11, 1482–1493.
understanding land-use/cover change. Geogr. J. 163, 133–140. Xin, Q.C., Olofsson, P., Zhu, Z., Tan, B., Woodcock, C.E., 2013. Toward near real-time
Turner, B.L., Lambin, E.F., Verburg, P.H., 2021. From land-use/land-cover to land system monitoring of forest disturbance by fusion of MODIS and Landsat data. Remote Sens.
science. Ambio 50, 1291–1294. https://doi.org/10.1007/s13280-021-01510-4. Environ. 135, 234–247. https://doi.org/10.1016/J.Rse.2013.04.002.
Turner, B.L., Lambin, E.F., Reenberg, A., 2007. The emergence of land change science for Yan, L., Roy, D.P., Zhang, H., Li, J., Huang, H., 2016. An automated approach for sub-
global environmental change and sustainability. Proc. Natl. Acad. Sci. 104, pixel registration of Landsat-8 Operational Land Imager (OLI) and Sentinel-2 Multi
20666–20671. https://doi.org/10.1073/pnas.0704119104. Spectral Instrument (MSI) imagery. Remote Sens. 8, 520. https://doi.org/10.3390/
Turner, M.G., 2010. Disturbance and landscape dynamics in a changing world. Ecology rs8060520.
91, 2833–2849. https://doi.org/10.1890/10-0097.1. Yang, X., Zhu, Zhe, Qiu, S., Kroeger, K.D., Zhu, Zhiliang, Covington, S., 2022. Detection
Ustin, S.L., Middleton, E.M., 2021. Current and near-term advances in Earth observation and characterization of coastal tidal wetland change in the northeastern US using
for ecological applications. Ecol. Process. 10, 1–57. https://doi.org/10.1186/ Landsat time series. Remote Sens. Environ. 276, 113047 https://doi.org/10.1016/j.
s13717-020-00255-4. rse.2022.113047.
Verbesselt, J., Hyndman, R., Newnham, G., Culvenor, D., 2010. Detecting trend and Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021a. A near-real-time approach for monitoring
seasonal changes in satellite image time series. Remote Sens. Environ. 114, 106–115. forest disturbance using Landsat time series: Stochastic continuous change detection.
https://doi.org/10.1016/j.rse.2009.08.014. Remote Sens. Environ. 252, 112167 https://doi.org/10.1016/j.rse.2020.112167.
Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using Ye, S., Rogan, J., Zhu, Z., Hawbaker, T.J., Hart, S.J., Andrus, R.A., Meddens, A.J.H.,
satellite image time series. Remote Sens. Environ. 123, 98–108. https://doi.org/ Hicke, J.A., Eastman, J.R., Kulakowski, D., 2021b. Detecting subtle change from
10.1016/j.rse.2012.02.022. dense Landsat time series: Case studies of mountain pine beetle and spruce beetle
Verrelst, J., Camps-Valls, G., Mun˜oz-Marí, J., Rivera, J.P., Veroustraete, F., Clevers, J.G. disturbance. Remote Sens. Environ. 263, 112560 https://doi.org/10.1016/j.
P.W., Moreno, J., 2015. Optical remote sensing and the retrieval of terrestrial rse.2021.112560.
vegetation bio-geophysical properties–A review. ISPRS J. Photogramm. Remote Zhang, X., Friedl, M.A., Schaaf, C.B., 2009. Sensitivity of vegetation phenology detection
Sens. 108, 273–290. https://doi.org/10.1016/j.isprsjprs.2015.05.005. to the temporal resolution of satellite data. Int. J. Remote Sens. 30, 2061–2074.
Verstraete, M.M., Pinty, B., 1996. Designing optimal spectral indexes for remote sensing Zhang, X., Friedl, M.A., Schaaf, C.B., Strahler, A.H., Hodges, J.C.F., Gao, F., Reed, B.C.,
applications. IEEE Trans. Geosci. Remote Sens. 34, 1254–1265. Huete, A., 2003. Monitoring vegetation phenology using MODIS. Remote Sens.
Vogelmann, J.E., Gallant, A.L., Shi, H., Zhu, Z., 2016. Perspectives on monitoring gradual Environ. 84, 471–475.
change across the continuity of Landsat sensors using time-series data. Remote Sens. Zhang, X., Liu, L., Liu, Y., Jayavelu, S., Wang, J., Moon, M., Henebry, G.M., Friedl, M.A.,
Environ. 185, 258–270. Schaaf, C.B., 2018. Generation and evaluation of the VIIRS land surface phenology
Vogelmann, J.E., Xian, G., Homer, C., Tolk, B., 2012. Monitoring gradual ecosystem product. Remote Sens. Environ. 216, 212–229.
change using Landsat time series analyses: Case studies in selected forest and Zhang, X., Wang, J., Henebry, G.M., Gao, F., 2020. Development and evaluation of a new
rangeland ecosystems. Remote Sens. Environ. 122, 92–105. https://doi.org/ algorithm for detecting 30 m land surface phenology from VIIRS and HLS time series.
10.1016/j.rse.2011.06.027. ISPRS J. Photogramm. Remote Sens. 161, 37–51.
19

Z. Zhu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t282(2022)113266
Zhang, Y., Woodcock, C.E., Chen, S., Wang, J.A., Sulla-Menashe, D., Zuo, Z., Olofsson, P., 2016b. Greening of the Earth and its drivers. Nat. Clim. Chang. 6, 791–795. https://
Wang, Y., Friedl, M.A., 2022. Mapping causal agents of disturbance in boreal and doi.org/10.1038/nclimate3004.
arctic ecosystems of North America using time series of Landsat data. Remote Sens. Zhu, Z., Qiu, S., He, B., Deng, C., 2018. Cloud and cloud shadow detection for Landsat
Environ. 272, 112935 https://doi.org/10.1016/j.rse.2022.112935. images : the fundamental basis for analyzing Landsat time series. Remote Sens. Time
Zhao, F., Huang, C., Goward, S.N., Schleeweis, K., Rishmawi, K., Lindsey, M.A., Ser. Image Process. 3–24 https://doi.org/10.1201/9781315166636-10.
Denning, E., Keddell, L., Cohen, W.B., Yang, Z., Dungan, J.L., Michaelis, A., 2018. Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
Development of Landsat-based annual US forest disturbance history maps cover using all available Landsat data. Remote Sens. Environ. 144, 152–171. https://
(1986–2010) in support of the North American Carbon Program (NACP). Remote doi.org/10.1016/j.rse.2014.01.011.
Sens. Environ. 209, 312–326. https://doi.org/10.1016/j.rse.2018.02.035. Zhu, Z., Woodcock, C.E., 2012. Object-based cloud and cloud shadow detection in
Zhao, M., Zhou, Y., Li, Xuecao, Cao, W., He, C., Yu, B., Li, Xi, Elvidge, C.D., Cheng, W., Landsat imagery. Remote Sens. Environ. 118, 83–94. https://doi.org/10.1016/j.
Zhou, C., 2019. Applications of satellite remote sensing of nighttime light rse.2011.10.028.
observations: Advances, challenges, and perspectives. Remote Sens. 11, 1971. Zhu, Z., Woodcock, C.E., Olofsson, P., 2012a. Continuous monitoring of forest
Zhu, Z., 2017. Change detection using landsat time series: A review of frequencies, disturbance using all available Landsat imagery. Remote Sens. Environ. 122, 75–91.
preprocessing, algorithms, and applications. ISPRS J. Photogramm. Remote Sens. https://doi.org/10.1016/j.rse.2011.10.030.
130, 370–384. https://doi.org/10.1016/j.isprsjprs.2017.06.013. Zhu, Z., Woodcock, C.E., Rogan, J., Kellndorfer, J., 2012b. Assessment of spectral,
Zhu, Z., Fu, Y., Woodcock, C.E., Olofsson, P., Vogelmann, J.E., Holden, C., Wang, M., polarimetric, temporal, and spatial dimensions for urban and peri-urban land cover
Dai, S., Yu, Y., 2016a. Including land cover change in analysis of greenness trends classification using Landsat and SAR data. Remote Sens. Environ. 117, 72–82.
using all available Landsat 5, 7, and 8 images: A case study from Guangzhou, China https://doi.org/10.1016/j.rse.2011.07.020.
(2000–2014). Remote Sens. Environ. 185, 243–257. https://doi.org/10.1016/j. Zhu, Z., Wulder, M.A., Roy, D.P., Woodcock, C.E., Hansen, M.C., Radeloff, V.C.,
rse.2016.03.036. Healey, S.P., Schaaf, C., Hostert, P., Strobl, P., Pekel, J.F., Lymburner, L.,
Zhu, Z., Piao, S., Myneni, R.B., Huang, M., Zeng, Z., Canadell, J.G., Ciais, P., Sitch, S., Pahlevan, N., Scambos, T.A., 2019. Benefits of the free and open Landsat data policy.
Friedlingstein, P., Arneth, A., Cao, C., Cheng, L., Kato, E., Koven, C., Li, Y., Lian, X., Remote Sens. Environ. 224, 382–385. https://doi.org/10.1016/j.rse.2019.02.016.
Liu, Y., Liu, R., Mao, J., Pan, Y., Peng, S., Peuelas, J., Poulter, B., Pugh, T.A.M., Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.
Stocker, B.D., Viovy, N., Wang, X., Wang, Y., Xiao, Z., Yang, H., Zaehle, S., Zeng, N., Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. 238, 111116 https://doi.org/10.1016/j.rse.2019.03.009.
20