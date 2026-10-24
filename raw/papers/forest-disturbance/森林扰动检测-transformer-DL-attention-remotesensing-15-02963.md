remote sensing
Article
A Combined Deep Learning and Prior Knowledge Constraint
Approach for Large-Scale Forest Disturbance Detection Using
Time Series Remote Sensing Data
BingDu1,2,3,ZhanliangYuan3,YanchenBo1,2,* andYushaZhang1,2
1 StateKeyLaboratoryofRemoteSensingScience,FacultyofGeographicalScience,BeijingNormalUniversity,
Beijing100875,China;zhangyusha@mail.bnu.edu.cn(Y.Z.)
2 BeijingEngineeringResearchCenterforGlobalLandRemoteSensingProducts,InstituteofRemoteSensing
ScienceandEngineering,FacultyofGeographicalScience,BeijingNormalUniversity,Beijing100875,China
3 SchoolofSurveyingandLandInformationEngineering,HenanPolytechnicUniversity,Jiaozuo454000,China;
yuan6400@hpu.edu.cn
* Correspondence:boyc@bnu.edu.cn
Abstract:Thescaleandseverityofforestdisturbancesacrosstheglobeareincreasingduetoclimate
changeandhumanactivities.Remotesensinganalysisusingtimeseriesdataisapowerfulapproach
fordetectinglarge-scaleforestdisturbancesanddescribingdetailedforestdynamics.Variouslarge-
scaleforestdisturbancedetectionalgorithmshavebeenproposed,butmostofthemareonlysuitable
fordetectinghigh-magnitudeforestdisturbances(e.g.,fire,harvest).Conversely,morecontinuous,
subtle,andgraduallower-magnitudeforestdisturbances(e.g.,thinning,pests,anddiseases)have
beensubjecttolessfocus.Deeplearning(DL)candistinguishsubtledifferencesininformationwithin
timeseriesdata,offeringnewopportunitiestocaptureforestdisturbancesinacompleteanddetailed
way.Thisstudyproposesanapproachforanalyzingforestdynamicsacrosslargeareasandlongtime
periodsbycombiningDLtimeseriesclassificationandpriorknowledgeconstraint.Theapproach
consistsoftwostages: (1)animprovedself-attentionmodelusedfortimeseriesclassificationto
identifysequenceswithforestdisturbancecharacteristics;(2)developedskip-disturbancerecovery
Citation:Du,B.;Yuan,Z.;Bo,Y.; index(S-DRI)characterizingthetemporalcontext,usingpriorknowledgeconstrainttoidentifyforest
Zhang,Y.ACombinedDeep disturbanceyearsintimeserieswithdisturbancecharacteristics. Inthisstudy,theyearofforest
LearningandPriorKnowledge disturbancesinfivestudyareaslocatedintheUnitedStates,Canada,andPolandfrom2001to2020
ConstraintApproachforLarge-Scale wasmapped.Atotalof3082manuallyinterpretedtestdatawithdifferentdisturbancecausalagents
ForestDisturbanceDetectionUsing
(suchasfire,harvest,conversion,hurricane,andpests)weresampledfromfiveresearchareasfor
TimeSeriesRemoteSensingData.
validation. Ourapproachwasalsoevaluatedagainsttwoforestdisturbancebenchmarkdatasets
RemoteSens.2023,15,2963. https://
derivedfromLandTrendrandtheGlobalForestChange(GFC)dataset. Theresultsdemonstrate
doi.org/10.3390/rs15122963
thatourapproachachievedanoverallaccuracyof87.8%,surpassingtheaccuracyofLandTrendr
AcademicEditors:NingLu,LeYu, (84.6%)andtheGlobalForestChangedataset(81.4%). Furthermore,ourapproachdemonstrated
HouJiangandWenliangLi loweromissionrates(rangingfrom10.0%to67.4%)indetectingsubtletoseverecausalagentsof
forestdisturbance,incomparisontoLandTrendr(witharangeof18.0%to81.6%)andGFC(with
Received:18April2023
Revised:28May2023 arangeof15.0%to88.8%). Thisstudy,whichinvolvedmappinglarge-scaleandlong-termforest
Accepted:31May2023 disturbanceinmultipleregions,revealedthatourapproachcanbeappliedtonewareaswithout
Published:7June2023 arequirementforcomplexparameteradjustments.Theseresultsdemonstratethepotentialofour
approachingeneratingcomprehensiveanddetailedforestdisturbancedata,thusprovidinganew
andeffectivemethodinthisdomain.
Copyright: © 2023 by the authors.
Keywords:forestdisturbance;remotesensing;timeseries;deeplearning;knowledgeconstraint
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditionsoftheCreativeCommons
Attribution(CCBY)license(https://
creativecommons.org/licenses/by/
4.0/).
RemoteSens.2023,15,2963.https://doi.org/10.3390/rs15122963 https://www.mdpi.com/journal/remotesensing

RemoteSens.2023,15,2963 2of23
1. Introduction
Thereisgrowingevidencethatmoreintenseforestdisturbanceeventshavebecome
morefrequentinrecentdecades,posingsignificantchallengestobiologicalhabitatsand
ecological sustainability [1–3]. Natural disturbances, such as fire, drought, hurricanes,
etc.,alongsidehumanactivities,suchasdeforestation,urbanization,andagriculturalland
reclamation, significantly impact the composition, structure, and function of the forest
system. These disturbance events release massive amounts of carbon stored in forest
vegetationintotheatmospherewhilealsodisruptingforestoxygen-releasefunctions[4,5].
Forestdisturbancescancausepermanentalterationsinforestfunctionswithconsiderable
effectsontheglobalforestcarbonbudgetandothervitalecosystemservices,includingthe
watercycleandenergybalance[6,7]. Thereisanurgentneedforretrospectiveanalysis
andcompilationofbasicdataonforestdisturbance,whichwillfacilitatethedevelopment
ofsustainableforestconservationpoliciesandmitigatetheincreaseincarbonemissions
generatedbytheforestdisturbance.
Detectingandcharacterizingchangeovertimeisthenaturalfirststeptowardidentify-
ingthedriverofthechangeandunderstandingthechangemechanism[8]. Remotesensing
data have long been used for forest cover research as they capture natural and anthro-
pogenicactivitiesonabroadspatialscaleandhavenaturaltemporalproperties[9–11]. The
LandsatArchivesprovidealong-term,large-scalecollectionofsatelliteimagesinstandard
formatthatcanbeusedonalargescaletodetectchangescausedbyforestdisturbance[12].
In2008,freeandopenaccesstoallLandsatarchivescontinuedtorevolutionizetheuseof
Landsatdata[13]. TheuseofLandsattimeseriesanalysisandextractionofspectraltrajec-
toryfeaturesisamainstreammethodforcurrentsystematicforestdisturbancemonitoring,
withsignificantprogress[8,14–20].
ManyforestdisturbancedetectionandLandsat-basedchangedetectionalgorithms
basedontimeseriesremotesensingdatahavebeendevelopedandwidelyused. Among
them,thethresholdmethod(e.g.,VCT),trajectoryfittingmethod(e.g.,CCDC),andtrajec-
torysegmentationmethod(e.g.,LandTrendr)arethemostoftenusedmethodsforforest
disturbancedetection[13,15,16]. Thesemethodshavebeenproventobeeffectiveindetect-
ingforestdisturbances,butthereliabilitiesoftendependontheseverityofthedisturbance
eventsthemselves[21]. Ideally,forestdisturbancehassignificanttimeseriesvariability
characteristicsthataresufficienttopassafixedthresholdfordetection[18]. However,data
gapsandnoiseduetoclouds,snow,orsatellitesystemfailuresstillmakeitchallengingto
extractreliablechangesfromtheremotesensingtimeseries[22–24]. Thespectralresponse
tonon-standreplacementdisturbanceissubtleanddelayed;therefore,somealgorithms
tendnottoconsiderdetectingnon-standreplacementdisturbanceortakeaconservative
approachtoavoiderrorsduetofactors,suchasdatanoiseandphenologicalchanges. Most
productsormethodsusedfordetectingforestdisturbancearesensitivetosuddenandrapid
standreplacementdisturbances(e.g.,harvest,fire)butineffectivefordetectingnon-stand
replacingdisturbances(e.g.,insectpests,drought)thatpersistovermanyyearsandchange
gradually[21,25,26]. Thegoalofforestmanagementistomitigateoradapttotheimpacts
ofconstantlychangingdisturbanceconditions,andsubtlelong-termdisturbancesoften
leadtomorevariedstandstructures,whichalsoneedtobeaddressed[27]. Therefore,new
methods are needed to comprehensively and accurately detect forest disturbances, not
solelyrelyingontheseverityofthedisturbanceeventsthemselves.
DL is powerful in modeling and learning capabilities and can extract information
about real-world changes from remote sensing data [28]. Current studies using DL for
forestdisturbancedetectionaremainlybasedoncomputervisiontechniques,whichdonot
capturelong-termforestdynamicsinformation. Mostofthestudieshavebeenevaluated
withlittlereferencedatafromasmallareaandonlyforsingledisturbancecausalagent
detection,whichlimitsthetransferabilityoftheproposedapproaches[29,30]. Inremote
sensing,thedetectionofforestdisturbancesisinherentlydifficultbecauselow-magnitude
andverysmallsizedisturbanceimagetexturesarenotobvious,similartootherbackground
noise[31].

RemoteSens.2023,15,2963 3of23
DLiswelladaptedtocomplexspatialandtemporalpatternsandhastheabilityto
detectanddifferentiatelandcoverwithverysimilarspectralcharacteristics[32,33]. Using
timeseriesremotesensingdatacanprovidedynamicchangeinformationoftheEarth’s
surface. In recent years, DL-based time series classification models have been used to
obtainperiodicinformationonvegetationdynamics, mowingfrequency, landuse, and
otherlandsurfacechangeinformationfromremotesensingdata,suchasconvolutional
neuralnetwork(CNN),longshort-termmemory(LSTM),andrecurrentneuralnetwork
(RNN)[34–37]. Thetransformerwasfirstproposedforapplicationsinnaturallanguage
processing[38]. Ithasbeenusedinotherareas, suchascomputervisionandsequence
generation,duetoitsefficientperformance,demonstratingitsadvances[38–40]. Inrecent
studies,thetransformerhasbeenusedfortimeseriespredictionandclassification,showing
superior performance on multiple datasets [41,42]. In contrast to RNN and CNN, the
self-attention mechanism of the transformer allows neural networks to extract features
fromobservationsatspecifictimestepsoftheinputtimeseriesofvalues[42]. Rußwurm
etal.[43]comparedsixDLmodelsbasedonSentinel-2rawandpre-processeddatafor
crop-type classification, showing better performance for self-attention neural networks
thantheCNN.
Freeopenaccesstodataandincreasedcomputingpowersolvethelimitedavailability
of the excessive computational demand for temporal stacks of large-scale satellite im-
ages[44,45]. Numerousstudieshaveshownthattheuseoftimedependenceandspectral
change is more suitable for forest disturbance detection [13,31]. However, the inherent
variability,dropouts,andextraneousdatapresentinremotesensingtimeseriesdatapose
significantchallengesinachievingend-to-endforestdisturbancedetectionusingDL[46].
Iftheremotesensingtimeseriescanbealignedandtrimmedtoequivalentlengths,itis
possibletouseDLtimeseriesclassificationtodistinguishbetweenlow-magnitudedistur-
bancesandspectralchangescausedbynoise[46]. DLcanidentifyasequenceofforest
disturbanceevents,andtheexacttimingoftheforestdisturbancecanbedeterminedby
utilizing simpler statistical methods or relying on prior knowledge of the disturbance
timespresentwithinthesequence. Priorknowledgeconstraintsintegratelogicalrulesinto
deeplearningmodels,encodehumanintentionsanddomainknowledgeintothemodel
tocontroltheoutputresults,andavoidheavyrelianceonlargeamountsoflabeleddata
fortraining[47]. Forestdisturbancecanbeconsideredatime-varyingprocessthatcanbe
effectivelymonitoredthroughtimeseriesanalysisandcharacteristicsextraction[48]. Based
on the time-varying characteristics of forest disturbances, integrating prior knowledge
constraintsintodeeplearningtimeseriesclassificationmodelstodetectforestdisturbances
canavoidtop-downapproachestoeliminatenoise-inducedvariationandfocusmoreon
lower-magnitudedisturbances.
Inthispaper,weproposedaforestdisturbancedetectionmodelthatcombinesDL
classification and prior knowledge constraints to achieve comprehensive and accurate
detection of forest disturbances using time series remote sensing data. The proposed
approachinvolvesatwo-phaseprocessformappingforestdisturbance: (1)Useamoving
windowalgorithmtoalignandsegmentremotesensingtimeseries; then, classifytime
seriesbasedonDLtopinpointthetimewindowwherethedisturbanceeventoccurred.
(2) Define and apply the prior knowledge constraints to locate the specific year of the
disturbanceeventintheidentifiedwindow. Weillustratedtheeffectivenessofourmodel
byanalyzingtimeseriesLandsatimagesspanningtwodecades(2001to2020)andtesting
onforestsinstudyareaslocatedinOregon,WestVirginia,Montana,Alberta,andPoland.
Inaddition,ourapproachiscomparedwithresultsfromtheLandTrendrandGFCdataset
andexplorestheomissionofthedifferentforestdisturbancecausalagentclasses.

| Remote Sens. 2023, 15, x FOR PEER REVIEW  |     |     |     |     |     | 4 of 24  |
| ----------------------------------------- | --- | --- | --- | --- | --- | -------- |

2. Materials and Methods
2.1. Study Area
Natural disasters, climate change, and land use change are interrelated, and different
regions have different spatial and temporal disturbance patterns and dominant disturb-
ance causal agents. To comprehensively evaluate the performance of the forest disturb-
ance detection approach in different environments, five regions located in North America
and Europe were selected as the study areas for this study, as shown in Figure 1. There
are diverse forest types and disturbance causal agents in the selected study areas. Most of
the study areas are covered by forest and vary greatly in elevation, climate, forest popu-
lations, and disturbance causal agents. The area, forest cover, elevation, and major species
of trees and the disturbance causal agents of each study area are summarized in Table 1
[25,49].
Table 1. Description of area, forest cover, elevation, forest species groups, and disturbance causal
agents in study area.
RemoteSens.2023,15,2963 4of23
Disturbance Causal
  Study Area  Area (ha)  Forest (%)  Elevation (m)  Forest Species Groups
Agents
|     |     |     |     |     | Douglas fir, Ponderosa  Harvest, Fire, Thin- |     |
| --- | --- | --- | --- | --- | -------------------------------------------- | --- |
2. MaterialsandMethods
| 1  Oregon, USA  |     | 1,468,571      | 88.3  | −17~1915  |                          |       |
| --------------- | --- | -------------- | ----- | --------- | ------------------------ | ----- |
|                 |     | 2.1. StudyArea |       |           | pine, Western red cedar  | ning  |
Naturaldisasters,climatechange,andReladn pdinues,e Ycehlalonwge pairneei,n  tePreresltas taendd,a dnidsedaisfefes,r ent
| 2  Montana, USA  |     | 526,423  | 61.1  | 368~3376  |     |     |
| ---------------- | --- | -------- | ----- | --------- | --- | --- |
regionshavedifferentspatialandtemporalCdihsitnuersbea npcineep,a Stpterruncsea nddomiHnaanrvtedsits turbance
West Virginia,  causal agents. To comprehensively evaluTaotercthh epipneer, fSohrmorat-nlecaef of thMeinfoinregs,t Hdaisrvtuersbt,a nce
| 3   |     | 2,932,182  | 90.3  | 164~1433  |     |     |
| --- | --- | ---------- | ----- | --------- | --- | --- |
USA  detectionapproachindifferentenvironmpeinntes,, Wfivheitree pgiinone,s Slpocruatceed  inNoTrhthinAnimnge ricaand
EuropewereselectedasthestudyareasfAosrptehnis psotupdlayr,, aBsalsshaomw niFnirFei,g Murinei1n.gT, Hhearre- are
| 4  Alberta, Canada  |     | 2,492,891  | 92.7  | 217~866  |     |     |
| ------------------- | --- | ---------- | ----- | -------- | --- | --- |
diverseforesttypesanddisturbancecausalpagoepnlatsr,i Pnatpheers beilrecchte dstudyarevaess.tM  ostofthe
studyareasarecoveredbyforestandvarygreatlyinelevation,climate,forestpopulations,
5  Poland  2,009,051  35.8  −8~289  Pine, Birch, Poplar  Hurricanes, Harvest
anddisturbancecausalagents. Thearea,forestcover,elevation,andmajorspeciesoftrees
andthedisturbancecausalagentsofeachstudyareaaresummarizedinTable1[25,49].

Figure1.Anillustrationofthestudyareaandthespatialdistributionoftrainingdataandtestdata.
Figure 1. An illustration of the study area and the spatial distribution of training data and test data.
Forestcoverinthestudyareaisrepresentedbytreecanopyheight[50].
Forest cover in the study area is represented by tree canopy height [50].
Table1. Descriptionofarea,forestcover,elevation,forestspeciesgroups,anddisturbancecausal
2.2. Data and Pre-Processing
agentsinstudyarea.
2.2.1. Landsat Imageries and Spectral Indices
In this study, remote sensing time series were created using Landsat imDagisetruirebsa fnrcoem
StudyArea Area(ha) Forest(%) Elevation(m) ForestSpeciesGroups
three sensors, namely Landsat 5 TM, Landsat 7 ETM+, and Landsat 8 OLI. WCea uustiallizAegde nthtse
|                    |                |           |      |          | Douglasfir,Ponderosa      | Harvest,Fire,    |
| ------------------ | -------------- | --------- | ---- | -------- | ------------------------- | ---------------- |
| 1                  | Oregon,USA     | 1,468,571 | 88.3 | −17~1915 |                           |                  |
|                    |                |           |      |          | pine,Westernredcedar      | Thinning         |
|                    |                |           |      |          | Redpine,Yellowpine,       | Pestsand         |
| 2                  | Montana,USA    | 526,423   | 61.1 | 368~3376 |                           |                  |
|                    |                |           |      |          | Chinesepine,Spruce        | diseases,Harvest |
|                    |                |           |      |          | Torchpine,Short-leafpine, | Mining,Harvest,  |
| 3 WestVirginia,USA |                | 2,932,182 | 90.3 | 164~1433 |                           |                  |
|                    |                |           |      |          | Whitepine,Spruce          | Thinning         |
|                    |                |           |      |          | Aspenpoplar,Balsam        | Fire,Mining,     |
| 4                  | Alberta,Canada | 2,492,891 | 92.7 | 217~866  |                           |                  |
|                    |                |           |      |          | poplar,Paperbirch         | Harvest          |
Hurricanes,
| 5   | Poland | 2,009,051 | 35.8 | −8~289 | Pine,Birch,Poplar |     |
| --- | ------ | --------- | ---- | ------ | ----------------- | --- |
Harvest
2.2. DataandPre-Processing
2.2.1. LandsatImageriesandSpectralIndices
Inthisstudy,remotesensingtimeserieswerecreatedusingLandsatimageriesfrom
threesensors,namelyLandsat5TM,Landsat7ETM+,andLandsat8OLI.Weutilizedthe
bestavailablepixel(BAP)algorithmtoproducecontinuous,cloud-free,andphenological
consistentimagecomposites[51]. TheBAPalgorithmusestheLandsatEcosystemDistur-
banceAdaptiveProcessingSystem(LEDAPS)algorithmtogeneratesurfacereflectance

RemoteSens.2023,15,2963 5of23
valuesforthesixLandsatopticalbands. Cloudsandtheirshadowsweredetectedand
maskedusingthefunctionofmask(Fmask)algorithm[52–54]. TheBAPalgorithmcal-
culatesfourseparatescoresforeachpixel: thesensorscore, theacquisitiondayofyear
score,thedistancetocloudorcloudshadowscore,andtheatmosphericopacityscore. All
scoresweresummedtoprovideatotalscoreforeachpixel,andthepixelwiththehighest
scorewasusedintheimagecomposite. DetailsonthepixelscoringrulesandannualBAP
developmentcanbefoundinWhiteetal.[51]. Inthisstudy,themaximumcloudcoverin
theLandsatscenesusedwassettobebelow70%,themaximumatmosphericopacitywas
0.3,andtheminimumatmosphericopacitywas0.2. Giventhatallstudyareasaresituated
in mid-latitudes of the Northern Hemisphere, the annual acquisition day of year score
selectstheclosestdaytoAugust1asthefirstclearpixel,with±30daysfromthedesignated
targetdayoftheyear. ThisstudyusedBAPtoproduceannualcompositeimagesforfive
TSAsfrom2000to2020.
For the forest not being disturbed, the canopy closure is relatively high with low
shortwave-infraredreflectance(SWIR).Afterthedisturbance,thebaresoilandlowvegeta-
tionincreasedthereflectanceofSWIRinthearea[55,56]. Duetothesuperiorperformance
ofSWIRinindicatingvegetationchange,spectralindicesinvolvingSWIR,suchasnormal-
izedburnratio(NBR)andnormalizeddifferencevegetationindex(NDVI),werewidely
usedindetectingforestdisturbance[7,26,57,58]. NumerousstudieshaveshownthatNBR
respondssignificantlytoforestchangeandissuitablefordetectingtheoccurrenceofforest
disturbance[16,23,26,59]. Inthisstudy,theNBRspectralindexwasusedtoconstructtime
seriesfordetectingpixel-levelforestdisturbance.
2.2.2. ReferenceData
ItisnecessarytocollectsufficientdatafortrainingtheDLmodel. Forestdisturbance
isarareevent,withanaveragefrequencyof1in1000yearspertreeexperiencingstand
replacement disturbance, and collecting manually interpreted training data is a labor-
intensiveexercise[60]. Wedesignedamethodforobtainingreferencedata. First,aclassifier
was trained to distinguish between forest and non-forest areas. Then, sampling points
wererandomlygeneratedintheforestareas,withaminimumdistanceof3kmbetween
two points to avoid spatial autocorrelation issues [1]. Manual interpretation based on
high-resolution images and Landsat time series was conducted to determine the forest
disturbancehistoryforallsamplesandexcludesamplesthatfelloutsideofforests.
Thecollectedreferencedataincludetrainingdatasetsfortheself-attentionmodelfor
trainingandvalidationandatestdatasetforevaluatingtheforestdisturbancedetection
approach. Figure1showsatotalof18,240referencedatapoints(bluepoints)collectedfor
trainingthetimeseriesclassifier,ofwhich45%experiencedatleastonedisturbancebetween
1988and2019. ThetrainingdatasetsforNorthAmericaandAsiaweregeneratedusing
theaforementionedprocess, andtheEuropeandatasetwasprovidedbySenfetal.[61].
The study area in this study does not include the training data. To evaluate the model
performance,3082referencesamples(redpoints)werecollectedfromthe5studyareas
asthetestdataset. Between2001and2020,2047forestpixelsremainedunchangedand
1035pixelsexperienceddisturbances. Thedisturbancetimeandthedisturbancecausal
agentclassesofthetestdatawerelabeledbyvisuallyinterpretingthetimeseriesofLandsat
imagesandthepubliclyavailablemedium-tohigh-resolutionimages. Figure2showsthe
distributionofthenumberofdisturbancecausalagentsforthetestdataineachstudyarea.
AdescriptionofthedisturbancecausalagentclassesisshowninTableA1.

Remote Sens. 2023, 15, x FOR PEER REVIEW 6 of 24
RReemmoottee SSeennss.. 22002233,, 1155,, 2x9 6F3OR PEER REVIEW 66 ooff 2234
Figure 2. Forest disturbance causal agent classes in test data.
2.3. Forest Disturbance Detection Model
To detect the annual forest disturbance using Landsat time series data, a two-stage
forest disturbance detection approach, consisting of DL time series classification and prior
knowledge constraint, was proposed in this study (Figure 3) . In the first stage, we apply
thFFieigg uumrreeo 2v2..i nFFogorr eewsstti dndidisstotuuwrrbb aaannlcgceeo crcaiatuuhssmaall aatggoee nnstte ccgllamassseseensst i innth tteeess ttt didmaatteaa .. series into multiple window se-
quences, where each window sequence corresponds to a specific time period for a given
2.3. ForestDisturbanceDetectionModel
p2ix.3e.l .F Worees tt hDeins tuusreb aan ctrea Dineetedc tsieolnf -Mattoednelt ion model to classify each window sequence, indi-
catingT wohdeettheectr tthhee saenqnuueanlcfeo creosnttadiinsstu ar fboarnecset duissitnugrbLaanncde seavtetnimt. Tehsee rsieecsodnadt as,taagtew aop-pstlaiegse
To detect the annual forest disturbance using Landsat time series data, a two-stage
forestdisturbancedetectionapproach,consistingofDLtimeseriesclassificationandprior
a prior knowledge constraint to the window sequences containing the disturbance event
forest disturbance detection approach, consisting of DL time series classification and prior
knowledgeconstraint,wasproposedinthisstudy(Figure3). Inthefirststage,weapply
that was identified by the self-attention model in the first stage to determine the specific
knowledge constraint, was proposed in this study (Figure 3). In the first stage, we apply
themovingwindowalgorithmtosegmentthetimeseriesintomultiplewindowsequences,
year of the forest disturbance.
the moving window algorithm to segment the time series into multiple window se-
where each window sequence corresponds to a specific time period for a given pixel.
To facilitate a better understanding of the methods proposed in this study, we de-
quences, where each window sequence corresponds to a specific time period for a given
Wethenuseatrainedself-attentionmodeltoclassifyeachwindowsequence,indicating
fined several concepts. For a given time series Y={Y ,...,Y }, it is a sequential order of
pixel. We then use a trained self-attention model to cl(cid:2868)assify (cid:2930)each window sequence, indi-
whetherthesequencecontainsaforestdisturbanceevent. Thesecondstageappliesaprior
spectral values of a pixel during the detection period. The s sample long sub-signal
cating whether the sequence contains a forest disturbance event. The second stage applies
{
k
Y
n
}
o(cid:2911)(cid:2878)w(cid:2929) l
(
e
0
dg
(cid:3409)
e
a
co
(cid:3407)
ns
a
tr
+
ai
s
n
(cid:3409)
tto
t)
t h
is
e
a
w
w
in
i
d
n
o
d
w
ow
se
s
q
e
u
q
e
u
n
e
c
n
e
c
s
e
c
,
o
w
nt
h
a
e
i
r
n
e
i n
s
g t
r
h
e
e
pr
d
e
i
s
s
e
tu
n
r
ts
b a
th
n
e
ce
m
e
o
v
v
en
e
t
w
th
in
a
d
tw
ow
as
a(cid:2919) p(cid:2919)(cid:2880)ri(cid:2911)or knowledge constraint to the window sequences containing the disturbance event
identifiedbytheself-attentionmodelinthefirststagetodeterminethespecificyearofthe
size. In the remainder of this article, we use the above notation.
that was identified by the self-attention model in the first stage to determine the specific
forestdisturbance.
year of the forest disturbance.
To facilitate a better understanding of the methods proposed in this study, we de-
fined several concepts. For a given time series Y={Y ,...,Y }, it is a sequential order of
(cid:2868) (cid:2930)
spectral values of a pixel during the detection period. The s sample long sub-signal
{Y}(cid:2911)(cid:2878)(cid:2929) (0(cid:3409)a(cid:3407)a+s(cid:3409)t) is a window sequence, where s represents the move window
(cid:2919) (cid:2919)(cid:2880)(cid:2911)
size. In the remainder of this article, we use the above notation.
FFigiguurree 33. .WWoorrkkflflooww sscchheemmee ooff tthhee ffoorreesstt ddiissttuurrbbaannccee ddeetteeccttiioonn..
Tofacilitateabetterunderstandingofthemethodsproposedinthisstudy,wedefined
2.3.1. Padding and Segmentation
several concepts. For a given time series Y = {Y ,...,Y }, it is a sequential order of
0 t
This study involves a time classifier that performs time series classification tasks,
spectral values of a pixel during the detection period. The s sample long sub-signal
w
{
h
Y
ic
}
ha +resq
(
u
0
i
≤
res
a
fi
<
rs
a
t t
+
ra
s
ns
≤
fo
t
r
)
m
is
in
a
g
w
in
in
p
d
u
o
t
w
rem
se
o
q
t
u
e
e
s
n
e
c
n
e
s
,
i
w
ng
h
d
er
a
e
ta
s
o
re
f
p
v
r
a
e
r
s
y
e
in
n
g
ts
l
t
e
h
n
e
g
m
th
o
s
v
in
e
t
w
o fi
in
x
d
e
o
d
w
-
leng
i
th
i=
i
a
nputs for the classifier to use. We used a moving window algorithm to segment
size. Intheremainderofthisarticle,weusetheabovenotation.
thFeig ruerme 3o.t We soernkflsionwg stcihmeem see orfi eths ed faotrae sitn dtois tau rnbuamncbe edre otefc wtioinn.d ow sequences [37]. A key part
2.3.1. PaddingandSegmentation
2.3.1. Padding and Segmentation
This study involves a time classifier that performs time series classification tasks,
whichThreisq usitruedsyfi rinstvtorlavnessf oar mtimineg cinlapsusitfireerm tohtaet spenersfionrgmdsa ttaimoef vsaerryieins gcllaesnsgifithcsatiinotno fitaxsekds-,
lwenhgicthh rineqpuuitrsefso firrtsht etrcalnassfsoifirmerintog uinspe.uWt reemusoeted saenmsoinvgin dgatwa ionfd voawryainlggo lreinthgmthst oinsteog fimxeendt-
tlhenegrtehm iontpeustesn fsoinr gthteim cleassesirfiieesr dtoa tuasien.t oWae nuusmedb ae rmoofvwiningd wowindseoqwu eanlgcoesri[t3h7m]. tAo kseegympeanrtt
othfem rienminogtet ismenessienrgie tsimdaet aseirsietos didaetna tiinfytot hae nmumovbeemr eonf twsiannddo/wo rsceoqmuepnocnees n[3ts7]w. Aith kineyt hpeamrt

Remote Sens. 2023, 15, x FOR PEER REVIEW 7 of 24
of mining time series data is to identify the movements and/or components within them
by segmenting the time series, which can efficiently discover the critical time segments via
the moving window [62]. The moving window algorithm progressively moves the win-
dow within the time detection period of each pixel, creating a new sequence based on the
values that fall into the window at each step (Figure 4a). This new sequence is called a
window sequence. The number of strides refers to the number of steps by which the win-
dow is shifted. The size of the window sequence, i.e., the number of composite images
containing observations in the sequence, controls the amount of information available in
the trajectory [37]. The window sequence corresponded to a period of time for a given
forest pixel, and a label indicated whether a disturbance event occurred or not during the
period or not is assigned to that window sequence (Figure 4a). In this study, we tested the
window sizes of 7, 9, and 11 progressively to explore the effect of window size on the
recognition of a window sequence. To improve the efficiency of the model operation, mov-
RemoteSens.2023,15,2963 7of23
ing window sizes of 7, 9, and 11 use strides of 2, 2, and 4, respectively.
For forest disturbance detection, an ideal window sequence should contain the pre-
disturbance forest features and the post-disturbance recovery features (as shown in Figure
bysegmentingthetimeseries,whichcanefficientlydiscoverthecriticaltimesegments
4aⅡ). For better detection of early or late disturbance events within the detection period,
via the moving window [62]. The moving window algorithm progressively moves the
before segmenting time series with a moving window, padding was applied using the
windowwithinthetimedetectionperiodofeachpixel,creatinganewsequencebasedon
shifting method to reduce information loss at the edges of the time series, as shown in
thevaluesthatfallintothewindowateachstep(Figure4a). Thisnewsequenceiscalled
Figure 4b. Specifically, the padding operation simulates forest time series information (for
awindowsequence. Thenumberofstridesreferstothenumberofstepsbywhichthe
example, in Figure 4b, we observed that the window sequence with padding operation
windowisshifted. Thesizeofthewindowsequence,i.e.,thenumberofcompositeimages
has trajectories similar to the raw spectral values) and ensures that disturbance events
containingobservationsinthesequence,controlstheamountofinformationavailablein
within the detection period are included in the created window sequence with sufficient
thetrajectory[37]. Thewindowsequencecorrespondedtoaperiodoftimeforagiven
information, thereby improving the accuracy of time series classification models [63]. In
forestpixel,andalabelindicatedwhetheradisturbanceeventoccurredornotduringthe
this study, we performed ⌊s/2⌋ times padding on the edges of the time series using 𝑌
periodornotisassignedtothatwindowsequence(Figure4a). Inthisstudy, wetested(cid:2868)
and 𝑌, respectively. For example, in Figure 4b, when using the moving window of size 9,
the wi(cid:3047)ndow sizes of 7, 9, and 11 progressively to explore the effect of window size on
the edges of the time series were padded four times using the NBR values of 2000 and
therecognitionofawindowsequence. Toimprovetheefficiencyofthemodeloperation,
2020, respectively.
movingwindowsizesof7,9,and11usestridesof2,2,and4,respectively.
FFiigguurree 44.. SScchheemmaattiicc ddiiaaggrraamm ooff tthhee mmoovviinngg wwiinnddooww aanndd ppaaddddiinngg ooppeerraattiioonn.. ((aa)) EExxaammppllee ooff mmoovviinngg
wwiinnddooww aallggoorriitthhmm aapppplilcicaatitoionn. .FoFroerset sdtidstiustrubrabnacne coeccoucrcruerdr eidn 2in00280. 0T8h.e Trehde preadrt preaprtrerseepnrtess ae nwtsina-
wdoinwd. oTwh.e Twhiendwoiwnd soiwze siisz 9e aisn9d athned stthreidset rsiidzee sisiz 2e. i(sb2) .A(nb )eAxanmepxlaem opf lpeaodfdpinadg doipnegraotpioenra. tTiohne. wTihne-
dows with the same color represent similar trajectory features.
windowswiththesamecolorrepresentsimilartrajectoryfeatures.
For forest disturbance detection, an ideal window sequence should contain the
pre-disturbanceforestfeaturesandthepost-disturbancerecoveryfeatures(asshownin
Figure4aII). Forbetterdetectionofearlyorlatedisturbanceeventswithinthedetection
period,beforesegmentingtimeserieswithamovingwindow,paddingwasappliedusing
theshiftingmethodtoreduceinformationlossattheedgesofthetimeseries,asshown
inFigure4b. Specifically,thepaddingoperationsimulatesforesttimeseriesinformation
(forexample,inFigure4b,weobservedthatthewindowsequencewithpaddingoperation
has trajectories similar to the raw spectral values) and ensures that disturbance events
withinthedetectionperiodareincludedinthecreatedwindowsequencewithsufficient
information,therebyimprovingtheaccuracyoftimeseriesclassificationmodels[63]. In
this study, we performed (cid:98)s/2(cid:99) times padding on the edges of the time series usingY
0
andY,respectively. Forexample,inFigure4b,whenusingthemovingwindowofsize
t
9,theedgesofthetimeserieswerepaddedfourtimesusingtheNBRvaluesof2000and
2020,respectively.
2.3.2. Self-AttentionModel
Inthisstudy,aself-attentionmechanisminthetransformermodelisusedfortime
seriesclassification[38]. LetX = {x , x ,..., x }betheinputsequenceoflengthn;the
1 2 n

Remote Sens. 2023, 15, x FOR PEER REVIEW 8 of 24
2.3.2. Self-Attention Model
RemoteSens.2023,15,2963 8of23
In this study, a self-attention mechanism in the transformer model is used for time
series classification [38]. Let 𝑋 = {x ,x ,...,x } be the input sequence of length 𝑛; the
(cid:2869) (cid:2870) (cid:3041)
s s e e lf l - f a -a tt tt e e n n t t i i o o n n m m e e c c h h a a n n i i s s m m c c o o m m p p u u t t e e s s t t h h e e k k e e y y 𝐾 K = = 𝑊 W(cid:3038) (cid:3021) T 𝑋 X , q , u q e u r e y r y 𝑄 Q = = 𝑊 (cid:3044) (cid:3021) W 𝑋 T, a X n , d a v n a d lu v e a l 𝑉 ue =
𝑊(cid:3021) 𝑋 vectors originate from the input matrix 𝑋 tra k nsformed by linear q transformation,
V =(cid:3049) WT XvectorsoriginatefromtheinputmatrixXtransformedbylineartransformation,
wherev 𝑊 , 𝑊, and 𝑊 are the learned weight matrices. Attention scores are computed
whereW ,(cid:3038)W ,(cid:3044)andW (cid:3049)arethelearnedweightmatrices. Attentionscoresarecomputed
k q v
between all pairs of positions in the input sequence using the dot product between the
betweenallpairsofpositionsintheinputsequenceusingthedotproductbetweenthe
query and key vectors, followed by softmax activation. The output representation for each
queryandkeyvectors,followedbysoftmaxactivation. Theoutputrepresentationforeach
position in the input sequence is computed as the weighted sum of the value vectors. This
positionintheinputsequenceiscomputedastheweightedsumofthevaluevectors. This
results in the generic formulation of self-attention, as shown in Equation (1).
resultsinthegenericformulationofself-attention,asshowninEquation(1).
𝑄𝐾(cid:3021)
Attention(𝑄,𝐾,𝑉)=softma(cid:18)xQ(cid:4678)KT(cid:19)(cid:4679)𝑉
(1)
Attention(Q,K,V) =softmax √(cid:3493)𝑑 V (1)
(cid:3038)
d
k
where 𝑑 is the dimensionality of the query and key vectors, and the attention scores are
(cid:3038)
whered isthedimensionalityofthequeryandkeyvectors,andtheattentionscoresare
scaled bky√ (cid:3493)𝑑 for better gradient backpropagation.
(cid:3038)
scaledby d forbettergradientbackpropagation.
In this sktudy, the encoder architecture of the transformer network was used [38]. The
In this study, the encoder architecture of the transformer network was used [38].
schematic architecture of the used model is shown in Figure 5. Since the input data are
TheschematicarchitectureoftheusedmodelisshowninFigure5. Sincetheinputdata
continuous time series data, the word embedding step was no longer required. For the
arecontinuoustimeseriesdata,thewordembeddingstepwasnolongerrequired. For
transformer, as a feed-forward architecture that was insensitive to the order of the inputs,
the transformer, as a feed-forward architecture that was insensitive to the order of the
position encoding was added in order to make it aware of the sequential nature of the time
inputs,positionencodingwasaddedinordertomakeitawareofthesequentialnature
series. The time series with location encoding was converted to a higher-dimensional fea-
of the time series. The time series with location encoding was converted to a higher-
ture representation by using a 3-layer transformer encoder block. Each block applies
dimensionalfeaturerepresentationbyusinga3-layertransformerencoderblock.Eachblock
multi-head self-attention and dense layers to each time instance independently and intro-
appliesmulti-headself-attentionanddenselayerstoeachtimeinstanceindependentlyand
duces skip connections and layer normalization for better gradient flow and model stabil-
introducesskipconnectionsandlayernormalizationforbettergradientflowandmodel
ity. The output of the last transformer block is reduced to a single vector of size by apply-
stability. Theoutputofthelasttransformerblockisreducedtoasinglevectorofsizeby
ing global maximum pooling along the time dimension. This reduced representation was
applyingglobalmaximumpoolingalongthetimedimension. Thisreducedrepresentation
then projected to the scores of each class using a final fully connected layer with a softmax
wasthenprojectedtothescoresofeachclassusingafinalfullyconnectedlayerwitha
activation function.
softmaxactivationfunction.
FFigiguurere5 5..S Scchheemmaatitcicd diaiaggrarammo offt hthees seelfl-fa-atttteenntitoionnm mooddeellf oforrt itmimees eserireiessc lcalasssisfiificacatitoionn..
TThhees seelfl-fa-atttteenntitoionnm mooddeellt atakkeess,,a assi ninppuutt,,a as seeqquueenncceec crreeaateteddu ussiningga am moovvininggw wininddooww
algorithm and produces a binary classification result indicating whether there is forest
algorithm and produces a binary classification result indicating whether there is forest
disturbancewithinthewindowsequence. Rußwurmetal.[43]developedaself-attention
disturbance within the window sequence. Rußwurm et al. [43] developed a self-attention
modeltoclassifylandcovertypesusingSentinel-2multispectralimages. Inthisstudy,we
model to classify land cover types using Sentinel-2 multispectral images. In this study, we
improvedtheself-attentionmodelproposedbyRußwurmetal.[43]toidentifywindow
improved the self-attention model proposed by Rußwurm et al. [43] to identify window
sequencescontainingforestdisturbanceevents[38]. Toreducetheriskofoverfittingin
sequences containing forest disturbance events [38]. To reduce the risk of overfitting in
model training, we reduced the dimension of its hidden state D , the number of self-
model training, we reduced the dimension of its hidden state 𝐷h , the number of self-
(cid:3035)
attentionlayersL,andthenumberofself-attentionheadsH. Thefinalmodelparameters
wereL =3,D =128,H =1.
h
Themodelwastrainedandtestedusingthetrainingdataandthetestdatafromthe
referencedataset(Figure1). Forsamplesthatunderwentdisturbances,wesegmentedthem

RemoteSens.2023,15,2963 9of23
usingamovingwindow,obtainedthewindowsequencethatthedisturbanceeventfellinto,
andlabeledasDisturbance. Forundisturbedreferencesamples,amovingwindowisused
tosegmentthetimeseries,andoneoftheresultingwindowsequencesisrandomlyselected
andlabeledasNochange. Onlyonewindowsequencewasselectedforeachreference
sample;wethentrainedthetimeseriesclassifierusingthelabeledwindowsequences. For
modeltraining,wesplittheinputdatasetintothreeparts: training,validation,andtest
data. Thetrainingdatasetwasusedtotrainthemodel,whileaftereachtrainingepoch,the
currentperformancewasevaluatedonthevalidationsettomonitortheconvergenceand
triggerlearningparameterchanges. Thetestdatafortheself-attentionmodelcomefrom
fivestudyareas,andthestrategyforobtainingwindowsequencesandlabelsisconsistent
withthestrategyusedtoobtainwindowsequencesfortraining.
Thelossfunctionusedintheself-attentionmodelisthebinarycross-entropyfunction,
whichhasbeentypicallyusedinneuralnetworksforclassificationtasks[64]. Theopti-
mizationalgorithmusedwasAdam,andthebatchsizewas128[65]. Theinitiallearning
ratewassetto1×10−3,andthelearningratedecaywas1×10−2. Themaximumnumber
oftrainingepochsinthemodelwassetto200. Anearlystoppingmechanismwasimple-
mentedtopreventoverfittingbyendingthetrainingwhenthelossfunctiondidnotchange
for10epochs.
2.3.3. PriorKnowledgeConstraints
Toidentifythespecificyearofaforestdisturbanceoccurringinthewindowssequence
thatcontainsdisturbanceevents,thepriorknowledgepresentingthetemporalchangesin
thespectralindexbeforeandafterdisturbanceeventswasintroduced. Forestdisturbances
in time series data usually coincide with sudden drops in NBR values. While spectral
changescausedbynoisearetemporaryandquicklyreturntonormalvalues,disturbance-
inducedspectralchangesaremorepersistentandlastforseveralyears,featuringprominent
patterns [16]. Based on this prior knowledge, we proposed S-DRI to constrain forest
disturbancesinthewindowsequence. TheS-DRIforagivenyear(targetyearreferstoa
specificyearinthetimeseriesthatisbeinganalyzed)isthefirst-orderlinearregression
slopeoftheNBRvaluesforthepreviousandsubsequentyears. Theslopeindicatesthe
direction and magnitude of the spectral index change in the time series and is used to
determinewhetheradisturbanceoccurred. TheS-DRIforthetargetyeariscalculatedas
showninEquation(2). Inthisstudy,theS-DRIofthetargetyearusedtheNBRvaluesfor
eachofthetwopreviousandsubsequentyearsandthetargetyear.
∑i (cid:0) Y −Y (cid:1)
S−DRI= i (2)
∑i2
whereY denotestheNBRvalueoftheiyeardistancefromthetargetyear,i ∈ {−2,−1,1,2}.
i
YdenotesthemeanvalueoftheNBRinvolvedinthecalculation.
Basedonpriorknowledgeofthetime-varyingfeaturesofforestdisturbance,weuse
S-DRI to constrain disturbance events in window sequences labeled as Disturbance by
self-attentionmodels(Figure6). Thestrategyisasfollows: First,wecalculatethefirst-order
difference(∆Y)ofspectralvaluesinwindowsequencestoanalyzethechangemagnitude
betweenadjacentyears(Equation(3)). Toprioritizethedetectionoflargeroutliersoryears
thatdeviatefromthespectraltrendinthetimeseries,theS-DRIvaluesforthetargetyears
aresequentiallycalculatedviathe∆Ymagnitudeoftheyear. Inotherwords,theS-DRI
valuesforeachtargetyeararecalculatedstartingfromtheyearwiththelargestdifference
inNBRvaluesandthengraduallymovingtowardsyearswithsmallerdifferences,until
alltargetyearshavebeencomputed. Thisapproachavoidsexploringknowninvalidor
irrelevantsolutions. Next,theS-DRIvalueofthetargetyeariscomparedtoapredefined
threshold. IftheS-DRIvalueexceedsthethreshold,weassumethatitisafalsedisturbance
causedbynoiseandcontinue,calculatingtheS-DRIvalueofthenexttargetyear. Ifthe
S-DRIvalueislessthanorequaltothepredefinedthreshold,thecurrentyearisoutput.
Therearetwostopcriteriainthisworkflow: (1)thewindowsequencehasatargetyear

Remote Sens. 2023, 15, x FOR PEER REVIEW 10 of 24
predefined threshold. If the S-DRI value exceeds the threshold, we assume that it is a false
RemoteSens.2023,15,2963 10of23
disturbance caused by noise and continue, calculating the S-DRI value of the next target
year. If the S-DRI value is less than or equal to the predefined threshold, the current year
is output. There are two stop criteria in this workflow: (1) the window sequence has a
thatmeetstherequirementsofthepredefinedthreshold,and(2)themaximumnumber
target year that meets the requirements of the predefined threshold, and (2) the maximum
ofiterationshasbeenreached. Ifnoneofthetargetyearsmetthesetthresholdafterall
number of iterations has been reached. If none of the target years met the set threshold
iterations,itwasconsideredthattherewasnochangeintheforestinthewindowsequence.
after all iterations, it was considered that there was no change in the forest in the window
Inawindowsequence,onlythetargetyearsthatmeettheS-DRIcalculationcriteriaare
sequence. In a window sequence, only the target years that meet the S-DRI calculation
calculated,suchasY toY inFigure6.
3 7
criteria are calculated, such as 𝑌 to 𝑌 in Figure 6.
(cid:2871) (cid:2875)
∆Y ∆ = 𝑌 Y =i − 𝑌 Y −i−𝑌1 (3 (3 ) )
(cid:3036) (cid:3036)(cid:2879)(cid:2869)
Figure 6. Workflow of S-DRI application. Difference sort is an example of the calculation order of S-
Figure6. WorkflowofS-DRIapplication. Differencesortisanexampleofthecalculationorderof
DRI values for different target years in a window sequence.
S-DRIvaluesfordifferenttargetyearsinawindowsequence.
22.4.4..R ReessuultltssA AsssseessssmmeennttM Meetthhoodd
TThheed disitsuturbrbananceced edteetcetciotinonac accucruarcaycwy awsaass saesssseesdseuds iunsginthge thbien bairnyacrlya scsliafiscsaifiticoantimonet mricest.-
Inrictsh.i sIns ttuhdisy ,satutdoyta, lao tfo3ta0l8 2off o3r0e8s2t pfoixreeslst pwiexreelsm waenruea mllyaninutaelrlyp rientteedrpinrefitevde isnt ufidvye asrteuadsy
aanrdeacso lalnecdt ecdolalesctteesdt dasa ttae.sTt dheatoav. eTrhaell oavcecurarlalc aycc(OurAa)c,yp (rOodAu),c eprr’osdauccceurr’asc ayc(cPuAra),cayn (dPAu)s,e arn’sd
auccseurr’asc aycc(uUrAac)yw (eUrAe)u wseedret ousaesds etsos atshseesasc tchuer aaccycuorfacthy eoff otrhees tfodriessttu drbisatnucrebadnectee cdteiotenct(iaosn
s(haosw shnoiwnnTa ibnl eTa2balne d2 Eanqdua Etiqouna(t4io))n. T(4h)e). OThAem OeAa smureeasstuhreesp trhoep oprrtoiopnorotfiocno rorfe cctolyrrcelcatslysi ficleads-
ssaimfiepdle ssamampolensg aamllosnagm aplll esas.mTphleesP. AThme PeaAs umreeasstuhreesp rthoep oprrtoiopnorotifotnr uolfy trpuolsyi tpivoesistiavme psalems-
apmleosn gamalolnsagm aplll essamclapslseisfi celdasassifipeodsi taisv ep.oTshiteivUe.A Tmhee aUsuAr emstehaesuprreosp tohreti opnroopfotrrutiloynp oofs ittriuvley
spamospitlievsea smamonpgleasl lasmamonpgle asllla sbaemlepdleass lpaobseilteivde a.sI tpiosswitoivrteh. Int oisti wngotrhtha tnaostitnrigc ttthiamt ea dsetrfiicnti ttiiomne
wasusedintheevaluationofforestdisturbancedetectionresults. Theinconsistentoutput
definition was used in the evaluation of forest disturbance detection results. The incon-
disturbancetimes(e.g.,ifadisturbanceoccurredin2007butthemodeldetecteditin2006
sistent output disturbance times (e.g., if a disturbance occurred in 2007 but the model de-
or2008)wereconsideredasfailuresofthemodelindetectingforestdisturbances.InTable2,
tected it in 2006 or 2008) were considered as failures of the model in detecting forest dis-
outputresultswithinconsistentdisturbancetimeareconsideredasFP.
turbances. In Table 2, output results with inconsistent disturbance time are considered as
FP.
Table2.Confusionmatrixfortheevaluationofforestdisturbancedetectionresults.
The method proposed in this study requires setting two parameters: the size of the
moving window and the predefined S-DRI threshold. Different parameter settings may
ReferenceData
resultM ina pdCifflaesrsent model output results. Therefore, we conducted a grUids esre’sarAcchc utora tceyst all
NoChange Disturbance
possible combinations to find the best parameters for each input set [37]. The grid search
Nochange TP FP TP
involved 60 (3 × 20) model setups, each defined by a combination of windoTwP+ sFiPzes and S-
Disturbance FN TN TN
DRI values, in order to determine the optimal configuration. Specifically, weF Nu+sTeNd window
Producer’sAccuracy TP TN
sizes of 7, 9, and 11 and S-DRI TvPa+luFNes ranging from −0FP.1+ tToN 0, with an interval of 0.005. This
study includes a time series classification model. When searching for window sizes, we
alsoT chaelcumlaetthedo dthper oovpeorsaeldl aicnctuhriascsyt uodf ythree tqiumiree ssesreiettsi nclgastswifiocpatairoanm metoedrse:lst hweitshiz deioffferthenet
movingwindowandthepredefinedS-DRIthreshold. Differentparametersettingsmay
result in different model output results. Therefore, we conducted a grid search to test
all possible combinations to find the best parameters for each input set [37]. The grid
searchinvolved60(3×20)modelsetups,eachdefinedbyacombinationofwindowsizes

RemoteSens.2023,15,2963 11of23
andS-DRIvalues,inordertodeterminetheoptimalconfiguration. Specifically,weused
windowsizesof7,9,and11andS-DRIvaluesrangingfrom−0.1to0,withanintervalof
0.005. Thisstudyincludesatimeseriesclassificationmodel. Whensearchingforwindow
sizes,wealsocalculatedtheoverallaccuracyofthetimeseriesclassificationmodelswith
differentwindowsizes. Themethodusedtopreprocessthetestingdatasetforevaluating
theclassificationaccuracyoftheself-attentionmodelisconsistentwiththepreprocessing
strategyusedforthetrainingdataset.
To further evaluate the performance of the proposed forest disturbance detection
method, the results of the forest disturbance detected in this study were compared to
thosedetectedbytheLandTrendrandtheGFCdataset[16,25,66]. LandTrendrandGFC
usetimeseriesofLandsatsatelliteimagestodetectchangesinforestcoverandprovide
important data for land management decisions. Utilizing the functions and datasets
provided in Google Earth Engine (GEE, https://earthengine.google.com, accessed on
1July2022),wedownloadedtheforestdisturbancemapsofLandTrendr(useparameters
asshowninTableA2)andGFC,andweextractedthepixelvaluesofthetestdatasetfor
evaluation. In this study, the performance of the three methods for forest disturbance
detection was evaluated using a confusion matrix. In addition, we also evaluated the
omission(Equation(5))ofdifferentdisturbancecausalagentsofthethreemethods.
TP+TN
Overall Accuracy = (4)
TP+FP+FN+TN
TN(i)
Omission(i) =1− (5)
FP(i)+TN(i)
whereiisforestdisturbancecausalagentclass.
3. Results
3.1. OptimalParameters
The evaluation results of the test dataset using different parameter combinations
obtainedthroughthegridsearchareshowninTable3. Foreachwindowsize,onlythebest
parametersetupwiththehighestaccuracyfortheS-DRIvalueisshown. Theresultsshow
thattheOAoftheself-attentionmodelswithdifferentwindowsizesisveryclose,about
95%,withadifferenceoflessthan1%. Thisdifferencemaybecausedbytherandomness
of DL or the machine environment. Increasing the window size does not improve the
accuracyofthemodel,indicatingthatthechangeinformationinthecontinuousseven-year
remotesensingtimeseriesprovidessufficientevidencetodistinguishwhethertheforest
hasbeendisturbed.
Table3.Evaluationresultsofthetestdatasetbasedondifferentparametercombinationsfromthe
gridsearch.
Self-AttentionModel DisturbanceDetection
WindowSize S-DRI
OA OA PA UA
7 95.5% −0.05 86.9% 66.5~97.4% 87.0~91.6%
9 95.1% −0.05 87.0% 66.5~97.3% 87.1~91.6%
11 95.5% −0.05 87.8% 68.9~97.4% 87.0~91.4%
WealsoobservedthattheoptimalS-DRIthresholdfordifferentwindowsizeswas
−0.05, indicating that this is the best balance between filtering out noise and detecting
disturbanceinthewindowsequence. Whenthewindowsizewaschangedwiththesame
S-DRI, it could be observed that the OA of the test dataset improved with an increase
in the window size. Based on the OA of the self-attention model of different window
sizes,thetimeseriesclassifierdoesnotimproveaccuracyasthewindowsizeincreases,
indicatingthatalargerwindowsizeisbeneficialinprovidingmoretemporalinformation

Remote Sens. 2023, 15, x FOR PEER REVIEW 12 of 24
PA increases from 66.5~97.4% to 68.9~97.4%. However, it does not mean that we should
use a larger window size because a larger window size means a sequence containing more
noise and a greater probability of multiple disturbances. With an increase in window size,
the UA of the model decreased from 87.0~91.6% to 87.0~91.4%. In view of both methods’
efficiency and accuracy, a window size of 11 and S-DRI of −0.05 were, therefore, identified
as the best-performing combination of parameters in this study.
Table 3. Evaluation results of the test dataset based on different parameter combinations from the
grid search.
Self-Attention Model Disturbance Detection
Window Size S-DRI
OA OA PA UA
7 95.5% −0.05 86.9% 66.5~97.4% 87.0~91.6%
9 RemoteSens.2023,15,2963 95.1% −0.05 87.0% 66.5~97.3% 12of8273.1~91.6%
11 95.5% −0.05 87.8% 68.9~97.4% 87.0~91.4%
thatconfirmsthedisturbanceyearsaccordingtopriorknowledgeconstraints,thusenabling
thFeigmuordee l7to idlleutescttrmaoteresd tishtuer bdainsctereibveunttisotnha toffa llSo-nDtRheI evdageluoefsth efowri nddioswtuserqbuaennccee and no-change
yeardsu ient oththee mtroaviinnignwgi nddaowta.sFeotr eaxnamd ptlees,wtihnegn tdhaetwaisnedto wofs itzheein scrteuadseys farormea9st.o T11h,eth me edian values of
PAincreasesfrom66.5~97.4%to68.9~97.4%. However,itdoesnotmeanthatweshould
S-DRI for no-change samples were concentrated around 0, while the S-DRI values for dis-
usealargerwindowsizebecausealargerwindowsizemeansasequencecontainingmore
turbneodis seaamndpalegrse rataenrgpreodba fbriolitmyo −f0m.0u7lti (pMledoinsttuarnbaan)c teos. −W0i.th16a n(Oinrcreegasoenin).w Ain tdhorwessihzeo,ld of −0.05 could
effectthievUelAyo dftehteemcto fdoelredesctr edaissetdufrrobman8c7.e0s~ 9w1.6it%hiton 8t7h.0e~ 9s1t.u4%d.yI navrieeaw. oTfhbeot hwmidetthhosd so’f the upper and
efficiencyandaccuracy,awindowsizeof11andS-DRIof−0.05were,therefore,identified
lower boundaries of the boxplots in different study areas reflect, to some extent, the abun-
asthebest-performingcombinationofparametersinthisstudy.
dance ofF ilgouwre-7 ainlluds thraitgesht-hmeadgisntriibtuutdioen dofisSt-uDrRbIavnalcueess fcoorndtisatiunrbeadn ciena tnhden ao-rcehaa.n gFeor example, Ore-
gon yheaasrs hinigthhe ftorariensint gcodavteasre (tNanBdRte ostfin agbdoautats e0t.8of),t haensdtu ddyisaturerabs.aTnhceems eindicalnuvdaelu mesore high-magni-
of S-DRI for no-change samples were concentrated around 0, while the S-DRI values
tude spectral variation (harvest, fire) and less low-magnitude spectral variation (thinning),
fordisturbedsamplesrangedfrom−0.07(Montana)to−0.16(Oregon). Athresholdof
resu−lt
0
in
.0 g
5 c
i
o
n
u l
l
d
ar
e
g
ff
e
ec
r
t i
b
v
o
el
x
y d
d
e
i
t
s
e
p
ct
e
f
r
o
s
r
i
e
o
st
n
d i
a
s
n
tu
d
rb
s
a
m
nce
a
s
ll
w
e
i
r
t h
m
in
e
t
d
he
ia
s
n
tu
s
d
.
y
F
a
i
r
g
e
u
a.
r
T
e
h
8
e
d
w
e
id
m
th
o
s
n
of
strates the appli-
catiotnhe oufp pSe-rDaRndI lionw derebtoeurnmdianriiensgof dthiestbuorxbplaontscien deivffeenretnst isntu dwyianrdeaoswrefl seectq,utoesnocmees, and S-DRI can
extent,theabundanceoflow-andhigh-magnitudedisturbancescontainedinthearea. For
capture disturbance events caused by abrupt spectral changes (conversion and thinning)
example,Oregonhashighforestcover(NBRofabout0.8),anddisturbancesincludemore
as well as changes that persisted over many years, such as forest cover loss due to pests
high-magnitudespectralvariation(harvest,fire)andlesslow-magnitudespectralvariation
and (dthiisnenainsge)s,.r eIsnu latidngdiintiloarnge, rthborxoduigsphe rrsieognraensdsisomnal luersminegd imansu.lFtiig-uyreea8rd sepmeocntsrtraalt evsalues, S-DRI can
the application of S-DRI in determining disturbance events in window sequences, and
also distinguish noise caused by image composites, phenological changes, or sensor fail-
S-DRIcancapturedisturbanceeventscausedbyabruptspectralchanges(conversionand
ures (Figure 8d).
thinning)aswellaschangesthatpersistedovermanyyears,suchasforestcoverlossdueto
pestsanddiseases. Inaddition,throughregressionusingmulti-yearspectralvalues,S-DRI
canalsodistinguishnoisecausedbyimagecomposites,phenologicalchanges,orsensor
failures(Figure8d).
Figure7. ThedistributionofS-DRIondifferentdatasets. Outliersthatlieoutsidetheupperand
Figure 7. The distribution of S-DRI on different datasets. Outliers that lie outside the upper and
lowerquartiles(IQR)aredisplayedasindividualpoints.
lower quartiles (IQR) are displayed as individual points.

RReemmoottee SSeennss.. 22002233,, 1155,, x2 9F6O3R PEER REVIEW  131 3oof f2243

FFiigguurree 88.. EExxaammppllee ooff aapppplliiccaattiinngg SS--DDRRII iinn mmuullttiippllee ttiimmee sseerriieess sscceennaarriiooss,, iinncclluuddiinngg ((aa)) ccoonnvveerrssiioonn;;
((bb)) tthhiinnnniinngg;; ((cc)) ppeessttss aanndd ddiisseeaasseess;; ((dd)) nnoo cchhaannggee..
3.2. AccuracyAssessment
3.2. Accuracy Assessment
Theevaluationresultsofthethreemethodson3082testdatainfivestudyareasare
The evaluation results of the three methods on 3,082 test data in five study areas are
showninTable4. Anassessmentofthediscriminationbetweennochange/disturbance
shown in Table 4. An assessment of the discrimination between no change/disturbance
samples indicated that our approach created reliable maps of forest disturbance. Our
samples indicated that our approach created reliable maps of forest disturbance. Our ap-
approach has the highest OA at 87.8%, which is higher than LandTrendr’s 84.6% and
proach has the highest OA at 87.8%, which is higher than LandTrendr’s 84.6% and GFC’s
GFC’s81.4%. Theforestdisturbancedetectionwasthefocusofthestudy. Thedisturbance
81.4%. The forest disturbance detection was the focus of the study. The disturbance class’s
class’sproduceraccuracyofourapproachwasrelativelyhigh,at68.9%,indicatingthatour
producer accuracy of our approach was relatively high, at 68.9%, indicating that our ap-
approachcapturesmoreaccurateforestdisturbances. LandTrendrevaluated2049samples
proach captures more accurate forest disturbances. LandTrendr evaluated 2,049 samples
for the no-change class, out of which only 24 were detected as the disturbance class.
for the no-change class, out of which only 24 were detected as the disturbance class. How-
However,therelativelylowUA(81.8%)fortheno-changeclassindicatesthatLandTrendr
ever, the relatively low UA (81.8%) for the no-change class indicates that LandTrendr
identifiessomedisturbancepixelsasnochange. GFChadhighdisturbancetimeconfusion
identifies some disturbance pixels as no change. GFC had high disturbance time confusion
anddisturbanceeventdropouts;therefore,thedisturbanceclasshasalowerUA(88.9%)
and disturbance event dropouts; therefore, the disturbance class has a lower UA (88.9%)  andPA(50.9%).
and PA (50.9%).
Table4.Confusionmatrixofforestdisturbancedetectionassessment.
Table 4. Confusion matrix of forest disturbance detection assessment.
ReferenceData
|     |            |     | MapCRleafsesrence Data  |     |                | PA UA | OA  |
| --- | ---------- | --- | ----------------------- | --- | -------------- | ----- | --- |
|     | Map Class  |     |                         |     | DisturbaPnAce  | UA    | OA  |
NoChange
|             |                      |      | No Change   | Disturbance  |        |             |        |
| ----------- | -------------------- | ---- | ----------- | ------------ | ------ | ----------- | ------ |
|             |                      |      | Nochange    | 1992         | 322    | 97.3% 86.1% |        |
|             | No change            | Ours | 1992        | 322          | 97.3%  | 86.1%       | 87.8%  |
| Ours        |                      |      | Disturbance | 55           | 713    | 68.9% 92.8% | 87.8%  |
|             | Disturbance          |      | 55          | 713          | 68.9%  | 92.8%       |        |
|             |                      |      | Nochange    | 2023         | 451    | 98.8% 81.8% |        |
|             | No changeL andTrendr |      | 2023        | 451          | 98.8%  | 81.8%       | 84.6%  |
| LandTrendr  |                      |      | Disturbance | 24           | 584    | 56.4% 96.1% | 84.6%  |
|             | Disturbance          |      | 24          | 584          | 56.4%  | 96.1%       |        |
|             |                      |      | Nochange    | 1981         | 508    | 96.8% 79.6% |        |
|             | No change            | GFC  | 1981        | 508          | 96.8%  | 79.6%       | 81.4%  |
| GFC         |                      |      | Disturbance | 66           | 527    | 50.9% 88.9% | 81.4%  |
|             | Disturbance          |      | 66          | 527          | 50.9%  | 88.9%       |        |
Table5showstheomissionrateofthreeapproachestodetectdifferentdisturbance
Table 5 shows the omission rate of three approaches to detect different disturbance
causal agent classes. The map omission via the test dataset disturbance agent class in-
causal agent classes. The map omission via the test dataset disturbance agent class indi-
dicatesthatthethreemethodsprovideloweromissionforhigh-magnitudedisturbances
cates that the three methods provide lower omission for high-magnitude disturbances
(wind,harvesting,andfire),whiledisturbanceswithlowermagnitudeandlongerduration
(wind, harvesting, and fire), while disturbances with lower magnitude and longer dura-
(thinning,pest,anddiseases)havehighomission. Theomissionoflow-magnitudedistur-
tion (thinning, pest, and diseases) have high omission. The omission of low-magnitude
bancesaffectsforestdisturbancedetectionsignificantly. Ourapproachismoresensitiveto
disturbances affects forest disturbance detection significantly. Our approach is more sen-
detectingharvest,conversion,wind,thinning,andpestdiseases,withsignificantlylower
sitive  to  detecting  harvest,  conversion,  wind,  thinning,  and  pest  diseases,  with

RemoteSens.2023,15,2963 14of23
omissionthantheothertwoapproaches,especiallyindetectingcomplexlandusechanges
(conversion,18.0%)andlong-termpestdiseases(pestanddiseases,32.7%).
Table5.Omissionrateofthreeapproachestodetectdifferentdisturbancecausalagentclasses.
Harvest Conversion Fire Wind Thinning PestandDiseases Other
Number 361 172 194 60 93 98 57
Ours 16.3% 18.0% 18.6% 10.0% 40.9% 32.7% 67.4%
LandTrendr 27.4% 32.0% 18.0% 20.0% 63.4% 66.4% 81.6%
GFC 25.5% 40.7% 27.3% 15.0% 60.2% 88.8% 69.4%
3.3. MappingForestDisturbance
Estimatesoftheareaofforestdisturbanceinthesestudyareasindicatedthatapproxi-
mately20%oftheforesthadexperiencedatleastonedisturbanceintheperiodof2001–2020.
Remote Sens. 2023, 15, x FOR PEER REVIEW Thethreeapproachesprovidedrelativelyconsistentspatialandtemporal1d5 isotfr i2b4u tionsof
forestdisturbanceinOregon,WestVirginia,Alberta,andPoland(Figure9). Visually,the
differentmethodsprovidedthespatialextentofcontinuouslyactivehumanactivitiesand
severenaturaldisastersthataretemporallyconsistentwiththehistoricalrecordobserved.
Figure9. Mapofforestdisturbancetimeinthe5studyareasfrom2001to2020,detectedbythe
Figure 9. Map of forest disturbance time in the 5 study areas from 2001 to 2020, detected by the
proposedmethod,theLandTrendr,andtheGFC.
proposed method, the LandTrendr, and the GFC.
However,threemethodsmappedsignificantlydifferentforestdisturbancedetection
resultsinMontana. PreviousstudiesindicatethatthepresenceofbarkbeetlesinMontana
State’spineforestswasdocumentedasearlyasthelate1990s. In2009,theforestsexpe-
riencedthelargestoutbreakofbarkbeetlesonrecord[67]. Basedonthehigh-resolution
remotesensingimageriesinthisarea, itwasfoundthattheforestsintheareabeganto
change from deep green to reddish brown around 2008 and then turned to dark gray
between2009and2010. Tofurtherevaluatethespatialandtemporaldistributionoftree
damagecausedbythebarkbeetle,wecitedthebark-beetle-causedtreemortalitydistur-
bance dataset of Berner et al. [68] as a supplement (Figure 10). The dataset shows that
Figure 10. Estimated tree mortality due to bark beetles with aerial surveys, forest inventory meas-
urements, and high-resolution satellite maps by Berner et al. [68] in the study area of Montana. Tree
mortality is expressed as the amount of AGC stored in trees killed by disturbance (Mg/km2).
Fine-scale differences between the various approaches are highlighted by selecting
an example from each study area, as shown in Figure 11. GFC has a longer detection pe-
riod and does not face any composite image limitations (Figure 11b). However, GFC ig-
nores disturbances occurring in partially mixed pixels (Figure 11a) and may result in the
omission and incorrect detection of low-magnitude disturbances (Figure 11e). Land-
Trendr and our approach both utilize composite images during the vegetation growing
season (July–September). Therefore, disturbances occurring after the vegetation growing
season can only be detected in the next year’s growing season. As a result, both Land-
Trendr and our method cannot detect the Oregon wildfires in October 2020 (Figure 11b)
and fail to completely detect the harvest of the rapid recovery (Figure 11a). LT-GEE (Land-
Trendr-GEE) filters out some small changes based on statistical patterns in spatial and
temporal dimensions in order to filter out noise, which makes it have a high PA of the no-

Remote Sens. 2023, 15, x FOR PEER REVIEW 15 of 24
RemoteSens.2023,15,2963 15of23
thesoutheasternpartoftheregionwasinfestedwithbarkbeetlesin2007,causingsevere
damagetoforestsinthenorthernpartoftheMontanastudyareain2008. By2009, the
Figure 9. Map of forest disturbance time in the 5 study areas from 2001 to 2020, detected by the
infestationhadshiftedtothesouthwest,causingdamagetoforeststhroughoutthestudy
proposed method,a trheae. LOaunrdapTprreonadchr,p arnovdi dtehsef oGreFsCtd. isturbancemappingresultsthataremoreconsistent
withthisdataset.
Figure 10. EstimatFeidgu trree1e0 .mEsotimrtaatleidtytr edeumeo rttoal ibtyadruke btoebeatrlkebse wetlietshw aitehraiearlia slusurrvveeyyss,f,o froesrteinsvt einntovreynmtoearsyu rme-eas-
ments,andhigh-resolutionsatellitemapsbyBerneretal.[68]inthestudyareaofMontana. Tree
urements, and high-resolution satellite maps by Berner et al. [68] in the study area of Montana. Tree
mortalityisexpressedastheamountofAGCstoredintreeskilledbydisturbance(Mg/km2).
mortality is expressed as the amount of AGC stored in trees killed by disturbance (Mg/km2).
Fine-scaledifferencesbetweenthevariousapproachesarehighlightedbyselecting
an example from each study area, as shown in Figure 11. GFC has a longer detection
Fine-scale differences between the various approaches are highlighted by selecting
periodanddoesnotfaceanycompositeimagelimitations(Figure11b). However,GFC
an example from each study area, as shown in Figure 11. GFC has a longer detection pe-
ignoresdisturbancesoccurringinpartiallymixedpixels(Figure11a)andmayresultinthe
riod and does noomt ifsascioen aanndyi nccoomrrepctodseitteect iiomnaofgleow li-mmaigtnaittiuodnesd i(sFtuirgbuanrcee s1(1Fibg)u.r eH1o1ew).eLvanedrT, rGenFdCr ig-
andourapproachbothutilizecompositeimagesduringthevegetationgrowingseason
nores disturbances occurring in partially mixed pixels (Figure 11a) and may result in the
(July–September). Therefore,disturbancesoccurringafterthevegetationgrowingseason
omission and incorrect detection of low-magnitude disturbances (Figure 11e). Land-
canonlybedetectedinthenextyear’sgrowingseason. Asaresult,bothLandTrendrand
Trendr and our oauprpmreotahocdh cbanontoht duettielcitzteh ecoOmregpoonswitield ifimresagineOs cdtoubreirn2g02 0th(Fei gvuereg1e1tba)tiaonnd fgairlotowing
completely detect the harvest of the rapid recovery (Figure 11a). LT-GEE (LandTrendr-
season (July–September). Therefore, disturbances occurring after the vegetation growing
GEE)filtersoutsomesmallchangesbasedonstatisticalpatternsinspatialandtemporal
season can only be detected in the next year’s growing season. As a result, both Land-
dimensionsinordertofilteroutnoise,whichmakesithaveahighPAoftheno-change
Trendr and our mclaessthbuotdo vcearnlonokost sdometeeocft tthheere Oalrdeisgtuornb awncielsd(fiFirgeusr ein11 cO,ec)t[o69b].eIrn 2a0d2d0iti o(Fn,igthuerLeT -11b)
GEEfitsthetimeseriesandpreventsone-yearrecovery,whichmayproduceomissionat
and fail to completely detect the harvest of the rapid recovery (Figure 11a). LT-GEE (Land-
theendofthedetectionperiod(Figure11a,d)[70]. Ourapproachismorecompleteand
Trendr-GEE) filters out some small changes based on statistical patterns in spatial and
accurate in mapping the forest disturbance. It is also noteworthy that S-DRI identifies
temporal dimensthioendsis tiunr boarndceery etaor fiwlittehrt hoeugtr enaoteisstes,p wechtriaclhch managke,ews hitil ehtahveep aer shisitgehnt PinAfe sotfa ttiohne no-
of trees by pests and diseases causes our approach to have a temporal delay (1 year)
indetectingsomedisturbance(Figure11e). Comparedtoothermethods,ourapproach
exhibits enhanced regularity and continuity in detecting forest disturbance boundaries
associatedwiththinningandharvestingactivities,withsignificantlyfeweromissionsand
fragmentedpatches(Figure11f).

Remote Sens. 2023, 15, x FOR PEER REVIEW 16 of 24
change class but overlooks some of the real disturbances (Figure 11c, e) [69]. In addition,
the LT-GEE fits the time series and prevents one-year recovery, which may produce omis-
sion at the end of the detection period (Figure 11a,d) [70]. Our approach is more complete
and accurate in mapping the forest disturbance. It is also noteworthy that S-DRI identifies
the disturbance year with the greatest spectral change, while the persistent infestation of
trees by pests and diseases causes our approach to have a temporal delay (1 year) in de-
tecting some disturbance (Figure 11e). Compared to other methods, our approach exhibits
enhanced regularity and continuity in detecting forest disturbance boundaries associated
with thinning and harvesting activities, with significantly fewer omissions and frag-
RemoteSens.2023,15,2963 16of23
mented patches (Figure 11f).
Figure11.ComFipgaurries o1n1.o Cfothmepraersiuslotns ooff dthifef erreesnutltasp opfr doiaffcehreesnfto arpmparopapcihnegsf foorre smtadpisptuinrgb afnorceessta dtifistnuerbances at fine
scale.Thelatitsucadlee.a Tnhdel olantgitiutudde eaanrde ltohnegcietundteer saroef tthhee caerneate.rTs hoef athcqe uairseitai.o Tnhdea atecqoufitswitioo-np hdaastee HofD two-phase HD
imageintheloimwaegr-er iignh tthceo lronwere.r-right corner.
4. Discussion
4. Discussion
An accurate understanding of forest dynamics is critical for both effective forest
An accurate understanding of forest dynamics is critical for both effective forest man-
managementandmitigatingtheeffectsofclimatechange. Theworkpresentedheredemon-
agement and mitigating the effects of climate change. The work presented here demon-
stratesanovelapproachfordetectingforestdisturbancesusingDLtimeseriesclassification
strates a novel approach for detecting forest disturbances using DL time series
andpriorknowledgeconstraint. Duringthedetectionperiod,themovingwindowalgo-
rithmprocessesthetimeseriesofpixelsasawindowsequenceandevaluatesthewindow
sequencewithanimprovedself-attentionmodeltoobtainanintervalestimateofthedis-
turbancetime. Theaprioriknowledgeconstraintsareappliedtotheresultingwindow
sequencewithdisturbanceeventstodeterminetheexactyearofdisturbance. Theresults
demonstratethatthecombinationofDLtimeseriesclassificationmodelsandpriorknowl-
edgeconstraintscanhelpdetectforestdisturbancesofvaryingmagnitudes,fromsubtleto
severe. Thisapproachprovidescomprehensiveanddetailedinsightintoforestdynamics
andcansupporteffectiveforestmanagementandclimatechangemitigationefforts.
AkeyinnovationofourworkliesinthecombinationofDLtimeseriesclassification
and prior knowledge constraints to detect the history of forest disturbance. Landsat-
based forest cover and change mapping using supervised expert-driven classification

RemoteSens.2023,15,2963 17of23
is a well-established and accepted methodology [71]. Recent studies have shown that
utilizing robust reference data and carefully constructed models results in disturbance
mapswithhigheraccuracy,suchasstackedgeneralization,secondaryclassification,and
ensemblemethods[22,23,26]. However, thesemethodsrelyonthefoundationofforest
disturbancedetectionalgorithms,suchasLandTrendr,toprovideevidence. Inprevious
studies,themainapplicationsofDLinforestdisturbancedetectionhavebeeninsemantic
segmentationandtimeseriesregressionandforecasting[30,72–75]. Whenusedforlarge-
scaledisturbancedetection,thesemethodsstillhavemorelimitations,suchastheneed
forlabor-intensivemanualannotationandhigher-qualityimages. Ourstudyemployeda
methodbasedontimeseriesdeeplearningandpriorknowledgeconstraints,effectively
addressingthechallengeofdetectinglow-amplitudedisturbances. Inthestudy,thedeep
learningtimeseriesclassifierdifferentiatedbetweenstableforestsanddisturbances,while
theapplicationofpriorknowledgeconstraintsreducedthelearningcostofthemodel. Our
methodisapplicablefordetectingdisturbancesofvaryingmagnitudesonaglobalscale,
asdemonstratedbythevalidationresultsacrossmultiplestudyareasworldwide. These
resultsprovideevidenceofthereliabilityofourmethod.
Ideally,noiseduetocloudcontamination,smokeobscuration,andsensorfailurein
thetimeseriesshouldbecompletelyremovedbeforetimeseriesanalysis,butcomplete
eliminationofthisnoiseisnotpossiblewithouthumanintervention[23]. Thedifferences
in spectral indices based on spectral reflectance ratio between observations before and
afterlow-magnitudeforestdisturbancesareverysimilartothespectralchangescaused
by phenological variations and solar angle differences [76,77]. Using high-magnitude
thresholdrulescanremovethesenoisyanderroneousspectralchanges,butitisdifficultto
capturelow-magnitudedisturbances[26].Evaluationoftheresultsfordifferentdisturbance
causalagentsshowsthatignoringlow-magnitudedisturbances(e.g.,thinning,pests,and
diseases)isstillanimportantfactoraffectingtheaccuracyofthemodel. Theself-attention
modelusesmulti-yearspectraltrajectoryprofilestotrackforestdisturbances,filteringout
mostspectralchangescausedbynoise,whichhelpstheknowledgeconstraint(S-DRI)run
inahigh-confidencewindowsequence.Bydoingso,alowerthresholdcanbeusedtodetect
theoccurrenceofforestdisturbance,avoidingoversensitivitytospectralchanges. When
weattemptedtodetectforestdisturbanceusingS-DRIaloneforeachpixelthroughoutthe
detectionperiodwithoutemployingamovingwindowandDLtimeseriesclassification,
therewasasignificantdecreaseinOAofthetestdataset. Specifically,theOAdecreasedto
68.1%,asexpected.
Thetimeseriesclassificationtaskiscomplicatedbyextraneous,erroneous,andun-
aligneddataofvariablelength[46]. Themovingwindowsolvestheproblemofthefixed
input data dimension of the time series classification model, and the priori knowledge
constraintisusedtodeterminetheexactyearsofdisturbanceevents. Thewindowcanbe
movedinfinitelytoprocessnewimagesaftertheself-attentionmodelhasbeentrained,
providingmoreefficientuseoftheforestdetectiondata.
OptimizingthethresholdforS-DRIallowsforthedetectionoflower-magnitudedistur-
banceswhileeffectivelydistinguishingmostnoise,strikingabalancebetweensensitivity
andspecificity. Todemonstratethisbriefly,thepredefinedthresholdwasfine-turnedto
evaluatetheimpactonourapproachperformance. Wesequentiallyadjustedthethresh-
oldofS-DRIfrom−0.1to0inintervalsof0.005andevaluatedthedisturbanceclassPA
and UA of the test dataset. As shown in Figure 12, when lower thresholds were used,
low-magnitudedisturbancesandnoisewereremoved,whilesignificantlyhigh-magnitude
disturbanceswithdistinctivefeatureswereretained. ThisresultedinlowerUAandhigher
PA.WiththeincreasedS-DRIthreshold,moreofthelow-magnitudedisturbancescanbe
effectivelyretained,andtheUAcorrespondinglyincreases. Meanwhile,highthresholds
allowedsomenoisetopassthroughconstraints,resultinginlowerPA.Whenthethreshold
isadjustedtoacertainvalue(−0.035),mostofthedisturbancecanbedetected,andthe
UAdoesnotincrease,evenifthethresholdisadjustedagain. However,asthethreshold
increases,italsoallowsmorefalsedisturbancestopassthedetection,resultinginacon-

Remote Sens. 2023, 15, x FOR PEER REVIEW 18 of 24
Optimizing the threshold for S-DRI allows for the detection of lower-magnitude dis-
turbances while effectively distinguishing most noise, striking a balance between sensi-
tivity and specificity. To demonstrate this briefly, the predefined threshold was fine-
turned to evaluate the impact on our approach performance. We sequentially adjusted the
threshold of S-DRI from −0.1 to 0 in intervals of 0.005 and evaluated the disturbance class
PA and UA of the test dataset. As shown in Figure 12, when lower thresholds were used,
low-magnitude disturbances and noise were removed, while significantly high-magni-
tude disturbances with distinctive features were retained. This resulted in lower UA and
higher PA. With the increased S-DRI threshold, more of the low-magnitude disturbances
can be effectively retained, and the UA correspondingly increases. Meanwhile, high
thresholds allowed some noise to pass through constraints, resulting in lower PA. When
the threshold is adjusted to a certain value (−0.035), most of the disturbance can be de-
tected, and the UA does not increase, even if the threshold is adjusted again. However, as
the threshold increases, it also allows more false disturbances to pass the detection, result-
ing in a continued decrease in UA. The threshold of S-DRI was the only parameter that
needed to be adjusted when the algorithm was applied in different regions and could be
adjusted by removing low-magnitude disturbances to obtain the required degree of dis-
turbance map.
The accuracy provided in this study may be slightly underestimated because strict
definitions were used in this study without allowing any leeway for time adjustments [78].
Disturbances that occur after the vegetation growth period are not detected by our ap-
proach and LandTrendr until the following year (e.g., one fire in Oregon is not detectable
using both approaches). In the assessment of the results, temporal inconsistencies were
RemoteSens.2023,15,2963 considered to be omissions in the disturbance detection; therefore, all three approaches1 8of23
have a low UA for the no-change class. In addition, GFC detection only targets stand re-
placement disturbances, and non-stand replacement disturbances included in the test data
also involve accuracy calculation, especially in Montana, where GFC can only correctly
tinueddecreaseinUA.ThethresholdofS-DRIwastheonlyparameterthatneededtobe
detect 31 out of 137 changed pixels, resulting in a lower OA.
adjustedwhenthealgorithmwasappliedindifferentregionsandcouldbeadjustedby
removinglow-magnitudedisturbancestoobtaintherequireddegreeofdisturbancemap.
FigureF i1g2u. rPeA1 a2n.dPA UaAn dofU thAe odfisthtuerdbaisntucer bcalanscse fcolra sSs-DfoRrIS t-hDreRsIhtohlrde smhoagldnimtuadgen ittruimdemtirnimg.m ing.
Theaccuracyprovidedinthisstudymaybeslightlyunderestimatedbecausestrict
When mapping the forest disturbance, our approach still suffers from some limita-
definitionswereusedinthisstudywithoutallowinganyleewayfortimeadjustments[78].
tions. It is observed from the S-DRI threshold adjustment (Figure 12) that even with a
Disturbancesthatoccurafterthevegetationgrowthperiodarenotdetectedbyourapproach
higher S-DRI threshold, the approach only has about 70~75% PA, which is caused by the
andLandTrendruntilthefollowingyear(e.g.,onefireinOregonisnotdetectableusingboth
omission in the self-attention model or spectral index application limitations. Due to the
approaches). Intheassessmentoftheresults,temporalinconsistencieswereconsidered
low-magnitude disturbance area being rare with difficult visual interpretation, the forest
tobeomissionsinthedisturbancedetection; therefore,allthreeapproacheshavealow
UAfortheno-changeclass. Inaddition, GFCdetectiononlytargetsstandreplacement
disturbances,andnon-standreplacementdisturbancesincludedinthetestdataalsoinvolve
accuracycalculation,especiallyinMontana,whereGFCcanonlycorrectlydetect31outof
137changedpixels,resultinginalowerOA.
Whenmappingtheforestdisturbance,ourapproachstillsuffersfromsomelimitations.
ItisobservedfromtheS-DRIthresholdadjustment(Figure12)thatevenwithahigherS-DRI
threshold,theapproachonlyhasabout70~75%PA,whichiscausedbytheomissioninthe
self-attentionmodelorspectralindexapplicationlimitations. Duetothelow-magnitude
disturbance area being rare with difficult visual interpretation, the forest disturbance
agentsintherandomlygeneratedtrainingsamplesmainlyincludetheharvest,wildfire,
and conversion [79]. Improving data quality and balancing the samples can enhance
thecapabilityoftimeseriesclassificationmodelstodetectlow-magnitudedisturbances
(thinning, pests, and diseases, etc.), although it requires more effort. Furthermore, the
reductioninforestcovercausedbyfactors,suchaspests,diseases,anddroughts,persistsfor
severalyears. Insubsequentstudies,itisnecessarytodevelopnewconceptualdefinitions
todescribetheentiredisturbanceprocess. Cohenetal.[26]showedthattheuseofmultiple
spectralbands/indicesisverybeneficialforforestdisturbancedetectionandmaysolve
theproblemthatsomedisturbancescannotbemonitoredusingasingleband(e.g.,due
tothesimilarityofNBRindexvaluesbetweenwaterandforests, itisdifficulttodetect
disturbanceswhereforestsareconvertedintowater). MultipleDL-basedmultivariatetime
series learning frameworks have been proposed, and using multiple indexes/bands to
detectforestchangeshouldbeconsideredinafuturestudy[42]. Duringthelaterstages
of our analysis of forest change (2018–2020), we identified an issue where the accuracy
oftheresultsbecameincreasinglyincorrectinallthreemodels. Thisissuearosebecause
spectralchangesovermultipleyearscontinuedtobeanessentialcriterionfordisturbance
determination. However,timeseriesconstructedfromcompositeimagesdidnotcontain

RemoteSens.2023,15,2963 19of23
sufficientdataattheendofthedetectionperiod,whichcontributedtodecreasedaccuracy.
The use of multi-source remote sensing data and a near-real-time change monitoring
approachmaysolvethisproblem. Thiswillbethefocusoffurtherwork[58].
5. Conclusions
Detailed access to long time series and large areas of forest disturbances can be
challengingwithoutrelyingsolelyontheseverityofthedisturbanceeventitself. DLallows
forthecaptureofsubtlelandchangesandadaptationtocomplextemporal–spatialpatterns.
However,itsusefordetectingforestdisturbancesisnotwidespread. Thisstudypresentsa
novelapproachthatcombinesDLtimeseriesclassificationwithpriorknowledgeconstraint
toaddressthisissue. TheintegrationofDLandpriorknowledgeconstraintinwindow
sequenceswithdisturbancefeaturesallowsforareductioninprocessingchangescaused
by noise while enabling the detection of more low-magnitude disturbances. The prior
knowledgeconstraintusesrulesthatconsidertemporalcontextualinformationtoaccurately
determine the year of the disturbance. The approach can be used for long time series
analysisandiseasilytransferabletonewregionswithouttheneedforcomplexparameter
tuning. ThisstudyoffersafreshperspectiveonhowDLcanbeusedtocomprehensively
detectforestdisturbancesonalargescale.
AuthorContributions:Conceptualization,B.D.andY.B.;dataprocessingandcoding,B.D.;formal
analysis, B.D., Y.B. and Z.Y.; methodology, B.D. and Y.B.; project administration, Z.Y.; funding
acquisition,Y.B.;writing—originaldraft,B.D.;andwriting—reviewandediting,B.D.,Y.B.andY.Z.
Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: ThisresearchwasfundedbytheNationalKeyResearchandDevelopmentProgramof
China,grantnumber2016YFB0501502.
DataAvailabilityStatement: Allsatelliteremotesensingusedinthisstudyisopenlyandfreely
available. The Landsat data are freely accessible via https://hls.gsfc.nasa.gov/ (accessed on 23
April 2022). The manually interpreted reference data on forest disturbances across Europe are
freely accessible via https://doi.org/10.5281/zenodo.4138867 (accessed on 15 April 2022). The
tree mortality from fires and bark beetles at 1 km resolution data are freely accessible via https:
//daac.ornl.gov/get_data/(accessedon3July2022).
Acknowledgments: This research was funded by the National Key Research and Development
ProgramofChina,grantnumber2016YFB0501502. Theauthorsalsowouldliketoacknowledge
NASAforprovidingtheharmonizedLandsatdataproductdownloadedfromhttps://hls.gsfc.nasa.
gov/(accessedon23April2022)andSenfetal. forthemanualinterpretationofreferencedata
onforestdisturbancesacrossEuropefromhttps://doi.org/10.5281/zenodo.4138867(accessedon
15April2022).
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
AppendixA
TableA1.Forestdisturbancecausalagentclassesanddescriptions.
Class Description
Harvestingreferstotheremovaloftreesfromaforestforthepurposeof
Harvest
timberproductionorotheruses.
Thinningisaforestrypracticethatinvolvestheselectiveremovaloftrees
Thinning
fromaforesttoimprovethegrowthandhealthoftheremainingtrees.
Conversionreferstotheprocessofchangingthelanduseofaforestedarea,
Conversion typicallytoanon-forestusesuchasagriculture,urbandevelopment,or
infrastructuredevelopment.
Firescanoccurnaturallyorbeintentionallysetandcanhavesignificant
Fire
impactsonforest.

RemoteSens.2023,15,2963 20of23
TableA1.Cont.
Class Description
Pestsanddiseasescanimpactforestsbyattackingandkillingtrees,which
Pestsanddiseases
canleadtode-creasedtreedensityandreducedforestproductivity.
Windeventssuchasstorms,hurricanes,andcyclonescanhavesignificant
Wind impactsonforests,causingdamagetotreesandothervegetationthrough
windandwind-bornede-bris.
Others Othereventsthatcausetreemortalityandcanopycoverreduction.
TableA2.ParametersusedintheLandTrendralgorithm.
Parameter Configuration
Baseindex NBR
MaxSegments 6
SpikeThreshold 0.9
VertexCountOvershoot 3
PreventOneYearRecovery True
RecoveryThreshold 0.25
PvalThreshold 0.05
BestModelProportion 0.75
MinObservationsNeeded 6
References
1. Schroeder,T.A.;Schleeweis,K.G.;Moisen,G.G.;Toney,C.;Cohen,W.B.;Freeman,E.A.;Yang,Z.;Huang,C.TestingaLandsat-
BasedApproachforMappingDisturbanceCausalityinU.S.Forests.RemoteSens.Environ.2017,195,230–243.[CrossRef]
2. Evans,P.M.;Newton,A.C.;Cantarello,E.;Martin,P.;Sanderson,N.;Jones,D.L.;Barsoum,N.;Cottrell,J.E.;A’Hara,S.W.;Fuller,L.
ThresholdsofBiodiversityandEcosystemFunctioninaForestEcosystemUndergoingDieback.Sci.Rep.2017,7,6775.[CrossRef]
[PubMed]
3. Abdullah-Zawawi,M.-R.;Ahmad-Nizammuddin,N.-F.;Govender,N.;Harun,S.;Mohd-Assaad,N.;Mohamed-Hussein,Z.-A.
ComparativeGenome-WideAnalysisofWRKY,MADS-BoxandMYBTranscriptionFactorFamiliesinArabidopsisandRice.Sci.
Rep.2021,11,19678.[CrossRef][PubMed]
4. Frolking,S.;Palace,M.W.;Clark,D.;Chambers,J.Q.;Shugart,H.;Hurtt,G.C.ForestDisturbanceandRecovery: AGeneral
ReviewintheContextofSpaceborneRemoteSensingofImpactsonAbovegroundBiomassandCanopyStructure.J.Geophys.
Res.Biogeosci.2009,114,G2.[CrossRef]
5. Shaw, C.H.; Rodrigue, S.; Voicu, M.F.; Latifovic, R.; Pouliot, D.; Hayne, S.; Fellows, M.; Kurz, W.A. Cumulative Effects of
NaturalandAnthropogenicDisturbancesontheForestCarbonBalanceintheOilSandsRegionofAlberta,Canada;aPilotStudy
(1985–2012).CarbonBalanceManag.2021,16,3.[CrossRef][PubMed]
6. Hicke,J.A.;Allen,C.D.;Desai,A.R.;Dietze,M.C.;Hall,R.J.;Hogg,E.H.;Kashian,D.M.;Moore,D.;Raffa,K.F.;Sturrock,R.N.;
etal.EffectsofBioticDisturbancesonForestCarbonCyclingintheUnitedStatesandCanada.Glob.Chang.Biol.2012,18,7–34.
[CrossRef]
7. Nguyen,T.H.;Jones,S.D.;Soto-Berelov,M.;Haywood,A.;Hislop,S.ASpatialandTemporalAnalysisofForestDynamicsUsing
LandsatTime-Series.RemoteSens.Environ.2018,217,461–475.[CrossRef]
8. Verbesselt,J.;Hyndman,R.;Newnham,G.;Culvenor,D.DetectingTrendandSeasonalChangesinSatelliteImageTimeSeries.
RemoteSens.Environ.2010,114,106–115.[CrossRef]
9. Reed,B.C.;Brown,J.F.;VanderZee,D.;Loveland,T.R.;Merchant,J.W.;Ohlen,D.O.MeasuringPhenologicalVariabilityfrom
SatelliteImagery.J.Veg.Sci.1994,5,703–714.[CrossRef]
10. Hansen,M.C.;Loveland,T.R.AReviewofLargeAreaMonitoringofLandCoverChangeUsingLandsatData. RemoteSens.
Environ.2012,122,66–74.[CrossRef]
11. Gómez,C.;White,J.C.;Wulder,M.A.OpticalRemotelySensedTimeSeriesDataforLandCoverClassification:AReview.ISPRS
J.Photogramm.RemoteSens.2016,116,55–72.[CrossRef]
12. Kennedy,R.E.;Yang,Z.;Cohen,W.B.;Pfaff,E.;Braaten,J.;Nelson,P.SpatialandTemporalPatternsofForestDisturbanceand
RegrowthwithintheAreaoftheNorthwestForestPlan.RemoteSens.Environ.2012,122,117–133.[CrossRef]
13. Zhu,Z.ChangeDetectionUsingLandsatTimeSeries:AReviewofFrequencies,Preprocessing,Algorithms,andApplications.
ISPRSJ.Photogramm.RemoteSens.2017,130,370–384.[CrossRef]
14. Kennedy, R.E.; Cohen, W.B.; Schroeder, T.A. Trajectory-Based Change Detection for Automated Characterization of Forest
DisturbanceDynamics.RemoteSens.Environ.2007,110,370–386.[CrossRef]

RemoteSens.2023,15,2963 21of23
15. Huang,C.;Goward,S.N.;Masek,J.G.;Thomas,N.;Zhu,Z.;Vogelmann,J.E.AnAutomatedApproachforReconstructingRecent
ForestDisturbanceHistoryUsingDenseLandsatTimeSeriesStacks.RemoteSens.Environ.2010,114,183–198.[CrossRef]
16. Kennedy,R.E.;Yang,Z.;Cohen,W.B.DetectingTrendsinForestDisturbanceandRecoveryUsingYearlyLandsatTimeSeries:1.
LandTrendr—TemporalSegmentationAlgorithms.RemoteSens.Environ.2010,114,2897–2910.[CrossRef]
17. Vogelmann,J.E.;Xian,G.;Homer,C.;Tolk,B.MonitoringGradualEcosystemChangeUsingLandsatTimeSeriesAnalyses:Case
StudiesinSelectedForestandRangelandEcosystems.RemoteSens.Environ.2012,122,92–105.[CrossRef]
18. Zhu,Z.;Woodcock,C.E.ContinuousChangeDetectionandClassificationofLandCoverUsingAllAvailableLandsatData.
RemoteSens.Environ.2014,144,152–171.[CrossRef]
19. DeVries,B.;Verbesselt,J.;Kooistra,L.;Herold,M.RobustMonitoringofSmall-ScaleForestDisturbancesinaTropicalMontane
ForestUsingLandsatTimeSeries.RemoteSens.Environ.2015,161,107–121.[CrossRef]
20. Ye,S.;Rogan,J.;Zhu,Z.;Eastman,J.R.ANear-Real-TimeApproachforMonitoringForestDisturbanceUsingLandsatTime
Series:StochasticContinuousChangeDetection.RemoteSens.Environ.2021,252,112167.[CrossRef]
21. Coops, N.C.; Shang, C.; Wulder, M.A.; White, J.C.; Hermosilla, T. Change in Forest Condition: Characterizing Non-Stand
ReplacingDisturbancesUsingTimeSeriesSatelliteImagery.For.Ecol.Manag.2020,474,118370.[CrossRef]
22. Healey,S.P.;Cohen,W.B.;Yang,Z.;KennethBrewer,C.;Brooks,E.B.;Gorelick,N.;Hernandez,A.J.;Huang,C.;JosephHughes,
M.;Kennedy,R.E.;etal.MappingForestChangeUsingStackedGeneralization:AnEnsembleApproach.RemoteSens.Environ.
2018,204,717–728.[CrossRef]
23. Hislop,S.;Jones,S.;Soto-Berelov,M.;Skidmore,A.;Haywood,A.;Nguyen,T.H.AFusionApproachtoForestDisturbance
MappingUsingTimeSeriesEnsembleTechniques.RemoteSens.Environ.2019,221,188–197.[CrossRef]
24. Zhu,Z.;Woodcock,C.E.;Olofsson,P.ContinuousMonitoringofForestDisturbanceUsingAllAvailableLandsatImagery.Remote
Sens.Environ.2012,122,75–91.[CrossRef]
25. Hansen,M.C.;Potapov,P.V.;Moore,R.;Hancher,M.;Turubanova,S.A.;Tyukavina,A.;Thau,D.;Stehman,S.V.;Goetz,S.J.;
Loveland,T.R.;etal.High-ResolutionGlobalMapsof21st-CenturyForestCoverChange.Science2013,342,850–853.[CrossRef]
26. Cohen,W.B.;Yang,Z.;Healey,S.P.;Kennedy,R.E.;Gorelick,N.ALandTrendrMultispectralEnsembleforForestDisturbance
Detection.RemoteSens.Environ.2018,205,131–140.[CrossRef]
27. McDowell,N.G.;Coops,N.C.;Beck,P.S.A.;Chambers,J.Q.;Gangodagamage,C.;Hicke,J.A.;Huang,C.;Kennedy,R.;Krofcheck,
D.J.;Litvak,M.;etal.GlobalSatelliteMonitoringofClimate-InducedVegetationDisturbances.TrendsPlantSci.2015,20,114–123.
[CrossRef]
28. Ma,L.;Liu,Y.;Zhang,X.;Ye,Y.;Yin,G.;Johnson,B.A.DeepLearninginRemoteSensingApplications:AMeta-Analysisand
Review.ISPRSJ.Photogramm.RemoteSens.2019,152,166–177.[CrossRef]
29. Khryashchev,V.;Larionov,R.WildfireSegmentationonSatelliteImagesUsingDeepLearning.InProceedingsofthe2020Moscow
WorkshoponElectronicandNetworkingTechnologies(MWENT),Moscow,Russia,11–13March2020;pp.1–5.
30. Kislov,D.E.;Korznikov,K.A.;Altman,J.;Vozmishcheva,A.S.;Krestov,P.V.ExtendingDeepLearningApproachesforForest
DisturbanceSegmentationonVeryHigh-ResolutionSatelliteImages.RemoteSens.Ecol.Conserv.2021,7,355–368.[CrossRef]
31. Zhu,Z.;Qiu,S.;Ye,S.RemoteSensingofLandChange: AMultifacetedPerspective. RemoteSens. Environ. 2022,282,113266.
[CrossRef]
32. Masolele,R.N.SpatialandTemporalDeepLearningMethodsforDerivingLand-UseFollowingDeforestation:APan-Tropical
CaseStudyUsingLandsatTimeSeries.RemoteSens.Environ.2021,264,112600.[CrossRef]
33. Zhong,L.;Hu,L.;Zhou,H.DeepLearningBasedMulti-TemporalCropClassification.RemoteSens.Environ.2019,221,430–443.
[CrossRef]
34. Garnot,V.S.F.;Landrieu,L.;Giordano,S.;Chehata,N.Time-SpaceTradeoffinDeepLearningModelsforCropClassificationon
SatelliteMulti-SpectralImageTimeSeries.InProceedingsoftheIGARSS2019—2019IEEEInternationalGeoscienceandRemote
SensingSymposium,Yokohama,Japan,28July–2August2019;pp.6247–6250.
35. Reddy,D.S.; Prasad,P.R.C.PredictionofVegetationDynamicsUsingNDVITimeSeriesDataandLSTM.Model. EarthSyst.
Environ.2018,4,409–419.[CrossRef]
36. Pelletier,C.;Webb,G.I.;Petitjean,F.TemporalConvolutionalNeuralNetworkfortheClassificationofSatelliteImageTimeSeries.
RemoteSens.2019,11,523.[CrossRef]
37. Lobert,F.;Holtgrave,A.-K.;Schwieder,M.;Pause,M.;Vogt,J.;Gocht,A.;Erasmi,S.MowingEventDetectioninPermanent
Grasslands:SystematicEvaluationofInputFeaturesfromSentinel-1,Sentinel-2,andLandsat8TimeSeries.RemoteSens.Environ.
2021,267,112751.[CrossRef]
38. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,L.;Polosukhin,I.AttentionIsAllYouNeed.In
Proceedingsofthe31stConferenceonNeuralInformationProcessingSystems(NIPS2017),LongBeach,CA,USA,4–9December
2017.
39. Devlin,J.;Chang,M.-W.;Lee,K.;Toutanova,K.BERT:Pre-TrainingofDeepBidirectionalTransformersforLanguageUnderstand-
ing.arXiv2019,arXiv:1810.04805.
40. Liu,Z.;Lin,Y.;Cao,Y.;Hu,H.;Wei,Y.;Zhang,Z.;Lin,S.;Guo,B.SwinTransformer: HierarchicalVisionTransformerUsing
ShiftedWindows.InProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision(ICCV),Montreal,BC,Canada,
11–17October2021;pp.10012–10022.

RemoteSens.2023,15,2963 22of23
41. Wu,N.;Green,B.;Ben,X.;O’Banion,S.DeepTransformerModelsforTimeSeriesForecasting:TheInfluenzaPrevalenceCase.
arXiv2020,arXiv:2001.08317.
42. Zerveas,G.;Jayaraman,S.;Patel,D.;Bhamidipaty,A.;Eickhoff,C.ATransformer-BasedFrameworkforMultivariateTimeSeries
RepresentationLearning;AssociationforComputingMachinery:NewYork,NY,USA,2021;pp.2114–2124.
43. Rußwurm,M.;Körner,M.Self-AttentionforRawOpticalSatelliteTimeSeriesClassification.ISPRSJ.Photogramm.RemoteSens.
2020,169,421–435.[CrossRef]
44. Woodcock,C.E.;Allen,R.;Anderson,M.;Belward,A.;Bindschadler,R.;Cohen,W.;Gao,F.;Goward,S.N.;Helder,D.;Helmer,E.;
etal.FreeAccesstoLandsatImagery.Science2008,320,1011.[CrossRef]
45. Zhu,M.;He,Y.;He,Q.AReviewofResearchesonDeepLearninginRemoteSensingApplication.Int.J.Geosci.2019,10,1–11.
[CrossRef]
46. Schäfer,P.TheBOSSIsConcernedwithTimeSeriesClassificationinthePresenceofNoise. DataMin. Knowl. Disc. 2015,29,
1505–1530.[CrossRef]
47. Roychowdhury,S.;Diligenti,M.;Gori,M.RegularizingDeepNetworkswithPriorKnowledge:AConstraint-BasedApproach.
Knowl.-BasedSyst.2021,222,106989.[CrossRef]
48. Zhang,L.;Wang,S.;Liu,H.;Lin,Y.;Wang,J.;Zhu,M.;Gao,L.;Tong,Q.FromSpectrumtoSpectrotemporal:ResearchonTime
SeriesChangeDetectionofRemoteSensing.Geomat.Inf.Sci.WuhanUniv.2021,46,451–468.[CrossRef]
49. Rodriguez,E.;Morris,C.S.;Belz,J.E.AGlobalAssessmentoftheSRTMPerformance.Photogramm.Eng.Remote.Sens.2006,72,
249–260.[CrossRef]
50. Potapov,P.;Li,X.;Hernandez-Serna,A.;Tyukavina,A.;Hansen,M.C.;Kommareddy,A.;Pickens,A.;Turubanova,S.;Tang,H.;
Silva,C.E.;etal.MappingGlobalForestCanopyHeightthroughIntegrationofGEDIandLandsatData.RemoteSens.Environ.
2021,253,112165.[CrossRef]
51. White,J.C.;Wulder,M.A.;Hobart,G.W.;Luther,J.E.;Hermosilla,T.;Griffiths,P.;Coops,N.C.;Hall,R.J.;Hostert,P.;Dyk,A.;
etal.Pixel-BasedImageCompositingforLarge-AreaDenseTimeSeriesApplicationsandScience.Can.J.RemoteSens.2014,40,
192–212.[CrossRef]
52. Masek,J.G.;Vermote,E.F.;Saleous,N.E.;Wolfe,R.;Hall,F.G.;Huemmrich,K.F.;Gao,F.;Kutler,J.;Lim,T.-K.ALandsatSurface
ReflectanceDatasetforNorthAmerica,1990–2000.IEEEGeosci.RemoteSens.Lett.2006,3,68–72.[CrossRef]
53. Lunetta,R.S.;Johnson,D.M.;Lyon,J.G.;Crotwell,J.ImpactsofImageryTemporalFrequencyonLand-CoverChangeDetection
Monitoring.RemoteSens.Environ.2004,89,444–454.[CrossRef]
54. Zhu,Z.;Woodcock,C.E.Object-BasedCloudandCloudShadowDetectioninLandsatImagery.RemoteSens.Environ.2012,118,
83–94.[CrossRef]
55. FRANKLIN,J.ThematicMapperAnalysisofConiferousForestStructureandComposition.Int.J.RemoteSens.1986,7,1287–1301.
[CrossRef]
56. Spanner,M.A.;Pierce,L.L.;Peterson,D.L.;Running,S.W.RemoteSensingofTemperateConiferousForestLeafAreaIndex
TheInfluenceofCanopyClosure,UnderstoryVegetationandBackgroundReflectance. Int. J.Remote. Sens. 1990,11,95–111.
[CrossRef]
57. Li,P.;Jiang,L.;Feng,Z.Cross-ComparisonofVegetationIndicesDerivedfromLandsat-7EnhancedThematicMapperPlus
(ETM+)andLandsat-8OperationalLandImager(OLI)Sensors.RemoteSens.2014,6,310–329.[CrossRef]
58. Cardille,J.A.;Perez,E.;Crowley,M.A.;Wulder,M.A.;White,J.C.;Hermosilla,T.Multi-SensorChangeDetectionforwithin-Year
CaptureandLabellingofForestDisturbance.RemoteSens.Environ.2022,268,112741.[CrossRef]
59. Huo,L.-Z.;Boschetti,L.;Sparks,A.M.Object-BasedClassificationofForestDisturbanceTypesintheConterminousUnitedStates.
RemoteSens.2019,11,477.[CrossRef]
60. Pugh,T.A.M.;Arneth,A.;Kautz,M.;Poulter,B.;Smith,B.ImportantRoleofForestDisturbancesintheGlobalBiomassTurnover
andCarbonSinks.Nat.Geosci.2019,12,730–735.[CrossRef][PubMed]
61. Senf,C.;Seidl,R.MappingtheForestDisturbanceRegimesofEurope.Nat.Sustain.2021,4,63–70.[CrossRef]
62. Lovric´,M.;Milanovic´,M.;Stamenkovic´,M.AlgoritmicMethodsforSegmentationofTimeSeries:AnOverview.J.Contemp.Econ.
Bus.Issues2014,1,31–53.
63. DeVries,B.;Decuyper,M.;Verbesselt,J.;Zeileis,A.;Herold,M.;Joseph,S.TrackingDisturbance-RegrowthDynamicsinTropical
ForestsUsingStructuralChangeDetectionandLandsatTimeSeries.RemoteSens.Environ.2015,169,320–334.[CrossRef]
64. Goodfellow,I.;Bengio,Y.;Courville,A.DeepLearning;MITPress:Cambridge,MA,USA,2016.
65. Kingma,D.P.;Ba,J.Adam:AMethodforStochasticOptimization.arXiv2014,arXiv:1412.6980.
66. Gorelick,N.;Hancher,M.;Dixon,M.;Ilyushchenko,S.;Thau,D.;Moore,R.GoogleEarthEngine:Planetary-ScaleGeospatial
AnalysisforEveryone.RemoteSens.Environ.2017,202,18–27.[CrossRef]
67. Audley,J.P.;Fettig,C.J.;StevenMunson,A.;Runyon,J.B.;Mortenson,L.A.;Steed,B.E.;Gibson,K.E.;Jørgensen,C.L.;McKelvey,
S.R.;McMillin,J.D.;etal.ImpactsofMountainPineBeetleOutbreaksonLodgepolePineForestsintheIntermountainWest,U.S.,
2004–2019.For.Ecol.Manag.2020,475,118403.[CrossRef]
68. Berner,L.T.;Law,B.E.;Meddens,A.J.H.;Hicke,J.A.TreeMortalityfromFires,BarkBeetles,andTimberHarvestduringaHotand
DryDecadeintheWesternUnitedStates(2003–2012).Environ.Res.Lett.2017,12,065005.[CrossRef]
69. Kennedy,R.E.;Yang,Z.;Gorelick,N.;Braaten,J.;Cavalcante,L.;Cohen,W.B.;Healey,S.ImplementationoftheLandTrendr
AlgorithmonGoogleEarthEngine.RemoteSens.2018,10,691.[CrossRef]

RemoteSens.2023,15,2963 23of23
70. Giannetti,F.;Pegna,R.;Francini,S.;McRoberts,R.E.;Travaglini,D.;Marchetti,M.;ScarasciaMugnozza,G.;Chirici,G.ANew
MethodforAutomatedClearcutDisturbanceDetectioninMediterraneanCoppiceForestsUsingLandsatTimeSeries.Remote
Sens.2020,12,3720.[CrossRef]
71. Potapov,P.V.;Turubanova,S.A.;Hansen,M.C.;Adusei,B.;Broich,M.;Altstatt,A.;Mane,L.;Justice,C.O.QuantifyingForest
CoverLossinDemocraticRepublicoftheCongo,2000–2010,withLandsatETM+Data.RemoteSens.Environ.2012,122,106–116.
[CrossRef]
72. Hamdi,Z.M.;Brandmeier,M.;Straub,C.ForestDamageAssessmentUsingDeepLearningonHighResolutionRemoteSensing
Data.RemoteSens.2019,11,1976.[CrossRef]
73. Kong,Y.-L.;Huang,Q.;Wang,C.;Chen,J.;Chen,J.;He,D.LongShort-TermMemoryNeuralNetworksforOnlineDisturbance
DetectioninSatelliteImageTimeSeries.RemoteSens.2018,10,452.[CrossRef]
74. Zhou,G.;Liu,M.;Liu,X.AnAutoencoder-BasedModelforForestDisturbanceDetectionUsingLandsatTimeSeriesData.Int.J.
Digit.Earth2021,14,1087–1102.[CrossRef]
75. Zhao,F.;Sun,R.;Zhong,L.;Meng,R.;Huang,C.;Zeng,X.;Wang,M.;Li,Y.;Wang,Z.MonthlyMappingofForestHarvesting
UsingDenseTimeSeriesSentinel-1SARImageryandDeepLearning.RemoteSens.Environ.2022,269,112822.[CrossRef]
76. Lu,J.;Huang,C.;Tao,X.;Gong,W.;Schleeweis,K.AnnualForestDisturbanceIntensityMappedUsingLandsatTimeSeriesand
FieldInventoryDatafortheConterminousUnitedStates(1986–2015).RemoteSens.Environ.2022,275,113003.[CrossRef]
77. Wu,L.;Liu,X.;Liu,M.;Yang,J.;Zhu,L.;Zhou,B.OnlineForestDisturbanceDetectionattheSub-AnnualScaleUsingSpatial
ContextFromSparseLandsatTimeSeries.IEEETrans.Geosci.RemoteSens.2022,60,1–14.[CrossRef]
78. Cohen,W.B.;Healey,S.P.;Yang,Z.;Stehman,S.V.;Brewer,C.K.;Brooks,E.B.;Gorelick,N.;Huang,C.;Hughes,M.J.;Kennedy,
R.E.;etal.HowSimilarAreForestDisturbanceMapsDerivedfromDifferentLandsatTimeSeriesAlgorithms?Forests2017,8,98.
[CrossRef]
79. Curtis,P.G.;Slay,C.M.;Harris,N.L.;Tyukavina,A.;Hansen,M.C.ClassifyingDriversofGlobalForestLoss.Science2018,361,
1108–1111.[CrossRef][PubMed]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.