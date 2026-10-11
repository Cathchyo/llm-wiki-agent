---
title: "Continuous monitoring of land disturbance based on Landsat time series"
publication_date: "2019-03-13"
publication_date_precision: "day"
publication_date_basis: "first_online"
journal_issue_year: 2020
doi: "10.1016/j.rse.2019.03.009"
source_pdf: "tmp/ccdc/Continuous monitoring of land disturbance based on Landsat time series.pdf"
source_pdf_pages: 18
converter: "MarkItDown 0.1.5 [pdf]"
date_reference: "原 PDF 首页 Available online"
source_note: "原 PDF 包含主论文及末尾更正页；日期前缀采用主论文首次在线发表日期，更正页一并保留。"
---

# Continuous monitoring of land disturbance based on Landsat time series

i An update to this article is included at the end
Remote Sensing of Environment 238 (2020) 111116
ContentslistsavailableatScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Continuous monitoring of land disturbance based on Landsat time series
T
ZheZhua,b,⁎ ,JunxueZhanga,b,ZhiqiangYangc,AmalH.Aljaddanib,WarrenB.Cohend,e,ShiQiub,
Congliang Zhoub
aDepartmentofNaturalResourcesandtheEnvironment,UniversityofConnecticut,Storrs,CT06269,UnitedStates
bDepartmentofGeosciences,MS1053,ScienceBuilding125,TexasTechUniversity,Lubbock,TX79409,UnitedStates
cUSDAForestService,RMRSResearchStation,50725thStreet,Ogden,UT84401,UnitedStates
dDepartmentofForestEcosystemsandSociety,OregonStateUniversity,Corvallis,OR97331,UnitedStates
ePacificNorthwestResearchStation,U.S.ForestService,Corvallis,OR97331,UnitedStates
ARTICLE INFO ABSTRACT
Keywords: We developed a new algorithm for COntinuous monitoring of Land Disturbance (COLD) using Landsat time
COLD series.COLDcandetectmanykindsoflanddisturbancecontinuouslyasnewimagesarecollectedandprovide
Landdisturbance historicallanddisturbancemapsretrospectively.Tobetterdetectlanddisturbance,wetesteddifferentkindsof
Changedetection inputdataandexploredmanytimeseriesanalysistechniques.Wehaveseveralmajorobservationsasfollows.
Timeseries
First, time series of surface reflectance provides much better detection results than time series of Top-Of-
Landsat
Atmosphere(TOA)reflectance,andwithsomeadjustmentstothetemporaldensity,timeseriesfromLandsat
Nearreal-time
AnalysisReadyData(ARD)isbetterthanitisfromthesameLandsatscene.Second,thecombineduseofspectral
bandsisalwaysbetterthanusingasinglespectralbandorindex,andifalltheessentialspectralbandshavebeen
employed,theinclusionofotherindicesdoesnotfurtherimprovethealgorithmperformance.Third,there-
mainingoutliersinthetimeseriescanberemovedbasedontheirdeviationfrommodelpredictedvaluesbased
onprobability-basedthresholdsderivedfromnormalorchi-squareddistributions.Fourth,modelinitializationis
pivotalformonitoringlanddisturbance,andagoodinitializationstabilitytestcaninfluencealgorithmperfor-
mancesubstantially.Fifth,timeseriesmodelestimationwitheightcoefficientsmodel,updatedforeverysingle
observation,basedonallavailableclearobservationsachievesthebestresult.Sixth,achangeprobabilityof0.99
(chi-squared distribution) with six consecutive anomaly observations and a mean included angle<45° to
confirmachangeprovidethebestresults,andthecombineduseoftemporally-adjustedRootMeanSquareError
(RMSE)andminimumRMSEisrecommended.Finally,spectralchanges(or“breaks”)contributedfromvege-
tationregrowthshouldbeexcludedfromlanddisturbancemaps.TheCOLDalgorithmwasdevelopedandca-
libratedbasedonalltheselessonslearnedabove.TheaccuracyassessmentshowsthatCOLDresultswereac-
curatefordetectinglanddisturbance,withanomissionerrorof27%andacommissionerrorof28%.
1. Introduction even including tundra in Alaska (Hu et al., 2010; Mack et al., 2011;
Racine et al., 2004). The hurricane activity in recent years also in-
Landdisturbancessuchasstress,wind,hydrology,debris,harvest, creaseddramaticallyintheAtlantic(Goldenbergetal.,2001;Saunders
mechanical,and fire,occurontheEarth's surfacewithhightemporal and Lea, 2008), with an increasing destructiveness trend (Emanuel,
andspatialvariability(Cohenetal.,2016;Grimmetal.,2008;Grogan 2005). Beetle infestation has been more severe and extensive than in
etal.,2015;Hansenetal.,2013;Kennedyetal.,2015;Mildrexleretal., the past for forests located at higher elevations in western North
2009; Senf et al., 2015; Turner, 2010). It is a key component of eco- America, which has changed the forest fragmentation patterns and
logical systems that affects terrestrial ecosystem at a wide range of carbon budgets significantly (Coops et al., 2010; Hicke et al., 2012;
scales. The spatial and temporal patterns of land disturbances are Meigs et al., 2015). Mechanical disturbances caused by human activ-
changing rapidly. For example, large fires are occurring more fre- ities, such as deforestation, reforestation/afforestation, agricultural
quently in many parts of the world (Kasischke and Turetsky, 2006; expansion/intensification, and urbanization, are increasing at an un-
Marlon et al., 2009; Westerling et al., 2006; Westerling et al., 2011), precedentedrate,whichaccountedfor60%ofalllandchanges(Song
⁎Correspondingauthorat:DepartmentofNaturalResourcesandtheEnvironment,UniversityofConnecticut,Storrs,CT06269,UnitedStates.
E-mailaddress:zhe@uconn.edu(Z.Zhu).
https://doi.org/10.1016/j.rse.2019.03.009
Received3November2018;Receivedinrevisedform28February2019;Accepted6March2019
Available online 13 March 2019
0034-4257/ © 2019 Elsevier Inc. All rights reserved.

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
et al.,2018). Ontheotherhand,landdisturbancescausedby natural et al., 2018). However, there is no comprehensive study on which
disastersthreatenhumanlife,property,andcanhavestaggeringeffects band/index or selections of bands/indices work best for disturbance
onhumanwell-beingandeconomiccosts.Between1980and2004,a detection algorithms that do not rely on training and classification.
total of two million people were killed by around 7000 natural dis- Therefore,itisofhighinterestandimportancetoexplorewhatkindof
asters,andthedirecteconomicdamagefromthesenaturaldisastersis input data (TOA reflectance vs. SR), which variable or selection of
estimatedaround1trilliondollars(Stromberg,2007). variable,andwhattemporalfrequency(ARDvs.thesamescene)would
Landdisturbancehasbeendefinedvariously.Here,wedefineland providethebestlanddisturbancedetectionresults.
disturbanceasanydiscreteeventthatoccursoutsidetherangeofnat- In this study, we describe a COntinuous monitoring of Land
ural variability of land surface. Both abrupt changes such as harvest, Disturbance(COLD)algorithmthatisdevelopedupontheContinuous
mechanical,hydrology,fire,wind,andgradualchanges(orstress),such Change Detection and Classification (CCDC) algorithm (Zhu and
as disease, insects, drought are our targeted land disturbance types. Woodcock, 2014b; Zhu et al., 2015b; Zhu et al., 2016), with the ob-
Unlikemostoftheotherstudiesthatassumealllanddisturbanceswill jectiveofprovidinglarge-scale,continuous,andaccuratedetectionof
haveanimpactofreducedvegetation(Cohenetal.,2018;Healeyetal., land disturbance with Landsat time series. Specifically, we will (i)
2018; Milesi etal.,2003), wedo nothavethis assumptioninourde- identify the best time series input for detecting land disturbance; (ii)
finition. This is because some of the land disturbances, such as me- develop and calibrate the land disturbance detection algorithm based
chanicalchanges,wind,hydrology,andfireinnon-vegetatedareas,do onawell-interpretedreferencedataset;and(iii)remove“breaks”that
not necessarily reduce vegetation volume. Moreover, regular agri- aredisturbanceirrelevant.
cultural practice is not defined as land disturbance, unless it is trans-
formedtosomeotherlanduseandlandcovertypesorhasundergone 2. Studyareaanddata
certainkindsofnonerepeatedagriculturalactivities,suchaschanging
croptypeorlyingfallow. 2.1. Studyarea
Manyalgorithmshavebeendevelopedformonitoringlandchange
basedonremotelysensedimagery(Franklinetal.,2015;Hansenand Ourstudyareaincludesatotalof180ThiessenSceneAreas(TSAs)
Loveland, 2012; Huang et al., 2018; Zhu and Woodcock, 2014b), but that are defined as the non-overlapping portions of individual frames
most of them are only focusing on land cover and land use change (Kennedy et al., 2010). These 180 TSAs are selected from 442 TSAs
(target of change), with very few studies on disturbance (agent of coveringthe conterminousUSbased ona stratifiedsamplingstrategy
change) (Zhu,2017).Moreover,almostall disturbancestudiesarefo- designedforselectingahigherproportionofTSAsfromforestedareas
cused on forest disturbance (Cohen et al., 2016; Grogan et al., 2015; (Fig. 1) (Cohen et al., 2016). Admittedly, our study areas are more
Hansenetal.,2016;Xinetal.,2013;Zhuetal.,2012),withverylimited forest-oriented,butconsideringthelargeamountsofforestdisturbance
knowledge ondisturbances that occur onnon-forested areas.Another intheUS,itislessofanissue.Actually,ifwecalculatethelandcover
majorissueisthatmostofthesealgorithmsdonothavethecapability area proportions of all 180 TSAs based on the 2006 National Land
ofmonitoring disturbanceinacontinuousmode,andthedisturbance Cover Database (NLCD) cover map (Fry et al., 2011), forest ac-
information derived from these algorithms is less helpful to resource counts<40% of the land areas, with other>60% of land that are
managersandpolicymakers. coveredbyagriculture,shrubland,herbaceous,wetland,water,devel-
Recently,aContinuousChangeDetectionandClassification(CCDC; oped, and barren land. Another reason for picking these TSAs as our
ZhuandWoodcock,2014b)algorithmhasbeendevelopedtomonitor studyareaisbecauseatotalof7200Landsatreferencesamplesacross
landcoverchangeusingallavailableLandsatdata.TheCCDCalgorithm all land types have already been interpreted by experts from United
can detecta variety of land cover and landuse changescontinuously StatesForestService(USFS)toestimateforestdisturbance(Cohenetal.,
with high spatial and temporal accuracies (Pengra et al., 2016; Zhu, 2016).Accordingtoourknowledge,thisistheonlypubliclyavailable
2017), but is reported to have relatively low producer's accuracy for dataset that provides a high spatial resolution (30-meter) disturbance
identifying forest disturbance withrelatively small change magnitude informationatanannualtimescaleforarelativelylargearea.
(Cohen et al., 2017). The CCDC algorithm was originally designed to
detect land cover and land use changes that usually result in a large 2.2. Referencedata
changemagnitude.However,forforestdisturbanceswithsubtlespec-
tral change (usually still the same forest cover type after the dis- Within each of the 180 TSAs, 40 Landsat plots (30-meter Landsat
turbance),suchasbeetleinfestationandselectivelogging,CCDCisless pixels)wereselectedbasedonasimplerandomstrategy,andasample
helpful.Ontheotherhand,manyofthechanges(or“breaks”)detected sizeof7200Landsatplotshavebeenselectedasourreferencedata,in
by CCDC do not necessarily correspond to land disturbances. For ex- which over half of them are non-forested and have been fully inter-
ample,CCDCidentifiesabreakifitdeviatesfromitspredictedstatis- pretedforcoverandchange.Thesedatasetswerepreviouslyinterpreted
ticalintervals,butforbreakscausedbygradualconditionchanges,such for estimating forest disturbance based on the Landsat time series vi-
as vegetation regrowth, there is no disturbance event associated with sualization and disturbance data collection software — TimeSync
them.Thiskindoferrorreducestheuser'saccuracyoflanddisturbance (Cohen et al., 2010). This tool provides a series of “image chips” (a
substantially. subsetofimages)aroundaLandsatplotofinterest(30-metersquare),as
Additionally, though most of the disturbance mapping algorithms wellasthetimeseriesgraphicalplots,ortemporaltrajectoriestohelp
werebasedonSurfaceReflectance(SR),thereweresomestudiesthat with interpreting the occurrence of disturbance. Both spectral bands
used Top-Of-Atmosphere (TOA) reflectance as well (Hansen et al., andavarietyofindicescanbeusedtovieworplotforthetimeseries
2013;Potapovetal.,2012).Accordingtoourknowledge,nocompre- and the “image chips”. For each disturbance event, the causal agent
hensive study compares the performance of TOA reflectance and SR classes such as Harvest, Fire, Stress, Wind, Mechanical, Hydrology, and
timeseriesformappinglanddisturbance.Moreover,theUnitedStates Other (Fig. 2B) were interpreted in TimeSync with help from Google
GeologicalSurvey(USGS)hasreleasedtheLandsatAnalysisReadyData Earth high spatial resolution images and a variety of ancillary data.
(ARD) for facilitating time series analysis (Dwyer et al., 2018). The Cohenetal.(2016)haveanalyzedthedisturbancemagnitudeforthis
LandsatARDcanprovidedensertimeseriesobservationsfor“side-lap” reference data, in which majority of the disturbances have relative
regionslocatedbetweenoverlappingLandsatscenesthanobservations spectralchangeslessthan50%,andtheaccumulatedtreecoverchanges
fromthesameLandsatscene.Finally,recentstudiesdemonstratedthat fromthesedisturbancesaregenerallylowerthan50%.
theuseofmultiplespectralbandsandindicescouldprovidemoreac- TheLandsatplotswereinterpretedforeachyear,andatimerange
curate forest disturbance results from a supervised classifier (Cohen was provided for each observed disturbance. For example, if a
2

| Z.Zhu,etal. |     |     |     |     |     |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
Fig.1.Studyarea(whitepolygons)andthe7200referencesamples(blackdots),showninthecontextofthe2006NationalLandCoverDatabase(NLCD)covermap.
disturbance is detected in the 2000 growing season image, but not sky observations (<24), have large gaps (more than three years
showingupinthepreviousyear,TimeSyncwilllabeladisturbancewith without any observations), or difficult to interpret were eliminated
atimerangebetween1999and2000.InCohenetal.(2016),onlythe fromthereferenceplots.Therefore,atotalof6634Landsatplotswere
later year (e.g., 2000) was given as the disturbance year, as it is im- usedasthereferencesamplesforthisstudy.
| possible to     | know | the exact   | year | of disturbance | based       | on  | the time in- |     |     |     |     |     |     |     |
| --------------- | ---- | ----------- | ---- | -------------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| terval provided |      | in TimeSync | and  | the higher     | possibility |     | that a dis-  |     |     |     |     |     |     |     |
2.3. LandsattimeseriesfromthesamesceneandAnalysisReadyData
turbancewilloccurbeforeandduringthegrowingseasonthanafterthe
(ARD)
growingseason.However,wefoundsomeproportionsofdisturbances
| occurred | after the | growing | season | (e.g., between |     | July 1999 | and De- |           |            |           |             |     |             |        |
| -------- | --------- | ------- | ------ | -------------- | --- | --------- | ------- | --------- | ---------- | --------- | ----------- | --- | ----------- | ------ |
|          |           |         |        |                |     |           |         | Recently, | USGS Earth | Resources | Observation |     | and Science | (EROS) |
cember1999),andifthelateryearisusedasthedisturbanceyear,the
|                     |     |      |         |          |       |          |             | Center reorganized | Landsat | data | into a | formal | tiered data | Collection |
| ------------------- | --- | ---- | ------- | -------- | ----- | -------- | ----------- | ------------------ | ------- | ---- | ------ | ------ | ----------- | ---------- |
| labeled disturbance |     | year | will be | one year | later | than the | actual dis- |                    |         |      |        |        |             |            |
structure,inwhichLandsatCollection1productsarecategorizedintoa
turbanceyear,whichwillartificiallyincreasebothomissionandcom-
|                |     |          |        |             |     |                |     | consistent | archive of known | data | quality, | such    | as Tier | 1, Tier 2, and |
| -------------- | --- | -------- | ------ | ----------- | --- | -------------- | --- | ---------- | ---------------- | ---- | -------- | ------- | ------- | -------------- |
| mission errors | (a  | one-year | offset | was allowed | for | the comparison | in  |            |                  |      |          |         |         |                |
|                |     |          |        |             |     |                |     | Real-Time. | Tier 1 images    | from | Landsats | 4–8 and | Tier    | 2 images from  |
Cohenetal.(2016)toreducethisimpact).Therefore,inthisstudy,we
|     |     |     |     |     |     |     |     | Landsat 8 | are reported | to have | high geometry |     | accuracy, | and both of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------- | ------------- | --- | --------- | ----------- |
donotgiveasingledisturbanceyear.Instead,wekeepthetimeinterval
themareusedtocreateLandsatARDfortheconterminousUS,Alaska,
foreachdisturbanceeventfortrainingandvalidationpurposes.Mostof
|     |     |     |     |     |     |     |     | and Hawaii | (Dwyer et | al., 2018). | Landsat | ARD | are consistently | pro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | ------- | --- | ---------------- | ---- |
thedisturbancesoccurbetweentwoconsecutiveyears(e.g.,fire,wind,
|     |     |     |     |     |     |     |     | cessed to | the highest scientific |     | standards | and | level of | processing re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------- | --- | --------- | --- | -------- | -------------- |
harvest,mechanical,andhydrology),andsomeofthemulti-yearpro-
|     |     |     |     |     |     |     |     | quired for | time series analysis, |     | in which | compared | with | Landsat Col- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | -------- | -------- | ---- | ------------ |
cessdisturbances(mostlystress)suchasinsectinfestationanddrought
lection1datafromthesamescene,densertimeseriesobservationsare
canhavelongertimeintervals.
|               |     |         |            |       |        |        |             | expected | for places in | the adjacent | Landsat | orbit | swath | overlap areas |
| ------------- | --- | ------- | ---------- | ----- | ------ | ------ | ----------- | -------- | ------------- | ------------ | ------- | ----- | ----- | ------------- |
| The reference |     | Landsat | plots from | Cohen | et al. | (2016) | are of high |          |               |              |         |       |       |               |
(Qiuetal.,2019).
| quality.However,wehaveobserved |     |     |     | twoproblemsforusing |     |     | themdi- |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Inthisstudy,wecomparedfourkindsoftimeseriesobservationsfor
| rectly for | detecting | land | disturbance. | First, | though | this reference | da- |            |                   |     |           |                 |     |              |
| ---------- | --------- | ---- | ------------ | ------ | ------ | -------------- | --- | ---------- | ----------------- | --- | --------- | --------------- | --- | ------------ |
|            |           |      |              |        |        |                |     | monitoring | land disturbance, |     | including | TOA reflectance |     | Collection 1 |
tasetistryingtorecordalllanddisturbancetypesinbothforestedand
datafromthesameLandsatscene(Scene-TOA),TOAreflectancefrom
| non-forested   | areas,      | it is less | accurate     | for | non-forested     | areas. | This is  |                |               |     |           |          |           |               |
| -------------- | ----------- | ---------- | ------------ | --- | ---------------- | ------ | -------- | -------------- | ------------- | --- | --------- | -------- | --------- | ------------- |
|                |             |            |              |     |                  |        |          | ARD (ARD-TOA), | SR Collection |     | 1 data    | from the | same      | Landsat scene |
| understandable | considering |            | the majority | of  | the interpreters |        | are from |                |               |     |           |          |           |               |
|                |             |            |              |     |                  |        |          | (Scene-SR),    | and SR from   | ARD | (ARD-SR). | All      | available | Landsat data  |
USFS.Second,wefoundthisreferencedatasetistoosensitivetorecord
wereusedastheinputforbothsamesceneCollection1dataandARD
forestdisturbance,assomeofthedisturbancesrecordedhavenosignal
|            |             |     |      |              |        |     |             | data (including | images       | with 100% | cloud | cover).   | We have | used seven   |
| ---------- | ----------- | --- | ---- | ------------ | ------ | --- | ----------- | --------------- | ------------ | --------- | ----- | --------- | ------- | ------------ |
| in Landsat | data(cannot | see | them | in the“image | chips” | or  | in the time |                 |              |           |       |           |         |              |
|            |             |     |      |              |        |     |             | major spectral  | bands within | Landsats  | 4–8,  | including | the     | Blue, Green, |
seriesplot).Therefore,wehavefiveremotesensingexpertslookedatall
Red,NearInfrared(NIR),Short-waveInfrared1(SWIR1),SWIR2,and
7200plotsinbothTimeSyncandGoogleEarthandcorrectedtheseis-
|             |           |          |            |     |         |           |         | Thermal    | Infrared (TIR) | bands. | Note that    | we extracted |           | all Landsat ob- |
| ----------- | --------- | -------- | ---------- | --- | ------- | --------- | ------- | ---------- | -------------- | ------ | ------------ | ------------ | --------- | --------------- |
| sues in the | reference | dataset. | Basically, | we  | labeled | all kinds | of land |            |                |        |              |              |           |                 |
|             |           |          |            |     |         |           |         | servations | directly from  | Google | Earth Engine |              | (Gorelick | et al., 2017),  |
disturbancesinthetimeseries,butdisturbancesthatwereinvisiblein
andastheUSGSLandsatARDarenotincludedinthecurrentGoogle
| Landsat data     | (time     | series | plot or   | “image chips”) | were   | changed     | to the |                |                |          |                |     |            |             |
| ---------------- | --------- | ------ | --------- | -------------- | ------ | ----------- | ------ | -------------- | -------------- | -------- | -------------- | --- | ---------- | ----------- |
|                  |           |        |           |                |        |             |        | Earth dataset, | we reprojected |          | the Collection | 1   | data and   | created our |
| stable category. | Moreover, |        | reference | pixels         | do not | have enough | clear  |                |                |          |                |     |            |             |
|                  |           |        |           |                |        |             |        | Landsat        | ARD based on   | the same | procedure      | for | generating | the USGS    |
3

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
3.1.1. Datapreparation
Wetland Water Developed Inthedatapreparationprocess,therearethreemainsteps,which
7% 6% 6% include Fmask, initializing the model window, and Tmask (blue rec-
tangleinFig.3).First,alltheavailableLandsattimeseriesforalocation
BarrenLand are downloaded, and cloud, cloud shadow, and snow are screened
Agriculture 1% basedontheFmaskalgorithm(Zhuetal.,2015a;ZhuandWoodcock,
19% 2012) that are provided in the Quality Assessment (QA) band. In-
itializing the model window in the second step specifies the time
windowrequiredtoinitiateatimeseriesmodel,whichshouldsatisfy
A three criteria including: (i) contain greater than or equal to 12 clear
(hereafterclearreferstoobservationsthatarenotcloud,cloudshadow,
Herbaceous orsnow)observations;(ii)thetotallengthofthetimeseriesshouldbe
Forest
9% atleastoneyear;and(iii)thelargestdatagapsshouldbelessthana
36%
year. If all three criteria are met, COLD applies the Tmask algorithm
(Zhu and Woodcock, 2014a) to all observations within the initialized
Shrubland model window to exclude cloud, cloud shadow, and snow that are
16% missed in the Fmask algorithm. Note that the COLD algorithm has
modified the Tmaskalgorithm for better monitoring landdisturbance
(seeSection3.3.2.1–Tmaskmodificationfordetails).
3.1.2. Modelinitialization
TheclearobservationsaredigestedbytheCOLDalgorithmtobuild
theinitialtimeseriesmodelforallspectralbands.Next,COLDteststhe
stabilityofthenewlyinitializedmodelstomakesurethemodelisstable
enough to detect change. See Section 3.3.3 for details on how COLD
teststhestabilityoftheinitializedmodels.Ifthemodelfailstopassthe
stabilitytest,COLDmovestothenextobservationbyincludinganew
clearobservation andremovestheearliestclear observation,andthis
process continues until the model stabilized (see the purple arrow in
Other Stress
Wind Fig.3).Finally,foreachnewlyinitializedtimeseriesmodel,itisusedas
10% 10%
1% thebasisforlookingbacktotheobservationsaheadofthetimeseries
Fire modeltomodifythestarttimeofthetimesseriesmodel.Todetermine
9% whether these observations should be included in the current model,
Mechanical
COLDusesthesamechangedetectionapproachusedinthecontinuous
16%
monitoringprocedure(seeSection3.3.5fordetails).COLDsearchesfor
allclearobservationsthatareaheadofthecurrentmodelbutarenot
B
included in previous and current time series models until it finds a
Hydrology confirmed change, or the search goes to the last observation. For ob-
4% servations that deviate substantially from model prediction but not
detected in a consecutive manner, COLD identifies them as non-dis-
turbance related ephemeral changes caused mainly by cloud, cloud
shadow,snoworsoilmoisturechanges,andareremovedinfuturetime
Harvest seriesanalysis(leftsideorangedashedarrowinFig.3andseeSection
50% 3.3.2.2 – Non-consecutive Outlier Removal for details). In this way,
COLD is able to initialize a time series model that includes all clear
observations collected earlier than the start time of the model and
followthepredictedtrajectoryofthecurrenttimeseriesmodel.Ifthere
Fig.2.Theareaproportionsofreferencedataattributionforthe180Thiessen is a change confirmed ahead of the current model and the current
SceneAreas.A:ReferencedatalandcovercategorybasedonNLCD2006;B: modelisinitializedforthefirsttimeforapixel,COLDestimatesanew
referencedatadisturbancetypebetween1985and2011.
model based on the observations before the change, and this new
model, as well as the confirmed change, is recorded in the time seg-
LandsatARDinternallyinGoogleEarthEngine(Dwyeretal.,2018). mentsdatabaseasdescribedinTable1.Otherwise,COLDwillusethe
current time series model to monitor land disturbance which is de-
scribedinthenextsection.
3. Methods
3.1.3. Continuousmonitoring
3.1. TheCOLDalgorithm In the continuous monitoring process, there are five major steps
including updating model, looking forward, detecting change, re-
TheCCDCalgorithmworkswellfordetectinglandcoverandland cordingtimesegments,andextractingdisturbance.First,allthenewly
usechanges(ZhuandWoodcock,2014b),butforlanddisturbancewith collected clear observations will be used to update the current time
smallchangemagnitude,ithaslargecommissionerrors(Healeyetal., seriesmodelforbetterpredictingfutureobservations.Thetimeseries
2018).TheCOLDalgorithmisdevelopedbasedonZhuandWoodcock model contains three sets of harmonic components with different
(2014b)andZhuetal.(2015b)butimprovedandcalibratedtobetter temporalfrequencies,whicharetriggeredbythenumberofavailable
monitor all kinds of land disturbance. It consists of three major pro- clearobservations(Eq.(1)).Basically,themoreclearobservations,the
cesses,includingdatapreparation,modelinitialization,andcontinuous higherfrequenciesofharmoniccomponentswillbeincluded(Zhuetal.,
monitoring(Fig.3). 2015b). For clear observations between 12 and 17 (k=1), the four
4

| Z.Zhu,etal. |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |                           |                     |     |
| ----------- | --- | --- | --- | --- | --- | ----------------------------------------------- | ------------------------- | ------------------- | --- |
|             |     |     |     |     |     | Fig. 3.The                                      | process chain of          | the COLD algorithm. |     |
|             |     |     |     |     |     | The blue,                                       | red, and green rectangles | represent           | the |
LandsatTimeSeries
|     |     |     |     |     |     | data preparation,                              | model initialization, | and | con- |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --------------------- | --- | ---- |
|     |     |     | No  |     |     | tinuousmonitoringprocessrespectively.Thedashed |                       |     |      |
Con nuousMonitoring
|     |       |     |     |     |     | orange arrows                                | represent the | process of include | or  |
| --- | ----- | --- | --- | --- | --- | -------------------------------------------- | ------------- | ------------------ | --- |
|     | Fmask |     |     |     |     | excludesinglenewobservationforupdatedmodels. |               |                    |     |
Thepurplearrowpresentstheprocessofmovingto
UpdateModel
|     |     |     |     |     |     | the next observation | by including | a new clear | ob- |
| --- | --- | --- | --- | --- | --- | -------------------- | ------------ | ----------- | --- |
Ini alizeModel servationandremovestheearliestclearobservation
|     | Window |     |     |             |     | intheinitializedmodelwindow.(Forinterpretation |     |     |     |
| --- | ------ | --- | --- | ----------- | --- | ---------------------------------------------- | --- | --- | --- |
|     |        |     |     | LookForward |     | ofthereferencestocolorinthisfigurelegend,the   |     |     |     |
readerisreferredtothewebversionofthisarticle.)
Tmask
DetectChange
|     | BuildIni alModel |     | No  |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ChangeConfirmed
No
|     | CheckStability |     |     |     | Yes |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Yes
FirstModel&
|     | Yes |     |     | RecordTimeSegments |     |     |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ChangeConfirmed
LookBack
ExtractDisturbance
DetectStartTime
No
LastObserva on?
| No  |     | Yes |     |     | Yes |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ChangeConfirmed
|     | orLastObserva on |     |     | End |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
coefficientsmodelisused.Forclearobservationsbetween18and23, Fig. 3). Otherwise, if the change is observed consecutively, it is con-
thesixcoefficientsmodelisused(k=2),andeightcoefficientsmodel firmed(seeSection3.3.5fordetails).Inthefourthstep,allthespectral
isusedformodelswithgreaterthanorequalto24clearobservations andtemporalinformationcreatedforeachtimesegmentisrecordedin
(k=3).Thereasonforpickingamaximumofeightcoefficientsisex- adatastructureformat.AsinglepixelwithN“breaks”,willhaveN+1
plainedinSection3.3.4.1–Numberofcoefficients.Next,COLDlooks time segments, and for each time segment, there are a total of 77
forward to the new clear observations collected after the updated variablesrecordedindifferentfieldsasdescribedinTable1.Finally,we
model.Foreachnewlycollectedclearobservation,COLDcomparesthe canextractlanddisturbancesfromallthepreviouslydetected“breaks”
modelpredictedvalue(fromtheupdatedmodel)withtheactualclear andprogresstothelastclearobservation(seeSection3.3.6fordetails).
observationtocalculatethemagnitudeofspectralchange.Ifthechange 3 2 2
|     |     |     |     |     | =a + | a cos x | +b sin x | +c x |     |
| --- | --- | --- | --- | --- | ---- | ------- | -------- | ---- | --- |
magnitude is within the expected range, the next observation is con- i,x 0,i k=1 k,i T k,i T 1,i
(1)
sideredstableandisusedtoupdatethetimeseriesmodeliteratively.In
| Section3.3.4.2–Updatefrequency,wewilldiscussthedetailsonthe |                     |            |                  |          | where, |     |     |     |     |
| ----------------------------------------------------------- | ------------------- | ---------- | ---------------- | -------- | ------ | --- | --- | --- | --- |
| optimal way                                                 | for model updating. | Similarly, | for observations | that de- |        |     |     |     |     |
viate substantially from model prediction but not detected in a con- x:Juliandate
secutive manner (for both magnitude and direction), COLD identifies i:TheithLandsatBand(i=1,2,3,4,5,and7)
them as non-disturbance related ephemeral changes, and they are re- k:Temporalfrequencyofharmoniccomponent(k=1,2,and3)
movedinfuturetimeseriesanalysis(rightsideorangedashedarrowin T:Numberofdaysperyear(T=365.25)
Table1
VariablesrecordedineachCOLDtimesegment.
| Variablename | Size(rows×cols) | Descriptions                        |     |     |     |     |     |     |     |
| ------------ | --------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| t_start      | 1               | Datewhenthetimeseriesmodelstarts.   |     |     |     |     |     |     |     |
| t_end        | 1               | Datewhenthetimeseriesmodelends.     |     |     |     |     |     |     |     |
| t_break      | 1               | Datewhenthefirst“break”isidentified |     |     |     |     |     |     |     |
coefs 56(8×7) Coefficientsforeachtimeseriesmodel(8coefficients)foreachspectralband(7bands)
rmse 7(7×1) Rootmeansquareerrorfromthemodelfitforeachspectralband(7bands)
| pos | 1   | Positionofeachtimeseriesmodel(x/ylocationinthestackedimages) |     |     |     |     |     |     |     |
| --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
change_prob 1 Changeprobability(0–1).ChangeprobabilityequalstothenumberofconsecutiveanomalyobservationsdividedbyN(N:numberof
consecutiveanomalyobservationstoconfirmachange)
| num_obs | 1   | Numberofclearobservationsusedformodelestimation |     |     |     |     |     |     |     |
| ------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
category 1 Qualityofthemodelestimation,wherethetensdigitspecifieswhatmodelfitprocedureisused(e.g.,5:aperennialsnowpixel,4:Fmask
failed,3:areservedvalue,2:modelfitsattheend,1:modelfitsatthebeginning,and0:normalprocedureformodelfit)andtheunitdigit
specifieswhatmodelisused(e.g.,4,6,and8:modelswith4,6,and8coefficientsrespectively).
magnitude 7(7×1) Magnitudeofspectralbanddifferencesbetweenmodelpredictionandobservationforeachspectralband(7bands).
5

| Z.Zhu,etal. |     |     |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
a0,i:CoefficientforoverallvaluefortheithLandsatBand provided a full comparison between COLD and CCDC in all these as-
ak, i, bk, i: Coefficients for intra-annual change for the ith Landsat pectsinTable2.NotethatthoughCCDChasmultipleversionsreleased
Band at different placesonline, there is only onepaper that well-explained
c1,i:Coefficientforinter-annualchange(slope)fortheithLandsat thealgorithmintheliterature(ZhuandWoodcock,2014b).Therefore,
| Band                 |             |                     |                  |      | wemainlycomparedCOLDwiththisversionofCCDC. |     |     |     |     |     |     |     |
| -------------------- | ----------- | ------------------- | ---------------- | ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| i,x: Surface         | reflectance | for the ith Landsat | Band at x Julian | date |                                            |     |     |     |     |     |     |     |
| frommodelprediction. |             |                     |                  |      | 3.3.1. Inputdata                           |     |     |     |     |     |     |     |
Weexploredthreesciencequestionsregardingwhatisthebestinput
3.2. Algorithmperformanceevaluationmetrics data for monitoring land disturbance: 1) ARD or same scene data; 2)
TOAorSR,and;3)whichvariableorselectionsofvariables?Tocom-
Everydisturbanceisidentifiedasanisolatedevent.Fordisturbances pensatetheinconsistencyoftemporaldensitycausedusingARDdata,
detected by COLD that are within the stable period of the reference wedevelopedanewapproachthatadjuststhechangeprobabilityand
samples, they are identified as commission errors. For disturbance thenumberofconsecutiveanomalyobservationsrequiredtoconfirma
segmentsinthereferenceplot,ifnodisturbanceisidentifiedbyCOLD, change based on the overall density of the time series (hereafter, we
|     |     |     |     |     | name it the | adjusted | approach). |     | See Section | 1.1 in | Supplementary |     |
| --- | --- | --- | --- | --- | ----------- | -------- | ---------- | --- | ----------- | ------ | ------------- | --- |
theyareidentifiedasomissionerrors.Notethattheagreementbetween
COLDdetectionandthereferencesamplesmeanstheyarecorrectnot materialsfordetails.
onlyinspacebutalsointime.Forexample,ifadisturbanceisdetected
at the time after (or before) the reference disturbance segment, both 3.3.1.1. ARDvs.scene&TOAreflectancevs.SR. Weobservedthatifno
omission and commission cases will increase by one in the confusion adjustment was made for the inconsistency of temporal density,
matrix.Theperiodbetween1985and2011(27years)wasusedforthis detection accuracy from SR was substantially higher than that from
evaluation.ConsideringtherearealmostseventhousandLandsatplots, TOAreflectance(bothARDandsamesceneimages).Anotherimportant
we have a total of approximately 189,000 evaluating cases (for each discovery is that the use of ARD (for both TOA reflectance and SR)
plotineachcalendaryear). wouldfindmorechangesthanusingimagesfromthesamescene,which
Werandomlyselected50%ofthereferencesamples(3317Landsat leadstoloweromissionerrorbuthighercommissionerror.Thiscanbe
troublesomeformonitoringlanddisturbanceusingLandsatARD,asthe
plots)foralgorithmdevelopmentandcalibration.Theremaining50%
differenceintemporaldensitybetweenoverlapandnon-overlapareas
| of the reference | samples | were used for validating | of the COLD | algo- |     |     |     |     |     |     |     |     |
| ---------------- | ------- | ------------------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
rithm. Three accuracy metrics, including omission error, commission wouldpresentinconsistentspatialpatternsinthedisturbancemaps.
error,andF1score,wereselectedforaccuracyassessment.Similaras Ontheotherhand,iftheadjustedapproachisappliedtoreducethe
Healey et al. (2018), the commission error and omission error were impactoftheinconsistencyoftemporaldensityintheinputdata,SRis
selected to evaluate the chances that stable land observations were stillbetterthanTOAreflectance.However,ARD(includingSRandTOA
falsely identified as land disturbance observations, and land dis- reflectance) with the adjusted approach demonstrate substantially
turbance observations were falsely identified stable land observations better performance than ARD without adjustment, in which the ad-
respectively(Eqs.(2)–(3)).Moreover,asweexpectedtohaveunbiased justed approach achieved the similar omission error but much lower
mapping results, algorithms with balanced omission and commission commission error (~10%). On the other hand, the adjusted approach
errorarepreferred(Healeyetal.,2018;Zhuetal.,2012).Therefore,we achievedalmostthesamedetectionaccuracyastheapproachwithout
anyadjustmentfordatafromthesamescene.Thisresultsuggeststhat
selectedtheF1score(orF-measure)asthethirdaccuracymetric(Eq.
|     |     |     |     |     | the adjustment | will | not artificially |     | change | the disturbance | detection |     |
| --- | --- | --- | --- | --- | -------------- | ---- | ---------------- | --- | ------ | --------------- | --------- | --- |
(4)),asitalsoprovidesameasureofbalancebetweenprecision(com-
mission error) and recall (omission error). For each algorithm perfor- results for the non-overlap area, and for overlap areas, the adjusted
mance evaluation, we will calculate the omission error, commission approachcandetectlanddisturbancewithevenhigheraccuracies.This
error,andF1scoreforfivedifferentchangeprobabilitythresholds(e.g., also demonstrates the importance of using dense time series, as the
0.90, 0.95, 0.99, 0.999, 0.9999). For each threshold, the locations of higher the temporal density, the better the detection of land dis-
markers are based on their omission and commission errors in the turbance. Considering the omission and commission errors were re-
omission-commissionplane,andthecolorsofthemarkersrepresentthe ducedatasimilarlevel,thespatialpatternoflanddisturbancebetween
valuesofF1score.Afterconnectingthemarkersfromthefivechange overlapandnon-overlapshouldbeverysimilar.Therefore,wewilluse
detectionthresholdsintheomission-commissionplane,thelinethatis LandsatARDSRastheinputdatatype,andtheadjustedapproachwill
closesttotheoriginandwiththehighestF1scoreisconsideredtohave beemployedatthesametime.
thebestperformances.
|     |     |     |     |     | 3.3.1.2. Variable |     | selection. | A recent | study | suggested | that | the |
| --- | --- | --- | --- | --- | ----------------- | --- | ---------- | -------- | ----- | --------- | ---- | --- |
detected disturbances disagree with reference
| commission= |     |     | ×100% |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
total number of detected disturbances combination of bands and indices works much better in detecting
(2)
forestdisturbancethanjustusingasinglevariable(Cohenetal.,2018).
reference disturbances disagree with detection Therefore,weexploredmanydifferentcombinationsofspectralbands
| omission= |     |     | ×100% |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
total number of reference disturbances andindicestodetectlanddisturbanceofallpossiblekinds.
(3)
|     |     |     |     |     | For scenarios |     | with a single | spectral | band, | the two | SWIR | bands |
| --- | --- | --- | --- | --- | ------------- | --- | ------------- | -------- | ----- | ------- | ---- | ----- |
precision×recall showedsimilar(SWIR2isslightlybetter)butmuchbetterperformance
| F1score= |     | ×200% |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precision+recall thantheotherspectralbandsifusedalone.TheRedbandwasranked
|     |                   |           |     |     | the third, | but its | performance | was | much | lower than | the two | SWIR |
| --- | ----------------- | --------- | --- | --- | ---------- | ------- | ----------- | --- | ---- | ---------- | ------- | ---- |
|     | (1 commission)×(1 | omission) |     |     |            |         |             |     |      |            |         |      |
= ×200% bands. The other spectral bands were almost useless if they are used
|     | 2 commission | omission |     | (4) |     |     |     |     |     |     |     |     |
| --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alone,andtheTIR,NIR,andBluebandsarethethreevariableswiththe
|     |     |     |     |     | worst performance. |     | Another | observation | is  | that the | use of a | single |
| --- | --- | --- | --- | --- | ------------------ | --- | ------- | ----------- | --- | -------- | -------- | ------ |
3.3. COLDalgorithmdevelopmentandcalibration index, such as Normalized Difference Vegetation Index (NDVI),
|     |     |     |     |     | Normalized | Burn | Ratio (NBR), | and | Tasseled | Cap Wetness | was | not as |
| --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --- | -------- | ----------- | --- | ------ |
We explored six major components for better detecting land dis- helpfulasexpected.Forexample,theindicesthatheavilyinvolvedwith
turbance, including input data, outlier removal, model initialization, SWIRbands,suchasNBRandWetness,didnotperformaswellasjust
model fit, change detection, and disturbance extraction (Fig. 4). usingasingleSWIRband,andthewidelyusedNDVIindexperformed
Methodsandthresholdswiththebestperformanceformonitoringland similarlytotheRedband.
disturbance were selected for the COLD algorithm. We have also Forscenarioswithtwoormorespectralvariables,thecombineduse
6

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
Fig.4.Overviewofthesixcomponentsforalgorithmdevelopmentandcalibration.ARD:AnalysisReadyData;TOARef:Top-Of-AtmosphereReflectance;SR:Surface
Reflectance;CCDC:ContinuousChangeDetectionandClassification;COLD:COntinuousmonitoringofLandDisturbance;LASSO:LeastAbsoluteShrinkageand
SelectionOperator;RMSE:RootMeanSquareError.
Table2
ComparisonsofCCDCandCOLDinthesixmajorcomponentsexploredforbettermonitoringlanddisturbance.ARD:AnalysisReadyData;SR:SurfaceReflectance;
CCDC:ContinuousChangeDetectionandClassification;COLD:COntinuousmonitoringofLandDisturbance;OLS:OrdinaryLeastSquare;LASSO:LeastAbsolute
ShrinkageandSelectionOperator;RMSE:RootMeanSquareError.
|     | CCDC(ZhuandWoodcock,2014b) | COLD |
| --- | -------------------------- | ---- |
Inputdata Blue,Green,Red,NIR,SWIR1,SWIR2,andTIRSR;Landsat Green,Red,NIR,SWIR1,andSWIR2SR;LandsatARDwiththeadjustedapproach
imagesfromthesamescene
Outlierremoval 0.04TOAreflectance(Tmask);non-consecutivechange Dynamicthreshold(Tmask);non-consecutivechangeprobabilitylargerthan99.999%
largerthantheempiricalchangethreshold
| Modelinitialization | CCDCapproach | COLDapproach |
| ------------------- | ------------ | ------------ |
Modelfit 4coefficients;updatedforeverynewobservation; 8coefficients;updatedforeverysingleobservation;observationsfromallavailable
|     | observationsfromallavailablestableyears;OLSfit | stableyears;LASSOfitwithalambdaof20 |
| --- | ---------------------------------------------- | ----------------------------------- |
Changedetection 3consecutiveanomalyobservations;empiricalchange 6consecutiveanomalyobservations;achangeprobabilityof99%normalizedby
thresholdnormalizedbyRMSE temporally-adjustedRMSEandminimumRMSE;meanincludedangle<45°
| Disturbanceextraction | No  | Yes |
| --------------------- | --- | --- |
7

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
A
B
C
Fig.5.Threepossiblemodelinitializationfits.A:Changesignalinfluencedmodelinitializationfitsignificantly;B:changesignal(occurredatthestartofthemodel)
haslittleinfluenceonmodelinitializationfit,and;C:changesignalhassomedegreeofinfluenceonmodelinitializationfit.
oftheRedandNIRbandsachievedsimilarperformanceastheuseofan (Functionofmask)algorithmforallavailableLandsattimeseries(Foga
NDVIindex,andthecombineduseoftheNIRandSWIR1bandsorthe et al., 2017; Zhu et al., 2018; Zhu et al., 2015a; Zhu and Woodcock,
combined use of the Red and SWIR1 bands achieved similar perfor- 2012). Considering Fmask is not perfect and any outlier in the time
mancesastheuseofasingleSWIR1band.However,thecombineduse series can be detrimental, we also applied the Tmask (multiTemporal
oftheRed,NIR,andSWIR1bandsachievedslightlybetterperformance mask)algorithm(ZhuandWoodcock,2014a)tofurtherscreencloud,
than the use of a single SWIR1 band, and the combined use of the cloudshadow,snow,andothernon-disturbancerelatedoutliers.Asthe
Green,Red,NIR,SWIR1,andSWIR2bandsachievedbestresults(used Tmaskalgorithmmayalsoexcludesomeephemeralchanges,weonly
for the COLD algorithm), in which omission error was substantially applied the Tmask algorithm during the model initialization period.
reduced.Wethinkthereductionofomissionerrorismainlycontributed After the model was initialized, observations that did not show as
totheuseofalltheinformativespectralbands,asforadifferentkindof anomaly consecutively were also removed, as land disturbance are
landdisturbance,thedirectionandmagnitudeofchangecanbequite moreconsistentintimethanoutliers.
different.Moreover,wealsoexploredthescenariosbyincludingother
spectralbandsandindicesinadditiontothefivebandsusedbyCOLD, 3.3.2.1. Tmask modification. In Tmask algorithm, a fixed threshold of
andtheresultssuggestedthattheinclusionoftheBlue,TIR,Blueand 0.04inGreenandSWIR1bands(TOAreflectance)wasusedtodetect
TIRbandsorotherindicesdidnotofferbetterperformance.Wethink anycloud,cloudshadow,andsnowinthetimeseries.Thisthreshold
thisismainlybecause1)theBlueandTIRbandssignalsaremorein- waschosenbasedonvisualassessmentofthecloud,cloudshadow,and
fluencedbyatmospherethanlanddisturbance(Zhuetal.,2015b);and snow mask created for Landsat images located in one New England
2) if all the useful spectral bands are already usedto detectland dis- scene,but it hasnot been tested andcalibrated for other parts ofthe
turbance,thesignalinthevegetationindiceswillberedundant. world and other kinds of landscapes. Moreover, for places with large
naturalvariations(e.g.,urbanandagriculturalareas),afixedthreshold
3.3.2. Outlierremoval will likely remove many clear observations, leaving very few
Cloud, cloud shadow, and snow were first screened by the Fmask observations for model fit. Therefore, we proposed a dynamic
8

| Z.Zhu,etal.                                                 |     |     |     |     |     |     |     |                 |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| thresholdingapproachforTmaskbasedonaspecifictypeofvariogram |     |     |     |     |     |     |     | 3.3.4. Modelfit |     |     |                                                 |     |     |     |     |     |
calledlag-1madogram(seeSection2.1inSupplementarymaterialsfor 3.3.4.1. Number of coefficients. Harmonic (Fourier) models have been
details). widely used for modeling satellite time series (Zhu, 2017). Previous
Weexploredtheuseofavarietyofdynamicthresholdsbasedona studies suggested that harmonic models with three harmonic terms
series of probabilities (e.g., 0.99, 0.999, 0.9999, 0.99999 and (annual, bimodal, and trimodal changes) work best for satellite time
0.999999).Thedynamicthresholdingapproachshowedbetterperfor- series (Verbesselt et al., 2012; Zhu et al., 2015b), but there is no
mancethanthemethodwithfixedthresholds,andachangeprobability evidence on this choice of harmonic terms. For example, the CCDC
of 0.99999 (normal distribution) achieved the best performance (see approachsuggeststheuseofoneharmonicterm(annualchange)can
Section2.2inSupplementarymaterialsfordetails). already provide high change detection and classification results.
|               |                 |             |          |           |        |            |       | Therefore, | we explored       |       | the use      | of time | series | models     | with      | a   |
| ------------- | --------------- | ----------- | -------- | --------- | ------ | ---------- | ----- | ---------- | ----------------- | ----- | ------------ | ------- | ------ | ---------- | --------- | --- |
|               |                 |             |          |           |        |            |       | maximum    | of 4, 6,          | and 8 | coefficients | (Eq.    | (1)).  | The models | with      | a   |
| 3.3.2.2.      | Non-consecutive | outlier     | removal. | During    | change | detection, | we    |            |                   |       |              |         |        |            |           |     |
|               |                 |             |          |           |        |            |       | maximum    | of 6 coefficients |       | achieved     |         | better | results    | than with | 4   |
| can calculate | change          | probability |          | for every | newly  | collected  | clear |            |                   |       |              |         |        |            |           |     |
coefficients,butmodelswithamaximumof8coefficientsshowedthe
| observation | (see | Eq. (8) for | details). | Outliers | would | show | up with |              |              |     |          |              |     |             |         |     |
| ----------- | ---- | ----------- | --------- | -------- | ----- | ---- | ------- | ------------ | ------------ | --- | -------- | ------------ | --- | ----------- | ------- | --- |
|             |      |             |           |          |       |      |         | best result. | The increase |     | of model | coefficients |     | has greatly | reduced |     |
largechangeprobabilitybutaremoreephemeralintime(e.g.,showup
|             |              |             |        |               |           |          |           | omission    | error and | maintained | a         | similar     | commission | error.       | We  | think  |
| ----------- | ------------ | ----------- | ------ | ------------- | --------- | -------- | --------- | ----------- | --------- | ---------- | --------- | ----------- | ---------- | ------------ | --- | ------ |
| once and    | disappear    | in the      | next   | observation). | If        | the next | a few     |             |           |            |           |             |            |              |     |        |
|             |              |             |        |               |           |          |           | the reduced | omission  | error      | is mostly | contributed |            | from         | the | better |
| consecutive | observations |             | do not | indicate      | a change, | but      | the first |             |           |            |           |             |            |              |     |        |
|             |              |             |        |               |           |          |           | modeling    | of land   | surface,   | and the   | use of      | more       | coefficients | did | not    |
| observation | in these     | consecutive |        | observations  | is        | larger   | than the  |             |           |            |           |             |            |              |     |        |
leadtolargeoverfit,whichismainlycontrolledbytheLeastAbsolute
| change     | threshold,  | we will      | exclude | this observation |     | if it     | has a  |           |               |     |          |         |          |         |         |     |
| ---------- | ----------- | ------------ | ------- | ---------------- | --- | --------- | ------ | --------- | ------------- | --- | -------- | ------- | -------- | ------- | ------- | --- |
|            |             |              |         |                  |     |           |        | Shrinkage | and Selection |     | Operator | (LASSO) | fit (see | Section | 3.3.4.4 | –   |
| relatively | high change | probability. |         | We explored      | a   | series of | change |           |               |     |          |         |          |         |         |     |
LASSOfit).Therefore,wechosethetimeseriesmodelwithamaximum
| probability | (e.g., | 0.99, 0.999, | 0.9999, | 0.99999, | and | 0.999999) | for |     |     |     |     |     |     |     |     |     |
| ----------- | ------ | ------------ | ------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of8coefficients.NotethatthisconclusionissolelybasedonLASSOfit
| removing | this kind | of non-consecutive |     | outliers. | The | best result | was |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ------------------ | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anditmaybedifferentifanotherregressionapproachsuchasordinary
| achieved | with | a change | probability | of  | 0.99999 | (chi-squared |     |     |     |     |     |     |     |     |     |     |
| -------- | ---- | -------- | ----------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
leastsquaresregressionisused.
| distribution). | Note | that if | the change | probability | is<0.99999, |          | this   |          |                   |     |            |     |        |          |     |       |
| -------------- | ---- | ------- | ---------- | ----------- | ----------- | -------- | ------ | -------- | ----------------- | --- | ---------- | --- | ------ | -------- | --- | ----- |
| observation    | will | be used | by COLD    | to update   | model       | fit (the | dashed |          |                   |     |            |     |        |          |     |       |
|                |      |         |            |             |             |          |        | 3.3.4.2. | Update frequency. |     | To provide |     | a more | accurate |     | model |
orangearrowsinFig.3).
|     |     |     |     |     |     |     |     | estimation, | all newly | collected |             | clear  | observations | were | digested |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | ----------- | ------ | ------------ | ---- | -------- | --- |
|     |     |     |     |     |     |     |     | iteratively | to update | the       | time series | model. | However,     |      | updating | the |
3.3.3. Modelinitialization modeltoofrequentlycancostahugeamountofcomputingtime,and
3.3.3.1. CCDC vs. COLD initialization. Changes that occur within the the benefit can be limited compared with less frequent updating.
timeofmodelinitializationcaninfluencemodelpredictionandimpact Therefore, we explored seven different updating scenarios, including
changedetectionafterward.Therefore,theCCDCalgorithmdesigneda updatingforafixedtime(e.g.,observationsaccumulatedforone,two,
stability test by examining the magnitude ofthe model slope and the or three years) and for a fixed proportion of previous time (e.g.,
differences in model prediction and observation for the first and last observations accumulated 1/5, 1/4, 1/3 or 1/2 of time range of
observations (Zhu and Woodcock, 2014b). For example, if a change previous model fit), and compared them with the scenario of
occursduringthetimeofmodelinitialization,theslopewillrespondto updating for every single observation. If there are 20 clear
thechange,andwecanusethechangemagnitudefromtheslope(lslope observations per year, updating for every observation is 20 times
|     |     |     |     |     |     |     |     | more computationally |     | expensive |     | than | the single | year | updating |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | --- | ---- | ---------- | ---- | -------- | --- |
inFig.5A)todeterminewhetheritisastablemodel.Alternatively,ifa
changeoccursatthestart(ortheend)ofthemodelinitialization,they approach,andthetwotothreeyearsupdatetimeintervalwillfurther
maynothaveenoughchangedobservationstoinfluencethemagnitude reducethe computationaltime linearly.Ifweupdatemodel basedon
of the slope, but they will show a large difference between model 1/Noftimelengthofpreviousmodelfitwindow(e.g.,ifthepreviousfit
predictions and actual observations (lstart in Fig. 5B). Therefore, in takesTdaysformodelfit,themodelneedsextraT/Ndaysforthenext
CCDC,themodelwillpassthestabilitytestiflslope,lstart,andlendareall round of model fit), the update frequency will be reduced
smallerthanthechangeprobability.However,theCCDCinitialization exponentially,andcanbeverycomputationalefficientwhenthetime
approachignoresonepossibilityofmodelfitthatmayfailthestability seriesmodelspansalongperiod.Basedonthealgorithmperformance
test.Thisoccurswhenthechangetimeisnotlocatedattheverystart comparisons,updatingmodelforeverysingleobservationachievedthe
(or end) of the time series or in the middle of the time series. For highestdetectionaccuracy.Whentheupdatingfrequencychangedfrom
example,ifitoccursinthemiddleof2001(Fig.5C),themodelslopeis 1to3years,accuracydroppedsubstantially.Ontheotherhand,ifthe
modelisupdatedbasedon1/Nofthetimerangeofpreviousmodelfit,
partiallyinfluencedbytheobservationsthathavechanged.Inthiscase,
lslope, lstart, and lend are likely to be all smaller than the change thesmallertheN,thebettertheperformance,butnoneofthemshowed
probability. To fix this issue, we modified the model initialization betterresultsthanitisupdatedforeverysingleobservation.Therefore,
basedonEq.(5),wheretheCOLDmodelstabilitytestisbasedonthe theCOLDalgorithmupdatesmodelforeverysingleobservation.
| combined | absolute | value | from lslope | and the | larger | absolution | values |     |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ----------- | ------- | ------ | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
betweenlstartandlend. 3.3.4.3. Moving window. Theoretically, the model fit will be more
|                    |     |     |     |     |     |     |     | accurate | with more | clear | observations |     | available, | and | therefore | the |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | ------------ | --- | ---------- | --- | --------- | --- |
| COLDStability Test |     | l   |     |     |     |     |     |          |           |       |              |     |            |     |           |     |
slope CCDCalgorithmusedalltheavailablehistoricalstablepixelsinmodel
+max{|l |+|l |} <Change Probability fit.However,allalgorithmsmakemistakes,anditispossiblethatsome
|     | start | end |     |     |     |     | (5) |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
subtlechangesarenotdetectedbythealgorithmandthechangedpixels
We compared algorithm performance by using CCDC model in- willbeincludedinthemodelfit.Thismaycauseproblemsinmodelfit,
itialization and the new approach we designed for COLD. Both ap- asasingletimeseriesmodelmaynotfitforalltheseobservations.One
proaches achieved a similar omission rate when change probability is way to reduce this impact is to limit the maximum window size for
larger than 0.90. However, the COLD initialization approach reduced model estimating and move the fitting window along with the new
commission rate by almost 10% with a change probability of 0.99. observations (moving window approach). In this way, the impact of
This demonstrates the importance of model initialization for missedchangeswillfadeawaywhenthewindowmovesforward.Note
changedetection. thatiftheavailablestableobservationsarelessthanthelengthofthe
9

| Z.Zhu,etal. |     |     |     |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
requiredmovingwindow,wewillusewhatwehaveformodelfit.We Brooksetal.(2014)detectsforestdisturbancebytheyearinwhichat
explored this moving window approach in model fit by changing the least four images signal a change. Most of these algorithms are only
windowsizefromtwoyearstoallavailableyear(forthestableperiod tested for relativelysmall areas, and there are noexperiments on the
only).Itturnedouttheuseofthreeyearsmovingwindowcanalready optimum number of consecutive anomaly observations needed to
achieve good accuracies, but with the number of years increases, the confirm a change. Therefore, we explored the different algorithm
accuracyalsoincreases,and theallavailable stable yearsshowedthe performances by using four to seven consecutive anomaly
bestresults.Therefore,weusedalltheavailablestableyearsformodel observations to confirm a change (Fig. 6). We found that the
fit. detection accuracy increased when the consecutive anomaly
|     |     |     |     |     |     | observations | increased | from | four to | six | and decreased |     | when |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | ---- | ------- | --- | ------------- | --- | ---- |
3.3.4.4. Least Absolute Shrinkage and Selection Operator (LASSO) consecutive anomaly observations increased to seven. Therefore, we
fit. Though the inclusion of more harmonic terms will generally selected six consecutive anomaly observations to confirm a change.
provide a more accurate estimation of the temporal trajectory of the Though the increase of the number of consecutive anomaly
land surface, this can also cause overfitting because of the extra observations will remove more false positive changes, some short-
freedom in the model. The LASSO regression approach (Tibshirani, term real surface changes may also disappear which increases the
|     |     |     |     |     |     | omission | error. It is | worth noting | that | for specific | disturbance |     | types |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------------ | ---- | ------------ | ----------- | --- | ----- |
2011)isknownforreducingtheoverfittingbyminimizingtheresidual
sum of squared errors and the sum of the absolute values of the suchasgrasslandfiresandfloodsiftheypresentonthelandsurfacefor
coefficients(Eq.(6)).OneofthemostcriticalvariablesintheLASSOfit less than six consecutive anomaly observations, the COLD algorithm
isthepenaltyparameter(λ),inwhichthehigherthevalue,themore will not be able to label them as change. Moreover, for places with
penaltyforoverfitting.Ifλissettozero,LASSOfitwillbethesameas heavycloudcover,theCOLDalgorithmwillwaitamuchlongertimeto
theOLSfit.WeexploredtheLASSOfitwithavarietyofλvalues(from collectatotalofsixclearobservationstoconfirmachange.
| 0 to 100) | for 8 coefficient | time | series models, | and the | LASSO fit |     |     |     |     |     |     |     |     |
| --------- | ----------------- | ---- | -------------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
achieved better detection results than the OLS fit did, and the best 3.3.5.2. Change probability. The threshold used for identifying land
detection result was achieved when λ equals to 20 (we selected this changeisthemostcriticalvariableforchangedetection.IntheCCDC
valueforCOLD). algorithm,anempiricalthresholdofthreetimesofRootMeanSquare
|     |     |     |     |     |     | Error (RMSE) | is used | to detect | land cover | change | (Eq. | (7)), and | in a |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | --------- | ---------- | ------ | ---- | --------- | ---- |
| n   |     | p   |     |     |     |              |         |           |            |        |      |           |      |
laterversion,itislowertotwotimesofRMSEtocapturemoresubtle
| min | (Y X )2+ | | | |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RP  | i i      | j   |     |     |     |     |     |     |     |     |     |     |     |
i=1 j=1 (6) changes (Zhu et al., 2015b). In Eq. (7), the RMSE normalized
|     |     |     |     |     |     | differences     | between model | predictions |          | and observations |     | are averaged  |     |
| --- | --- | --- | --- | --- | --- | --------------- | ------------- | ----------- | -------- | ---------------- | --- | ------------- | --- |
|     |     |     |     |     |     | for all Landsat | spectral      | bands.      | This can | be problematic   |     | for detecting |     |
3.3.5. Changedetection landdisturbancesthatonlyshowchangeinoneofthespectralbands,as
3.3.5.1. Number of consecutive anomaly observations. Satellite time thedifferencefoundinthisbandwillbeaveragedforallspectralbands.
series contains rich information but is also inherently impacted by Therefore, in the COLD algorithm, a normalized change vector
noisefromavarietyofsources(Cohenetal.,2017).Fortunately,unlike magnitudeisusedasthethresholdforchangedetection(Eq.(8)),and
noise that appears randomly throughout the time series, land change byusingthesumofsquareddeviates,changeinanyoneofthespectral
signal is usually more consistent. Therefore, the majority of the false bandswillshowlargedeviationsevenitisaveragedwithotherbands.
positivechangecontributedtonoisewillbeeliminatedifweuseafew Considering each of the normalized change deviates follows the
consecutiveanomalyobservationstoconfirmachange.Thisapproach standard normal distribution, the sum of the square of the deviates
hasbeenwidelyusedinrecentchangedetectionstudies.Forexample,
followsthechi-squareddistribution,withadegreeoffreedomequalto
| the CCDC | algorithm confirms | a change | based | on 3 consecutive | clear |     |     |     |     |     |     |     |     |
| -------- | ------------------ | -------- | ----- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thenumberofspectralbandsusedinchangedetection.Therefore,we
observations (Zhu and Woodcock, 2014b); Hansen et al. (2016) cancreatechangethresholdsbasedonchangeprobabilityderivedfrom
requires 4 consecutive clear observations to alert forest loss; and thechi-squareddistribution,inwhichachangeprobabilityof0.99with
fivespectralbandworksbest.
|     |     |     |     |     |     | 1 k | i i |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
>1
|     |     |     |     |     |     | k i=1 3×RMSE | i   |     |     |     |     |     | (7) |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
2
|     |     |     |     |     |     | k i      | i      | 2     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |          | ~ 2(k) | > (5) |     |     |     |     |     |
|     |     |     |     |     |     | i=1 RMSE |        | 0.99  |     |     |     |     | (8) |
i
where,
i:theithLandsatband
k:NumberofLandsatbandsusedforchangedetection
ρi:ObservedvaluefortheithLandsatband
i:PredictedvaluefortheithLandsatband.
|     |     |     |     |     |     | 3.3.6. Changeangle |               |     |            |       |      |               |     |
| --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --- | ---------- | ----- | ---- | ------------- | --- |
|     |     |     |     |     |     | Unlike             | environmental | and | systematic | noise | that | is completely |     |
random,thedisturbancesignalsaremoreconsistentnotonlyintermsof
absolutechangemagnitudebutalsochangevectorangle.Itispossible
thatnoiseorothernon-disturbancesignalsmayexistinthetimeseries
forafewconsecutivetimes;itisunlikelythatallofthemarechanging
inthesamedirection.Therefore,wecanusethemeanincludedangles
betweeneachpairofneighboringchangevectors(afternormalization)
Fig.6.Changedetectionwithdifferentnumber(e.g.,4,5,6,and7)ofcon-
|     |     |     |     |     |     | to confirm | a real land | disturbance | (Fig. | 7 and | Eq. (9)). | The | optimal |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | ----- | ----- | --------- | --- | ------- |
secutiveanomalyobservationstoconfirmachange.
resultwasachievedwithathresholdof45°ofmeanincludedangles.In
10

| Z.Zhu,etal. |     |     |     |     |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- |
Fig.7.A:Anincludedanglebetweenapairofneighboringchangevectors.B:Meanincludedanglefromfivepairsofneighboringchangevectors.
| short, COLD | confirms | a   | change | if the mean | included | angle | between |     |     |     |     |     |
| ----------- | -------- | --- | ------ | ----------- | -------- | ----- | ------- | --- | --- | --- | --- | --- |
Change Vector
pairsofneighboringchangevectorsmallerthan45°.
Yes
| 1 k 1 |     |     |     |     |     |     |     |     |     |     | No  |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<45°
| k i=1 | i,i+1 |     |     |     |     |     | (9) |     |            |                   |     |     |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | --- |
|       |       |     |     |     |     |     |     |     | “Greener”  | Land Disturbance  |     |     |
where,
i:theithconsecutiveanomalyobservation
Slope Mag (A#er Change) > Slope Mag (Before Change)
| k: Number | of  | consecutive |     | anomaly | observations | to  | confirm a |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
change.
|          |           |        |       |         |      |           |          |     | No  |     | Yes |     |
| -------- | --------- | ------ | ----- | ------- | ---- | --------- | -------- | --- | --- | --- | --- | --- |
| 3.3.6.1. | Root Mean | Square | Error | (RMSE). | RMSE | from each | spectral |     |     |     |     |     |
Land Disturbance from
bandinmodelfitisusedtonormalizethechangevector.Therefore,the
Regrowth Breaks
largertheunexplainedvariations,thelesstheweightincontributingto Reforesta!on/Afforesta!on
thefinalchangeprobability.Thisapproachworkswellformanyofthe
land cover types, as the unexplained variations are usually the same Fig. 8.Extraction of land disturbance based on change vector direction and
| throughout | the years. | However, |     | for some | land cover | types | such as | modelslopes. |     |     |     |     |
| ---------- | ---------- | -------- | --- | -------- | ---------- | ----- | ------- | ------------ | --- | --- | --- | --- |
agriculture,semi-aridshrublands,andgrassland,thereisconsiderable
year-to-yearvariabilityinthetimeofgreen-upthatisrelatedtohuman
activities and interannual climate variability. Therefore, for a certain vegetation regrowth (e.g., the break between the young forest and
time ofyear,thevariationofthedatacan bemuch largerthan other matureforest).Toexcluderegrowthbreaksfromlanddisturbance,we
timeofyear,makingafixedRMSElessidealforthiskindofsituation. developedageneric-rule-basedlanddisturbanceextractionapproachas
|         |        |                 |     |             |     |         |             | illustrated in           | Fig. 8. Unlike most | of the other   | disturbance  | algorithms |
| ------- | ------ | --------------- | --- | ----------- | --- | ------- | ----------- | ------------------------ | ------------------- | -------------- | ------------ | ---------- |
| Similar | to Zhu | et al. (2015b), |     | we proposed | to  | use the | temporally- |                          |                     |                |              |            |
|         |        |                 |     |             |     |         |             | that extract disturbance | based               | on a threshold | of a certain | vegetation |
adjustedRMSEasthedenominatorfornormalizingthechangevector.
index(e.g.,NDVI,NBR,orTasseledCapWetness),weassumeallpre-
| The temporally-adjusted |     |     | RMSE uses | the | nearest (day | of the | year) 24 |     |     |     |     |     |
| ----------------------- | --- | --- | --------- | --- | ------------ | ------ | -------- | --- | --- | --- | --- | --- |
viouslyidentified“breaks”arereallanddisturbances,andonlyremove
| observations | to calculate |     | the RMSE | when | the total | number | of clear |     |     |     |     |     |
| ------------ | ------------ | --- | -------- | ---- | --------- | ------ | -------- | --- | --- | --- | --- | --- |
observations is>24. The other important component for RMSE cal- “breaks”fromthevegetationregrowth.Inthisway,landdisturbances
culation is that for spectrally dark pixels or models with a limited that are not related to gain or loss in vegetation amount will also be
numberofclearobservations,sometimesRMSEcanbeextremelysmall includedintheresults.Wefirstusedthechangevectorfromthethree
(see Fig. 21 in Zhu and Woodcock, 2014b). Considering the change important spectral bands (Red, NIR, and SWIR1) to separate all
vector magnitudeisnormalizedbyRMSE,aminorchangeinspectral
| bands can  | cause           | a large    | difference | in the | final change | probabilities. |            |     |     |     |     |     |
| ---------- | --------------- | ---------- | ---------- | ------ | ------------ | -------------- | ---------- | --- | --- | --- | --- | --- |
| Therefore, | it is important |            | to provide | a      | predefined   | minimum        | value of   |     |     |     |     |     |
| RMSE, and  | if the          | calculated | RMSE       | value  | is less      | than this      | value, the |     |     |     |     |     |
minimumvaluewillbeused(seeSection5.2inSupplementarymate-
rialsfordetails).
WeexploredfourdifferentscenariosofusingRMSEfornormalizing
changevectormagnitude.ThescenariosofusingRMSEandRMSEwith
minimumRMSEshowedsimilarperformances.Theuseoftemporally-
| adjusted | RMSE showed | better | performance, |     | and the | combined | use of |     |     |     |     |     |
| -------- | ----------- | ------ | ------------ | --- | ------- | -------- | ------ | --- | --- | --- | --- | --- |
bothtemporally-adjustedRMSEandminimumRMSEachievedthebest
results(usedinCOLD).
3.3.7. Disturbanceextraction
The change detection process identifies “breaks” contributed from Fig.9.The“greener”directioninNIRbandforaregrowthbreak.Notethatthe
spectralchangesthatdeviatefrommodelprediction,inwhichsomeof matureforestNIRobservationvaluesarehigherthanthepredictedvaluesfrom
them may not related to land disturbance, such as breaks from themodelbeforethebreak.
11

| Z.Zhu,etal. |     |     |     |     |     |     |     |     |     | Remote Sensing of Environment 238 (2020) 111116 |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
)%(etaRnoissimmoC
| Fig. 10.The | slope | magnitude | in NIR band | for a | reforestation/afforestation |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | ----------- | ----- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
break.NotethattheNIRslopemagnitudeforthemodelafterthebreakispo-
sitiveandlargerthantheslopmagnitudeforthemodelbeforethebreak.
| “breaks” | into two | categories: | “greener” | direction | breaks (higher | NIR |     |     |     |     |     |     |     |     |
| -------- | -------- | ----------- | --------- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
band,andlowerRedandSWIR1bandsafterthe"break";Eq.(10))and
landdisturbance.Unlikelanddisturbancethatcanhavechangevector
inall directions,theregrowthbreakswillonlyshowinthe“greener”
|     |     |     |     |     |     |     | Fig. 11.Omission |     | and commission | error | when change | probability |     | threshold |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | ----- | ----------- | ----------- | --- | --------- |
direction(Fig.9).Allbreaksthatarenotinthis“greener”directionwill
changesfrom0.90to0.9999.
belabeledaslanddisturbances.Thiswouldidentifyalmostallkindsof
landdisturbances,exceptforreforestationandafforestation,whichalso
|     |     |     |     |     |     |     | area in California |     | to examine | the detection |     | results qualitatively. |     | We  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | ------------- | --- | ---------------------- | --- | --- |
sharethesame“greener”changevectordirectionwithregrowthbreaks.
choosethisurbanareamainlybecauseithasexperiencedavarietyof
| Fortunately, | the | slopes of | time series | models | before and | after the |                   |     |                     |     |             |              |     |     |
| ------------ | --- | --------- | ----------- | ------ | ---------- | --------- | ----------------- | --- | ------------------- | --- | ----------- | ------------ | --- | --- |
|              |     |           |             |        |            |           | land disturbances |     | (e.g., earthquakes, |     | fire, house | development, |     | and |
changearequitedifferentbetweentheregrowthbreaksandthebreaks
transitionofurbanlanduse),andtheyarewell-documented.
fromreforestationandafforestation.Forexample,forbreaksfromve-
| getation | regrowth, | the magnitude | of  | the slope | before the breaks | are |     |     |     |     |     |     |     |     |
| -------- | --------- | ------------- | --- | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
usually largerthan itafter the breakand itisthe oppositeforbreaks 4.1. Quantitativeevaluationofdetectionaccuracy
fromreforestationandafforestation.Moreover,astheslopedirections
fortimeseriesmodelsafterthereforestationorafforestationarealready WetestedtheCOLDalgorithmagainstthe3317referenceLandsat
determined (positive in NIR band and negative in Red and SWIR1 plots based on a series of change probabilities (e.g., 0.90, 0.95, 0.99,
|     |     |     |     |     |     |     | 0.999, and | 0.9999) | (Fig. | 11). Optimum | detection |     | accuracy | was |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ------------ | --------- | --- | -------- | --- |
bands),wecancreateafewrulesbasedonthemagnitudeanddirection
ofslopestoextractreforestationandafforestationbreaksoutfromthe achievedwhenchangeprobabilityequalsto0.99.COLDhasreacheda
regrowthbreaks(Eq.(11))(Fig.10). producer'saccuracyof73%(27%ofomissionerror),auser'saccuracy
of72%(28%ofcommissionerror),andanF1scoreof73%.Itisworth
“Greener”direction: notingthatthisaccuracyisachievedbasedonreferencesampleswitha
|      |            |                |     |        |           |     | large number | of  | small magnitude | disturbances |     | and a | variety | of land |
| ---- | ---------- | -------------- | --- | ------ | --------- | --- | ------------ | --- | --------------- | ------------ | --- | ----- | ------- | ------- |
| Red< | Threshold& | NIR>Threshold& |     | SWIR1< | Threshold |     |              |     |                 |              |     |       |         |         |
disturbanceseventsthathavenotbeenusedinalgorithmdevelopment
(10)
|     |     |     |     |     |     |     | and calibration.  |     | We also          | evaluated | COLD | algorithm | performance |         |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------------- | --------- | ---- | --------- | ----------- | ------- |
|     |     |     |     |     |     |     | against different |     | land disturbance | types.    | COLD | performed | well        | for all |
Slopemagnitudesbefore(SBef)andafterchange(SAft): sevendisturbancetypes,inwhichmostoftheHarvest(75%),Mechan-
S < |S | &S > |S |&S < |S | ical(74%),Wind(74%),Fire(76%),andOther(72%)disturbanceswere
| Red, Aft | Red,Bef | NIR,Aft | NIR,Bef | SWIR1,Aft | SWIR1,Bef |     |           |             |          |           |        |        |       |         |
| -------- | ------- | ------- | ------- | --------- | --------- | --- | --------- | ----------- | -------- | --------- | ------ | ------ | ----- | ------- |
|          |         |         |         |           |           |     | correctly | identified, | and more | than half | of the | Stress | (60%) | and Hy- |
(11)
drology(63%)disturbanceswerecorrectlydetected.
3.3.7.1. Thresholdsfordisturbanceextraction. Wedefinedthe“greener” 4.2. QualitativeevaluationoflanddisturbancemapsintheBerkeley-
| directioniswhereNIRincreased,butRed/SWIR |     |     |     |     | decreased.However, |     |     |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Oaklandarea
howmuchincreaseordecreaseisconsideredasthe“greener”direction
hasnotbeenassessed.Therefore,weevaluatedalgorithmperformances
|             |     |           |              |               |           |      | The Berkeley-Oakland |     | area | has a quite | complex | landscape, |     | where |
| ----------- | --- | --------- | ------------ | ------------- | --------- | ---- | -------------------- | --- | ---- | ----------- | ------- | ---------- | --- | ----- |
| by changing | the | threshold | for defining | the “greener” | direction | from |                      |     |      |             |         |            |     |       |
commonlandcoverandlandusecategoriesincludeurban,water,and
−0.04to0.04andincludedthescenariowithoutusingthedisturbance
variouskindsofvegetationtypes(Fig.12E).Thisurbanandsuburban
extractionprocess(identifyallbreaksaslanddisturbance).Theuseof
areahasbeenfrequentlydisturbedbyavarietyofdifferenteventsthat
disturbanceextractionachievedmuchbetterresultsthanwithoutusing include the 1989 Loma Prieta earthquake (Fig. 12A), the Oakland
it,andathresholdof−0.02providedthebestresults(usedbyCOLD). firestormof1991(Fig.12B),thedecommissionofOaklandArmyBase
(Fig.12C),andWilderhousingprojects(Fig.12D).
4. Results To demonstrate the algorithm's capability of monitoring land dis-
turbanceinacontinuousmode,wecreatedtheaccumulatedlanddis-
WeevaluatedtheCOLDdisturbancedetectionresultsbothquanti- turbance maps during the time of each previously mentioned land
tativelyandqualitatively.The50%unseenreferenceLandsatplots(not disturbanceevent(Fig.13).ThefirstdemonstrationisfromtheLoma
usedforalgorithmdevelopmentandcalibration)wereusedtovalidate Prietaearthquake.The1989LomaPrietaearthquakeoccurredonOc-
the COLD land disturbance detection accuracy, and accuracy metrics tober 17 in the San Francisco Bay Area heavily damaged the Cypress
such as producer's accuracy (or omission error), user's accuracy (or Viaduct,leadingtotheinstantdeathof41people.TheCOLDalgorithm
commissionerror),andF1scorewereusedforthisassessment.Wealso detectedthislanddisturbanceeventaccuratelyinaveryshorttime,and
appliedtheCOLDalgorithmtoanareathatcoverstheBerkley-Oakland wecanseeapreciseshapeofthecollapsedviaductintheDecember10,
12

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
Fig.12.HistoricallanddisturbancedetectedbyLandsattimeseriesfortheBerkeley-Oaklandarea.A:AerialviewofcollapsedsectionsoftheCypressViaductof
Interstate880(photoadaptedfromH.G.Wilshire,U.S.GeologicalSurvey,1989).B:The1991Oakland-Berkeleyfirestormwhichdevastated1500acresinthehills
(photoadaptedfromCaliforniaGovernor'sOfficeofEmergencyServices,1991).C:(Left)ViewofOaklandArmyBase,MaritimeStreetatWestGrandAvenue,
Oakland,AlamedaCounty,CA(photoadaptedfromOrdenana,Adrian,1994.Institution:LibraryofCongressPrintsandPhotographsDivisionWashington,D.C.).
(Right)AerialviewoftheportofOakland,California,USA(photoadaptedfromRobertCampbell,U.S.ArmyCorpsofEngineersDigitalVisualLibrary).D:Wilder
luxuryhomecommunityinOrinda,California(photoadaptedfromGoogleMaps).E:FalsecolorcompositeLandsatimage(SWIR-NIR-Redbands)forthisarea,
capturedonthe56thdayof2018.(Forinterpretationofthereferencestocolorinthisfigurelegend,thereaderisreferredtothewebversionofthisarticle.)
1989, accumulated disturbance map (Fig. 13A). The second demon- “breaks”. The reference data revealed that the COLD results were ac-
stration is from the Oakland firestorm. In the weekend of October curate formonitoring land disturbance,with both omissionerror and
19–20, 1991, Oakland experienced a severe fire over the hills in commissionerror < 30%.TheCOLDalgorithmisprogrammedinthe
northernOaklandandsouthernBerkeley.Thisfirestormwastheworst MATLAB environment and is provided online as an open-source
fire in East Bay history. It ultimately killed 25 people, injured 150 packagethatincludesbothsourcecodeandstandalonesoftware.
others, and a large number of dwellings and apartments were de- Wefullyexploredandverifiedvariouskindsofinputdataandtime
stroyed.ThiseventwasalsoaccuratelycapturedbytheCOLDalgorithm series techniques for better detection of land disturbance.
in the November 14, 1991, accumulated land disturbance map Recommendationsinsixmajoraspectswereprovided,includinginput
(Fig.13B).Thethirddemonstrationisfromtheurbanlandusetransi- data,outlierremoval,modelinitialization,modelfit,changedetection,
tionfromanarmybasetocargohubs.TheOaklandArmyBaseserved anddisturbanceextraction.Thebestinputdataforlanddisturbanceare
from 1944 to 1999 on the Oakland waterfront, south to the eastern LandsatARDSR.Moreover,thecombineduseofspectralbandsisbetter
entrancetotheSanFrancisco-OaklandBay,andlaterthisregionstarted thanusingasinglespectralbandorindex,andtheintegrateduseoffive
itsgatewayandportdevelopment.TheCOLDalgorithmalsodetected bandsincludingGreen,Red,NIR,SWIR1,andSWIR2providedthebest
thislanduserelateddisturbanceinatimelyfashion,andwecanseean result.Foroutlierremoval,aprobabilitythresholdof0.99999(basedon
apparent patch in the yellow box of the June 13, 1999, accumulated normal distribution orthechi-squared distribution)providedthe best
land disturbance map (Fig. 13C). The fourth demonstration is from result. Moreover, model initialization is also essential for change de-
wilder housing development. There were several house development tection, and the COLD initialization approach is recommended.
projectsinthewesternofOrinda,California,startedapproximatelyin Furthermore, a good model fit provides a better prediction of ob-
2007.Thesehomesinthecommunitywereconstructedtoservepeople servations,whichwillalsobenefitthedetectionoflanddisturbance.We
working in downtown San Francisco but living away from crowded recommendtimeseriesmodelswithamaximumofeightcoefficients,
cities.Thehousingdevelopmentrelatedlanddisturbancewasalsowell updated for every single observation, based on all available stable
capturedbytheCOLDalgorithm,andwecanseethespatialpatternin years,andusingLASSOregression(λ=20).Forchangedetection,the
theblueboxoftheFebruary14,2008,accumulateddisturbancemap useofachangeprobabilityof0.99(chi-squareddistribution),atotalof
(Fig.13D).TheCOLDalgorithmmonitoredthisareacontinuouslyuntil six consecutive anomaly observations, and a mean included angle <
February25,2018,andthefinalaccumulateddisturbancemapisillu- 45°toconfirmachangeprovidesthebestresult,andthecombineduse
stratedinFig.13E.Manysmallscalelanddisturbanceshaveoccurredin of temporally-adjusted RMSE and minimum RMSE is also re-
this busy urban area, with a majority of them related to urban mod- commended.Finally,wedevelopedanewgeneric-rule-basedapproach
ificationsandintensifications. to exclude non-disturbance related “breaks”, which substantially re-
ducedthecommissionerror.Itisworthnotingthatthoughmanyofthe
time series techniques can only provide limited improvements, the
5. Discussionsandconclusion
impactofcombineduseofallproposedtechniquescanbesubstantial.
TheCOLDalgorithmhasmanyadvantages.First,unlikemanyother
Continuous monitoring of land disturbance is difficult in remote
disturbancealgorithmsthatrelyheavilyontheavailabilityoftraining
sensing. The availability of dense Landsat time series provides the
dataorinputsfromseveralcomplicatedalgorithms(Cohenetal.,2018;
possibility.Inthisstudy,wedevelopedanewalgorithmforcontinuous
Healey et al., 2018), COLD detects land disturbance fully automated
monitoringoflanddisturbanceathighspatial(30-meter)andtemporal
withLandsattimeseriesastheonlyinputdata.Thoughweusedsome
(uptoeveryfourdays)resolutions.ByusingallavailableLandsatARD,
referencesamplesforalgorithmdevelopmentandcalibration,mostof
this approach creates time series model for pixels during the stable
therulesandtechniquesarebasedonecologicalandbiophysicalpro-
periods, and by comparing model predictions with Landsat observa-
cesses that can be generalized for large areas and different kinds of
tions,“breaks”(orspectralchanges)areidentifiediftheyshowchange
environments. With some adjustments (e.g., region-based thresholds),
forafewconsecutivetimes.TheCOLDalgorithmflagsallthe“breaks”
the COLD algorithm should have the capability of providing land
aspotentiallanddisturbances,andlaterexcludesthenon-disturbance
13

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
Fig.13.Accumulatedlanddisturbancemapduringthetimeoffourmajorlanddisturbanceevents,withcolorsdenotingthedisturbancetime.A:Accumulatedland
disturbancemapfrom1982toDecember10,1989.Withinthegreenbox,thecollapseoftheCypressStreetViaductiscapturedalongInterstate880.B:Accumulated
landdisturbancemapfrom1982toNovember14,1991.Withintheredbox,alargepatchoflanddisturbancecausedbytheOaklandfireisalsowellcaptured.C:
Accumulateddisturbancemapfrom1982toJune13,1999.Withintheyellowbox,thechangeoftheOaklandArmyBasetoacargohubiscapturedinthePortof
Oakland.D:Accumulateddisturbancemapfrom1982toFebruary14,2008.Withinthebluebox,thelanddisturbancesfromthehousingdevelopmentarewell
detected.E:Accumulatedlanddisturbancemapsfrom1982toFeb25,2018.(Forinterpretationofthereferencestocolorinthisfigurelegend,thereaderisreferred
tothewebversionofthisarticle.)
disturbancemapsatcontinentalorevenglobalscales.Itisworthnoting thatincludesmanykindsoflanddisturbancetypesoccurredonallland
that though COLD can create disturbance maps without any training surface, including disturbances that are not occurring in vegetated
data, for optimal results, the use of training data to calibrate the al- areas. This timely generic disturbance information can be pivotal for
gorithmparametersforeachspecificlocationishighlyrecommended. many different purposes, such as disaster response, urban planning,
Second, by digesting newly collected Landsat ARD continuously, the resourcesmanagement,etc.
COLDalgorithmcanprovidelanddisturbancemapsassoonastheland TheCOLDalgorithmalsohaslimitations.First,itiscomputationally
surfaceisbeingdisturbed.Currently,weonlyusedLandsatARD,which expensive and requires a large amount of data storage. The time re-
providesnew imagesinlessthaneight days(fourdaysinoverlapped quired toprocessoneLandsat ARDtile (1–3 thousandimages)would
areas)whenbothLandsat7and8areused.Thisapproachcanbeeasily still cost 1000–3000 computing hours, and it takes around 0.5–2
adaptedtoincludeSentinel-2images,andbycombiningLandsat7and Terabytes to store Landsat time series in one ARD tile. Second, the
8,andtwoSentinel2Aand2B,therewouldbetypicallytenobserva- COLDalgorithmworkswellforplacesthatarerelativelystable,butfor
tionspermonth(newobservationseverythreedays),makingnearreal- placesthatarefrequentlydisturbed(e.g.,agricultureandurbanareas),
timemonitoringoflanddisturbanceathighspatialresolutionpossible. theCOLDalgorithmstrugglestofindastableperiodtoinitializetime
Third,theCOLDalgorithmisthefirstdisturbancemappingalgorithm series models and may miss those disturbance events. Finally, the
14

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
currentCOLDalgorithmcanonlyidentifydisturbanceeventbutcannot increaseinAtlantichurricaneactivity:causesandimplications.Science.https://doi.
provide more detailed information on disturbance type. Recently, the org/10.1126/science.1060040.
Gorelick,N.,Hancher,M.,Dixon,M.,Ilyushchenko,S.,Thau,D.,Moore,R.,2017.Google
USGSandUSFSareworkingtogethertocollectindependentreference
EarthEngine:planetary-scalegeospatialanalysisforeveryone.RemoteSensingof
samples forvalidation and characterization ofannual landcover pro- Environment.https://doi.org/10.1016/j.rse.2017.06.031.
ducts for the Land Change Monitoring, Assessment, and Projection Grimm,N.B.,Faeth,S.H.,Golubiewski,N.E.,Redman,C.L.,Wu,J.,Bai,X.,Briggs,J.M.,
2008.Globalchangeandtheecologyofcities.Science.https://doi.org/10.1126/
(LCMAP)project(Pengraetal.,2016;Zhuetal.,2016),inwhichatotal
science.1150195.
of 25,000 Landsat plots will be collected. This dataset provides both Grogan,K.,Pflugmacher,D.,Hostert,P.,Kennedy,R.,Fensholt,R.,2015.Cross-border
land cover and disturbance information for every pixel in every ca- forestdisturbanceandtheroleofnaturalrubberinmainlandSoutheastAsiausing
annualLandsattimeseries.RemoteSensingofEnvironment169,438–453.https://
lendaryear,andasitiscreatedbasedonsimplerandomsampling,itis
doi.org/10.1016/j.rse.2015.03.001.
notbiasedtoforests.Wecanvalidate(orre-calibrate)theCOLDalgo- Hansen,M.C.,Loveland,T.R.,2012.Areviewoflargeareamonitoringoflandcover
rithm and develop methods to classify different kinds of disturbance changeusingLandsatdata.RemoteSensingofEnvironment122(September),66–74.
agentwhenthesereferencesamplesareavailable. https://doi.org/10.1016/j.rse.2011.08.024.
Hansen,M.C.C.,Potapov,P.V.,Moore,R.,Hancher,M.,Turubanova,S.A.a,Tyukavina,
In conclusion, we developed a new algorithm called COLD for A.,...Townshend,J.R.G.R.G.,2013a.High-resolutionglobalmapsof.Science342
continuousmonitoringoflanddisturbance.Itcanprovideaccurateland (November),850–854.https://doi.org/10.1126/science.1244693.
disturbancemapsfullyautomatedathighspatial(30-meter)andhigh Hansen,M.C.,Krylov,A.,Tyukavina,A.,Potapov,P.V.,Turubanova,S.,Zutta,B.,...
Moore,R.,2016.HumidtropicalforestdisturbancealertsusingLandsatdata.
temporal(uptofourdays)resolutionsforlargeareas.
EnvironmentalResearchLetters11(3),034008.https://doi.org/10.1088/1748-
9326/11/3/034008.
Acknowledgments Healey,S.P.,Cohen,W.B.,Yang,Z.,KennethBrewer,C.,Brooks,E.B.,Gorelick,N.,...Zhu,
Z.,2018.Mappingforestchangeusingstackedgeneralization:anensembleapproach.
RemoteSensingofEnvironment.https://doi.org/10.1016/j.rse.2017.09.029.
WegratefullyacknowledgethesupportoftheUSGS-NASALandsat Hicke,J.A.,Allen,C.D.,Desai,A.R.,Dietze,M.C.,Hall,R.J.,Hogg,E.H.T.,...Vogelmann,
Science Team (LST) Program for “Toward Near Real-time Monitoring J.,2012.EffectsofbioticdisturbancesonforestcarboncyclingintheUnitedStates
andCanada.GlobalChangeBiology.https://doi.org/10.1111/j.1365-2486.2011.
andCharacterizationofLandSurfaceChangefortheConterminousUS”
02543.x.
(#G17PS00256),andUSGSGreatPlainsCooperativeEcosystemStudies Hu,F.S.,Higuera,P.E.,Walsh,J.E.,Chapman,W.L.,Duffy,P.A.,Brubaker,L.B.,Chipman,
Unit (CESU) Program for “Algorithm Improvement, Near Real-time M.L.,2010.TundraburninginAlaska:linkagestoclimaticchangeandseaiceretreat.
JournalofGeophysicalResearch:Biogeosciences.https://doi.org/10.1029/
Monitoring, and New Change Product Designed for the LCMAP
2009JG001270.
Initiative”toZheZhu(#G17AC00057).Wealsogratefullyacknowledge Huang,B.,Zhao,B.,Song,Y.,2018.Urbanland-usemappingusingadeepconvolutional
the support of the NASA's Terrestrial Ecology Program and Carbon neuralnetworkwithhighspatialresolutionmultispectralremotesensingimagery.
CycleandEcosystemsFocusAreatoWarrenCohen(#NNH11AR29I). RemoteSensingofEnvironment.https://doi.org/10.1016/j.rse.2018.04.050.
Kasischke,E.S.,Turetsky,M.R.,2006.RecentchangesinthefireregimeacrosstheNorth
Americanborealregion-spatialandtemporalpatternsofburningacrossCanadaand
AppendixA. Supplementarydata Alaska.GeophysicalResearchLetters33(9). https://doi.org/10.1029/
2006GL025677.
Kennedy,R.E.,Yang,Z.,Cohen,W.B.,2010.Detectingtrendsinforestdisturbanceand
Supplementary data to this article can be foundonline at https://
recoveryusingyearlyLandsattimeseries:1.LandTrendr-temporalsegmentation
doi.org/10.1016/j.rse.2019.03.009. algorithms.RemoteSensingofEnvironment114(12),2897–2910.https://doi.org/
10.1016/j.rse.2010.07.008.
Kennedy,R.E.,Yang,Z.,Braaten,J.,Copass,C.,Antonova,N.,Jordan,C.,Nelson,P.,
References
2015.AttributionofdisturbancechangeagentfromLandsattime-seriesinsupportof
habitatmonitoringinthePugetSoundregion.USA.RemoteSensingofEnvironment
Brooks,E.B.,Wynne,R.H.,Thomas,V.A.,Blinn,C.E.,Coulston,J.W.,2014.On-the-fly 166,271–285.https://doi.org/10.1016/j.rse.2015.05.005.
massivelymultitemporalchangedetectionusingstatisticalqualitycontrolchartsand Mack,M.C.,Bret-Harte,M.S.,Hollingsworth,T.N.,Jandt,R.R.,Schuur,E.A.G.,Shaver,
landsatdata.IEEETransactionsonGeoscienceandRemoteSensing52(6), G.R.,Verbyla,D.L.,2011.CarbonlossfromanunprecedentedArctictundrawildfire.
3316–3332.https://doi.org/10.1109/TGRS.2013.2272545. Nature.https://doi.org/10.1038/nature10283.
Cohen,W.B.,Yang,Z.,Kennedy,R.,2010.Detectingtrendsinforestdisturbanceand Marlon,J.R.,Bartlein,P.J.,Walsh,M.K.,Harrison,S.P.,Brown,K.J.,Edwards,M.E.,...
recoveryusingyearlyLandsattimeseries:2.TimeSync-toolsforcalibrationand Whitlock,C.,2009.WildfireresponsestoabruptclimatechangeinNorthAmerica.
validation.RemoteSensingofEnvironment114(12),2911–2924.https://doi.org/ ProceedingsoftheNationalAcademyofSciencesoftheUnitedStatesofAmerica.
10.1016/j.rse.2010.07.010. https://doi.org/10.1073/pnas.0808212106.
Cohen,W.B.,Yang,Z.,Stehman,S.V.,Schroeder,T.A.,Bell,D.M.,Masek,J.G.,...Meigs, Meigs,G.W.,Kennedy,R.E.,Gray,A.N.,Gregory,M.J.,2015.Spatiotemporaldynamicsof
G.W.,2016.ForestdisturbanceacrosstheconterminousUnitedStatesfrom recentmountainpinebeetleandwesternsprucebudwormoutbreaksacrossthe
1985–2012:theemergingdominanceofforestdecline.ForestEcologyand PacificNorthwestRegion.USA.ForestEcologyandManagement339(1),71–86.
Management360,242–252.https://doi.org/10.1016/j.foreco.2015.10.042. https://doi.org/10.1016/j.foreco.2014.11.030.
Cohen,W.B.,Healey,S.P.,Yang,Z.,Stehman,S.V.,Brewer,C.K.,Brooks,E.B.,...Zhu,Z., Mildrexler,D.J.,Zhao,M.,Running,S.W.,2009.TestingaMODISglobaldisturbance
2017.Howsimilarareforestdisturbancemapsderivedfromdifferentlandsattime indexacrossNorthAmerica.RemoteSensingofEnvironment.https://doi.org/10.
seriesalgorithms?Forests.https://doi.org/10.3390/f8040098. 1016/j.rse.2009.05.016.
Cohen,W.B.,Yang,Z.,Healey,S.P.,Kennedy,R.E.,Gorelick,N.,2018.ALandTrendr Milesi,C.,Elvidge,C.D.,Nemani,R.R.,Running,S.W.,2003.Assessingtheimpactof
multispectralensembleforforestdisturbancedetection.RemoteSensingof urbanlanddevelopmentonnetprimaryproductivityinthesoutheasternUnited
Environment.https://doi.org/10.1016/j.rse.2017.11.015. States.RemoteSensingofEnvironment.https://doi.org/10.1016/S0034-4257(03)
Coops,N.C.,Gillanders,S.N.,Wulder,M.A.,Gergel,S.E.,Nelson,T.,Goodwin,N.R.,2010. 00081-6.
Assessingchangesinforestfragmentationfollowinginfestationusingtimeseries Pengra,B.,Gallant,A.,Zhu,Z.,Dahal,D.,2016.Evaluationoftheinitialthematicoutput
Landsatimagery.ForestEcologyandManagement259(12),2355–2365.https://doi. fromacontinuouschange-detectionalgorithmforuseinautomatedoperationalland-
org/10.1016/j.foreco.2010.03.008. changemappingbytheU.S.GeologicalSurvey.RemoteSensing8(10),811.https://
Dwyer,J.L.,Roy,D.P.,Sauer,B.,Jenkerson,C.B.,Zhang,H.K.,Lymburner,L.,2018. doi.org/10.3390/rs8100811.
Analysisreadydata:enablinganalysisofthelandsatarchive.RemoteSensing. Potapov,P.V.,Turubanova,S.A.,Hansen,M.C.,Adusei,B.,Broich,M.,Altstatt,A.,...
https://doi.org/10.3390/rs10091363. Justice,C.O.,2012.QuantifyingforestcoverlossinDemocraticRepublicofthe
Emanuel,K.,2005.Increasingdestructivenessoftropicalcyclonesoverthepast30years. Congo,2000–2010,withLandsatETM+data.RemoteSensingofEnvironment122,
Nature.https://doi.org/10.1038/nature03906. 106–116.https://doi.org/10.1016/j.rse.2011.08.027.
Foga,S.,Scaramuzza,P.L.,Guo,S.,Zhu,Z.,Dilley,R.D.,Beckmann,T.,...Laue,B.,2017. Qiu,S.,Lin,Y.,Shang,R.,Zhang,J.,Ma,L.,Zhu,Z.,...Zhu,Z.,2019.MakingLandsat
ClouddetectionalgorithmcomparisonandvalidationforoperationalLandsatdata timeseriesconsistent:evaluatingandimprovingLandsatanalysisreadydata.Remote
products.RemoteSensingofEnvironment.https://doi.org/10.1016/j.rse.2017.03. Sensing11(1),51.https://doi.org/10.3390/RS11010051.
026. Racine,C.,Jandt,R.,Meyers,C.,Dennis,J.,2004.Tundrafireandvegetationchange
Franklin,S.E.,Ahmed,O.S.,Wulder,M.A.,White,J.C.,Hermosilla,T.,Coops,N.C.,2015. alongahillslopeontheSewardPeninsula,Alaska,U.S.A.Arctic,Antarctic,and
Largeareamappingofannuallandcoverdynamicsusingmultitemporalchange AlpineResearch.https://doi.org/10.1657/1523-0430.((2004)036[0001:TFAVCA]2.
detectionandclassificationofLandsattimeseriesdata.CanadianJournalofRemote 0.CO;2).
Sensing41(4),293–314.https://doi.org/10.1080/07038992.2015.1089401. Saunders,M.A.,Lea,A.S.,2008.Largecontributionofseasurfacewarmingtorecent
Fry,J.,Xian,G.,Jin,S.,Dewitz,J.,Homer,C.G.,Limin,Y.,...Wickham,J.,2011. increaseinAtlantichurricaneactivity.Nature.https://doi.org/10.1038/
Completionofthe2006nationallandcoverdatabasefortheconterminousUnited nature06422.
States.PhotogrammetricEngineeringandRemoteSensing.77(9),858–864. Senf,C.,Pflugmacher,D.,Wulder,M.A.,Hostert,P.,2015.Characterizingspectral-tem-
Goldenberg,S.B.,Landsea,C.W.,Mestas-Nuñez,A.M.,Gray,W.M.,2001.Therecent poralpatternsofdefoliatorandbarkbeetledisturbancesusingLandsattimeseries.
15

Z.Zhu,etal. Remote Sensing of Environment 238 (2020) 111116
RemoteSensingofEnvironment170,166–177.https://doi.org/10.1016/j.rse.2015. Zhu,Z.,Woodcock,C.E.,2012.Object-basedcloudandcloudshadowdetectionin
09.019. Landsatimagery.RemoteSensingofEnvironment118,83–94.https://doi.org/10.
Song,X.-P.,Hansen,M.C.,Stehman,S.V.,Potapov,P.V.,Tyukavina,A.,Vermote,E.F., 1016/j.rse.2011.10.028.
Townshend,J.R.,2018.Globallandchangefrom1982to2016.Nature.https://doi. Zhu,Z.,Woodcock,C.E.,2014a.Automatedcloud,cloudshadow,andsnowdetectionin
org/10.1038/s41586-018-0411-9. multitemporalLandsatdata:analgorithmdesignedspecificallyformonitoringland
Stromberg,D.,2007.Naturaldisasters,economicdevelopment,andhumanitarianaid. coverchange.RemoteSensingofEnvironment152,217–234.https://doi.org/10.
JournalofEconomicPerspectives.https://doi.org/10.1257/jep.21.3.199. 1016/j.rse.2014.06.012.
Tibshirani,R.,2011.Regressionshrinkageandselectionviathelasso:aretrospective. Zhu,Z.,Woodcock,C.E.,2014b.Continuouschangedetectionandclassificationofland
JournaloftheRoyalStatisticalSociety.SeriesB:StatisticalMethodology.https://doi. coverusingallavailableLandsatdata.RemoteSensingofEnvironment144,
org/10.1111/j.1467-9868.2011.00771.x. 152–171.https://doi.org/10.1016/j.rse.2014.01.011.
Turner,M.G.,2010.Disturbanceandlandscapedynamicsinachangingworld.Ecology. Zhu,Z.,Woodcock,C.E.,Olofsson,P.,2012.Continuousmonitoringofforestdisturbance
https://doi.org/10.1890/10-0097.1. usingallavailableLandsatimagery.RemoteSensingofEnvironment122,75–91.
Verbesselt,J.,Zeileis,A.,Herold,M.,2012.Nearreal-timedisturbancedetectionusing https://doi.org/10.1016/j.rse.2011.10.030.
satelliteimagetimeseries.RemoteSensingofEnvironment123(Turner2010), Zhu,Z.,Wang,S.,Woodcock,C.E.,2015a.ImprovementandexpansionoftheFmask
98–108.https://doi.org/10.1016/j.rse.2012.02.022. algorithm:cloud,cloudshadow,andsnowdetectionforLandsats4–7,8,andSentinel
Westerling,A.L.,Hidalgo,H.G.,Cayan,D.R.,Swetnam,T.W.,2006.Warmingandearlier 2images.RemoteSensingofEnvironment159,269–277.https://doi.org/10.1016/j.
springincreaseWesternU.S.forestwildfireactivity.Science.https://doi.org/10. rse.2014.12.014.
1126/science.1128834. Zhu,Z.,Woodcock,C.E.,Holden,C.,Yang,Z.,2015b.GeneratingsyntheticLandsat
Westerling,A.L.,Turner,M.G.,Smithwick,E.A.H.,Romme,W.H.,Ryan,M.G.,2011. imagesbasedonallavailableLandsatdata:predictingLandsatsurfacereflectanceat
ContinuedwarmingcouldtransformGreaterYellowstonefireregimesbymid-21st anygiventime.RemoteSensingofEnvironment162,67–83.https://doi.org/10.
century.Proceedingsofthe.NationalAcademyofSciences. https://doi.org/10. 1016/j.rse.2015.02.009.
1073/pnas.1110199108. Zhu,Z.,Gallant,A.L.,Woodcock,C.E.,Pengra,B.,Olofsson,P.,Loveland,T.R.,...Auch,
Xin,Q.,Olofsson,P.,Zhu,Z.,Tan,B.,Woodcock,C.E.,2013.Towardnearreal-time R.F.,2016.Optimizingselectionoftrainingandauxiliarydataforoperationalland
monitoringofforestdisturbancebyfusionofMODISandLandsatdata.Remote coverclassificationfortheLCMAPinitiative.ISPRSJournalofPhotogrammetryand
SensingofEnvironment135,234–247.https://doi.org/10.1016/j.rse.2013.04.002. RemoteSensing122,206–221.https://doi.org/10.1016/j.isprsjprs.2016.11.004.
Zhu,Z.,2017.ChangedetectionusingLandsattimeseries:areviewoffrequencies,pre- Zhu,Z.,Qiu,S.,He,B.,Deng,C.,2018.CloudandcloudshadowdetectionforLandsat
processing,algorithms.andapplications.ISPRSJournalofPhotogrammetryand images:thefundamentalbasisforanalyzingLandsattimeseries.In:RemoteSensing
RemoteSensing130,370–384.https://doi.org/10.1016/j.isprsjprs.2017.06.013. TimeSeriesImageProcessing.CRCPress,pp.25–46.
16

Update
Remote Sensing of Environment
Volume 244, Issue , July 2020, Page
DOI: https://doi.org/10.1016/j.rse.2020.111824

Remote Sensing of Environment 244 (2020) 111824
ContentslistsavailableatScienceDirect
|     |     | Remote  | Sensing   |                             | of Environment |     |     |     |
| --- | --- | ------- | --------- | --------------------------- | -------------- | --- | --- | --- |
|     |     | journal | homepage: | www.elsevier.com/locate/rse |                |     |     |     |
Corrigendum
Corrigendum to continuous monitoring of land disturbance based on
T
Landsat time series, remote sensing of environment, 238, (2020), 11116
ZheZhua,b,⁎
,JunxueZhanga,b,ZhiqiangYangc,AmalH.Aljaddanib,WarrenB.Cohend,e,ShiQiub,
| Congliang | Zhoub |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
aDepartmentofNaturalResourcesandtheEnvironment,UniversityofConnecticut,Storrs,CT06269,UnitedStates
bDepartmentofGeosciences,MS1053,ScienceBuilding125,TexasTechUniversity,Lubbock,TX79409,UnitedStates
cUSDAForestService,RMRSResearchStation,50725thStreet,Ogden,UT84401,UnitedStates
dDepartmentofForestEcosystemsandSociety,OregonStateUniversity,Corvallis,OR97331,UnitedStates
ePacificNorthwestResearchStation,U.S.ForestService,Corvallis,OR97331,UnitedStates
:CoefficientforoverallvaluefortheithLandsatBand
| TheauthorsregretthatatypowasdiscoveredinEq.(1),wherethe |     |     |     |     | a   |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0,i
variable‘k’wasnotincluded.Eq.(1)shouldbecorrectedasfollows: a , b : Coefficients for intra-annual change for the ith Landsat
k, i k, i
Band
| +∑3 | 2kπ | 2kπ |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ρ =a ⎧a cos⎛ x⎞+b sin⎛ x⎞⎫+c x c :Coefficientforinter-annualchange(slope)fortheithLandsat
| i,x 0,i | k=1 ⎨⎩ k,i T | k,i T ⎠⎬⎭ | 1,i |     | 1,i                      |                     |                  |      |
| ------- | ------------ | --------- | --- | --- | ------------------------ | ------------------- | ---------------- | ---- |
|         | ⎝            | ⎠ ⎝       |     | (1) | Band                     |                     |                  |      |
|         |              |           |     |     | ρ^ : Surface reflectance | for the ith Landsat | Band at x Julian | date |
| where,  |              |           |     |     | i,x                      |                     |                  |      |
frommodelprediction.
x:Juliandate
Theauthorswouldliketoapologiseforanyinconveniencecaused.
i:TheithLandsatBand(i=1,2,3,4,5,and7)
_______________________
k:Temporalfrequencyofharmoniccomponent(k=1,2,and3).
DOIoforiginalarticle:https://doi.org/10.1016/j.rse.2019.03.009
T:Numberofdaysperyear(T=365.25)
| DOIoforiginalarticle: | https://doi.org/10.1016/j.rse.2019.03.009 |     |     |     |     |     |     |     |
| --------------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
⁎Correspondingauthorat:DepartmentofNaturalResourcesandtheEnvironment,UniversityofConnecticut,Storrs,CT06269,UnitedStates.
E-mailaddress:zhe@uconn.edu(Z.Zhu).
https://doi.org/10.1016/j.rse.2020.111824
Available online 17 April 2020
0034-4257/ © 2020 Elsevier Inc. All rights reserved.
