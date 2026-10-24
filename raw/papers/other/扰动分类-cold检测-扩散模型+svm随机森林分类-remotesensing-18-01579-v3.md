Article
Forest Disturbance Classification Under Imbalanced and
Small-Sample Conditions Based on Collaborative
Semi-Supervised Learning and Sample Generation
YudanLiu,YuxinZhao,YanYan,YanShao,XinqiQuandLingWu*
SchoolofArtificialIntelligence,ChinaUniversityofGeosciences,Beijing100083,China;
1004235202@email.cugb.edu.cn(Y.L.);3004250022@email.cugb.edu.cn(Y.Z.);2004220026@email.cugb.edu.cn(Y.Y.);
2104250089@email.cugb.edu.cn(Y.S.);2104250090@email.cugb.edu.cn(X.Q.)
* Correspondence:wuling@cugb.edu.cn
Highlights
Whatarethemainfindings?
• The proposed framework for multi-type forest disturbance classification based on
collaborativesemi-supervisedlearningandsamplegenerationenableseffectiveuse
ofunlabeleddataandsuppressespseudo-labelnoise. Themethodachievesrobust
classificationunderimbalancedandsmall-sampleconditions,withanoverallaccuracy
of93.2%,outperformingsingleclassificationmethods.
• Thelatentdiffusionmodeleffectivelyaddressesclassimbalancebygeneratinghigh-
fidelitypseudo-samplesforraredisturbancetypes. Thegeneratedsamplesareconsis-
tentwithrealspectralandspatialpatterns,improveclassbalance,andfurtherenhance
classificationperformance.
Whataretheimplicationsofthemainfindings?
• The study provides a practical solution for forest disturbance classification when
labeledsamplesarescarceandclassdistributionishighlyimbalanced.
• Provides a practical and generalizable method for precision forestry; it could be
extendedtootherremotesensingtaskswithsimilarsmallsampleandimbalanceissues.
Themethodhasthepotentialtoimproveforestmanagement,carbonaccounting,and
ecologicalassessment.
Abstract
Accurateandtimelyinformationonforestdisturbancedriversisimportantforsustain-
able forest management, global carbon cycle accounting, and climate change response.
However,forestdisturbanceclassificationisdifficultduetotwomajorchallenges: limited
labeledsamplesandhighlyimbalanceddisturbanceclassdistribution. Inthisarticle, a
AcademicEditor:Krzysztof
new framework for multi-type forest disturbance classification based on collaborative
Steren´czak
semi-supervisedlearningandsamplegenerationwasproposed. First,forestdisturbance
Received:2April2026
is detected using long-term remote sensing time series data and disturbance detection
Revised:6May2026
algorithms. Spatiotemporal,spectralandterrainfeaturesofdifferentdisturbancetypes
Accepted:10May2026
Published:14May2026 are extracted. On this basis, to address the problem of imbalanced and small-sample
Copyright:©2026bytheauthors. conditions,acollaborativeclassificationstrategyisdeveloped. Basedonasmallnumber
LicenseeMDPI,Basel,Switzerland. of labeled samples, Support Vector Machine (SVM) and Random Forest (RF) are used
Thisarticleisanopenaccessarticle to build dual base classifiers. A confident learning (CL) framework is applied to select
distributedunderthetermsand
high-confidence pseudo-labeled samples from unlabeled data. Then, a latent diffusion
conditionsoftheCreativeCommons
model(LDM)isintroducedtogeneratehigh-fidelitypseudo-samples. Thisincreasesthe
Attribution(CCBY)license.
RemoteSens.2026,18,1579 https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 2of22
samplesizeandbalancestheclassdistribution. Basedontheaugmenteddataset,thedual
classifiersareiterativelyoptimizedusingaco-trainingstrategy,whichimprovesmodel
generalizationundercomplexconditions. Theresultsshowthattheproposedframework
couldgeneratehigh-qualitypseudo-samplesandeffectivelyreduceclassimbalance. The
overallaccuracy(OA)oftheproposedframeworkreaches93.2%,whichis5.7%and4.4%
higher than single classifier baselines, respectively. After introducing the LDM-based
balancingmechanism,performanceisfurtherimprovedby1.8%comparedwiththepure
semi-supervised framework. This study provides an efficient and reliable solution for
large-scaleforestecosystemmonitoring.
Keywords: forest disturbance classification; latent diffusion model (LDM); confident
learningframework;imbalancedandsmallsamples;remotesensingtimeseries
1. Introduction
Forestecosystemsareakeycomponentoftheterrestrialsystemandplayanimpor-
tantroleinclimateregulation,biodiversityconservation,andcarbonsequestration[1–3].
However,forestdisturbancesdrivenbyglobalclimateanomalies,suchasintensifiedwild-
fire regimes, together with human activities including logging, road construction, and
landclearing,areplacingseriouspressureonthestructureandfunctionofforestecosys-
tems[4–8]. Accurateclassificationofforestdisturbancetypesandtheirdrivingfactorsis
importantnotonlyforunderstandingforestsuccession,butalsoforsupportingecological
managementdecisions[9–11].
Inrecentdecades,long-termsatelliteremotesensingdata,suchastheLandsatseries,
haveprovidednewopportunitiesfordetailedcharacterizationofforestdisturbance. The
researchfocushasshiftedfromdetectingwhetherdisturbanceoccurstoclassifyingthetype
ofdisturbance[12–15]. Differentdrivingfactorsleadtodifferentspectral,structural,and
functionalresponses,andtheseresponsesarecomplexanddynamic. Basedonwhether
disturbancedetectionisperformedbeforeclassification,methodsforforestdisturbance
classificationusingremotesensingtimeseriescanbedividedintodirectmethods[16]and
two-stagemethods[17]. Thedirectmethodusestemporalspectralmetricsderivedfrom
remotesensingtimeseriesandpriorknowledgeofdisturbancedriverstosimultaneously
detectandclassifydisturbanceatthepixellevel[18,19]. Thismethodhashigherefficiency
becauseitdoesnotrequiremergingdisturbancepatches. However,thedirectmethodis
difficulttodistinguishdisturbancetypeswithsimilarspectralfeaturesbutdifferentdrivers
without considering spatial context. It also tends to produce fragmented results with
salt-and-peppernoise. Onestrategyinthetwo-stagemethodfirstdetectsdisturbanceatthe
pixellevelusingchange-detectionalgorithms[20–22]. Then,disturbedpixelsaregrouped
into patches, and spatial and spectral features of disturbance events are extracted [23].
Machinelearningmodelsordeeplearningmodelsarethenusedforclassification. Another
strategyistouseexistingdisturbancedetectionproducts,suchastheglobal30mforest
changedatasetproducedbytheUniversityofMaryland[24],andthenclassifydisturbance
typesusingmachinelearningalgorithms[25,26]. Theadvantageofthetwo-stagemethod
isthatitoperatesatthepatchlevelandcanusemorespatialinformation. Therefore, it
iscurrentlythemainapproachforforestdisturbanceclassification[27,28]. Forexample,
directmethodsincludechange-vectoranalysisandwithin-yeardisturbancelabelingusing
time-seriesspectraltrajectories,whiletwo-stagemethodscommonlycombineLandTrendr,
CCDC, COLD, or similar disturbance detection algorithms with subsequent machine-
learningattribution.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 3of22
Mostexistingmethodsrequirealargenumberoflabeledsamplestobuildclassification
models.Previousstudiesoftencollectsamplesthroughvisualinterpretationusinghistorical
records,high-resolutionimagery,andfieldsurveys[29,30]. Forexample,Lietal. collected
1708 disturbance patches using high-resolution images from Google Earth, including
632 wildfire samples, 345 logging samples, and 731 plantation samples [31]. However,
high-qualitylabeledsamplesareexpensivetoobtain. Inforestdisturbancemapping,this
difficultyismainlycausedbyuncertaindisturbancetiming, cloudcontamination, high
field-surveycost,incompletehistoricalrecords,andtherarityofsomedisturbancetypes.
Inaddition,disturbancessuchasroadconstructionandfirearerandomandrare,which
leadstoahighlyimbalanceddistributionofdisturbancetypes. Toaddresstheproblemof
imbalancedandsmall-sampleconditions,currentresearchmainlyfocusesontwodirections.
Oneistodevelopmethodsforgeneratingaugmentedlabeledsamples[32,33]. Theotheris
todesignmethodsthatcanachievestableperformancewithlimitedlabeleddata[34,35].
Dataaugmentationmethodsaimtolearnthelatentevolutionofdisturbancesintempo-
ral,spatial,andspectraldimensionsandgeneratehigh-qualitypseudo-samplesatscale[36].
Byincreasingthenumberofminority-classsamples,thesemethodscancorrectclassimbal-
anceandprovideimportantdatasupportforimprovingclassificationaccuracy. Previous
methods, including basic transformations, mixed sample [37], can reduce data scarcity
in the feature space, but they often ignore the physical consistency of spectral features
andcannotrepresentspectralvariabilityundercomplexlandsurfaceconditions. Genera-
tiveAdversarialNetworks(GANs)havebeenintroducedintoremotesensingtogenerate
pseudo-samples[38]. However,conventionalGAN-basedmethodsmaysufferfrommode
collapsewhendealingwithextremelysmallsamplesandmayhavedifficultycapturing
finedistributionsinhigh-dimensionalfeaturespaces. Generativemodelsrepresentedby
latentdiffusionmodels(LDMs)haveshownstrongabilityindistributionmodeling[39].
ComparedwithGANs,LDMisbasedonprobabilisticgeneration. Itcanlearnthestatistical
distributionofasmallnumberofhigh-qualitysamplesandgeneratedisturbancefeatures
underdifferentintensitiesandgeographicconditions. Thishelpsreducefeaturesparsity
causedbylimitedsampling. Atthesametime,LDMcanreconstructthedistributionof
rareclassesandprovidemorerepresentativeanddifficultsamples. Thisimprovesmodel
robustnessunderimbalancedsmall-sampleconditions. Previousstudieshaveshownthat
LDMcangeneratedatawithbothdiversityandhighfidelity,whichprovidesanewsolution
totheproblemofsparsefeaturespaceinremotesensing[40,41].
Whenlabeledsamplesarelimited,existingmethodsmainlyincludetransferlearn-
ing[42,43]andsemi-supervisedlearning[44,45]. Transferlearningfocusesontransferring
feature-extraction ability from large public datasets to specific tasks, such as BigEarth-
Net[46]. However,datasetsspecificallydesignedforforestdisturbanceclassificationare
verylimited[47,48],sopretrainedmodelscannotlearnsufficientpriorknowledgeofdistur-
bancepatterns. Inaddition,differencesinsensors,acquisitiontime,andgeographicregions
leadtodomaindifferences,whichoftencausespectralmismatchincross-regiontransfer.
Fordisturbanceswithstrongregionalcharacteristics,suchasspecificloggingpatterns,the
lackoftargetedtrainingdataandlimitedgeneralizationoftransferredfeaturesrestricts
modelperformance. Semi-supervisedlearninguseslargeamountsofunlabeleddatato
compensateforthelackoflabels. Typicalmethods,suchaspseudo-labelingandconsis-
tencyregularization,relyonmodelconfidencetoguidetraining. Forexample,Yanetal.
usedaconfidentlearning(CL)frameworktoiterativelyselecthigh-confidencesamples
fromunlabeleddataandexpandthelabeleddataset[49]. However,thistypeofmethod
isessentiallyasecondselectionfromexistingunlabeleddata. Althoughitcanincrease
samplesize,itsperformancedependsstronglyonthequalityoftheinitiallabeledsamples
andthenaturaldistributionofunlabeleddata. Underextremelyimbalancedconditions,
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 4of22
CLoftencannotobtainenoughminoritysamplesandmayintroducelabelnoise,which
causes the classification boundary to shift toward majority classes. In addition, simple
sampleselectioncannotreconstructthefeaturedistributionsofrareclassesandtherefore
cannotfundamentallysolvethebiascausedbyclassimbalance. Toaddressthisproblem,
thecombinationofLDMandCLframeworkscanimprovebothdatarepresentationand
modelrobustnessthroughfeaturegenerationandknowledgealignment.
Basedonthesechallenges,thisstudyuseslong-termremotesensingdatatoextract
richtemporal, spectral, andspatialfeaturesofforestdisturbance. Anewframeworkis
proposedbyintegratingLDM-basedsamplegenerationandtheMutualGuideFramework
(MGF)forCL.Undertheconditionoflimitedandhighlyimbalancedlabeledsamples,this
frameworkprovidesanefficientandreliablesolutionforlarge-scaleandfineclassification
offorestdisturbanceincomplexenvironments.
2. StudyAreaandData
2.1. StudyArea
ThestudyareaislocatedinJingzhouMiaoAutonomousCountyandTongdaoDong
AutonomousCountyinthesouthernpartofHuaihuaCity,HunanProvince,China(25◦52′N
to26◦47′N,109◦16′Eto110◦01′E)(Figure1). TheforestcoverageratesofJingzhouand
Tongdaoareapproximately74.93%and77.24%,respectively. Themainforesttypeisthe
mid-subtropicalhumidevergreenbroadleafforest. Thisregionbelongstokarsttopography.
Duetotheinfluenceofspecialgeologicalandsoilconditions,extremeclimate,aswellas
drivingfactorssuchasdeforestationandmining,theforestecosysteminthisareaisfragile
and highly susceptible to disturbances, leading to degradation of the forest ecosystem.
Therefore,thisstudyselectsfourtypesofforestdisturbances: roadconstruction,logging,
clearingforcultivation,andfires,astheresearchobjects,whicharehighlyrepresentative.
Figure1.Overviewofthestudyarea(redarea).Quotefrom[49].
2.2. LandsatTimeSeriesData
Toobtainforestdisturbancedata,Landsattimeseriesdatafrom1986to2022were
used,includingLandsat5TM,Landsat7ETM+,andLandsat8OLI/TIRS.Tomaximize
data availability under the climatic conditions of the study area, all available Landsat
imageswithcloudcoverlessthan80%werecollected. Fmaskalgorithmwasusedforcloud
removal. Afterprocessing,atotalof357imageswereobtained. Statisticsonthenumberof
imagesbymonthareshowninTable1.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579
5of22
Table1.Numberofallavailableimagesbymonth.
Month January February March April May June July August September October November December
Numberof
|     | 28 24 | 19 21 | 28 14 | 28 35 | 39 34 | 47 37 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- |
Images
2.3. TrainingandValidationData
In this study, a forest disturbance sample dataset was constructed through multi-
source data integration and visual interpretation. First, the Continuous Monitoring of
Land Disturbance (COLD) algorithm was applied to preprocess Landsat series images.
Harmonicmodelfittingandresidualanalysiswereusedtoextractthespatiallocationsand
occurrencetimeofpotentialdisturbancepatches. Disturbancesamplesderivedfromthe
COLDalgorithmserveasbaselineinputsforthesubsequentcollaborativesemi-supervised
learningandsamplegenerationframework. Basedonthis,aforestdisturbancedataset
wasbuiltbyintegratingannualfirepointdata(obtainedfromtheannualsurfacethermal
anomalydatasetprovidedbytheInstituteofRemoteSensingandDigitalEarth,Chinese
AcademyofSciences),loggingrecords(primarilycollectedfromofficialgovernmentportals
andnews),andvisualinterpretationusingGoogleEarthPro(GEP,version7.3.3). Figure2
showsthetruecolorandfalsecolorimagesforeachtypeofdisturbance. Thedisturbance
typesshowastrongimbalance(Table2).
Figure2.Imagefeaturesofdifferentdisturbancetypes.
Table2.Typeandsamplecountofforestdisturbance.
| DisturbanceType |     | Description |     |     | Source | SampleCount |
| --------------- | --- | ----------- | --- | --- | ------ | ----------- |
Constructionofroadsandroadside
| Roadconstruction |     |     |     |     | GEP | 54  |
| ---------------- | --- | --- | --- | --- | --- | --- |
servicefacilitieswithinforests.
Forestdisturbancecausedbylogging
| Logging |     | withoutconversiontoother |     | GEPandloggingrecords |     | 380 |
| ------- | --- | ------------------------ | --- | -------------------- | --- | --- |
land-usetypes.
Clearingforestsforcropsoreconomic
| Clearingforcultivation |     |     |     |     | GEP | 86  |
| ---------------------- | --- | --- | --- | --- | --- | --- |
treeplantations.
|     | Forestburningcausedbyfire,including |                                |     | GEPandLandsat8annual |                 |     |
| --- | ----------------------------------- | ------------------------------ | --- | -------------------- | --------------- | --- |
|     | Fire                                |                                |     |                      |                 | 142 |
|     |                                     | wildfiresandhuman-causedfires. |     |                      | firehotspotdata |     |
Theinterpretedlabelswerecross-checkedusingtemporalLandsattrajectories,avail-
ablefirerecords,loggingrecords,andGEPhigh-resolutionimagerytoensureconsistency
betweenthedisturbancetypeandtheobservedspectral-spatialevidence.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579
6of22
Amongthem,roadconstructionandclearingforcultivationhaveverylimitedsamples.
Thelargestdifferenceinsamplesizeisaboutseventimes.Thedatasetwassplitintotraining
andtestingsetswitharatioof7:3.
3. Methodology
Theframeworkofthisstudyintegratedmultidimensionalremotesensingfeatures,
semi-supervisedlearning,andsamplegenerationmethodsformulti-typeforestdisturbance
classification. First,longtemporalLandsatimagesareusedforforestdisturbancedetection
andfeatureextraction. Then,acollaborativesemi-supervisedlearningframeworkwitha
generativemodelisconstructed. MGFisconstructedusingtheheterogeneouspropertiesof
SVMandRF.Toaddresstheproblemofsamplelimitation,CLisappliedtoidentifylabel
noiseandselecthigh-confidencepseudo-labeledsamplesfromunlabeleddata. Amutual
guidestrategyisusedtoiterativelyrefinethetrainingdataset. Inaddition,toaddressthe
problem of sample imbalance, LDM is introduced for distribution reconstruction. This
helpsbalancethefeaturespaceandimprovesclassificationperformance.
3.1. SpatiotemporalandSpectralResponseAnalysisandFeatureConstructionof
ForestDisturbance
TheCOLDalgorithmisusedforchangedetectioninlong-termLandsatdata. The
COLDalgorithmfitsseasonalpatternsusingaharmonicmodelandcapturesabruptnon-
seasonalchanges. Thisallowsaccuratedetectionofthetimingandlocationofdisturbances
incomplexforestenvironments.Basedonthetemporaltrajectoriesfordifferentdisturbance
types,amulti-dimensionalfeaturespaceisconstructedfromtemporal,spatial,spectral,
andtopographicaspects(Table3).
Table3.Categoricalfeaturesforforestdisturbanceattribution.
| Type | Feature(Abbr.) | SpectrumIndex(SI) | Description |
| ---- | -------------- | ----------------- | ----------- |
Indicesorbandspectralvalues
Pre-change(PreC_SI),
|                  |                        | NBR,SWIR1, beforeandafterchange,andspectral |     |
| ---------------- | ---------------------- | ------------------------------------------- | --- |
| Temporalfeatures | Post-change(PostC_SI), |                                             |     |
|                  |                        | TCW,TCG differencesbetweenpost-change       |     |
Changemagnitude(MagC_SI)
andpre-change.
Standarddeviationandmeanof
| Pixelstdinslidingwindow |     | NBR,SWIR1,                       |     |
| ----------------------- | --- | -------------------------------- | --- |
| Spatialfeatures         |     | indicesorbandvalueswithinsliding |     |
| (STD_SI),Mean(Mean_SI)  |     | TCW,TCG                          |     |
windows(3×3,5×5,7×7,9×9).
|                          | Dissimilaritychanges | Differencesintexturefeatures      |              |
| ------------------------ | -------------------- | --------------------------------- | ------------ |
| magnitude(MagDiss_SI),   |                      | (dissimilarity,contrast,variance) |              |
| Spatialfeatures          |                      | NBR,SWIR1,TCG                     |              |
|                          | Contrast(MagCon_SI), | betweenpost-changeandpre-change   |              |
|                          | Variance(MagVar_SI)  |                                   | (3×3window). |
| Interceptchangemagnitude |                      | Interceptorslopedifferencesinthe  |              |
Spectralfeatures (Mag_INTP),Slopechange INTP,SLP fittedsegmenttrendlinebetween
|                 | magnitude(Mag_SLP) |     | post-changeandpre-change |
| --------------- | ------------------ | --- | ------------------------ |
| Terrainfeatures | Elevation,Slope    | DEM | Elevationandslope.       |
Temporal features include the pre-change spectral values (PreC_SI), post-change
spectralvalues(PostC_SI),andchangemagnitude(MagC_SI=PostC_SI−PreC_SI).For
spatialfeatures,spectralmean(Mean_SI)andstandarddeviation(STD_SI)arecalculated
usingslidingwindowsfrom3×3to9×9. Texturedifferencesbeforeandafterdisturbance
arealsocomputedusinga3×3window,includingdissimilarity,contrast,andvariance.
Todistinguishdifferentdisturbancetypes,spectralfeaturesarederivedfromdifferences
betweenpre-andpost-changetemporaltrajectories. Theseincludethechangeinintercept
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 7of22
(Mag_INTP)andslope(Mag_SLP).Inaddition,topographicfeaturessuchaselevationand
slopeareincludedintheclassification.
3.2. ForestMulti-TypeDisturbanceClassificationUnderImbalancedSmall-SampleConditions
BasedonCollaborativeSemi-SupervisedLearningandSampleGeneration
Basedontheinputmultidimensionalspatiotemporal,spectral,andterrainfeatures,a
MutualGuideFramework(MGF)isconstructedusingSVMandRFasbaseclassifiersto
activelyselecthigh-confidencepseudo-labeledsamplesforexpandingtheground-truthset.
AsamplegenerationmethodbasedonLDMistrainedbyutilizingtheaugmentedlabeled
set from the MGF. Synthetic samples are generated to balance class proportions across
differentdisturbancetypes. TheMGFthenre-trainsitsbaseclassifiersusingthisbalanced
settofurtheridentifypseudo-labeledsamples. Throughoutthisprocess,aselectioncrite-
rionbasedonConfidentLearning(CL)isdesignedtospecificallyrecruithigh-confidence
pseudo-labelsandfilteroutlow-qualitygeneratedsamples. Throughthiscycliciteration,a
large-scale,highlyreliable,andbalancedlabeleddatasetisestablished,ultimatelyachieving
high-precisionforestdisturbanceclassificationunderimbalancedsmall-sampleconditions.
TheworkflowisshowninFigure3.
Figure3.Theworkflowforclassifyingmultipletypesofforestdisturbances.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 8of22
3.2.1. ForestDisturbanceClassificationBasedontheMGF
Themulti-dimensionalfeaturesconstructedinSection3.1areusedasinputforclassifi-
cation. Toovercometheinductivebiasofasingleclassifierundersmall-sampleconditions,
anMGFisbuiltusingtwoheterogeneousclassifiers,SVMandRF.SVMandRFoffercom-
plementarylearningmechanisms: SVMexcelsatfindingglobaloptimalhyperplaneswith
stronggeneralizationundersmall-sampleconditions,whileRFcaptureslocalnonlinear
relationshipsthroughensembledecisiontrees. Theirdistinctglobal-versus-localperspec-
tivesprovidethe“multi-view”informationnecessaryforCL,allowingtheframeworkto
identifynoisysamplesandsuppressbiaspropagationthroughmutualguidance.
The workflow is as follows. First, the base classifiers are trained using a small set
oflabeledsamples. Theyarethenusedtopredictlarge-scaleunlabeleddisturbancedata
and assign initial pseudo-labels. To reduce noise in pseudo-labels, the CL criterion is
appliedtoremovesampleswithambiguousboundariesorinconsistentpredictions. High-
confidencepseudo-labeledsamplesareretained. Across-guidancestrategyisthenused.
High-confidencesamplesselectedbyclassifierAareaddedtothetrainingsetofclassifier
B, and vice versa. The classifiers are retrained, and pseudo-label selection is repeated.
Previously selected high-confidence pseudo-labeled samples are retained during later
iterationsandarenotremovedfromtheaugmentedlabeledset. Thisprocessiteratively
expandsthelabeleddatasetandimprovesclassificationperformance. Afterconvergence,if
thepredictionsofthetwoclassifiersareconsistent,thesampleisassignedtothatclass. If
not,theclasswithhigherconfidenceisselected.
3.2.2. Pseudo-SampleGenerationUsingtheLDM
TheLDMisusedtolearnthelatentprobabilitydistributionoflimitedforestdistur-
bancesamples. Itaimstogeneratehigh-fidelitypseudo-samplesforminorityclasses. As
showninFigure4,theframeworkincludestwomainlevels: thepixelspaceandthelatent
space. Theprocessconsistsofthreekeystepsasfollows.
ThefollowingdescriptionretainsonlythekeyLDMstepsneededtoexplainforest
disturbancefeaturegeneration.
Figure4.ThestructureofLDM.
LatentSpaceMapping
Toreducecomputationalcostinhigh-dimensionalspatiotemporalandspectralfeature
spaceandsuppressnoise,avariationalautoencoder(VAE)isusedforlatentmapping. An
encoder ε maps the original disturbance feature vector x into a low-dimensional latent
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 9of22
representation z = ε(x). Thisstepcapturesessentialpatternsofforestdisturbanceand
succession. Itallowsthegenerationprocesstooperateinacompactlatentspace.
ForwardDiffusionandConditionalDenoisingLearning
TheLDMisbasedontwostochasticprocesses. Intheforwarddiffusionprocess,small
Gaussiannoiseisgraduallyaddedtotheinitiallatentvariablez overTtimesteps. This
0
produces a sequence of noisy states z ,..., z . When T is large, the signal approaches
1 T
isotropicGaussiannoise. Thereverseprocessisaconditionaldenoisingprocessandisused
togeneratepseudo-samples. Atime-dependentdenoisingnetworkϵ (z ,t,y),basedon
θ t
U-Net,istrainedtopredicttheinjectednoise. Themodeltakesthenoisylatentvariable
z ,timestept,anddisturbanceclassconditionyasinput. Theobjectiveistoestimatethe
t
noiseaddedateachstep. Thelossfunctionisdefinedasfollows:
(cid:104) (cid:105)
L =E ∥ϵ−ϵ (z ,t,y)∥2 (1)
{LDM} {z,ϵ∼N(0,1),t} θ t
The guiding signal y is derived from high-purity labeled samples filtered through
confidencelearning,ensuringthedirectionalityofthegenerationprocess. Thismechanism
enablestheprecisesynthesisoffeaturescorrespondingtospecificforestdisturbancetypes
basedonpracticalrequirements.
ReconstructionofMinorityClassPseudo-Samples
Duringtheinferencestage, theprocessoriginatesfromrandomGaussiannoise z .
T
Guidedbythetargetminorityclasslabel,thedenoisedlatentvectorzˆ isobtainedthrough
0
aniterativereversedenoisingprocess. Finally,theVAEDecoderxˆ = D(ˆzˆ )mapsitbackto
0
theoriginalmultidimensionalfeaturespace.
Thepseudo-samplessynthesizedviatheLDMmaintainhighstatisticalconsistency
withtheauthenticsamples. Moreover,theyeffectivelycapturethenon-linearcorrelations
betweenspectralbandsundervaryingdisturbanceintensities. Comparedtotraditional
interpolation-basedaugmentationmethods,thisgenerativeprobabilisticapproachprovides
more diverse and physically meaningful hard examples. Consequently, it significantly
enhancesthedecisionrobustnessoftheclassifierwhenoperatingwithinhighlyimbalanced
dataenvironments.
3.2.3. DesignofaCL-BasedCriterionforLabeledSampleAugmented
Toensurethequalityofaugmentedsamples,thisstudyincorporatestheCLframework.
Byestimatingthejointdistributionbetweennoisylabelsandtruelabels,theframework
enablestheautomatedfiltrationofhigh-confidencesamples.
The core of CL lies in estimating the joint distribution matrix Q∼
y,y∗
through the
correspondencebetweenthesample’spredictedprobabilitymatrixanditsnoisylabels.
ThepredictedprobabilityP(y = j|x )forsampleibelongingtoclassjisobtainedviacross-
i
validation. Foreachclassj,theaverageprobabilitywithintheclassassignedbythebase
classifieriscalculatedastheconfidencethresholdt :
j
1 ∑ (cid:16)∼ (cid:17)
t[j] = (cid:12) (cid:12) ∼ P y = j,x,θ (2)
(cid:12)
(cid:12)
X∼
y=j
(cid:12)
(cid:12)
x∈y=j
whereθdenotesthemodel. AcountingmatrixC∼
y,y∗
(analogoustoaconfusionmatrix)is
thencomputedasfollows:
(cid:12) (cid:12)
C∼
y,y∗
[i][j]:= (cid:12)
(cid:12)
X∼
y=i,y∗=j
(cid:12)
(cid:12)
(3)
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579
10of22
|     |     | (cid:110) |     | (cid:16)∼ | (cid:17) |     |     | (cid:16)∼ (cid:17)(cid:111) |     |
| --- | --- | --------- | --- | --------- | -------- | --- | --- | --------------------------- | --- |
whereX∼ = xϵX∼ : P y = j,x,θ ≥ t[j],j =argmaxP y = l;x,θ ,andl ∈ [m]
|            | y=i,y∗=j  |         | y=i      |     |     |     |     |     |     |
| ---------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
|            | (cid:16)∼ |         | (cid:17) |     |     |     |     |     |     |
| satisfiesP | y         | = l;x,θ | ≥ t      | .   |     |     |     |     |     |
l
Subsequently,thecountingmatrixiscalibratedtoensurethetotalcountmatchesthe
numberofsampleslabeledbythebaseclassifier:
C
|     |     |     | ∼          |     |           | ∼ y = i,y ∗ = j |     | (cid:12) (cid:12)     |     |
| --- | --- | --- | ---------- | --- | --------- | --------------- | --- | --------------------- | --- |
|     |     |     | C          | =   |           |                 | ×   | (cid:12) X∼ (cid:12)  | (4) |
|     |     |     | ∼ y=i,y∗=j |     | ∑         |                 |     | (cid:12) y=j (cid:12) |     |
|     |     |     |            |     | j∈1,2 ,3, | .. .,m C ∼      |     |                       |     |
y = i,y∗=j
| (cid:12)      | (cid:12)     |                                              |     |     |     |     |     |       |     |
| ------------- | ------------ | -------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- |
| where(cid:12) | (cid:12)     |                                              |     |     |     |     |     | ∼     |     |
|               | X∼           | isthetotalnumberofsampleswiththepseudo-label |     |     |     |     |     | y =i. |     |
| (cid:12)      | y=j (cid:12) |                                              |     |     |     |     |     |       |     |
∼
andtruelabelsy∗isestimatedasfollows:
| ThejointdistributionQ∼ |     |     |     | ofnoisylabels |     | y   |     |     |     |
| ---------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
y,y∗
∼
C∼
y=i,y∗=j
|     |     |     | Q∼  |          | =   |     |     |     | (5) |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     | y=i,y∗=j |     |     | ∼   |     |     |
∑
|     |     |     |     |     | i∈1,...,m,j∈1,...,m |     | C∼  |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
y=i,y∗=j
Thisjointdistributioneffectivelyreflectsthedistributionofnoisy(erroneous)labels
andtruelabelsinreal-worldscenarios;asthedatascaleexpands,thisestimationincreas-
ingly converges toward the true distribution. Upon obtaining the joint distribution, a
clean-upstrategyisimplementedforqualitycontrolbasedonthefollowingcriteria:
ConsistencyFiltering: Samplesareidentifiedwheretheclassindexcorrespondingto
themaximumpredictedprobabilitydoesnotmatchthelabelassignedbythebaseclassifier.
̸=
Samplesfallingintothenon-diagonalunits(j k)ofthecountingmatrixarefilteredoutas
suspectednoise.
ProbabilityGapRanking: Forsamplesinnon-diagonalunits,filteringisperformed
basedontheestimatednoisequantityn foreachclass. Sampleswiththesmallestmargin
jk
betweenthepredictedprobabilityandthethreshold,calculatedasP(y = k|x)−P(y = j|x),
areprioritizedforexclusion.
3.3. AccuracyEvaluationMetrics
To quantitatively evaluate the similarity between the multidimensional pseudo-
samplesgeneratedbytheLDMandtheauthenticforestdisturbancesamples,theFréchet
InceptionDistance(FID)isemployed. Assumingthatthefeaturedistributionoftheauthen-
ticsamplesfollowsamultivariatenormaldistributionwithmeanµ andcovariancematrix
r
σ r ,andthegeneratedsampledistributionfollowsamultivariatenormaldistributionwith
| meanµ | g andcovariancematrixσ |     |     | g ,theFIDisdefinedasfollows: |     |     |     |     |     |
| ----- | ---------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
(cid:12)
|     |     |     | (cid:0)P | P (cid:1)    |          | (cid:16) |       | (cid:0)Σ (cid:1)1/2 (cid:17) |     |
| --- | --- | --- | -------- | ------------ | -------- | -------- | ----- | ---------------------------- | --- |
|     |     | FID | ,        | = (cid:12)µ  | −µ |2+Tr | Σ        | +Σ −2 | Σ                            | (6) |
|     |     |     | r        | g (cid:12) r | g 2      | r        | g     | r g                          |     |
whereTrrepresentsthetraceofthematrix. AlowerFIDvalueindicatesahigherdegree
of statistical similarity between the synthetic and authentic forest disturbance features,
suggestingsuperiorgenerativeperformance.
Toquantitativelyevaluatethefidelityofthephysicalattributesofthepseudo-samples,
theCorrelationCoefficient(R)isemployedtomeasurethelinearcorrelationbetweenthe
| synthesizedandauthenticspectralcurves. |     |     |     |     |         | Theformulaisasfollows: |         |     |     |
| -------------------------------------- | --- | --- | --- | --- | ------- | ---------------------- | ------- | --- | --- |
|                                        |     |     |     |     | (cid:0) | (cid:1)(cid:0)         | (cid:1) |     |     |
|                                        |     |     |     |     | ∑n S    | −S G                   | −G      |     |     |
|                                        |     |     |     | R = | i=1     | i                      | i       |     | (7) |
(cid:113)
|     |     |     |     |     | (cid:0) | (cid:1)2∑n | (cid:0) | (cid:1)2 |     |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- | -------- | --- |
|     |     |     |     | ∑n  | S −S    |            | G −G    |          |     |
|     |     |     |     |     | i=1 i   | i=1        | i       |          |     |
wherenrepresentsthetotalnumberofspectralbandsintheLandsatimagery;S andG
i i
denotethemeanspectralreflectanceoftheauthenticandgeneratedsamplesintheband
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 11of22
i,respectively;SandGrepresenttheoverallaveragespectralreflectanceacrossallbands.
ThevalueofRrangesfrom[−1,1].
The accuracy of both the disturbance detection and the classification models is as-
sessedusingaconfusionmatrix,whichreflectsthepredictiveperformanceforeachindi-
vidualcategory. Basedontheconfusionmatrix,OverallAccuracy(OA),User’sAccuracy
(UA)/Precision, Producer’s Accuracy (PA)/Recall, F1-score, and the Kappa coefficient
arecalculated.
TheOAiscalculatedasfollows:
∑k n
OA = i=1 ii ×100% (8)
N
wherekisthetotalnumberofclasses,n representsthenumberofpixelscorrectlyclassified
ii
onthediagonalofthematrix,andNisthetotalnumberofvalidationsamples.
ThePAiscalculatedasfollows:
n
PA = ii ×100% (9)
i
n+i
wheren+i isthetotalnumberofreferencesamplesforthedisturbanceclassi. AhigherPA
indicatesfeweromissionerrorsforthatspecificcategory.
TheUAiscalculatedasfollows:
n
UA = ii ×100% (10)
i
n i+
wheren i+ isthetotalnumberofpixelsclassifiedintothedisturbanceclassiintheclassifi-
cationmap. AhigherUAindicatesfewercommissionerrorsforthatspecificcategory.
2×Precision ×Recall
F1 = i i (11)
i (Precision +Recall )
i i
The Kappa coefficient was used to evaluate the agreement between classification
resultsandreferencelabels:
(p −p )
Kappa = o e (12)
(1−p )
e
where p istheobservedagreementand p istheexpectedagreementbychance.
o e
4. Results
4.1. EvaluationofLDMPseudo-SampleGenerationQuality
ByintroducingtheLDMfortargetedsynthesis,theforestdisturbancelabeledsample
databaseinthestudyareaachievedastateofdynamicbalance. Intheoriginaldataset,
theratiobetweenmajorityandminorityclasseswasashighas7:1, exhibitingatypical
long-taildistributioncharacteristic. Intheinitialstage,theLDMlearnedtheunderlying
featurepatternsofvariousdisturbancetypes,leadingtoasteadyincreaseinsamplesize
acrossallcategoriesthroughpreliminarysynthesis. Ultimately, throughthesynergyof
class-specificguidedgenerationbytheLDMandsemi-supervisedsampleaugmentation
withintheSVM-RFframework,thescaleofminorityclasssampleswasexpandedtoreach
paritywiththemajorityclasses,whilethetotalsamplevolumereachedasufficientlevel.
AsillustratedinFigure5,theclassfrequencyhistogramtransitionedfromaprominent
“step-like”structuretoastable,“levelled”distribution.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 12of22
Figure 5. Statistical distribution of sample sizes for various forest disturbance types during the
generationandaugmentationprocess.
4.1.1. QualitativeEvaluationofPseudo-Samples
Inthisstudy,thephysicalfidelityofthegenerateddatawasqualitativelyevaluated
by comparing the visualization of authentic disturbance samples with LDM-generated
samplesbeforeandafterdisturbances(Figure6)andtheircorrespondingspectralresponse
curves(Figure7).
AsshowninFigure6,thepseudo-samplesgeneratedbytheLDMaccuratelyreplicate
thespatialtextureandcolorcharacteristicsofauthenticdisturbancepixelsacrossfourdis-
turbancetypes. Notably,intheRoadConstructioncategory,despitetheextremescarcityof
initiallabeledsamples,theLDMsuccessfullylearnedthedynamicevolutioncharacteristics
ofartificialimpervioussurfaces(appearinggray-white)withincomplexforestbackgrounds
from the latent space. The generated post-disturbance images exhibit a high degree of
similaritytoauthenticobservations.
Figure6. Visualcomparisonofgeneratedsamplesbeforeandafterperturbation,withredboxes
indicatingkeyareasofchange.(an),(bn),(cn),n=1,2,3,4,representthethreerepresentativecases
ofthistype.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 13of22
Regardingthemorphologyofspectralevolution,thepseudo-samplesgeneratedbythe
LDMpreciselycapturedthespectralshiftpatternsdrivenbydifferentdisturbancefactors.
IntheRoadConstructionclass,asignificantincreaseinreflectanceacrossallbandswas
observed,particularlyintheShort-WaveInfrared(SWIR,1610nmand2200nm)regions;
thegeneratedsamplesaccuratelyreconstructedthehigh-reflectancepropertiescausedby
forest replacement with impervious surfaces or bare soil. In the Logging category, the
synthesizedsamplessuccessfullysimulatedthesharpdeclineintheNear-Infrared(NIR)
band due to canopy loss, accompanied by a subtle increase in visible-light reflectance,
reflectingtheexposureofunderstoryvegetationorsoil. FortheClearancecategory,the
LDMpreciselycapturedthecoreshiftpatternwherereflectanceintheRed(655nm)and
SWIRbandsrisessignificantlyduringtheinitialclearingstage. IntheFirecategory,the
carbonizationofthelandsurfaceleadstoasubstantialdecreaseinreflectanceacrossthe
entire spectrum. The curves generated by the LDM nearly overlap with the authentic
ones,demonstratingexceptionallyhighfidelityinsimulatingthelow-reflectancephysical
attributesofburnscars.
Thehighconsistencyinthespatiotemporalandspectraldimensionsbeforeandafter
changes forcefully demonstrates that the LDM could overcome the constraints of limited
observationsamples. Bygeneratinghardexampleswithrigorousspectrallogic,themodel
provideshigh-qualitydatasupportforestablishingrobustclassificationdecisionboundaries.
Figure7. ComparisonofreflectanceatLandsatbandcentersbeforeandafterfourtypesofforest
disturbance.(a)Roadconstruction,(b)logging,(c)clearingforcultivation,and(d)fire.
4.1.2. QuantitativeEvaluationofPseudo-Samples
Inthisstudy,theFIDandtheRwereemployedtoquantitativelyevaluatethequality
ofLDM-generatedsamplesfromtwodimensions: featurespacedistributionandphysical
spectralfidelity(Table4). TheresultsindicatethattheLDMmaintainedconsistentlylow
FID values, even for disturbance categories with limited initial samples, such as road
constructionandclearingforcultivation. Thissuggeststhatthemodelhassuccessfully
capturedtheunderlyingmanifoldstructureofminorityclassdisturbanceswithinthelatent
space,ratherthanperformingsimplepixel-levelcloning. SuchlowFIDvaluesensurethat
theaugmentedsampledatabasenotonlyachievesnumericalbalancebutalsoaccurately
reflectsthestochasticityandcomplexityofnaturalforestdisturbancesintermsofstatistical
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579
14of22
characteristics. Furthermore, the correlation coefficients between the average spectral
curvesofauthenticandgeneratedsamplesdemonstrateahighdegreeofconsistencyacross
thefourprimaryforestdisturbancetypes.
Table4.Quantitativeevaluationresultsofpseudo-samples.
|     |     | DisturbanceType        |         | OriginalCount |     | FID   |     | R    |
| --- | --- | ---------------------- | ------- | ------------- | --- | ----- | --- | ---- |
|     |     |                        | Logging |               | 380 | 22.41 |     | 0.85 |
|     |     |                        | Fire    |               | 142 | 24.73 |     | 0.82 |
|     |     | Clearingforcultivation |         |               | 86  | 27.56 |     | 0.79 |
|     |     | Roadconstruction       |         |               | 54  | 29.18 |     | 0.76 |
ThesynergisticperformanceofFIDandthecorrelationcoefficientprovesthattheLDM
doesnotmerelyreplicatesamples.Instead,bylearningthedistributionpatternsofminority
disturbances,itachieveshigh-qualitydistributioncompletion. Thisprovidesarobustdata
foundationformitigatingtheclassificationbiastypicallyinducedbysampleimbalance.
4.2. ClassificationAccuracyEvaluationofForestDisturbanceTypes
4.2.1. OverallClassificationAccuracyAssessment
Theproposedcross-guidanceframeworkservesasthefinaltoolforevaluatingthe
classificationaccuracyofforestdisturbancetypes. AspresentedinTable5,theframework
demonstratesexceptionalperformanceinidentifyingthefourforestdisturbancecategories,
achievinganOAof93.2%. TheRecallvaluesforalldisturbancetypesexceeded90%,while
thePrecisionvaluesforClearingforCultivationandFirewererelativelylower,at86.2%
and89.3%,respectively. Theseresultsvalidatetherobustnessofthesynergisticmechanism
betweengenerativeaugmentationandsemi-supervisedlearningwhenaddressingtasks
characterizedbyimbalancedandsmall-sampledatasets.
Table5. Confusionmatrixforforestdisturbancetypeclassificationbasedonconfidencelearning
mutualguidanceframework.
RoadConstruction Logging ClearingforCultivation Fire PA/Recall F1-Score
|     | (Pred.) |     | (Pred.) | (Pred.) |     | (Pred.) | (%) | (%) |
| --- | ------- | --- | ------- | ------- | --- | ------- | --- | --- |
Road
|     |     | 50  | 3   |     | 1   | 0   | 92.6 | 92.6 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- |
Construction(Ref.)
| Logging(Ref.) |     | 3   | 353 |     | 9   | 15  | 92.9 | 94.8 |
| ------------- | --- | --- | --- | --- | --- | --- | ---- | ---- |
Clearingfor
|     |     | 1   | 3   |     | 81  | 1   | 94.2 | 90.0 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- |
Cultivation(Ref.)
| Fire(Ref.)      |      | 0   | 6    |      | 3    | 133  | 93.7 | 91.4 |
| --------------- | ---- | --- | ---- | ---- | ---- | ---- | ---- | ---- |
| UA/Precision(%) | 92.6 |     | 96.7 |      | 86.2 | 89.3 | —    | —    |
| OA(%)           |      |     |      | 93.2 |      |      |      | —    |
| Kappa(%)        |      |     |      | 88.9 |      |      |      | —    |
Theannualspatialdistributionofdisturbancetypesfrom2000to2021isillustrated
inFigure8. LoggingandFirearethepredominantdisturbancetypes. RoadConstruction
eventsaremainlydistributedwithintheforestmarginsandperipheralregions. Fourtypes
ofdisturbancesspannearlytheentirestudyarea. Basedonthestatisticalanalysis,thetotal
forestareaaffectedbyvariousdisturbancetypesreached1392.3km2.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 15of22
Figure8.Overallspatialdistributionofforestdisturbancetypes.Theenlargedsubfiguresrepresent
typicalexamplesof(a)roadconstruction,(b)logging,(c)clearingforcultivation,and(d)fire.
4.2.2. AblationExperiment
To evaluate the effectiveness of the LDM and the MGF based on CL, four sets of
ablationexperimentswereconducted(Table6). Bycomparingclassificationperformance
acrossdifferentstrategies,thecontributionofeachmoduletoaddressingtheimbalancein
smallsamplesizeswasanalyzed.
Table6.Theresultsoftheablationexperiment.
Strategy OA EffectSize
ExperimentalDescription 95%CI p-Valuevs. M4
Number (%) (Cohen’sd)vs. M4
Originalimbalancedsmallsample
M1 87.5±1.5 [86.4,88.6] <0.001 4.39
+SingleRFclassifier
Originalimbalancedsmallsample
M2 88.8±1.3 [87.9,89.7] <0.001 3.70
+SingleSVMclassifier
Originalimbalancedsmallsample
M3 91.4±1.0 [90.7,92.1] 0.004 1.99
+SVM-RFMGFbasedonCL
LDMsamplebalancing+SVM-RF
M4 93.2±0.8 [92.6,93.8] Reference Reference
MGFbasedonCL
Note:OAvaluesarereportedasmean±standarddeviationbasedon10repeatedrandomexperiments. The
p-valueswerecalculatedusingpairedt-testsbycomparingeachbaselinestrategywithM4.Cohen’sdwasusedto
quantifytheeffectsizeoftheimprovement.
Duetotheconstraintsoftheoriginalimbalancedandsmall-scaledatasets,traditional
singleclassifiers(M1andM2)exhibitedlimitedperformance,withOAof87.5%and88.8%,
respectively. AnalysisofFigure9revealsaseveremajority-classbiasinthebaselinemod-
els,drivenbythesparsityofminority-classsamples(e.g.,RoadConstruction,Fire). This
biasledtonumerousfinedisturbancepatchesbeingmisclassifiedasbackgroundforestor
large-scaleloggingareas. WiththeintroductionoftheMGFbasedonCL(M3),theoverall
accuracyimprovedto91.4%. Thisdemonstratesthattheco-trainingmechanismcaneffec-
tivelyextracthigh-confidenceinformationfromunlabeleddata. However,M3remained
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 16of22
constrained by the long-tail distribution of the original data, and the improvement for
extrememinorityclassesencounteredaperformancebottleneck(e.g.,RoadConstruction).
Thecompleteframeworkproposedinthisstudy(M4)achievedthehighestclassification
accuracy,representingafurtherimprovementof1.8%overM3. Theexperimentalresults
indicatethatfilteringatthealgorithmiclevelaloneisinsufficient;distributionreconstruc-
tionviaLDMatthedatalevelisessential. AsshowninFigure9,acomparisonbetween
M3andM4revealsthatM4significantlyreducestheomissionrateforRoadConstruction.
Significantly,intheclearing-for-cultivationsample,M4effectivelydetectedthelongand
narrowunchangedareas.
Figure 9. Samples of the classification results of various types of perturbations under different
schemes.Sample(a)representsroadconstruction;(b)representslogging;(c)representsclearingfor
cultivation;(d)representsfire.Theblackoutlinesrepresenttheboundaryofdisturbancedetection
resultsfromtheCOLDalgorithm.Colorsindicatedisturbancetypes:blue,roadconstruction;orange,
logging;yellow,clearingforcultivation;andred,fire.
Thepowerfulsynergisticeffectbetweenthebalanceddistributionprovidedbythe
LDMandthehigh-qualityfiltrationprovidedbyCLnotonlycompletesthefeaturespaceof
raredisturbancesbutalsoenhancesthemodel’sdiscriminativerobustnesswithincomplex
landscapebackgrounds.
Tofurtherevaluatetherobustnessoftheablationresults,eachstrategywasrepeated
underdifferentrandomseeds. TheOAwasreportedasmean±standarddeviation,and
statisticalsignificancewasassessedusingp-values,Cohen’sd,and95%confidenceintervals.
ThecompleteframeworkM4achievedthehighestmeanOAandshowedstatistically
significantimprovementsoverthebaselinestrategies,indicatingthattheperformancegain
wasstableacrossrepeatedexperiments.
4.3. ErrorAnalysisofForestDisturbanceClassification
Figure 10 illustrates two typical cases of misclassification. In the region shown in
Figure10a–d,severelogging-inducedcanopydestructionresultedinextensivebare-soil
exposure,exhibitingacharacteristicgray-whitetone. Thisappearanceishighlysimilarto
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 17of22
typicalclearancefeatures,leadingtosomeloggingareasbeingmisclassifiedasclearingfor
cultivation. Undertheconstraintsofextremelysmallsamplesizes,theMGFreliesheavily
on the feature manifold of the latent space. Consequently, when the post-disturbance
surface of a logging area exhibits such extreme atypical features, the model tends to
categorize it into the clearance class due to their similar spectral responses. Also, this
confusion may be attributed to the 30 m spatial resolution of Landsat images, because
exposedsoil,residualvegetation,andsmalldisturbanceboundariescanbemixedwithin
onepixel.
Figure10.Typicalmisclassificationcasesinforestdisturbanceclassification.(a)GEPhigh-resolution
imagery of a logging-induced disturbance area; (b) Landsat 3-2-1 composite image of the same
loggingarea;(c)classificationresultshowingthattheloggingareawasmisclassifiedasclearingfor
cultivation; (d)aclearing-for-cultivationareawithsimilarspectralcharacteristics. (e)GEPhigh-
resolutionimageryofafire-affectedarea;(f)Landsat3-2-1compositeimageofthesamefire-affected
area;(g)classificationresultshowingthatalocalizedfire-affectedpatchwasmisclassifiedaslogging;
and(h)aloggingareawithsimilarspectralcharacteristics. Theredoutlinesindicatedisturbance
boundariesdetectedbytheCOLDalgorithm,andtheblackrectanglesmarkthecomparisonregions.
Colorsindicatedisturbancetypes:blueforroadconstruction,orangeforlogging,yellowforclearing
forcultivation,andredforfire.
Figure 10e–h present another representative misclassification case. In this region,
the overall background is dominated by large-scale forest fire disturbances; however,
alocalizedpatchwasincorrectlyidentifiedasLogging. Thiserroroccurredbecausethe
specificpatchexhibitedmorethoroughvegetationdestructioncomparedtothesurrounding
fire-affectedareas.Thenear-completecombustionofvegetationandorganiclitterlayersled
tohighsoilexposure,creatingahighdegreeofphysicalsimilaritytocommerciallogging
sites—specifically, forest clearing areas or temporary log landings. Although the MGF
learnedthetypicalspectralmanifoldoffiresviatheLDM,itremainssusceptibletothe
spectralconfusioneffectwhenencountering“brightoutlier”samplesthatdeviatefromthe
normalfiredistributionduetoextremecombustion. Insuchcases,themodeldefaultsto
theloggingcategory,whichoffersamoreconsistentspectralmatch. Thisresultindicates
thatfirescarsunderextremecombustionandloggingsiteswithstrongsoilexposuremay
showsimilarmixed-pixelspectralresponsesatLandsatresolution.
Figure11illustratestworepresentativecasesofomissionerrors. Intheregionshown
inFigure11a–c,severalloggedpatchesareclassifiedasundisturbedforest. Althoughthese
areasunderwentlogging,thegroundsurfacewasnotentirelydenuded;instead,itwas
rapidlycoveredbydensesecondaryherbaceousvegetationorresidualunderstory. Inthe
Landsatband3-2-1composite(false-color),thesepatchesexhibitaprominentgreenhue,
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 18of22
resultinginminimalspectraldifferentiationfromhealthyforestcanopies. Thisrapidreveg-
etationphenomenon(e.g.,fastweedencroachmentfollowingselectivelogging)effectively
masks the distinctive spectral signature of the underlying soil layer. Consequently, the
modelcategorizesthesepixelsasstableforest,leadingtosignificantomission.
Figure11.Typicalomissioncasesinforestdisturbanceclassification.(a)GEPhigh-resolutionimagery
ofaloggingcase;(b)Landsat3-2-1compositeimageoftheloggingarea;(c)classificationresultofthe
loggingcase;(d)GEPhigh-resolutionimageryofaclearing-for-cultivationcase;(e)Landsat3-2-1
compositeimageoftheclearing-for-cultivationarea;and(f)classificationresultoftheclearing-for-
cultivationcase.TheredoutlinesindicatedisturbanceboundariesdetectedbytheCOLDalgorithm,
andtheblackrectanglesmarktheomittedregions. Colorsindicatedisturbancetypes: blue,road
construction;orange,logging;yellow,clearingforcultivation;andred,fire.
In the region depicted in Figure 11d–f, certain clearing for cultivation areas were
omittedduetotheinfluenceofcloudcover. Duringthedatapreprocessingstage,affected
pixelswereremoved,preventingtheMGFfromacquiringthecontinuousfeatureevolution
of these specific locations. The lack of temporal consistency in the spectral trajectory
resultedinthefailuretodetectthesedisturbanceevents.
5. Discussion
Theproposedframeworkeffectivelyaddressestheproblemsofsmallsamplesandclass
imbalanceinforestdisturbanceclassification. Althoughgoodclassificationperformanceis
achieved,thereisstillroomforimprovement.
First, althoughtheLDMshowsstrongperformanceandeffectivelyalleviatesclass
imbalance,ithashighmodelcomplexityandrequiressubstantialcomputationalresources.
ItsadvantageisnotlimitedtothefinalOAimprovement;italsoprovidesminority-class
distribution completion and reduces the bias caused by long-tailed samples. The dif-
fusion model used in this study achieves high-quality sample generation but imposes
high demands on computation and inference efficiency. This limits its deployment in
resource-constrainedenvironments. Forforestdisturbancemonitoringatnationalorglobal
scales,spatialtransferofmodelweightsandincrementallearningremainkeychallenges.
Futureworkcanexplorelightweightdiffusionmodelsbyintegratingtechniquessuchas
knowledgedistillation,modelpruning,andstructuralreparameterization. Thismayenable
efficientandlow-powersamplegenerationandimprovethepracticalityandscalabilityof
theframeworkacrossedgedevicesandlarge-scalesystems.
Therequirementfordataaugmentationalsohasalearning-curvelimitation.Increasing
the number of generated samples can improve minority-class representation, but the
improvementisnotunlimited. AsshowninFigure12, aftertheclassifierapproachesa
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 19of22
stableperformancelevel,additionalsyntheticsamplesmaymainlyintroduceredundancy
or distributional bias rather than further accuracy gains. Therefore, the number and
qualityofsyntheticsamplesshouldbecarefullycontrolled. Thetheoreticalproxylearning
curve provides an important perspective for estimating sample-size requirements and
understandingtherelationshipbetweentrainingsamplesizeandprobabilityoferror. In
futurework,wewillfurtherexplorehowtocombineproxylearningcurveswithLDM-
basedsamplegenerationtooptimizetheamountofsyntheticsamplesrequiredforforest
disturbanceclassification.
Figure 12. Variation in overall accuracy with increasing LDM-generated samples during itera-
tivetraining.
The proposed MGF is related to collaborative learning and classifier fusion, but it
differsfromlate-fusionmethods. Meanfusion,Dempster–Shafertheory,BehaviorKnowl-
edge Space, copula-based fusion, and alpha-integration-based [50] soft fusion combine
classifier[51,52]outputsatthedecision-scoreorprobability-distributionlevel. Incontrast,
thecurrentMGFmainlyusesSVMandRFforconfidence-basedhardselectionofreliable
pseudo-labeledsamples. Therefore,theproposedframeworkfocusesonexpandingthe
reliablelabeledsetandreducingpseudo-labelnoiseunderimbalancedandsmall-sample
conditions. Advanced fusion methods, such as graph-regularized soft fusion based on
alphaintegration,mayprovideusefulextensionsforoptimizingdecision-levelintegration
infutureforestdisturbanceclassificationtasks.
Also,inthisstudy,samplelabelingfocusesonfourtypicaldisturbancetypes,including
roadconstruction,logging,clearingforcultivation,andfire. Thesetypescoverthemajor
disturbanceprocessesinthestudyarea. However,forestdisturbanceinrealscenariosis
morecomplexandheterogeneous. Somedisturbancetypesarenotincluded,suchaspest
infestationanddroughtstress. Thesebioticandabioticstressorsmayinfluencecanopy
structure, moisture condition, and thermal characteristics over longer time scales than
abruptdisturbances. Futureworkcouldexpandthedisturbancecategoriesduringsample
construction. Thiscanimprovetherepresentationofcomplexdisturbanceprocessesand
enhancemodelgeneralization. Thermalindicators,meteorologicalvariables,andpestor
droughtrecordscouldalsobeincorporatedwhenreliablelabelsareavailable.
In addition, this study performs forest disturbance classification at the pixel level.
Goodquantitativeaccuracyisachieved,buttheresultsshowspatialdiscontinuityandlim-
itedmappingquality. Thisismainlybecausepixel-basedmethodsignorespatialstructure.
Futureresearchshouldexploreobject-basedclassificationmethods. Byintegratingspatial
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 20of22
contextandspectralfeatures,thespatialconsistencyandmappingqualitycanbeimproved,
andclassificationaccuracycanbefurtherenhanced.
6. Conclusions
Toaddressthebottleneckissuesofextremescarcityoflabeledsamplesandsevere
classimbalanceinforestdisturbancemonitoring,thisstudyproposesanewframeworkfor
multi-typeforestdisturbanceclassificationthatcombinescollaborativesemi-supervised
learningandsamplegeneration. Theprimaryconclusionsareasfollows:
(1) Addressingclassificationbiasinducedbysampleimbalance. Bymininglatentevolu-
tionpatternsacrossmultiplespectralbands,theLDMachievedtargetedaugmentation
ofsamplesforraredisturbancetypes. Thegeneratedpseudo-samplesstrictlyfollow
thebiophysicallogicofvegetationdestructionintermsofspatialtextureandspectral
morphology. QuantitativeevaluationshowsthattheaverageFIDindexofthegen-
eratedsamplesis25.97,andallspectralcorrelationcoefficientsaregreaterthan0.75,
indicatingthatthedistributionofLDM-synthesizedsamplesishighlyalignedwith
authenticobservationsandprovidingareliabledatafoundationforthemodel.
(2) Addressinglabeledsmall-sampleconstraints: TheMGF,combinedwithCLcriteria,
achievedhigh-efficiencyknowledgeextractionfromunlabeleddataandeffectively
suppressed pseudo-label contamination. This allowed the model to obtain robust
classification results even with a very small number of manually labeled samples.
The OA reached 93.2%, which is an improvement of 5.7% and 4.4% over the sin-
gle RF and SVM baselines, respectively. Furthermore, after introducing the LDM
sample-balancingmechanism,theaccuracyfurtherincreasedby1.8%comparedto
thepuresemi-supervisedcross-guidanceframework. Thisprovesthepracticalvalue
ofthemethodinreducingmanualinterpretationcostsandenhancinggeneralization
capabilitiesincomplexscenarios.
In summary, this study provides a new technical paradigm for fine-grained forest
disturbance mapping under conditions of imbalanced and small size samples. While
significantlyreducingthecostofmanualinterpretation,thismethodensuresthetimeliness
andaccuracyofidentifyingdifferentdisturbancetypes,providingscientificandreliable
datasupportforregionalforestresourcemanagement,ecologicalcompensationaccounting,
andcarbonsinkevaluation.
AuthorContributions: Conceptualization, Y.L., Y.Z.andL.W.; methodology, Y.L., Y.Z., Y.Y.and
L.W.; software, Y.Z., Y.Z.andY.Y.; validation, Y.S.andX.Q.; formatanalysis, Y.L., Y.S.andX.Q.;
resources,L.W.;datacuration,Y.L.,Y.Y.,Y.S.andX.Q.;writing—originaldraftpreparation,Y.L.and
Y.Z.;writing—reviewandediting,Y.L.,Y.Z.andL.W.;supervision,L.W.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbytheDepartmentofScienceandTechnologyofGuangxiZhuang
AutonomousRegion,grantnumberGXKJAA24263014-2.
DataAvailabilityStatement:Therawdatasupportingtheconclusionsofthisarticlewillbemade
availablebytheauthorsonrequest.
Acknowledgments: ThisworkwassupportedbytheHigh-performanceComputingPlatformof
ChinaUniversityofGeoscience,Beijing. WethanktheGoogleEarthEngineforprovidingLand-
satdata.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 21of22
References
1. Costa,J.R.S.;Brancalion,P.H.S.;Joly,F.-X.;Simões,L.H.P.;Bonfanti,J.;Maire,G.l.;Robin,A.;Guillemot,J.ForestEcosystem
Multifunctionality:ASystematicReviewofMeasuresandDrivers.Curr.For.Rep.2026,12,2.[CrossRef]
2. Pang,D.;Xu,H.CarbonSequestrationandStabilityandSoilErosioninForestEcosystems.Forests2024,15,1961.[CrossRef]
3. Wu,Y.;Zheng,J.;Gao,J.;He,X.;Liu,X.;Chen,Y.;Liu,J.;Li,C.FunctionalDiversityExplainsEcosystemCarbonStoragein
SubtropicalForests.Glob.ChangeBiol.2025,31,e70120.[CrossRef]
4. Chen,S.;Woodcock,C.E.;Gu,H.;Dong,L.;Tang,X.;Olofsson,P.DriversofforestdisturbanceinSoutheastAsia. Int. J.Appl.
EarthObs.Geoinf.2026,148,105220.[CrossRef]
5. Suarez,D.R.;Rozendaal,D.M.A.;DeSy,V.;Decuyper,M.;Málaga,N.;Montesinos,P.D.;Olivos,A.A.;DelaCruzPaiva,R.;
Martius,C.;Herold,M.ForestdisturbanceandrecoveryinPeruvianAmazonia.Glob.ChangeBiol.2023,29,3601–3621.[CrossRef]
6. Hurteau,M.D.;Baker,R.;Gonterman,K.;Granath,A.;Lopez-Binder,J.;Taylor,M.D.;Rojas,L.S.;Rotche,L.;Graves,A.;Goodwin,
M.J.;etal.ChangingclimateanddisturbanceeffectsonsouthwesternUSforests.For.Ecol.Manag.2025,575,122388.[CrossRef]
7. Liu,X.;Li,Z.-L.;Li,J.-H.;Leng,P.;Liu,M.;Gao,M.TemporalupscalingofMODIS1-kminstantaneouslandsurfacetemperature
tomonthlymeanvalue:Methodevaluationandproductgeneration.IEEETrans.Geosci.RemoteSens.2023,61,5001214.[CrossRef]
8. Liu,X.;Li,Z.-L.;Li,Y.;Wu,H.;Zhou,C.;Si,M.;Leng,P.;Duan,S.-B.;Yang,P.;Wu,W.;etal. Localtemperatureresponsesto
actuallandcoverchangespresentsignificantlatitudinalvariabilityandasymmetry.Sci.Bull.2023,68,2849–2861.[CrossRef]
9. Huo,L.-Z.;Boschetti,L.;Sparks,A.M.Object-BasedClassificationofForestDisturbanceTypesintheConterminousUnitedStates.
RemoteSens.2019,11,477.[CrossRef]
10. van der Woude, S.; Reiche, J.; Balling, J.; Nabuurs, G.-J.; Sterck, F.; Welsink, A.-J.; Slagter, B.; Herold, M. European forest
disturbancealertingusingSentinel-1.RemoteSens.Environ.2026,337,115325.[CrossRef]
11. Zhang,T.;Wu,L.;Liu,X.;Liu,M.;Chen,C.;Yang,B.;Xu,Y.;Zhang,S.DetectionofForestDisturbanceswithDifferentIntensities
UsingLandsatTimeSeriesBasedonAdaptiveExponentiallyWeightedMovingAverageCharts.Forests2024,15,19.[CrossRef]
12. Qiu,L.;Chang,Z.;Luo,X.;Chen,S.;Jiang,J.;Lei,L.MonitoringForestDisturbancesandAssociatedDrivingForcesinGuangdong
ProvinceUsingLong-TermLandsatTimeSeriesImages.Forests2025,16,189.[CrossRef]
13. Fekety,P.A.;Vogeler,J.C.;Filippelli,S.K.;Nelson,M.D.Forestdisturbanceattributionandsensitivitytoharvestdetectionwith
LandsatintheGreatLakesregion,USA.For.Ecol.Manag.2025,595,123039.[CrossRef]
14. Zhang, Y.; Wang, X.; Li, X.; Zhao, W.; Zhong, X.; Yu, B.; Du, Y.; Atkinson, P.M. Characterizing Tropical Evergreen Forest
DisturbancesandPost-DisturbanceRecoveryUsingTime-SeriesLandsatCanopyOpenings.IEEETrans.Geosci.RemoteSens.2025,
63,4420823.[CrossRef]
15. Liang,Y.;Shang,R.;Chen,J.M.;Lin,X.;Li,P.;Yang,Z.;Fan,L.;Xu,S.;Lin,Y.;Chen,Y.ComprehensiveComparisonandValidation
ofForestDisturbanceMonitoringAlgorithmsBasedonLandsatTimeSeriesinChina.RemoteSens.2025,17,680.[CrossRef]
16. Singh,A.Digitalchangedetectiontechniquesusingremotely-senseddata.Int.J.RemoteSens.1989,10,989–1003.[CrossRef]
17. Griffiths,P.;Kuemmerle,T.;Baumann,M.;Radeloff,V.C.;Abrudan,I.V.;Lieskovsky,J.;Munteanu,C.;Ostapowicz,K.;Hostert,P.
Forestdisturbances,forestrecovery,andchangesinforesttypesacrosstheCarpathianecoregionfrom1985to2010basedon
Landsatimagecomposites.RemoteSens.Environ.2014,151,72–88.[CrossRef]
18. Xiao,P.;Sheng,G.;Zhang,X.;Liu,H.;Guo,R.Direction-dominatedchangevectoranalysisforforestchangedetection. Int. J.
Appl.EarthObs.Geoinf.2021,103,102492.[CrossRef]
19. Cardille,J.A.;Perez,E.;Crowley,M.A.;Wulder,M.A.;White,J.C.;Hermosilla,T.Multi-sensorchangedetectionforwithin-year
captureandlabellingofforestdisturbance.RemoteSens.Environ.2022,268,112741.[CrossRef]
20. Verbesselt,J.;Hyndman,R.;Newnham,G.;Culvenor,D.Detectingtrendandseasonalchangesinsatelliteimagetimeseries.
RemoteSens.Environ.2010,114,106–115.[CrossRef]
21. Kennedy,R.E.;Yang,Z.;Cohen,W.B.DetectingtrendsinforestdisturbanceandrecoveryusingyearlyLandsattimeseries:1.
LandTrendr—Temporalsegmentationalgorithms.RemoteSens.Environ.2010,114,2897–2910.[CrossRef]
22. Zhu,Z.;Woodcock,C.E.ContinuouschangedetectionandclassificationoflandcoverusingallavailableLandsatdata.Remote
Sens.Environ.2014,144,152–171.[CrossRef]
23. DeMarzo,T.;Gasparri,N.I.;Lambin,E.F.;Kuemmerle,T.AgentsofForestDisturbanceintheArgentineDryChaco.RemoteSens.
2022,14,1758.[CrossRef]
24. Hansen,M.C.;Potapov,P.V.;Moore,R.;Hancher,M.;Turubanova,S.A.;Tyukavina,A.;Thau,D.;Stehman,S.V.;Goetz,S.J.;
Loveland,T.R.;etal.High-ResolutionGlobalMapsof21st-CenturyForestCoverChange.Science2013,342,850–853.[CrossRef]
25. Sebald,J.;Senf,C.;Seidl,R.Humanornatural?Landscapecontextimprovestheattributionofforestdisturbancesmappedfrom
LandsatinCentralEurope.RemoteSens.Environ.2021,262,112502.[CrossRef]
26. Senf,C.;Seidl,R.MappingtheforestdisturbanceregimesofEurope.Nat.Sustain.2021,4,63–70.[CrossRef]
27. Oeser,J.; Pflugmacher,D.; Senf,C.; Heurich,M.; Hostert,P.UsingIntra-AnnualLandsatTimeSeriesforAttributingForest
DisturbanceAgentsinCentralEurope.Forests2017,8,251.[CrossRef]
https://doi.org/10.3390/rs18101579

RemoteSens.2026,18,1579 22of22
28. Ahmed,O.S.;Wulder,M.A.;White,J.C.;Hermosilla,T.;Coops,N.C.;Franklin,S.E.Classificationofannualnon-standreplacing
boreal forest change in Canada using Landsat time series: A case study in northern Ontario. Remote Sens. Lett. 2017, 8,
29–37.[CrossRef]
29. Hislop,S.;Haywood,A.;Alaibakhsh,M.;Nguyen,T.H.;Soto-Berelov,M.;Jones,S.;Stone,C.Areferencedataframeworkforthe
applicationofsatellitetimeseriestomonitorforestdisturbance.Int.J.Appl.EarthObs.Geoinf.2021,105,102636.[CrossRef]
30. Rodman,K.C.;Andrus,R.A.;Veblen,T.T.;Hart,S.J.Disturbancedetectioninlandsattimeseriesisinfluencedbytreemortality
agentandseverity,notbypriordisturbance.RemoteSens.Environ.2021,254,112244.[CrossRef]
31. Li,Y.;Xu,X.;Wu,Z.;Fan,H.;Tong,X.;Liu,J.Aforesttype-specificthresholdmethodforimprovingforestdisturbanceandagent
attributionmapping.GIScienceRemoteSens.2022,59,1624–1642.[CrossRef]
32. Liu, S.; Du, K.; Bruzzone, L.; Du, Q.; Bovolo, F.; Tong, X. An Adaptive Pseudo-Labeled Sample Generation Approach to
Unsupervised Multiclass Change Detection in Bitemporal Remote Sensing Images. IEEE Trans. Geosci. Remote Sens. 2026,
64,5503616.[CrossRef]
33. Chen,P.;Li,P.;Wang,B.;Zhao,S.;Zhang,Y.;Zhang,T.;Ding,X.B3-CDG:Apseudo-samplediffusiongeneratorforbi-temporal
buildingbinarychangedetection.ISPRSJ.Photogramm.RemoteSens.2024,218,408–429.[CrossRef]
34. Dong,W.;Yang,Y.;Qu,J.;Xiao,S.;Li,Y.LocalInformationEnhancedGraph-TransformerforHyperspectralImageChange
DetectionwithLimitedTrainingSamples.IEEETrans.Geosci.RemoteSens.2023,61,5509814.[CrossRef]
35. Wang,X.;Du,P.;Chen,D.;Liu,S.;Zhang,W.;Li,E.ChangeDetectionBasedonLow-LeveltoHigh-LevelFeaturesIntegration
withLimitedSamples.IEEEJ.Sel.Top.Appl.EarthObs.RemoteSens.2020,13,6260–6276.[CrossRef]
36. Wang,Z.; Wang,P.; Liu,K.; Wang,P.; Fu,Y.; Lu,C.-T.; Aggarwal,C.C.; Pei,J.; Zhou,Y.AComprehensiveSurveyonData
Augmentation.IEEETrans.Knowl.DataEng.2026,38,47–66.[CrossRef]
37. Zhang, H.; Cisse, M.; Dauphin, Y.N.; Lopez-Paz, D. MixUp: Beyond empirical risk minimization. arXiv 2018, arXiv:
1710.09412.[CrossRef]
38. Goodfellow,I.J.;Pouget-Abadie,J.;Mirza,M.;Xu,B.;Warde-Farley,D.;Ozair,S.;Courville,A.;Bengio,Y.GenerativeAdversarial
Nets.arXiv2014,arXiv:1406.2661.[CrossRef]
39. Rombach,R.;Blattmann,A.;Lorenz,D.;Esser,P.;Ommer,B.High-ResolutionImageSynthesiswithLatentDiffusionModels.
arXiv2022,arXiv:2112.10752.[CrossRef]
40. Shi,B.;Guo,H.;Sun,Y.;Long,J.;Yang,L.;Zhou,Y.;Jiao,J.;Zhou,J.;He,Y.;Li,H.BiFusion-LDSeg:ALatentDiffusionFramework
withBi-DirectionalAttentionFusionforLandslideSegmentationinSatelliteImagery.RemoteSens.2026,18,719.[CrossRef]
41. Wang,Z.;Hao,Z.;Zhang,Y.;Feng,Y.;Guo,Y.UP-Diff:LatentDiffusionModelforRemoteSensingUrbanPrediction.IEEEGeosci.
RemoteSens.Lett.2025,22,7502505.[CrossRef]
42. Chen,C.;Lu,H.;Wang,H.;Zhang,L.;Fan,W.DeepActiveTransferLearningforCross-DomainFaultDiagnosiswithLimited
Samples.IEEETrans.Instrum.Meas.2025,74,3527012.[CrossRef]
43. Zhu,L.;Dai,J.;Liu,Y.;Yuan,S.;Qin,T.;Walker,J.P.Across-resolutiontransferlearningapproachforsoilmoistureretrievalfrom
Sentinel-1usinglimitedtrainingsamples.RemoteSens.Environ.2024,301,113944.[CrossRef]
44. Zhang,L.;Yang,L.;Ma,T.;Shen,F.;Cai,Y.;Zhou,C.Aself-trainingsemi-supervisedmachinelearningmethodforpredictive
mappingofsoilclasseswithlimitedsampledata.Geoderma2021,384,114809.[CrossRef]
45. Fang,B.;Li,Y.;Zhang,H.;Chan,J.C.-W.Collaborativelearningoflightweightconvolutionalneuralnetworkanddeepclustering
forhyperspectralimagesemi-supervisedclassificationwithlimitedtrainingsamples.ISPRSJ.Photogramm.RemoteSens.2020,
161,164–178.[CrossRef]
46. Chaudhuri,U.;Dey,S.;Datcu,M.;Banerjee,B.;Bhattacharya,A.Inter-bandRetrievalandClassificationUsingtheMulti-labeled
Sentinel-2BigEarthNetArchive.IEEEJ.Sel.Top.Appl.EarthObs.RemoteSens.2021,14,9884–9898.[CrossRef]
47. Viana-Soto,A.;Senf,C.TheEuropeanForestDisturbanceAtlas: AforestdisturbancemonitoringsystemusingtheLandsat
archive.EarthSyst.Sci.Data2025,17,2373–2404.[CrossRef]
48. Wang,L.;Liu,S.;Song,W.;Ding,S.;Zhang,J.;Zhang,J.Globalhigh-resolutionforestdisturbancetypedataset.EarthSyst.Sci.
Data2026,18,1601–1617.[CrossRef]
49. Yan,Y.;Ling,W.;Junji,L.;Yuxin,Z.;Xin,Y.ForestDisturbanceAttributionunderSmallSampleConditionsBasedonConfidence
LearningMutualGuidanceFramework.Chin.J.SpaceSci.2025,45,397–412.[CrossRef]
50. Salazar, A.; Safont, G.; Vergara, L.; Vidal, E. Graph Regularization Methods in Soft Detector Fusion. IEEE Access 2023, 11,
144747–144759.[CrossRef]
51. Salazar,A.;Vergara,L.;Vidal,E.AproxylearningcurvefortheBayesclassifier.PatternRecognit.2023,136,109240.[CrossRef]
52. Vergara,L.;Salazar,A.OntheOptimumLinearSoftFusionofClassifiers.Appl.Sci.2025,15,5038.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/rs18101579