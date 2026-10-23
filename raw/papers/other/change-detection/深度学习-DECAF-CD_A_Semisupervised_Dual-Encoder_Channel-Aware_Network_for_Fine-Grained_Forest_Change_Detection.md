IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19, 2026 12687
|     | DECAF-CD: |               |     |        | A   | Semisupervised |     |           |              | Dual-Encoder |     |     |     |     |
| --- | --------- | ------------- | --- | ------ | --- | -------------- | --- | --------- | ------------ | ------------ | --- | --- | --- | --- |
|     |           | Channel-Aware |     |        |     | Network        |     | for       | Fine-Grained |              |     |     |     |     |
|     |           |               |     | Forest |     | Change         |     | Detection |              |              |     |     |     |     |
JingheZhou ,JinmeiShi ,Member,IEEE,XianPengWang ,Member,IEEE,
XingwangLi ,SeniorMember,IEEE,JianglinLuo,andYu-BengLeau ,SeniorMember,IEEE
Abstract—Accurateforestchangedetection(CD)iscrucialfor outperforms seven state-of-the-art semisupervised CD methods
ecosystemhealthmonitoring,deforestationanddegradationassess- consistentlyacrossannotationratiosfrom5%to40%.Themodel
ment,andsustainablelarge-scaleforestmanagement.However,for- evensurpassesfullysupervisedmethods,whilefurthervalidating
estchangedetectionremainshighlychallengingduetostrongspec- the strong generalization capability of the proposed framework.
tralsimilarityamongvegetationtypes,irregularandfragmented Notably,DECAF-CDlowersannotationrequirementbyasmuch
geometryofdisturbances,blurredcanopyboundaries,andasevere as87.5%forallevaluateddatasets.Thelargestperformanceim-
scarcity of high-quality annotations. Acquiring labeled data is provementsareseenontheRF-CDdataset,whereweakspectral
costlyandlabor-intensive,typicallyrequiringexpertinterpretation contrastandirregularboundarystructuresmakethedetectionof
ofhigh-resolutionimagery,whichlimitsthescalabilityandgeneral- fine-grained forest disturbances especially difficult, which high-
izationoffullysupervisedmodels.Toaddresstheselimitations,we lightstheeffectivenessofourmethodintacklingthechallenging
| proposedual-encoderchannel-awareforestchangedetectionnet- |     |     |     |     |     |     | forestscenarios. |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
work(DECAF-CD),asemisuperviseddeeplearningframeworkfor
|     |     |     |     |     |     |     | Index | Terms—Change |     | detection | (CD), | channel-aware, |     | dual- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --------- | ----- | -------------- | --- | ----- |
fine-grainedforestCD.Thisframeworkjointlyleveragestemporal
encoder,semisupervised.
alignment,multiscalestructuralaggregation,andboundary-aware
modelingtocapturesubtleandirregularforestdisturbanceswhile
| effectively | utilizing | unlabeled | data. | Specifically, |     | the framework |     |     |     |     |     |     |     |     |
| ----------- | --------- | --------- | ----- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
first,alignsbitemporalfeaturestosuppresspseudochanges,second, I. INTRODUCTION
| aggregates | multiscale | structural | cues | to  | distinguish | complex dis- |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ---------- | ---- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ACCURATE
turbancepatterns,andthird,refinesobjectboundariestoenhance monitoring of forest disturbances is essen-
spatialcoherence,allwithinasemisupervisedlearningparadigm tial for assessing ecosystem health, evaluating the im-
thatsignificantlyreducesrelianceonscarceannotations.Extensive pacts of deforestation and forest degradation, and supporting
| experiments |     | on five benchmark | datasets |     | show | that DECAF-CD |             |        |             |     |     |         |               |     |
| ----------- | --- | ----------------- | -------- | --- | ---- | ------------- | ----------- | ------ | ----------- | --- | --- | ------- | ------------- | --- |
|             |     |                   |          |     |      |               | sustainable | forest | management. |     | The | growing | accessibility | of  |
high-resolutionremotesensingimagery,coupledwithadvances
Received7December2025;revised22February2026;accepted21March in deep learning, presents unprecedented opportunities for au-
2026.Dateofpublication24March2026;dateofcurrentversion21April2026. tomated forest [1]. Unlike traditional manual delineation and
Thisworkwassupportedinpartbythe“NewStaroftheSouthChinaSea” on-sitesurveys,whicharecharacterizedbylaborintensity,time
ScienceandTechnologyInnovationTalentPlatformProjectinHainanProvince
|     |     |     |     |     |     |     | consumption, |     | and difficulty |     | in scaling, | automated | approaches |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | ----------- | --------- | ---------- | --- |
ofChinaunderGrantNHXXRCXM202321andGrantJYNHXX2023-14Qand
inpartbytheNaturalScienceFoundationofHainanProvinceinChinaunder are capable of facilitating continuous, large-scale monitoring,
Grant624QN283.(Correspondingauthors:JinmeiShi;XianPengWang.)
|     |     |     |     |     |     |     | and | timely detection |     | of both | natural | disturbances | and | anthro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------- | ------------ | --- | ------- |
JingheZhouiswiththeFacultyofComputingandInformatics,Universiti
pogenicactivities[2].Thesetechnologicaladvanceslayasolid
MalaysiaSabah,KotaKinabalu88400,Malaysia,alsowiththeSchoolofInfor-
foundationforaddressingtheintricatespatiotemporaldynamics
mationEngineering,HainanVocationalUniversityofScienceandTechnology,
Haikou570100,China,andalsowiththeHainanProvinceWisdomInternet
|           |             |                |     |          |         |                   | inherent | in forest | ecosystems, |     | which | remain | challenging | for |
| --------- | ----------- | -------------- | --- | -------- | ------- | ----------------- | -------- | --------- | ----------- | --- | ----- | ------ | ----------- | --- |
| of Things | Engineering | and Technology |     | Research | Center, | Hainan Vocational |          |           |             |     |       |        |             |     |
conventionalremotesensingtechniques.
UniversityofScienceandTechnology,Haikou570100,China(e-mail:chau-
|     |     |     |     |     |     |     | Forest | change | detection |     | (CD) presents | unique | challenges |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | --- | ------------- | ------ | ---------- | --- |
jhe@163.com).
JinmeiShiandJianglinLuoarewiththeSchoolofInformationEngineering, that are distinct from urban or built-up change analysis. First,
| Hainan | Vocational | University of | Science | and Technology, |     | Haikou 570100, |     |     |     |     |     |     |     |     |
| ------ | ---------- | ------------- | ------- | --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
forestlandscapesarehighlyheterogeneousandexhibitcomplex
China,andalsowiththeHainanProvinceWisdomInternetofThingsEngineer-
ingandTechnologyResearchCenter,HainanVocationalUniversityofScience spatial patterns, with disturbances spanning a wide spectrum,
andTechnology,Haikou570100,China(e-mail:Shijinmei1003@hvust.edu.cn; fromselectiveloggingandnarrowaccessroadstocanopygaps
leal_ljl@163.com). andlargeclear-cuts[3].Second,spectralvariabilitycausedby
| XianPeng | Wang | is with the | School | of Information |     | and Communica- |     |     |     |     |     |     |     |     |
| -------- | ---- | ----------- | ------ | -------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tion Engineering, Hainan University, Haikou 570228, China (e-mail: wx- seasonal phenology and illumination effects complicates the
peng2016@hainanu.edu.cn). discrimination between genuine changes and pseudochanges,
| Xingwang |     | Li is with the School | of  | Physics | and Electronic | Information |     |     |     |     |     |     |     |     |
| -------- | --- | --------------------- | --- | ------- | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Engineering, Henan Polytechnic University, Jiaozuo 454000, China (e-mail: particularly among forests, low vegetation, and croplands [4].
lixingwangbupt@gmail.com). Third, changes occur across multiple spatial scales, requiring
Yu-Beng Leau is with the Faculty of Computing and Informatics, modelscapableofcapturingbothfinedetailsandbroadercontex-
| Universiti | Malaysia | Sabah, Kota | Kinabalu | 88400, | Malaysia | (e-mail: ly- |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | -------- | ------ | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tualstructures[5].Finally,andmostcritically,annotateddatasets
beng@ums.edu.my).
DigitalObjectIdentifier10.1109/JSTARS.2026.3677133 forforestdisturbancesareextremelylimited,especiallyforrare
©2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.Formoreinformation,see
https://creativecommons.org/licenses/by-nc-nd/4.0/

12688 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
orsmall-scaleevents,whichseverelyrestrictstheeffectiveness extensively employed in bitemporal imagery, enabling hierar-
andgeneralizationcapacityofpurelysupervisedapproaches[6]. chical feature extraction and robust modeling of spatial pat-
Amongthesechallenges,thescarcityoflabeleddatarepresents terns[10].Comparedwithtraditionalpixel-wiseorobject-based
theprimarybottleneckforadvancingforestCD. methods,deeplearningmodelspossessthecapabilitytodiscern
Existingdeeplearning-basedCDmethodologieshavedemon- intricate semantic discrepancies between pre- and postevent
stratedexceptionalperformanceinurbanandland-covermon- images, improving the detection of subtle or heterogeneous
itoring endeavors [7]. However, these methods are frequently changes. The integration of attention mechanisms, multiscale
devised for general CD or fully supervised settings and fail featureaggregation,andfeaturefusionstrategieshasfurtheren-
toaddressthespecificcomplexitiesofforestenvironments[8]. hancedthediscriminativecapacityofthesenetworks,allowing
Inparticular,fewframeworksexplicitlyconfrontthecombined them to capture long-range dependencies and subtle structural
challenges posed by irregular forest morphologies, multiscale variations. Nevertheless, the majority of early-stage methods
heterogeneity, ambiguous boundaries, and scarce annotations. weredesignedforurbanoranthropogenicenvironments,where
Consequently, a substantial research gap persists for the de- targets exhibit homogeneous textures, regular geometries, and
velopmentofadedicated,annotation-efficient,semisupervised spatiallydiscretechanges.Whendeployedinforestecosystems,
frameworkthattailoredforfine-grainedforestCD. these models frequently encounter challenges in effectively
To address this gap, we introduce a semisupervised deep managingirregularmorphologies,multiscaledisturbances,and
learning framework specifically designed for forest CD. The diffuseboundaries,therebylimitingtheirpracticalapplicability
proposed network amalgamates three pivotal modules to sur- forlarge-scaleecologicalmonitoring.
mount the aforementioned challenges: a dual-branch encoder
equippedwithglobalattentionfusion(GAF)mechanism,which B. ChallengesinForestCD
is designed for temporal alignment and suppression of pseu-
Forest CD presents a series of distinctive challenges that
dochanges; a cross-scale group-concat (CGC) module, aug-
are largely absent in urban or built-up areas. First, spectral
mentedwithlargekernelattention(LKA),tocaptureirregular
variabilitystemmingfromseasonalphenologyorenvironmental
and multiscale forest disturbances while enforcing boundary
conditionscaninducepseudochanges,consequentlyresultingin
consistency;andamultipathdilateddecoder(MDD)toprogres-
elevated false-positive rates [11], [12]. Second, natural distur-
sivelyrefinemultiscalefeatures,therebyenablingprecisedelin-
bances, such as selective logging, wildfires, pest infestations,
eation.Furthermore,theframeworkisfurtherfortifiedbyincor-
and canopy regeneration, generate irregular, fragmented, and
porating a teacher–student semisupervised learning paradigm,
elongatedspatialpatterns,therebycomplicatingprecisebound-
which empowers the network to leverage unlabeled data and
ary delineation [6]. Third, forest disturbances manifest across
attainsuperiorperformancewithminimalannotatedsamples.
multiplescales,rangingfromnarrowloggingroadstoextensive
The principal contributions of this work are summarized as
clear-cuts, requiring models to concurrently capture both fine-
follows.
and coarse-grained structures features [13], [14]. Finally, the
1) We propose dual-encoder channel-aware forest change
scarcity of accurately annotated datasets, particularly for rare
detection network (DECAF-CD), an annotation-efficient
orsmall-scaledisturbances,constraintheeffectivenessoffully
semisupervisedframeworktailoredforforestCD,which
supervisedmethodsandchallengesmodelgeneralization[15],
attainsperformancelevelscomparabletofullysupervised
[16].Thesefactorsemphasizetheneedtodeveloparchitectures
approaches, with only a small fraction of labeled data,
that are both structurally cognizant and temporally consistent
therebysubstantiallyreducingtheannotationworkload.
whileremainingefficientundersemisupervisedconditions.
2) We design a GAF module specifically engineered for
channel-leveltemporalalignment,whicheffectivelymit-
C. MultiscaleandBoundary-AwareMethods
igatespseudochangesinducedbyillumination,shadows,
andphenologicalvariations. Toaddressthechallengesposedbyheterogeneousandmulti-
3) WedevelopaCGCmoduleintegratedwithLKAtocap- scalechangepatterns,recentapproacheshaveincorporatedmul-
ture irregular and multiscale disturbance patterns while tiscalefeaturefusion,attention-basedmodeling,andboundary
enhancingboundaryconsistency. enhancement. Multiscale networks amalgamate low-level spa-
4) Extensiveexperimentsonbenchmarkdatasetssubstantiate tialdetailswithhigh-levelsemanticcontext,enablingdetection
the efficacy of the proposed framework, achieving com- of both minor and extensive changes [17], [18]. Edge-aware
petitiveperformancewithareductionofupto87.5%inthe modules or mechanisms with large receptive fields improve
numberoflabeledsamplesrequired,therebyhighlighting boundaryprecision,enablingthecaptureofirregularanddiffuse
itspracticalviabilityforlarge-scaleforestmonitoring. forest edges [19], [20]. Although these methods advance the
state-of-the-art,themajorityofexistingarchitectureseithercon-
II. RELATEDWORK centrateonasingularaspect,suchasmultiscaleaggregationand
edgemodeling,orrelyheavilyonlabeleddataandpostprocess-
A. DeepLearningforRemoteSensingCD
ing procedures, which consequently restricts their robustness
The emergence of deep learning has revolutionized the andannotationefficiencyincomplexnaturalenvironments.
paradigmofremotesensingCD[9].Convolutionalneuralnet- Channel attention mechanisms, such as SENet, re-
works (CNNs) and encoder–decoder architectures have been calibrate channel-wise feature responses for single-image

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12689
representationsbutfailtoaccountforthecross-temporalnature Fig.1,theframeworkprocessespre-andposteventimagesthat
inherentinbitemporalCD.TheproposedGAFmoduleextends arecoregisteredusingadual-encoderbackbonetoextractmulti-
thisparadigmtoconcatenatedbitemporalfeaturemaps,enabling leveltemporalfeatures.Channelblocksareusedtorefinethefea-
temporal-awarechannelrecalibrationthatadaptivelysuppresses turerepresentationsbyincreasingdiscriminativeresponsesand
pseudochanges arising from illumination shifts and seasonal reducingtheirrelevantinformation.Afterward,aGAFmodule
variations. For cross-scale feature fusion, existing methods, restructures and fuses cross-level features. The fused features
such as FPN and ASPP aggregate multiscale context indepen- are further modeled by a CGC module coupled with LKA,
dentlyateachscale,withoutexplicitlymodelingtheelongated whichallowsgoodmultiscalecontextualaggregationandspatial
and anisotropic spatial patterns characteristic of forest distur- dependencymodeling.Theresultingfeaturerepresentationsare
bances. The LKA offers an efficient mechanism for capturing thenfedtoanMDDmodulethatfocusesontemporaldiscrepan-
long-range dependencies through decomposed depth-wise op- ciesbetweenbitemporalinputs.Finally,asegmentationheadis
erations. However, it has not been applied within a grouped usedtogeneratethefine-grainedforestdisturbancemaps,which
cross-scalefusioncontext.TheproposedCGCmoduleaddresses arefollowedbypostprocessingrefinementtoenhancethespatial
thisgapbyembeddingLKAintoagroupedcross-scaleconcate- consistency and boundary delineation. To further improve ro-
nation framework, specifically designed to capture the long- bustnessandreducerelianceondenseannotations,DECAF-CD
range spatial dependencies along irregular forest boundaries adoptsateacher–studentsemisupervisedstrategy,whichenables
that isotropic single-scale convolutions are inherently limited the model to leverage abundant unlabeled bitemporal images
inrepresenting. throughpseudolabelguidanceandconsistencyregularization.
|     |     |     |     |     |     |     | Givenapre-eventimageI |     |     |     | andaposteventimageI |     |     |     | ,the |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |                       |     |     |     | pre                 |     |     |     | post |
dualencodersextractmultilevelfeaturerepresentations
D. SemisupervisedLearningforLimitedAnnotations
|                                                       |     |     |     |     |     |     |     |     | (cid:2)    |     | (cid:3) |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | --- | --- | --- |
| Thescarcityoflabeleddatasetshasmotivatedtheadoptionof |     |     |     |     |     |     |     |     |            |     | 4       |     |     |     |     |
|                                                       |     |     |     |     |     |     |     |     | Fpre,Fpost |     | =E(I    | ,I  | ).  |     | (1) |
semisupervised learning strategies within the realm of remote pre post
|          |                     |     |            |     |             |               |       |          | l   | l         | l=1 |         |        |     |         |
| -------- | ------------------- | --- | ---------- | --- | ----------- | ------------- | ----- | -------- | --- | --------- | --- | ------- | ------ | --- | ------- |
| sensing  | CD. Teacher–student |     | paradigms, |     | consistency | regular-      |       |          |     |           |     |         |        |     |         |
|          |                     |     |            |     |             |               | These | features | are | processed | by  | the GAF | module |     | to pro- |
| ization, | and pseudolabeling  |     | techniques |     | have        | been employed |       |          |     |           |     |         |        |     |         |
duceadaptivediscrepancy-awarerepresentationsthatemphasize
| to leverage    | unlabeled    | samples, |       | thereby     | effectively | diminish-     |          |         |          |                  |     |           |     |             |      |
| -------------- | ------------ | -------- | ----- | ----------- | ----------- | ------------- | -------- | ------- | -------- | ---------------- | --- | --------- | --- | ----------- | ---- |
|                |              |          |       |             |             |               | temporal | changes | while    | suppressing      |     | unchanged |     | background. |      |
| ing annotation | requirements |          | while | maintaining |             | model perfor- |          |         |          |                  |     |           |     |             |      |
|                |              |          |       |             |             |               | The      | refined | features | are subsequently |     | enhanced  |     | by the      | CGC- |
mance[21],[22].Theseapproacheshavedemonstratedpromis-
LKAmodule,wherechannelreweightingandlarge-kernelfields
| ing results | in urban | and | building-change |     | datasets. | However, |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
jointlyenhancedisturbedforeststructuresandboundaryclarity.
theirefficacyinhighlyheterogeneousandspectrallyambiguous
|     |     |     |     |     |     |     | Ultimately, |     | the MDD | modulea | multidimensional |     |     | decoder | pro- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------- | ---------------- | --- | --- | ------- | ---- |
forestecosystemsremainsconstrained.Theabsenceofexplicit
gressivelyaggregatescross-scaleinformationtoreconstructsa
structural priors in numerous semisupervised frameworks can ˆ
fine-grainedchangemapY.
leadtounstablepredictionsorlossoffine-graineddetailswhen
T
|     |     |     |     |     |     |     | During | the | semisupervised |     | learning, | the | teacher | network |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------- | --- | --------- | --- | ------- | ------- | --- |
addressingirregularnaturaldisturbances[23],[24].
generatessoftpseudolabelsforunlabeledsamples
|     |     |     |     |     |     |     |     |     | (cid:4) |     |     | (cid:5) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- | --- |
E. MotivationfortheProposedFramework ˜ =T {Fpre,Fpost}4 ˜ ∈[0,1]H×W
|          |      |       |               |     |              |           |     | Y   |     |     | l=1 | , Y |     |     | (2) |
| -------- | ---- | ----- | ------------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |      |       |               |     |              |           |     |     |     | l l |     |     |     |     |     |
| Building | upon | these | observations, |     | an effective | forest CD |     |     |     |     |     |     |     |     |     |
model must jointly address temporal misalignment, spectral whilethestudentnetworkSisoptimizedthroughtheutilization
ambiguity,multiscaleheterogeneity,andboundaryirregularity, of both supervised and unsupervised consistency losses. The
while efficiently leveraging limited labeled data. Our frame- teacherparametersareupdatedviaexponentialmovingaverage
(EMA)
| work integrates | these       | requirements |         | into        | a unified | architecture |     |     |     |     |         |     |     |     |     |
| --------------- | ----------- | ------------ | ------- | ----------- | --------- | ------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
| by combining    | dual-branch |              | feature | extraction, |           | GAF for tem- |     |     |     |     |         |     |     |     |     |
|                 |             |              |         |             |           |              |     |     |     | ←αθ | +(1−α)θ |     |     |     |     |
poral alignment, CGC enhanced with LKA for structural and θ T T S . (3)
boundary-awarefeatureaggregation,andanMDDforprogres-
|     |     |     |     |     |     |     | This | EMA-based |     | update | stabilizes | pseudolabel |     | quality | and |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | ------ | ---------- | ----------- | --- | ------- | --- |
siverefinementofchangepredictions(CPs).Thesemisupervised
|     |     |     |     |     |     |     | circumvents |     | confirmation |     | bias. | This integrated |     | framework |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | --------------- | --- | --------- | --- |
teacher–studentstrategyfurtherensuresrobustlearninginlow- enables DECAF-CD to effectively learn disturbance patterns,
| annotation | scenarios. | This | integrated | design | explicitly | targets |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ---- | ---------- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sharpenboundaries,andgeneralizeacrossdiverseforestecosys-
thekeychallengesidentifiedinSectionsII-B–II-D,establishing
temsdespitelimitedmanualannotations.
| a clear foundation |     | for the | detailed | architectural |     | description | in  |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | -------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SectionIII.
B. Dual-EncoderFeatureExtractionandGAF
III. MATERIALANDMETHODS Discerning authentic forest disturbances from seasonal or
|     |     |     |     |     |     |     | phenological |     | variations | is  | arduous | due to | the interference |     | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------- | ------ | ---------------- | --- | --- |
A. OverallArchitecture
|     |     |     |     |     |     |     | illumination, |     | shadow, | and | atmospheric | noise. | The | acquisition |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | ----------- | ------ | --- | ----------- | --- |
The proposed DECAF-CD is a semisupervised framework of both fine-grained spectral details and high-level semantic
designedforfine-grainedforestCDunderlimitedlabeleddata contextisimperativeformitigatingpseudochangesandretaining
andhighlyheterogeneousforestenvironments.Asillustratedin pertinenttemporalinformation[25].

12690 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
Fig.1. OverviewoftheproposedDECAF-CDnetwork.Theframeworkintegratesadual-encoderbackboneforbitemporalrepresentationlearning,aGAFmodule
forcross-temporalinteraction,aCGCblockwithLKAforglobal-localsemanticenhancement,andamultidimensionaldecodercalledMDDforhigh-resolution
reconstruction.
features
(cid:4)
|     |     |     |     | F ,F =E(I | ),E(I    | ), i=1,...,4 | (4) |
| --- | --- | --- | --- | --------- | -------- | ------------ | --- |
|     |     |     |     | i i       | pre post |              |     |
andF(cid:4)denotethepre-and
whereiindexesthefeaturescale,F
|     |     |     |                                           |     |     | i i        |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | ---------- | --- |
|     |     |     | posteventfeaturemapswithchanneldimensionC |     |     | andspatial |     |
i
×W
|     |     |     | dimensions | H i i . | To enhance | temporal consistency | and |
| --- | --- | --- | ---------- | ------- | ---------- | -------------------- | --- |
suppresspseudochanges,theGAFmoduleconcatenatesfeatures
channel-wise
|     |     |     |     | ˜     | (cid:4)]∈R2Ci | ×Hi ×Wi |     |
| --- | --- | --- | --- | ----- | ------------- | ------- | --- |
|     |     |     |     | Z =[F | ,F            |         | (5) |
|     |     |     |     | i     | i i           |         |     |
andgeneratesachannel-wiseattentionmapviaglobalpooling
andsoftmaxnormalization
|                                    |     |     |            | (cid:6) | (cid:7) |                 |     |
| ---------------------------------- | --- | --- | ---------- | ------- | ------- | --------------- | --- |
|                                    |     |     |            |         | ˜ ∈R2Ci | ×1×1 ˆ ˜        |     |
|                                    |     |     | α =Softmax | Pool(Z  | )       | , Z =Z (cid:5)α | (6) |
| Fig.2. ArchitectureoftheGAFmodule. |     |     | i          |         | i       | i i             | i   |
where(cid:5)denoteselement-wisemultiplication.Finally,thefused
featuresareprojectedthroughachannelblock
| As presented | in Fig. 2, DECAF-CD | employs a dual-branch |     |     |        |      |     |
| ------------ | ------------------- | --------------------- | --- | --- | ------ | ---- | --- |
|              |                     |                       |     |     | =σ(W ˆ | +b ) |     |
encoder with shared weights to extract multilevel bitemporal x Z (7)
|     |     |     |     |     | i i i | i   |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12691
| whereW                                | ,b arelearnableweightsandσistheSiLUactivation |     |     |     |                    |     |     |     |     |     |
| ------------------------------------- | --------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
|                                       | i i                                           |     |     |     |                    |     |     |     |     |     |
| function.Allfusedfeatures{x1,x2,x3,x4 |                                               |     |     |     | }areresizedtoauni- |     |     |     |     |     |
fiedspatialresolutionH/16×W/16forsubsequentmultiscale
processing.
Thedual-encoderwithGAFprovidesdiscrepancy-awareand
temporallyalignedfeaturesthateffectivelydistinguishgenuine
forestdisturbanceswhilesuppressingpseudochangesfromsea-
sonaloratmosphericvariations.
C. CGC-LKAModule
| Forest | disturbances |     | exhibit | irregular | and | multiscale | hetero- |     |     |     |
| ------ | ------------ | --- | ------- | --------- | --- | ---------- | ------- | --- | --- | --- |
geneity.Capturinglong-rangedependenciesandaligningmul-
| tiscale features             |     | are crucial                           | for | detecting  |          | subtle changes | and     |     |     |     |
| ---------------------------- | --- | ------------------------------------- | --- | ---------- | -------- | -------------- | ------- | --- | --- | --- |
| enhancingboundarydelineation |     |                                       |     | [26],[27]. |          |                |         |     |     |     |
| The structure                |     | of the                                | LKA | module     | is shown | in Fig.        | 3. Each |     |     |     |
| fusedfeaturex                |     | isrefinedviaLKA,whichdecomposesalarge |     |            |          |                |         |     |     |     |
i
convolutionalkernelintodepth-wiseandpoint-wiseoperations
tocapturelong-rangespatialdependencies
|             |          |     | ←LKA(x   |             | ).  |           |          |     |     |     |
| ----------- | -------- | --- | -------- | ----------- | --- | --------- | -------- | --- | --- | --- |
|             |          |     | x        |             |     |           | (8)      |     |     |     |
|             |          |     | i        |             | i   |           |          |     |     |     |
| The refined | features |     | are then | partitioned |     | into four | nonover- |     |     |     |
lappingchannelgroups
|     |     | x ={x | [0],x | [1],x | [2],x | [3]}, |     |     |     |     |
| --- | --- | ----- | ----- | ----- | ----- | ----- | --- | --- | --- | --- |
|     |     | i     | i     | i     | i i   |       |     |     |     |     |
[j]∈RC/4×H/16×W/16
|     |     | x   |     |     |     |     | (9) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
andcross-scaleconcatenatedwithineachgroupj
|     |     | =Concat[x1 |     | [j],x2 | [j],x3 [j],x4 | [j]] |     |     |     |     |
| --- | --- | ---------- | --- | ------ | ------------- | ---- | --- | --- | --- | --- |
G
d
|     | j   | =d−1, | d∈{1,3,5}. |     |     |     | (10) |     |     |     |
| --- | --- | ----- | ---------- | --- | --- | --- | ---- | --- | --- | --- |
TheCGC-LKAmoduleintegratesshallow,intermediate,and
| deep-level    | features | to  | enhance  | sensitivity  |     | to irregular | distur-      |     |     |     |
| ------------- | -------- | --- | -------- | ------------ | --- | ------------ | ------------ | --- | --- | --- |
| bance shapes, | sharpen  |     | boundary | delineation, |     | and          | align multi- |     |     |     |
scalecontextualinformation.
D. MDDModule
| Forest | CD inherently |     | involves | a   | tradeoff | between | boundary |     |     |     |
| ------ | ------------- | --- | -------- | --- | -------- | ------- | -------- | --- | --- | --- |
precisionandsemanticcompleteness.High-resolutionfeatures
| preserve     | fine-grained |     | disturbance |            | edges. Low-resolution |       | fea-       |     |     |     |
| ------------ | ------------ | --- | ----------- | ---------- | --------------------- | ----- | ---------- | --- | --- | --- |
| tures encode | broader      |     | contextual  | semantics, |                       | which | are essen- |     |     |     |
tialfordisambiguatingspectrallysimilarland-covertransitions
| [28], [29].  | The  | proposed | MDD      | addresses |       | this challenge | by    |     |     |     |
| ------------ | ---- | -------- | -------- | --------- | ----- | -------------- | ----- | --- | --- | --- |
| constructing | four | parallel | decoding |           | paths | with dilation  | rates |     |     |     |
d∈{1,3,5,7}.
|     |     | The spacing |     | with | odd intervals | among | these |     |     |     |
| --- | --- | ----------- | --- | ---- | ------------- | ----- | ----- | --- | --- | --- |
Fig.3. ArchitectureoftheLKAmodule.
| rates minimizes |     | feature | redundancy |     | between | adjacent | paths, |     |     |     |
| --------------- | --- | ------- | ---------- | --- | ------- | -------- | ------ | --- | --- | --- |
whileenablingasystematicexpansionoftheeffectivereceptive
|                   |     |        |     |        |                |        | featuresS  | ,andtheoutputoftheprecedingpathH | d−1          |      |
| ----------------- | --- | ------ | --- | ------ | -------------- | ------ | ---------- | -------------------------------- | ------------ | ---- |
| fieldacrosspaths. |     |        |     |        |                |        |            | d                                |              |      |
| The structure     |     | of the | MDD | module | is illustrated |        | in Fig. 4. |                                  |              |      |
|                   |     |        |     |        |                |        |            | H =U (Deconv(S                   | ),S ,H d−1 ) | (11) |
|                   |     |        |     |        |                |        |            | d d                              | d d          |      |
| Each scale-hybrid |     | group  | G d | from   | the CGC        | module | is first   |                                  |              |      |
processedthroughachannelblockandadown-blocktogenerate whereH d−1 isinitializedtozeroford=1.Throughthisserial
skip features S , which capture local structural context at the cascade,eachH implicitlyencodestheaccumulatedcontextual
|     | d   |     |     |     |     |     |     | d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
informationfromallprecedingpaths.Forthefinalpathd=7,
correspondingscale.Subsequently,thefourdecodingpathsare
executedinaserialtop-downcascade.Forpathsd∈{1,3,5}, H5 already carries the aggregated multiscale representation of
each up-block integrated with a DMLP (detailed in Section allpriorpaths.Therefore,broadercontextisfurtherincorporated
III-E)fusesthedeconvolvedfeaturemap,thecorrespondingskip viaelement-wisesummationratherthanconcatenationtoavoid

12692 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
|     |     |     |     |     |     | TheteachernetworkT |     |     | generatessoftpseudolabelsforunla- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------------------------------- | --- | --- | --- | --- |
beledsamples
ˆ
|     |     |     |     |     |     |     |             |         | Y =T(I | ,I       | )      |             | (14) |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------ | -------- | ------ | ----------- | ---- |
|     |     |     |     |     |     |     |             |         | t      | pre post |        |             |      |
|     |     |     |     |     |     | and | the student | network | S is   | trained  | with a | combination | of   |
supervisedandunsupervisedconsistencylosses
|     |     |     |     |     |     |     |     |      |      | ˆ    | ˆ      | ˆ   |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ------ | --- | ---- |
|     |     |     |     |     |     |     |     | L =L | (Y,Y | )+λL | (Y ,Y  | ).  | (15) |
|     |     |     |     |     |     |     |     | semi | sup  | s    | cons t | s   |      |
TeacherparametersareupdatedusingEMA
|     |     |     |     |     |     |     |     | θ   | ←αθ | +(1−α)θ | .   |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | T   | T   |         | S   |     |      |
ThissemisupervisedstrategyenablesDECAF-CDtoexploit
|     |     |     |     |     |     | unlabeled | bitemporal |     | imagery | while | maintaining | stable | pseu- |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | ----- | ----------- | ------ | ----- |
dolabelquality.
G. ChangeMapGenerationandLossFunction
AccurateCDrequiresboundary-awaresupervisionandrobust
semisupervisedlearning[33].
|     |     |     |     |     |     | ThedecoderoutputsfromallpathsH1,H3,H5,H7 |     |     |     |     |     |     | arecon- |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
catenated
Fig.4. ArchitectureoftheMDDmodule.
|     |     |     |     |     |     |     | H   | =Concatenate[H1,H3,H5,H7 |     |     |     | ].  | (17) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | ---- |
final
inflatingchanneldimensionality Two1×1convolutionsthenreducethechanneldimensionto
=U7 (S7 +H5,S7 ). produceasingle-channellogitmapY.Apostprocessingstepre-
|     |     |     | H7  |     | (12) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
movessmallspuriousregions.Theoveralllossintegratesbinary
|     | The outputs | H1,H3,H5, | and | H7 are subsequently | concate- |     |     |     |     |     |     |     |     |
| --- | ----------- | --------- | --- | ------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
cross-entropy(BCE),diceloss,andteacher–studentconsistency
| natedwithintheMDDtoformthefinalmultiscalerepresenta- |      |            |                |              |                            | loss |     |     |     |     |     |     |     |
| ---------------------------------------------------- | ---- | ---------- | -------------- | ------------ | -------------------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| ti o                                                 | n H  | = C o n ca | t [ H , H 3, H | , H ], w h i | c h i s p a s se d t o t h | e    |     |     |     |     |     |     |     |
|                                                      | fi n | a l        | 1              | 5 7          |                            |      |     | ˆ   |     | ˆ   |     |     | ˆ ˆ |
s e g m en t a t i on h e ad f o r c h a ng e m a p g e n er a t io n . T h i s c as c ad e d L=L (Y,Y )+βL (Y,Y )+λL (Y ,Y ).
|     |     |     |     |     |     |     | BCE | s   | Dice | s   | consistency |     | t s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----------- | --- | --- |
multipath design enables MDD to progressively integrate fine (18)
boundarydetailsfromshallowpathswithbroadsemanticcon- Thisobjectiveensuresthegenerationofaccurate,boundary-
preservingchangemaps,andfacilitateseffectivesemisupervised
| text | from | deeper paths, | providing | a principled | mechanism | to  |     |     |     |     |     |     |     |
| ---- | ---- | ------------- | --------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
delineatetheirregularanddiffusedisturbanceboundarieschar- learningfordata-scarceforest-CD.
acteristicofforestCD.
IV. EXPERIMENTSRESULTANDANALYSIS
E. CoreComputationalBlocks
Thissectiongivesafullevaluationoftheexperimentaleval-
Efficientanddiscriminativefeatureextractionisessentialfor uation of the proposed method. We start with introducing the
high-resolution satellite imagery. Specialized blocks include benchmarkdatasets,semisupervisedexperimentalprotocol,and
depthwise separable convolution with BN and SiLU for pa- detailed implementation settings, followed by a description
rameter efficiency (DWBS), down-block (two Re Blocks + of the evaluation criteria and metrics. Subsequently, we show
DWBS for robust local features), and up-block with DMLP extensivecomparisonswithstate-of-the-artsemisupervisedCD
(fusingskipconnectionswithupsampledfeaturesusingdilated approaches.Inaddition,detailedablationstudiesareperformed
convolutions): inordertoevaluatethecontributionofeachofthecomponents,
aswellasacomparativestudyofthecomputationalcomplexity.
=Conv2d(LayerNorm(DilatedConv(x,d)))
|                                                         | y   |     |     |     | (13) |             |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| wherethedilationmatchesthecorrespondingpathtoadaptively |     |     |     |     |      | A. Datasets |     |     |     |     |     |     |     |
capturebothfine-scaleandbroadcontextualinformation.These
Experimentswereperformedonthreeforest-specificremote
blocksbalancecomputationalefficiencywithexpressivepower,
|     |     |     |     |     |     | sensing | CD  | datasets | to fully | assess | the performance |     | of the |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------- | -------- | ------ | --------------- | --- | ------ |
enablingthedecodertocapturemultiscaletexturesandseman-
|     |     |     |     |     |     | proposed | algorithm |     | in forest | environments. |     | In addition, | two |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | ------------- | --- | ------------ | --- |
tics.
urbanbuildingCDdatasetswereusedtoconductablationstudies
andfurthervalidatetheeffectivenessofindividualcomponents.
F. SemisupervisedTeacher–StudentStrategy
1) RF-CDisamultitemporalsatelliteimagedatasetderived
Limited labeled data motivates the utilization of unlabeled frompubliclyavailableGoogleEarthimagery,whosepub-
bitemporal images to improve generalization and reduce over- licavailabilityhasgreatlyenabledawiderangeofremote
fitting[30],[31],[32]. sensing research [34]. The dataset captures changes in

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12693
rainforest environments and presents a much more chal- Overall, we test the major performance of the proposed
lengingscenariocomparedtourbanbuildingCDdatasets, DECAF-CD algorithm in the forest domain using three
due to subtle spectral variations, complex backgrounds, forest-specificdatasets.Furthermore,ablationstudiesare
and irregular object boundaries that often result in frag- carried out on two commonly used public datasets that
mented change regions. It also exhibits significant in- representdiverseurbanscenestochecktherobustnessand
traclass variations caused by seasonal effects, lighting generalizabilityofthekeycomponentsoftheframework.
conditions, and natural vegetation dynamics. We obtain 4) WHU-CD [37]compriseshigh-resolutionaerialimagery
4312imagepairsofsize256×256,partitionedinto2620 (0.2m/pixel)capturingbuildingchangesinChristchurch,
fortraining,846forvalidation,and846fortesting.Forest NewZealand,followingthe2011earthquake.Thedataset
disturbances are organic and irregular, which lack the presents significant challenges due to substantial varia-
clear geometric structures of built-up areas, making this tionsinimagingconditions,seasonalchanges,andongo-
datasetparticularlychallenging.Baselineperformanceon ingreconstructionactivities.Originalimagesaredivided
RF-CDismuchlowerthanthatseenonurbanbuildingCD intononoverlapping256×256patches,resultingin7487
datasets,suchasWHU-CDandLEVIR-CD.Thisdiscrep- imagepairsdistributedas5947fortraining,743forval-
ancyhighlightstheinherentdifficultiesindetectingsubtle idation, and 744 for testing. This dataset is particularly
changes in vegetation from complex and heterogeneous valuableforevaluating modelrobustnessagainstdiverse
natural backgrounds, where weak spectral contrast and environmental conditions and complex change patterns,
irregularspatialpatternsgreatlycomplicatethedetection including building demolition, construction, and modifi-
ofsuchchanges. cation.
2) Landsat-SCD [35], which consists of 8468 bitemporal 5) LEVIR-CD [38] contains very high-resolution Google
imagepairs,acquiredbetween1990and2020,withspa- Earth imagery (0.5 m/pixel) of urban building changes
tial resolution of 30 m/pixel and 416×416 pixels. The across 20 regions in Texas, USA. The dataset empha-
dataset contains a “no-change” category and ten types sizes geometric structures and well-defined architectural
of semantic change, which cover four main land-cover changescharacteristicofurbandevelopment.Preprocess-
classes: farmland, desert, building, and water. For the ingyields10240nonoverlapping256×256patches,split
forest CD task that is addressed in this study, we are into 7120 for training, 1024 for validation, and 2048
specifically interested in green land and forest regions, fortesting.Itscleargeometricboundariesandstructured
andcombinethesetwolandcovertypesintoonecategory change patterns enable the evaluation of model perfor-
to simplify classification objective. As no official train manceonregularurbanexpansionanddevelopment.
validation-testsplitisgivenwerandomlysplitasubsetof
1908imagepairsintotraining,validation,andtestingsets B. SemisupervisedExperimentalProtocol
containing956,476,and476imagepairs,respectively.To
In accordance with standard semisupervised learning prac-
becompatiblewiththemodelarchitectureproposedandto
tices,low-annotationscenariosaresimulatedbyrandomlypar-
accommodatethecomputationalresourceconstraints,all
titioning the training set into labeled and unlabeled subsets
imageswereuniformlyresizedto256×256pixelsbefore
at four different annotation ratios: 5%, 10%, 20%, and 40%
trainingandevaluation.
(detailed partitions in Table I). For each annotation ratio, five
3) SECOND [36]isapubliclyavailablesemanticCDdataset
independentrunswithdifferentrandomseedsareperformedto
thatconsistsofaerialimagepairscapturedfromanumber
ensure statistical reliability, and report the mean performance
ofdifferentcities.Thedatasetconsistsof4662bitemporal
acrossallruns.Thevalidationandtestsetsremainfullylabeled
image pairs with a spatial size of 512×512 pixels, ac-
andfixedthroughoutforfaircomparison.
quired from high-resolution platforms, including optical
andSARsensors.ForthetaskofforestCDthatistackled
C. ImplementationDetails
in this study, we mainly consider green land and forest
areas, i.e., tree canopy and low-lying vegetation. These The proposed model was implemented in PyTorch using a
twocategoriesarecombinedintooneclass,called“forest ResNet-34 backbone pretrained on ImageNet. Input images
green land,” in order to match the goals of our analysis. were uniformly resized to 256×256 pixels. The network was
Thedatasetcontainspixel-levelannotationsmanuallyla- optimizedusingAdamWoptimizerwithaninitiallearningrate
beled by domain experts to ensure the high-quality and of6×10 −4,weightdecayof1×10 −4,andapolynomiallearn-
reliablegroundtruth(GT).Thedatasetisrandomlysplit ing rate decay schedule with an exponent of 0.9 was adopted.
into training, validation, and testing datasets with 2,671, Training was conducted with a batch size of 16 comprising 8
297,and297imagepairs,respectively.Thispartitioning labeledand8unlabeledpairs,andthenetworkwastrainedfor
strategy ensures that there is enough data to train the 40kiterations.Weakaugmentationsincludingrandomhorizon-
◦
model but still enough data to validate the model and tal/verticalflippingand90 rotationwereappliedtoallsamples.
assess performance in a unbiased manner. In order to Following UniMatch [42], each unlabeled sample addition-
be compatible with the proposed architecture, and also allyreceivedtwoindependentlysampledstrongaugmentations,
to account for computational resources, all images are comprising color jitter, Gaussian blur, CutMix, and random
resizedto256×256pixelsuniformlybeforethetraining grayscaleconversion.Thesestrongaugmentationswereapplied
andevaluationprocess. synchronouslytobothimagesofagivenbitemporalpairtoavoid

12694 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
TABLEI Intersection over union (IoU), also known as the Jaccard
STATISTICSOFDATAPARTITIONSUNDERDIFFERENTANNOTATIONRATIOSIN
index,evaluatesthespatialoverlapbetweenpredictionsandGT
SEMISUPERVISEDSETTINGS
TP
IoU= . (20)
TP+FP+FN
IoU is a stringent metric that simultaneously penalizes both
oversegmentationandundersegmentation,makingitastringent
measureoflocalizationaccuracy.
Panopticquality(PQ)evaluates instance-levelsegmentation
quality(SQ)bycombiningSQandrecognitionquality(RQ)
(cid:8)
PQ= (p,g)∈TP
IoU(p,g)
×
|TP|
(21)
|TP| |TP|+ 1|FP|+ 1|FN|
2 2
where (p,g) represents matched prediction-GT instance pairs,
andIoU(p,g)measurestheirspatialoverlap.SQcapturesshape-
alignmentaccuracy,whileRQevaluatesdetectioncompleteness.
In CD, instances are defined as connected components in the
binary change maps, and compute PQ to assess the geometric
integrityandstructuralpreservationofdetectedchangeregions.
This metric is particularly valuable for applications requiring
precise boundary delineation, which is critical for practical
introducing artificial pseudochanges. The loss weights for the applications,suchasurbanplanninganddisasterassessment.
CP branch were set to λ =0.5, λ =0.5, and for the Together,thesemetricsprovideamultifacetedevaluationof
CPBCE CPDice
consistencytraining(CT)branchλ =0.6,λ =0.4. pixel-wise accuracy, localization precision, and instance-level
CTFT CTCombo
TheGAFmoduleemploysgroupeddepthwisedilatedconvo- detectionquality.
lutions with dilation rates {1,3,5,7}, while the CGC module
integratesLKAusing5×5and7×7depthwiseconvolutional
E. ComparisonAlgorithms
kernels. A mean-teacher framework with an EMA momentum
Weperformedcomparativeanalysisofsevenstate-of-the-art
ofα=0.996isadopted.Theconsistencylossweightislinearly
CD methods, SemiCD, FixMatch, UniMatch, C2F-SemiCD,
ramped from 0 to 2.0 over the first 8k iterations. A fixed con-
SCanNet, SEIFNet, and SARASNet, to rigorously assess the
fidencethresholdofτ =0.95isappliedtoteacherpredictions
performance of the proposed approach with current advanced
tofilterunreliablepseudolabelsandsuppressconfirmationbias,
techniques.
followingcommonpracticeinsemisupervisedlearning[42].For
1) SemiCD[39]:SemiCDisasemisupervisedCDmodelthat
datasets, such as Landsat-SCD and SECOND, which contain
enforcesconsistencyonthepredictedchangeprobability
multipleland-covercategories,thegreenlandandforestclasses
maps of unlabeled dual-temporal images. Small random
aremergedintoasingleforestchangecategoryacrossallmeth-
perturbations are applied to the latent feature difference
ods. This ensures a consistent label space for all comparable
maps to encourage robustness. During the training pro-
evaluation.Allbaselinemodelswerereimplementedandtrained
cess,bothunsupervisedCDlossandthesupervisedcross-
underidenticaldatasplits,augmentationpipelines,categorydef-
entropylossarecomputed.Thisconsistency-basedstrat-
initions,andoptimizationsettingstoguaranteereproducibility
egy effectively utilizes unlabeled data while preserving
andenablevalidperformancecomparisons.
fine-grainedchangedetails.
2) FixMatch [40]: FixMatch is a generic semisupervised
D. EvaluationMetrics
framework adapted for remote sensing CD, combining
Five complementary metrics are employed to assess both pseudolabelingandconsistencyregularization.Themodel
pixel-levelaccuracyandinstance-levelquality. generates pseudolabels for weakly augmented unlabeled
Precision(P),recall(R),andF1-score(F1)serveasfunda- samples and enforces consistency under strong augmen-
mentalmetricsforbinaryclassificationperformance tations.Thisprincipledintegrationofunlabeleddataim-
proves generalization in low-annotation regimes and re-
TP TP 2×P ×R
P = , R= , F1= (19) ducesdependencyonfullsupervision.
TP+FP TP+FN P +R
3) UniMatch [41]: UniMatch is a semisupervised CD
whereTP,FP,andFNdenotetruepositives(correctlydetected paradigm that unifies pseudolabeling and consistency-
changes),falsepositives(backgroundmisclassifiedaschanges), basedlearningwithinasingleframework.UniMatchdy-
and false negatives (missed changes), respectively. Precision namicallygeneratespseudolabelsforunlabeledbitempo-
reflects prediction reliability, recall measures detection com- ral images, while enforcing consistency constraints on
pleteness, and F1 provides a balanced harmonic mean that multiscalefeaturerepresentations.Thisstrategyenhances
addressesprecision–recalltradeoff. the detection of both subtle and large-scale changes by

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12695
TABLEII
COMPREHENSIVEPERFORMANCECOMPARISONONRF-CDDATASETUNDERVARYINGANNOTATIONRATIOS(%)
effectivelyleveragingthespatial-temporalinformationin Following subtraction, a scale-aware attention module
unlabeleddata. calculates cross-scale attention on the difference maps,
4) C2F-SemiCD [42]: C2F-SemiCD is a coarse-to-fine effectivelyhandlingscenechangesduetoobjectsofdif-
semisupervised CD network that progressively refines ferent sizes. Finally, a cross-transformer module is used
predictions using labeled and unlabeled samples. The to fuse multilevel features to highlight the spatial infor-
coarsestageproducesinitialchangemapsfrombitemporal mation,whichhelpstobetterseparatetheforegroundand
inputs,afinestagethenrefinesthemwithhigh-resolution background and reduce the false positives in the change
| featuresandpseudolabelguidance.Theframeworklever- |      |         |             |     |              | map. |     |     |     |     |     |
| ------------------------------------------------- | ---- | ------- | ----------- | --- | ------------ | ---- | --- | --- | --- | --- | --- |
| ages unlabeled                                    | data | through | consistency |     | learning and |      |     |     |     |     |     |
F. OverallPerformanceComparison
| entropy minimization, |     | enabling | robust | detection | of het- |     |     |     |     |     |     |
| --------------------- | --- | -------- | ------ | --------- | ------- | --- | --- | --- | --- | --- | --- |
erogeneous, and small-scale changes in complex natural TablesIIandIIIshowadetailedcomparisonoftheproposed
scenes. method with seven state-of-the-art semisupervised CD meth-
5) SCanNet[43]:SCanNetisahybridsemanticCDframe- ods on the RF-CD, Landsat-SCD, and SECOND benchmark
| work that | uses triple | CNN | and | transformer. | A triple |                       |     |           |       |            |           |
| --------- | ----------- | --- | --- | ------------ | -------- | --------------------- | --- | --------- | ----- | ---------- | --------- |
|           |             |     |     |              |          | datasets. Evaluations | are | performed | under | annotation | ratios of |
encoder–decodernetworkisusedtoextracttemporalfea- 5%, 10%, 20%, and 40%, thus emphasizing the ability of the
tures and change representations from bitemporal im- method in cases where different amounts of labeled data are
agery.Followingthis,asemanticchangetransformermod- available. All quantitative results are averaged over five inde-
elsspatio-temporaldependenciesinthetokenspace,and pendent runs with different random seeds to ensure statistical
explicitlycaptures“fromto”semantictransitionsbetween
|     |     |     |     |     |     | robustness | and mitigate | the effect | of random | partitioning. | The |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | --------- | ------------- | --- |
theimages.Inaddition,asemanticlearningschemeleads threedatasetstogethercoveravarietyofforestandnaturalvege-
the network to make use of spatio-temporal constraints tationsettings,includingprimaryrainforests,secondarygrowth
andtomodel intrinsiccorrelations between changes and forests, and mixed forest ecosystems. In particular, RF-CD is
their semantic classes. By combining these joint spatio- composed solely of tropical rainforest scenes, and captures
temporal representations, SCanNet can significantly im- natural vegetation dynamics with irregular boundaries, grad-
provetheaccuracyofsemanticCDtasks. ual spectral transitions, and low-contrast disturbances. From
6) SEIFNet[44]:SEIFNetisaspatiotemporalenhancement Landsat-SCD and SECOND, we derive subsets that mainly
| and interlevel | fusion | network | for | CD. The | framework |                  |         |             |      |           |          |
| -------------- | ------ | ------- | --- | ------- | --------- | ---------------- | ------- | ----------- | ---- | --------- | -------- |
|                |        |         |     |         |           | focus on changes | related | to forests, | thus | expanding | the sce- |
starts by extracting multiscale feature maps from the narios for forest CD and increasing the assessment of model
bitemporal images using a backbone network. A spa- performanceincomplexnaturalenvironments.
tiotemporaldifferenceenhancementmodulewithadual- 1) PerformanceonRF-CDDataset: Fig.5showstheresults
branch architecture then captures the global changes at of forest CD for 8 representative image pairs. Methods like
thetargetlevelandfine-grainedlocaldifferencesbetween
|     |     |     |     |     |     | SemiCD, FixMatch, | and | UniMatch | completely | miss | most of |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ---------- | ---- | ------- |
temporalfeaturesatthesamescale.Enhancedfeaturesare the change regions and only capture a few isolated changes in
thendecodedusinganadaptivecontextfusionmoduleand thelatterpairs.C2F-SemiCD,SCanNet,SEIFNet,andSARAS-
refinementmodule.Finally,asummation-basedprediction Net produce more complete change maps but they still have
headcombinesmultiscalerepresentationstoproducethe omissionsandfragmentedboundaries.Incontrast,theproposed
finalchangemap,whicheffectivelyfusesglobalandlocal
DECAF-CDmethodcanalwaysgenerateresultsthatareclose
spatio-temporalinformation. to the GT, and can delineate the entire change regions with
7) SARSNet [45]: SARASNet is a scale and relation aware well-definededgesandlittlefalsedetectionsinallimagepairs,
Siamese network for CD. First, a relation-aware module showingthesuperiorabilityoftheproposedmethodtohandle
worksonfeaturemapsextractedfromthetwoinputimages subtleandcomplexforestdisturbances.
| before feature | subtraction |     | to strengthen | the | interactions |           |          |       |            |              |      |
| -------------- | ----------- | --- | ------------- | --- | ------------ | --------- | -------- | ----- | ---------- | ------------ | ---- |
|                |             |     |               |     |              | The RF-CD | dataset, | which | is focused | on detecting | for- |
betweenthetwoimagesforbetterfeaturediscrimination. est disturbance, presents great challenges because of spectral

12696 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
TABLEIII
COMPREHENSIVEPERFORMANCECOMPARISONONLANDSATDATASETUNDERVARYINGANNOTATIONRATIOS(%)
Fig.5. QualitativeevaluationresultsofSOTAcomparisonmethodswitha40%labeledratioontheRF-CDdataset.
variability and complex texture patterns. As summarized in which is 0.7 points higher than C2F-SemiCD (36.8%) and
Table II, the proposed DECAF-CD method achieves an IoU achieves better instance-level segmentation under extremely
of 49.8% under 5% annotation and 58.8% under 40% anno- limitedsupervision.Thiskindofcomprehensive improvement
tation, which is consistently better than all the baseline ap- isespeciallyimportantinthecaseofforestCD,wheremissed
proaches. Among the compared methods, C2F-SemiCD is the disturbancesmayhavesevereecologicalconsequences.Perfor-
best baseline and can be used as the main reference to assess manceimprovementsareconsistentacrossallannotationratios
theeffectivenessofourmodel.At5%annotation,DECAF-CD with IoU improvements ranging from 0.5 to 1.3 percentage
outperformsC2F-SemiCDby1.3ppinIoUand1.6pointsinF1, points.At40%annotation,DECAF-CDimprovestherecallby
with an increase of 1.7 points in precision. More importantly, 1.8pointscomparedtoC2F-SemiCDandalsohasthehighestPQ
the method achieves the best PQ of 37.5% at 5% annotation, of43.6%,beatingthesecondbestmethod(42.5%)by1.1points.

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12697
Fig.6. QualitativeevaluationresultsofSOTAcomparisonmethodswitha40%labeledratioontheLandsat-SCDdataset.
These results highlight the robustness of the proposed frame- as C2F-SemiCD (74.8%) and UniMatch (73.8%). Notably, at
work under different levels of supervision, suggesting that the 5% annotation, DECAF-CD achieves an F1 of 86.1% and a
effectiveness of the framework is not limited to a particular PQ of 76.4%, which is the highest among all methods, with
annotationsetting. PQ better than the second-best (75.8%) by 0.6 points. This
2) PerformanceonLandsat-SCDDataset: Fig.6showsCD showsexcellentinstance-levelSQwithverylimitedsupervision.
resultsontheLandsat-SCDdataset.Methods,suchasSemiCD, Theseperformanceadvantagescontinuetoaccrueastheratioof
FixMatch, and UniMatch, produce coarse boundaries and annotationincreases.At40%annotation,DECAF-CDachieves
suffer from considerable detail loss. C2F-SemiCD, SCanNet, 79.4% IoU, 89.0% precision, and 87.1% recall, achieving the
SEIFNet,andSARASNetgeneratemorecompletechangemaps highestF1of88.0%andthehighestPQof80.3%.PQexceeds
than these methods, but still have gaps and fragmented edges. ScanNet(80.2%)by0.1pointsandC2F-SemiCD(78.8%)by1.5
In contrast, the proposed DECAF-CD technique produces points,demonstratingsteadyimprovementsinSQdespitemore
well-defined boundaries and is effective in suppressing noise, labeleddata.Thesimultaneousimprovementinbothprecision
and retaining fine-grained details from all samples. It has the and recall in all settings suggests that DECAF-CD improves
highest prediction accuracy consistently, especially in difficult feature discriminability while preserving a tradeoff between
cases, which is much better than all the compared methods falsepositiveandfalsenegative,supportingrobustnessinforest
and shows its robustness in capturing subtle and complex CDtasks.
forest-relatedchanges. 3) Performance on SECOND Dataset: The SECOND
Tables III shows a detailed performance comparison on the dataset reflects changes in land-cover in a variety of environ-
Landsat-SCDdataset,wheretheproposedDECAF-CDmethod mentswithcharacteristicsdifferentfromthemostlyvegetation-
is consistently better than all competing approaches for any focusedLandsat-SCDdataset.Visualcomparisonsoftheresults
annotationratioandevaluationmetric.Withonly5%annotated of forest CD on SECOND are shown in Fig. 7. Methods like
samples, DECAF-CD achieves IoU of 75.6% which is better SemiCD,FixMatch,andUniMatchdonotaccuratelydelineate
thanthesecond-bestmethod,SEIFNet(75.1%),by0.5percent- disturbanceboundaries,leadingtobothfalsepositiveandmissed
agepoints,andisclearlybetterthanotherstrongbaselines,such detections.C2F-SemiCD,SCanNet,SEIFNet,andSARASNet

12698 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
Fig.7. QualitativeevaluationresultsofSOTAcomparisonmethodswitha40%labeledratioontheSECONDdataset.
TABLEIV
COMPREHENSIVEPERFORMANCECOMPARISONONSECONDDATASETUNDERVARYINGANNOTATIONRATIOS(%)
facechallengeswithcomplexforeststructures,resultinginfrag- DECAF-CDachievesarecallof75.8%,whichoutperformsthe
mented or misaligned change maps. In contrast, the proposed secondbestmethod,SEIFNet(74.2%)by1.6percentagepoints
DECAF-CDmethodproducescleanandcontinuousboundaries andoutperformsC2F-SemiCD(74.0%)by1.8points.Moreim-
and robustly detects changes in all samples. It has the highest portantly,itreachesthebestF1(77.6%)andPQ(63.2%)atthis
accuracyscoresespeciallyforchallengingcases,whichdemon- annotationlevel,whichshowsabetterbalancebetweenprecision
stratesitssuperiorabilitytohandleheterogeneousforestpatterns andrecallandabetterSQontheinstancelevel.Giventhesubtle
andcomplexland-covervariations. and gradual nature of many changes in forests, high recall is
Tofurtherquantifytheseimprovements,wetestedDECAF- critical to ensure that ecologically significant disturbances are
CDontheSECONDdatasetwithdifferentannotationratios.As not overlooked. The IoU gains over SEIFNet are stable for all
showninTableIV,themethodachieves63.5%IoUat5%anno- annotation ratios, which are about 0.7–1.1 percentage points,
tationand68.7%IoUat40%annotation,whichissignificantly while improvements over C2F-SemiCD range from 1.1 to 1.6
better than all baseline approaches. At 5% annotation level, points, indicating the robustness of the proposed framework.

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12699
At40%annotation,DECAF-CDachievesthehighestIoU,F1, samplesandgeneralizewellacrossdiverseforestandland-cover
and PQ of 68.7%, 80.3%, and 68.7% respectively, compared scenarios.
with the other methods. The F1 outperforms the second-best TheannotationefficiencyofDECAF-CDisalsorevealedby
(79.4%)by0.9points,whichfurthervalidatestheeffectiveness the fact that with only 5% annotated data, it is already better
ofthemethodundermoreabundantsupervision.Althoughthe than fully supervised baselines trained with 40% annotations
SECOND dataset has more heterogeneous and less structured in all three datasets. Specifically, our method achieves 49.8%
change patterns compared to Landsat-SCD, DECAF-CD still IoU on RF-CD, which surpasses the 40% supervised baseline
provides significant performance improvements, validating its of49.2%;75.6%IoUonLandsat-SCD,whichbeats73.8%;and
robustnessacrossdifferentspatialstructuresandcomplexscene 63.5%IoUonSECOND,whichbeats62.9%.Thistranslatesto
types. annotationsavingsofupto87.5%,whichshowsthepracticality
4) Overall Performance Discussion: Compared with other of the framework for large-scale remote sensing applications
methodsevaluatedinourexperiments,DECAF-CDbringsout wheremanuallabelingisprohibitivelyexpensive.
the benefits of a domain-aware architectural design. The pro- Theperformancesaturationbehaviorisdifferentindifferent
posed GAF module achieves multilevel feature integration, datasets.On Landsat-SCD, DECAF-CD achieves 95.2% of its
whichisequivalenttocombininglow-levelspatialinformation 40%annotationperformance(75.6%versus79.4%IoU)requir-
andhigh-levelsemanticinformation.Thiscapabilityiscritical ingonly5%annotation.OnSECOND,thisratiois92.4%(63.5%
for accurate detection of heterogeneous land-cover change in versus 68.7% IoU). On the more difficult RF-CD dataset, the
complex landsat scenes, where different types of change, in- ratio is 84.7% (49.8% versus 58.8% IoU), which reflects the
cluding vegetation change, village relocation, and water body inherent difficulty of the dataset and the continued benefit of
fluctuation,co-occur.TheCGCmodulefurtherincreasesthero- additionalannotations.Nonetheless,evenonRF-CD,DECAF-
bustnessofthemodelthroughbidirectionalfeatureinteractions, CDat5%annotationsignificantlyoutperformsallbaselinesat
reducingtheimpactofpseudochangesandatmosphericpertur- thesameannotationlevel,whichconfirmsitseffectivenessand
bationsthatarecommoninmultispectralsatelliteimagery,es- robustnessacrossdiversescenarios.
peciallywhenlowannotationratiosareused.Embeddedwithin
CGC,theLKAcomponentisveryeffectiveincapturingforest
H. ComparisonWithDifferentMethodCategories
disturbance patterns together with their surrounding context,
due to its large receptive field. Combined with the learnable 1) Comparison With Supervised Baseline: Compared with
weighted fusion mechanism in CGC, DECAF-CD adaptively thefullysupervisedbaseline,DECAF-CDachievessignificant
emphasizes features at suitable scales, which allows more ac- improvementsunderlowannotationratiosforallthedatasets.At
curatedelineationofchangeboundariesandbetterdetectionof 5%annotation,IoUimprovementsoverthesupervisedbaseline
subtle, small-scale forest disturbances. This integrated design are9.6percentagepointsonRF-CD(49.8%versus40.2%),5.9
is the basis for the superior performance of the method across pointsonLandsat-SCD(75.6%versus69.7%)and12.9pointson
differentdatasetsandannotationsettings. SECOND(63.5%versus50.6%).Theseconsistentgainsshow
Collectively,theseresultsconfirmthattheproposedarchitec- theeffectivenessofsemisupervisedlearningforremotesensing
tural innovations substantially extend the capacity of semisu- CDinavarietyofscenetypes.
pervised learning to capture spatially and spectrally complex 2) Comparison With Early Semisupervised Methods: Rel-
changepatternsunderlow-annotationscenarios,particularlyin ative to previous semisupervised methods (e.g. SemiCD),
naturalenvironmentswheretraditionalmodelsfailtogeneralize. DECAF-CDisabletoachievesignificantimprovementsonall
thedatasets.OnRF-CDat5%annotationtheIoUisimproved
by 5.0 points (49.8% versus 44.8%) compared with SemiCD.
G. AnalysisofAnnotationEfficiency
OnLandsat-SCD,thegainis5.4points(75.6%versus70.2%),
A major advantage of the proposed DECAF-CD method is andonSECOND,ourmethodis4.0pointsbetterthanSemiCD
that it achieves outstanding performance under little supervi- (63.5% versus 59.5%). These consistent improvements con-
sion. The performance differences between our approach and firm the benefit of combining consistency regularization with
baseline methods are the largest at low annotation ratios. On domain-specific architectural modules, overcoming the short-
RF-CD(seeTablesII),DECAF-CDoutperformsthebestbase- comings of previous approaches that rely only on pseudola-
line, C2F-SemiCD, by 1.3 percentage points in IoU with 5% belingoradversarialapproachesandfinditdifficulttocapture
annotation,andkeepsthesameadvantagewith40%annotation, the complex spectral and structural patterns in remote sensing
showingconsistentsuperioritywhentheamountoflabeleddata imagery.
varies.Whencomparedwiththegenericsemisupervisedmethod 3) ComparisonWithGenericSemisupervisedMethods: Al-
UniMatch,thedifferenceisevenmorestrikingatlowannotation thoughFixMatchandUniMatchachievegoodperformanceon
ratios, with a 5.0-point IoU advantage at 5% annotation that naturalimagebenchmarks,theirperformancevariesonthethree
narrowsdownto2.6pointsat40%,underliningtheeffectiveness remote sensing datasets. On Landsat-SCD and SECOND, the
of our domain-aware design under extremely limited supervi- twomethodshavecompetitiveresults,withUniMatchachieving
sion. Similar trends are seen on Landsat-SCD (see Table III) 73.8%and62.0%IoUat5%annotation,respectively.However,
and SECOND (see Table IV), confirming that the proposed onRF-CDtheirperformancedecreasesto45.5%and44.8%IoU,
architecturalinnovationsareabletomakegooduseofunlabeled whichislessthanDECAF-CD’s49.8%.Thisdiscrepancyshows

12700 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
Fig.8. F1comparisonofdifferentmethodson(a)RF-CD,(b)Landsat-SCD,and(c)SECONDundervaryingannotationratios(5%,10%,20%,and40%).Our
methodconsistentlyachievesthebestperformanceacrossalldatasetsandlabelregimes.
thatconsistencyregularizationstrategiesthathavebeendevel- I. PerformanceVisualizationandAnalysis
opedfornaturalimagesclassificationneedcarefuladaptationto
Figs. 8 –10 show in total the comprehensive performance
capturesubtlespectralandtexturalchangesincomplexremote
of different methods among the three datasets and multiple
sensing scenarios. The consistent improvements that DECAF-
annotation ratios. Fig. 8 illustrates that DECAF-CD is able to
CDhasachievedoverthesegenericapproachesislargelyaresult consistentlyachievethehighestF1scoresforallthreedatasets
ofthedomain-awaredesignofDECAF-CD’smodules.TheGAF
(RF-CD,Landsat-SCD,andSECOND)andallannotationlevels,
module is a multilevel feature integration module specifically
withespeciallystronggainsatlowannotationratios.Thethree
designed for bitemporal CD, which effectively combines low-
datasetsshowdifferentlevelsofdifficulty:Landsat-SCDhasthe
levelspatialdetailsandhigh-levelsemanticcontext.TheCGC highest F1 scores (81.2%–86.1% at 5% annotation), followed
modulewithLKAoffersalargeeffectivereceptivefieldthatcan
bySECOND(71.6%–77.6%at5%),whileRF-CDhasthemost
capture the compact building footprint and the irregular forest
difficulty(60.6%–70.6%at5%),indicatingthedifficultyofiden-
patchboundary.Together,theseelementsmaketheframework
tifyingirregularforestboundariesinhigh-resolutionimagery.
adaptabletovariouspatternsofchangewithoutrequiringmanual
AunifiedvisualizationoftheIoUperformanceacrossallthe
tuning for particular datasets to ensure robust performance in
experimental configurations is given in Fig. 9, where darker
heterogeneousscenarios.
green indicates higher values, yellow represents intermediate
4) ComparisonWithState-of-the-ArtSemisupervisedMeth-
performance, and red corresponds to lower values. The color-
ods: Compared with the state-of-the-art semisupervised CD
coded matrix shows a clear stratification of performance, with
methods, such as C2F-SemiCD, SEIFNet, SCanNet, and
DECAF-CD(bottomrow)alwayshavingadeepergreencolour
SARASNet,DECAF-CDconsistentlyoutperformsalltheother
forall12configurations.Datasetspecificpatternsareapparent:
methods in all datasets and annotation ratios. On Landsat-
Landsat-SCDshowsoverallgreen-dominantcolors,whileRF-
SCD and SECOND, the improvements are small but con-
CD shows yellowish to reddish tones, confirming it is a more
sistent, with IoU improvements at 5% annotation between
difficultdatasetasapureforestdataset.Thecolortransitionfrom
0.5 and 1.4 percentage points. On RF-CD, the improvements
5%to40%annotationisthemostpronouncedonRF-CD,which
are more pronounced with DECAF-CD outperforming these
meansthisdatasetisthemostbenefitedfromadditionallabeled
baselines by 1.3 to 4.3 percentage points in IoU at 5%
data.
annotation. The robustness of these gains across heteroge-
Fig. 10 demonstrates the superior data efficiency of our
neousdatasetsemphasizesthegeneralizabilityoftheproposed
method. On RFCD, LandsatSCD, and SECOND, our method
framework, showing that the effectiveness of the framework
at 5% annotation (49.8%, 75.6%, and 63.5% IoU) surpasses
is not restricted to specific dataset characteristics or scene
thesupervisedbaselineat40%annotation(49.2%,74.2%,and
types.
60.3% IoU, respectively), representing annotation savings of
ThehigherimprovementsseenonRF-CDcanbeexplainedby
upto87.5%acrossallthreedatasets.Thecurvesrevealdiffer-
theimprovedcapabilityofDECAF-CDindealingwithirregular
ent saturation behaviors: LandsatSCD converges rapidly after
boundariesandsubtlechanges.Thebidirectionalfeatureprop-
5%annotation,SECONDexhibitsgradualimprovement,while
agation in the CGC module enables information propagation
RFCD maintains a steeper slope, indicating continued benefit
betweenspatiallocations,whichisespeciallyeffectiveincap-
from additional supervision on the most challenging forest
turingthecomplexspatialdependenciesofnaturalvegetation.In
scene.Thesevisualizationscollectivelyconfirmtherobustness
addition, the learnable weighted fusion mechanism adaptively
and practical value of our semisupervised framework across
weights the features at the most relevant scales, allowing for
diverseCDtasks.
more accurate delineation of forest boundaries than strategies
Fig.10highlightsthebetterannotationefficiencyofDECAF-
withfixedfusions.Thiscombinationofadaptiveandscale-aware
CD. On RF-CD, Landsat-SCD, and SECOND datesets, the
featureintegrationandbidirectionalpropagationisthekeytothe
method with 5% annotation (49.8%, 75.6%, and 63.5% IoU,
superiorperformanceofthemethodinchallengingscenariosof
respectively)alreadyoutperformsthefullysupervisedbaseline
forestCD.

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12701
Fig.9. ComprehensiveIoUperformanceheatmapacrossninemethods,threedatasets,andfourannotationratios.DarkergreenindicateshigherIoU.Vertical
bluelinesseparatedatasets.Ourmethod(bottomrow)consistentlyachievesthehighestIoUacrossallconfigurations.
Fig.10. AnnotationefficiencyanalysisshowingIoUversusannotationratioforfourrepresentativemethods.Ourmethodat5%annotationonalldatasets
surpassesthesupervisedbaselineat40%,demonstratingsignificantannotationsavings.(a)RF-CD.(b)Landsat-SCD.(c)SECOND.
with 40% annotation (49.2%, 74.2%, and 52.3% IoU), which ontheLEVIR-CD,WHU-CD,andRF-CDdatasetswitha40%
correspondstoannotationsavingupto87.5%acrossalldatasets. annotationratio.Theselectioncoversbothstructuredurbanen-
The curves show different saturation behaviors: Landsat-SCD vironments(LEVIR-CDandWHU-CD)andthemorechalleng-
convergesveryfastafter5%annotation,SECONDshowsagrad- ing,irregularforestdisturbancesinRF-CD,enablingathorough
ualimprovementandRF-CDshowsasteeperslope,indicating evaluationofeachmodule’srobustnessandgeneralization.As
thepersistentbenefitofextrasupervisionforthemostchalleng- summarizedinTableV,thebaselinemodelachievesIoU/F1/PQ
ing forest scenes. Collectively, these visualizations show the scoresof81.2/90.1/72.8,75.9/86.0/70.5,and49.2/68.5/35.8on
robustness, data efficiency, and practical value of our semisu- LEVIR-CD,WHU-CD,andRF-CD,respectively.Theseresults
pervisedframeworkforavarietyofCDtasks. provideastablereferencepointforevaluatingtheimpactofin-
dividualmodules.Thesignificantlylowerbaselineperformance
onRF-CD(49.2%IoU)comparedtoLEVIR-CD(81.2%IoU)
J. AblationStudyAnalysis
andWHU-CD(75.9%IoU)highlightstheinherentchallengeof
Tosystematicallyassessthecontributionofeachofthepro- forest CD, which is characterized by irregular boundaries and
posedcomponents,weperformedasetofablationexperiments smallspectralvariations.

12702 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
TABLEV
ABLATIONSTUDYOFTHEPROPOSEDCOMPONENTSONLEVIR-CD,WHU-CD,ANDRF-CD(40%ANNOTATIONRATIO).BESTRESULTSAREHIGHLIGHTEDIN
BOLD.
Integrating the GAF module provides consistent improve- Ofparticularnote,onRF-CD,thecombinedmodulesachieve
ments for all the datasets with significant improvements on 56.5% IoU, a 7.3 percentage point improvement over the
WHU-CDandRF-CD.OnRF-CD,IoUimprovesfrom49.2%to baseline, substantially larger than that of LEVIR-CD (+1.8
51.8%,whichindicatesthattheproposedchannel-leveltemporal points) and WHU-CD (+8.7 points). This amplified improve-
alignment mechanism improves the model’s ability to capture mentdemonstratestheimportanceofdomain-awarearchitecture
fine-grained spatio-temporal features, thereby enabling it to designsforchallengingforestmonitoringsituations.
betterdetectsubtlestructuralchanges.Therelativeimprovement Finally,thefullDECAF-CDmodel,whichcombinesallthe
onRF-CD(+2.6IoUpoints)ismoresignificantthanonLEVIR- components(GAF+CGC+LKA+FT+Combo),getsthehigh-
CD (+0.7 points), which means that channel-level temporal est performance on all three datasets, which is 83.8/91.4/76.5
alignment is more beneficial for complex natural scenes with onLEVIR-CD,85.8/92.7/79.1onWHU-CDand58.8/77.1/43.6
heterogeneousstructures. on RF-CD (IoU/F1/PQ). The regular improvements across di-
AddingtheCGCmodulewithoutLKAimprovesperformance verse datasets point to the synergy between the architectural
evenmoreonallthedatasets.Notably,onWHU-CD,theF1is design and advanced loss formulation. On RF-CD, the full
improved from 86.0 to 89.5, and on RF-CD, IoU is improved model achieves a 9.6 percentage point IoU improvement over
from 49.2% to 52.5%. These improvements suggest that the the baseline (49.2% → 58.8%), which is significantly greater
bidirectionalfeatureinteractioninCGCaddressesthesemantic thantheabsoluteimprovementonLEVIR-CD(+2.6points)and
misalignmentbetweenshallowanddeeplayerswhilereducing similartoWHU-CD(+9.9points).Notably,thecontributionof
noisecausedbylow-levelfeatures.Replacingthestandardcon- theFT+CombolossonRF-CD(+2.3IoUpoints,from56.5%to
volution in CGC with the LKA block yields additional gains 58.8%)ismorepronouncedcomparedtotheotherdatasets,con-
for all the datasets. For example, PQ on WHU-CD goes from firmingthatsophisticatedlossfunctionsareparticularlyeffective
73.9 to 75.4, and IoU on RF-CD goes from 52.5% to 54.1%, inaddressingsevereclassimbalanceandirregularboundaries,
confirmingthatLKAiseffectiveinmodelinglong-rangespatial whicharekeychallengesinforestCD.Theseresultscollectively
dependencies, which are important for modeling the irregular validatetheeffectiveness,robustness,andpracticalvalueofthe
forest patch boundaries and other subtle changes in remote proposed DECAF-CD framework for semisupervised remote
sensingimagery. sensingCD,inawiderangeofscenarios.
Onthelossfunctionside,theintroductionoftheFocalTver-
K. ComplexityComparison
sky+Combo(FT+Combo)lossoffersstableimprovementson
alldatasets.OnRF-CD,IoUisimprovedfrom49.2%to53.2%, Fig.11showsascatterplotforthecomputationalcomplexity
which isan increase of 4.0 percentage points.This shows that and segmentation accuracy of various methods. The x-axis
FocalTverskyandCombolossescombinationbetteraddresses is FLOPs (G), the y-axis represents IoU (%), the number of
the class imbalance and has a better sensitivity to small or parameters (M) is represented by the point size. DECAF-CD
irregularchangeregions,whicheventuallyimprovesthePQand achieves the highest accuracy (88.5% IoU) with a moderate
boundary-levelaccuracy.ThehigherimprovementsonRF-CD computationalfootprint(150GFLOPsand36.8Mparameters)
relative to more structured data sets (LEVIR-CD: +1.0 points, aswellasfastinferencespeed.SEIFNethasthelowestFLOPs
WHU-CD: +6.1 points) emphasize the specific usefulness of (80G) with competitive accuracy (87.4%) but is still slightly
advanced loss formulations for heterogeneous natural scenes behind our method. UniMatch has a reasonable balance (90G
withsignificantclassimbalance. FLOPs,87.1%IoU),whileSCanNetandSARSNethavemuch
WhenGAFandCGC(withLKA)areusedtogether,perfor- higher computational costs (160G and 330G FLOPs, respec-
manceissignificantlyimproved,resultingin83.0/91.2/75.4on tively)withoutsurpassingtheaccuracyofDECAF-CD.Notably,
LEVIR-CD, 84.6/91.5/77.4 on WHU-CD, and 56.5/75.4/41.8 the performance of the most massive model (330G FLOPs,
onRF-CD.Theseresultsshowastrongcomplementaryeffect: 111Mparameters)isthelowest(85.0%IoU)inthecaseofthe
GAFenricheschannel-leveltemporalalignment,andCGCwith modelcalledSARSNet.Thisvisualizationemphasizesthebetter
LKAprovidesstrongmultiscalecontextualreasoning. efficiency-accuracy tradeoffofDECAF-CD,whichshowsthat

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12703
boundaries,inconsistentspectralresponses,andgradualrather
than abrupt changes. The analysis underscores that modules,
such as GAF, CGC, and LKA, are essential for mitigating
thesedifficulties,yetfurtherdomain-specificmodelingmaybe
required.Futureworkcouldincorporatephenology-awarefea-
turenormalization,structure-from-motionpriors,orecological-
process-guided constraints to address the intrinsic irregularity
offorestdisturbance.
Finally,thisstudyfocusesonbitemporalCD.Althoughbitem-
poralmodelingiswidelyadopted,real-worldforestmonitoring
increasingly involves long-term analysis where multitempo-
ral dependencies contain rich temporal cues about progressive
degradation or recovery. Extending the semisupervised frame-
worktorecurrentortransformer-basedmultitemporalarchitec-
tures could unlock more powerful representations of temporal
trajectories. Such extensions are particularly valuable for con-
Fig.11. Performanceversuscomputationalcostcomparison.Theredcircle
tinuous Earth observation programs, enabling more accurate
highlightsourmethod,whichachievesthehighestIoU@40%withcompetitive
parameterefficiency. modelingofdisturbancepropagation, regeneration cycles,and
seasonalvariabilityatscale.
DECAF-CD achieves state-of-the-art performance with much Overall,theselimitationsdonotdetractfromthecontributions
lowercomputationaloverheadthanheavierarchitectures. oftheproposedframework;instead,theyoutlinecleardirections
foradvancinghigh-resolutionforestCD.
V. LIMITATIONSANDFUTUREWORK
Althoughtheproposedframeworkexhibitsstrongrobustness
VI. CONCLUSION
acrossdatasetsandannotationregimes,severallimitationssug-
gestdirectionsforrefinement.Themultiscalefeatureaggrega- In this work, we proposed DECAF-CD, a semisupervised
tionandbidirectionalinteractionpathwaysintroduceincreased dual-encoderchannel-awarenetworkforfine-grainedforestCD,
computational overhead, raising inference approximately 15% designedtoaddressthechallengesoflimitedlabeleddata,het-
relative to the baseline. This reflects the inherent tradeoff be- erogeneousforeststructures,andsubtletemporalchangesinre-
tween model expressiveness and computational efficiency, but motesensingimagery.Theframeworkintegratesadual-encoder
also confirms highlights that the architectural gains are driven backbone,GAF,CGCblockswithLKA,andanMDD,DECAF-
bymoduleswithsubstantialrepresentationalcapacity.Futureef- CDeffectivelycapturesmultiscale,discrepancy-awarefeatures
fortswillinvestigatemoreefficientattentionformulations,such whileenhancedboundaryprecisionandstructuralfidelity.
asreparameterizableLKAanddynamicsparseattention,along Toalleviateannotationscarcity,ateacher–studentsemisuper-
with lightweight multibranch designs, to preserve long-range vised strategy leverages unlabeled bitemporal images through
modelingabilitywhilereducinginferencelatency. pseudolabelguidanceandconsistencyregularization.Extensive
A second limitation concerns the detection of extremely experiments on RFCD, LandsatSCD, and SECOND demon-
small change regions (often below 10 pixels), which remains stratedthatDECAF-CDconsistentlyoutperformsstate-of-the-
challenging despite the improvements from GAF and LKA- artsemisupervisedCDmethodsacrossmultipleannotationra-
enhanced CGC. This is especially pronounced on RF-CD, tios,achievinghigherIoU,F1,andPQscores,particularlyunder
whereselectivelogging,understorythinning,andlow-intensity extremelylowsupervision.Theproposedarchitecturenotonly
degradation produce subtle spatial signatures that can be lost improves detection accuracy of complex and irregular forest
during down-sampling operations. The difficulty in capturing disturbancesbutalsosignificantlyreducestheannotationeffort,
these fine-grained changes implies that the current architec- enabling comparable, or superior results with only 5%–10%
ture, while effective at multiscale contextual reasoning, still labeleddata.
underrepresentsmicroscalestructures.Futureeffortscouldex- AblationstudiesfurtherconfirmedthecontributionsofGAF,
plore super-resolution-guided decoders, boundary-focused re- CGC, LKA, and multiscale feature fusion in enhancing both
finementheads,oradaptivehigh-frequencyenhancementmod- globalcontextualunderstandingandlocalboundaryrefinement.
ulesmayfurtheramplifythemodel’s sensitivitytosmall,spa- Collectively,theseresultsvalidatetheeffectivenessandgeneral-
tiallyfragmentedchangepatterns. izabilityofDECAF-CDforcapturingfine-grainedforestdistur-
Athirdlimitationisthepersistentperformancegapbetween bancesacrossdiversenaturalenvironments,offeringapractical
naturalforestenvironmentsandstructuredurbandatasets.With solutionforlarge-scale,high-frequencyforestmonitoringwhere
thefullmodelat40%annotation,IoUonRF-CDreaches58.8%, labeleddataisscarce.Futureworkwillexploretheintegration
substantially lower than the 83.8% and 85.8% obtained on of multimodal data (e.g., LiDAR, SAR) to further improve
LEVIR-CDandWHU-CD.Thisdiscrepancydoesnotindicate detectioninchallengingcanopysettings,aswellasextendthe
a weakness in the proposed design, but rather reflects the in- semisupervised paradigm to continuous temporal monitoring
herentlygreatercomplexityofforestdynamics,suchasdiffuse tasksfornearreal-timeforestmanagementapplications.

12704 IEEEJOURNALOFSELECTEDTOPICSINAPPLIEDEARTHOBSERVATIONSANDREMOTESENSING,VOL.19,2026
REFERENCES [20] C.Liang,B.Xiao,B.Cheng,andY.Dong,“Xanet:Anefficientremote
sensingimagesegmentationmodelusingelement-wiseattentionenhance-
[1] A.Lausch,S.Erasmi,D.J.King,P.Magdon,andM.Heurich,“Under- mentandmulti-scaleattentionfusion,”RemoteSens.,vol.15,no.1,2022,
standingforesthealthwithremotesensing-partII—Areviewofapproaches Art.no.236.
anddatamodels,”RemoteSens.,vol.9,no.2,2017,Art.no.129.[Online]. [21] X.Yang,Z.Song,I.King,andZ.Xu,“Asurveyondeepsemi-supervised
Available:https://www.mdpi.com/2072-4292/9/2/129 learning,”IEEETrans.Knowl.DataEng.,vol.35,no.9,pp.8934–8954,
[2] N.Zhou,J.Hong,W.Cui,S.Wu,andZ.Zhang,“Amultiscaleattention Sep.2023.
segmentnetwork-basedsemanticsegmentationmodelforlandslideremote [22] H.Li,Z.Wu,A.Shrivastava,andL.S.Davis,“Rethinkingpseudolabels
sensing images,” Remote Sens., vol. 16, no. 10, 2024, Art. no. 1712. forsemi-supervisedobjectdetection,”inProc.AAAIConf.Artif.Intell.,
[Online].Available:https://www.mdpi.com/2072-4292/16/10/1712 2022,vol.36,no.2,pp.1314–1322.
[3] A.Stritihetal.,“Same,butdifferent:Similarstatesofforeststructurein [23] K.Ye,Z.Huang,Y.Xiong,Y.Gao,J.Xie,andL.Shen,“Progressivepseudo
temperatemountainregionsofEuropedespitedifferentsocial-ecological labelingformulti-datasetdetectionoverunifiedlabelspace,”IEEETrans.
forest disturbance regimes,” Landscape Ecol., vol. 39, no. 6, 2024, Multimedia,vol.27,pp.531–543,2025.
Art.no.114. [24] Y.Chen,D.Xu,Y.Lou,H.Li,W.Ding,andY.Huang,“Semi-supervised
[4] L.Han,Q.Han,Y.Zhang,G.Guo,andS.Jing,“Acategory-awarefeature medical image classification via cross-training and dual-teacher fusion
disentanglementandspatial-awareframeworkforcultivatedlandchange model,”Inf.Fusion,vol.124,2025,Art.no.103389.
detectionindiversescenarios,”IEEETrans.Geosci.RemoteSens.,vol.63, [25] L.Miller,C.Pelletier,andG.I.Webb,“Deeplearningforsatelliteimage
2025,Art.no.4419820. time-seriesanalysis:Areview,”IEEEGeosci.RemoteSens.Mag.,vol.12,
[5] K.Malik,C.Robertson,S.A.Roberts,T.K.Remmel,andJ.A.Long, no.3,pp.81–124,Sep.2024.
“Computervisionmodelsforcomparingspatialpatterns:Understanding [26] J. Yang, H. Jiang, S. Wang, and X. Ma, “A multi-scale deep learning
spatialscale,”Int.J.GeographicalInf.Sci.,vol.37,no.1,pp.1–35,2023, algorithmforenhancedforestfiredangerpredictionusingremotesensing
doi:10.1080/13658816.2022.2103562. images,”Forests,vol.15,no.9,2024,Art.no.1581.
[6] S.Frolking,M.W.Palace,D.B.Clark,J.Q.Chambers,H.H.Shugart, [27] J. LV et al., “STMTNet: Spatio-temporal multiscale triad network for
andG.C.Hurtt,“Forestdisturbanceandrecovery:Ageneralreviewinthe croplandchangedetectioninremotesensingimages,”IEEEJ.Sel.Topics
contextofspaceborneremotesensingofimpactsonabovegroundbiomass Appl.EarthObserv.RemoteSens.,vol.18,pp.26005–26020,2025.
andcanopystructure,”J.Geophys.Res.:Biogeosciences,vol.114,no.G2, [28] L.T.RamosandA.D.Sappa,“Multispectralsemanticsegmentationfor
2009,Art.no.G00E02. landcoverclassification:Anoverview,”IEEEJ.Sel.TopicsAppl.Earth
[7] H. He, J. Yan, D. Liang, Z. Sun, J. Li, and L. Wang, “Time-series Observ.RemoteSens.,vol.17,pp.14295–14336,2024.
landcoverchangedetectionusingdeeplearning-basedtemporalsemantic [29] Z.Hanetal.,“CAEM-DETR:Smallaerialtargetdetectionviacontrastive
segmentation,”RemoteSens.Environ.,vol.305,2024,Art.no.114101. attention-enhanced multidomain fidelity fusion,” IEEE Trans. Geosci.
[8] L.Wang,M.Zhang,X.Gao,andW.Shi,“Advancesandchallengesin RemoteSens.,vol.63,2025,Art.no.5646614.
deeplearning-basedchangedetectionforremotesensingimages:Areview [30] B. Hou, Q. Liu, H. Wang, and Y. Wang, “From W-Net to CDGAN:
throughvariouslearningparadigms,”RemoteSens.,vol.16,no.5,2024, Bitemporalchangedetectionviadeeplearningtechniques,”IEEETrans.
Art.no.804.[Online].Available:https://www.mdpi.com/2072-4292/16/ Geosci.RemoteSens.,vol.58,no.3,pp.1790–1802,Mar.2020.
5/804 [31] X.Qin,H.Guo,X.Su,Z.Zhao,D.Wang,andL.Zhang,“Spatiotemporal
[9] T. Bai et al., “Deep learning for change detection in remote sensing: maskedpre-trainingforadvancingcropmappingonsatelliteimagetime
A review,” Geo-Spatial Inf. Sci., vol. 26, no. 3, pp.262–288, 2023, serieswithlimitedlabels,”Int.J.Appl.EarthObservationGeoinformation,
doi:10.1080/10095020.2022.2085633. vol.137,2025,Art.no.104426.
[10] W. Liu, Z. Kang, J. Liu, Y. Lin, Y. Yu, and J. Li, “A multitask CNN- [32] H.M.Gomes,M.Grzenda,R.Mello,J.Read,M.H.LeNguyen,andA.
transformernetworkforsemanticchangedetectionfrombitemporalre- Bifet,“Asurveyonsemi-supervisedlearningfordelayedpartiallylabelled
motesensingimages,”IEEETrans.Geosci.RemoteSens.,vol.62,2024, datastreams,”ACMComput.Surv.,vol.55,no.4,pp.1–42,2022.
Art.no.5647215. [33] F.Jiangetal.,“BARNet:Boundary-awarerefinementnetworkforweakly
[11] Y.Taoetal.,“Aself-supervisedlearningapproachforextractingChina supervisedchangedetection,”IEEETrans.Geosci.RemoteSens.,vol.63,
physical urban boundaries based on multi-source data,” Remote Sens., 2025,Art.no.5647115.
vol.15,no.12,2023,Art.no.3189.[Online].Available:https://www. [34] G.-S.Xiaetal.,“DOTA:Alarge-scaledatasetforobjectdetectioninaerial
mdpi.com/2072-4292/15/12/3189 images,”inProc.IEEEConf.Comput.Vis.PatternRecognit.,Jun.2018,
[12] M. Zhang, G. Li, D. Lu, C. Xu, H. Zhao, and D. Li, “Self-supervised pp.3974–3983.
deeplearningfordetectionofforestdisturbancetypesinasubtropical [35] P. Yuan, Q. Zhao, X. Zhao, X. Wang, X. Long, and Y. Zheng, “A
ecosystem using transformer and sentinel-1 and sentinel-2 time series transformer-basedsiamesenetworkandanopenopticaldatasetforse-
data,” Int. J. Digit. Earth, vol. 18, no. 1, 2025, Art. no. 2537325, manticchangedetectionofremotesensingimages,”Int.J.Digit.Earth,
doi:10.1080/17538947.2025.2537325. vol.15,no.1,pp.1506–1525,2022.
[13] M.Nikoueietal.,“Smallobjectdetection:Acomprehensivesurveyon [36] K. Yang et al., “Semantic change detection with asymmetric Siamese
challenges, techniques and real-world applications,” Intell. Syst. Appl., networks,”2020,arXiv:2010.05687.
vol.10,no.3,2025,Art.no.200561. [37] S.Ji,S.Wei,andM.Lu,“Fullyconvolutionalnetworksformultisource
[14] X. Li, Y. Qiu, J. Liao, F. Meng, and P. Ren, “Unsupervised domain buildingextractionfromanopenaerialandsatelliteimagerydataset,”
adaptationsemanticsegmentationofremotesensingimageswithmask IEEETrans.Geosci.RemoteSens.,vol.57,no.1,pp.574–586,Jan.2019.
enhancementandbalancedsampling,”IEEETrans.Geosci.RemoteSens., [38] H.ChenandZ.Shi,“Aspatial-temporalattention-basedmethodanda
vol.63,2025,Art.no.5609114. newdatasetforremotesensingimagechangedetection,”RemoteSens.,
[15] Y. Yang, L. Xie, Z. Fu, J. Yan, and S. M. Naqvi, “Pose-oriented vol.12,no.10,2020,Art.no.1662.
scene-adaptivematchingforabnormaleventdetection,”Neurocomputing, [39] D. Peng, L. Bruzzone, Y. Zhang, H. Guan, H. Ding, and X. Huang,
vol.611,2025,Art.no.128673. “SemiCDNet:Asemisupervisedconvolutionalneuralnetworkforchange
[16] K.Nasirietal.,“Usingcitizensciencedataaspre-trainingforsemantic detectioninhighresolutionremote-sensingimages,”IEEETrans.Geosci.
segmentation of high-resolution UAV images for natural forests post- RemoteSens.,vol.59,no.7,pp.5891–5906,Jul.2021.
disturbanceassessment,”Forests,vol.16,no.4,2025,Art.no.616. [40] K. Sohn et al., “Fixmatch: Simplifying semi-supervised learning with
[17] Q.He,M.Wu,P.Zhang,L.Wang,andQ.Shi,“Multimodalimagesegmen- consistencyandconfidence,”inProc.Adv.NeuralInf.Process.Syst.,2020,
tationwithdynamicadaptivewindowandcross-scalefusionforheteroge- vol.33,pp.596–608.
neousdataenvironments,”Appl.Sci.,vol.15,no.19,2025,Art.no.10813. [41] L. Yang, L. Qi, L. Feng, W. Zhang, and Y. Shi, “Revisiting weak-
[Online].Available:https://www.mdpi.com/2076-3417/15/19/10813 to-strong consistency in semi-supervised semantic segmentation,” in
[18] D.Lu,S.Cheng,L.Wang,andS.Song,“Multi-scalefeatureprogressive Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2023,
fusion network for remote sensing image change detection,” Sci. Rep., pp.7236–7246.
vol.12,no.1,2022,Art.no.11968. [42] C. Han, C. Wu, M. Hu, J. Li, and H. Chen, “C2F-semiCD: A coarse-
[19] Y. Chen, W. Jiang, and Y. Wang, “FAMHE-net: Multi-scale feature to-fine semi-supervised change detection method based on consistency
augmentationandmixtureofheterogeneousexpertsfororientedobject regularization in high-resolution remote sensing images,” IEEE Trans.
detection,”RemoteSens.,vol.17,no.2,2025,Art.no.205. Geosci.RemoteSens.,vol.62,2024,Art.no.4702621.

ZHOUetal.:DECAF-CD:ASEMISUPERVISEDDUAL-ENCODERCHANNEL-AWARENETWORKFORFINE-GRAINEDFORESTCD 12705
[43] Y.Huang,X.Li,Z.Du,andH.Shen,“Spatiotemporalenhancementand XingwangLi(SeniorMember,IEEE)receivedthe
interlevelfusionnetworkforremotesensingimageschangedetection,” M.Sc.degreeincommunicationengineeringfromthe
IEEETrans.Geosci.RemoteSens.,vol.62,2024,Art.no.5609414. UniversityofElectronicScienceandTechnologyof
[44] L. Ding, J. Zhang, H. Guo, K. Zhang, B. Liu, and L. Bruzzone, China,Chengdu,China,in2010andthePh.D.degree
“Joint spatio-temporal modeling for semantic change detection in re- incommunicationengineeringfromtheBeijingUni-
motesensingimages,”IEEETrans.Geosci.RemoteSens.,vol.62,2024, versity of Posts and Telecommunications, Beijing,
Art.no.5610814. China,in2015.
[45] C.-P. Chen, J.-W. Hsieh, P.-Y. Chen, Y.-K. Hsieh, and B.-S. Wang, From2010to2012,hewaswithCombaTelecom
“SARAS-Net: Scale and relation aware siamese network for change Ltd., Guangzhou, China, as an Engineer. He was
detection,” in Proc. AAAI Conf. Artif. Intell., 2023, vol. 37, no. 12, a Visiting Scholar with Queens University Belfast,
pp.14187–14195. Belfast,U.K.,from2017to2018.Heiscurrentlyan
AssociateProfessorwiththeSchoolofPhysicsandElectronicInformationEn-
JingheZhoureceivedtheB.Sc.degreeinmechanical gineering,HenanPolytechnicUniversity,Jiaozuo,China.Hisresearchinterests
engineering and automation from the Beijing Uni- spanwirelesscommunication,intelligenttransportsystem,artificialintelligence,
versity of Posts and Telecommunications, Beijing, andInternetofThings.
China,in2015,andtheM.Sc.degreeincomputersci- Dr. Li is on the editorial board of IEEE TRANSACTIONS ON COMMUNI-
enceandtechnologyfromHainanUniversity,Haikou, CATIONS,IEEETRANSACTIONSONINTELLIGENTTRANSPORTATIONSYSTEMS,
China,in2018.Sheiscurrentlyworkingtowardthe IEEETRANSACTIONSONVEHICULARTECHNOLOGY,IEEEWIRELESS,COM-
Ph.D.degreeincomputersciencewiththeFaculty MUNICATIONSLETTERS,IEEECOMMUNICATIONSLETTERS,etc.
ofComputingandInformatics,UniversitiMalaysia
Sabah,KotaKinabalu,Malaysia.
SheiscurrentlyanAssociateProfessorwiththe
HainanVocationalUniversityofScienceandTech-
nology,Haikou,China.Herresearchinterestsincludeartificialintelligence(AI),
ecologicalremotesensing,andspatiotemporalanalysis.
Dr. Zhou was the recipient of Hainan’s “New Star of the South China
Sea”talentaward,theThirdPrizeofthe2024HainanProvincialScienceand
TechnologyProgressAward,andtheSecondPrizeofthe2024HainanProvincial
ArtificialIntelligenceScienceandTechnologyAchievementAward.
JinmeiShi(Member,IEEE)receivedthePh.D.de- JianglinLuoreceivedtheB.E.degreeincomputer
greeincomputersciencefromUniversitiMalaysia scienceandtechnologyfromtheHunanInstituteof
Sabah,KotaKinabalu,Malaysia,in2023. Technology,Hengyang,China,in2022andtheM.E.
SheiscurrentlyaProfessorandDoctoralSuper- degreeincomputertechnologyfromHainanNormal
visorwiththeHainanVocationalUniversityofSci- University,Haikou,China,in2025.
enceandTechnology,Haikou,China.Sheleadsthe Heiscurrentlyafull-timeLecturerwiththeHainan
“ComputerScienceandTechnology”keydiscipline Vocational University of Science and Technology,
anddirectsthe“HainanProvinceWisdomInternetof Haikou,China.Hiscurrentresearchinterestsinclude
ThingsEngineeringandTechnologyResearchCen- ecologicalremotesensing,andtime-seriesanalysis.
ter.” She has led multiple projects funded by the
NationalandProvincialNaturalScienceFoundations
andhasauthoredorcoauthoredmorethan50papers.Herresearchfocuseson
artificialintelligence,imageanalysis,andelectronicinformation.
Dr.ShiwastherecipientofHainan’s“NewStaroftheSouthChinaSea”talent
award,theThirdPrizeofthe2024HainanProvincialScienceandTechnology
ProgressAward,andtheSecondPrizeofthe2024HainanProvincialArtificial
IntelligenceScienceandTechnologyAchievementAward.
XianPengWang(Member,IEEE)wasbornin1986.
HereceivedtheM.S.andPh.D.degreesinnavigation, Yu-BengLeau(SeniorMember,IEEE)receivedthe
guidanceandcontrolfromtheCollegeofAutoma- B.Sc. degree in multimedia technology from Uni-
tion,HarbinEngineeringUniversity,Harbin,China, versiti Malaysia Sabah, Kota Kinabalu, Malaysia,
in2012and2015,respectively. in 2004, the M.Sc. degree in information security
Hewasafull-timeResearchFellowwiththeSchool from Universiti Teknologi Malaysia, Johor Bahru,
of Electrical and Electronic Engineering, Nanyang Malaysia, in 2007, and the Ph.D. degree in inter-
Technological University, Singapore, from 2015 to net infrastructures security from University Sains
2016. He is currently a Professor with the School Malaysia,GeorgeTown,Malaysia,in2016.
of Information and Communication Engineering, He is currently an Associate Professor with the
HainanUniversity,Haikou,China.Heistheauthorof Faculty of Computing and Informatics, Universiti
morethan80paperspublishedinrelatedjournalsandinternationalconference Malaysia Sabah. His current research interests in-
proceedingsandwasaReviewerofmorethan20journals.Hismajorresearch cludeintrusiondetectionandprediction,networksecuritysituationawareness,
interestsincludecommunicationsystem,arraysignalprocessing,radarsignal IPv6security,theInternetofThings(IoT),andinformationcentricnetworks
processing,compressedsensing,anditsapplications. (ICN).