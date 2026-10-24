22300 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18, 2025
|     | Early |     | Detection      |     |     | of    | Forest     | Disturbances |     |      |     |     |     |     |
| --- | ----- | --- | -------------- | --- | --- | ----- | ---------- | ------------ | --- | ---- | --- | --- | --- | --- |
|     |       | in  | Homogeneous    |     |     |       | Stands     |              | –   | Deep |     |     |     |     |
|     |       |     | Learning-Based |     |     |       | Monitoring |              |     |      |     |     |     |     |
|     |       |     |                |     | of  | Picea | Abies      |              |     |      |     |     |     |     |
MaximilianKirsch ,JakobWernicke,PawanjeetSinghDatta,andChristinePreisach
Abstract—Climate change has increased the vulnerability of change. In Thuringia, Germany, for example, approximately
foreststoinsect-relateddamage,resultinginwidespreadforestloss 20%oftheforestareawasaffectedbyabarkbeetleinfestation
inCentralEuropeandhighlightingtheneedforeffective,continu-
|     |     |     |     |     |     |     | between | 2018 | and 2023, | eventually | resulting |     | in a timber | loss |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --------- | ---------- | --------- | --- | ----------- | ---- |
ousmonitoringsystems.Remotesensing-basedapproaches,often
|     |     |     |     |     |     |     | of 28 million | m3  | in the | region | [1]. The | primary | impact | was |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------ | -------- | ------- | ------ | --- |
relyonsupervisedmachinelearning(ML)algorithmsthatrequire
labeledtrainingdata.Monitoringtemporalpatternsthroughtime observedinpurestandsofNorwayspruce(Piceaabies),which
seriesanalysisoffersapotentialalternativeforearlierdetectionof were predominantly affected by the two most common bark
disturbancesbutrequiressubstantialstorageresources.Thisstudy beetle species in Germany: Ips typographus and Pityogenes
investigatesthepotentialofaDeepLearningalgorithmbasedona
chalcographus.Thislevelofforestdisturbanceisunprecedented
LongShortTermMemory(LSTM)Autoencoderforthedetection
|     |     |     |     |     |     |     | not only | in Central | Germany, |     | but also | across | many | spruce- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | --- | -------- | ------ | ---- | ------- |
ofanomaliesinforesthealth(e.g.,barkbeetleoutbreaks),utilizing
Sentinel-2 time series data. This approach is an alternative to dominated forest regions throughout Central Europe. Climate
supervisedMLmethods,avoidingthenecessityforlabeledtraining changeinducesstressorsthatnegativelyimpacttheoverallhealth
data. Furthermore, it is more memory-efficient than other time and growth of forests [2], [3]. Particularly, hot summers and
seriesanalysisapproaches,asarobustmodelcanbecreatedusing
associateddroughtsimpairtheefficacyofdefensemechanisms
onlya26-week-longtimeseriesasinput.Inthisstudy,wemonitored
|     |     |     |     |     |     |     | of spruce | trees | [4]. Secondary |     | pests | like thermophilic |     | bark |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------------- | --- | ----- | ----------------- | --- | ---- |
purestandsofspruceinThuringia,Germany,overa7-yearperiod
|     |     |     |     |     |     |     | beetle populations |     | thrive | under | such | circumstances, |     | as their |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ----- | ---- | -------------- | --- | -------- |
from2018totheendof2024.Ourbestmodelachievedadetection
accuracy of 87% on test data and was able to detect 65% of all reproduction depends on predisposed and already weakened
| anomaliesataveryearlystage(morethanamonthbeforevisible |     |     |     |     |     |     | trees[5],[6]. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
signsofforestdisturbance).Comparedtotheestablishedtimeseries
|     |     |     |     |     |     |     | Predicting | disturbances |     | is  | challenging | due | to the | unpre- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --- | ----------- | --- | ------ | ------ |
breakdetectionalgorithm–breaksforadditiveseasonandtrend
|     |     |     |     |     |     |     | dictable | nature | of insect-induced |     | calamities | [7]. | An early | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------------- | --- | ---------- | ---- | -------- | --- |
andisolationforestanomalydetection,ourapproachconsistently
|     |     |     |     |     |     |     | spatially | precise | detection | of  | potential | bark beetle | infestation |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | --- | --------- | ----------- | ----------- | --- |
detectedahigherpercentageofanomaliesatanearlierstage.These
findingssuggestthatLSTM-basedAutoencoderscouldprovidea centers are needed to mitigate an epidemic bark beetle re-
promising,resource-efficientapproachtoforesthealthmonitoring, production [8], [9]. Accordingly, several studies stressed the
enablingmoretimelyresponsestoemergingthreats.
|     |     |     |     |     |     |     | hypothesis | of green | attack | detection | based | on  | remote | sensing |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | --------- | ----- | --- | ------ | ------- |
Index Terms—Anomaly detection, autoencoder, bark beetle, data [10], [11], [12]. However, there is wide consensus that
forest,longshorttermmemory(LSTM),remotesensing,spruce. greenattackdetectioniseitherunreliableorinfeasibleonlarge
spatialscales[9],[13],[14].Instead,ourfocusisonidentifying
I. INTRODUCTION anomalous patterns in forest health that may serve as early
FORESTS in Central Europe are increasingly threatened warning indicators of potential disturbances. A limitation of
earlydisturbancedetectionisoftenthelackoflabeledtraining
| by intensified |     | insect outbreaks, |     | largely | driven | by climate |                 |         |              |        |          |       |         |         |
| -------------- | --- | ----------------- | --- | ------- | ------ | ---------- | --------------- | ------- | ------------ | ------ | -------- | ----- | ------- | ------- |
|                |     |                   |     |         |        |            | data. Satellite | image   | time         | series | (SITS)   | based | anomaly | detec-  |
|                |     |                   |     |         |        |            | tion can        | operate | unsupervised |        | and does | not   | rely on | labeled |
Received28February2025;revised25July2025;accepted18August2025.
trainingsamplestocaptureseasonalvariations[15],[16].Often
| Date of publication | 26  | August 2025; | date | of current | version 15 | September |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------ | ---- | ---------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2025.ThisworkwassupportedinpartbytheAgencyforRenewableResources SITS approaches, such as the Breaks for Additive Season and
(FachagenturNachwachsendeRohstoffee.V.,FNR)onbehalfoftheFederal
|     |     |     |     |     |     |     | Trend (BFAST) |     | algorithm, | learn | temporal | patterns, | and | detect |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ----- | -------- | --------- | --- | ------ |
MinistryofFoodandAgriculture(BMEL)andinpartbytheFederalMinistryfor
deviationsfromthenormalstate[17].Otherapproachesutilize
theEnvironment,NatureConservation,NuclearSafetyandConsumerProtection
(BMUV).(Correspondingauthor:MaximilianKirsch.)
|            |                     |     |          |          |                 |        | deep learning | such | as  | LSTM | neural networks |     | that remember |     |
| ---------- | ------------------- | --- | -------- | -------- | --------------- | ------ | ------------- | ---- | --- | ---- | --------------- | --- | ------------- | --- |
| Maximilian | Kirsch andChristine |     | Preisach | are with | the Intelligent | System |               |      |     |      |                 |     |               |     |
temporalpatternsintimeseries[18].Mostapproachesdependon
| Research Group, | University | of Applied | Science, | 76187 | Karlsruhe, | Germany |     |     |     |     |     |     |     |     |
| --------------- | ---------- | ---------- | -------- | ----- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
extensivehistoricalinformationforeveryobservedtimeseries
(e-mail:maximilian.kirsch@h-ka.de).
JakobWernickeandPawanjeetSinghDattaarewiththeThüringenForstAöR, andoftenmonitorunivariatetimeseries,creatinghyperspectral
| Forstliches | Forschungs-und | Kompetenzzentrum |     | (FFK) | Gotha, 99867 | Gotha, |     |     |     |     |     |     |     |     |
| ----------- | -------------- | ---------------- | --- | ----- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
relationshipsonlybycalculatingvegetationindices(VIs)[15],
Germany.
| DigitalObjectIdentifier10.1109/JSTARS.2025.3603094 |     |     |     |     |     |     | [16],[18]. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
©2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,see
https://creativecommons.org/licenses/by/4.0/

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22301
We investigated the potential of a deep learning, A. RemoteSensing-BasedBarkBeetleDetection
| reconstruction-based |     | time | series | anomaly |     | detection | approach |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---- | ------ | ------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Classifyinggreenattackusingsingleremotesensingimagesis
tocreateanearlywarningsystembasedonSentinel-2satellite
consideredinfeasiblewithmedium-resolutionsatellitedata[14].
| images. | We built | a LSTM-AE |     | model | for | real-time | anomaly |     |     |     |     |     |     |     |     |
| ------- | -------- | --------- | --- | ----- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Somestudieshaveexploredmachinelearning(ML)approaches
| detection | with | a 10-m | spatial | resolution. |     | We applied | our | ap- |                |       |        |      |         |             |          |
| --------- | ---- | ------ | ------- | ----------- | --- | ---------- | --- | --- | -------------- | ----- | ------ | ---- | ------- | ----------- | -------- |
|           |      |        |         |             |     |            |     |     | to distinguish | green | attack | from | healthy | vegetation. | Abdullah |
proachtodatacollectedfromseverelythreatenedsprucestands
|               |          |     |         |     |          |     |        |       | et al. [10] | analyzed | Sentinel-2 | spectral | bands | and | VIs, using |
| ------------- | -------- | --- | ------- | --- | -------- | --- | ------ | ----- | ----------- | -------- | ---------- | -------- | ----- | --- | ---------- |
| in Thuringia, | Germany, |     | between |     | 2018 and | the | end of | 2024. |             |          |            |          |       |     |            |
statisticalMLforvariableselection.However,theresultswere
Throughobservationandmeasurementofthehealthdynamicsof
deemedunsuitableforforestryapplicationsbytheauthors[10].
thestands,weaimtoflaganomaliesinearlydisturbancestages
Otherstudiesfocusedonchangesinforeststresslevelsusingran-
wall-to-wall.Ouralgorithmemploysunsuperviseddeeplearn-
domforestclassification,todistinguishbarkbeetleinfestedtrees
| ing and | is independent |     | from | labeled | training | data. | This | makes |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ---- | ------- | -------- | ----- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
fromhealthyvegetation[19].ThesesupervisedMLapproaches
| our method | accessible |     | for | a wide | range | of users, | especially |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | ------ | ----- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
relyonlabeledtrainingdata.Thedifficultyofcreatingreliable
pairedwithfreelyavailableSentinel-2data.Inaddition,unlike
labelsfromsatellitedata,makessupervisedMLimpractical.
| many SITS | approaches, |       | this  | technique | minimizes    |           | the need | for |     |     |     |     |     |     |     |
| --------- | ----------- | ----- | ----- | --------- | ------------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| extensive | historical  | data, | which | is        | particularly | important |          | for |     |     |     |     |     |     |     |
B. SITSAnalysis
singlecell-basedanalysesinordertoreducememorydemands.
Theimplementationofthisearlywarningsystemissuitablefor
|     |     |     |     |     |     |     |     |     | SITS | analysis | is widely | used to | detect | forest disturbances, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --------- | ------- | ------ | -------------------- | --- |
an operational forest disturbance monitoring and thus might includingbarkbeetleoutbreaks[11],[20],[21].Akeyadvantage
supportforesthealthmanagementstrategies.
ofSITSisitsabilitytoretrospectivelyanalyzepatternsleading
Ourmaincontributionsareasfollows.
todisturbances,suchasredattack.SITShasbeenappliedtoclas-
1) We propose a robust unsupervised approach for SITS sifybarkbeetleinfestationsusingMLtechniques.Forinstance,
anomalydetectioninforesthealthdynamicsthatishighly
Bartaetal.[11]usedarandomforestmodelonSITStopinpoint
accurateindetectinganomaliesuptoseveralmonthsear- early separability between healthy and infested trees across
lierthanstaticmethodsbasedonVIthresholds,bylever-
|     |     |     |     |     |     |     |     |     | various | indices. | They identified | Sentinel-2 |     | spectral | bands and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------------- | ---------- | --- | -------- | --------- |
agingthetemporalrelationshipbetweenthemultispectral
VIsthatbestdifferentiatehealthyfrominfestedtrees.Abdullah
channelsonasinglecellbasis. et al. [20] explored the relationship between bark beetle and
| 2) Weintroduce |     | anapproach |     | foronlineanomaly |     |     | detection, |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
canopychlorophyllcontentderivedfromSPOT-5andRapidEye
leveraging freely available Sentinel-2 satellite data. In SITSdataincombinationwithgroundtruthdata.
contrast to conventional SITS methods, that require ex- Anomaly detection methods are also prevalent in SITS re-
| tended | historical |     | time | series, | our method |     | processes | in- |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ---- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
search.Anapproach,introducedbyDutrieuxetal.[22]proposed
comingdatainrealtime,mitigatingtheneedforsubstan- a model, that detects time series harmonics and forecasts the
tialtemporalarchiveswhilemaintainingrobustdetection
patternandiftheactualtimeseriesdeviatesstronglyfromthat
performance. pattern,ananomalyisflagged.Thewellknownbreakdetection
3) We analyzed the importance of temporal information by modelBFAST,detectschangesbydecomposingtimeseriesinto
| testing | LSTM-AE |     | models | that | observe | diverse | window |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | ------ | ---- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
trend,seasonal,andresidualcomponents[17].Thisapproachis
sizes from one month to one year. Thereby balancing commonly utilized to detect structural changes in vegetation
| model | performance |     | and | historical | data | requirements |     | to  |             |       |       |              |     |            |          |
| ----- | ----------- | --- | --- | ---------- | ---- | ------------ | --- | --- | ----------- | ----- | ----- | ------------ | --- | ---------- | -------- |
|       |             |     |     |            |      |              |     |     | time series | [16], | [23]. | Furthermore, | the | sequential | analysis |
reducestoragedemands.
|     |     |     |     |     |     |     |     |     | method | CUSUM | has been | employed | to identify |     | deviations in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | -------- | ----------- | --- | ------------- |
4) We compared the LSTM models against a SITS method attackedtreesfromstandardSITSpatterns[21],[24].Another
| for | break | detection | in  | time series | called | BFAST | and | the |     |     |     |     |     |     |     |
| --- | ----- | --------- | --- | ----------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
unsupervisedanomalydetectionmethodistheIsolationForest
anomaly detection algorithm isolation forest (IF). Our (IF)algorithm.IFisfrequentlyappliedintimeseriesanomaly
modelachievedahigherlevelofaccuracy,aswellasasig-
|     |     |     |     |     |     |     |     |     | detection | [25] and | has | also been | successfully | used | in SITS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --------- | ------------ | ---- | ------- |
nificantincreaseinthenumberofcorrectearlypredictions.
applications[26].
| 5) Ultimately, |     | we propose |     | a scoring | method | that | allows | us  |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | --------- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tocomparediversemodels’anomalydetectionandearly
C. DeepLearningApproaches
| warning |     | potential | exceeding |     | the generally |     | used | perfor- |     |     |     |     |     |     |     |
| ------- | --- | --------- | --------- | --- | ------------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
mancemetrics,byrewardingearlierdetections. Deep learning has gained traction in SITS for forest health
|     |     |     |             |     |     |     |     |     | classification | and                                      | disturbance | detection | [18], | [27], | [28], [29]. |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | -------------- | ---------------------------------------- | ----------- | --------- | ----- | ----- | ----------- |
|     |     |     |             |     |     |     |     |     | Zhouetal.      | [28]proposedanunsupervisedAEmodelthatde- |             |           |       |       |             |
|     |     | II. | RELATEDWORK |     |     |     |     |     |                |                                          |             |           |       |       |             |
tectsanomaliesinunivariateLandsattimeseriesbyidentifying
Earlydetectionofbarkbeetleoutbreaksisacriticalresearch reconstructionerrors.RecurrentNeuralNetworks(RNNs),par-
areaduetotheirsignificantimpactonforestecosystems.Detect- ticularlyusingLSTMarchitectures,excelatcapturingtemporal
inginfestedtreesduringthe“greenattack”stage–whenbeetles dynamics in vegetation phenology and outperform traditional
have infested a tree but crown symptoms are not yet visible – methods in land cover classification [30], [31]. LSTM models
isparticularlychallenging,eveninsitu.Thisstageprecedesthe have been applied to change detection on Sentinel-1 data [32]
“redattack,”wherecanopydiscolorationbecomesdetectablein and burned area mapping using MODIS data [18], [27]. Kong
aerialimagery[14]. etal. [18]introducedaLSTM-basedframeworkthatforecasts

22302 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
time series and flags disturbances when predictions deviate duetoextensivebarkbeetleoutbreaks,followingtheprolonged
| significantlyfromobservations. |     |     |     |     |     |     |     | droughtsince2018.[1]. |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
Furthermore, recent advances in disturbance detection from We used available open forest mapping data provided from
SITSincludetheworkbySchilleretal. [29],whointroduceda ThüringenForest1toselectconiferpurestands.Sincenodetailed
transformer-basedmodelforclassifyingtimeseriesasdisturbed treespeciesdatawereavailableweadditionallyusedtrue-color,
orundisturbed.Theirapproachdemonstratedtheabilitytodetect orthorectifiedaerialimagery(orthophotoswithaspatialresolu-
evensubpixel-levelanomalies.However,themodelrequiredex- tionof0.2m),providedbytheStateofThuringiaandrecorded
tensiveamountsoflabeledtrainingdata(theirmodelwastrained onJune4,2023.2 Theseimageswereusedtovisuallyidentify
on1.5millionpixeltimeseries)andoperatedonlongtemporal andselectareascorrespondingtopuresprucestandsexhibiting
inputs,relyingonfour-yearsoftimeseriesforeachobservation. varyingdegreesofforesthealth.
High-qualitylabeleddataareoftenlimitedinforestdisturbance We selected four training areas, as well as a larger area for
detection,andtheuseoflongtimeseriesconsiderablyincreases testing in the Thuringia Forest region. In addition, eight test
storageandcomputationaldemands. areaswerechosenfromtheSüdharzNaturePark,locatedinthe
In parallel, LSTM-AE have been widely used for unsuper- northernpartofThuringia(seeFig.1).Themodelwastrained
vised anomaly detection across domains, such as renewable usingtimeseriesofhealthysprucestands.Forthis,weselected
energy monitoring, medical signal processing, cybersecurity, visually healthy forest patches with green crowns as training
andenvironmentalsystems[33],[34],[35],[36].Thesemodels areas,coveringatotalof28.85ha.Thehealthstatusoftheseareas
effectivelycapturecomplextemporaldependencies,particularly throughouttheobservationperiodwasconfirmedbyanalyzing
inmultivariatesettings.However,tothebestofourknowledge, thetimeseriesofVIs(NDVI,DWSI).Theselectedtrainingareas
LSTM-AEhavenotbeenexploredextensivelyinthecontextof areshowninFig.2.
forestmonitoringsystems. The areas designated for testing depict varying degrees of
OurstudyexplorestheuseofmultivariateLSTM-AEmodels disturbance(e.g.,healthyforest,crowndiscolorationsandclear-
onSentinel-2timeseriesfordetectingforesthealthdisturbances cuts).Thepolygonalareasvariedinsizefrom25to561pixels
insprucestands.Unlikemanyexistingapproachesthatrelyon totaling3175pixels(31ha).Furthermore,weselectedalarger
univariateinputs,longhistoricalrecords,orextensivelabeling, test region in which various stages of disturbance were repre-
ourmethodleveragesmultispectralandtemporalpatternsover sentedinacontiguousareaof44519pixels(445ha).Weused
shorter input windows (e.g., 26 to 52 weeks) to identify early thisregiontocreateananomalymap.
signsofdisturbance.Byevaluatingdifferentinputlengthsand
usingareconstruction-basedunsupervisedframework,weaim B. Sentinel-2TimeSeries
| to minimize | false | positives | while | reducing |     | data volume | and |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | ----- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
TheSentinel-2datawereselectedfortheirhighspatialreso-
computationaldemands.Thisworkaddressesakeygapincur-
|     |     |     |     |     |     |     |     | lution, frequent | revisit | time, | and free | availability. |     | These data |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ----- | -------- | ------------- | --- | ---------- |
rentSITS-basedforestmonitoringbyenablingearly,label-free
|     |     |     |     |     |     |     |     | capture high-resolution |     | images | of  | the Earth’s | surface | with a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ------ | --- | ----------- | ------- | ------ |
disturbancedetectionfromshortermultivariatesequences.
combinedrevisitintervaloffivedays[37].
WeselectedatmosphericallycorrectedSentinel-2Level2A
III. STUDYAREAANDDATA (L2A) data, which also include a scene classification (SCL)
Inthischapter,wedescribeourstudyareas,thelargerstudy map [38]. The SCL algorithm characterizes every pixel in a
area,theThuringianForestandtheSüdharzNaturePark,which Sentinel-2 image into one of 12 classes [39]. These classes
aretheselectedareasfortrainingandtesting,andtheSentinel-2 describe cloud types, snow, vegetation, or nonegetated areas,
timeseriesdatabasis. which we utilized to filter instances where an observed pixel
wascoveredbycloudorsnowatagiventimestep.
A. StudyArea TheSentinel-2L2Adataisrepresentedbymultivariatetime
|          |             |     |               |     |            |     |           | series for each  | pixel, | covering | 12 spectral |           | bands from | January   |
| -------- | ----------- | --- | ------------- | --- | ---------- | --- | --------- | ---------------- | ------ | -------- | ----------- | --------- | ---------- | --------- |
| In order | to evaluate |     | the potential |     | of LSTM-AE |     | for early |                  |        |          |             |           |            |           |
|          |             |     |               |     |            |     |           | 2018 to December |        | 2023.    | These were  | organized | into       | spatially |
disturbancedetection,weobservedNorwayspruce(Piceaabies)
andtemporallyindexedtables.
| stands in      | the Thuringian |          | Forest   | and             | the southern | part      | of the |     |                                 |     |     |     |     |     |
| -------------- | -------------- | -------- | -------- | --------------- | ------------ | --------- | ------ | --- | ------------------------------- | --- | --- | --- | --- | --- |
| Harz Mountains |                | (central | Germany) | retrospectively |              | during    | the    |     |                                 |     |     |     |     |     |
|                |                |          |          |                 |              |           |        | IV. | BACKGROUND:LSTMAUTOENCODERMODEL |     |     |     |     |     |
| period from    | January        | 2018     | to       | December        | 2024.        | Thuringia | is     | a   |                                 |     |     |     |     |     |
suitable study area for the detection of disturbances due to its Inthissection,weprovideacomprehensiveoverviewofthe
|           |             |         |     |        |             |       |       | model components |     | and the | model | architecture | of the | unsuper- |
| --------- | ----------- | ------- | --- | ------ | ----------- | ----- | ----- | ---------------- | --- | ------- | ----- | ------------ | ------ | -------- |
| extensive | bark-beetle | induced |     | forest | degradation | since | 2018. |                  |     |         |       |              |        |          |
ThepredominatelymanagedforestsofThuringiaarecomposed vised Deep Learning algorithm we used for early detection of
bark-beetleoutbreaks.First,thegeneralfunctionalityofAutoen-
| of three | main tree | species: | Norway |     | spruce, | European | beech |     |     |     |     |     |     |     |
| -------- | --------- | -------- | ------ | --- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
(Fagus sylvatica),andScots pine(Pinus sylvestris),which are coder(AE)’sissetout,followedbytheoperatingprinciplesof
partlyintermixedwithsecondarytreespecies.Before2018,the
| region was | covered | primarily |     | by single-layered |     | spruce | stands | 1Mapping |     |     |     |     |     |     |
| ---------- | ------- | --------- | --- | ----------------- | --- | ------ | ------ | -------- | --- | --- | --- | --- | --- | --- |
data: https://geomis.geoportal-th.de/geonetwork/srv/ger/catalog.
of a uniform age, reflecting the typical forest structure of the search#/metadata/c70f0858-af9b-4395-9a0d-1b577e6d09e6.Lastaccessedon
30August2024.
time.Thepersistentdroughtsince2018initiatedthemostsevere
|                    |     |        |         |               |     |               |     | 2Orthophotos:                                 | https://geoportal.thueringen.de/gdi-th/download-offene- |     |     |      |           |           |
| ------------------ | --- | ------ | ------- | ------------- | --- | ------------- | --- | --------------------------------------------- | ------------------------------------------------------- | --- | --- | ---- | --------- | --------- |
| forest degradation |     | in the | region. | Consequently, |     | approximately |     |                                               |                                                         |     |     |      |           |           |
|                    |     |        |         |               |     |               |     | geodaten/download-luftbilder-und-orthophotos. |                                                         |     |     | Last | accessed: | 30 August |
110000haofprimarilyspruce-dominatedstandswereclear-cut
2024

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22303
Fig.1. LocationsofthestudyareainThuringia,Germany.
Fig.3. Autoencoder:Reconstructionofatimeseries.
|     |     |     |     | ThedecoderD | convertsthelatentspacerepresentationz |     |     |     |
| --- | --- | --- | --- | ----------- | ------------------------------------- | --- | --- | --- |
back
totheoriginalshape,producingthereconstructeddataxˆ[40]
|     |     |     |     |               |          | xˆ=D(z).        |                   | (2) |
| --- | --- | --- | --- | ------------- | -------- | --------------- | ----------------- | --- |
|     |     |     |     | The structure | of an AE | and the process | of reconstruction | is  |
illustratedinFig.3.
Duringtraining,theAEoptimizesparameters,suchasweights
|     |     |     |     | and biases, | to minimize | the reconstruction | error | between the |
| --- | --- | --- | --- | ----------- | ----------- | ------------------ | ----- | ----------- |
Fig.2. Areasselectedtouseastrainingdata.Theimagesshowrecordings x xˆ
fromJune4,2023. input and the reconstruction [41]. In anomaly detection,
AE’saretrainedexclusivelyon“normal”datasamples,without
LSTM.Inconclusion,weoutlinethegeneralfunctionalityand anomaliesandlearntocapturethekeyfeatures[42],[43].The
|     |     |     |     | difference | between input | data x and | reconstructed | data xˆ is |
| --- | --- | --- | --- | ---------- | ------------- | ---------- | ------------- | ---------- |
structureoftheLSTMAEmodel.
knownasthereconstructionerror[41].Sinceanomaliesexhibita
typicalcharacteristics,theycannotbeaccuratelyreconstructed,
A. Autoencoder
leadingtohighreconstructionerrors[44].Anomaliesareiden-
| We built | an AE for anomaly | detection. | An AE is a neural |     |     |     |     |     |
| -------- | ----------------- | ---------- | ----------------- | --- | --- | --- | --- | --- |
tifiedwhenthereconstructionerrorexceedsathresholdchosen
networkdesignedtoreconstructinputdatausingtwofunctions:
basedonthedistributionofreconstructionerrors[44].
anencoderandadecoder[35].TheencoderE
learnsthemost
| importantfeatures | oftheinputdata | xand | reduces themintoa |     |     |     |     |     |
| ----------------- | -------------- | ---- | ----------------- | --- | --- | --- | --- | --- |
B. LSTM
lower-dimensionalrepresentationcalledthelatentspacez[40]
|     |     |        |     | We incorporated | LSTM | into our AE | model, | making it an |
| --- | --- | ------ | --- | --------------- | ---- | ----------- | ------ | ------------ |
|     | z   | =E(x). | (1) |                 |      |             |        |              |
effectivemethodforreconstruction-basedanomalydetectionin

22304 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
Thesigmoidactivationfunctioniscalculatedasfollows:
1
|     |     |     |     |     |     |     |     |     |     | σ(x)= |       | .   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |       | 1+e−x |     | (9) |
Thetanhactivationfunctioniscalculatedasfollows:
ex−e−x
|     |     |     |     |     |     |     |     |     | tanh(x)= |     |     | .   | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ---- |
ex+e−x
|     |     |     |     |     |     |     | The operational |     | mechanics |     | of this | LSTM unit, | as detailed |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ------- | ---------- | ----------- |
by[48],areasfollows:
Theequations3–5calculatethegatedunits.Eachgatedunit
x
|     |     |     |     |     |     |     | vector multiplies |         | the input | at             | the current | time step  | t with the   |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | --------- | -------------- | ----------- | ---------- | ------------ |
|     |     |     |     |     |     |     | respective        | weights | w         | and multiplies |             | the Hidden | State of the |
Fig.4. ComponentsofaLSTM-Unit.
|     |     |     |     |     |     |     | previoustimesteph |     |     | withtherespectiverecurrentweightu. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ---------------------------------- | --- | --- | --- |
t−1
Thevectorsarethensummedbeforeabiasisadded.Theresults
time series [35]. LSTM is a type of RNN, that is designed to arethenpassedthroughasigmoidactivationfunction,producing
efficientlyprocesssequentialdatae.g.,timeseries.Thisensures
avaluebetween0and1.Thegatedunitsdifferonlyintermsof
thattemporalrelationshipsarepreservedduringprocessing[35]. theirrespectiveweightsandbiases,allowingtheLSTMcellto
| TheLSTMarchitectureincludes |     |     | acomponent |     | formaintaining |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
forgetirrelevantinformationofasequence[41],[45].
long-termdependenciesandanotherforpropagatingshort-term Equation(6),thecellcandidategatedefinesthepotentialnew
CellStateC˜
memories [45]. At each time step, new information is added, t.Likewisetotheequationofthegatedunits,x tand
updating the memory of the cell [45]. The LSTM unit archi- h t−1aremultipliedwiththerespectiveweightsw Candu
C.The
tecture that we applied is an adaptation of the original LSTM products are summed and a bias b is then added. The result
C
model from [46] and incorporates a mechanism known as the servesasinputforatanhactivationfunctionthatregulatesthe
forgetgate.ThisadvancedLSTMcell,proposedby[47],addsa informationflowinthenetwork.
weightedfunctionthatdetermineswhichinformationfromthe To determine the new Cell State C t, (7) takes the previous
| inputshouldbediscarded.TheLSTMarchitectureisillustrated |     |     |     |     |     |     | CellStateC |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
t−1andmultipliesitbytheoutputoftheforgetgate.
inFig.4. Sincef tisavaluebetween0and1,itdictatestheproportionof
Fig.4depictsthecomponentswithinabasicLSTMcell,as C t−1thatisretained.Subsequently,thepotentialnewCellState
C˜ tispoint-wisemultipliedbyi
wellasthestructuralflowofthedata.TheCellState,denoted ttodeterminetheproportionof
C˜
C, represents the long-term memory, while the Hidden State, tthatisadded.
denotedh,storesinformationabouttheshort-termmemory.The Equation(8)definesthenewHiddenStateh
t.Itiscalculated
inputdatax
tdescribesthevaluesforthemultivariatetimeseries by using the new Cell State C t as input for a Tanh Function
at the current time step. Furthermore, the LSTM unit contains resultinginapotentialnewHiddenState.Thisisthenpoint-wise
socalledgatedunits,thesearetheforgetgatef t,inputgatei multipliedbytheoutputgateo
|                     |     |                  |     |                     |     | t,  |     |     |     |     | t todeterminetheproportionof |     |     |
| ------------------- | --- | ---------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
| cellcandidategateC˜ |     | t,andoutputgateo |     | t.Theweightsw,u,and |     |     |     |     |     |     |                              |     |     |
potentialHiddenStatethatispassedontothenexttimestep.
thebiasbarelearnedontheinputdataandthehiddenstate,and
anactivationfunctionσortanhisapplied.σisdisplayedwith
C. LSTM-AEArchitecture
ablueframeandtanhred.
|           |     |          |               |     |                |        | We incorporate |     | stacked | LSTM | neurons | into an | AE network |
| --------- | --- | -------- | ------------- | --- | -------------- | ------ | -------------- | --- | ------- | ---- | ------- | ------- | ---------- |
| Each LSTM |     | unit has | three inputs: | 1)  | The input data | of the |                |     |         |      |         |         |            |
currenttimestepx (seeFig.5).LSTMunitsdetectlong-andshort-termdependen-
t,2)theCellStateoftheprevioustimestep
|            |        |        |          |              |           |        | cies, as | well as | relationships |     | between | input features, | making |
| ---------- | ------ | ------ | -------- | ------------ | --------- | ------ | -------- | ------- | ------------- | --- | ------- | --------------- | ------ |
| C t−1, and | 3) the | Hidden | State of | the previous | time step | h t−1. |          |         |               |     |         |                 |        |
C them highly effective for multivariate time series anomaly de-
| Furthermore, | it  | creates | a new Cell | State | t and a new | Hidden |     |     |     |     |     |     |     |
| ------------ | --- | ------- | ---------- | ----- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
tection[35],[40].
Stateh tasoutputs.
|     |     |     |     |     |     |     | We applied |     | a LSTM-AE |     | architecture | based on | the method |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | ------------ | -------- | ---------- |
Thegatedunits,aswellastheinformationforwardpassofan
|     |     |     |     |     |     |     | proposed | by [35]. | They | built | an LSTM | AE to detect | DDoS |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ----- | ------- | ------------ | ---- |
LSTMunit,aredefinedbythefollowingequations:
attacks3inmultivariatetimeseriesdata.
f =σ(w x +u h +b ) Beforeapplyingthemodeltoatimeseries,thedataaredivided
|     | t   |     | f t f | t−1 | f   | (3) |                |     |                 |     |        |          |              |
| --- | --- | --- | ----- | --- | --- | --- | -------------- | --- | --------------- | --- | ------ | -------- | ------------ |
|     |     |     |       |     |     |     | into sequences |     | of a predefined |     | window | size, as | explained in |
i =σ(w x +u h +b ) (4) Section V-A. Within each sequence, the relationships between
|     | t   |     | i t i t−1 |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
o =σ(w x +u h +b ) features and time steps are computed using hidden LSTM
|     | t   |     | o t o | t−1 | o   | (5) |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
units[35].
C˜ = tanh(w x +u h +b ) Multiple LSTM units are stacked in each layer of the AE.
|     | t   |             | C˜ t | C˜ t−1    | C˜  | (6) |              |           |             |              |         |                    |                  |
| --- | --- | ----------- | ---- | --------- | --- | --- | ------------ | --------- | ----------- | ------------ | ------- | ------------------ | ---------------- |
|     |     |             |      |           |     |     |              |           |             |              |         | C                  | t                |
|     |     |             |      |           |     |     | W it h in ea | c h u n i | t , th e lo | n g - t e rm | m e m o | ry t ,i ( w h e re | re p re se n t s |
|     | C   | =f (cid:2)C | +i   | (cid:2)C˜ |     |     |              |           |             |              |         |                    |                  |
t t t−1 t t (7) tim e a nd i d e n o t e s th e u n it i n d ex )a n d th e sh o r t- te r m m e m o ry h
t , i
|     | h   | =o (cid:2)tanh(C | )   |     |     | (8) |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | t   | t                | t   |     |     |     |     |     |     |     |     |     |     |
3DDoSstandsforDistributedDenialofService.DDoSattacksarecyberat-
where(cid:2)denotesthepoint-wisemultiplicationoftwovectors.
tacksaimedatoverwhelmingaserverbysendingenormousamountsofdata[35].

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22305
|     |     |     |     |     |     | A. DataPreparation |     |            |        |     |      |         |          |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | ------ | --- | ---- | ------- | -------- |
|     |     |     |     |     |     | As mentioned       |     | in Section | III-B, | the | data | for all | observed |
sitesarecontainedinspatialandtemporalindexeddataframes.
Duringpreprocessing,themultivariatetimeseriesforeachpixel
wastreatedindividually.
|     |     |     |     |     |     | The time   | series  | contain      | a signal | for           | every     | fifth     | day. Due |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------ | -------- | ------------- | --------- | --------- | -------- |
|     |     |     |     |     |     | to cloud   | or snow | coverage,    | many     | data          | instances | are       | deemed   |
|     |     |     |     |     |     | unsuitable | and     | are excluded | from     | the analysis. |           | To filter | these    |
instances,weusedtheSCLlayerfromtheL2Aimagestoretain
|     |     |     |     |     |     | only pixels | classified | as  | either | vegetated | or nonvegetated. |     | As  |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------ | --------- | ---------------- | --- | --- |
shownin(11)wedecomposedthetimeseriesintotrend,seasonal
componentandremainderandappliedTukey’smethod[50]to
theremainderR
ttoremoveremainingoutliers
|     |     |     |     |     |     |            |         | x               | =T +S         | +R         |           |        |       |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | --------------- | ------------- | ---------- | --------- | ------ | ----- |
|     |     |     |     |     |     |            |         | t               | t             | t          | t         |        | (11)  |
|     |     |     |     |     |     | where T    | denotes | trend,          | S t, seasonal | component, |           | and    | R the |
|     |     |     |     |     |     |            | t       |                 |               |            |           |        | t     |
|     |     |     |     |     |     | remainder. | We      | then aggregated |               | the data   | to weekly | values | and   |
Fig.5. ConceptualillustrationofanLSTM-AEarchitecture.
imputedthegapstoobtainhomogeneoustimeseries.First,we
smoothedthetimeseriesusingtheSavitzky–Golayfilter(SGF)
arecontinuouslyupdatedwitheveryadditionaltimestep[41]. and then filled the gaps with exponentially weighted moving
TheoutputsC t,i andh t,i fromeachunitarethenpassedtoall average (EWMA). The SGF smooths and differentiates data
unitsinthesubsequentAElayer.Sincethesecondlayercontains
|     |     |     |     |     |     | by performing |     | a local | least squares | polynomial |     | fit | within a |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------------- | ---------- | --- | --- | -------- |
fewerLSTMunits,theinformationisprogressivelycompressed, slidingwindow.Itdetectstheunderlyingtrendofthedatawhile
reducing the dimensionality while retaining the most relevant reducingnoise.ApplyingSGFtoenhancethequalityofsatellite
features. image-basedtimeseriesbysmoothingoutfluctuationsandnoise
ThefinalLSTMlayerintheencodingphaseproduceshighly has been widely referenced [51], [52], [53], [54]. A window
compressedrepresentationsofthemultivariateinputdata[41],
|     |     |     |     |     |     | size is selected, |     | determining | the | number | of observations |     | used |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --- | ------ | --------------- | --- | ---- |
Z.
forming the latent space, which is denoted as Before the in the smoothing process. If the window consists of 2S+1
dataispassedtothedecodernetwork,aRepeatVectorlayeris points, the consecutive observations within the window are
| appliedtoreshapeZ |     |     |     |     |     | x ,x | ,...,x | ,...,x |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ---- | ------ | ------ | --- | --- | --- | --- | --- |
tomatchthelengthoftheinputsequence. i−S i−S+1 i i+S.Tomodelthetrendwithineach
These repeated vectors then serve as inputs for the decoder window, a polynomial of order r is fitted using least squares
network[35].
regression.Thefittedpolynomialfunction
| During | the decoding | phase, | the compressed | information |     | is  |     |     |     |     |     |     |     |
| ------ | ------------ | ------ | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2)r
gradually decompressed through successive layers, ultimately F(k)= β kj
|     |     |     |     |     |     |     |     |     |     | j   |     |     | (12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
restoringthedatatoitsoriginalstructure.Adenselayerisapplied
j=0
toreshapethereconstructedoutputtomatchtheoriginalinput
wherek
dimensions [35]. Throughout the training process, the model denotestherelativepositionofadatapointwithinthe
|     |     |     |     |     |     | local window, |     | centered | at i, β | denotes | the coefficients |     | of the |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------- | ------- | ---------------- | --- | ------ |
optimizes its weights and biases to minimize reconstruction j
polynomialfunction,andrdenotestheirorder.Thecoefficients
errorandaccuratelyreconstructtheinputmultivariatetimeseries
sequence[35],[49]. of the polynomial function are then calculated using the least
squaresmethodbyminimizingthefollowingexpression:
| The processing | and | data flow | within an | LSTM AE | is illus- |     |     |         |     |     |         |     |     |
| -------------- | --- | --------- | --------- | ------- | --------- | --- | --- | ------- | --- | --- | ------- | --- | --- |
|                |     |           |           |         |           |     |     | (cid:3) |     |     | (cid:4) |     |     |
tratedinFig.5.
(cid:2)S
−F(k))2
Fig.5providesaconceptualillustrationofthedataflowwithin min (y i+k . (13)
anLSTMAE.Multivariateinputtimeseriesxareencodedinto
k=−S
acompressedlatentrepresentationZ,referredtoasthefeature
|     |     |     |     |     |     |         |      |                   |     |     | x ,x |       | ,...,x , |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ----------------- | --- | --- | ---- | ----- | -------- |
|     |     |     |     |     |     | The SGF | uses | all observations, |     | so  | i−S  | i−S+1 | i        |
space.Thislatentrepresentationisthendecodedtoreconstruct
|     |     |     |     |     |     | ...,x i+S | todetermineanewvalueforx |     |     |     | tatt=i. |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------ | --- | --- | --- | ------- | --- | --- |
theoriginalinputsequence,denotedasxˆ.Thefigureisintended
|           |             |           |          |                |     | After | smoothing | the time | series, | the | gaps were | filled | using |
| --------- | ----------- | --------- | -------- | -------------- | --- | ----- | --------- | -------- | ------- | --- | --------- | ------ | ----- |
| to convey | the general | structure | and flow | of information | and |       |           |          |         |     |           |        |       |
EWMA-imputation,whichfillsmissingvaluesofatimeseries
doesnotreflecttheexactlayerconfigurationoftheimplemented
bycalculatingthemeanfromanequalnumberofobservations
model.
oneithersideofamissingvalue.EWMAemploysaweighting
factorthatdecreasesexponentiallywiththenumberoftimesteps
V. EARLYDETECTIONFRAMEWORK
|     |     |     |     |     |     | fromthemissingvalue.Theweightingfactorisgivenbyw |     |     |     |     |     |     | =   |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
j
2−j,wherejrepresentsthetemporaldistancefromthemissing
Inthissection,weoutlineourproposedframeworkforearly
| disturbancedetection.Webeginwithdatapreparation,followed |     |     |     |     |     | value[55]. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
by the initialization, training, and testing of our LSTM AE The LSTM AE model is designed to process sequences of
model.Finally,weintroduceanewevaluationframework.Fig.6 multivariate time series. The length of the input sequences is
showsthestepsoftheprocesswefollowed. referred to as the “window size,” This defines the observation

22306 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
Fig.6. Methodologyoutline.
TABLEI
Algorithm1:LSTMAutoencoderAnomalyDetection.
SENTINEL-2BANDS,DESCRIPTION,WAVELENGTHRANGE,ANDRESOLUTION
Tr ←Trainingdatasetoftimeseriesofhealthypixels
Te←Testdatasetoftimeseriesofhealthyand
unhealthypixels
τ ←Anomalydetectionthreshold
ws←Windowsize
x←timeseriesinTrorTe
t←timestepinx
TrainLSTM-AE:
forws∈{4,12,26,52}do
forx∈Trdo
|         |     |                 |     |     | a) Initialization: |     | To  | initialize | the model, | we  | constructed | a   |
| ------- | --- | --------------- | --- | --- | ------------------ | --- | --- | ---------- | ---------- | --- | ----------- | --- |
| LSTM_AE |     | ←train_model(x) |     |     |                    |     |     |            |            |     |             |     |
ws
|     |     |     |     |     | multilayer | LSTM | AE  | architecture | designed | to  | process | multi- |
| --- | --- | --- | --- | --- | ---------- | ---- | --- | ------------ | -------- | --- | ------- | ------ |
endfor
variatetimeseriessequencesderivedfromSentinel-2imagery.
endfor
Asinputfeatures,weselectedninespectralbands:B2,B3,B4,
LSTM-AEinference:
|     |     |     |     |     | B5, B6, | B7, B8, | B11, | and B12. | These | bands | were selected | to  |
| --- | --- | --- | --- | --- | ------- | ------- | ---- | -------- | ----- | ----- | ------------- | --- |
forws∈{4,12,26,52}do
|     |     |     |     |     | cover the | spectral | regions | relevant | for | vegetation | monitoring. |     |
| --- | --- | --- | --- | --- | --------- | -------- | ------- | -------- | --- | ---------- | ----------- | --- |
forx∈Tedo
xˆ←LSTM_AE (x) Prioritywasgiventobandsavailableat10mspatialresolution
ws
(cid:3) to enhance the model’s ability to detect subtle canopy-level
|     |         | 1, if|x | −xˆ |>τ, |     |                                                      |     |     |     |     |     |     |     |
| --- | ------- | ------- | -------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |         | t       | t        |     | changesacrossforestplots.Inspectralregionswhereno10m |     |     |     |     |     |     |     |
|     | Anomaly | =       |          |     |                                                      |     |     |     |     |     |     |     |
x,t 0, bands exist, we incorporated the best available alternatives at
otherwise.
20mresolutioninordertocapturesubtletemporalandspatial
endfor
variationsinforestcondition.Anoverviewoftheselectedbands,
endfor theircentralwavelengths,andspatialresolutionsisprovidedin
TableI.
Ourmodelarchitectureconsistsofthreeencodinglayerswith
|     |     |     |     |     | 256, 128, | and 64 | LSTM | units | per layer. | A dropout | layer | with |
| --- | --- | --- | --- | --- | --------- | ------ | ---- | ----- | ---------- | --------- | ----- | ---- |
windowofthemodelandthustheminimumamountofhistorical
adropoutrateof0.2wasinsertedbetweenthefirstandsecond
| data required | for the model | to operate. | For the initial | run, we |            |     |         |             |     |           |       |          |
| ------------- | ------------- | ----------- | --------------- | ------- | ---------- | --- | ------- | ----------- | --- | --------- | ----- | -------- |
|               |               |             |                 |         | LSTM layer | to  | prevent | overfitting | of  | the model | [56]. | First, a |
selected a window size of 52 instances (one year) to cover repeat layer was used in the decoder, which repeats the latent
| an entire | seasonal period. | Both, healthy | training time | series |     |     |     |     |     |     |     |     |
| --------- | ---------------- | ------------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
spacevectortotheinitialwindowsize.Thisisfollowedbytwo
andthetestingtimeseries,werepreprocessedusingtheabove
LSTMlayerswith64unitsand128units,aswellasadropout
mentionedmethodsandthesamewindowsizewasselected.
layerwithadropoutrateof0.2.Finally,anotherLSTMlayerwith
256unitsisinsertedintothearchitectureandatimedistributed
|     |     |     |     |     | dense function |     | layer, | which compresses |     | the | decoder | output |
| --- | --- | --- | --- | --- | -------------- | --- | ------ | ---------------- | --- | --- | ------- | ------ |
B. LSTMAEModel-TrainingandInference
backtotheinputsize,isusedforeachtimestepindividually.4
Here, we outline the development, training, and evaluation The multilayer model structure with the number of trainable
ofourmodel.Toassessperformanceacrossdifferenttemporal parametersineachlayerisdescribedinTableII.
| contexts, | the procedure | was carried out | for multiple window |     |     |     |     |     |     |     |     |     |
| --------- | ------------- | --------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sizesof4,12,26,and52weeks.Thecompleteprocessisdetailed
inAlgorithm1. 4Themodelwasdefinedusingtheopen-sourceMLplatformTensorFlow.

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22307
TABLEII
LSTM-AEMODELSTRUCTURE
Fig.8. Processofmodeltraining.
Fig.9. Processofmodelinference.
ThemodelwastrainedusingtheKerasAPI,specificallythe
compileandfitmethods.TheAdamoptimizationalgorithm[58]
wasemployedformodelupdates,whilemeansquarederrorwas
|     |     |     |     |     |     |     | used as     | loss function. | The            | training  | process |        | involves    | adjusting |       |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | -------------- | --------- | ------- | ------ | ----------- | --------- | ----- |
|     |     |     |     |     |     |     | the model’s | parameters     |                | – weights | and     | biases | – over      | multiple  |       |
|     |     |     |     |     |     |     | iterations  | to minimize    | reconstruction |           |         | error. | Key         | training  | con-  |
|     |     |     |     |     |     |     | figurations | included       | a batch        |           | size of | 128,   | 200 epochs, |           | and a |
Fig.7. ShortwaveinfraredIItrainingdatasamples.
|     |     |     |     |     |     |     | validation | split of | 0.28. | The batch | size | defined | the | number | of  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | --------- | ---- | ------- | --- | ------ | --- |
traininginstancesprocessedbeforeupdatingparameters,while
b)ModelTraining:Afterdefiningthemodel,thepreprocessed epochs determined the total number of dataset iterations. This
timeseriesofthehealthytrainingareas,whichweredescribed processwasrepeatedforthewindowsizesof26,12,and4time
inSectionIII-A,werevisuallyanalyzed,andtheirhealthstatus
steps,resultinginfourmodels.
was assessed using VIs. Pixels exhibiting disturbances at any c)ModelInference:Duringtheinferencephase,themodels
pointwereexcluded,resultingin2885timeseriesfrom2018to processes time sequences and compresses them into a lower-
2024.Fig.7showsonevariable(band)ofthetrainingdata. dimensional representation, known as the latent space. After-
Then, each variable is scaled between 0 and 1 and the time ward, the latent space is expanded to match the length of the
seriesissegmentedaccordingtoaselectedwindowsize,initially
inputsequence,andthisrepresentationisthenreconstructedby
set to 52 to encapsulate a full seasonal cycle. This results in thedecodernetwork[41],[45](seeFig.9).
17310batches,eachcontaining52timestepsand9features. The data transformation within the AE is regulated by the
| Since | the model | operates | in  | an unsupervised |     | setting, no |         |             |        |     |       |               |     |        |     |
| ----- | --------- | -------- | --- | --------------- | --- | ----------- | ------- | ----------- | ------ | --- | ----- | ------------- | --- | ------ | --- |
|       |           |          |     |                 |     |             | weights | of the LSTM | units, |     | which | are optimized |     | during | the |
labeled anomalies or disturbance classes are required during training phase. Since these weights are trained to reconstruct
| training.Theobjectivewastolearntypicalseasonalreflectance |     |     |     |     |     |     |         |              |     |            |         |     |           | x   |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------- | ------- | --- | --------- | --- | --- |
|                                                           |     |     |     |     |     |     | healthy | time series, | the | difference | between |     | the input | and | its |
patternsofhealthyspruceforests,enablingittoaccuratelyrecon- reconstructionxˆwillbelargerifxcontainsanomalousdata.An
structtimeseriesofhealthyforestswhilerecognizinganomalous anomalyatatimesteptisidentifiedifthemeanabsoluteerror
patterns,suchasbark-beetleinfestations[35],[41]. acrossallfeatures,betweenxˆ tandx texceedsathresholdτ[44].
| Each | LSTM | unit | is defined | by  | four | input weights |     |     |     |     |     |     |     |     |     |
| ---- | ---- | ---- | ---------- | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:3)
| ( w ,w , | w , w | ), f o u r | re cu r r e nt | w e ig h | ts ( u ,u | , u , u ) , a n | d   |     |     |     |        |      |      |     |     |
| -------- | ----- | ---------- | -------------- | -------- | --------- | --------------- | --- | --- | --- | --- | ------ | ---- | ---- | --- | --- |
| f i      | C o   |            |                |          | f         | i C o           |     |     |     | 1 , | i f |x | − xˆ | |>τ, |     |     |
|          |       | (b , b     | , b , b        |          |           |                 |     |     |     | =   |        | t t  |      |     |     |
fo u r bi a s v a lu e s f i C o ) [4 7 ]. T h e n u m b e r o f t ra i n a b l e Anomaly t 0 , (15)
|     |     |     |     |     |     |     |     |     |     |     | o th | e rw is e . |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- |
parametersinanLSTMlayerisdeterminedby
θ =4(h(h+i)+h).
|     |     |     |     |     |     | (14) | Foreverymodel,wereconstructeverymultivariatetimeseries |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
withinthetestdataset.Foreverytimeseries,eachband’stime
Thenumberofunitsinalayerisdenotedashandtheinputfea- series is reconstructed based on its own temporal pattern, the
turesaredenotedasi.θrepresentsthetunableparameters[57].
relationshipsbetweendifferentbands,andtheirtemporaldepen-
All parameters are optimized during training to best recon- dencies.Notethatthemodelisabletoreconstructsomebands
struct normal time series behavior [35], [41]. Fig. 8 describes betterinhealthyareasthaninunhealthyforestareas,asshown
| theoperationinabstractterms. |     |     |     |     |     |     | inFig.10. |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |

22308 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
Fig.10. Originaltimeseriesanditsreconstructionsacrossallfeaturesofasingletimeseries,includingreconstructionerrorscalculatedusingtheMAEbetween
differentfeaturecombinations.Redverticallineslabelthedateofdefoliation.TheappliedmodelisLSTM-AE52.
Consequently, we calculated the adjusted reconstruction er- pixelsbasedonVIthresholdsandcreatedascoringmethodthat
rors, which are based on the MAE of different band combina- assumes an anomaly window around the defoliation date. The
tions.Thisadjustmentisintendedtohelptodistinguishbetween earlier anomalies are detected within the window, the higher
healthy and unhealthy time points. We selected the following theygetrewarded.
combinations: a)DefoliationThreshold:Severalauthorsusedstaticthresh-
1) rec_err:allbands. olds based on VIs to determine if spruce vegetation within
2) rec_err_adj1:NIR,RED,REDEDGE1-3,SWIRI/II. a cell is defoliated [59], [60]. NDVI is frequently cited in
3) rec_err_adj2:REDEDGE1-3,SWIRII. the literature as a health indicator of forest vegetation [59],
4) rec_err_adj3:NIR,REDEDGE1-3,SWIRI,SWIRII. [60],[61],[62],[63]andisanefficientmeasuretodistinguish
5) rec_err_adj4:NIR,RED,SWIRI,SWIRII. dead from healthy spruce trees [60], [61]. Although the 10-m
Thethresholdwascalculatedonanindividualbasisforeach resolution of Sentinel-2 imagery does not allow the analysis
windowsizeandbandcombination.Thiswasachievedbyfirst of individual trees, changes in crown color, and needle loss
applying the model to time series representing healthy forest alter the NDVI value in a pixel. Previous studies suggest a
conditions.The99.8thpercentile(quantile0.998)ofthedistri- NDVIrangeof0.481–0.584asthresholdtoassessdefoliationin
bution of the resulting reconstruction errors was then selected mixed conifer-deciduous stands [59]. More recent research by
astheanomalydetectionthreshold. Goldbergs and Upenieks [60] evaluated an NDVI threshold of
All data preprocessing and time series handling as well as 0.46todistinguishbetweenlivinganddeadtreeswithinspruce
trainingandinferencewereconductedinR(v4.4.2).5Themodel monocultures.Throughvisualanalysisoftheimageswefound
wastrainedandevaluatedonaCPU-onlysetup(AMDRyzen5 0.53tobeafittingthresholdfortheNDVI.
7730U,32GBRAM).TrainingtheLSTM-AE26andLSTM- B8−B4
AE52 models for 200 epochs required approximately 7.7 and NDVI= B8+B4 . (16)
15.8h,respectively.Inferenceonaone-yeartimeseriesaveraged
Inaddition,weselectedtheTasseledCapWetness(TCW)index,
0.109 s (LSTM-AE26) and 0.094 s (LSTM-AE52) per pixel
(n=1211),includingpreprocessingandreconstructionsteps. which is a suitable index for disturbance detection on sentinel
time series, especially being more precise during the winter
months[11]
C. EvaluationFramework
TCW=0.1509·B2+0.1973·B3+0.3279·B4
As mentioned in Section II, in remote sensing-based forest
healthmonitoring,labeleddataisextremelydifficulttoobtain. +0.3406·B8−0.7112·B11−0.4572·B12. (17)
The exact start of the bark beetle infestation cannot be deter-
Wefoundathresholdof−0.03tobeespeciallysuited.Inourtest
mined from remote sensing [9]. Therefore, evaluating models
data,wesearchedforpixelsthatfallbelowthethresholdforthree
thatdetectearlyanomaliestopredictforestdisturbanceisvery
consecutiveweeksandclassifiedthefirstinstanceasdefoliation.
difficultifthereisnolabeleddata.Weclassifieddefoliationin
A portion of the defoliation dates was visually checked and
confirmedusingSentinel-2images.
5Inadditiontostandarddatasciencelibraries,thefollowingpackageswere
b)AnomalyWindow:Anticipatingthattheanomalydetection
usedforgeospatialdatahandlingandML:terra,sf,sp,keras,tensor-
flow,isotree,bfast algorithm detects anomalies prior to the apparent defoliated

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22309
state,weimplementedabufferzonetocategorizeinfectedcells
| before | the | needle loss | or discoloration |     | of the | canopy | (i.e., de- |     |     |     |     |     |     |     |     |
| ------ | --- | ----------- | ---------------- | --- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
foliation).Weanalyzedthelagbetweenpredictedanomalyand
| defoliation, |     | to generate | a buffer | period | preceding | defoliation, |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | -------- | ------ | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
duringwhichanomaliesarecorrectlylabeledassuchratherthan
| erroneously |     | classified | as false | positives. | We  | chose a | 52-week |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | -------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalywindowtocaptureearlyindicatorsofhealthdeclinein
sprucestandsthatleadtodefoliation.Bark-beetleinfestedtrees
shownoevidenceofdifferencesinNDVIforupto75daysafter
infestation[24],[64].Timelydetectionisfurtherhamperedby
thedelayedandirregularvitalityresponseofsprucecrownsas
| well    | as frequent | cloud                | cover  | [9],          | both of which | we           | observed |          |                |         |        |       |        |          |             |
| ------- | ----------- | -------------------- | ------ | ------------- | ------------- | ------------ | -------- | -------- | -------------- | ------- | ------ | ----- | ------ | -------- | ----------- |
| in      | our time    | series. Bark-beetles |        | primarily     | attack        | trees        | that are |          |                |         |        |       |        |          |             |
| already | weakened    | by                   | stress | factors,      | such as       | reduced      | resin or |          |                |         |        |       |        |          |             |
| sap     | flow due    | to a disturbed       |        | water balance | [5].          | In addition, | our      |          |                |         |        |       |        |          |             |
|         |             |                      |        |               |               |              |          | Fig. 11. | Predefoliation | Scoring | system | based | on the | temporal | position of |
methoddetectsgeneralhealthanomalies–notjustbark-beetle anomalydetectionrelativetodefoliation.Earlydetectionsarerewarded,while
infestations – a full seasonal cycle allows us to capture phe- lateorfalsedetectionsarepenalized.
| nological |     | variations that | signal | tree | weakening, | improving | the |     |     |     |     |     |     |     |     |
| --------- | --- | --------------- | ------ | ---- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
detectionoftrueanomaliesandenhancingthepredictiveability late detections, ensuring a more reliable assessment of model
ofdefoliationevents.
performance.(seeFig.11.)
Ifananomalyisdetectedwithinthebufferintervalaroundthe To implement the predefoliation Score, we defined an
defoliation,itisclassifiedasatruepositive(TP).Ifananomalyis
anomalywindowaroundthetimeofdefoliation,i.e.,themoment
flaggedoutsidethebuffer,itisclassifiedasafalsepositive(FP). whenvegetationlossiscertaintohaveoccurred.Anomaliesde-
Ifnoanomalyisflaggedwithinthebuffer,itisclassifiedasafalse tectedearlierwithinthiswindowreceiveahigherscore,whereas
negative(FN).Ifapixel’stimeseriesshowsnodefoliationand
detectionsfollowingthedefoliationeventareassignedincreas-
no anomaly is flagged, it is classified as a true negative (TN). ingly negative values. False detections, outside the anomaly
| These | results | were utilized |     | to calculate | the | overall accuracy, |     |        |       |         |              |         |     |        |          |
| ----- | ------- | ------------- | --- | ------------ | --- | ----------------- | --- | ------ | ----- | ------- | ------------ | ------- | --- | ------ | -------- |
|       |         |               |     |              |     |                   |     | window | or in | healthy | time series, | receive | the | lowest | possible |
balanced accuracy, F1 score, commission error and omission score(-1).Anomaliesdetectedwithinthefirstthirdofthepre-
errortoevaluatethemodelsperformance defoliationwindowwereassignedascoreof1,asweobserved
TP+TN thatdetectionsinthistimeframeprovideequallyvaluableearly
OverallAccuracy=
|     |     |     |     |     |     |     | (18) | warnings. | The | score decreases |     | linearly | for | later detections. | It  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | --------------- | --- | -------- | --- | ----------------- | --- |
TP+TN+FP+FN
(cid:5) (cid:6) reacheszerotwoweeksafterthedefoliationevent.Thisdesign
1 TP TN accounts for practical constraints, such as cloud cover, which
|     | BalancedAccuracy= |     |     |     | +   |     | (19) |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2 TP+FN TN+FP can hinder detection in earlier satellite images. If an anomaly
|     |     |     |     |     |     |     |     | is detected | beyond | this | time | frame, | it is assigned |     | an increas- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---- | ---- | ------ | -------------- | --- | ----------- |
2·TP inglynegativescore.Anomaliespredictedoutsidethepredefined
|     |     | F1Score= |     |     |     |     | (20) |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2·TP+FP+FN
anomalywindoworinahealthyforesttimeseriesarepenalized
|     |     |     |     |     |     |     |     | with a | score | of -1. Hence, | if  | no anomaly | is  | detected | in a time |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------- | --- | ---------- | --- | -------- | --------- |
CommissionError= FP serieswherenodefoliationoccurred(i.e.,ahealthyforest),the
(21)
TP+FP
|     |     |     |     |     |     |     |     | model | is rewarded | with | a TN | score | of 0.5. | The predefoliation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ---- | ---- | ----- | ------- | ------------------ | --- |
Scoreisdefinedbythefollowingequation:
FN
|     | OmissionError= |     |       |     | .   |     | (22) |     |     |           |     |     |          |     |     |
| --- | -------------- | --- | ----- | --- | --- | --- | ---- | --- | --- | --------- | --- | --- | -------- | --- | --- |
|     |                |     | TP+FN |     |     |     |      |     |     |           |     | −3  |          |     |     |
|     |                |     |       |     |     |     |      |     |     | pd_score= |     |     | ·(lag−s) |     |     |
(23)
2·k+s
Thismethodicalapproachensuresarobustandtransparenteval-
uationofthemodels,providingasolidfoundationfordetermin-
|     |     |     |     |     |     |     |     | where | the difference | between |     | time | of anomaly | detection | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | ------- | --- | ---- | ---------- | --------- | --- |
|     |     |     |     |     |     |     |     |       |                | (t      | −t  |      |            |           | k   |
ingthebest-performingmodel[65]. defoliation time ) is denoted as lag and
|     |     |     |     |     |     |     |     |     |     | anomaly | defoliation |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- | --- |
c)Pre-DefoliationScore:Theabovemeasuresarecommonly represents the anomaly window (52). A shift, denoted as s is
usedinanomalydetection,butallfailtopromoteearlydetection,
|     |     |     |     |     |     |     |     | added | to award | an anomaly |     | detected | at the | time | of obvious |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---------- | --- | -------- | ------ | ---- | ---------- |
despiteitscriticalimportanceinmitigatingecologicaldamage. defoliationwithapositivevalue.
| Kautzetal.[9]highlightthatonly23%ofthestudiesonearly     |     |     |     |     |     |     |     |     |     | ⎧     |            |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
|                                                          |     |     |     |     |     |     |     |     |     | ⎪⎨−1, | if|lag−s|> |     | 2 k |     |     |
| bark-beetledetectionrelyonaccurategroundtruthdata,under- |     |     |     |     |     |     |     |     |     |       |            |     | 3   |     |     |
scoring the rarity of well-labeled datasets. We have developed pd_score= 1, if(lag−s)<−2k∧lag>=−k
|         |         |                |     |          |             |                 |         |     |     | ⎪⎩       |            |     | 3   |     |     |
| ------- | ------- | -------------- | --- | -------- | ----------- | --------------- | ------- | --- | --- | -------- | ---------- | --- | --- | --- | --- |
| a novel | scoring | method         | to  | address  | this gap:   | the Predefolia- |         |     |     |          |            |     |     |     |     |
|         |         |                |     |          |             |                 |         |     |     | pd_score | otherwise. |     |     |     |     |
| tion    | Score.  | It is designed | to  | evaluate | and compare |                 | anomaly |     |     |          |            |     |     |     |     |
(24)
detectionmodelsinthecontextofforestdisturbanceswhenno
labeledanomalydatesareavailable.Thismetricrewardsearly Ifmultipleanomaliesweredetectedwithintheanomalywin-
anomaly detection while penalizing both false positives and dow, only the first anomaly was considered, while subsequent

22310 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
detectionswereassignedascoreofzerotoensurethatthemodels
arenotrewardedmultipletimesforasingledefoliationevent.
Thepredefoliationscoreprovidesarobustframeworktoeval-
uate early forest disturbance detection. By prioritizing timely
anomalyidentificationwhilepenalizingfalsealarmsanddelayed
detections,thismetricoffersameaningfulwaytocomparemod-
els,evenintheabsenceofperfectlylabeledground-truthdata.
Future studies can leverage this approach to improve remote
sensing-basedforesthealthmonitoring.
D. ModelScoring
Toaddresstheresearchobjectiveofanalyzingtheimportance
of temporal information, we tested LSTM-AE models using
Fig.12. PredefoliationScorecomparisonofLSTMmodelsusingdifferent
diverseinputsequencelengthsof4,12,24,and52weeks.The sequencelengthsandfeaturecombinationsusedforscoring.Boxplotsillustrate
adjustedreconstructionerrorsofallfourmodelswerecompared thedistributionofpd_scoresforeachconfiguration.Whileallspectralbands
wereusedduringmodeltraining,thereconstructionerror(MAE)wascalcu-
witheachother.
latedusingdifferentfeaturecombinationstoevaluatetheirimpactonanomaly
To assess the performance advantages of our models com- sensitivity.
pared to established methods, we compared the LSTM-AE
models to the break detection algorithm BFAST and the other
SWIR22bands,consistentlyachievedthehighestpredefoliation
widely used anomaly detection algorithm IF. BFAST detects
Scores(pd_scores)acrossallLSTM-AEwindowsizes.
structural breaks in time series trends, making it particularly
Thepd_scorequantifieshowearlyananomalywasdetected
suitableforanalyzingVIs.WetestedtheBFASTalgorithmon
relative to a known defoliation event: a score of 0 indicates
the following VIs: NDVI, DWSI, EVI, and DRS, which are
detection at the time of defoliation (including a two-week
frequently used in bark-beetle detection [15], [16], [19], [66],
buffer),while higher values represent earlier detection. Scores
[67]. BFAST requires a historical reference period for each
greater than 0.17 correspond to detections made at least one
observed pixel, we set the training phase from January 2018
month in advance. Except for window size 12, it yielded the
toJanuary2020toensureasufficientnumberofobservations.
highestmeanandmedianpd_scores,withvaluesof0.222and
IFisanunsupervised,tree-basedanomalydetectionalgorithm
0.216 for LSTM-AE52, respectively. Consequently, this fea-
commonly used due to its independence from labeled training
ture combination was selected for further analysis. TNs were
data, making it a suitable baseline for comparison with our
excluded from all box plots to avoid clustering at a pd_score
reconstruction-based approach. We trained IF models on the
of0.5.
samedatasetastheLSTM-AEmodels,applyingarollingwin-
Furthermore,thewindowsizehadanotableeffectonmodel
dow strategy with sequence lengths of 26 and 52, as shorter
performance.Wewillrefertotheseexperimentsas“LSTM-AE”
windows(4and12)yieldedunstableresults.Modelperformance
concatenated with the respective window size (e.g., LSTM-
was further optimized by tuning the number of trees, testing
AE26).Modelswithlongerinputsequences(LSTM-AE26and
configurationsof100,300,and500estimators.
LSTM-AE52) exhibited higher median and mean pd_scores.
Bothalgorithmsoutputthetimingdetectedanomaliesforeach
Forinstance,LSTM-AE26achievedameanpd_scoreof0.194,
time series, which we then use to compute the predefoliation
while LSTM-AE4 yielded a lower value of 0.135. Although
Score,alongwiththeperformancemetricsoverallaccuracy,bal-
LSTM-AE4 produced fewer false positives and late detec-
ancedaccuracy,F1-score,commissionerror,andomissionerror.
tionsandhadlowerscorevariance,itunderperformedinearly
Finally, we compared these results to those of the LSTM-AE
anomalydetection.
modelstoevaluatetheirrelativeeffectivenessinearlyanomaly
Fig. 13(a) displays the pd_score distributions as box plots,
detection.
showingthatpd_scoresincreasewithsequencelength.LSTM-
AE52 produced the highest values overall. Fig. 13(b) presents
VI. RESULTS
cumulative probability curves, highlighting that LSTM-AE26
Toevaluatemodelperformance,weappliedfourLSTM-AE andLSTM-AE52detectagreaterproportionofanomalieswith
variants using temporal input sequences of 4, 12, 26, and 52 scoresabove0.17,indicatingearlierdetectionsrelativetodefo-
weeks.Thesewerecomparedagainsttwoestablishedanomaly liation.
detection approaches: BFAST and IF. In the following, we
presenttheresultsofthesecomparisonsusingthepredefoliation B. PerformanceComparisonAgainstBaselineModels
scoreandstandardclassificationmetrics.
To compare the performance of our LSTM-AE models to
BFAST and IF, we calculated the mean predefoliation score
A. SequenceLengthandAdjustedReconstructionErrors
(PDSµ) and the percentage of pixels where anomalies were
The results in Fig. 12 show that rec_err_adj4, the adjusted flagged more than four weeks prior to defoliation (PDS %).
reconstruction error based on the NIR, RED, SWIR16, and Weadditionallycomputedoverallaccuracy,balancedaccuracy,

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22311
Fig.13. PredefoliationScorecomparisonusingdifferentsequencelengthsin
Fig.14. Distributionofpredefoliationscoresacrossallmodels.LSTM-AE
LSTMmodels.(a)Boxplotsillustratingthedistributionofscoresacrossdifferent modelsareshowninblue,BFASTvariantsinredandIFingreen.Boxplots
models. (b) Cumulative probability curves depicting the score distributions. andviolinplotsillustratethespread,density,andmedianpd_scoresforeach
| Higherscoresindicateearlierdetectionsrelativetodefoliation. |     |     |     |     |     |     |     | method. |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
TABLEIII
PERFORMANCESUMMARYOFTHELSTM-AEMODELSANDTHECOMPARISON C. EvaluationMaps
MODELSBFASTANDIF
|     |     |     |     |     |     |     |     | The predefoliation |     |     | scoring | system | enables | the creation | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------- | ------ | ------- | ------------ | --- |
mapsthatvisualizemodelperformancewithinanobservedarea.
|     |     |     |     |     |     |     |     | Fig. 15 | visualizes | the | predefoliation |     | scores of | the respective |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | -------------- | --- | --------- | -------------- | --- |
pixelsinalargersprucecultivationareaforthetimespanfrom
2020totheendof2024.
|     |     |     |     |     |     |     |     | Both | LSTM-AE | variants | demonstrate |     | more | robust anomaly |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | -------- | ----------- | --- | ---- | -------------- | --- |
detection,withsignificantlyfewerfalsepositivesthanBFAST.
ThisisvisualizedinthetestareashowninFig.15,comprising
|     |     |     |     |     |     |     |     | approximately |     | 44 500 | pixels | (445 ha). | LSTM-AE26 | produces |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------ | --------- | --------- | -------- | --- |
around6500falsepositivesandLSTM-AE52about8000,com-
F1 score, commission error, and omission error to compre- pared to approximately 10 500 for BFAST. LSTM-AE26 also
hensivelyassessmodelperformance.Weselectedtheseperfor- resultsinslightlyfewerlatedetections(redpixels)thanLSTM-
mancemetricstoensurecomparabilitywithotherstudies,such AE52,byroughly300pixels.However,LSTM-AE52achieves
asSchilleretal.[29],whichemployedsimilarevaluationcriteria the highest number of early detections, defined as anomalies
for classification-based disturbance detection. Since BFAST detectedmorethanfourweekspriortodefoliation(pd_score>
| requiresatwo-yearreferenceperiod,weexcludedallpixeltime |             |     |        |           |        |      |          | 0.17). |     |     |     |     |     |     |     |
| ------------------------------------------------------- | ----------- | --- | ------ | --------- | ------ | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| series with                                             | defoliation |     | events | occurring | before | 2020 | from the |        |     |     |     |     |     |     |     |
evaluation.TheperformanceresultsaresummarizedinTableIII. VII. DISCUSSION
TableIIIsummarizesmodelperformanceusingrec_err_adj4,
Thisstudydemonstratestheeffectivenessoftheunsupervised
basedonSentinel-2bandsNIR,RED,SWIR16,andSWIR22.
|         |           |             |     |        |      |       |         | deep learning |     | LSTM-AE | model, | for | early detection | of  | forest |
| ------- | --------- | ----------- | --- | ------ | ---- | ----- | ------- | ------------- | --- | ------- | ------ | --- | --------------- | --- | ------ |
| Results | are shown | for LSTM-AE |     | models | with | input | windows |               |     |         |        |     |                 |     |        |
disturbancesinNorwaysprucestandsusingmultispectraltime
of4,12,26,and52weeks;forBFASTusingmultiplevegeta-
|              |         |       |        |        |        |             |            | series. By | focusing | on  | physiologically |     | relevant       | spectral | bands |
| ------------ | ------- | ----- | ------ | ------ | ------ | ----------- | ---------- | ---------- | -------- | --- | --------------- | --- | -------------- | -------- | ----- |
| tion indices | (DRS,   | DWSI, | NDVI,  | EVI2); |        | and for     | IF applied |            |          |     |                 |     |                |          |       |
|              |         |       |        |        |        |             |            | (NIR, RED, | SWIR16,  |     | and SWIR22)     |     | and optimizing | sequence |       |
| with input   | windows | of    | 26 and | 52     | weeks. | The metrics | used       |            |          |     |                 |     |                |          |       |
lengths,theLSTM-AEmodels,especiallythe26-weekvariant,
forcomparisonarePDSµ,PDS%,balancedaccuracy(BA),F1
achievedastrongbalancebetweenearlyanomalydetection,low
score,commissionerror(CE),andomissionerror(OE).Among
commissionerrorandsmallinputdatademands.Comparedto
theLSTM-AEmodels,LSTM-AE4hadthelowestcommission
traditionalmethodslikeBFASTandIF,ourmodelsconsistently
error(0.041),whileLSTM-AE26showedthehighestbalanced
outperformedacrossmultipleevaluationmetrics.Thesefindings
| accuracy | (0.873) | and F1 | score | (0.899). | LSTM-AE52 |     | reached |     |     |     |     |     |     |     |     |
| -------- | ------- | ------ | ----- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
highlightthepotentialofourmodelforearlyanomalydetection
| the highest | values | in PDSµ | (0.274) |           | and PDS% | (64.84%). | The    |                |              |        |        |            |       |              |        |
| ----------- | ------ | ------- | ------- | --------- | -------- | --------- | ------ | -------------- | ------------ | ------ | ------ | ---------- | ----- | ------------ | ------ |
|             |        |         |         |           |          |           |        | in operational |              | forest | health | monitoring | and   | proactive    | forest |
| baseline    | models | BFAST   | and     | IF showed | lower    | scores    | across |                |              |        |        |            |       |              |        |
|             |        |         |         |           |          |           |        | management,    | particularly |        | in     | scenarios  | where | labeled data | are    |
allmetrics.Thedistributionofpredefoliationscoresacrossthe
limited.
| LSTM-AE,BFAST,andIFmodelsis |       |     |              |     | illustratedinFig.14. |     |        |     |     |     |     |     |     |     |     |
| --------------------------- | ----- | --- | ------------ | --- | -------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Fig. 14                     | shows | the | distribution |     | of Pre-Defoliation   |     | Scores |     |     |     |     |     |     |     |     |
A. SpectralSensitivityandTemporalResolution
| across all | models. | LSTM-AE |     | models | tend | to produce | higher |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | --- | ------ | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
scoresaswindowsizeincreases.BFASTmodelsdisplaygreater AsshowninFig.12,themosteffectivebandcombinationfor
variance, and the DRS variant yields a positive median. IF anomaly scoring was rec_err_adj4, consisting of NIR, RED,
modelsshowlowermediansandnarrowerinterquartileranges. SWIR16, and SWIR22. These bands yield great sensitivity to

22312 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
Fig.15. PredefoliationscoremapsforLSTM-AE52,LSTM-AE26,andBFASToverasprucecultivationareaintheThuringianForest.Thepd_scorevalues
indicatethetimingofdetectedanomaliesrelativetothedefoliationevent.Yellowpixelsrepresentfalsepositives;redpixelsindicatelatedetections.Bluepixels
denotetimelyorearlydetections:mediumbluecorrespondstodetectionsmorethanfourweekspriortodefoliation(pd_score≥0.18),whiledarkblueindicates
detectionsmorethan26weeksprior(pd_score>0.75).
|     |     |     |     |     | vegetation-related |     | changes | as SWIR | relates | to  | water | content, |
| --- | --- | --- | --- | --- | ------------------ | --- | ------- | ------- | ------- | --- | ----- | -------- |
NIRreflectsmesophyllstructure,andREDissensitivetochloro-
|     |     |     |     |     | phyll content | in vegetation |     | [68]. | Furthermore, |     | we noticed | that |
| --- | --- | --- | --- | --- | ------------- | ------------- | --- | ----- | ------------ | --- | ---------- | ---- |
thesebandstendtodeviateearlierormoredistinctlyfromnormal
|     |     |     |     |     | temporal | patterns | under | disturbance | conditions. |     | Although | the |
| --- | --- | --- | --- | --- | -------- | -------- | ----- | ----------- | ----------- | --- | -------- | --- |
modelstillutilizesallbandinputsforreconstruction,restricting
|     |     |     |     |     | the reconstruction |               | error   | calculations | to          | these bands | enhanced  |       |
| --- | --- | --- | --- | --- | ------------------ | ------------- | ------- | ------------ | ----------- | ----------- | --------- | ----- |
|     |     |     |     |     | sensitivity        | to vegetation | changes |              | and allowed | earlier     | detection |       |
|     |     |     |     |     | of disturbances.   | Using         | other   | combinations |             | or          | all bands | could |
diluteordelaytheanomalysignal.
However,itisimportanttonote,remotelydetectablechanges
incanopyvitalityoftenlagbehindtheactualinfestationevent.
|     |     |     |     |     | For example, | bark | beetle | infestations | in  | late summer | may | not |
| --- | --- | --- | --- | --- | ------------ | ---- | ------ | ------------ | --- | ----------- | --- | --- |
causevisiblespectralchangesuntilthefollowingspringdueto
winterdormancy[9].Toaddressthis,ouranomalyscoringuses
Fig.16. LSTM-AE26scoremapwithforesttracks.Foresttracksareoverlaid
a52-weekwindowtoensuredelayedmortalitysignalsarenot
| on the evaluation | map, revealing | that many | false positives predicted | by the |     |     |     |     |     |     |     |     |
| ----------------- | -------------- | --------- | ------------------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
LSTM-AEmodelalignwiththesepaths. misclassifiedasfalsepositives.
|     |     |     |     |     | The chosen | sequence      |         | length | of a model | determines    |     | how     |
| --- | --- | --- | --- | --- | ---------- | ------------- | ------- | ------ | ---------- | ------------- | --- | ------- |
|     |     |     |     |     | temporal   | relationships | between |        | features   | are captured. |     | Smaller |
windows(e.g.,size4)focusstrongeronshort-termdependencies
|     |     |     |     |     | and relationships |           | between | features. | Larger | windows  |             | capture |
| --- | --- | --- | --- | --- | ----------------- | --------- | ------- | --------- | ------ | -------- | ----------- | ------- |
|     |     |     |     |     | broader temporal  | patterns, |         | enabling  | more   | abstract | representa- |         |
tionsofthetimeseries.However,thiscanleadtostrongerdevi-
ationsbetweenthereconstructedandoriginalsignals,increasing
theriskoffalsepositiveswhenshort-termphenologicalchanges
|     |     |     |     |     | are mistakenly | flagged | as  | anomalies. | Although |     | LSTM-AE52 |     |
| --- | --- | --- | --- | --- | -------------- | ------- | --- | ---------- | -------- | --- | --------- | --- |
excelsinearlydetection,LSTM-AE26offeredthebesttradeoff,
|     |     |     |     |     | combining | strong | early | detection | with | minimal | false | alarms. |
| --- | --- | --- | --- | --- | --------- | ------ | ----- | --------- | ---- | ------- | ----- | ------- |
Thistradeoffillustrateshowwindowsizeshouldbetunedbased
Fig.17. AnomalydetectioninshorttimeseriesusingLSTM-AE26.Thefigure
demonstrates the model’s capability to detect anomalies early despite using onoperationalneedsandtoleranceforfalsepositives.
onlyshortinputsequences.Theupperrowshowstheoriginalandreconstructed Inasimilarvein,theinterpretationofanomalyscoresandthe
valuesfortheSWIR22band,whilethelowerrowdisplaysthecorresponding classification of a time step as anomalous depend strongly on
reconstructionerroracrosstherec_err_adj4features.LSTM-AE26isapplied
independentlytoeachinputwindow. theselectedthreshold.Inthisstudy,weusedastrictthreshold

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22313
Fig.18. Anomalydetectionmap.Thegradientchangesymbolizestheweeksafterthebeginningoftheobservation,inwhichanomaliesaredetected.Theused
modelwasLSTM-AE26.
correspondingtothe0.998quantileoftheanomalyscoredistri- by analyzing the temporal relationships between all variables,
butioninahealthytestarea.Thisallowsthedetectionofsubtle isillustratedinFig.17.
deviations from normal behavior, enabling early disturbance Furthermore,theLSTM-AEmodelscanbeusedtogenerate
detection but also increasing the risk of false positives. The anomalydetectionmaps,whichprovideaspatialandtemporal
thresholdcanbeadjusteddependingontheapplicationcontext. representation of detected anomalies within a given area. This
Compared to the baseline models, the LSTM-AE models visualizationallowsforamoreintuitiveinterpretationofwhen
demonstrated superior performance across all evaluation met- andwheredisturbancesinsprucehealthoccurovertime.Retro-
rics.BFASTusingtheDRSindexwasthestrongestamongthem spectiveapplicationoftheanomalydetectionmethodtoprevi-
butstilllaggedbehindbothLSTM-AEmodels.Thesefindings ouslydisturbedforestregionsenablesadeeperunderstandingof
highlighttheadvantageofdeeplearningmodelsthatincorporate thepatternsofprogressionofdisturbances.Fig.18visualizesthe
temporalcontexts,particularlyforearlystagedetectionofdefo- disturbancedynamic,inoneofthetestareas,showinganomalies
liation.AsshowninFig.14,theLSTM-AEmodelsconsistently that initially appear in central hotspots and then expand out-
producehigherpredefoliationscores,indicatingstrongerearly ward.Despitebeingtestedonasmallarea,theapproachholds
detectioncapabilities.Incontrast,IFandmostBFASTvariants significant potential for investigating disturbance dynamics on
showlowerormorevariablescores,suggestingamorereactive a broader scale. The analysis of breakout patterns has become
detectionbehavior. a key focus of research with important implications for forest
Theevaluationmaps(seeFig.15)confirmthistrend,where managementplanning[69],[70],[71].
BFAST also shows substantially more false positives and less To assess the generalizability of the model, it should be
early detections. Many FPs in the LSTM-AE models match applied to a broader range of study areas that include diverse
forest tracks (see Fig. 16). These false positives correspond to foreststructuresandtreespecies.Furthermore,transferlearning
nonforestfeatures,suggestingtheneedforimprovedmasking. methodsmayofferapromisingapproachforadaptingthemodel
tonewregionsandconditionswithoutextensivetraining.While
thisstudyprovidesanimportantfoundation,furtherresearchis
B. ImplicationonForestMonitoring
requiredtoexploreandvalidatethemodel’sapplicabilityacross
Unlike more complex architectures such as Transformers, differentecologicalsettings.
which may require millions of labeled samples [29], our ap-
proachachievedstrongperformanceusingjust2885pixeltime
C. Limitations
series.Moreover,ourmodelissuitedfor,wall-to-wallmonitor-
ingofspruceforestsatfederalstatetonationalscales,givenits While the LSTM-AE models demonstrated strong perfor-
short time series inputs. An example of the model’s ability to mance, several limitations should be acknowledged. First, in-
detectanomaliesbeforethedefoliationonshortinputtimeseries, ferencetimewaslongerthanforbaselinemethodswhenusing

22314 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
long input sequences (e.g., six years), which may constrain anovelscoringmethodthatcomplementsconventionalperfor-
long-term,large-areareconstructionsincomputationallylimited mancemetricsbyrewardingearlydetections,acrucialfactorin
environments. However, this was partly due to the absence disturbancepredictiontasks.
of GPU acceleration and can be mitigated with appropriate This work provides a foundation for future research by
hardware. Second, as an unsupervised method, the LSTM-AE demonstrating the potential of LSTM Autoencoders for early
lacksdirectinterpretability.Themodeldoesnotprovideinsights detectionofforestdisturbancesbasedonSentinel-2timeseries.
intowhichspectralbandsortemporalfeaturescontributemost The model and evaluation framework developed in this study
toadetectedanomaly.Althoughnotexploredinthisstudy,tech- weretailoredtothespecificcontextofdetectingearlysignsof
niquesforevaluatingfeatureimportanceandimprovingmodel disturbanceinpureconifer(Norwayspruce)standsinThuringia.
interpretabilitysuchasintegratedgradients[72]shouldbecon- Whilethisfocusedapproachensuredacontrolledandconsistent
sideredinfutureresearch.Third,thisstudyfocusedonrelatively test environment, it naturally limits the generalizability of our
homogeneousNorwaysprucestandswithinalimitedgeographic findings.Infuturework,weaimtoextendouranalysistobroader
region. While this constraint limits immediate generalizability spatialdomains,incorporatingdiverseforesttypessuchasdecid-
to other forest types or biomes, its focus lies on the pressing uousandmixedstands,andapplyingtheapproachtoadditional
issueofsprucedeclineduetobarkbeetleoutbreaks.Ourstudy geographic regions within Central Europe. This will allow for
establishes a methodological foundation for early disturbance a more comprehensive assessment of the model’s robustness
detection.Futureresearchwillaimtoadaptandtestthemodel and general applicability across varying forest structures and
across more diverse forest ecosystems, using approaches such landscapes.Furthermore,weaimtoenhancetheinterpretability
astransferlearningtosupportbroaderapplicability. ofthemodelbyprovidinggreatertransparencyregardingfeature
importance. Ultimately, the approach presented here provides
a flexible foundation for developing scalable early warning
VIII. CONCLUSION
systemsforforesthealthandholdspotentialfortransfertoother
We introduced an anomaly detection framework for moni- domainsofenvironmentalanomalydetection.
toringforesthealthdynamicsinspruce-dominatedstands,using
barkbeetleoutbreaksasacasestudy.Theapproachisbasedonan
unsuperviseddeeplearningalgorithm,specifically,amultilayer REFERENCES
LSTMAutoencoder,trainedonSentinel-2timeseriestoidentify [1] Thüringer Ministerium für Infrastruktur und Landwirtschaft,
deviations from typical spectral–temporal patterns. Although “Waldzustandsbericht,” 2023. [Online]. Available: https://digitales-
infrastruktur.thueringen.de/fileadmin/Forst_und_Jagd_Fischerei/
not explicitly trained to detect specific disturbance types, the
Forstwirtschaft/2023_Waldzustandsbericht.pdf
modelwasappliedtopuresprucestandswherecanopydeteriora- [2] T.O.RandhirandA.Erol,“Emergingthreatstoforests:Resilienceand
tionisstronglyassociatedwithIpstypographusoutbreaks.Thus, strategiesatsystemscale,”Amer.J.PlantSci.,vol.4,no.3,pp.739–748,
2013.
the detected anomalies likely reflect early bark beetle-induced
[3] Z.Vacek,S.Vacek,andJ.Cukor,“Europeanforestsunderglobalclimate
stress. More generally, the model will also respond to other change:Reviewoftreegrowthprocesses,crisesandmanagementstrate-
disturbances,suchasstormdamage,drought-induceddieback, gies,”J.Environ.Manage.,vol.332,2023,Art.no.117353.
[4] C.BoisvenueandS.W.Running,“Impactsofclimatechangeonnatural
or clear cuts, provided they cause detectable spectral changes
forestproductivity–evidencesincethemiddleofthe20thcentury,”Glob.
overtime. ChangeBiol.,vol.12,no.5,pp.862–882,2006.
The model was tested with different input window sizes, [5] W. Schwenke, “Beziehungen zwischen tierischen schädlingen und
baumerkrankungen,”ForstwissenschaftlichesCentralblatt,vol.104,no.1,
revealingthatlargerwindowsleadtoearlierdetectionsofdistur-
pp.220–225,1985.
bances,allowingtheidentificationofearlysignsofstressprior [6] B.J.Bentzetal.,“ClimatechangeandbarkbeetlesofthewesternUnited
to visible damage. Notably, the LSTM-AE52 variant achieved StatesandCanada:Directandindirecteffects,”BioScience,vol.60,no.8,
pp.602–613,2010.
anaccuracyof87%,with65%ofthedetectedanomaliesflagged
[7] F.Sergio,J.Blas,andF.Hiraldo,“Animalresponsestonaturaldistur-
morethanfourweeksbeforevisibledefoliationoccurredinthe banceandclimateextremes:Areview,”Glob.Planet.Change,vol.161,
pixel.Inaddition,wefoundthatawindowsizeof26timesteps pp.28–40,2018.
[8] T.Hlásnyetal.,“BarkbeetleoutbreaksinEurope:Stateofknowledge
was sufficient to ensure robust and early anomaly detection.
andwaysforwardformanagement,”Curr.ForestryRep.,vol.7,no.3,
Thememory-efficientdesignofourmodeleliminatestheneed pp.138–165,2021.
forlabeledtrainingdataorextensivehistoricalrecordsforeach [9] M.Kautz,J.Feurer,andP.Adler,“Earlydetectionofbarkbeetle(Ips
typographus)infestationsbyremotesensing–Acriticalreviewofrecent
pixel. This renders it well-suited for large-scale near-real-time
research,”ForestEcol.Manage.,vol.556,Mar.2024,Art.no.121595.
monitoring,whereoldertimeinputscanbeignored.Bycaptur- [10] H.Abdullah,A.K.Skidmore,R.Darvishzadeh,andM.Heurich,“Sentinel-
ingbothspectralandtemporalrelationshipsacrossallSentinel-2 2accuratelymapsgreen-attackstageofEuropeansprucebarkbeetle(ips
typographus,l.)comparedwithlandsat-8,”RemoteSens.Ecol.Conserva-
bands,ourmethodprovidesapowerfultoolfordetectingsubtle
tion,vol.5,no.1,pp.87–106,2019.
changes in the health of pure spruce stands, that can indicate [11] V.Bárta,P.Lukeš,andL.Homolová,“Earlydetectionofbarkbeetlein-
early signs of stress, due to abiotic or biotic factors such as festationinNorwayspruceforestsofcentralEuropeusingsentinel-2,”Int.
J.Appl.EarthObserv.Geoinformation,vol.100,2021,Art.no.102335.
drought,orinsectattacks.Theseearlysignsofstresscanserve
[12] V.Bárta,J.Hanuš,L.Dobrovolný,andL.Homolová,“Comparisonoffield
aspredictorsofsubsequentdefoliationevents. surveyandremotesensingtechniquesfordetectionofbarkbeetle-infested
The proposed models were evaluated against BFAST and trees,”ForestEcol.Manage.,vol.506,2022,Art.no.119984.
[13] A.Lausch,M.Heurich,D.Gordalla,H.-J.Dobner,S.Gwillym-Margianto,
the IF algorithm. The results of this comparison highlight the
and C. Salbach, “Forecasting potential bark beetle outbreaks based on
superiorityoftheLSTMAutoencoderapproach,particularlyin spruce forest vitality using hyperspectral remote-sensing techniques at
termsofearlyanomalydetection. Furthermore,weintroduced differentscales,”ForestEcol.Manage.,vol.308,pp.76–89,2013.

KIRSCHetal.:EARLYDETECTIONOFFORESTDISTURBANCESINHOMOGENEOUSSTANDS–DEEPLEARNING-BASEDMONITORING 22315
[14] M. A. Wulder, J. C. White, A. L. Carroll, and N. C. Coops, “Chal- [35] Y.Wei,J.Jang-Jaccard,F.Sabrina,W.Xu,S.Camtepe,andA.Dunmore,
lengesfortheoperationaldetectionofmountainpinebeetlegreenattack “Reconstruction-basedLSTM-autoencoderforanomaly-basedDDoSat-
with remote sensing,” Forestry Chronicle, vol. 85, no. 1, pp.32–38, tackdetectionovermultivariatetime-seriesdata,”2023.[Online].Avail-
2009. able:https://arxiv.org/abs/2305.09475
[15] J.Verbesselt,R.Hyndman,G.Newnham,andD.Culvenor,“Detecting [36] M.Li,Y.Li,K.Cao,andB.Han,“Anomalydetectionofecologicalmon-
trendandseasonalchangesinsatelliteimagetimeseries,”RemoteSens. itoringdatabasedonlongandshort-termmemorynetwork-autoencoder,”
Environ.,vol.114,no.1,pp.106–115,2010. inProc.5thInt.SeminarArtif.Intell.,Netw.Inf.Technol.,Nanjing,China:
[16] L.M.WattsandS.W.Laffan,“EffectivenessoftheBFASTalgorithm Mar.2024,pp.962–965.
fordetectingvegetationresponsepatternsinasemi-aridregion,”Remote [37] D.Nakar,“Sentinel-2:Multispectralinstrument(MSI)designandsystem
Sens.Environ.,vol.154,pp.234–245,2014. performance,”2019,doi:10.13140/RG.2.2.27242.67529.
[17] J. Verbesselt, D. Masiliunas, A. Zeileis, and M. Appel, “Bfast: Breaks [38] J.LouisandL.Team,“Level-2aalgorithmtheoreticalbasisdocument,”
foradditiveseasonandtrend,”Rpackageversion1.6.1,2009.[Online]. 2021.
Available:https://CRAN.R-project.org/package=bfast [39] M. Campos-Taberner et al., “Understanding deep learning in land use
[18] Y.-L. Kong, Q. Huang, C. Wang, J. Chen, J. Chen, and D. He, “Long classificationbasedonsentinel-2timeseries,”Sci.Rep.,vol.10,no.1,
short-termmemoryneuralnetworksforonlinedisturbancedetectionin 2020,Art.no.17188.
satelliteimagetimeseries,”RemoteSens.,vol.10,no.3,2018,Art.no.452. [40] P.Li,Y.Pei,andJ.Li,“Acomprehensivesurveyondesignandapplication
[19] L.Huo,H.J.Persson,andE.Lindberg,“Earlydetectionofforeststress of autoencoder in deep learning,” Appl. Soft Comput., vol. 138, 2023,
from European spruce bark beetle attack, and a new vegetation index: Art.no.110176.
Normalized distance red & SWIR (NDRS),” Remote Sens. Environ., [41] I.Goodfellow,Y.Bengio,andA.Courville,DeepLearning.Cambridge,
vol.255,2021,Art.no.112240. MA,USA:MITPress,2016.
[20] H.Abdullah,A.K.Skidmore,R.Darvishzadeh,andM.Heurich,“Timing [42] L.Ma,Y.Liu,X.Zhang,Y.Ye,G.Yin,andB.A.Johnson,“Deeplearning
of red-edge and shortwave infrared reflectance critical for early stress inremotesensingapplications:Ameta-analysisandreview,”ISPRSJ.
detectioninducedbybarkbeetle(ipstypographus,l.)attack,”Int.J.Appl. PhotogrammetryRemoteSens.,vol.152,pp.166–177,2019.
EarthObserv.Geoinformation,vol.82,2019,Art.no.101900. [43] H.D.Trinh,E.Zeydan,L.Giupponi,andP.Dini,“Detectingmobiletraffic
[21] M. Löw and T. Koukal, “Phenology modelling and forest disturbance anomaliesthroughphysicalcontrolchannelfingerprinting:Adeepsemi-
mappingwithsentinel-2timeseriesinAustria,”RemoteSens.,vol.12, supervisedapproach,”IEEEAccess,vol.7,pp.152187–152201,2019.
no.24,2020,Art.no.4191. [44] V.Chandola,A.Banerjee,andV.Kumar,“Anomalydetection:Asurvey,”
[22] R. Dutrieux, J.-B. Feret, and K. Ose, “Mise au point d’une méthode ACMComput.Surv.,vol.41,no.3,pp.1–58,2009.
reproductiblepourlesuivigénéralisédesdégâtsdescolytespartélédétec- [45] S.J.RussellandP.Norvig,inArtificialintelligence:AModernApproach,
tionsatellitaire,”RevueONFRendez-VousTechniques,SpécialGestionde (Pearson Series inArtificial Intelligence Series), 4thed. Hoboken, NJ,
crise:l’exempledelaCriseScolytes,vol.69,no.70,pp.37–44,2021. USA:Pearson,2020.
[23] L.Xuetal.,“Timeseriesanalysisforgloballandcoverchangemonitoring: [46] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
A comparison across sensors,” Remote Sens. Environ., vol. 271, 2022, Comput.,vol.9,no.8,pp.1735–1780,1997.
Art.no.112905. [47] F. A. Gers, J. Schmidhuber, and F. Cummins, “Learning to forget:
[24] S.Jamali,P.-O.Olsson,A.Ghorbanian,andM.Müller,“Examiningthe Continual prediction with LSTM,” Neural Comput., vol. 12, no. 10,
potential for early detection of spruce bark beetle attacks using multi- pp.2451–2471,2000.
temporalsentinel-2andharvesterdata,”ISPRSJ.PhotogrammetryRemote [48] Y.Yu,X.Si,C.Hu,andJ.Zhang,“Areviewofrecurrentneuralnetworks:
Sens.,vol.205,pp.352–366,2023. LSTMcellsandnetworkarchitectures,”NeuralComput.,vol.31,no.7,
[25] V.L.S.Ginoetal.,“Integratingunsupervisedmachineintelligenceand pp.1235–1270,2019.
anomaly detection for spatio-temporal dynamic mapping using remote [49] S.J.RussellandP.Norvig,ArtificialIntelligence:AModernApproach,
sensingimageseries,”Sustainability,vol.15,no.6,2023,Art.no.4725. (Pearson Series in Artificial Intelligence), 4th ed. Hoboken, NJ, USA:
[Online].Available:https://www.mdpi.com/2071-1050/15/6/4725 Pearson,2021.
[26] Y.QinandY.Lou,“Hydrologicaltimeseriesanomalypatterndetection [50] J.W.Tukey,ExploratoryDataAnalysis,Ser.Addison-WesleySeriesin
basedonisolationforest,”inProc.IEEE3rdInf.Technol.,Netw.,Electron. BehavioralScience.Reading,MA,USA:Addison-WesleyPubl,1977.
Autom.ControlConf.,2019,pp.1706–1710.[Online].Available:https: [51] R.Caoetal.,“AsimplemethodtoimprovethequalityofNDVItime-series
//ieeexplore.ieee.org/document/8729405/ databyintegratingspatiotemporalinformationwiththeSavitzky-Golay
[27] Y.Yuanetal.,“Usinganattention-basedLSTMencoder–decodernetwork filter,”RemoteSens.Environ.,vol.217,pp.244–257,2018.
fornearreal-timedisturbancedetection,”IEEEJ.Sel.TopicsAppl.Earth [52] J.Chen,P.Jönsson,M.Tamura,Z.Gu,B.Matsushita,andL.Eklundh,“A
Observ.RemoteSens.,vol.13,pp.1819–1832,2020. simplemethodforreconstructingahigh-qualityNDVItime-seriesdataset
[28] G.Zhou,M.Liu,andX.Liu,“Anautoencoder-basedmodelforforest basedontheSavitzky–Golayfilter,”RemoteSens.Environ.,vol.91,no.3,
disturbancedetectionusingLandsattimeseriesdata,”Int.J.Digit.Earth, pp.332–344,2004.
vol.14,no.9,pp.1087–1102,Sep.2021. [53] J.FengandY.Tao,“ReconstructionofMODISNDVItimeseriesincloudy
[29] C. Schiller, J. Költzow, S. Schwarz, F. Schiefer, and F. E. Fassnacht, areabasedonSavitzky-Golayfilterwithspatial-temporalkrigingimprove-
“Forest disturbance detection in central Europe using transformers ment,” in Proc. Int. Conf. Signal Process., Comput. Netw., Commun.,
and sentinel-2 time series,” Remote Sens. Environ., vol. 315, 2024, H.Wang,Ed.SPIE,2023,pp.382–387.
Art. no. 114475. [Online]. Available: https://linkinghub.elsevier.com/ [54] H. Kordestani and C. Zhang, “Direct use of the savitzky–golay filter
retrieve/pii/S0034425724005017 to develop an output-only trend line-based damage detection method,”
[30] M.RußwurmandM.Körner,“Multi-temporallandcoverclassification Sensors,vol.20,no.7,2020,Art.no.1983.
with long short-term memory neural networks,” Int. Arch. Photogram- [55] S.MoritzandT.Bartz-Beielstein,“imputeTS:Timeseriesmissingvalue
metry, Remote Sens. Spatial Inf. Sci., vol. XLII-1/W1, pp.551–558, imputationinR,”RJ.,vol.9,no.1,2017,Art.no.207.
May2017. [56] N.Srivastava,G.Hinton,A.Krizhevsky,I.Sutskever,andR.Salakhutdi-
[31] M.RußwurmandM.Körner,“Self-attentionforrawopticalsatellitetime nov,“Dropout:Asimplewaytopreventneuralnetworksfromoverfitting,”
seriesclassification,”ISPRSJ.PhotogrammetryRemoteSens.,vol.169, J.Mach.Learn.Res.,vol.15,no.56,pp.1929–1958,2014.
pp.421–435,Nov.2020,arXiv:1910.10536[cs]. [57] R.Karim,“Countingno.ofparametersindeeplearningmodelsbyhand,”
[32] S.Saha,F.Bovolo,andL.Bruzzone,“Changedetectioninimagetime- 2019,[Online].Available:https://towardsdatascience.com/counting-no-
series using unsupervised LSTM,” IEEE Geosci. Remote Sens. Lett., of-parameters-in-deep-learning-models-by-hand-8f1716241889
vol.19,2022,Art.no.8005205. [58] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
[33] Y.Lee,C.Park,N.Kim,J.Ahn,andJ.Jeong,“LSTM-autoencoderbased versionNumber:9,2014.[Online].Available:https://arxiv.org/abs/1412.
anomalydetectionusingvibrationdataofwindturbines,”Sensors,vol.24, 6980
no.9,2024,Art.no.2833.[Online].Available:https://www.mdpi.com/ [59] K.Otsu,M.Pla,A.Duane,A.Cardil,andL.Brotons,“Estimatingthe
1424-8220/24/9/2833 thresholdofdetectionontreecrowndefoliationusingvegetationindices
[34] P. Liu, X. Sun, Y. Han, Z. He, W. Zhang, and C. Wu, “Ar- fromUASmultispectralimagery,”Drones,vol.3,no.4,pp.80–103,2019.
rhythmia classification of LSTM autoencoder based on time series [60] G. Goldbergs and E. M. Upenieks, “Hierarchical integration of UAS
anomaly detection,” Biomed. Signal Process. Control, vol. 71, 2022, and sentinel-2 imagery for spruce bark beetle grey-attack detection by
Art. no. 103228. [Online]. Available: https://linkinghub.elsevier.com/ vegetation index thresholding approach,” Forests, vol. 15, no. 4, 2024,
retrieve/pii/S1746809421008259 Art.no.644.

22316 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.18,2025
[61] O.Brovkina,E.Cienciala,P.Surový,andP.Janata,“Unmannedaerial JakobWernickereceivedthePh.Ddegreeinphysi-
vehicles (UAV) for assessment of qualitative classification of Norway calgeographyfromtheFriedrichAlexanderUniver-
spruceintemperateforeststands,”Geo-SpatialInf.Sci.,vol.21,no.1, sityofErlangen-Nuremberg,Erlangen,Germany,in
pp.12–20,2018. 2017.
[62] A.MarxandB.Kleinschmit,“SensitivityanalysisofRapidEyespectral HeistheheadoftheDepartmentforDigitalForest
bandsandderivedvegetationindicesforinsectdefoliationdetectionin Information Systems of the Forestry Research and
purescotspinestands,”iForest-BiogeosciencesForestry,vol.10,no.4, Competence Centre ThüringenForst AöR. In 2018,
pp.659–668,2017. hejoinedThüringenForstAöRwiththeDepartment
[63] P.Rahimzadeh-Bajgiran,A.Weiskittel,D.Kneeshaw,andD.MacLean, forClimateImpact,ResearchandAppliedSciences
“Detectionofannualsprucebudwormdefoliationandseverityclassifica- asafull-timeResearcherandbecameconsultantfor
tionusinglandsatimagery,”Forests,vol.9,no.6,2018,Art.no.357. ForestryRemoteSensingin2023.
[64] M. Kautz, F. J. Peter, L. Harms, S. Kammen, and H. Delb, “Patterns,
driversanddetectabilityofinfestationsymptomsfollowingattacksbythe
Europeansprucebarkbeetle,”J.PestSci.,vol.96,no.1,pp.403–414,
2023.
[65] D. Powers, “Evaluation: From precision, recall and f-factor to ROC,
informedness,markedness&correlation,”Mach.-Learn.Technol.,vol.2,
pp.37–63,2011.
[66] S.Jamali,P.-O.Olsson,M.Müller,andA.Ghorbanian,“Kernel-based PawanjeetSinghDattareceivedthM.Sc.inforestry
earlydetectionofforestbarkbeetleattackusingvegetationindicestime (EconomicsandManagement)fromtheForestRe-
seriesofsentinel-2,”IEEEJ.Sel.TopicsAppl.EarthObserv.RemoteSens., search Institute, Dehradun, India, in 2002, and the
vol.17,pp.12868–12877,2024. Ph.D.degreeinenvironmentalscienceasaDAAD
[67] A.Trubinetal.,“Detectionofgreenattackandbarkbeetlesusceptibility scholar from the University of Freiburg, Freiburg,
inNorwayspruce:UtilizingPlanetScopemultispectralimageryfortri- Germany,in2012.
stagespectralseparabilityanalysis,”ForestEcol.Manage.,vol.560,2024, Hisdoctoralresearchfocusedonsoilerosionmod-
Art.no.121838. elingintheLesserHimalayas,bridgingGIS,remote
[68] H.W.Gausman,J.J.Burke,andJ.E.Quisenberry,UseofLeafOptical sensing,soilscienceandphysicalgeography.From
PropertiesinPlantStressResearch(ACSSymposiumSeries).Washing- 2012 to 2023, he was affiliated with the Chair of
ton,DC,USA:AmericanChemicalSociety,1984,no.257,pp.215–233. RemoteSensingandLandscapeInformationSystems
[69] P. Washaya, R. Modlinger, D. Tyšer, and T. Hlásny, “Patterns and with the University of Freiburg, where he worked as a Senior Scientist and
impacts of an unprecedented outbreak of bark beetles in central Eu- Assistant,contributingtoteaching,researchandstudentsupervisioninremote
rope: A glimpse into the future?,” Forest Ecosyst., vol. 11, 2024, sensing,GIS,andenvironmentalmodeling.HeiscurrentlyworkingasRemote
Art. no. 100243. [Online]. Available: https://linkinghub.elsevier.com/ Sensing Expert with the Department of Digital Forest Information Systems,
retrieve/pii/S2197562024000794 ForestResearchandCompetenceCentreoftheThüringenForst,Germany,where
[70] J.Gohli,P.Krokene,E.S.FloHeggem,andB.Økland,“Climaticand hisresearchfocusesonremotesensingbasedforestdisturbancemonitoring.He
management-related drivers of endemic European spruce bark beetle iscurrentlyengagedintheForstEOproject.
populationsinborealforests,”J.Appl.Ecol.,vol.61,no.4,pp.809–820,
2024. [Online]. Available: https://besjournals.onlinelibrary.wiley.com/
doi/10.1111/1365-2664.14606
[71] A. Karpov, N. Pirtskhalava-Karpova, A. Trubin, P. Mezei, M. Potterf,
andR.Jakuš,“Infestationpatternsoftwobarkbeetlespeciesinmulti-
speciesconiferousforestsonkunashirislandinnorthpacificoceanregion,”
ForestEcol.Manage.,vol.558,2024,Art.no.121774.[Online].Available:
https://linkinghub.elsevier.com/retrieve/pii/S0378112724000860 ChristinePreisachreceivedthePh.D.degreeinma-
[72] M.Sundararajan,A.Taly,andQ.Yan,“Axiomaticattributionfordeep chine learning from the University of Hildesheim
networks,”versionNumber:2.[Online].Available:https://arxiv.org/abs/ in 2010, after completing her studies in computer
1703.01365 science with the University of Freiburg, Breisgau,
Germany.
Afterward,sheheldvariouspositionsatSAPSE,
mostrecentlyservingasVicePresidentofDataSci-
ence in IoT, where she led an international team
andspecializedinpredictivemaintenance.Shesub-
Maximilian Kirsch received the B.Sc. degree in
sequentlybecameHeadofAdvancedAnalyticsand
forestryandenvironmentalstudiesfromtheUniver-
ChiefDataOfficeratAllianzLebensversicherungs-
sityofFreiburg,Breisgau,Germany,in2022,andthe
AG.Since2021,shehasbeenaProfessorofDataScienceandComputerScience
M.Sc.degreeingeomaticsfromKarlsruheUniversity
withKarlsruheUniversityofAppliedSciences,Germany,whereherresearch
ofAppliedSciences,Karlsruhe,Germany,in2024.
focusesonartificialintelligenceandsustainability.
HeiscurrentlyworkingtowardthePh.D.degreein
Dr.PreisachwasarecipientoftheKarlsruheUniversityofAppliedSciences
data science with Karlsruhe University of Applied
ResearchAwardforherworkontheuseofartificialintelligencefortheenergy
Sciences, where his research focuses on anomaly
transition.
detectionforforesthealth.
Hisresearchinterestsincludetime-seriesanomaly
detection,machinelearning,andremotesensing.