Remote Sensing of Environment 315 (2024) 114475
ContentslistsavailableatScienceDirect
Remote Sensing of Environment
journalhomepage:www.elsevier.com/locate/rse
Forest disturbance detection in Central Europe using transformers and
Sentinel-2 time series
Christopher Schillera,*, Jonathan Ko ¨ ltzowa, Selina Schwarzb, Felix Schieferc,
Fabian Ewald Fassnachta
aInstituteofGeographicalSciences,RemoteSensingandGeoinformatics,FreieUniversita¨tBerlin,Malteserstraße74-100,12249Berlin,Germany
bInstituteofMeteorologyandClimateResearch-AtmosphericEnvironmentalResearch,(IMK-IFU),KarlsruheInstituteofTechnology(KIT),82467Garmisch-
Partenkirchen,Germany
cInstituteofGeographyandGeoecology,KarlsruheInstituteofTechnology,Kaiserstraße12,76131Karlsruhe,Germany
A R T I C L E I N F O A B S T R A C T
EditedbyMarieWeiss Forestsprovideimportantecosystemfunctionssuchascarbonsequestrationandclimateregulation,particularly
incountrieswithhighforestcover.Climatechange-inducedextremeweathereventshaveanegativeimpacton
Keywords: manyforestecosystems.InGermany,forinstance,thedroughtoftheyears2018until2020resultedinsignsof
Monitoring damage in almost 80% of trees. This decline in forest vitality has additionally led to severe bark beetle in-
Sentinel-2
festationsandwidespreadtreemortality,posingsignificantchallengestoforestmanagerstoobtainacomplete
Forestdisturbance
pictureofthestateoftheirforests.Sinceacompletelyground-basedmonitoringofforestconditionisnotfeasible
Deeplearning
duetotheforests’vastextent,remotesensingandparticularlymultispectralsatelliteimagetimeseries(SITS)
Transformer
analysisweresuggestedasefficientalternatives.Transformers,astate-of-the-artDeepLearning(DL)architec-
ture,haveshownpromisingresultsintheclassificationofmultivariateSITSforotherapplications.Here,weuse
TransformersincombinationwithSentinel-2(S2)timeseriesdatatotestiftheycanimproveforestdisturbance
detectioncapabilitiesincomparisontoconventionalmethodsbyautomaticallyextractingrelevantinformation
from background variability throughout the whole time series. To match the large training data needs of
Transformers,weuseatwo-stepapproachincludingpre-trainingandfinetuning.Duringpre-training,weuse
outputsofearlierpresentedSITSapproaches,whileduringfinetuning,weusedetailedreferencedataofknown
disturbancescoveringbetween10and100%ofaSentinel-2pixelasextractedfromaerialimages.Wetestthree
setups:DLbaseusingtenS2bands,DLINDusingtenvegetationindices(VIs),andDL+INDutilisingbothas
modelinput.F1-scoresacrossallofoursixstudysitesrangebetweenapprox.0.65(DL+IND)and0.72(DLbase)
inabinaryclassification(undisturbedvs.disturbed)whenconsideringbothfullandpartialdisturbances.DLbase
outperformstheothersetupsinforestdisturbancedetection,anddetectsdisturbanceextentsassmallas40m2
withinpixelsof100m2size.GiventhebestperformanceofDLbase,handcraftedvegetationindices(VIs)donot
improvethemodel.Ourmodeliscompetitivewithexistingapproachesandslightlyoutperformsmostearlier
reportedresults,eventhoughadirectcomparisonischallenging.Consideringtheoptiontofurtherrefineour
trained model if additional reference data becomes available over time, we conclude that a combination of
TransformersandSentinel-2timeseriescanbedevelopedintoaneffectivetoolforforestdisturbancemonitoring
ofCentralEuropeanforestsatfinespatialgrain.
1. Introduction (Bo¨schetal.,2018;SenfandSeidl,2020;Thometal.,2017).Moreover,
forestsareanimportanteconomicfactor,providingmorethan1million
Forests cover more than 30% of Germany’s (Bo¨sch et al., 2018; jobsandaturnoverofbillionsofEurosinGermany(Holzwarthetal.,
Holzwarthetal.,2023;Holzwarthetal.,2020)andLuxembourg’sland 2020).
surface(Schwarzetal.,2023),providingmanyecosystemservicessuch In the last decades, extreme climatic events such as heat waves,
as carbon sequestration, climate regulation and space for recreation droughtsandstormsnegativelyimpactedthevitalityofGermanforests
* Correspondingauthor.
E-mailaddress:christopher.schiller@fu-berlin.de(C.Schiller).
https://doi.org/10.1016/j.rse.2024.114475
Received23July2024;Receivedinrevisedform23September2024;Accepted14October2024
Available online 24 October 2024
0034-4257/© 2024 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
(Holzwarth et al., 2020). As a result, about 80% of trees in Germany promising tool in remote sensing. Numerous successful applications
have been reported to show signs of damage in 2023 suchasthemappingofstandingdeadwood(Schieferetal.,2023),crop
(BundesministeriumfürErn¨ahrungundLandwirtschaft(BMEL),2023). classification (Yuan and Lin, 2021), wildfire detection (Kong et al.,
Drivenbyclimatechange(IonitaandNagavciuc,2021),thefrequencyof 2018)andforestdisturbanceagentclassification(Duetal.,2023)have
extremeweathereventsisexpectedtoincreaseevenmoreinthefuture been presented. Transformers (Vaswani et al., 2017), a Deep Learning
(García-Herrera et al., 2019; Grillakis, 2019; Ionita and Nagavciuc, architecture that revolutionized Natural Language Processing (NLP)
2021),presumablyleadingtoahigherfrequencyofforestdisturbances (Ahmedetal.,2023),e.g.inNeuralMachineTranslationtasks(Vaswani
(Br´edaetal.,2006;GazolandCamarero,2022;Holzwarthetal.,2020; etal.,2017),havebeenadaptedtocopewithavarietyoftimeseriesdata
Seidletal.,2017;SenfandSeidl,2021).Climate-inducedtreestressand (Ahmed et al., 2023; Yuan and Lin, 2021) including SITS. The main
increased deadwood volumes as well as generally increased tempera- innovationofTransformersistheself-attentionalgorithm,whichenables
tures also benefit European bark beetles (Ips typographus L. and Pity- the model to learn (the strength of) both long- and short-term de-
ogenes chalcographus L.) which have infested wide parts of forests in pendenciesbetweendifferentobservations.
Germany and central Europe over the last years (Latifi et al., 2014; Transformers exhibit at least three potential advantages over the
Nethereretal.,2019;Pataccaetal.,2022;Senfetal.,2017). aforementionedapproachesforforestdisturbancedetectionusingSITS:
A timely and area-wide monitoring of forest condition is urgently (1)Transformerscanconsidersingledecisiveobservationsatanyposi-
needed, for example to prevent bark beetles from spreading by con- tion withinthe time seriesexplicitly andcapturetheir links tosubse-
ductingsanitationfellings(Doboretal.,2020;Kautzetal.,2023),orto quent events. This could be advantageous with respect to events that
assess drought-induced forest dieback and plan preventive measures. triggertreemortalityafteracertaintimelag(Bigleretal.,2007)suchas
For Germany’s large forest areas of more than 11 million ha forestdiebackoccurringmorethanayearafteradroughtatcertainsites
(BundesministeriumfürErn¨ahrungundLandwirtschaft(BMEL),2023), (Haberstroh et al., 2022). Even an increased photosynthetic activity
anefficientandtimelyarea-widemonitoringofforestconditiononthe observedatthebeginningofadrought(causedbyalotofphotosynthetic
groundisimpossible(Holzwarthetal.,2020).Hence,remotesensing- activeradiationhours)couldbeasubtlemarkerofadisturbanceevent
based approaches have been discussed frequently over the last years. following much later (Reinermann et al., 2019). Related to that,
Remotesensinghasshownpotentialforforestmonitoringinnumerous Transformers seem to offer an improved ability to detect small and
earlierstudies(Abdullahetal.,2019;Grabskaetal.,2020;Latifietal., gradualdisturbancesignalswhicharehardtodisentanglefromspectral
2014;SenfandSeidl,2020;Thonfeldetal.,2022).Manyofthesestudies variationcausedbynaturalprocesses(Coopsetal.,2020;Rodmanetal.,
showthatparticularlythemultispectralSentinel-2(S2)satellitesystem 2021;Yeetal.,2021).RecentstudiessuggestthatTransformersmaybe
bearsgreatpotentialduetoitshighspatialresolutionofupto10mand able to capture such subtle disturbance signals in SITS (Perbet et al.,
its short revisit time of approx. 5 days in Europe. The multispectral 2024).
sensoronboardofS2capturesspectraldatainthevisibletoshortwave (2)Manyestablishedmethodsonlyoperateonunivariatetimeseries.
infraredrange,whichenablesittocaptureinformationrelatedtoforest Theyeitherusesatellitebandsorvegetationindices(VIs)thataresen-
condition(Dutrieuxetal.,2021a;Grabskaetal., 2020;Mouretetal., sitivetodisturbance(e.g.Dutrieuxetal.,2021b;Verbesseltetal.,2010),
2024; Verbesselt et al., 2010; Zhu and Woodcock, 2014) and make it orthealgorithmisappliedtomultipleVIs/bandsseparately,followedby
suitable as input for satellite image time series (SITS)-based forest a cumulative sum of detected anomalies to decide about the final
disturbancemonitoringapproaches. disturbancedetection(e.gPuhmetal.,2020).Additionally,someofthe
The analysis of SITS allows for the detection of changes in forest establishedmethodsdemandaveragingorinterpolationoftheSITSas
coverandstateovertime.MajorchallengesofSITSapproachesinclude theyrequireregular(e.g.5or7days)timeseriesasinput(Verbesselt
the creation of homogeneous time series and extracting disturbance- etal.,2010).Transformers(oradaptationsthereof),ontheotherhand,
related changes from the diverse range of natural fluctuations in the cantakeasinputnon-interpolated,multivariatetimeseries(Yuanand
spectralcharacteristicsoftemperateforests.Thelatterarecaused,for Lin, 2021; Zhang et al., 2024). This is favorable, since interpolation
instance, by the complex phenology of temperate forests with inter- leadstoinformationloss(Zhangetal.,2024),andusingunivariatetime
annual variations (Puhm et al., 2020), varied species compositions seriesasinputdoesnotexploitalloftheavailableinformation.
andgradientsinstructuralcomplexity(e.g.differentstandages,multi- (3)Someoftheestablishedmethodsneedparametertuningtowork
or single-layered stands, canopy gaps, various topographic situations fordifferentregionsandtimeframes(Pasquarellaetal.,2022).Inideal
affectingsun-sensorgeometries). case,aDeepLearningmodeltrainedonaverylargeamountofdatahas
ThesechallengeshavebeenaddressedinatleastthreeexistingSITS beenexposedtomanydisturbedandundisturbedspectraltimeseries,
analysis approaches: near real-time (NRT) monitoring, temporal seg- whicharerepresentativeforthevastmajorityoftheexistingvariability
mentationandtimeseriesclassification.Nearreal-timemonitoringal- inspectralpropertiesofdisturbancesofforests.Ifthisisthecase,itcan
gorithmsutiliseatrainingperiodofpresumablyundisturbedforestto be assumed that Deep Learning models can be readily applied across
modelabaselineanddetectdeviationsfromforecastsofthisbaselinein widerareaswithoutfurthertuning.
newobservations.ExamplesforNRTmonitoringalgorithmsareBFAST Giventhesepotentialadvantages,Transformershavebeensuccess-
Monitor(Verbesselt etal., 2012),CCDC/COLD(Zhu etal., 2020;Zhu fullyusedinclassificationofSITSforcrop(YuanandLin,2021)andland
and Woodcock, 2014) and FORDEAD (Dutrieux et al., 2021b). The coverclassification(Zhangetal.,2024)aswellastreespeciesmapping
secondapproachisreferredtoastemporalsegmentationapproachand (Muetal.,2024).InthecontextofDeepLearning-basedforestdistur-
includes, for instance, BFAST (Verbesselt et al., 2010). Temporal seg- bance detection, Schiefer et al. (2023) use Long Short Term Memory
mentation approaches decompose the SITS signal into a seasonal Networks(LSTMs)toestimatethefractionofstandingdeadwoodgiven
component,atrendcomponentandresidualstosubsequentlyidentify S2pixeltimeseriesinGermany.Wittichetal.(2022)usesingleSentinel-
breakpoints in the spectral time series. Depending on the strength of 2 scenes to estimate the time of upcoming disturbances using a Con-
signal changes at the breakpoints and the direction of the change, a volutionalNeuralNetworkatastudysiteinGermany.However,only
forest disturbance is then assumed. Features extracted from temporal fewstudiesusingTransformersforSITShavebeenpublished,yet.Du
segmentationapproachescanalsobeusedasinputtotimeseriesclas- et al. (2023) and Mullissa et al. (2023) detect stand-replacing distur-
sificationmethods.Thisapproachisusuallybasedonmachinelearning bancesusingLandsatandSentinel-1/2,respectively.Perbetetal.(2024)
andcanalsobeappliedonthetimeseriesitselfinsteadofthefeatures successfullydetectstand-replacingaswellaspartialdisturbancesusing
engineered by temporal segmentation (Du et al., 2023; Perbet et al., annualcompositesofSITSoftheLandsatsatellites.Tothebestofour
2024). knowledge,however,thereisnostudysofarthatusesTransformerson
DeepLearning(DL),asub-classofmachinelearning,hasevolvedasa SITS of raw Sentinel-2 data without temporal compositing to detect
2

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
forestdisturbanceintemperateforests. Learning(DL)modelsfortimeseriesclassification(Ahmedetal.,2023;
To fill this gap, we test if Transformers are capable of extracting Du et al., 2023; Yuan and Lin,2021). We implement themodel for a
relevantinformationfromcomplexanddensemulti-yeartimeseriesof binary classification task (undisturbed vs. disturbed forest). In the
S2observationstoidentifyforestdisturbancesacrossawideandvaried following,wedescribeindetailthestepstoprocessinputdata(Sections
geographicareacoveringGermanyandLuxembourg.Weimplementthe 2.1and2.2),trainthemodels(Sections2.3and2.4)andcomparethe
studyasabinaryclassificationtask(undisturbedvs.disturbedforest). results(Section2.5),assummarizedinFig.1.
Wetrainonstand-replacingaswellaspartialdisturbancesofmultiple
disturbance agents (incl. logging) in order to enable the detection of 2.1. Sentinel-2datapreprocessing
disturbancesatsub-pixelsizeaswell.Wehypothesizethatthisapproach
mightempowerthemodeltodetectearlystagesofgradualdisturbances Sentinel-2(S2)dataforGermanyandLuxembourgwereprocessed
such as bark beetle infestations. Since VIs have been widely and suc- usingtheFrameworkforOperationalRadiometricCorrectionforEnvi-
cessfully utilised in spaceborne forest disturbance detection tasks ronmental Monitoring (FORCE) (Frantz, 2019), including co-
(Abdullahetal.,2019;Bandyopadhyayetal.,2017;Cohenetal.,2010; registration,atmosphericandtopographiccorrectionandcloudmask-
MandlandLang,2023;Mouretetal.,2024),weexaminethreesetups:1) ing,amongothers.Intheresultingdatacube,S2tileswithacloudcover
DLbaseusingonlytheten10to20mS2bands,2)DL+INDusingboth
ofmorethan70%asstatedinthemetadataoftherespectiveS2sceneor
thetenS2bandsandtencommonlyusedVIs,3)DLINDusingonlythe 90%asdeterminedby theFORCEcloud maskingalgorithmwere dis-
tenVIs.Inshort,thegoalofthisstudyisprovidinganadvancedforest carded. The level 2 datacube of bottom of atmosphere (BOA) re-
disturbancemonitoringtoolcapableofidentifyingspatiallysmallforest flectancesforGermanywasreadilyavailablefromtheEO-Labplatform
disturbancesapplicabletoallforestpixelsinGermanyandLuxembourg (EO-Lab, 2023), while the FORCEdatacube for Luxembourg was pro-
at any time of the year using state-of-the-art transformer models to cessed on the high-performance cluster of Free University Berlin
supportforestmanagement.Suchatoolhasbeencalledforbynumerous (CURTA)(Bennettetal.,2020)usingallavailableS2dataandthesame
stakeholdersintheforestsectorinthelastyears(Holzwarthetal.,2023; FORCE parameters as the aforementioned datacube. We used the
Holzwarthetal.,2020). following ten spectral bands of S2, which were upsampled to 10 m
Thisresultsinthreeresearchquestions: spatialresolutionusingtheImproPhealgorithmimplementedinFORCE:
Red (RED), Green (GRN), Blue (BLU), Red Edge 1 (RE1), Red Edge 2
• To what degree can Transformers accurately detect forest distur- (RE2), Red Edge 3 (RE3), Near Infrared (NIR), Broad Near Infrared
banceonformerlyunseenS2timeseries? (BNR),ShortwaveInfrared1and2(SWIR1,SWIR2).Additionally,we
• Whatisthesmallestdisturbanceextentthatcanbedetectedbythe computed the ten following vegetation and disturbance indices (VI’s)
proposedmethod? fromtheaforementionedtenspectralbands,whicharecommonlyused
• Do Transformers need vegetation/disturbance indices for accurate for disturbance analyses: Continuum Removal Shortwave Infrared
predictions? (CRSWIR) (Dutrieux et al., 2021a; Mouret et al., 2024), Normalized
Burn Ratio (NBR) (García and Caselles,1991), Tasselled-Cap Wetness
2. Methods (TCW) (Crist and Cicone, 1984), Tasselled-Cap Disturbance (TCD)
(Healeyetal.,2005),NormalizedDifferenceVegetationIndex(NDVI)
We use Sentinel-2 multispectral time series and forest disturbance (Tucker, 1979), Normalized Difference Water Index (NDWI) (Gao,
information derived from published (mostly satellite-based) datasets 1996),NormalizedDifferenceMoistureIndex(NDMI)(Gao,1996),Leaf
(pre-trainingstep)andhigh-resolutionaerialimagery(finetuningstep) AreaIndex(LAI)(Boeghetal.,2002),MoistureStressIndex(MSI)(Rock,
to train a transformer model, a state-of-the-art architecture of Deep 1985) and Normalized Difference Red Edge (NDRE) (Gitelson and
Fig.1. Workflowofthestudy.AfterSentinel-2timeseriespreprocessing(left),tenvegetationanddisturbanceindiceswerecomputed(left).Forthethreesetups,pre-
trainingwasconductedaftersamplinglabelsfrompublishedremotesensing-baseddisturbancedatasetsandCopernicusLandMonitoringService(CLMS;topcenter
andtopright).Thepre-trainedDeepLearningmodelswerethenfinetunedusinglabelsfromsixvisuallyinterpretedstudysitesandauxiliarydata(bottomcenterand
right).Aspatialblockcross-validationonAOIlevelwasconductedasvalidation(bottomright).
3

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Merzlyak,1998)(seeSupplementaryTable1fordetails).Forthepre- Thesesampleswereassignedtothe‘undisturbed’class.SincetheSenf
training dataset, we computed the time series from the described S2 methodrelies onmedoid compositesofthegrowingseason endingin
datacubeasthearea-weightedmeanofpolygonsdescribedinSection September30thofeachyear,wedeterminedtheenddateofthecorre-
2.2.1withendandstartdatesbeingselectedaccordingtothedetection spondingtimeserieslabelledwithSenfdataasOctobre1sttomakesure
date of each disturbance (for details see below). Regarding the fine- it contains the disturbance. For Thonfeld, we used the 1st day of the
tuningdataset,wecomputedthedisturbedarea(dieback+logging)for month after the disturbance detection. Next, we randomly assigned a
eachS2pixel,usingeachpixel’sfractionalcoverofdisturbanceaslabel datebetweentheaforementionedenddateandthedateupto6months
(seeSection2.2.2).WeextractedtheS2timeseriesforeachpixelindi- latertoensurethat1)thefulltimeseriesactuallycontainsthereference
viduallyandtheenddateofthetimeserieswasselectedtomatchthe disturbancetime(possibleuncertaintiesintimeofdetectionanddueto
acquisition date of the DOPs from which the detailed reference data temporalresolutionofdisturbancedatasets)and2)tosupportgeneral-
werecollected. izationofthemodelbypreventingitfromlearningartefacts.Potential
artefactsoccur,forinstance,iftimeserieslabelledasdisturbedalways
2.2. Labelsandvalidationdatasets endinSeptember.Inthiscase,themodelmightlearnthatanenddatein
September qualifies for a disturbed prediction even in the absence of
2.2.1. Pre-training disturbance(overfittingtoartefacts).Moreover,themodelismeantto
Forpre-trainingthetransformermodels,weacquiredthreespatially enableforestdisturbancedetectionatanydateinayear,meaningthatit
explicit datasets containing forest disturbances andtheir approximate needstobetrainedontimeseriesendingonanarbitrarydate.Thestart
time of occurrence in Germany. In the following, we refer to these dateofeachtimeserieswasfixedfouryearsbeforethechosenenddate.
datasetsasSenf(SenfandSeidl,2020),Thonfeld(Thonfeldetal.,2022) Hence, the resulting dataset contained time series of four years, the
and Forwind (Forzieri et al., 2020) (see Table 1 for details). Forwind reference disturbance detection occurring approximately, but not
containswindthrowdisturbancesfollowingmajorstorms(Forzierietal., exactlyattheendofthetimeseriesandcontainingenddatesbetween
2020)withexactdates,whileThonfeldmainlycontainsstand-replacing
July1st,2019andMay1st,2021(lastdateofdetecteddisturbancesin
disturbancesinandafterthedroughtyearsof2018–2020inmonthly Thonfeld). Accordingly, the Undisturbed dataset was assigned an end
temporal resolution (Thonfeld et al., 2022). Senf contains forest
dateofthetimeseriesbetweenJuly1st,2019,andMay1st,2021.Hence,
disturbanceareasoriginatingfromavarietyofforestdisturbanceagents weassumeaforestpixeloftheundisturbedclasstobeundisturbed(orat
(Senf and Seidl, 2020), among them harvest, bark beetle, drought, least resistant) during this period, meaning that omissions in the
windthrowandfire,withayearlytemporalresolution.Additionally,it disturbance datasets have led to time series labelled as undisturbed
provides the disturbance severity of detected disturbance events as a despiteitsactualdisturbanceinourpre-trainingdata.Italsoimpliesthat
percentageoflostcanopycoverwithina30mpixel.Inthedisturbance weexpectthatapixeldeterminedasforestbyCLMSin2018hasbeen
datasets,wefilteredfordisturbanceeventsthatoccurredafterJuly2019 forestbackinJuly2015already.AccordingtoSenfandSeidl(2020)’s
toensurethatS2timeserieswithaminimumdurationof4yearscould validation,theirdatasetexhibitsrathersmallcommissionerrors(14.6
besampled(S2dataisavailablefromJuly2015).Weavoidedspatial ± 1.8%). Still, we tried to prevent the models from adopting these
autocorrelationbyremovingForwinddisturbancesfromThonfeldand mistakes of the pre-training datasets by removing disturbances below
Senf,andThonfelddisturbancesfromSenf,applyingabufferof30mto 50% severity. This also guarantees a clear distinction between undis-
eachdisturbanceevent.WegaveprioritytoForwindandThonfeld,since turbedanddisturbedclassduringpre-training.Thedatafromthesefour
theformerismostlybasedonaerialimagery,andthelatterisderived datasets(Forwind,Thonfeld,SenfandUndisturbed)coverthewholeof
fromS2asopposedtoSenf’sLandsatapproach,meaningthatForwind Germany(SupplementaryFig.1)andwereusedforpre-trainingtheDL
and Thonfeld are spatially higher resolved and able to reflect forest models.
disturbances at smaller extents. Additionally, both commission and
omissionerrorsaresmallerinThonfeldaccordingtotheirownvalida- 2.2.2. Finetuning
tion(SenfandSeidl,2020;Thonfeldetal.,2022).Thesamplesderived For the finetuning step, we used data from one forested area for
fromthesethreedatasetswereassignedtothedisturbedclass. Luxembourg(LUX)(fromSchwarzetal.,2023)andforfivefederalstates
WethenremovedalltheforestdisturbanceareasofForwind,Senf of Germany with significant forest cover and openly available digital
and Thonfeld including a buffer of 30 m from a forest mask of 2018 orthophotos(DOPs)tovisuallydelineateforestdisturbancesourselves.
acquired from European Union’s Copernicus Land Monitoring Service The five federal states included Brandenburg (BB), Saxony (SAX),
(CLMS) and randomly sampled S2 forest pixels from the remaining Thuringia (THU), Rhineland-Palatinate (RLP) and Northrhine-
forestpatches.Wemadesuretohaveabufferofatleast30minbetween Westphalia (NRW). We made sure to cover areas representative for a
twosampledpixelstoavoidspatialautocorrelationintrainingcaused, variety of environmental and forest characteristics such as open (BB)
forinstance,byanindividualtreespanningovermorethanonesample. and dense forest stands (RLP, LUX, NRW), steep slopes (RLP, NRW),
heavily (NRW),medium (THU, RLP)and moderatelydisturbed (LUX)
forest.Thesesixareasofinterest(AOIs)werecomplementedbyforest
Table1
Table characterising the four datasets Senf (Senf and Seidl, 2020), Thonfeld disturbancedatafrom(Schieferetal.,2023)(inthefollowing:Schiefer)
(Thonfeldetal.,2022),Forwind(Forzierietal.,2020)andUndisturbedinthe originating from (mainly southwestern) Germany, from the FNEWS
pretrainingstepofthestudy.Ntraining:amountoftrainingsamplesdrawnforpre- projectinthestatesofBaden-Württemberg,LowerSaxonyandSaxony
training. (Langner et al., 2023), and (Schwarz et al., 2023) (in the following:
Dataset Disturbanceagents Temporal Sensor Ntraining Schwarz)inLuxembourg(Fig.2).InthesixAOIswherewedelineated
resolutionof the forest disturbances ourselves, we considered all Sentinel-2 pixels
disturbance containingforest(afterremovalofnaturalforestopenings,arableland,
detection urbanareas,gravelpits,etc.byvisualinterpretation)excludinga15m
Senf harvest,biotic/ year Landsat4/ 41,832 bufferofftheforestedgestopreventedgeeffectsforouranalyses.We
abioticandothers 5/7/8 manuallydelineatedforestdisturbanceareasincl.loggingandstanding
mainlyclear-cuts
Sentinel-2, deadwood using the very high resolution aerial imagery from image
Thonfeld afterdrought/bark month 87,665
beetledamage Landsat8 flightsfromLuxembourgandGermany(between10and40cmspatial
aerial resolution,seeTable2)and,incaseofSchiefer,uncrewedaerialvehicles
Forwind windthrow day 377
imagery (UAV).WecomparedtherespectiveDOPwiththeprecedingDOPsof
Undisturbed – – Sentinel-2 927,005
eachAOItoenableadistinctionbetweenolderloggingareasandnatural
4

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Fig.2. StudysiteforfinetuningandvalidationinGermanyandLuxembourg.BluemarkersrepresentthesixAOIsofthestudy,whileblackrectanglesarethe
boundingboxesoftheregionsinwhichsomeauxiliarydatafromSchieferetal.(2023),FNEWS(Langneretal.,2023)andSchwarzetal.(2023)wereavailable.
Coordinatereferencesystem:EPSG:3035.(Forinterpretationofthereferencestocolourinthisfigurelegend,thereaderisreferredtothewebversionofthisarticle.)
Table2
InformationonfinetuningdatasetsfromBrandenburg(BB),Saxony(SAX),Thuringia(THU),Northrhine-Westphalia(NRW),Rhineland-Palatinate(RLP),Luxembourg
(LUX;Schwarzetal.,2023),Schiefer(Schieferetal.,2023),Schwarz((Schwarzetal.,2023))andFNEWS(Langneretal.,2023).DOP:digitalorthophoto,number
indicatingspatialresolution;RGB:red-green-blue;RGBI:reg-green-blue-infrared;extent:referstospatialextentofstudiedscene(onlyprovidedforthesixAOIs);UAV:
uncrewedaerialvehicle;N:numberofsamplesusedinvalidation(Schiefer,SchwarzandFNEWS:onlyusedintrainingphase,numberapproximateduetomultiple
trainingrunswithrandomsampling).DOPsaresubjecttocourtesyofGeoBasis(licence:dl-de/by-2-0),open.NRW(dl-zero-de/2.0),LandesamtfürVermessungund
GeobasisinformationRheinland-Pfalz(dl-de/by-2-0),LandesamtfürGeobasisinformationSachsen(GeoSN)(dl-de/by-2-0),LandesamtfürBodenmanagementund
GeoinformationThüringen(dl-de/by-2-0),AdministrationduCadastreetdelaTopographie(ACT),Grand-DuchyofLuxembourg(CC0).
Dataset Product Acquisitiondate Location Extent N Nbroeadleaved; Source
Nconiferous
BB DOP20 2022–06-18(2019-04-19,2016-04- Brandenburg(GER) 2*2km 29,879 3779;26,100 ownwork
RGBI 21)
SAX DOP20 2022–06-03(2020-07-30,2017-08- Saxony(GER) 2*2km 32,940 3865;29,075 ownwork
RGBI 05)
THU DOP20 2022–06-19/15(2021-04-28,2020- Thuringia(GER) 2*2km 26,880 5599;21,281 ownwork
RGBI 03-15,2019-04-17,2018-04-07,
2016-05-06)
NRW DOP10 2021-06-14(2018-04-07,2015-06- Northrhine-Westphalia(GER) 2*2km 19,995 13,989;6006 ownwork
RGBI 05)
RLP DOP40 2021-09-06/07(2019-07-24,2018- Rhineland-Palatinate(GER) 4*4km 49,503 45,752;3751 ownwork
RGB 07-02,2015-06-05)
LUX DOP10 2019-08-22(2018-07-02,2017-06- Luxembourg 1.75*1.3 19,683 17,731;1952 Schwarzetal.,
RGBI 14,summer2016) km 2023;ownwork
Schiefer DOPRGB 2019/2021–09/10 BlackForest(GER),DresdenHeath(GER), – ~1819 ~560;~1259 Schieferetal.,
(UAV) Karlsruhe-Bretten(GER),HainichNational 2023
Park(GER)
Schwarz DOP10 allDOPs2016–2020 Luxembourg – ~4884;~988 Schwarzetal.,
RGBI ~5872 2023
FNEWS DOP differentdates Baden-Württemberg,LowerSaxony,Saxony – ~ ~188,104;~ Langneretal.,
502,789 314,685 2023
forestopenings,sincethelatterareneitherundisturbedforestnorforest disturbancecoverdistributionandnumberofsamplesdidnotallowfora
disturbanceand,thus,hadtobeexcludedfromanalyses.Allapparent multi-classapproach.We,however,madeuseoftheinformationabout
lossofcanopycoverbetweentheDOPswithoutanysignofdieback(e.g. thetwodisturbancecategoriesduringthevalidationstep.
standingdeadwood)waslabelledaslogging.Whenindoubtiftheforest
disturbance happened within a maximum of 3.5 years preceding the
DOPofinterest,weexcludedthesepixelsfromanalysis.Forestdistur- 2.3. Transformermodelandsetups
bancelabelswerethenacquiredbycomputingtheareapercentageof
thedelineatedforestdisturbancesforeachS2pixelcoveredbyforest. DeepLearning(DL)modelsapplytransformationstotheinputdata
Note that although we distinguished between logging and dieback in (here:S2timeseries)inordertoproduceanoutput(here:binaryclass
visualinterpretationoftheDOPs,wecombinedthesetwodisturbance predictions)thatisasclosetothelabels(here:undisturbedvs.disturbed
categoriesintoasingle‘disturbed’classduringclassification,sincetheir pixels)aspossible.Thesetransformationsarestackeduponeachotheras
so-called layers. The difference between predictions and labels
5

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
(referencedata),whichiscalledloss,isdescribedbyalossfunction(here: validationdatasetisnotusedforvalidationofthemodel,butforvali-
binarycross-entropyloss).TheStochasticGradientDescent(SGD)algo- dationoftheprogressofthemodeltraining.Validationofthemodelis
rithmisthenappliedtocomputethegradientofthelossfunction.Af- doneusingthetestdataset.Thelossandaccuracywerecomputedonthe
terwards,theweights,whicharetheparametersofthelayersdefiningthe validationdataafterthecompletesetoftrainingbatcheswasfedtothe
data transformations, are adjusted such that the loss approaches the model(whichiscalledanepoch).Afterwards,thetrainingsampleswere
minimumofthelossfunction.Thelearningratedetermineshowmuch shuffledandinputtothemodelinthenextepoch.Thiswasrepeated
theweightsarechangedinonestep,i.e.afteronebatchofdatahasbeen untilastopcriterionwasreached(seebelow).
inputtothemodel. FortheDLbasesetup,weusedthetenS2bandswith10and20m
Transformers, a state-of-the-art DL model architecture originating spatialresolution,namelyBLU,GRN,RED,RE1,RE2,RE3,BNR,NIR,
from Natural Language Processing (NLP; Vaswani et al., 2017), are SWIR1andSWIR2.SinceVIsarewidelyusedinremotesensingtodetect
becomingincreasinglypopularinpredictivetimeseriesanalysistasks changesinvegetation(e.g.(Bandyopadhyayetal.,2017;Cohenetal.,
(Ahmed et al., 2023) and have been adapted to specifically suit the 2010; Grabska et al., 2020; Kennedy et al., 2010; Mandl and Lang,
challengesaccompanyingsatelliteimagetimeseries(SITS;e.g.irregular 2023)),wetesttwomoresetups,takingasinputonlythetenVIs(DL
time series) as well (Yuan and Lin, 2021). The main innovation of IND)orboththetenVIsandthetenS2bands(DL+IND).
Transformersaretheself-attentionlayers(alsocalledself-attentionheads),
within which attention scores are computed. These attention scores 2.4. DeepLearningtrainingprocedure
inform the model which and to what extent observations of the time
series(inNLP:wordsofasequence)arelinked(Vaswanietal.,2017). ThetrainingofDLmodelscanbeconductedinmultiplesteps.Here,
Self-attentionlayerscanberuninparalleltolearndifferentrepresen- weconductapre-trainingonalargeamountofmediumqualitydata(pre-
tations(Vaswanietal.,2017).Intheencoder,self-attentionheadsare trainingdatasets),followedbyafinetuningonamediumamountofhigh
followedbyadenselayerthatcanbefoundinanyDLmodelcontaining qualitydata(finetuningdatasets).Thepre-trainingdatasetisconsidered
weightstotransformtheinputoftheprecedingself-attentionlayers.The less accurate, as the reflectance values acquired from it are area-
self-attention layers and succeeding dense layers together form the weighted means of the pixels using coverage fractions of disturbance
encoder.Encoderblockscanbestackedtoallowthemodeltolearnfrom polygons (polygon-based approach), while we use pixel-based distur-
differentlevelsofabstractionofthetimeseries(e.g.long-termperiod- bancelabelsandnoaveragingofreflectancesinfinetuning.Addition-
icityvs.short-termevents)(Jawaharetal.,2019;YuanandLin,2021). ally,mostofthepre-trainingdatasetsaresatellite-deriveditselfandthus
Thesucceedingencoderblockgetsasinputtheoutputofthepreceding containerrors.Theideaofthistwo-stepapproachisthatthemodelgets
encoderblock,i.e.theweightsofthedenselayerfollowingeachself- ageneralnotionofthetasktosolveinpre-training,andimprovesonthat
attentionblock. infinetuning.Thus,thegeneraldependenceonBigDataismetandat
Theself-attentionalgorithmdoesnotknowtheorderoftheobser- the same time, data with higher quality is used for training the best
vations,however.Therefore,aPositionalEncoding(PE)isaddedtothe modelforthetask.Weaddedthedayoftheyear(DOY)ofeachobser-
inputdata,whichinforms themodel aboutthenotionoforder(here: vation as additional input for the Positional Encoding. The DOY
time)(Ahmedetal.,2023;Vaswanietal.,2017). increasedwitheveryyear,i.e.inthesecond yearofeachtimeseries,
Here, we deploy SITS-BERT (Yuan and Lin, 2021), which is a DOYswerecomputedbyadding365,andsoon.Thiswasdonetomake
Transformer architecture specifically designed to approach the chal- surethatthemodeldoesnotconsidertwoobservationswiththesame
lengesusuallyfacedinsatelliteimagetimeseries(SITS),e.g.irregular DOY from different years as the same time step, since the order and
timeseriesduetocloud-maskedobservations.Otherthanintheoriginal timelinessoftheobservationsisrelevantforclassification.
Transformer(Vaswanietal.,2017),thePEsarenotsummedtotheinput We used a single classification layer with one output unit for this
data, but concatenated (i.e., processed separately). This prevents the binaryclassificationtask,andBinaryCross-Entropylossaslossfunction.
model from confusing the representations of time with the actual ob- The learning rate was set to 0.0001 in pre-training and 0.00001 in
servations(YuanandLin,2021).Infact,inSITSotherthaninNLP,there finetuning.Thelearningratewasonemagnitudesmallerinfinetuningin
isaveryimportantseasonalpatterninthedataset,sothedatesshouldbe order not to erase the learned representations from pre-training.
modelleddistinctly(YuanandLin,2021).ThisalsoimpliesthatSITS- Trainingwasconductedwithabatchsizeof128.Theembeddingsize
BERT does not need equidistant time steps in the sequences (i.e., no was128,where64unitswerereservedfortheSITSembeddings,and
gapfilling,interpolationoraveragingofmultipleobservations)(Yuan another 64 units modelled the observation dates. We utilised three
andLin,2021).Thiswasconsideredimportantsinceinterpolationand encoder blocks with eight attention heads each. The complete model
averagingalwaysinducesadditionalnoiseintothesequence,deviating contained594,753trainableweights.Foralltrainingruns,weutilised
fromrealobservations(Zhangetal.,2024). early stopping with a patience of 10, meaning that training was con-
Furthermore,embeddinglayersprecedetheencoderblocks.InNLP, ducted until the validation loss did not improve for ten consecutive
they are used to encode words into integer values and reduce the epochs.Thebest-performingmodelwasdeterminedbythebestaccuracy
dimensionality of the vocabulary, since DL models can only process onthevalidationdataset.
numbers,notwords.Intimeseriesanalysis,theyserveadifferentpur- The forest types in both pre-training and finetuning dataset were
pose: they provide higher-dimensional representations of the input strongly skewed towards coniferous trees in the disturbed class and
features(S2bandsandVIs).Insimpleterms,thiscanbeinterpretedas broadleaved trees inthe undisturbed class.Inpre-training, we under-
computing its own VIs from combinations of the input features in a sampledthemajorityforesttypeinboththeundisturbedanddisturbed
dynamical(andlessrigid)way.Forinstance,theembeddinglayermight classtopreventthemodelfromadoptingthisbias.Sincetheresulting
combinetheREDandNIRbandstomodelthedifferencebetweenthose dataset contained many more samples in the undisturbed than in the
bands. disturbedclass,weusedclassweightsinordertopreventthemodelfrom
Ontopoftheencoderblocks,aclassifierisstacked,whichconsistsof majority votes on the undisturbed class. The class weight was deter-
adenselayerandprovidesasingleoutputforeachinputtimeseries. mined by the ratio of amount of undisturbed to amount of disturbed
This represents the confidence score for the disturbed class (range: samplesdivided by3. Infinetuning, thedata distributionallowed for
[0,1]),whichcanthenbetranslatedintobinaryclassesbyathreshold applying a different sampling strategy in the training phase. In the
(here:0.5).InDLtraining,thedataisusuallysplitintotraining,vali- disturbedclass,weoversampledtheminorityforesttypebyafactorof2,
dationandtestdatasets.Themodelweightsarealteredinsteps,which followedby undersamplingthesamplesofthemajorityforest typeto
consistofbatchesoftrainingdata,whilethevalidationdataisusedto yieldthesameamountofsamplesasthedoubledminorityclass.Inthe
monitorthetrainingprogress.NotethatinDeepLearning,theso-called undisturbedclass,weundersampledthesamplesofthemajorityforest
6

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
type to the equal amount of data of the minority forest type. The annual variations (Puhm et al., 2020)). The satellite signal jitter was
resulting dataset contained the same amount of deciduous and conif- meant to account for the noise inherent to satellite data due to topo-
erousforests’pixelsinbothclasses.Resamplingtoovercomechallenges graphic and atmospheric effects, undetected clouds and cloud/tree
associated with class imbalance has shown to be effective before shadows,etc.(YuanandLin,2021).
(Wittichetal.,2022).Applyingclassweightsasinthepre-trainingstep Windowslicingconsistedofdroppingthebeginningofthesequence
was not necessary in finetuning, since the resulting dataset was less toyieldatimeseriesbetweentwoandfouryears(pre-training),or3.5
imbalanced.Thissamplingstrategyforpre-trainingandfinetuningwas and 4 years (finetuning) randomly. This guaranteed a minimum time
confirmedbythebestperformanceinpreliminarymodelruns. serieslengthof2(pretraining)and3.5(finetuning)yearswhilemaking
In finetuning, we discarded all samples with disturbance labels surethatthedisturbanceeventisstillpartofthetimeseries(temporal
greaterthan0%andsmallerthan10%inordertomakeadistinction resolutionofaslowasapprox.3yearsinDOPacquisitiondatesusedfor
between undisturbed and disturbed time series during model training labelling).
and hence enable it to differentiate between the two classes. The
thresholdof10%infinetuningdiffersfromthethresholdof50%inpre- 2.5. Validation
training,sincethelabelsofthelattercontaincommissionerrors,which
are more likely in case of low disturbance severities. In finetuning, We performed a number of analyses to validate and compare the
however, the labels are sufficiently accurate to allow for a lower models with respect to performance and plausibility of the detected
threshold.Athresholdwasnecessary,sincewecannotexpectthemodel disturbancepatterns,accuracy,minimumdetectabledamageextentand
tobeabletodifferentiatebetween,forinstance,0%(healthy)and1% generalisability(i.e.,predictiveperformanceacrossforesttypesbroad-
(disturbedclass)disturbancefraction.Takingalldisturbancelabelsas leavedandconiferous).
trainingdatawouldhaveledtoaninsufficientseparabilityofthetwo Firstly,wemappedtheconfidenceofthemodelswithrespecttothe
classes. disturbedclass(i.e.,beforebinarization)toinvestigateifdetectedpat-
Inthevalidationphase(i.e.thetestinginthefinetuningstep),wedid ternsmatchwiththedamageobservationsbasedonaerialimageryin
notdiscardverylowdisturbancepixels(smallerthan10%)fromanalysis thesixAOIs.Weprovideerrormatricesandperformancemetricsforthe
toavoidanoverestimationofmodelperformance(seealsoSection4.1). three setups. Afterwards, we analysed the capability of the models to
Forpre-training,thedatasetcomprisedofForwind,Thonfeld,Senf detectsmalldisturbanceareasbystratifyingthefractionofdisturbance
and Undisturbed dataset (see Section 2.2) was split into training and (diebackandloggingcombined)perpixelinto10m2categories,e.g.10
validationdatasetsrandomlybysampling20%ofthesamplesasvali- to20m2,20to30m2,andsoon.Notethatincaseofour100m2S2
dationand80%astrainingdataset.Thevalidationdatasetwasusedto pixels, m2 equals percentage. Only the 0 m2 damage category was
monitortheincreaseofmodelaccuracyduringeachtrainingepoch.The consideredundisturbedforest.Weshowthemodels’Producer’sAccu-
testdatawasusedtoverifythemodel’sabilitytoreproducethelabels
racies for each of these strata. Afterwards, we further stratified these
fromthepre-trainingdatasetsaftercompletingthetrainingprocedure resultsbyforesttype,i.e.broadleavedandconiferousforest.Theforest
(forresultsseeSupplementaryTable2). typeinformationwasextractedfromEuropeanUnion’sCopernicusLand
Inthefinetuningstep,weconductedaspatialblockcross-validation MonitoringService(CLMS).
onAOIlevelwiththreerepetitions.Hence,weusedeachofthesixAOIs PreprocessingofalldatasetsandretrievalofS2timeseriesfromthe
asspatialhold-outonce,performingthetrainingonthetimeseriesofthe FORCEdatacubewasconductedinR(RCoreTeam,2023)(v4.3.1)using
fiveremainingAOIsandtheauxiliaryfinetuningdata(Schiefer,FNEWS terra (Hijmans, 2023) (v1.7–39), sf (Pebesma, 2018) (v1.0–14) and
andSchwarz).Weusedthreedifferentrandomsamplesoftrainingand exactextractr(Baston,2022)(v.9.1)packages,whilemodeltrainingand
validation datasets (with a ratio of 4:1) in the cross-validation steps validationwasconductedinPython3(VanRossumandDrake,2009)
(hencethethreerepetitions),whilethetestdatasetremainedstable(all (v3.8) using PyTorch (Paszke et al., 2019) (v1.13.1), and captum
forestpixelsofthecorrespondingAOI).Using3repetitionsensuredthat (Kokhlikyanetal.,2020)(v.6.0).
the model predictions did not depend on the split into training and
validation dataset. Note that the term validation dataset refers to the
3. Results
Deep Learning training process here (see Section 2.3), and not to the
spatial hold-out for testing. The described procedure guarantees that
3.1. Generalperformancemetrics
eachmodelisneitherexposedtothetestdataset’stimeseriesnortotheir
siteconditionsduringtraining.Thus,thevalidationprocedurecontains False positives across all AOIs range between 0.01 ± 0.001 (DL
independenttestdata(spatialhold-outAOIineachtrainingrun)while +IND) and 0.027 ± 0.004 (DL base) in the relative error matrices
at the same time, the number of data and exposure to different site (Tables 3, 4 and 5), while the false negatives yield between 0.055 ±
conditionsismaximizedduringtraining.Weusedthesamepre-trained 0.002 (DL base) and 0.078 ± 0.001 (DL +IND). Commission errors
modelforallofthefinetuningsetups. (omissionerrors) arehighest (lowest) inDL basewith0.032 ± 0.005
(0.34±0.014;Table6).Theoverallaccuracyreachesabove0.91forall
2.4.1. Timeseriesaugmentationduringtraining setups.Thehighest(lowest)f1-scoreisachievedbyDLbase(DL+IND)
To reduce overfitting and improve generalization of the model with0.722±0.001(0.654±0.002).Whenconsideringalldisturbances
(Iwana and Uchida, 2020), we applied the following time series (i.e.,alldisturbances>0%ofapixel),omissionerrorsyieldupto0.485
augmentation(TSA)proceduresduringtraining: ±0.004(DL+IND).
window slicing, window warping, and adding random noise (also
calledjitter)insatellitesignalandDOYofobservationstothetraining
Table3
process.
Relativeerrormatrixofallpredictionsandreferencedataacrossallofthe6AOIs
WindowwarpingwasimplementedasinIwanaandUchida(2020)
forDLbasesetupexpressedasmeanandstandarddeviationacrossthreerepe-
by randomly picking a window within the time series and either titionsofspatialblockcross-validation.
stretchingitby2orcontractingitby0.5.Thismethodhasbeenshownto
Reference Total
improveaccuracyandgeneralization(IwanaandUchida,2020).Jitter
was added to the time series by adding or subtracting up to 5 days Undisturbed Disturbed
randomlytotheDOYoftheobservation,andaddingrandomvaluesof Undisturbed 0.812±0.004 0.055±0.002 0.867±0.007
mean0andstandarddeviation0.05tothesatellitevalues.Theformer Predictions Disturbed 0.027±0.004 0.106±0.002 0.133±0.007
Total 0.839±0 0.161±0 1
allowedformoregeneralizationconcerningphenologicalevents(inter-
7

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Table4 WhenlookingatthesingleAOI’sresults,omissionerrorsrangebe-
Relativeerrormatrixofallpredictionsandreferencedataacrossallofthe6AOIs tween 0.2 ± 0.027 (DL Base) and 0.249 ± 0.008 (DL +IND) in NRW
forDLINDsetupexpressedasmeanandstandarddeviationacrossthreerepe- (Supplementary Table 3). When only considering larger disturbance
titionsofspatialblockcross-validation. extentswithinapixel(>50%),theomissionerrorsinNRWarereduced
to0.029±0.011(DLbase)and0.052±0.005(DL+IND).Asopposed
Reference
tothat,omissionerrorsreachupto0.85±0(DL+IND)inTHU.Com-
|     |     | Undisturbed | Disturbed | Total |     |     |     |     |
| --- | --- | ----------- | --------- | ----- | --- | --- | --- | --- |
missionerrorsarelowerthan0.1inalmosteveryAOIandsetup,butare
|     | U n d is t | u r bed 0 . 8 2 ± 0. 0 0 | 2 0 . 0 6 4 ± 0 . 0 | 0 3 0 . 8 8 4 ± 0 . 0 0 5 |     |     |     |     |
| --- | ---------- | ------------------------ | ------------------- | ------------------------- | --- | --- | --- | --- |
highestinNRWandRLP,reachingupto0.103±0.034(DLIND)and
| Predictions | Di s tu r | b e d 0 . 0 19 ± 0 . 0 | 02 0 . 0 9 7 ± 0 . 0 | 0 3 0 . 1 1 6 ± 0 . 0 0 5 |                                   |     |     |     |
| ----------- | --------- | ---------------------- | -------------------- | ------------------------- | --------------------------------- | --- | --- | --- |
|             |           | 0.839±0                | 0.161±0              |                           | 0.036±0.024(DLbase),respectively. |     |     |     |
|             | Total     |                        |                      | 1                         |                                   |     |     |     |
3.2. Disturbancemaps,detectableminimaldisturbanceextent
Table5
Concerningthedisturbanceareaofapixel,allmethods’Producer’s
Relativeerrormatrixofallpredictionsandreferencedataacrossallofthe6AOIs
forDL+INDsetupexpressedasmeanandstandarddeviationacrossthreerep- Accuracies increase with larger damage proportions: DL base shows
Producer’s
etitionsofspatialblockcross-validation. Accuracies higher than 50% (i.e., better than random) for
disturbanceareasofapprox.40m2(=40%,aspixelareais100m2),
Reference whileDL+INDandDLINDreachmorethan50%Producer’sAccuracy
Undisturbed Disturbed Total atapprox.60m2disturbancearea(Fig.3).Inthefollowing,wefocuson
Undisturbed 0.829±0.001 0.078±0.001 0.907±0.001 THU, NRW and RLP for brevity. In THU, most disturbed pixels are
|     |     | 0.01±0.001 | 0.083±0.001 | 0.093±0.001 |     |     |     |     |
| --- | --- | ---------- | ----------- | ----------- | --- | --- | --- | --- |
Predictions Disturbed missedbyallmethodsexceptDLbaseandDLINDwithapprox.76%and
|     | Total | 0.839±0 | 0.161±0 | 1   |     |     |     |     |
| --- | ----- | ------- | ------- | --- | --- | --- | --- | --- |
65%Producer’sAccuraciesinthedisturbancestratumof>90%(Sup-
|     |     |     |     |     | plementary | Fig. 2). Fig. 4, | however, showsthat | the large disturbance |
| --- | --- | --- | --- | --- | ---------- | ---------------- | ------------------ | --------------------- |
areas(especiallylogging)inTHUarecapturedcompletelybyDLbase,
Table6
PerformancemetricsacrossallAOIsforthethreesetups.OE:omissionerror(>50%:onlydisturbanceslargerthan50%ofpixel),CE:commissionerror,BA:balanced
accuracy,OA:overallaccuracy.
| Setup  |     | CE          | OE  |                  | F1          |     | BA          | OA          |
| ------ | --- | ----------- | --- | ---------------- | ----------- | --- | ----------- | ----------- |
|        |     |             | 0   | .3 4 ± 0.0 1 4   |             |     |             |             |
| DLbase |     | 0.032±0.005 |     |                  | 0.722±0.001 |     | 0.814±0.005 | 0.918±0.002 |
|        |     |             | (0  | .2 0 4± 0 .0 11) |             |     |             |             |
±
DLIND 0.023±0.003 0 .4 0.0 1 8 0.697±0.008 0.788±0.008 0.916±0.001
|        |     |             | (0  | .2 7± 0 .0 18)    |             |       |             |         |
| ------ | --- | ----------- | --- | ----------------- | ----------- | ----- | ----------- | ------- |
|        |     |             | 0   | .4 8 5 ± 0 .0 0 4 |             |       |             |         |
| DL+IND |     | 0.012±0.001 |     | ±                 | 0.654±0.002 |       | 0.752±0.002 | 0.912±0 |
|        |     |             | (0  | .3 6 8 0 .0 0 3)  |             |       |             |         |
|        |     | Producer’s  |     |                   |             | +IND, |             |         |
Fig. 3. Barplot showing the Accuracies of the three studied methods (DL base, DL DL IND) for undisturbed class (left group of bars; white
background)anddisturbedclass(diebackandloggingpixels)stratifiedbydisturbanceareain10m2strata(othertengroupsofbars,graybackground)ofspatial
block cross-validation with three repetitions across all of the six AOIs. Numbers indicate amount of pixels in the respective class/stratum. Error bars indicate
standarddeviation.
8

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
andpartiallybyDLIND/+IND. extentofourmethod(Section4.2)anddiscusstheperformanceofthe
ThesmalldiebackareasinthenortheastofTHUarenotcapturedby models depending on the input of VIs (Section 4.3). We discuss the
any method.Asopposedtothat,all methodsshowaccuracies greater generalisability of the models in Section 4.4. Section 5 draws conclu-
|     |     |     | 20–30 | m2  |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
than 50% for disturbances between approx. in NRW (Sup- sionsfromthestudy.
plementaryFig.3).InNRW,smalldisturbancesarepartlydetectedbyall
setups,excepttheverysmalldiebackareas(mainlysingledeadtrees)in 4.1. Researchquestion1:towhatdegreecanTransformersaccurately
| the southwest, | south and | southeast | of the AOI | (Fig. 5). Finally, | Pro- |     |     |     |     |     |
| -------------- | --------- | --------- | ---------- | ------------------ | ---- | --- | --- | --- | --- | --- |
detectforestdisturbanceonformerlyunseenS2timeseries?
ducer’sAccuraciesofthedisturbedclasspixelsinRLParegreaterthan
50%fromdamageareasofbetweenapprox.40m2inDLbase,whilethe
SeveralSITS-basedforestdisturbancemonitoringproductsonCen-
othertwosetupsreachmorethan50%Producer’sAccuracyonlyinthe
tralEuropeanforestshavebeenpublishedsofar,e.g.Puhmetal.(2020),
disturbancestratumof>90%(SupplementaryFig.4).InRLP,however,
SenfandSeidl(2020);Thonfeldetal.(2022)andDutrieuxetal.(2021a).
DLbasereachesalowerProducer’sAccuracyintheundisturbedclass
|          |                 |       |                    |            |     | Senf and | Seidl (2020) | use Landsat | SITS and | the LandTrendr seg- |
| -------- | --------------- | ----- | ------------------ | ---------- | --- | -------- | ------------ | ----------- | -------- | ------------------- |
| (approx. | 96%), while the | other | setup’s Producer’s | Accuracies | are |          |              |             |          |                     |
mentationalgorithm(Kennedyetal.,2010)todetecttrendchangesin
approx.99%.ThisisreflectedinpatchesoffalsepositivesbytheDLbase
medoidcompositesofeachyear’sgrowingseason,yieldingcommission
setup,whicharenotpresentinDL+INDandDLIND(Fig.6).Resultsfor
|     |     |     |     |     |     | and omission | errors of | 0.17 and | 0.37, respectively. | Thonfeld et al. |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | ------------------- | --------------- |
SAX,LUXandBBareshowninSupplementaryFigs.2,3,and4. (2022)defineathresholdTasselled-CapDisturbanceIndexvalueusing
S2andLandsat8inthepresumablyundisturbedyearof2017(beforethe
4. Discussion
|         |               |           |                 |                    |     | hot drought | years) and        | use this   | value as threshold | for disturbance |
| ------- | ------------- | --------- | --------------- | ------------------ | --- | ----------- | ----------------- | ---------- | ------------------ | --------------- |
|         |               |           |                 |                    |     | detection   | afterwards. Their | commission | and omission       | errors are 0.29 |
| In this | study, we use | data from | (mostly public) | forest disturbance |     |             |                   |            |                    |                 |
and0.08,respectively.Twoapproachesusingfittedharmonicmodelsof
datasetsandsixvisuallyinterpretedAOIstotraintransformermodelsto
undisturbedtimeseriesofeachpixel,anddetectingdeviationsoftheir
| detectforestdisturbancesusing |     |     | satelliteimagetimeseries(SITS)ina |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
consecutivepredictionsfromnewobservations,havebeendevelopedby
| two-step approach | (pre-training |     | and finetuning). | We include samples |     |     |     |     |     |     |
| ----------------- | ------------- | --- | ---------------- | ------------------ | --- | --- | --- | --- | --- | --- |
Puhmetal.(2020)andDutrieuxetal.(2021a).Theyachieveaverage
withsmalldisturbedpixelfractionsintraininginordertotestifthese
commissionerrorsof0.23and0.15aswellasaverageomissionerrorsof
| models, using | either ten | S2 bands, | 10 VIs or | both, are capable | of  |     |     |     |     |     |
| ------------- | ---------- | --------- | --------- | ----------------- | --- | --- | --- | --- | --- | --- |
0.2and0.1,respectively.Ourvalidationindicatesasmallercommission
detectingforestdisturbancesofsub-pixelsize. errorthanthementionedmethodsofbetweenapprox.0.012(DL+IND)
models’
In the following, we discuss the three performances and and 0.032 (DL base). Regarding the omission error, most of the
| challenges | (Section 4.1), | assess | the minimal | detectable disturbance |     |     |     |     |     |     |
| ---------- | -------------- | ------ | ----------- | ---------------------- | --- | --- | --- | --- | --- | --- |
mentionedmethodsachievebetterperformancethanours,whichyield
DisturbancemapsofNRWforA)DLbase(topleft),B)DL+IND(topright)andC)(bottomleft)ofthebestseedofspatialblockcross-validationwiththree
Fig.4.
repetitions.Predictions(disturbanceconfidences)greaterthan0.5belongtodisturbedclass,whilepredictionslowerthan0.5belongtoundisturbedclass.Thehigher
thepredictedvalue,themoreconfidentthemodelisaboutadisturbance.DOPscourtesyofopen.NRW(dl-zero-de/2.0).
9

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Fig.5. DisturbancemapsofTHUforA)DLbase(topleft),B)DL+IND(topright)andC)(bottomleft)ofthebestseedofspatialblockcross-validationwiththree
repetitions.Predictions(disturbanceconfidences)greaterthan0.5belongtodisturbedclass,whilepredictionslowerthan0.5belongtoundisturbedclass.Thehigher
thepredictedvalue,themoreconfidentthemodelisaboutadisturbance.DOPscourtesyofLandesamtfürBodenmanagementundGeoinformationThüringen(dl-de/
by-2-0).
between 0.34 (DL base) and 0.485 (DL +IND). The overall omission morecomplexphenologyandspeciescompositionofdeciduous,conif-
error in our study, however, is strongly influenced by the very high erous and potentially mixed forest types in temperate forest, which
omission errors in the small disturbance extent strata (cp. Table 6: imposesmanychallengesonSITS-basedforestdisturbancemonitoring.
omissionerrorwhenonlyconsideringdisturbancesgreaterthan50%). Broadleavedandmixedforestsexhibitmorefluctuationsinthespectral
Note that most of the mentioned publications do not consider partial signal of the time series, for instance caused by a more pronounced
disturbances (Dutrieux et al., 2021a; Puhm et al., 2020) or explicitly phenological cycle and understory vegetation during leaf-off periods.
remove disturbances smaller than three pixels from their validation TheDLmodelarchitectureusedinthisstudyisspecificallydesignedto
(Thonfeldetal.,2022).Whenconsideringonlylargedisturbanceextents address these challenges, as half of the weights in the encoder of the
ofatleast90%ofapixel,ourmethodsomitbetweenapproximately0.08 modelshavethesolepurposeofmodellingtheunderstandingoftime
(DL base) and 0.23 (DL +IND) of the disturbances (cp. Fig. 3), thus and seasonality (Yuan and Lin, 2021). Accordingly, the periodicity of
improvinguponmostoftheaforementionedmethodsinthisdisturbance broadleavedforestisalmostneverconfusedwithadisturbancesignal,as
stratumw.r.t.omissionerroraswell. shown in the stable and low commission errors across forest types in
Additionally,mostoftheearlierstudies(Puhmetal.,2020;Senfand SupplementaryTable4.Whiletheomissionerrorsarehigherinbroad-
Seidl,2020;Thonfeldetal.,2022)haveincommonavalidationusing leavedforest,Producer’sAccuraciesarestillreasonablyhigh.
random sampling points, which is not directly comparable to ours, Another key challenge of SITS-based forest disturbance detection
whichtakesintoaccountallforestpixelsofourAOIsandfocusesonall models is the occurrence of gradual and partial disturbances and co-
disturbanceextentsinthedisturbedclass.Recently,Perbetetal.(2024) morbidities. Biotic disturbance agents, for instance, often lead to
examinedthecapabilityofTransformerstoidentifydisturbancesonsub- gradualorpartialcrowndiebackwithwidelydifferingdurations(Senf
pixellevel(called“partialdisturbances”,here:partialharvestandpar- et al., 2017), e.g. drought dieback within years (Bigler et al., 2007;
tialwindthrow,definedasbetween25%and75%ofthepixelcovered Haberstroh et al., 2022) and mortality from bark beetle infestations
by a disturbed area) on Landsat yearly composites of boreal forest in withinweeks(S ˇ tursova´etal.,2014).Additionally,disturbanceagents
Canada.Theyreportomissionerrorsof0.155(partialwindthrow)and differintheirintra-annualtiming(e.g.windthrowinwinter,barkbeetle
0.205(partialharvest)withasimilarvalidationapproach.Whiletheir in spring/summer) (Senf et al., 2017) and co-morbidities occur
reported results clearly outperform ours, note that these metrics are frequently (Seidl et al., 2017). All of this may lead to mixed spectral
stronglydependentonthelabeldistribution(e.g.ifmostofthepartial responses.Tocopewiththischallenge,differentlevelsofaggregation
harvestwasactually25%harvestedorrather75%harvested),whichis areconsideredbyTransformersbystackingencoderblocksuponeach
notreportedinthestudy.Additionally,ourmethodhastocopewiththe other (Jawahar et al., 2019; Yuan and Lin, 2021). Hence, the overall
10

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Fig.6. DisturbancemapsofRLPforA)DLbase(topleft),B)DL+IND(topright)andC)(bottomleft)ofthebestseedofspatialblockcross-validationwiththree
repetitions.Predictions(disturbanceconfidences)greaterthan0.5belongtodisturbedclass,whilepredictionslowerthan0.5belongtoundisturbedclass.Thehigher
thepredictedvalue,themoreconfidentthemodelisaboutadisturbance.DOPscourtesyofLandesamtfürVermessungundGeobasisinformationRheinland-Pfalz(dl-
de/by-2-0).
periodicityacrossyearscanbemodelledaswellasshort-termdeviations unknownfromtrainingwhentryingtodistinguishbetweenundisturbed
thereof. As indicated by an additional analysis using explainable AI anddisturbedpixels.Thisexplanationissupportedbytheobservation
(SupplementaryFig.11;Sundararajanetal.,2017),ourmodelsseemto thatinthesouthwesternpartofBB,thedenseforeststandsarelargely
takeintoaccounttemporalcuesthroughoutthewholetimeseries,while classifiedcorrectly,whileintheopenstandsinthenorthernpart,mis-
at thesame time putting emphasis onspecificobservations. Thissug- classificationsoccur(especiallyDLbaseandDLIND,cp.Supplementary
geststhat suddenforest disturbancessuchaswindthrows andharvest Fig. 7). Secondly, in open forest stands on sandy soils as in BB, the
canlikelybe detectedbyTransformersaswellasgradualdroughtef- spectralsignalofsoillikelysuperimposestheoverallspectraltrajectory
fects,asconfirmedbyPerbetetal.(2024)andDuetal.(2023).During oftheforestcanopy.Thismightalsobethecaseforopenbedrockinthe
training,ourmodelshavebeenexposedtoaverylargenumberoftime steepslopesinourAOIinRLP,whichmightexplaintheoverpredictions
seriesofmultipledisturbanceagents’responses(SenfandSeidl,2020; ofdisturbanceintheDLbasemodel(cp.Fig.6).
Thonfeldetal.,2022),potentiallyenablingthemtointernalisealarge Anotherreasonformisclassificationsinopenstandsandsteepslopes
variety of spectral trajectories under different conditions. Due to co- might be a strong impact of the understory on the spectral signal
morbidities and the lack of reliable reference data for disturbance (Haberstrohetal.,2022).Thismightbeaparticularproblemincaseof
agents,wecouldunfortunatelynottestifthisisreallythecase. openforeststands(Erikssonetal.,2006).Sincegrasslands’photosyn-
While all ofthemodels areableto detectmostofthe disturbance thetic activity and the corresponding spectral signal change more
patchesacrossallAOIs(exceptDL+INDinsomecases,e.g.Fig.5),the rapidly than forests under adverse conditions (Nicolai-Shaw et al.,
performance metrics of our validation reveal large differences in the 2017),itispossiblethattheunderstoryofopenforeststandsappears
predictiveperformanceamongthesixAOIs(cp.SupplementaryTable3, stressedmorerapidlyindroughtyears,whiletheresponsefromthetrees
Figs.3,4,5,SupplementaryFigs.2,3,4).F1-scoresinTHUandBBare isdelayed(Haberstrohetal.,2022;Nicolai-Shawetal.,2017;Reiner-
especiallylowacrossallsetups.InBB,thismightbeattributedtothe mannetal.,2019).Themodelsthenmightperceivethedegradationof
influenceofsoilbackgroundonthespectraltrajectoryshiningthrough theundergrowthasdiebackofthecanopytreesinBB.
the sparse canopy. BB is the only AOI with large areas of open Pinus InTHU,theeffectofundergrowthonthehighomissionerrormight
sylvestrisL.standswithacorrespondingnotableamountofsubpixelbare be attributed to natural succession and remaining undergrowth after
soilfractions. logging. Here, the disturbances (mostly logging) mainly occurred
Given that such stands only occur in BB, our spatial block cross- around 2019/2020 as confirmed by visual interpretation of historical
validationapproachmayleadtopessimisticresults(Kattenbornetal., DOPs, while the time series for validation ended in June 2022. Thus,
2022),asthemodelshavetocopewiththisfeatureofthetimeseries many of the disturbances happened early in the time series, and
11

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
vegetationrecoverybecameapparentafterwards.AsindicatedinSup- treesonly,theminimumdisturbanceextentswithProducer’sAccuracies
plementaryFig.11,allsetupstendtoregardthemostrecentobserva- greaterthan50%areevensmaller(e.g.30–40m2stratumforDLbase,
tionsofthetimeseriesasmostimportant,meaningthatre-growthand Supplementary Table 4). In coniferous forest, detecting small distur-
naturalsuccessionhavealargeimpactonthepredictions.Consequently, bancesismoreimportant,asitmaybebeneficialforthedetectionofthe
vegetation (but not necessarily tree) recovery seems to lead to undis- beginningofbarkbeetleinfestationsandotherpests(Kautzetal.,2023).
turbedpredictionsinDL+INDandDLIND,andlesspronouncedinDL Thismightenableearlywarningsinfutureapplications.Thecapability
base. This is supported by the observation that recent clear-cuts ofTransformerstodetectdisturbancesonsub-pixellevelusingSITShas
revealingbaresoilasshowninNRW(Fig.4)aredetectedmuchmore beenconfirmedbyPerbetetal.(2024)evenonyearlycomposites.Yet,
accuratelythanthelargeloggingactivitiesinTHU.Consequently,the thedisturbancesignalofdisturbancessmallerthan30–40%ofapixel(in
performanceonloggingareaswilllikelyimproveifrunningthemodels coniferous forest; about 50% in deciduous forest, Supplementary
operationally on each new S2 observation and keeping record of Table4)mightbetoosubtleanddominatedbynoiseandphenological
disturbedpredictions.Suchanoperationalmodeisfullyfeasibleforthe variabilityforareliabledetection.
currentversionofthemodel.Thiswouldalsoenabletheretrievalofa
disturbancedate,whichthemodeliscurrentlynotcapableofproviding 4.3. Researchquestion3:doTransformersneedvegetation/disturbance
for a single prediction. To show the mentioned effect, we made pre- indicesforaccuratepredictions?
dictionsonTHUforeachyearbetween2019and2022usingDLbase,
revealingthatthedisturbanceshavebeencapturedearlier,butsucces- Although thethreeDLsetupsare exposedtoroughlythe samein-
sionledthemodeltoreverttoundisturbedpredictionsafterwards(e.g. formation, they express considerable differences in their predictions
inthenorth-andsoutheastinSupplementaryFig.8). (Fig.3).Thisissurprising,sinceDL+INDshouldbeabletoreverttothe
Since dieback patches are often logged afterwards, the dieback S2bandsasinDLbaseandtheVIsasinDLIND.TheVIsofDLINDand
apparentinourDOPslikelyhappenedclosertotheDOPacquisitiondate DL +IND, in turn, resort to the S2 bands exclusively. Therefore, one
thanmanyoftheloggingactivities(iftheyhappenedearlier,theywould mightexpectthemodelstodrawsimilarconclusionsfromtheSITS,and
appear as logging). Observing that recent disturbances are detected theDL+INDsetuptobebest,asitcontainsalltheinformation.TheVIs,
more accurately by our models (see above), it is plausible that less however, have been handcrafted for a specific purpose, meaning that
omissionsoccurwhenconsideringonlydiebackandexcludinglogging they condense information to be sensitive for a specific vegetation
fromanalyses(SupplementaryFig.9).Here,Producer’sAccuraciesin- feature.SomeoftheappliedVIs,forinstance,aresensitivetochangesin
creasetoapprox.59%inthe40–50m2and94%inthe>90m2distur- chlorophyll content or cell structure (e.g. NDVI, NDRE, TCG), while
banceextentstrata(bothDLbase). othersfocusonwaterstress(MSI,TCW,NDMI,NDWI,CRSWIR).This
also imposes prior knowledge ontheDL IND/DL +INDsetups, which
4.2. Researchquestion2:whatisthesmallestdisturbanceextentthatcan mightlimitDLIND’spredictivecapability(so-calledhypothesisspace)to
bedetectedbytheproposedmethod? specifictargetfeatures.AlthoughnotrestrictedtospecificfeaturesasDL
IND, we also include a high redundancy of information in DL +IND,
Whilelargedisturbancesabove90%disturbanceextentofapixelare whichmightconfusethemodel.Zhuetal.(2020)alsoconfirmedthat
detected reliably by all setups (e.g. >90% Producer’s Accuracy in DL inputtingmorethantheessentialbandstotheirmodeldoesnotleadto
base,seeSection4.1),adropofProducer’sAccuraciesisvisibleinthe furtherimprovementofmodelperformance.Inourcase,itevenresults
60–90%disturbanceextents.Thismightindicatethatevenlargepartial inDL+INDperformingworsethantheothertwomethods.
disturbances are much more difficult to detect than stand-replacing Asopposedtothat,DLbasecancombinetheS2bandsdifferentlyand
disturbances,astheystillshowaspectraltrajectoryresemblingforest. more dynamically, not being limited to prior knowledge constraints.
Additionally,thesepixelsareusuallylocatedattheedgeofdisturbance SinceDLbaseisabletodetectmore(andsmaller)disturbances,while
areas,whicharedifficulttodelineate.Hence,inaccuraciesinthegeo- appearingtowronglyclassifymoreundisturbedpixels,itseemstobe
locationofthereferencedatacomparedtotheS2dataorimprecisely moresensitivetosubtledeviationsofthesatellitesignalfromtheun-
labelled disturbances could also lead to this effect. Additionally, very disturbedclass.Thisisalsoindicatedbythehigherconfusionbetween
smallandisolatedforestdisturbancepatchesaremostlyomittedbyour confidencescoresregardingsmalldiebackandundisturbedforestinDL
transformer models. Examples are the single isolated trees and small basecomparedtoDL+IND/IND(SupplementaryFig.10).Also,DLbase
dieback patches scattered around SAX (Supplementary Fig. 5), in the appears to overpredict the disturbed class in case of steep terrain, as
southwestofNRW(Fig.4)andinthenorthwestofBB(Supplementary visibleinthecenterandnorthofRLP(Fig.6).Steepterrainusuallyhas
Fig.7),amongothers.Onereasonthatsingleisolatedorsmallgroupsof shallower soils, sometimes even exposing bedrock, which desiccates
trees cannot be detected is that we exclude pixels with disturbance morerapidly.Thus,ahighersensitivitytosmalldisturbancesinevitably
fractionsoflessthan10%fromtraining.This,however,wasanecessary leads to commission errors regarding forests with less stable spectral
step,sincethemodelneedstobeabletodistinguishbetweenthetwo conditions. Indeed, a certain amount of false positives is likely un-
classesinthefirstplace.Wedecreasedthisthresholdasmuchaspossible avoidable in the attempt of detecting small forest disturbance. The
inordertoallowforthedetectionofdisturbancesthatareassmallas outputoftheDLmodels,however,isnotabinaryclasslabelinthefirst
possible. Investigating the distribution of disturbance confidences place,butratheraconfidencescoreforthedisturbedclass.Therefore,it
amongthedisturbanceextentstrata(severities;SupplementaryFig.10) is possible to shift the threshold for binarization to, for instance, 0.8
indicatesthatthemodelsare1)abletoidentifyundisturbedandclearly rather than the commonly used 0.5 to address these false positives.
disturbed(largedisturbancefractions)pixelswithhighconfidence,and When doing so, commission errors are further reduced and these po-
2) are increasingly confident about disturbance predictions with tentialsystematicerrorsareavoided(cp.Fig.6).Weconcludethatour
increasing disturbance size. Obviously, there is greater uncertainty in modelsdonotrelyonVIsforaccuratepredictions.
the smaller disturbance area strata (Supplementary Fig. 10), as the
model has to distinguish between phenological fluctuations of partly 4.4. Generalisability
intactforest,thepotentiallydiversedisturbancesignalssuperimposed
byphenology(Perbetetal.,2024),spectralinfluenceoftheunderstory In this study, we tried to covermany different environmental and
(seeSection4.1),andnoiseinherenttosatellitedata(atmosphericand forestconditionsinoursixvalidationAOIs.Yet,thenumberofpixels
topographiceffects,etc.).Still,themodelsachieveaProducer’sAccu- andAOIsaswellastheirdistributionwaslimitedduetolimitedhuman
racygreaterthan50%fordisturbancefractionsassmallasapprox.40 resourcesforlabelingandavailabilityofDOPsacrossGermany.Thus,
m2(DLbase)and60m2(DL+IND,DLIND).Whenregardingconiferous largepartsofGermanysuchasthenorthandthesoutheast,including
12

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
whole ecoregions such as the German Alps, have been completely Fundinginformation
omittedinvalidation(cp.Fig.2).Whiletheabsenceofcomprehensive
validation data prevents an accuracy assessment for these areas, we ThisworkwasfundedbyGermanFederalMinistryforEnvironment,
provide predictions throughout Germany for time series ending in Nature Conservation, Nuclear Safety and Consumer Protection in the
September2021(aftertheendofthemajordroughtfrom2018to2020) FutureForestprojectundergrantnumber67KI21002C.
forageneralassessmentinSupplementaryFig.12.Theseresultsshow
majordisturbancesinregionsthatareknowntobeaffectedstronglyby CRediTauthorshipcontributionstatement
the drought, e.g. eastern Northrhine-Westphalia (A in Supplementary
Fig. 12),theHarzMountains(B)aswellastheNationalPark Saxony ChristopherSchiller:Writing–originaldraft,Visualization,Vali-
Switzerland (C). On the contrary, the south and north of Germany dation, Methodology, Formal analysis, Data curation, Conceptualiza-
appearlessaffectedbydisturbances.Allinall,thisresultshowsthatthe tion.JonathanKo¨ltzow:Writing–review&editing.SelinaSchwarz:
modelprovidesplausiblepredictionsinareaswithoutfinetuningdataas Writing – review & editing, Data curation. Felix Schiefer: Writing –
well.Yet,withoutcomprehensivevalidationdata,itremainsunclearif review&editing,Datacuration.FabianEwaldFassnacht:Writing–
themodelisreadytobeemployedthroughoutGermany. review&editing,Supervision,Fundingacquisition,Conceptualization.
5. Conclusionsandoutlook
Declarationofcompetinginterest
Here, we present a forest disturbance monitoring method using
Theauthorsdeclarenocompetinginterests.
Transformers,astate-of-the-artDeepLearning(DL)architecture,using
dense Sentinel-2 time series. Our models have been trained on a rich
Dataavailability
input dataset (more than 1 million Sentinel-2 pixels in pre-training,
more than 500k in finetuning) consisting of different forest types
The code to reproduce the findings and continue with the trained
(coniferous,broadleaved),environmentalconditions(steepvs.shallow
model in further studies will be available upon acceptance of this
slopes),forestcharacteristics(openforeststandswithlargeamountof
manuscript under https://github.com/ChrSchiller/dl_forest_
baregroundinBBvs.denseforestcoverintheotherAOIs)anddistur-
disturbance. Interactive versions of the maps and barplots shown in
bance agents (windthrow, bark beetle, drought damage, etc.). Our
this manuscript are available under: https://futureforest.eu.
transformermodelsdonotneedcompositingorgapfillingandcancope
pythonanywhere.com/servedownload/dl_forest_decline. The five
with multivariate time series as input. The results are stable across
disturbance datasets of the AOIs from Germany are available upon
differentrandomsetsoftrainingdata(threerepetitionsinspatialblock
requestunderhttps://zenodo.org/records/8397141.
cross-validation)andnumberofobservationsinthetimeseries(average
numberofobservations:62inLUXvs.180inTHU).SinceDLbasede-
Acknowledgments
tectsmore(andsmaller)disturbancesthanthesetupsusingVIs,hand-
craftedvegetationanddisturbanceindicesseemnottoberequiredby
TheauthorswouldliketothanktheHPCServiceofZEDAT(CURTA),
Deep Learning-based remote sensing of forest disturbance. The rather FreieUniversita¨tBerlin,forcomputingpowerandtime.Especially,the
small performance gains compared to existing methods, however, are
firstauthorwantstothankLorisBenettandBerndMelchersfromCURTA
tradedoffbyalargeamountoftrainingdataneededandthecomplexity
fortheirsupport,ideasand-aboveall-theirpatienceandforbearance.
ofthemodel.
We also want to thank the providers of the eo-lab platform for their
Sincedisturbancesthathappenedearlyintheclassifiedtimeseries
magnificentservice.Wearegreatlythankfulfortheopendataservicesof
tendtobeomitted,anoperationalmonitoringsystemshouldencompass
Luxembourg and the German federal states of Brandenburg, Saxony,
arecordofformerdetections.Sincewevarytheenddatesoftheinput
Thuringia,Northrhine-WestphaliaandRhineland-Palatinate.
timeseriesthroughouttraining,weexpectthemodelstobeapplicableat
anytimeoftheyear.GiventhatourDLbasemodelisabletocapturesub-
AppendixA. Supplementarydata
pixeldisturbancesstartingatabout40m2andlarger,thismightenablea
nearreal-timemonitoringbyinvokinganewmodelinferenceeverytime
Supplementarydatatothisarticlecanbefoundonlineathttps://doi.
anewS2acquisitionisavailable,andcomparingthechangeofitspre-
org/10.1016/j.rse.2024.114475.
dictionsafterwards.However,towhatextentourmodelsarecapableof
timely detections of emerging disturbances such as early-stage bark
References
beetleinfestationshasyettobeinvestigatedinfurtherstudies.
Somestepscanbeundertakentofurtherenhancethemodel’sper-
Abdullah,H.,Darvishzadeh,R.,Skidmore,A.,Heurich,M.,2019.SensitivityofLandsat-8
formanceandgeneralisability.Thedatacoverageinfinetuningmustbe OLIandTIRSdatatofoliarpropertiesofearlystagebarkbeetle(Ipstypographus,L.).
improved, e.g. by incorporating data from southeastern and northern Infestat.RemoteSens.11,398.https://doi.org/10.3390/rs11040398.
Ahmed,S.,Nielsen,I.E.,Tripathi,A.,Siddiqui,S.,Ramachandran,R.P.,Rasool,G.,2023.
Germany.Wehopethatwithfutureadvancementsinopendatapolicies,
Transformersintime-seriesanalysis:atutorial.CircuitsSyst.SignalProc.42,
thiscanberealizedinthenearfuture.Limitedaccesstoremotesensing 7433–7466.https://doi.org/10.1007/s00034-023-02454-8.
data(e.g.aerialimages)collectedbyfederaladministrationscurrently Bandyopadhyay,D.,Bhavsar,D.,Pandey,K.,Gupta,S.,Roy,A.,2017.Rededgeindexas
prevents an operational nationwide application of the model in Ger- anIndicatorofvegetationgrowthandvigorusinghyperspectralremotesensingdata.
Proc.Natl.Acad.Sci.,IndiaSect.APhys.Sci.87,879–888.https://doi.org/10.1007/
many. Furthermore, the spatial context of time series also contains s40010-017-0456-4.
valuableinformationaboutdisturbanceregimesandtheirgrowth,e.g. Baston,D.,2022.Exactextractr:FastExtractionfromRasterDatasetsUsingPolygons.
bark beetles spreading out to infest neighboring trees (Kautz et al., Bennett,L.,Melchers,B.,Proppe,B.,2020.Curta:AGeneralPurposeHigh-Performance
ComputeratZEDAT.FreieUniversit¨at,Berlin.
2023).Recentlydevelopedadaptationsoftransformermodelscanalso
Bigler,C.,Gavin,D.G.,Gunning,C.,Veblen,T.T.,2007.Droughtinduceslaggedtree
incorporate the spatial context (Yuan et al., 2022), which could be mortalityinasubalpineForestintheRockyMountains.Oikos116,1983–1994.
beneficialforenhancingdetectioncapabilities.Suchanapproachcould Boegh,E.,Soegaard,H.,Broge,N.,Hasager,C.B.,Jensen,N.O.,Schelde,K.,Thomsen,A.,
2002.Airbornemultispectraldataforquantifyingleafareaindex,nitrogen
also enable a model to distinguish between standing deadwood and
concentration,andphotosyntheticefficiencyinagriculture.RemoteSens.Environ.
logging,whichwouldbevaluableinformationformanystakeholdersin 81,179–193.https://doi.org/10.1016/S0034-4257(01)00342-X.
forestry(Holzwarthetal.,2023).
Bo¨sch,M.,Elsasser,P.,Franz,K.,Lorenz,M.,Moning,C.,Olschewski,R.,Ro¨dl,A.,
Schneider,H.,Schro¨ppel,B.,Weller,P.,2018.Forestecosystemservicesinrural
areasofGermany:insightsfromthenationalTEEBstudy.Ecosyst.Serv.31,77–83.
https://doi.org/10.1016/j.ecoser.2018.03.014.
13

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
Br´eda,N.,Huc,R.,Granier,A.,Dreyer,E.,2006.Temperateforesttreesandstandsunder oftheAssociationforComputationalLinguistics.AssociationforComputational
severedrought:areviewofecophysiologicalresponses,adaptationprocessesand Linguistics,Florence,Italy,pp.3651–3657.https://doi.org/10.18653/v1/P19-1356.
long-termconsequences.Ann.For.Sci.63,625–644.https://doi.org/10.1051/ Kattenborn,T.,Schiefer,F.,Frey,J.,Feilhauer,H.,Mahecha,M.D.,Dormann,C.F.,2022.
forest:2006042. Spatiallyautocorrelatedtrainingandvalidationsamplesinflateperformance
BundesministeriumfürErn¨ahrungundLandwirtschaft(BMEL),2023.Ergebnisseder assessmentofconvolutionalneuralnetworks.ISPRSOpenJ.Photogramme.Remote
Waldzustandserhebung2022(ResultsoftheForestConditionSurvey2022).Bonn, Sens.5,100018.https://doi.org/10.1016/j.ophoto.2022.100018.
Germany. Kautz,M.,Peter,F.J.,Harms,L.,Kammen,S.,Delb,H.,2023.Patterns,driversand
Cohen,W.B.,Yang,Z.,Kennedy,R.,2010.Detectingtrendsinforestdisturbanceand detectabilityofinfestationsymptomsfollowingattacksbytheEuropeansprucebark
recoveryusingyearlyLandsattimeseries:2.TimeSync—toolsforcalibrationand beetle.J.Pest.Sci.96,403–414.https://doi.org/10.1007/s10340-022-01490-8.
validation.RemoteSens.Environ.114,2911–2924.https://doi.org/10.1016/j. Kennedy,R.E.,Yang,Z.,Cohen,W.B.,2010.Detectingtrendsinforestdisturbanceand
rse.2010.07.010. recoveryusingyearlyLandsattimeseries:1.LandTrendr—temporalsegmentation
Coops,N.C.,Shang,C.,Wulder,M.A.,White,J.C.,Hermosilla,T.,2020.Changeinforest algorithms.RemoteSens.Environ.114,2897–2910.https://doi.org/10.1016/j.
condition:characterizingnon-standreplacingdisturbancesusingtimeseriessatellite rse.2010.07.008.
imagery.For.Ecol.Manag.474,118370.https://doi.org/10.1016/j. Kokhlikyan,N.,Miglani,V.,Martin,M.,Wang,E.,Alsallakh,B.,Reynolds,J.,
foreco.2020.118370. Melnikov,A.,Kliushkina,N.,Araya,C.,Yan,S.,etal.,2020.Captum:AUnifiedand
Crist,E.P.,Cicone,R.C.,1984.Aphysically-basedtransformationofThematicMapper GenericModelInterpretabilityLibraryforPytorch.
Data—TheTMTasseledCap.IEEETrans.Geosci.RemoteSens.GE-22,256–263. Kong,Y.-L.,Huang,Q.,Wang,C.,Chen,Jingbo,Chen,Jiansheng,He,D.,2018.Long
https://doi.org/10.1109/tgrs.1984.350619. short-termmemoryneuralnetworksforonlinedisturbancedetectioninsatellite
Dobor,L.,Hla´sny,T.,Rammer,W.,Zimova´,S.,Barka,I.,Seidl,R.,2020.Issalvage imagetimeseries.RemoteSens.10,452.https://doi.org/10.3390/rs10030452.
loggingeffectivelydampeningbarkbeetleoutbreaksandpreservingforestcarbon Langner,N.,Puhm,M.,Deutscher,J.,Wimmer,A.,Adler,P.,Backa,J.,Eisenecker,P.,
stocks?J.Appl.Ecol.57,67–76.https://doi.org/10.1111/1365-2664.13518. Reinosch,E.,Wiesehahn,J.,Hoffmann,K.,Oehmichen,K.,2023.FNEWS-
Du,B.,Yuan,Z.,Bo,Y.,Zhang,Y.,2023.Acombineddeeplearningandpriorknowledge Jahresprodukte2018bis2022.
constraintapproachforlarge-scaleForestdisturbancedetectionusingtimeseries Latifi,H.,Fassnacht,F.E.,Schumann,B.,Dech,S.,2014.Object-basedextractionofbark
remotesensingdata.RemoteSens.15,2963.https://doi.org/10.3390/rs15122963. beetle(IpstypographusL.)infestationsusingmulti-dateLANDSATandSPOTsatellite
Dutrieux,R.,F´eret,J.-B.,Ose,K.,2021a.Miseaupointd’unem´ethodereproductible imagery.Progr.Phys.Geogr.:EarthEnviron.38,755–785.https://doi.org/10.1177/
pourlesuivig´en´eralis´edesd´egatsdescolytespart´el´ed´etectionsatellitaire.ONF 0309133314550670.
Rend.Techn.ONFRend.Techn.37–44. Mandl,L.,Lang,S.,2023.UncoveringearlytracesofbarkbeetleinducedForeststressvia
Dutrieux,R.,F´eret,J.-B.,Ose,K.,DeBoissieu,F.,2021b.PackageFordead. semanticallyenrichedSentinel-2dataandspectralindices.PFG91,211–231.
EO-Lab,2023.FutureForestProjct(FF.ai). https://doi.org/10.1007/s41064-023-00240-4.
Eriksson,H.M.,Eklundh,L.,Kuusk,A.,Nilson,T.,2006.Impactofunderstoryvegetation Mouret,F.,Morin,D.,Martin,H.,Planells,M.,Vincent-Barbaroux,C.,2024.Towardan
onforestcanopyreflectanceandremotelysensedLAIestimates.RemoteSens. operationalmonitoringofoakdiebackwithmultispectralsatellitetimeseries:acase
Environ.103,408–418.https://doi.org/10.1016/j.rse.2006.04.005. studyinCentre-ValDeLoireregionofFrance.IEEEJ.Sel.Top.Appl.EarthObservat.
Forzieri,G.,Pecchi,M.,Girardello,M.,Mauri,A.,Klaus,M.,Nikolov,C.,Rüetschi,M., RemoteSens.17,643–659.https://doi.org/10.1109/JSTARS.2023.3332420.
Gardiner,B.,Tomaˇstík,J.,Small,D.,Nistor,C.,Jonikavicius,D.,Spinoni,J., Mu,Y.,Guo,J.,Shahzad,M.,Zhu,X.X.,2024.NationwideTreeSpeciesMappingin
Feyen,L.,Giannetti,F.,Comino,R.,Wolynski,A.,Pirotti,F.,Maistrelli,F., GermanywithForestformer:AssessingForestResilienceandUnveilingDistribution
Savulescu,I.,Wurpillot-Lucas,S.,Karlsson,S.,Zieba-Kulawik,K.,Strejczek- Patterns.https://doi.org/10.2139/ssrn.4800294.
Jazwinska,P.,Mokroˇs,M.,Franz,S.,Krejci,L.,Haidu,I.,Nilsson,M.,Wezyk,P., Mullissa,A.,Reiche,J.,Saatchi,S.,2023,July.SeasonalForestDisturbanceDetection
Catani,F.,Chen,Y.-Y.,Luyssaert,S.,Chirici,G.,Cescatti,A.,Beck,P.S.A.,2020. UsingSentinel-1SAR&Sentinel-2OpticalTimeseriesDataandTransformers.In:
AspatiallyexplicitdatabaseofwinddisturbancesinEuropeanforestsovertheperiod IGARSS2023-2023IEEEInternationalGeoscienceandRemoteSensingSymposium.
2000–2018.EarthSyst.Sci.Data12,257–276.https://doi.org/10.5194/essd-12- IEEE,pp.3122–3124.
257-2020. Netherer,S.,Panassiti,B.,Pennerstorfer,J.,Matthews,B.,2019.Acutedroughtisan
Frantz,D.,2019.FORCE—Landsat+Sentinel-2analysisreadydataandbeyond.Remote importantdriverofbarkbeetleinfestationinAustrianNorwaysprucestands.Front.
Sens.11,1124.https://doi.org/10.3390/rs11091124. For.Glob.Change2,39.https://doi.org/10.3389/ffgc.2019.00039.
Gao,B.,1996.NDWI—Anormalizeddifferencewaterindexforremotesensingof Nicolai-Shaw,N.,Zscheischler,J.,Hirschi,M.,Gudmundsson,L.,Seneviratne,S.I.,2017.
vegetationliquidwaterfromspace.RemoteSens.Environ.58,257–266.https://doi. Adroughteventcompositeanalysisusingsatelliteremote-sensingbasedsoil
org/10.1016/S0034-4257(96)00067-3. moisture.RemoteSens.Environ.203,216–225.https://doi.org/10.1016/j.
García,M.J.L.,Caselles,V.,1991.Mappingburnsandnaturalreforestationusing rse.2017.06.014.
thematicmapperdata.GeocartoInt.6,31–37.https://doi.org/10.1080/ Pasquarella,V.J.,Ar´evalo,P.,Bratley,K.H.,Bullock,E.L.,Gorelick,N.,Yang,Z.,
10106049109354290. Kennedy,R.E.,2022.DemystifyingLandTrendrandCCDCtemporalsegmentation.
García-Herrera,R.,Garrido-Perez,J.M.,Barriopedro,D.,Ordo´n˜ez,C.,Vicente-Serrano,S. Int.J.Appl.EarthObs.Geoinf.110,102806.https://doi.org/10.1016/j.
M.,Nieto,R.,Gimeno,L.,Sorí,R.,Yiou,P.,2019.TheEuropean2016/17drought. jag.2022.102806.
J.Clim.32,3169–3187.https://doi.org/10.1175/JCLI-D-18-0331.1. Paszke,A.,Gross,S.,Massa,F.,Lerer,A.,Bradbury,J.,Chanan,G.,Killeen,T.,Lin,Z.,
Gazol,A.,Camarero,J.J.,2022.Compoundclimateeventsincreasetreedrought Gimelshein,N.,Antiga,L.,Desmaison,A.,Kopf,A.,Yang,E.,DeVito,Z.,Raison,M.,
mortalityacrossEuropeanforests.Sci.TotalEnviron.816,151604.https://doi.org/ Tejani,A.,Chilamkurthy,S.,Steiner,B.,Fang,L.,Bai,J.,Chintala,S.,2019.PyTorch:
10.1016/j.scitotenv.2021.151604. AnImperativeStyle,High-PerformanceDeepLearningLibrary.
Gitelson,A.,Merzlyak,M.N.,1998.Remotesensingofchlorophyllconcentrationin Patacca,M.,Lindner,M.,Lucas-Borja,M.E.,Cordonnier,T.,Fidej,G.,Gardiner,B.,
higherplantleaves.Adv.SpaceRes.22,689–692. Hauf,Y.,Jasineviˇcius,G.,Labonne,S.,Linkeviˇcius,E.,Mahnken,M.,Milanovic,S.,
Grabska,E.,Hawryło,P.,Socha,J.,2020.ContinuousdetectionofSmall-scalechangesin Nabuurs,G.,Nagel,T.A.,Nikinmaa,L.,Panyatov,M.,Bercak,R.,Seidl,R.,
scotspinedominatedstandsusingdenseSentinel-2timeseries.RemoteSens.12, Ostrogovi´cSever,M.Z.,Socha,J.,Thom,D.,Vuletic,D.,Zudin,S.,Schelhaas,M.,
1298.https://doi.org/10.3390/rs12081298. 2022.SignificantincreaseinnaturaldisturbanceimpactsonEuropeanforestssince
Grillakis,M.G.,2019.IncreaseinsevereandextremesoilmoisturedroughtsforEurope 1950.Glob.Chang.Biol.29,1359–1376.https://doi.org/10.1111/gcb.16531.
underclimatechange.Sci.TotalEnviron.660,1245–1255.https://doi.org/ Pebesma,E.,2018.SimplefeaturesforR:standardizedsupportforspatialvectordata.
10.1016/j.scitotenv.2019.01.001. RJ.439–446.https://doi.org/10.32614/RJ-2018-009.
Haberstroh,S.,Werner,C.,Grün,M.,Kreuzwieser,J.,Seifert,T.,Schindler,D., Perbet,P.,Guindon,L.,Coˆt´e,J.-F.,B´eland,M.,2024.Evaluatingdeeplearningmethods
Christen,A.,2022.CentralEuropean2018hotdroughtshiftsscotspineforesttoits appliedtoLandsattimeseriessubsequencestodetectandclassifyborealforest
tippingpoint.PlantBiol.J.24,1186–1197.https://doi.org/10.1111/plb.13455. disturbancesevents:thechallengeofpartialandprogressivedisturbances.Remote
Healey,S.,Cohen,W.,Zhiqiang,Y.,Krankina,O.,2005.Comparisonoftasseledcap- Sens.Environ.306,114107.https://doi.org/10.1016/j.rse.2024.114107.
basedLandsatdatastructuresforuseinforestdisturbancedetection.RemoteSens. Puhm,M.,Deutscher,J.,Hirschmugl,M.,Wimmer,A.,Schmitt,U.,Schardt,M.,2020.
Environ.97,301–310.https://doi.org/10.1016/j.rse.2005.05.009. Anearreal-timemethodforForestchangedetectionbasedonastructuraltimeseries
Hijmans,R.J.,2023.Terra:SpatialDataAnalysis. modelandtheKalmanfilter.RemoteSens.12,3135.https://doi.org/10.3390/
Holzwarth,S.,Thonfeld,F.,Abdullahi,S.,Asam,S.,DaPonteCanova,E.,Gessner,U., rs12193135.
Huth,J.,Kraus,T.,Leutner,B.,Kuenzer,C.,2020.Earthobservationbased RCoreTeam,2023.R:ALanguageandEnvironmentforStatisticalComputing.
monitoringofforestsinGermany:areview.RemoteSens.12,3570.https://doi.org/ Reinermann,S.,Gessner,U.,Asam,S.,Kuenzer,C.,Dech,S.,2019.Theeffectofdroughts
10.3390/rs12213570. onvegetationconditioninGermany:ananalysisbasedontwodecadesofsatellite
Holzwarth,S.,Thonfeld,F.,Kacic,P.,Abdullahi,S.,Asam,S.,Coleman,K.,Eisfelder,C., earthobservationtimeseriesandcropyieldstatistics.RemoteSens.11,1783.
Gessner,U.,Huth,J.,Kraus,T.,Shatto,C.,Wessel,B.,Kuenzer,C.,2023.Earth- https://doi.org/10.3390/rs11151783.
observation-basedmonitoringofforestsinGermany—recentProgressandresearch Rock,B.N.,1985.Fieldandairbornespectralcharacterizationofsuspectedacid
Frontiers:areview.RemoteSens.15,4234.https://doi.org/10.3390/rs15174234. depositiondamageinredspruce(Picearubens)fromVermont.In:Proc.Symp.On
Ionita,M.,Nagavciuc,V.,2021.ChangesindroughtfeaturesattheEuropeanlevelover MachineProcessingRemotelySensedData,pp.71–81.
thelast120years.Nat.HazardsEarthSyst.Sci.21,1685–1701.https://doi.org/ Rodman,K.C.,Andrus,R.A.,Veblen,T.T.,Hart,S.J.,2021.Disturbancedetectionin
10.5194/nhess-21-1685-2021. landsattimeseriesisinfluencedbytreemortalityagentandseverity,notbyprior
Iwana,B.K.,Uchida,S.,2020.TimeSeriesDataAugmentationforNeuralNetworksby disturbance.RemoteSens.Environ.254,112244.
TimeWarpingwithaDiscriminativeTeacher. Schiefer,F.,Schmidtlein,S.,Frick,A.,Frey,J.,Klinke,R.,Zielewska-Büttner,K.,
Jawahar,G.,Sagot,B.,Seddah,D.,2019.WhatdoesBERTlearnaboutthestructureof Junttila,S.,Uhl,A.,Kattenborn,T.,2023.UAV-basedreferencedataforthe
language?.In:Proceedingsofthe57thAnnualMeetingoftheAssociationfor predictionoffractionalcoverofstandingdeadwoodfromsentineltimeseries.ISPRS
ComputationalLinguistics.Presentedattheproceedingsofthe57thAnnualMeeting
14

C.Schilleretal. Remote Sensing of Environment 315 (2024) 114475
OpenJ.Photogramme.RemoteSens.8,100034.https://doi.org/10.1016/j. Verbesselt,J.,Hyndman,R.,Newnham,G.,Culvenor,D.,2010.Detectingtrendand
ophoto.2023.100034. seasonalchangesinsatelliteimagetimeseries.RemoteSens.Environ.114,106–115.
Schwarz,S.,Werner,C.,Fassnacht,F.E.,Ruehr,N.K.,2023.Forestcanopymortality https://doi.org/10.1016/j.rse.2009.08.014.
duringthe2018-2020summerdroughtyearsinCentralEurope:theapplicationofa Verbesselt,J.,Zeileis,A.,Herold,M.,2012.Nearreal-timedisturbancedetectionusing
deeplearningapproachonaerialimagesacrossLuxembourg.Forestr.:Int.J.Forest satelliteimagetimeseries.RemoteSens.Environ.123,98–108.https://doi.org/
Res.97,376–387.https://doi.org/10.1093/forestry/cpad049. 10.1016/j.rse.2012.02.022.
Seidl,R.,Thom,D.,Kautz,M.,Martin-Benito,D.,Peltoniemi,M.,Vacchiano,G.,Wild,J., Wittich,D.,Rottensteiner,F.,Voelsen,M.,Heipke,C.,Müller,S.,2022.Deeplearningfor
Ascoli,D.,Petr,M.,Honkaniemi,J.,Lexer,M.J.,Trotsiuk,V.,Mairota,P., thedetectionofearlysignsforForestdamagebasedonsatelliteimagery.ISPRSAnn.
Svoboda,M.,Fabrika,M.,Nagel,T.A.,Reyer,C.P.O.,2017.Forestdisturbances Photogramm.RemoteSens.Spatial.Inf.Sci.V-2–2022,307–315.https://doi.org/
underclimatechange.Nat.Clim.Chang.7,395–402.https://doi.org/10.1038/ 10.5194/isprs-annals-V-2-2022-307-2022.
nclimate3303. Ye,S.,Rogan,J.,Zhu,Z.,Hawbaker,T.J.,Hart,S.J.,Andrus,R.A.,Meddens,A.J.H.,
Senf,C.,Seidl,R.,2020.MappingtheforestdisturbanceregimesofEurope.Nat.Sustain. Hicke,J.A.,Eastman,J.R.,Kulakowski,D.,2021.Detectingsubtlechangefromdense
4,63–70.https://doi.org/10.1038/s41893-020-00609-y. Landsattimeseries:casestudiesofmountainpinebeetleandsprucebeetle
Senf,C.,Seidl,R.,2021.Persistentimpactsofthe2018droughtonforestdisturbance disturbance.RemoteSens.Environ.263,112560.https://doi.org/10.1016/j.
regimesinEurope.Biogeosciences18,5223–5230.https://doi.org/10.5194/bg-18- rse.2021.112560.
5223-2021. Yuan,Y.,Lin,L.,2021.Self-supervisedPretrainingoftransformersforsatelliteimage
Senf,C.,Seidl,R.,Hostert,P.,2017.Remotesensingofforestinsectdisturbances:current timeseriesclassification.IEEEJ.Sel.Top.Appl.EarthObservat.RemoteSens.14,
stateandfuturedirections.Int.J.Appl.EarthObs.Geoinf.60,49–60.https://doi. 474–487.https://doi.org/10.1109/JSTARS.2020.3036602.
org/10.1016/j.jag.2017.04.004. Yuan,Y.,Lin,L.,Liu,Q.,Hang,R.,Zhou,Z.-G.,2022.SITS-former:apre-trainedspatio-
S ˇ tursov´a,M.,S ˇ najdr,J.,Cajthaml,T.,B´arta,J.,S ˇ antrůˇckova´,H.,Baldrian,P.,2014. spectral-temporalrepresentationmodelforSentinel-2timeseriesclassification.Int.
Whentheforestdies:theresponseofforestsoilfungitoabarkbeetle-inducedtree J.Appl.EarthObs.Geoinf.106,102651.https://doi.org/10.1016/j.
dieback.ISMEJ.8,1920–1931.https://doi.org/10.1038/ismej.2014.37. jag.2021.102651.
Sundararajan,M.,Taly,A.,Yan,Q.,2017.AxiomaticAttributionforDeepNetworks. Zhang,H.K.,Luo,D.,Li,Z.,2024.Classifyingrawirregulartimeseries(CRIT)forlarge
Thom,D.,Rammer,W.,Seidl,R.,2017.Theimpactoffutureforestdynamicsonclimate: arealandcovermappingbyadaptingtransformermodel.Sci.RemoteSens.9,
interactiveeffectsofchangingvegetationanddisturbanceregimes.Ecol.Monogr. 100123.https://doi.org/10.1016/j.srs.2024.100123.
87,665–684.https://doi.org/10.1002/ecm.1272. Zhu,Z.,Woodcock,C.E.,2014.Continuouschangedetectionandclassificationofland
Thonfeld,F.,Gessner,U.,Holzwarth,S.,Kriese,J.,2022.AFirstAssessmentofCanopy coverusingallavailableLandsatdata.RemoteSens.Environ.144,152–171.https://
CoverLossinGermany’sForestsafterthe2018–2020DroughtYears,19. doi.org/10.1016/j.rse.2014.01.011.
Tucker,C.J.,1979.Redandphotographicinfraredlinearcombinationsformonitoring Zhu,Z.,Zhang,J.,Yang,Z.,Aljaddani,A.H.,Cohen,W.B.,Qiu,S.,Zhou,C.,2020.
vegetation.RemoteSens.Environ.8,127–150. ContinuousmonitoringoflanddisturbancebasedonLandsattimeseries.Remote
VanRossum,G.,Drake,F.L.,2009.Python3ReferenceManual. Sens.Environ.238,111116.https://doi.org/10.1016/j.rse.2019.03.009.
Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,Ł.,
Polosukhin,I.,2017.AttentionIsallyouNeed.
15