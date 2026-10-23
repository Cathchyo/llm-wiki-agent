Article
A Novel Framework for Long-Term Forest Disturbance
Monitoring: Synergizing the LandTrendr Algorithm with CNN
in Northeast China
ZhaoyiZheng,YingYu* ,XiguangYang ,XinyiYuanandZhuohanHou
SchoolofForestry,NortheastForestryUniversity,Harbin150040,China;2021214017@nefu.edu.cn(Z.Z.);
yangxiguang@nefu.edu.cn(X.Y.);yuanxinyi7@nefu.edu.cn(X.Y.);parzival@nefu.edu.cn(Z.H.)
* Correspondence:yuying@nefu.edu.cn;Tel.:+8618204618971
Highlights
• ALandTrendr-CNNframeworkachieves92.26%accuracyinclassifyingforestdistur-
bances.
• NBRandSWIR2bandsarekeyfordetectingfire,pest,andgeologicaldisturbances
• Multi-sourcevalidationintegratesLandsat,fire,pest,logging,andhazarddata.
• Slopeanalysisrevealsdistinctdisturbancepatternsacrosstopographicgradients.
Abstract
Ascarboncyclingandglobalenvironmentalprotectiongainincreasingattention,forest
disturbanceresearchhasintensifiedworldwide. Constrainedbylimiteddataavailability,
existingframeworksoftenrelyonextractingindividualspectralbandsforsimplebinary
disturbancedetection,lackingsystematicapproachestovisualizeandclassifycausesof
disturbanceoverlargeareas. Accuratelyidentifyingdisturbancetypesiscriticalbecause
differentdisturbances(e.g.,fires,logging,pests)exhibitvastlydifferentimpactsonforest
structure,successionalpathwaysand,consequently,forestcarbonsequestrationandstorage
capacities. This study proposes an integrated remote sensing and deep learning (DL)
methodforforestdisturbancetypeidentification,enablinghigh-precisionmonitoringin
AcademicEditor:BrendenE.McNeil Northeast China from 1992 to 2023. Leveraging the Google Earth Engine platform, we
integrated Landsat time-series data (30 m resolution), Global Forest Change data, and
Received:9September2025
Revised:20October2025 othermulti-sourcedatasets. Weextractedfourkeyvegetationindices(NDVI,EVI,NBR,
Accepted:21October2025 NDMI)toconstructlong-termforestdisturbancefeatureseries. Acomparativeanalysis
Published:23October2025 showedthattheproposedconvolutionalneuralnetwork(CNN)modelwithsixfeature
Citation: Zheng,Z.;Yu,Y.;Yang,X.; bandsachieved5.16%higheroverallaccuracyanda6.92%higherKappacoefficientthana
Yuan,X.;Hou,Z.ANovelFramework randomforest(RF)algorithm. Remarkably,evenwithonlysixfeatures,theCNNmodel
forLong-TermForestDisturbance
outperformedtheRFmodeltrainedonfifteenfeatures,achievinga0.4%higheroverall
Monitoring:Synergizingthe
accuracyanda0.58%higherKappacoefficient,whileutilizing60%fewerparameters. The
LandTrendrAlgorithmwithCNNin
CNNmodelaccuratelyclassifiedforestdisturbances—includingfires,pests,logging,and
NortheastChina.RemoteSens.2025,17,
3521. https://doi.org/10.3390/ geologicaldisasters—achievinga92.26%overallaccuracyandan89.04%Kappacoefficient.
rs17213521 This surpasses the 81.4% accuracy of the Global Forest Change product. The method
significantly improves the spatiotemporal accuracy of regional-scale forest monitoring,
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. offeringarobustframeworkfortrackingecosystemdynamics.
Thisarticleisanopenaccessarticle
distributedunderthetermsand Keywords: forest disturbance; LandTrendr algorithm; deep learning; long time-series;
conditionsoftheCreativeCommons CNN;secondaryclassification;randomforest
Attribution(CCBY)license
(https://creativecommons.org/
licenses/by/4.0/).
RemoteSens.2025,17,3521 https://doi.org/10.3390/rs17213521

RemoteSens.2025,17,3521 2of25
1. Introduction
As an important component of global ecosystems, forests have a direct impact on
the stabilityand function ofecosystems. Forest disturbance, as a typeof forest change,
notonlyaltersthespeciescomposition,structure,andbiodiversityofforestsbutalsohas
a profound impact on ecological processes such as carbon storage, soil protection, and
the water cycle[1,2]. With the rapid development of remote sensing technology, forest
disturbancemonitoringusingsatelliteimageryhasbecomeanimportanttoolforglobal
forest management and ecological environment assessment. The types of forest distur-
bancesarenumerousandcomplex,includingfires,pests,diseases,andhumanlogging.
Thesedifferentformsofdisturbanceshavedifferentimpactsonforestecosystems. While
significantprogresshasbeenmadeinthedetectionandmonitoringofsingle-typedistur-
bances,acriticalresearchgapremainsinthereliableclassificationofmultipleco-existing
orspectrallysimilardisturbancetypes(e.g.,pestsvs. diseases,loggingvs. geologicaldisas-
ters). Currentmethodologiesoftenlackthegeneralizabilityandprecisiontodisentangle
thiscomplexity,creatinganurgentneedforarobustframeworkcapableofhigh-accuracy,
multi-classdisturbancetyping.
Substantial progress has been made in developing time-series algorithms (e.g.,
VegetationChangeTracker(VCT),BreaksforAdditiveSeasonandTrend(BFAST),Continu-
ousChangeDetectionandClassification(CCDC),LandTrendr)fordetectingtheoccurrence,
timing, and extent of forest disturbances with high accuracy [3–8]. As summarized in
AppendixB,thesemethodsexcelatidentifyingthatadisturbancehashappenedbutare
primarilydesignedforchangedetectionratherthanthedifferentiationofdisturbancetypes.
Afterdetectingforestdisturbanceareas,secondaryclassificationofdisturbancecategories
is necessary to meet ecological monitoring requirements, facilitating the identification
ofdisturbancecauses(e.g.,fires,logging,pestsanddiseases,geologicalhazards)within
the region. Globally, researchers have widely applied machine learning algorithms for
secondaryclassificationofforestdisturbances. Algorithmssuchasrandomforest(RF)and
support vector machine (SVM) have been used to process multi-source remote sensing
data,enhancingtheclassificationaccuracyandrobustness. Byintegratingmultiplefeatures
(e.g.,spectralindices,texturefeatures),thesealgorithmseffectivelydistinguishdifferent
disturbancetypes.
Deeplearningalgorithmsalsodemonstratestrongperformanceinthesecondaryclas-
sificationofforestdisturbances,particularlywhenhandlingcomplexremotesensingdata.
Convolutionalneuralnetworks(CNNs),acornerstonearchitectureforprocessingimage
data (e.g., high-resolution remote sensing imagery), can automatically extract features
fromremotesensingimages,enablinghigh-precisionclassificationofdisturbancetypes.
UtilizingCNNsforforestdisturbancetypeclassificationisexpectedtoprovidelarge-scale
forestdisturbancemapswithdetaileddisturbanceinformation[9]. Althoughvariousdeep
learning algorithms such as ResNet [10], Recurrent Neural Network (RNN) [11], Long
Short-TermMemory(LSTM)[12],andGraphConvolutionalNetwork(GCNs)canbeap-
pliedtoforestdisturbanceclassification[13],westillchoosetheCNNalgorithmdueto
itsprovenabilitytocapturespatial–temporalpatternsofdisturbancewithrelativelylow
computationalcost.
Inthisstudy,forestdisturbanceareasacrossthestudyregionfrom1992to2023were
extractedusingtheLandTrendralgorithm,whichwasappliedtoLandsat5,7,and8image
data combined with various vegetation indices. Global Forest Change datasets, forest
firedisturbancedata,pestanddiseasedata,geologicaldisasterdata,andhuman-induced
deforestationdatawereintegratedtodeterminedisturbancecategoriesandconstructthe
disturbancecategorydataset. Subsequently,CNNandrandomforestmodels(withvarying
numbersoffeatures)wereemployedtoclassifytheforestdisturbances,achievinghigh-

RemoteSens.2025,17,3521 3of25
accuracyvisualizationof30m-resolutiondisturbancecategorymapsforNortheastChina
(Figure1).
Figure1.Experimentalflowchart.
2. MaterialsandMethods
2.1. StudyAreaOverview
ThethreeprovincesofChina(Heilongjiang,Jilin,andLiaoning)consideredinthis
study are located in the northeast of China, with geographic coordinates ranging from
40◦Nto55◦Nand120◦Eto135◦E(Figure2). Mostoftheregionhasatemperatemonsoon
climatewithrelativelylimitedheatresources,andthemeanannualtemperatureranges
from2◦Cto6◦C.Precipitationischaracterizedbyaclearrain–heatcycle,withobvious
rain–heatsynchronizationcharacteristics,andismainlyconcentratedinsummer,withmore
rainfallinthesoutheastandlessinthenorthwestinregardtospatialdistribution. Thetotal
annualprecipitationrangesfrom500to800mm. Forestecosystemsunderthisclimateare
vulnerabletoextremeweatherevents(e.g.,drought,highwinds,heavyrainfall)[14]. The
terrainisdominatedbyplains,hills,andmountains,andthelandcoverisdominatedby
woodlands,scrublands,andcroplands,withabundantandconcentratedforestresources.
Accordingtothelatestdata,theforestcoveragerateis43.78%forHeilongjiangProvince,
41.49%forJilinProvince,and39.24%forLiaoningProvince. Thereisavarietyofforest
types, mainly including coniferous forests (e.g., red pines and larch), mixed coniferous
and broadleaf forests, and deciduous broadleaf forests, with significant changes in the
dynamics of forests in the region. In terms of natural factors, under the influence of

RemoteSens.2025,17,3521 4of25
amonsoonclimate,forestfires(especiallyinspringandfall)areanimportantsourceof
naturaldisturbancesintheregion;atthesametime,wind-drivendisasterscausedbystrong
convectivewinds,heavyprecipitation,secondarydisasters,andpestoutbreaksoccurfrom
timetotimeintheregion[15,16]. Asforanthropogenicactivities,asatraditionalforest
managementarea,forestharvesting(includingcommercialloggingandnurserylogging)
isthemainanthropogenicactivitythatchangestheforestcover, whiletheconstruction
ofroadsintheforestarea,theexpansionoftheedgeofagriculturalreclamation[17,18],
thedevelopmentofminerals,andtheconstructionoftourisminfrastructurealsoaffectthe
stabilityoftheforestedareatodifferentdegrees[19]. Therefore,thisnortheasternregion
hasbecomeatypicalandimportantareaforthestudyofforestdisturbancesandtheirtype
identification[17].
Figure2.DistributionmapofforestlandinNortheastChina.
2.2. DataSourcesandPreprocessing
2.2.1. Landsat5/7/8Data
Landsat series satellite data were acquired from the US Geological Survey (USGS)
publicarchiveplatform(https://earthexplorer.usgs.gov/,accessedon10January2025).
ThedatasetincludesLandsat5ThematicMapper(TM)imagery(1984–2011),Landsat7
EnhancedThematicMapperPlus(ETM+)imagery(1999–2022),andLandsat8Operational
LandImager/ThermalInfraredSensor(OLI/TIRS)imagery(2013–2023)(Table1),spanning
theperiod1984–2023witha30mspatialresolution;thesedatacovertheentirenortheastern
region. Tominimizeseasonaleffectsonvegetationsignals,imagesbetweenJune20and
August10wereprioritized. AlthoughthedatawerepreprocessedbyUSGSandGoogle
Earth Engine (GEE), additional cloud removal and masking were applied. The FMask
algorithm was implemented to automatically mask clouds, cloud shadows, and snow,
ensuring > 80% valid pixels per scene. Forest areas (coniferous, broadleaf, and mixed
forests)wereextracted,usingtheESAClimateChangeInitiative(CCI)LandCoverdataset
(v2.0.7, 300 m resolution) as a mask template. This excluded non-forest disturbances
(e.g.,croplands,waterbodies,andurbanareas)fromsubsequentanalyses.

RemoteSens.2025,17,3521
5of25
Table1.EquivalentmultispectralbandsacrossLandsatsensors.
Landsat8
GeneralBandNumber Landsat5TM Landsat7ETM+ Band WavelengthRange(µm)
OLI/TIRS
| B1  |     | B1                       | B1  | B2  | Blue  | 0.45–0.52/0.45–0.51 |
| --- | --- | ------------------------ | --- | --- | ----- | ------------------- |
| B2  |     | B2                       | B2  | B3  | Green | 0.52–0.60/0.53–0.59 |
| B3  |     | B3                       | B3  | B4  | Red   | 0.63–0.69/0.64–0.67 |
| B4  |     | B4                       | B4  | B5  | NIR   | 0.76–0.90/0.85–0.88 |
| B5  |     | B5                       | B5  | B6  | SWIR1 | 1.55–1.75/1.57–1.65 |
| B7  |     | B7                       | B7  | B7  | SWIR2 | 2.08–2.35/2.11–2.29 |
|     |     | 2.2.2. AuxiliaryDatasets |     |     |       |                     |
(1)GlobalForestChange[20]
This 30 m resolution dataset (2000–2022) from the University of Maryland com-
prises three layers: tree cover, forest loss, and forest gain. It was cross-validated with
the Landsat data to identify long-term forest cover trends and served as a baseline for
disturbanceanalysis.
(2)Treecoverlossduetofire[21]
The global 30 m resolution forest fire grids (University of Maryland) were used.
Firelocationsandtimestampswithinthestudyarea(2001–2023)wereextractedandinte-
gratedwithLandsattemporalanalysistoquantifytheextentandintensityoffire-induced
forestloss.
(3)ForestPestandDiseaseData
The Northeast China Forest Pest and Disease Dataset (2023) was integrated with
field survey records of outbreak locations. Spatial analysis was conducted to delineate
pest/diseasedisturbanceimpacts.
(4)LEAF[22]
The 30 m resolution Long-term HarvEst and Allocation of Forest Biomass (LEAF)
dataset (Peking University) was processed to map harvesting locations and scales
(2003–2018). Harvest-inducedcarbondynamicswereestimatedthroughintegrationwith
forestrystatistics.
(5)GeologicalHazardData
Spatialdistributionsofhazards(landslides,debrisflows,collapses,andgroundsub-
sidence)wereobtainedfromtheNationalGeologicalHazardPointDataset(Geograph-
ical Remote Sensing Ecology Network). Only hazards intersecting the forested areas
wereretained.
TheaccesslinksfortheabovedatasetscanbefoundinAppendixA.
|     |     | 2.2.3. VegetationIndexCalculation |     |     |     |     |
| --- | --- | --------------------------------- | --- | --- | --- | --- |
Toquantifychangesinthestateofforestecosystems,thevegetationindicespresented
inTable2werecalculated.
Table2.Comparisontableofvegetationindiceswiththeirformulasandsignificance.
| Name |     | Formula |     |     | Significance |     |
| ---- | --- | ------- | --- | --- | ------------ | --- |
ρNIR−ρSWIR2 Thisindexissensitivetoburnscarsandiscapableofdetectingvegetation
| NBR |     | ρNIR+ρSWIR2 |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- |
recoveryprocessesfollowingfireswithinashortperiod(1–3years).
Thisindexreducesatmosphericandsoilbackgrounddisturbances,andis
| EVI | G×  | ρNIR− ρRED |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- |
ρNIR+C1×ρRED− C2×ρBLUE+L suitableforlong-termmonitoringinhigh-biomassforestareas.
Thisindexiswidelyusedforassessingvegetationcoverandphotosynthetic
| NDVI |     | ρNIR− ρRED |     |                                                |     |     |
| ---- | --- | ---------- | --- | ---------------------------------------------- | --- | --- |
|      |     | ρNIR+ρRED  |     | intensity,butitissensitivetosaturationeffects. |     |     |
ρNIR− ρSWIR1 Thisindexreflectsvegetationcanopymoisturecontent,andisusefulforearly
NDMI
|     |     | ρNIR+ρSWIR1 |     | warningofdroughtstressorpestinfestations. |     |     |
| --- | --- | ----------- | --- | ----------------------------------------- | --- | --- |

RemoteSens.2025,17,3521 6of25
Table2.Cont.
Name Formula Significance
Byintroducingbluebandcorrectionforredbandatmosphericscatteringeffects,
ARVI ρNIR−(2ρRED−ρBlue) thisindexismoresuitablethanNDVIforareaswithhighlevelsofairpollution
ρNIR+(2ρRED−ρBlue)
oraerosolconcentration,improvingthestabilityofvegetationmonitoring.
Replacingtheredband(Red)withthegreenband(Green)makesthisindex
GNDVI ρNIR−ρGREEN moresensitivetochlorophyllcontentinleaves,anditiscommonlyusedto
ρNIR+ρGREEN
assessphotosyntheticactivityandvegetationstress.
Bycomparingthegreenbandwithshortwaveinfrared,thesensorenhancesthe
MNDWI ρGREEN−ρSWIR abilitytodistinguishbetweenwaterbodiesandbackgrounds(suchasbuildings
ρGREEN+ρSWIR
andsoil),makingitsuitableforwetlandvegetationdetection.
Thisindexsimplyreflectsvegetationgreenness,makingitsuitableforareas
RVI
ρNIR
withlowcoverage,butitiseasilyaffectedbylightingconditionsandsoil
ρRED
backgrounddisturbances.
SAVI ρNIR−ρRED ×(1+L) ByintroducingthesoiladjustmentfactorL(0.5),backgrounddisturbancesin
ρNIR+ρRED+L baresoilorlowvegetationcoverageareasarereduced.
2.2.4. Multi-SourceValidationSampleConstruction
In this study, a multi-source sample construction method was used to construct
a spatiotemporal validation framework on Google Earth Engine (GEE) by integrating
LandTrendrimagemaps,GlobalForestChangedatasets,USGSglobalforestfiredistur-
bancedata,PekingUniversityglobalchangeandterrestrialecosystemsdisturbancedatasets,
andnortheastregionpestanddiseasethematicdata. Thedatasetcontainsbothdisturbed
andundisturbedsamples. Theselectionprocessfordisturbedsamplesspecificallyincluded
multi-temporalvisualinterpretation,utilizingLandsat5/7/8historicalimagetime-series
(1992–2023),supplementedwithGoogleEarthhistoricalimagery,andcombinedwithdy-
namictrajectoryanalysistoverifythetypeofdisturbance. Eachsamplepointmustmeet
theevidencechainsupportofatleasttwoindependentyears;qualitycontrolofthesamples
was conducted, and a three-level validation system was established (automatic screen-
ing→independentvisualinterpretation→verificationofcontroversialsampledataset).
Finally,3100validationsampleswereconstructed,andtheirspatialdistributionandsample
categorycompositionareshowninTable3. Theselectioncriteriaforundisturbedsamples
werethatnospectralchangesignalsappearedinthelong-termtime-series,nodisturbance
records in the aforementioned auxiliary datasets, and no disturbance changes detected
intheforestareasthroughvisualinterpretation. Ultimately, 2233undisturbedsamples
wereconstructed.
Table3.Samplecategorycomposition.
DisturbanceType Samplesize Percentage(%) TimeSpan SpatialDistribution
Fire 656 21.1 2001–2023 DaHingganRidgeForestFireHotspot
DiseaseandPest 673 21.7 1992–2023 DensePlantationForestArea
Artificiallogging 943 30.4 2003–2018 BufferZoneNearRoadsandBuildings
Grounddisaster 828 26.7 1992–2023 CoreAreaofNortheastForestRegion
2.3. Methodology
2.3.1. LandTrendrAlgorithm
TheLandTrendralgorithmisaforestdisturbancedetectionmethodbasedontime-
seriessegmentedregression,whichiscapableofcapturingsuddenevents(e.g.,fire,logging)
andlong-termgradualprocesses(e.g.,pestsanddiseases)offorestcover. Inthisstudy,we
implementedtheLandTrendralgorithmbasedontheGoogleEarthEngine(GEE)platform
(AppendixC),andcombineditwiththetime-seriesanalysisofmultiplevegetationindices
toextractforestdisturbanceinformationfromthestudyarea. Thecoreofthealgorithmis
tofitthevegetationindextime-seriesviaasegmentedlinearmodeltoidentifythesudden
changepoints(breakpoints)andthegradualtrendinforestcover[23].

RemoteSens.2025,17,3521 7of25
TheperformanceoftheLandTrendralgorithmishighlydependentontheparame-
ter settings, and this study identified the key parameters through pre-experimentation
(Table4).
Table4.LandTrendrmodelparametersettings.
Parameters Value ParameterDescription
Max.Segments 7 Themaximumnumberofsegmentsfittedonthetime-series.
SpikeThreshold 0.9 Thethresholdforsuppressingspikes.
VertexCountOvershoot 3 Thenumberofverticesthattheinitialmodelcanoverfit.
PreventOne-YearRecovery True Preventcompletioninjustoneyear.
Iftherecoveryrateofasegmentexceedstherecoverythreshold,thatsegmentis
RecoveryThreshold 0.25
notallowed.
p-valueThreshold 0.05 Ifthefittedp-valueexceedsthisthreshold,thecurrentmodelisdiscarded.
BestModelProportion 0.75 Minimumnumberofverticesformodelselection.
Min.ObservationsNeeded 7 Minimumnumberofobservationsrequiredforoutputfitting.
2.3.2. AccuracyVerificationoftheLandTrendrAlgorithm
TheLandTrendralgorithmcaneffectivelyidentifydisturbedandundisturbedareas.
Weused3100samplepointsasvalidationdatafordisturbedareasand2233samplepointsas
validationdataforundisturbedareas. Becauseofpotentialminorpositionaldiscrepancies
betweenthesedatasetsandourfield-measureddata,wefurtherexpandedthecalculated
rangesforvalidationwithinthe30mand60mbufferzones.
2.3.3. RandomForestandDeepLearningClassificationConstruction
MultidimensionalFeatureSystem
BasedonLandsatspectral–temporal–spatialthree-dimensionalfeatureconstruction,
blue(B1),green(B2),red(B3),near-infrared(B4),short-waveinfrared1(B5),andshort-wave
infrared2(B7)bands[24],aswellasNBR,EVI,NDVI,NDMI,SAVI,GNDVI,andMNDWI,
wereselected,togetherwithARVIandRVIfeatureindices,toformamultidimensional
featuresystem.
RandomForestModelArchitectureDesign
ThisstudyconstructedarandomforestclassificationframeworkbasedontheGEE
platform,andthemodelachievestherapididentificationandspatialmappingofforest
disturbancetypesthroughthecollaborativeanalysisofmulti-sourcefeaturesandtheinte-
grateddecision-makingmechanism. Thecorecomponentsofthenetworkarchitectureare
asfollows: Inthefeatureoptimizationlayer,15-dimensionalspectralindexfeatures(Land-
sat6bands+9vegetationindices)arefusedtogether,andthesignificanceofeachindex
isdeterminedandappliedtothemodelforcalculation. Intheforestconstructionlayer,
100classificationandregressiontrees(CART)aretrainedinparallel,withbootstrapresam-
√
plingstrategyforindividualtreesandrandomselectionoffeaturesubsets(m= 15 ≈4).
Intheperturbationdiscriminationlayer,themajorityvotingmechanismfusesthesubtree
predictionresultsandoutputsfourtypesofperturbationprobabilitydistributions. The
modeltrainingparametersweresetasshowninTable5.
Table5.Modeltrainingstrategy.
Parameter SettingValue EcologicalSignificance
Numberofdecisiontrees 100 Balancingmodelaccuracyandcomputationalefficiency
Maximumtreedepth 30[25] Controllingmodelcomplexitytopreventoverfitting
Minimumsamplesizefornodesplitting 2(defaultvalue) Maintainingfine-grainedfeaturelearningcapabilities
Featuresubsetsize 4 Enhancingsubtreediversity
Samplingstrategy Bootstrap(defaultscale) Improvinggeneralizationcapabilities
Randomseed 42 Ensuringexperimentalreproducibility

RemoteSens.2025,17,3521
8of25
FeatureimportancewasquantifiedusingtheGiniImportancemethod,whichwas
implementedasthedefaultfeature_importances_attributeintheRandomForestClassifier
oftheScikit-learnlibrary. ThismethodaccumulatesthereductioninGiniimpurityatall
decisiontreenodesplits,usingthefollowingformula:
|     |            | (cid:0) (cid:1) | 1 ∑   | ∑          | (cid:0)       | (cid:1) |     |
| --- | ---------- | --------------- | ----- | ---------- | ------------- | ------- | --- |
|     | Importance | f               | =     | ∆Gini(n)×I | f splitsnoden |         | (1) |
|     |            | j               | N     |            | j             |         |     |
|     |            |                 | trees | n∈T        |               |         |     |
T
where f indicatesafeature,Tisthenumberoftrees,andnisthenumberofnodes. Feature
j
importanceiscalculatedusingthedefaultimplementationinScikit-learn,whichisbased
ontheaveragereductioninGiniimpuritywhensplittingalltreenodes.
| 2.3.4. CNNModelArchitectureDesign |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
The study constructed a convolutional neural network (CNN) to accomplish the
accuraterecognitionofforestdisturbancetypes. Thenetworkarchitecturecontainsthe
followingcorecomponents: Afeatureembeddinglayerthatspatiallymaps6-dimensional
inputfeatures(Landsat6Bands)viaa32-channelconvolutionalkernel(kernel_size=3).
Afeatureabstractionlayerthatcontainstwoconvolutionalmodules,eachconsistingof
convolutionallayer→batchnormalization→rectifiedlinearunit(ReLU)activation→
maximumpooling,with32→64channels. Globalfeaturesaremappedtothecategory
→
space through a fully connected layer (64 4). In the classification decision layer, the
global average pooling is accessed by the fully connected layer (64 → 4), and SoftMax
outputsfourcategoriesofperturbationprobabilitiesthataremathematicallyexpressed
asfollows:
|     |      |     | (cid:16)     | (cid:16) (cid:16) | (cid:16) (cid:17)(cid:17)(cid:17)(cid:17) |     |     |
| --- | ---- | --- | ------------ | ----------------- | ----------------------------------------- | --- | --- |
|     | Hl+1 |     |              |                   | Hl                                        |     |     |
|     |      | =   | MaxPool ReLU | BN Conv1D         |                                           |     | (2) |
Hl
where denotes the feature map of the lth layer, and BN is the batch normalization
operation. Astratifiedrandomsamplingstrategyisusedtodividethedataset(training
set/testset=8:2),andthekeytrainingparametersareasshowninTable6.
Table6.CNNparameters.Thepoolingstrategyofkeepingthefeaturedimensionsconstantduring
modelimplementationcaneffectivelyavoidinformationlossundersmallsampledata,andthefixed
learningratesettingimprovesthestabilityofthetrainingprocess.
| Parameter      |     |     |     |                  | Configuration    |     |     |
| -------------- | --- | --- | --- | ---------------- | ---------------- | --- | --- |
| Optimizer      |     |     |     | Adam(β           | 1=0.9,β 2=0.999) |     |     |
| Learningrate   |     |     |     |                  | 0.0005(fixed)    |     |     |
| Regularization |     |     |     | BatchNorm(m=0.9) |                  |     |     |
| Lossfunction   |     |     |     | CrossEntropyLoss |                  |     |     |
| Trainingepochs |     |     |     |                  | 200epochs        |     |     |
| Batchsize      |     |     |     |                  | 32               |     |     |
2.4. DisturbanceMagnitudeQuantification
To comprehensively evaluate the overall intensity of disturbance for each pixel, a
Synthetic Disturbance Magnitude Index (SDMI) was calculated. This index integrates
informationfromfourvegetationindices(NDVI,EVI,NDMI,andNBR)toavoidpotential
biasesfromanysingleindexandtoprovidearobustone-dimensionalmeasure. Itwas
computedusingthefollowingformula:
|     | (|  | ∆NDVI| | + | ∆EVI| | + | ∆NDMI| | + | ∆NBR|)×1000 |     |     |
| --- | --- | ------ | --------- | ---------- | --------------- | --- | --- |
=
|     | M synth |     |     |     |     |     | (3) |
| --- | ------- | --- | --- | --- | --- | --- | --- |
4
where M representsthesyntheticdisturbancemagnitudevalue(dimensionless)for
synth
∆Indexrepresentsthedifferenceinthecorrespondingvegetationindexvalue
thepixel.

RemoteSens.2025,17,3521 9of25
betweenthepost-disturbanceperiodandthepre-disturbancebaselineperiodforthepixel.
Thenotation| ∆Index |indicatesthattheabsolutevalueofthedifferenceistaken. This
ensuresthatchangesinallindicesareuniformlytreatedasa“deviation”fromthenormal
state,therebymeasuringthepureintensityandpreventingsignalcancelationthatcould
occur if the responses of different indices were in opposite directions. The sum of the
absolutedifferencesismultipliedby1000toscaletheresultintoanintegervalueforeasier
handlingandinterpretation. Thefinaldivisionby4calculatesthearithmeticmeanofthe
absolutechangemagnitudesfromthefourindices,resultinginasingle,syntheticmeasure
of disturbance intensity. A higher value indicates a stronger overall disturbance to the
pixel’svegetationacrossmultipledimensions,includinggreenness,biomass,watercontent,
andburnseverity.
2.5. VerificationMethodsandParameters
Toestimatetheaccuracyofforestdisturbanceextraction,ananalyticalmethodcombin-
ingmultiplevegetationindiceswithdifferentbufferdistanceswasapplied. Theconfusion
matrix(includingfourindicators: truepositive(TP),falsepositive(FP),falsenegative(FN),
andtruenegative(TN))andfiveindicatorsderivedfromtheconfusionmatrix(accuracy,
useraccuracy(UA),produceraccuracy(PA),F1score,andKappa)wereusedforevaluation.
To estimate the accuracy of forest disturbance classification, the predicted results were
compared with the validation dataset, with the results’ accuracy estimated using four
indicators: UA,PA,accuracy,andKappa. Intheconfusionmatrix,TPreferstothenumber
ofsamplescorrectlypredictedaspositivebythemodel,FPreferstothenumberofsamples
incorrectlypredictedaspositive,FNreferstothenumberofsamplesincorrectlypredicted
asnegative,andTNreferstothenumberofsamplescorrectlypredictedasnegative. Ad-
ditionally,accuracyreferstotheproportionofcorrectpredictionsoutofallpredictions,
whichmeasurestheoverallcorrectnessofthemodel. Itsformulais
Accuracy = (TP + TN)/(TP + FP + FN + TN) (4)
UAreferstotheproportionofcorrectlypredictedpositivesamplesamongallsamples
predictedaspositive,measuringthemodel’s“precision.”Theformulais
UA =TP/(TP + FP) (5)
PAreferstotheproportionofactualpositivesamplesthatthemodelcorrectlypredicts,
measuringthemodel’s‘coverage’. Theformulais
PA =TP/(TP + FN) (6)
TheF1scoreisacomprehensivemetricthatcanbetterreflectthetrueperformanceof
themodel. Itsformulais
F1− Score=2×(Precision × Recall)/(Precision + Recall) (7)
Kappaisusedtomeasuretheconsistencybetweentheclassificationresultsandactual
outcomes, taking into account the agreement that may occur by random chance. The
formulais
N×(TP+TN)−[(TP+FP)×(TP+FN)+(FN+TN)×(FP+TN)]
Kappa = (8)
N2−[(TP+FP)×(TP+FN)+(FN+TN)∗(FP+TN)]
whereN=TP+FP+FN+TN.

RemoteSens.2025,17,3521 10of25
3. Results
3.1. ForestDisturbanceExtraction
TheNBR,EVI,NDVI,andNDMItime-seriescalculatedfromLandsatimagesfrom
1992to2023wereimportedintotheGEEplatform,andclouds,snow,waterbodies,and
non-forestedareasweremasked. Segmentedlinearmodelsofthefourvegetationindices
werefittedtoeachpixel,andthelocationsofthebreakpointsandthemagnitudeofchanges
weredetected. ThedateswererestrictedtotheperiodfromJune20toAugust10ofeach
year(forestgrowingseason),andfinallyMann–WhitneyU(MMU)filteringwasperformed
tominimizetheeffectofnoise. TheresultsareshowninFigure3.
Figure3.LandTrendrcalculationresults.Thecombinedmap(Figure3e)wasobtainedbytakingthe
unionoffourvegetationindices(NDVI,NDMI,NBR,andEVI).
UsingthevegetationindeximagesfittedbytheLandTrendralgorithm,itcanbeseen
thatalthoughtheperturbationareasandtimesbasedonthefourvegetationindicesare
approximatelythesame,therearestillsomeareaswithdifferentvaluesfortheseindices,
indicatingdifferentperturbationresults. Intheundisturbedareas,thevaluesofthefour
indicesareapproximatelythesame,reflectinganormalvegetationgrowthpattern. Inthe
disturbedareas,however,thevegetationindicesshowsignificantabruptchanges. This
indicatesthatdifferentvegetationindicespresentdifferentrecognitionresultsfordifferent
disturbancecategories.
AsshowninTable7,theuseoftheLandTrendralgorithmincombinationwiththe
KappaindexforforestdisturbanceextractionachievedaKappacoefficientof0.83,indi-
catinggoodextractionperformance. Amongthevariousindices, theNBRindexyields
goodresultsfordisturbanceextraction. Thisindexexhibitssensitivitytochangesinsoil
moisturecontent,vegetationcover,andvegetationhealth. NDMI,asaconstructionindex,
demonstratesgoodidentificationcapabilitiesforartificialconstructionland. Therefore,
forareasthatwerepreviouslycoveredbyvegetationbutlaterbecameconstructionland,
NDMIhasrelativelyoutstandingidentificationcapabilities.

RemoteSens.2025,17,3521
11of25
Table7.Accuracyassessmentofforestdisturbancedetectionusingvariousvegetationindicesand
bufferdistances.
Buffer
| Index |     | TP  | FP  | FN  | TN  | Accuracy | UA  | PA  | F1Score | Kappa |
| ----- | --- | --- | --- | --- | --- | -------- | --- | --- | ------- | ----- |
Distance
| EVI   | 0   | 2233 | 1989 | 0   | 1111 | 0.627  | 0.5289 | 1      | 0.6919 | 0.3187 |
| ----- | --- | ---- | ---- | --- | ---- | ------ | ------ | ------ | ------ | ------ |
|       | 30  | 2230 | 1488 | 3   | 1612 | 0.7204 | 0.5998 | 0.9987 | 0.7495 | 0.4745 |
|       | 60  | 2211 | 1319 | 22  | 1781 | 0.7485 | 0.6263 | 0.9901 | 0.7673 | 0.5222 |
| NBR   | 0   | 2231 | 817  | 2   | 2283 | 0.8464 | 0.732  | 0.9991 | 0.8449 | 0.6998 |
|       | 30  | 2230 | 580  | 3   | 2520 | 0.8907 | 0.7936 | 0.9987 | 0.8844 | 0.7833 |
|       | 60  | 2230 | 519  | 3   | 2581 | 0.9021 | 0.8112 | 0.9987 | 0.8952 | 0.8052 |
| NDMI  | 0   | 2230 | 883  | 3   | 2217 | 0.8339 | 0.7164 | 0.9987 | 0.8343 | 0.6765 |
|       | 30  | 2230 | 621  | 3   | 2749 | 0.8886 | 0.7822 | 0.9987 | 0.8773 | 0.7781 |
|       | 60  | 2226 | 554  | 7   | 2546 | 0.8948 | 0.8007 | 0.9969 | 0.8881 | 0.7911 |
| NDVI  | 0   | 2231 | 1545 | 2   | 1555 | 0.7099 | 0.5908 | 0.9991 | 0.7426 | 0.4566 |
|       | 30  | 2230 | 1242 | 3   | 1858 | 0.7665 | 0.6423 | 0.9987 | 0.7818 | 0.5550 |
|       | 60  | 2227 | 1138 | 6   | 1962 | 0.7855 | 0.6618 | 0.9973 | 0.7956 | 0.5885 |
| MERGE | 0   | 2226 | 430  | 7   | 2670 | 0.9181 | 0.8381 | 0.9969 | 0.9106 | 0.8360 |
|       | 30  | 2217 | 357  | 16  | 2743 | 0.9301 | 0.8613 | 0.9928 | 0.9224 | 0.8593 |
|       | 60  | 2171 | 294  | 62  | 2806 | 0.9332 | 0.8807 | 0.9722 | 0.9242 | 0.8648 |
To mitigate the inherent sample selection bias and the edge effects of 30 m resolu-
tionimagery,weimplementedastratifiedsamplingstrategy. Samplingwasconducted
in the core area, and disturbed samples were limited to pixels within continuous dis-
turbance patches. An additional exclusion was applied to the edge buffer zone, with
undisturbedsamplescollectedfromareasmorethan60mbeyondthedisturbancebound-
ary. Thismethodsignificantlyimprovedtheaccuracyofallindices(e.g.,theNBRKappa
value increased from 0.73 to 0.81). This improvement validates two key observations:
the spectral distinguishability between disturbed and undisturbed forest categories is
significant,andthismethodeffectivelyreducesmixed-pixelcontaminationattransition
boundaries. Notably,themulti-indicatorfusionmethod(MERGE)achievedpeakperfor-
mance(Kappa=0.86),confirmingLandTrendr’sreliabilityindisturbancecharacterization
whilemaintainingspatialresolution.
3.2. RandomForestDisturbanceClassificationResults
|     |     |     | 3.2.1. RandomForestModelAccuracy |     |     |     |     |     |     |     |
| --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Wedevelopedaclassificationmappingframeworkbasedontherandomforestalgo-
rithmontheGoogleEarthEngineplatform. Byintegratingmulti-sourcetemporalfeatures
withgeospatialanalysis,wegeneratedspatiotemporaldistributiondataandcalculatedthe
accuracyofthemodelinclassifyingforestdisturbancetypesinthenortheastregionfrom
1992to2023(Table8).
Table8.RFmodelaccuracy.
|     |     |     | Category          |          | ProducerAccuracy(PA) |     | UserAccuracy(UA) |        | F1Score |     |
| --- | --- | --- | ----------------- | -------- | -------------------- | --- | ---------------- | ------ | ------- | --- |
|     |     |     | Fire              |          | 0.8837               |     | 0.8976           |        | 0.8906  |     |
|     |     |     | Grounddisaster    |          | 0.9231               |     | 0.9449           |        | 0.9339  |     |
|     |     |     | Artificiallogging |          | 0.9235               |     | 0.9086           |        | 0.9160  |     |
|     |     |     | DiseaseandPest    |          | 0.9412               |     | 0.9275           |        | 0.9343  |     |
|     |     |     |                   | Accuracy |                      |     |                  | 0.9186 |         |     |
|     |     |     |                   | Kappa    |                      |     |                  | 0.8906 |         |     |
From Table 8, it can be seen that the random forest model achieves high accuracy
inthe classification ofalltypes offorest disturbances. TheF1 scoresfor fires, disasters,
logging,andpestsanddiseasesareallabove0.89,indicatingtheRFmodeliscapableof
recognizingthesefourtypesofdisturbances. Theproduceraccuracyanduseraccuracy
arealsoabove0.88,demonstratingthatthemodel’sperformanceinavoidingfalsealarms
andomissionsisexcellent. Theoverallaccuracyreaches0.9186andtheKappacoefficient

RemoteSens.2025,17,3521 12of25
is0.8906,whichfurthervalidatesthereliabilityandstabilityofthemodel. Therefore,the
RFmodelhasgoodidentificationaswellasillustrativecapabilitiesforclassifyingforest
disturbancecategories.
3.2.2. FeatureImportanceAnalysis
Thefeatureimportanceranking(Figure4)showsthattheNBRandSWIR2(B7)bands
contributethemost,confirmingtheuniquesensitivityofthisindextovegetationcanopy
structuredamageandmoisturelossduringLandTrendr’saccuracyidentification. NBR
effectivelyamplifiesspectralresponsedifferencesinburnedareasorareassubjectedto
severedisturbancesbycombiningtheratiocalculationofthemoisture-sensitiveSWIR2
bandandthenear-infraredband. Whenfirescausecanopydestruction,SWIR2reflectance
significantly increases due to exposed bare soil (compared with the low reflectance of
healthyvegetation),andNBRfurtherreinforcesthissignalthroughstandardizedcalcula-
tions. Notably,NBRnotonlycapturesrapidchangesfollowingsuddendisturbances(such
asfires)butalsoexhibitssignificantresponsivenesstoprogressivevegetationdehydration
causedbypestsanddiseases. Thismulti-sensitivitymakesitacoreindicatorfordistur-
banceidentification,andthehighcontributionoftheSWIR2bandpreciselyreflectsthekey
physicalsignificanceoftheNBRindex—acomprehensivecharacterizationofvegetation
moisturecontentandsoil/litterreflectance,asexpressedbythefollowingformula:
1
ρ ∝ +ϵsoil moisture (9)
SWAR2
vegetationcover
Figure4.Importanceleveloffeatureindices.
NBRisspecificallydesignedfordetectingfiredisturbances[26],anditscalculation
formulaemphasizesthecontrastbetweenSWIRandNIRbands. Severedisturbances(such
asfiresorclear-cutting)causeasharpdropinNIRreflectanceandanincreaseinSWIR2
reflectance, resulting in a significantly negative NBR value. Additionally, in previous
LandTrendraccuracyvalidationstudies,NDMIdemonstratedexcellentdisturbanceidenti-
ficationcapabilities;inthisstudy,NDMIalsomanifestsstrongdisturbanceclassification
capabilities.NDMIcaneffectivelydistinguishbetweenconstructionlandandbareland[27],
aswellasbetweenconstructionlandandforestlandasthetwoexhibitdistinctdifferences.
Ifthereisachangefromforestlandtoconstructionlandinthestudyarea,itistypically
identifiedbytherandomforestalgorithmasanareaaffectedbyartificialloggingdistur-

RemoteSens.2025,17,3521 13of25
bances. Furthermore,thecontributionlevelsoftheindividualbandscomprisingNDMIare
relativelyhigh,whichisofsignificantimportanceforthisindex’shighcontributionrate.
Comparedwiththerandomforestalgorithmusingsixoriginalbandswithoutvege-
tationindexfeatures(Table9),therandomforestalgorithmwithninevegetationindices
achievedevenhigheraccuracyscoresinallaspects.
Table9.RF(6-index)modelaccuracy.
Category ProducerAccuracy(PA) UserAccuracy(UA) F1Score
Fires 0.9091 0.8824 0.8955
Grounddisasters 0.9172 0.8636 0.8896
Artificiallogging 0.8457 0.8785 0.8618
DiseasesandPests 0.8258 0.8591 0.8421
Accuracy 0.8710
Kappa 0.8272
3.3. CNNModelPerformanceValidation
3.3.1. DynamicAnalysisoftheTrainingProcess
Figure5showstheevolutionofthelossfunctionandclassificationaccuracyofthe
CNNmodelover200trainingcycles(epochs). BothTrainLossandTestLossintheleft
figureshowanexponentialdecaytrend,whichisinlinewiththetypicalconvergencelaw
ofdeeplearningmodels. Thisindicatesthemodel’searlyabilitytoquicklycapturespectral
features. Aftermoretrainingcycles,thedeclinerateslowsdown,thetraining/validation
loss difference value always stays within 0.05, and the validation batch normalization
(BatchNorm) effectively controls the risk of gradient explosion. It meets the expected
convergencethresholdoftheCrossEntropyLossfunctioninthefour-categoryclassification
task [28]. The training accuracy and validation accuracy in the right figure show syn-
chronousimprovementcharacteristicsandeventuallyreachasteadystate. Thehyperbolic
overlapissignificantlyimprovedafter150cycles,confirmingthemodelarchitecturedesign
(32→64-channel convolution)’s ability to adequately fit the four types of perturbation
featuresinthenortheastregion,withnoover-andunder-fittingphenomena.
Figure5.LosscurveandaccuracycurveofCNN.
TheCNNmodelachievesanoverallaccuracy(OA)of92.26%onthetestset,witha
Kappacoefficientof0.8964. Theconfusionmatrixshowsanaccuracyhigherthan93.9%
fortherecognitionofsuddendisturbances(firesandgeodeticdisasters),andanaccuracy
higherthan89.6%fortheclassificationofpest,disease,andloggingdisturbances(Table10).

RemoteSens.2025,17,3521
14of25
Table10.CNNmodelaccuracy.
| Category          | ProducerAccuracy(PA) | UserAccuracy(UA) | F1Score |
| ----------------- | -------------------- | ---------------- | ------- |
| Fires             | 0.8986               | 0.9394           | 0.9185  |
| Grounddisasters   | 0.8974               | 0.9655           | 0.9302  |
| Artificiallogging | 0.9494               | 0.8989           | 0.9235  |
| DiseasesandPests  | 0.9392               | 0.8968           | 0.9175  |
Accuracy 0.9226
Kappa 0.8964
3.3.2. FeatureImportanceAnalysis
TherelativeimportanceofthespectralfeaturesintheCNNclassificationmodelis
illustratedinFigures6and7. TheB7(SWIR2)bandexhibitsthehighestcontributionto
disturbancediscrimination(indicatedbyitsdominanthorizontalaxislength),significantly
impactingalldisturbancecategories. Vegetationmoistureabsorptioncharacteristicsinthe
SWIRwavelengthsenablethisbandtocapturehydricstressvariationsacrossdisturbance
types. TheB4(Red)band’sutilityarisesfromvegetation’slowreflectanceinthisspectral
region,allowingittosharplydelineateforestedfromnon-forestedareas. Followinggeolog-
icaldisturbances(e.g.,landslidesordebrisflowsthatcauselarge-scaleforestdestruction),
thedrasticreductioninvegetationcoverproducespronouncedreflectanceincreasesinB4.
Consequently,B4exertssubstantiallygreaterinfluenceontheCNNmodel’sgeohazard
classificationdecisionscomparedtootherdisturbancetypes.
Figure6.MeanabsoluteSHAP(averageimpactmagnitudeonmodeloutput).
Figure7.SHAPvalues(impactonCNNmodeloutput).

RemoteSens.2025,17,3521 15of25
3.4. ModelAccuracyComparison
Overall, through the deep mining of spectral–temporal features, the CNN model
achievesanoverallclassificationaccuracyof92.26%whilemaintaininghighcomputational
efficiency,whichisbetterthantraditionalmachinelearningmethods. TheCNNalgorithm
andtherandomforestalgorithmusing15featurebandseachhavetheirownadvantagesfor
theclassificationofthefourdisturbancecategories;theCNNhasasignificantadvantage
overtherandomforestalgorithmintherecognitionofforestfiredisturbances(+2.3%),with
therandomforestalgorithmbeinginferiortotheCNNalgorithmregardlessofitsuseofthe
originalfeaturebandsorthe15featurebands. TheCNNalgorithmalsohasanadvantage
(+0.75%)inrecognizingforestdisturbancescausedbylogging(Figure8). Inaddition,we
conductedsignificancetestsonthethreemodels.Theresultsofthesignificancetestanalysis
canbefoundinAppendixD.
Figure8.Classificationaccuracybycategoryandmethod(*p<0.05;**p<0.01;***p<0.001).
ComparedwiththeCNNmodel,theoverallaccuracyoftherandomforestmodelis
2.3%lower,butithasthefollowingadvantagesforapplications: Randomforestisahead
of CNN in the recognition and classification accuracy of pest and disease disturbances
aswellasgeodeticdisturbances,anditscomputationalefficiencyishigh,whilethetime
requiredfortheclassificationofthewholeregionandthewholeyearismuchlowerthan
thatofdeeplearningalgorithms. RFhasgoodinterpretabilityandprovidesquantitative
indicatorsoffeatureimportancetosupporttheanalysisofecologicalmechanisms. Ithas
strongplatformcompatibility,canbedirectlyintegratedintotheGEEcloudcomputing
framework,andsupportsdynamicupdate(Figure9).

RemoteSens.2025,17,3521 16of25
Figure9.Disturbancecategoryanddistribution.
3.5. VerificationofTypicalDisturbanceEventYears
To verify the disturbance classification results of different years more clearly, this
studyreimportedtheclassificationimagesintotheGEEplatformforvisualverification
andextractedsatelliteimagesofdisturbanceeventsfromthemwithobviousrecognition
effects(Figure10). Itwasfoundthatdifferentindicescouldrecognizedifferenttypesof
disturbances with different focuses, among which the B7 and NBR indices were more
sensitive to fire, pest, and ground disturbances, but B7 was not effective in detecting
clearcuttingdisturbances;theNBRindices,althoughtheycouldrecognizeallfourtypesof
disturbances,wereweakerthanB7forfire,pest,andgrounddisturbanceandweakerthan
EVIandNDVIforclearcuttingdisturbances.
Meanwhile,theforestdisturbancetypesindifferentareashadtheiruniquespectral
trajectoriesandtime-seriescharacteristics.Forexample,firedisturbancesintheHumaRiver
areaandthenorthernpartoftheGreaterKhinganMountainsshowedsignificantchanges
in the vegetation indices before and after the disturbance, and the NBR and B7 indices
wereabletobetterreflectthedegreeandextentoffiredamagetovegetation. Thechanges
in the vegetation indices due to ground disturbances in Fusong County were closely
related to the topographic conditions and soil stability, and the location and influence
rangeofgrounddisturbancescouldbeeffectivelyidentifiedbyanalyzingtheabnormal
changes in these indices. Regarding logging disturbances in Harbin area, the EVI and

RemoteSens.2025,17,3521 17of25
NDVIindicesperformedwellindetectingthechangesinvegetationcoverandwereable
toaccuratelydistinguishbetweenloggedandunloggedareas. InFushunCity,thechanges
inthevegetationindicesexhibitedacertainprogressivenatureduetodisturbancecaused
bypestsanddiseases,andtheNBRindexwasabletocapturethewaterlossandspectral
responsechangesinvegetationintheprocessofpestanddiseaseinfestation,providinga
basisforearlymonitoringandcontrolofpestsanddiseases.
Figure10. Algorithmidentificationofregionssubjectedtodisturbanceeventsandactualimages
oftheseregions.Thefirstrow(a)showstheHumaRiverregion(firedisturbance);thesecondrow
(b)showsthenorthernGreaterKhinganRangeregion(firedisturbance);thethirdrow(c)showsthe
FusongCountyregion(geologicaldisasterdisturbance);thefourthrow(d)showstheHarbinregion
(loggingdisturbance);thefifthrow(e)showstheFushunCityregion(pestanddiseasedisturbance).
ThefirstcolumnshowstheLandsattrue-colorcompositeimagerybeforethedisturbance;thesecond
columnshowsthedetectionresults;thethirdcolumnshowstheimageryofthedisturbanceevent.
Thehorizontalaxisinthegraphrepresentsyear.
4. Discussion
ThisstudyintegratedtheLandTrendralgorithmwithaCNNmodeltoachievehigh-
precisionclassificationoffourtypesofforestdisturbances(fire,pestsanddiseases,geologi-
caldisasters,andhumanlogging)inNortheastChina,withanoverallaccuracyof92.26%.
Thestudyfoundthatdifferentdisturbancetypesexhibitsignificantdifferencesinvegeta-
tionindexresponses,terraindistribution,andtime-seriescharacteristics,outperforming
traditionalmethodsandprovidingimportantevidenceforregionalforestmanagement
andcarboncycleresearch.

RemoteSens.2025,17,3521
18of25
4.1. TerrainGradientandDisturbanceDistribution
Torobustlyassesstheintensityofidentifieddisturbances,weemployedthesynthetic
disturbancemagnitudeindex(M )introducedintheMethods. Thisintegratedmeasure,
synth
reflectingconsolidatedchangesacrossfourvegetationindices,revealedacleargradientof
disturbancestrengthacrossthestudyarea(Table11).
Table11.Correlationbetweendisturbanceamplitudeandslope.
| Slope | Logging  | Fires    | GroundDisasters | DiseasesandPests |
| ----- | -------- | -------- | --------------- | ---------------- |
| <5    | 380.8801 | 425.2484 | 183.8017        | 246.9693         |
| 5–10  | 318.2914 | 379.1219 | 126.2781        | 177.4038         |
| 10–15 | 295.362  | 397.091  | 118.7163        | 165.9079         |
| 15–20 | 284.4945 | 395.7004 | 120.1452        | 166.8593         |
| 20–25 | 279.9943 | 387.9092 | 126.8186        | 165.883          |
| 25–30 | 280.6063 | 390.2207 | 139.1888        | 170.1358         |
| 30–35 | 283.4847 | 375.8809 | 157.8814        | 174.6508         |
| 35–40 | 284.4708 | 323.4955 | 176.2545        | 183.4997         |
| 40–45 | 289.2918 | 335.2328 | 187.3475        | 207.9093         |
| >45   | 286.4268 | 301.2049 | 198.7862        | 229.5157         |
Table 11 shows that the four types of disturbances exhibit significant differences
acrossdifferentslopezones(Table11). Thefourmajorforestdisturbances(logging,fires,
geologicaldisasters,andpestsanddiseases)allexhibitlargerdisturbanceamplitudesin
flatareaswithslopes<5◦. Thisfindingmayreflecttheuniquevulnerabilitycharacteristics
offorestecosystemsinflatareas. Concerningloggingactivities,thedisturbanceamplitude
value of 380.88 in flat areas is significantly higher than in other slope zones. This is
primarilyduetothefactthatflatterrainfacilitatesmechanizedloggingoperationsand
transportationactivities,resultinginasignificantincreaseintheintensityandfrequency
of human disturbances [29]. Fire disturbances also reach the highest value (425.25) in
flat areas, which is related to the increased number of fire sources caused by frequent
humanactivitieswhilealsoreflectingthegreateraccumulationsofcombustiblematerials
inflatareas[30]. Althoughthedisturbanceamplitudesinflatareasarethehighestoverall,
significant differences still exist in regard to the topographic gradient characteristics of
differenttypesofdisturbances. Geologicaldisastersaretheonlydisturbancetypeshowing
amonotonicallyincreasingtrend,withtheirmagnitudeincreasingto198.79insteepslope
areas,clearlydemonstratingthepositivepromotionaleffectofincreasedslopeongeological
disasters[31].
Firedisturbancesexhibitanotablesecondarypeak(397.09)inthe10–15◦ slopezone,
potentiallyrelatedtotheuniquewindspeedandcombustiblematerialdistributioncondi-
tionsinmoderatelyslopedareas[32]. Pestanddiseasedisturbancesshowanunusually
highvalue(207.91)inthe35–45◦ slopezone—aphenomenonthatmayreflecttheunique
vegetation community structure and limited pest control efforts in this slope zone [33].
These findings have important implications for forest management. For example, fire
preventionmeasuresshouldbestrengthenedinmoderatelyslopedareas,whilegeological
hazardsshouldbeprioritizedinsteeplyslopedareas. Theresultsofthisstudyalsopoint
thewayforfutureresearch,particularlytheneedtofurtherexploretheimpactofmicroto-
pographicfeaturesondisturbanceprocessesandtodevelopmorerefinedslopecorrection
algorithmstoimprovemonitoringaccuracyinsteeplyslopedareas.
4.2. EcologicalandManagementImplications
This study is the first to quantify the spatiotemporal patterns of various types of
disturbancesintemperateforestsinNortheastChinaattheregionalscale. High-precision
firedetectionprovidesadatafoundationforfireclassification,whiletheconcentrationof
logginghotspotsinflatareasandurbanregionsrevealstheindirectimpactofurbanization

RemoteSens.2025,17,3521 19of25
onforestcarbonstorage. Additionally,thehighincidenceofgeologicaldisastersinsteeply
slopedareas(areaproportionincreasesby35%whentheslopeexceeds45◦)underscoresthe
needtostrengthenmountainprotectionengineering. Fromamethodologicalperspective,
theCNNmodeloutperformsthemulti-featurerandomforestmodel(15bands)evenwith
limitedfeatures(only6bands),confirmingthepotentialofdeeplearninginremotesensing
time-seriesanalysis.
Higher-precisionforestdisturbanceextractionandclassificationmethodsprovidea
theoreticalfoundationforelucidatingdisturbance–recoveryecologicalmechanisms, ex-
ploringthequantificationandinteractionsofdrivingfactors,andrevealingdisturbance
differentiationpatternsandidentifyingdisturbancefactors(Figure8). Forexample,this
studyfoundthathigh-incidencefirezonesareconcentratedintheGreaterKhinganRange,
whichiscloselyrelatedtotheregion’scontinentalaridclimateandlightning-inducedfire
sources;pestoutbreakhotspotsarecommonlyfoundinartificialforestsinLiaoning/Jilin,
confirmingtheconclusionthatsingle-speciesforestsaremoresusceptibletoinvasion[34];
andlogginghotspotsaredistributedalongroadsandurbannetworks,suggestingurban-
izationeffectsandhumanloggingrisks[35]. Thesefindingsprovideascientificbasisfor
carbonmanagement: firesleadtorapidcarbonrelease(consistentwiththeLEAFdataset),
whileinsectpestdisturbancesmanifestasasustaineddeclineincarbonsinkcapacity. This
iscrucialforrefiningregionalcarbonbudgetsundertheIPCCframework.
4.3. MethodologicalAdvancesandComparativePerformance
TheLandTrendr-CNNcollaborativemethodproposedinthisstudyintegratestempo-
raltrajectoryanalysiswithdeeplearningtechnology,fullyleveragingthetemporalfeature
extractionadvantagesoftheLandTrendralgorithmandthespatialfeatureextractionad-
vantagesoftheCNNalgorithm[36]. Thisapproachachieveshigherclassificationaccuracy
comparedtopreviousstudiesthatusedsingletemporalmodelsortraditionalmachine
learning methods for forest disturbance monitoring. When compared specifically with
the widely used Hansen Global Forest Change (GFC) dataset, which identifies general
forestlosswithoutdistinguishingdisturbancetypes,ourmethoddemonstratesasignifi-
cantadvantageinclassifyingspecificdisturbancetypes. Thestudyshowsthattheoverall
classificationaccuracyforthefourtypesofforestdisturbances(fires,pestsanddiseases,
geological disasters, and human logging) achieved using this method reaches 92.26%,
thus outperforming the Hansen Global Forest Change dataset (81.4%), and accuracy is
alsoimprovedby5.16%whencomparedwiththerandomforest(RF)modelunderthe
sameinputfeatures. Thissuperiorperformancehighlightsthevalueofourapproachfor
applicationsrequiringdetailedinformationondisturbancetypes. Thisresultfullyvalidates
theeffectivenessofthehybridmethodof“time-seriesanalysis+deeplearning”inthefield
ofremotesensinginrecentyears[37].
The core innovations of this method include the proposal of a multidimensional
index combination of NDVI, NBR, EVI, and NDMI, which can efficiently distinguish
forestdisturbancetypeswithdifferenttemporalcharacteristics,suchasgradual(e.g.,pest
infestation)andsudden(e.g.,fire)disturbances. TheNBRandSWIR2band(B7)havebeen
proven to be key features (Figures 4 and 6), effectively highlighting their sensitivity to
vegetationstructureloss,whilealsovalidatingthefindingsofKennedy[8]andMeng[38].
UnlikeRF,whichreliesonmanuallyconstructedindices,CNNdirectlyextractsspectral–
spatialfeaturesfromLandsatbands. Itsadvantagesindetectingfires(F1score+2.3%)and
logging(+0.75%)highlightitsabilitytocapturenonlineardisturbancefeatures(e.g.,the
SWIRband’sresponsetobaresoilafterafire)[39].

RemoteSens.2025,17,3521 20of25
4.4. LimitationsandDirectionsforImprovement
Thisstudyhasthefollowinglimitations:
(1)Limitationsinthejudgmentofvisualinterpretationsamples: thevalidationsample
constructionreliesonmulti-temporalvisualinterpretation,butmanualinterpretationis
subjecttosubjectiveerrors. Earlysamplesfrom1992to2002relyonLandsat5TMimagery
(spatialresolutionof30m),whichhasgenerationaldifferencesinradiometriccalibration
accuracycomparedtoLandsat8OLI,potentiallyintroducingvisualinterpretationbiases.
Improvementscouldincludeintroducingacross-validationmechanisminvolvingmultiple
interpretersandcombininghigh-resolutionhistoricalaerialphotographs(suchasCORONA
KH-4Bimagerywitharesolutionof1.8m)forhigh-precisioninterpretation.
(2)Theimpactofcloudandfogdisturbancesontemporalcontinuity. Althoughthe
FMaskcloudmaskalgorithmwasused[40],theaverageannualcloudcoverinthenorth-
easternregionishigh(June–October),resultinginfewerthanfiveeffectiveobservations
peryearinsomeyears. Thismayresultinincreasedfalsenegativesforcertaindisturbances
(e.g.,pineneedlepests)whenusingtheLandTrendralgorithm. Multi-sourcetemporalfea-
turescanbeconstructedbyintegratingSentinel-1SARdata(C-bandpenetratesclouds)[41],
andpolarizationfeatures(VV/VH)canbeusedtoenhancedisturbancesignalextraction
capabilitiesduringcloudyseasons.
(3)Theclassificationofraredisturbancetypesischallenging. Duetotheinsufficient
samplesandlimitedvisualinterpretationcapabilitiesofobservers,thisexperimentcould
notfurtherclassifygeologicaldisasterdisturbances(e.g.,mudslides,collapses,landslides).
Additionally, this experiment did not deeply explore the causes of geological disaster-
inducedforestdisturbances,suchasextremetemperatures,extremeprecipitation,orhuman
constructionactivities. Italsolackstheabilitytoidentifycertainmeteorologicaldisasters,
suchaswinddisastersorflooddisasters,andrequirestheintegrationofmulti-sourcedata,
suchasprecipitationdataortemperaturechangedata,forauxiliaryidentificationtoachieve
betterrecognitionofdisturbancetypesandhigherclassificationaccuracy.
5. Conclusions
Toachievetheaccurateclassificationofmultipleforestdisturbancetypes,thisstudy
developedanovelforestdisturbanceclassificationandmonitoringframework,integrating
remote sensing data with deep learning technology. It achieved high-precision separa-
tionoffourdisturbancefactors—fires,pestinfestation,geologicaldisasters,andhuman
logging—inChina’snortheasttemperateforestregionforthefirsttime. Byintegratingthe
LandTrendrtime-seriesanalysisalgorithmwithaCNNdeeplearningmodel,theframe-
worksignificantlyimprovedthespatiotemporalaccuracyofforestdisturbancemonitoring
attheregionalscale. Thecorecontributionliesinquantifyingdisturbancesbyidentifying
specificreferencedisturbanceareasandtimepoints. Human-induceddisturbancesand
naturaldisturbancesexhibitsignificantdifferences,andclassificationfacilitatescarbonre-
sponsibilityallocation. Additionally,theparametersystemwedeveloped(e.g.,LandTrendr
segmentcount,CNNconvolutionkernel)canbeadaptedtosimilarecologicalregionsin
NortheastAsia(e.g.,theRussianFarEast),enablingtransferableapplicationsandcontribut-
ingtoregionalecologicalsecurity. Thisstudyprovidesafeasiblemethodandbasicdata
fortherefinedmanagementoftemperateforestecosystemsandresearchonresponsesto
globalchange. Themodelframeworkisscalableandhasreal-timeplatformfunctionality.
We believe that this framework has the potential to achieve real-time, automated, and
intelligentforestdisturbancemonitoring,supportingthescientificassessmentofcarbon
neutralitygoalsinNortheastChina’sforestregions.

RemoteSens.2025,17,3521 21of25
AuthorContributions:Conceptualization,Y.Y.;methodology,Z.Z.andZ.H.;software,X.Y.(Xinyi
Yuan);validation,Y.Y.andZ.H.;formalanalysis,Z.Z.,X.Y.(XiguangYang),andX.Y.(XinyiYuan);
investigation,Z.Z.andX.Y.(XinyiYuan);resources,X.Y.(XiguangYang);datacuration,Z.Z.;writing—
originaldraftpreparation,Z.Z.;writing—reviewandediting,Y.Y.andX.Y.(XiguangYang);visual-
ization,X.Y.(XinyiYuan);supervision,Y.Y.;projectadministration,Y.Y.andX.Y.(XiguangYang);
fundingacquisition,Y.Y.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchwasfundedbythenationalkeyresearchanddevelopmentprogramofthe
“14thfive-yearplan”projectannualupdatetechnologyofforestresourcedatabasedonmulti-source
datacollaboration(2023YFD2201704),andtheNationalUndergraduateInnovationandentrepreneur-
shiptrainingprogram(202410225297).
DataAvailabilityStatement:Therawdatasupportingtheconclusionsofthisarticlewillbemade
availablebytheauthorsuponrequest.
Acknowledgments: The author acknowledges the providers of the following datasets: global
forest loss due to fire (https://glad.umd.edu/dataset/Fire_GFL/, access on 10 January 2025),
Global Forest Change (https://earthenginepartners.appspot.com/science-2013-global-forest, ac-
cesson10January2025),geologicalhazarddataset(www.gisrs.cn,accesson10January2025),and
LEAF(https://www.nesdc.org.cn/sdo/detail?id=6656e3b17e28172539d2b90e,accesson10January
2025).Duringthepreparationofthismanuscript,theauthorsusedDeepL(https://www.deepl.com/
zh/translator, accesson10January2025)forthepurposesoftranslationandproofreading. The
authorshavereviewedandeditedthemanuscriptandtakefullresponsibilityforthecontentofthis
publication.Atthesametime,theauthorsextendgratitudetoallreviewersandeditorswhoprovided
constructivesuggestionsforthisarticle,offeringinvaluableassistanceinitsrefinement.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
NBR NormalizedBurnRatio
EVI EnhancedVegetationIndex
NDVI NormalizedDifferenceVegetationIndex
NDMI NormalizedDifferenceMoistureIndex
ARVI AtmosphericallyResistantVegetationIndex
GNDVI GreenNormalizedDifferenceVegetationIndex
MNDWI ModifiedNormalizedDifferenceWaterIndex
RVI RatioVegetationIndex
SAVI Soil-AdjustedVegetationIndex
VCT VegetationChangeTracker
BFAST BreaksforAdditiveSeasonandTrend
CCDC ContinuousChangeDetectionandClassification
CMFDA ContinuousMonitoringofForestDisturbanceAlgorithm
LandTrendr Landsat-basedDetectionofTrendsinDisturbanceandRecovery
AppendixA
Thewebsiteaddressesofthefourdatasetsusedinthisarticleareasfollows:
Globalforestlossduetofire(https://glad.umd.edu/dataset/Fire_GFL/,accesson
10January2025).
GlobalForestChange(https://earthenginepartners.appspot.com/science-2013-global-
forest,accesson10January2025).
Geologicalhazarddataset(www.gisrs.cn, accesson10January2025), providedby
Geographicremotesensingecologicalnetworkplatform.

RemoteSens.2025,17,3521 22of25
LEAF(https://www.nesdc.org.cn/sdo/detail?id=6656e3b17e28172539d2b90e,access
on10January2025)
AppendixB
Basedonexistingresearch,numerousmatureandsuccessfulalgorithmshavebeen
developed for monitoring forest disturbances using remote sensing satellite data, such
as VCT, BFAST, CCDC, CMFDA, and LandTrendr. These algorithms possess distinct
advantagesanddisadvantages,whichdeterminetheirvaryingapplicability. TableA1lists
thenames,principles,advantages,anddisadvantagesofdifferentalgorithms.
TableA1.Advantagesanddisadvantagesofremotesensingtime-serieschangedetectionalgorithms.
Algorithm Advantages Disadvantages
1.Lowcomputationalcomplexity,enablinghighautomation 1.Slowforestdisturbances,suchaspestinfestations,aredifficultto
throughthreshold-basedmethods. detect.
VCT 2.Suitableformonitoringlarge-scaleforestchanges. 2.Sensitivetonoise,resultinginpronenesstomisclassification.
3.Strongrobustness,insensitivetorelativelypoorobservation 3.Sensitivetoconsecutiveanomalousobservationpoints,resulting
points. inpronenesstomisclassification.
1.Computationallycomplex,requiringhigh-performance
1.Capableofsimultaneouslycapturingbothhigh-intensityand
computinghardware.
gradualdisturbances.
BFAST 2.Poorperformanceinprocessinglow-frequencydata.
2.Enableslarge-areachangedetectionusingmultipledatasources.
3.Limiteddetectioncapabilityforregionswithrepetitive
3.Highlyrobust,whileminimizingnoiseinterference.
disturbances.
1.Highcomplexity,requiringsubstantialcomputationalresources
1.Real-timemonitoringcapability.
andextendedprocessingtime.
2.Highclassificationaccuracy,capableofprocessingimagerywith
2.High-qualityinputdatarequired,necessitatingrigorous
CCDC complexterraintypes.
preprocessingofremotesensingimagery.
3.Multi-dimensionalapproach,enablingcalculationsthatintegrate
3.Sensitivetonoise,assignificantnoiselevelscancompromiseresult
spectralandseasonalinformation.
accuracy.
1.Multi-sourcedatafusioncapturesinformationacrossdifferent
1.Highcomputationalcomplexityandsubstantialprocessing
scalesforcomputation.
demands.
2.Capableofdetectinglow-intensityforestdisturbances,suchas
CMFDA 2.Advancedprogrammingskillsrequiredformodeltraining.
small-scaleloggingandpestinfestations.
3.High-qualityinputimageryrequired,withrigorousradiometric
3.Suitableforcomplexgeologicalandtopographicalenvironments
calibration.
withintricatesurfacefeatures.
1.Capableofsimultaneouslydetectingdisturbancetrendsand 1.Limitedcapabilitytomonitorsmall-scaledisturbances.
disturbanceyears. 2.Multipleadjustmentstoalgorithmparametersrequired.
LandTrendr
2.Suitableforlarge-scale,long-termsequencemonitoring. 3.Processinglargeareasnecessitatesdistributedcomputingsupport,
3.Capableofsimultaneouslydetectingmultipledisturbancetypes. imposinghighdemandsonequipment.
TableA2.Descriptionsofvariousdeeplearningalgorithms.
PotentialApplicationsinForest
ModelArchitecture CorePrinciples MainAdvantages
DisturbanceClassification
CNNmodelscandirectlyextractthespatial
Specificallydesignedforprocessing CNNmodelsofferpowerfulspatialfeature featuresofdisturbancepatches(suchas
grid-likedata(suchasimages),CNN extractioncapabilities,arerelativelyefficient shape,texture,andpatterns)fromremote
CNN
modelsautomaticallyextractspatial inmodeling,andaretechnicallymaturein sensingimages,whichcanbeemployedto
featuresusingconvolutionalkernels. imageclassificationtasks. distinguishdisturbancescausedbyfires,
logging,andpestsanddiseases.
AdeepCNNthataddressestheproblemof Itcanbuildextremelydeepnetworks, Suitableforhandlingextremelycomplexor
vanishinggradientsinverydeepnetworks therebylearningmorecomplexfeatures; subtleperturbationfeatures,itmayprovide
ResNet
byincorporatingresidualconnections(skip trainingismorestableandperformanceis higherclassificationaccuracywhen
connections). powerful. standardCNNperformanceisinsufficient.
Suitableforanalyzinglong-termtime-series
vegetationindices(suchasNDVI),
Specificallydesignedtohandlesequential Proficientinhandlingtime-seriesdata;
capturingtheoccurrence,duration,and
RNN/LSTM data,ithasa‘memory’functionandcan capableofcapturingthedynamicprocessof
recoverydynamicsofdisturbances,and
capturetemporaldependencies. eventsandlageffects.
helpfulindistinguishingdisturbancetypes
withdifferenttemporaltrajectories.
Theoretically,itcanbeusedtosimulatethe
Specificallydesignedtohandle spatialcorrelationbetweendisturbance
Abletoutilizespatialtopological
graph-structureddata(non-Euclidean patchesinforestlandscapes(suchasthe
GCN relationshipsanddependenciesbetween
space),itlearnsandpropagatesinformation spreadofpestsanddiseases),butdata
entities.
throughnoderelationships. constructioniscomplex,anditsapplication
isstillintheexploratorystage.
AppendixC
Oregon State University has established a system-level forest change monitoring
algorithm(LandTrendr)onGoogleCloudPlatform. Whenutilizingthisalgorithm,users
can simply call the corresponding code to activate it. Additionally, we have obtained

RemoteSens.2025,17,3521 23of25
aparameter-tuningUIinterface(https://emaprlab.users.earthengine.app/view/lt-gee-
pixel-time-series,accesson10January2025)thatrunsonthecloudplatform. Userscan
accessitwithsimpleclicksorinputoperationstoselectparametersandregionsofinterest.
FigureA1belowprovidesanoverviewoftheUIinterface.
FigureA1.LandtrendrparameteradjustmentUIinterface.
AppendixD
Due to space constraints, we have presented the results of the significance tests in
TablesA3andA4below.
TableA3.McNemar’sstatisticvaluesinthesignificancetestresults.
McNemar’sStatistic Fires GroundDisasters ArtificialLogging DiseasesandPests Overall
RF15vsRF6 13.0 23.0 21.0 20.0 20.0
RF15vsCNN 9.0 17.0 8.0 12.0 11.0
RF6vsCNN 5.0 5.0 5.0 6.0 9.0
TableA4.p-valuesinsignificancetestresults.
p-Value Fires GroundDisasters ArtificialLogging DiseasesandPests Overall
RF15vsRF6 0.0000 0.0000 0.0000 0.0000 0.0000
RF15vsCNN 0.0000 0.0000 0.0000 0.0000 0.0000
RF6vsCNN 0.0266 0.0169 0.0169 0.0002 0.0000
References
1. Chapin,F.S.,III;Matson,P.A.;Vitousek,P.M.PrinciplesofTerrestrialEcosystemEcology;Springer:NewYork,NY,USA,2011.
2. Liu,Y.ThecharacteristicsofradiationbudgetofearthatmospheresystemovertheQinghai-XizangPlateauandtheirrelationship
withclimatechange.PlateauMeteorol.1998,17,37–44.
3. Wu,L.;Liu,X.;Liu,M.;Yang,J.;Zhu,L.;Zhou,B.OnlineForestDisturbanceDetectionattheSub-AnnualScaleUsingSpatial
ContextfromSparseLandsatTimeSeries.IEEETrans.Geosci.RemoteSens.2022,60,4507814.[CrossRef]
4. Huang,C.;Goward,S.N.;Masek,J.G.;Thomas,N.;Zhu,Z.;Vogelmann,J.E.AnAutomatedApproachforReconstructingRecent
ForestDisturbanceHistoryUsingDenseLandsatTimeSeriesStacks.RemoteSens.Environ.2010,114,183–198.[CrossRef]
5. Verbesselt,J.;Hyndman,R.;Newnham,G.;Culvenor,D.Detectingtrendandseasonalchangesinsatelliteimagetimeseries.
RemoteSens.Environ.2010,114,106–115.[CrossRef]
6. Zhu,Z.;Woodcock,C.E.ContinuousChangeDetectionandClassificationofLandCoverUsingAllAvailableLandsatData.
RemoteSens.Environ.2013,144,152–171.[CrossRef]
7. Zhu,Z.;Woodcock,C.E.;Olofsson,P.ContinuousmonitoringofforestdisturbanceusingallavailableLandsatimagery.Remote
Sens.Environ.2012,122,75–91.[CrossRef]

RemoteSens.2025,17,3521 24of25
8. Kennedy,R.E.;Yang,Z.;Cohen,W.B.DetectingTrendsinForestDisturbanceandRecoveryUsingYearlyLandsatTimeSeries:1.
LandTrendr—TemporalSegmentationAlgorithms.RemoteSens.Environ.2010,114,2897–2910.[CrossRef]
9. Chen,X.;Zhao,W.;Chen,J.;Qu,Y.;Wu,D.;Chen,X.MappingLarge-ScaleForestDisturbanceTypeswithMulti-TemporalCNN
Framework.RemoteSens.2021,13,5177.[CrossRef]
10. Yahya,A.A.;Liu,K.;Hawbani,A.;Wang,Y.;Hadi,A.N.ANovelImageClassificationMethodBasedonResidualNetwork,
Inception,andProposedActivationFunction.Sensors2023,23,2976.[CrossRef]
11. Wu,T.;Feng,F.;Lin,Q.;Bai,H.AdvancedMethodtoCapturetheTime-LagEffectsbetweenAnnualNDVIandPrecipitation
VariationUsingRNNintheAridandSemi-AridGrasslands.Water2019,11,1789.[CrossRef]
12. Vasilakos,C.;Tsekouras,G.E.;Kavroudakis,D.LSTM-BasedPredictionofMediterraneanVegetationDynamicsUsingNDVI
Time-SeriesData.Land2022,11,923.[CrossRef]
13. Pei,H.;Owari,T.;Tsuyuki,S.;Zhong,Y.ApplicationofaNovelMultiscaleGlobalGraphConvolutionalNeuralNetworkto
ImprovetheAccuracyofForestTypeClassificationUsingAerialPhotographs.RemoteSens.2023,15,1001.[CrossRef]
14. Peña-Gallardo,M.;Vicente-Serrano,S.M.;Camarero,J.J.;Gazol,A.;Sánchez-Salguero,R.;Domínguez-Castro,F.;ElKenawy,A.;
Beguería-Portugés,S.;Gutiérrez,E.;DeLuis,M.;etal. DroughtSensitivenessonForestGrowthinPeninsularSpainandthe
BalearicIslands.Forests2018,9,524.[CrossRef]
15. Wang,Y.;Jia,X.;Zhang,X.;Lei,L.;Chai,G.;Yao,Z.;Qiu,S.;Du,J.;Wang,J.;Wang,Z.;etal. TrackingForestDisturbancein
NortheastChina’sCold-TemperateForestsUsingaTemporalSequenceofLandsatData.RemoteSens.2024,16,3238.[CrossRef]
16. Wegler,M.;Kuenzer,C.PotentialofEarthObservationtoAssesstheImpactofClimateChangeandExtremeWeatherEventsin
TemperateForests—AReview.RemoteSens.2024,16,2224.[CrossRef]
17. Sheng,J.;Gao,X.;Zhang,Z.SustainabilityofForestDevelopmentinChinafromthePerspectiveoftheIllegalLoggingTrade.
Sustainability2023,15,12250.[CrossRef]
18. Liu, S.; Wang, D.; Lei, G.; Li, H.; Li, W. Elevated Risk of Ecological Land and Underlying Factors Associated with Rapid
UrbanizationandOverprotectedAgricultureinNortheastChina.Sustainability2019,11,6203.[CrossRef]
19. Li,Q.;Yang,Y.;Zhang,W.;Zhang,L.;Hu,C.EffectsofForestManagementandDroughtDisturbanceonForestNetPrimary
ProductivityinThreeNortheasternProvincesfrom2000to2022.Bull.SoilWaterConserv.2024,44,308–317.[CrossRef]
20. Hansen,M.C.;Potapov,P.V.;Moore,R.;Hancher,M.;Turubanova,S.A.;Tyukavina,A.;Thau,D.;Stehman,S.V.;Goetz,S.J.;
Loveland,T.R.;etal.High-ResolutionGlobalMapsof21st-CenturyForestCoverChange.Science2013,342,850–853.[CrossRef]
21. Tyukavina,A.;Potapov,P.;Hansen,M.C.;Pickens,A.;Stehman,S.;Turubanova,S.;Parker,D.;Zalles,V.;Lima,A.;Kommareddy,
I.;etal.Globaltrendsofforestlossduetofire,2001–2019.Front.RemoteSens.2022,3,825190.[CrossRef]
22. Wang,D.;Ren,P.;Xia,X.;Fan,L.;Qin,Z.;Chen,X.;Yuan,W.Nationalforestcarbonharvestingandallocationdatasetforthe
period2003to2018.EarthSyst.Sci.Data2024,16,2465–2481.[CrossRef]
23. Kennedy,R.E.;Yang,Z.;Gorelick,N.;Braaten,J.;Cavalcante,L.;Cohen,W.B.;Healey,S.ImplementationoftheLandTrendr
AlgorithmonGoogleEarthEngine.RemoteSens.2018,10,691.[CrossRef]
24. Wulder,M.A.;White,J.C.;Loveland,T.R.;Woodcock,C.E.;Belward,A.S.;Cohen,W.B.;Fosnight,E.A.;Shaw,J.;Masek,J.G.;Roy,
D.P.TheglobalLandsatarchive:Status,consolidation,anddirection.RemoteSens.Environ.2016,185,271–283.[CrossRef]
25. Louppe,G.UnderstandingRandomForests:FromTheorytoPractice.arXiv2014,arXiv:1407.7502.
26. Liu,D.;Qu,Y.;Yang,X.;Zhao,Q.TSSA-NBR:ABurnedAreaExtractionMethodBasedonTime-SeriesSpectralAnglewithFull
SpectralShape.RemoteSens.2025,17,2283.[CrossRef]
27. Zha,Y.;Gao,J.;Ni,S.Useofnormalizeddifferencebuilt-upindexinautomaticallymappingurbanareasfromTMimagery.Int.J.
RemoteSens.2003,24,583–594.[CrossRef]
28. Bjorck,N.;Gomes,C.P.;Selman,B.;Weinberger,K.Q.Understandingbatchnormalization.arXiv2018,arXiv:1806.02375.[CrossRef]
29. Watson,J.E.M.;Evans,T.;Venter,O.;Williams,B.;Tulloch,A.;Stewart,C.;Thompson,I.;Ray,J.C.;Murray,K.;Salazar,A.;etal.
Theexceptionalvalueofintactforestecosystems.Nat.Ecol.Evol.2018,2,599–610.[CrossRef]
30. Elia,M.;Lafortezza,R.;Colangelo,G.;Sanesi,G.Astreamlinedapproachforthespatialallocationoffuelremovalsinwildland–
urbaninterfaces.Landsc.Ecol.2014,29,1771–1784.[CrossRef]
31. Qiu,H.;Cui,P.;Regmi,A.D.;Hu,S.;Wang,X.;Zhang,Y.Theeffectsofslopelengthandslopegradientonthesizedistributionsof
loessslides:Fieldobservationsandsimulations.Geomorphology2018,300,69–76.[CrossRef]
32. Hayajneh,S.M.;Naser,J.WindandSlopeInfluenceonWildlandFireSpread,aNumericalStudy.Fire2025,8,217.[CrossRef]
33. Ferrenberg,S.LandscapeFeaturesandProcessesInfluencingForestPestDynamics. Curr. Landsc. Ecol. Rep. 2016,1,19–29.
[CrossRef]
34. Bell,G.;Sena,K.L.;Barton,C.D.;French,M.EstablishingPineMonoculturesandMixedPine-HardwoodStandsonReclaimed
SurfaceMinedLandinEasternKentucky:ImplicationsforForestResilienceinaChangingClimate.Forests2017,8,375.[CrossRef]
35. Tanveer, A.; Song, H.; Faheem, M.; Daud, A. Caring for the environment. How do deforestation, agricultural land, and
urbanizationdegradetheenvironment?FreshinsightthroughtheARDLapproach.Environ.Dev.Sustain.2025,27,11527–11562.
[CrossRef]

RemoteSens.2025,17,3521 25of25
36. Zhang,L.;Zhang,L.;Du,B.DeepLearningforRemoteSensingData:ATechnicalTutorialontheStateoftheArt.IEEEGeosci.
RemoteSens.Mag.2016,4,22–40.[CrossRef]
37. Xie,G.;Liu,P.;Chen,Z.;Chen,L.;Ma,Y.;Zhao,L.TimeSeriesRemoteSensingImageClassificationwithaData-DrivenActive
DeepLearningApproach.Sensors2025,25,1718.[CrossRef]
38. Meng,R.;Dennison,P.E.;D’Antonio,C.M.;Moritz,M.A.Remotesensinganalysisofvegetationrecoveryfollowingshort-interval
firesinSouthernCaliforniashrublands.PLoSONE2014,9,e110637.[CrossRef][PubMed][PubMedCentral]
39. Wang,Z.;Yang,P.;Liang,H.;Zheng,C.;Yin,J.;Tian,Y.;Cui,W.SemanticSegmentationandAnalysisonSensitiveParametersof
ForestFireSmokeUsingSmoke-UnetandLandsat-8Imagery.RemoteSens.2022,14,45.[CrossRef]
40. Mateo-García,G.;Gómez-Chova,L.;Amorós-López,J.;Muñoz-Marí,J.;Camps-Valls,G.MultitemporalCloudMaskinginthe
GoogleEarthEngine.RemoteSens.2018,10,1079.[CrossRef]
41. Philipp,M.B.;Levick,S.R.ExploringthePotentialofC-BandSARinContributingtoBurnSeverityMappinginTropicalSavanna.
RemoteSens.2020,12,49.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.