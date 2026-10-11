International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
ContentslistsavailableatScienceDirect
International Journal of Applied Earth
Observation and Geoinformation
journalhomepage:www.elsevier.com/locate/jag
A refined edge-aware convolutional neural networks for agricultural
parcel delineation
Rui Lua, Yingfan Zhanga, Qiting Huangb, Penghao Zenga, Zhou Shia, Su Yea,c,*
aInstituteofAgriculturalRemoteSensingandInformationTechnologyApplication,CollegeofEnvironmentalandResourceSciences,ZhejiangUniversity,Hangzhou
310058,China
bAgriculturalScienceandTechnologyInformationResearchInstitute,GuangxiAcademyofAgriculturalSciences,Nanning530007,China
cKeyLaboratoryofEnvironmentRemediationandEcologicalHealth,MinistryofEducation,CollegeofEnvironmentalResourceSciences,ZhejiangUniversity,310058
Hangzhou,China
A R T I C L E I N F O A B S T R A C T
Keywords: Accurate delineation of agricultural parcels is crucial for ensuring food security and implementing precision
Agriculturalparcels agriculturepractices.However,oneoftheprimarychallengesinparceldelineationrevolvesaroundtheaccurate
Convolutionalneuralnetworks extractionofparceledgesduetothediversemorphologiesoftheseparcels.Currentdeeplearningmodelsfor
Edgedetection
agriculturalparceldelineationoftenproduceunclosedorincompleteedges,highlightingtheneedtoenhancethe
Deepsupervision
edge-awarenessofthemodel.Inthisstudy,weproposedarefinededge-awareU-Net(REAUNet)toextractac-
Boundaryrefinement
curateagriculturalparcelboundariesfromSentinel-2imagesandGF-2images.REAUNetintegratesfourinno-
vativecomponentsforedgeenhancement,i.e.,thedeepsupervision,theedgedetectionblock,thedualattention
blockandtherefinemodule.Theedgedetectionblockandthedualattentionblockstrengthentheabilityof
capturingspatialcontextualinformation,andthedeepsupervisionconstrainsparceldelineationacrossmultiple
scales,andtherefinemodulefurtherrefinestheparceledges.Together,thesecomponentsenhancetheedge-
awarenessofthemodel,resultinginmoreaccurateagriculturalparceldelineation.Fromtheablationexperi-
ment,REAUNetwithallfourcomponentsreachedthehigheraccuracythanthescenariosthatonlythreeoutof
fourcomponentswereretained,whichsuggestedthattheinclusionofallfourcomponentswasessential.The
comparativeevaluationshowedthatourproposedmodelsurpassedtherepresentativedeeplearningmodelsfor
boththematicandgeomanticaccuracy.REAUNetdemonstratedanincreaseof2.0%inF1-scoreandadecrease
of3.4%inGTC(GlobalTotal-Classification)comparedtotheSEANet,andexhibiteda0.8%increaseinIoUand
a2%decreaseinGTCrelativetotheMPSPNet.WealsoassessedthecapabilityoftheREAUNetmodeltrans-
ferredforanewgeographicregion,andreportedthatapre-trainREAUNetmodelwithonlyasmallnumberof
localsamplescouldachieveasatisfactoryaccuracy.Toconclude,thenewlyproposedREAUNetmodelreachesa
highmappingaccuracyfordelineatingagriculturalparcelsfromthehigh-resolutionimages.Withthepowerful
edge-awarecapability,REAUNetcaneffectivelyutilizelimitedtrainingsamplestotransferadeeplearningmodel
foranewregion,facilitatingthegenerationofagriculturalparcelproductsandalarge-scaleagriculturalparcel
mappinginpracticalapplications.
1. Introduction industrializedagricultureexpansion(Liuetal.,2021a).Thesuccessof
these efforts is contingent on the availability of highly accurate
Withglobalpopulationgrowthandclimatechange,foodsecurityhas geographic information on agricultural parcels (Potapov et al., 2022;
becomeasignificantconcernworldwide(Godfrayetal.,2010;Luetal., Zabel et al., 2019). Particularly, parcel boundary maps could deliver
2015). Numerous efforts were made to address various facets of this fine-scale information on the size, geometry and spatial locations of
challenge, including field yield enhancement (Garibaldi et al., 2016; agriculturalparcel,potentiallyprovidingkeyinputstotheapplications
Pywelletal.,2015),climateadaptationandriskmanagement(Kuang suchasparcelsizeanalysis(Estesetal.,2022),croptypemapping(Cai
et al., 2022), cropping intensity monitoring (Huang et al., 2024), et al., 2018), crop yield forecasting (Lobell et al., 2015) and natural
* Correspondingauthor.
E-mailaddress:su.ye@zju.edu.cn(S.Ye).
https://doi.org/10.1016/j.jag.2024.104084
Received14April2024;Receivedinrevisedform2August2024;Accepted5August2024
Available online 16 August 2024
1569-8432/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
disastermonitoring(Yeetal.,2021). thisissue,Lietal.(2023)presentedanedge-awareSEANetincorporated
Whileenormouseffortshavebeenmadetomapagriculturalparcel localandglobaledgesemanticsatmultiplelevelstoderivemoreaccu-
usingsatellite-basedtechnology,fewdatasetsareavailableonagricul- rateagriculturalparcelextraction.WhileSEANetdemonstratedefficacy
turalparcelboundaries.Themajorimpedimentisthatparcelboundaries in delineating agricultural parcels of diverse shapes and sizes, the
tend to intergrade with surrounding vegetation from optical satellite method exhibited certain limitations. Primarily, the proposed edge-
images,leadingtoanalgorithmicchallengeforboundarydetection.The awareapproachgeneratesedgefeaturerepresentationsbyusing1×1
edge detector was widely applied to delineate parcel boundaries by convolutions from the scratch which requires considerable training
identifying object edges as discontinuities of image brightness samplestoachieveanacceptableaccuracy.Additionally,theextracted
(Crommelincketal.,2017;GraesserandRamankutty,2017;Turkerand agricultural parcel boundaries were either indistinct or obscured by
Kok,2013;YanandRoy,2014),butoftenfailedtogeneratesatisfactory surroundinglandcovers(Lietal.,2023),suggestingmoreedgerefine-
segmentation results (Waldner and Diakogiannis, 2020). An edge de- mentneededonthesegmentationresults.
tectorcomputesanimagegradientusinganimagefiltering/kernel.The In this study, our aim was to delineate agricultural parcels with
gradient threshold required by the edge detector for identification is boundariesthatarebothpreciseandgeometricallysound,employinga
universally unavailable for the whole image. Besides, the parcel sizes deeplearningmodelintegratedwithrefinededge-awaremethods.We
often vary from 0.01 to 100 ha (Waldner and Diakogiannis, 2020), developed a sematic segmentation neural network, named Refined
whichposesaknottychallengeondetectingmultiscaleboundaries.A Edge-Aware U-Net (REAUNet), to enable an extraction of multi-scale
delineationofasmallerparcelismorepronetonoiseagainstalarger parcel information and fine-tune parcel edge. REAUNet contains four
parcel.Asaresult,weareoftenunabletoapplyoneedgedetectorwitha innovative components to enhance its ability of delineating parcel
gradientthresholdforparcelsegmentation(Crommelincketal.,2017; boundaries: the deep supervision, the edge detection block, the dual
Hongetal.,2021). attentionblockandtherefinemodule.Differentwiththepreviouswork
Toenableamoreaccuratedelineationofcropboundaryandextent, suchasSEANet,REAUNetdirectlyintegratestraditionaledgedetection
ConvolutionalNeuralNetwork(CNN)hasbeenwidelyappliedtomap operators instead of data-driven tuning, which allows the model to
agriculturalparcelrecently(Perselloetal.,2019;Taravatetal.,2021; diminish the reliance on extensive labeled dataset and to reduce the
WaldnerandDiakogiannis,2020;Zhangetal.,2020).CNNiscapableof requiredvolumeoflocalsamplesforspatialgeneralization.Finally,the
learning complexhierarchicalcontextualfeatures(Yuanetal.,2021), modelperformancewillbeassessedincomparisontootherstate-of-the-
thereby mapping accurate parcels for various crop types in multiple artdeeplearningmodels.Themaincontributionsare:
scales. AmongthevariousCNN algorithms,theycanbe broadlycate-
gorizedintothreetypes:modelrefinement,multi-modalmethods,and (1) developing a refined edge-aware deep learning model to effec-
multi-task learning methods. Model refinement primarily aims to tivelydelineateagriculturalparcelsfromremotesensingimages;
enhance model performance by modifying the model architecture. (2) formulatingapost-processingworkflowtooptimizethegeometry
Zhangetal.(2020)demonstratedMPSPNettocombinelow-leveland andshapeofextractedparcels;
high-levelinformation.Thelow-levelinformationcapturesedgedetails (3) demonstrating the capability for utilizing limited samples to
related to object boundaries, while the high-level information learns transferatrainedmodelforanewregion.
long-rangespatialdependencies,bothofwhichaidintherecognitionof
agricultural parcels. Waldner and Diakogiannis (2020) proposed 2. Studyareasanddatasets
ResUNet-a,whichincorporatesparallelbranchingatrousconvolutions.
This enables multi-scale feature extraction and fusion across different 2.1. Studyareas
receptivefields.Panetal.(2023)proposedtheE2EVAPframeworkto
extract the vertices of each parcel boundary individually, where Fourtestingsiteswereselectedtoevaluateourmethod(Fig.1):the
semantic-contourinteraction andtopologicallosswereusedtoaggre- Netherlands (NL), Denmark (DK), and two regions Huantai (HT) and
gate foreground features and establish topological relationships. This TarimRiver(TR)inChina.Twoimagesourcesweretested,i.e.,10-m
approachhasmultipledirectionsformodelimprovement,allowingthe Sentinel-2 and 1-m Gaofen-2 (GF-2) images. Sentinel-2 images were
modeltofocusondifferentkindsofsituations.Multi-modalmethodsuse acquired from Google Earth Engine (GEE) for the areas NL and DK,
multipledataascomplementaryinformationtoimproveparcelextrac- whichwerepreprocessedthroughatmosphericcorrection,radiometric
tion accuracy. Caiet al. (2023a) proposedDSTFNet, which integrates correction,geometriccorrection,andterraincorrection.Wechosedata
high-resolutionimageswithmedium-resolutiontime-seriesimages.This for the year 2022 with cloud cover less than 10 %. A temporal
model captures spectral dynamics, aiding in the extraction of diverse compositing technique was employed to generate composite data
agriculturalparcels.Sunetal.(2022)combinedmulti-temporaloptical coveringtheentirestudyareabasedonthemeanvalue.Thereference
andSARremotesensingdatatoaddressthelimitationsofopticaldata dataforagriculturalparcelsinNLwasavailablefromtheBasisregistratie
availability,especiallyincloudyandrainyregion.Thisapproachcom- Gewaspercelen(BRP)(https://www.pdok.nl/introductie/-/article/basi
pensatesfortheshortcomingsofusingasingledatasource.However,it sregistratie-gewaspercelen-brp-), while corresponding data in DK was
canpresentchallengesrelatedtodatacollectionandavailability.Multi- sourced from the European Union Land Parcel Identification System
task learning methods enable the model to simultaneously extract (LPIS) (https://collections.eurodatacube.com/). The polygons of agri-
correlated information, such as parcel extent and parcel edges. Long culturalparcelsinBRPandLPISweremanuallycreatedbytheagencies.
et al. (2022) proposed BsiNet with multi-task learning and attention The other two study regions in China comprised of HT in Shandong
mechanismtobetterdelineateagriculturalparcels.Wangetal.(2023) Province, and TR in Xinjiang Province. High-resolution GF-2 images
introduced BSNet, which employs multitask learning to extract agri- wereobtainedrespectivelyonMarch2022forHT,andonSeptember
culturalparcelsandtheiredges,andthenfusestheseresultstoproduce 2022forTR.ThepreprocessingstepsforGF-2imageryincludedatmo-
the final output. However, multi-task learning is a training approach spheric correction, radiometric calibration, geometric correction, and
thatdoesnotalterthemodelstructureanddoesnotinherentlyenhance PANsharpening,resultinginthefinal1-mresolutionmultispectraldata.
themodelabilitytobetterfocusonedges. ThegroundtruthparcelsforGF-2imagerywerecraftedthroughmanual
Despitetheirimpressiveaccuracy,currentdeeplearningmodelsstill annotation.
face limitations in delineating agricultural parcels with varying mor- Thefourregionscoveradiversityofagriculturalsystems.IntheNL
phologiesandcomplexshapes(Lesivetal.,2019;Zhangetal.,2021). area, agricultural parcels are diverse, including well-organized large-
Many CNN-based approaches might lose edge information during the scaleparcels,intensivenarrowparcels,andirregularparcels.Themain
backpropagation process, causing vanishing gradient issue. To tackle crops are ornamental crops, potatoes, sugar beet, maize, cereals, and
2

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.1. Overviewoffourstudyareasincluding(a)Netherlands(NL),(b)Denmark(DK),(c)Huantai(HT)and(d)TarimRiver(TR).Sentinel-2imageswereselected
for(a)NLand(b)DK,andGF-2imageswereselectedfor(c)HTand(d)TR.Thedatafrom(b)DKand(d)TRwereexclusivelyusedinthetransferexperiment.The
redboxesdenotethedatautilizedfortrainingandvalidation,whiletheyellowboxesrepresentthetestdata.(Forinterpretationofthereferencestocolorinthis
figurelegend,thereaderisreferredtothewebversionofthisarticle.)
| onions.WhilesimilartoNLwithwell-organizedagriculturalparcels,DK |     |     |     |     |     |     |     | 3. Methods |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
alsoincludessmaller,moreirregularlyshapedparcelsduetoitsdiver-
sified terrain, with barley, wheat, rapeseed, and corn as the primary TheworkflowofourstudyisillustratedinFig.2.Afterimagepre-
crops.Thesetwoareasrequirethemodeltodelineatedifferentpatterns processing,wewilltrainthenewRefinedEdge-AwareU-Net(REAUNet)
and complex boundaries of agricultural parcels. In the HT area, agri- modelwhichconsistedoffourinnovativecomponentsforanimproved
cultural parcels vary in size and shape, predominantly cultivated for agriculturalparcelidentification, thenapply apost-processingstepto
wheatandcornwithparcelsatdifferentsizes.TheXJareafeaturesvast enhance edge delineation, andfinally performamulti-angle accuracy
| land resources | with       | large       | agricultural | parcels | mixed            | with      | smaller, | assessment.                          |     |     |     |     |     |     |
| -------------- | ---------- | ----------- | ------------ | ------- | ---------------- | --------- | -------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| irregular      | ones. The  | differences | among        | the     | four areas       | highlight | the      |                                      |     |     |     |     |     |     |
| challenge      | of calling | for model’s | versatility  | and     | generalizability |           | across   |                                      |     |     |     |     |     |     |
|                |            |             |              |         |                  |           |          | 3.1. Refinededge-awareU-Net(REAUNet) |     |     |     |     |     |     |
variouslandscapes.
WedevelopedthearchitectureofourproposedREAUNetbasedupon
2.2. Datasets
|     |     |     |     |     |     |     |     | U-Net (Ronneberger |     | et  | al., 2015) with | four innovative | components |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------------- | --------------- | ---------- | --- |
(Fig.3).TheproposedarchitectureadoptstheResBlock-34(Heetal.,
Thetraining,validation,andtestingregionswererandomlyselected
2016)asthebasicconvolutionalblock(Fig.3b),anduses5×5con-
| from the | images, as | displayed | in  | Fig. 1. The | regions | designated | for |            |         |         |                      |        |     |          |
| -------- | ---------- | --------- | --- | ----------- | ------- | ---------- | --- | ---------- | ------- | ------- | -------------------- | ------ | --- | -------- |
|          |            |           |     |             |         |            |     | volutional | kernels | in some | of the convolutional | layers | of  | the deep |
trainingandvalidationwerecroppedintochipswithauniformsizeof
encodertoexpandthereceptivefieldandbettercaptureglobalinfor-
256*256pixelsandsubsequently dividedintotrainingandvalidation mation.Themodelcanbedividedintotwoparts:thepredictmoduleand
sets using a random 8/2 split. During the training process, a total of the refine module, with the prediction module serving as the model
2,287 training chips and 572 validation chips were used in the NL backbone. This backbone employs an encoder-decoder structure with
dataset.TheHTdatasetconsistedof1,962trainingchipsand491vali-
skipconnections,enablingthesimultaneouscaptureofhigh-levelglobal
dationchips.Weemployeddataaugmentationtoenhancetheamount
contextsandlow-leveldetailedfeatures.Itisorganizedintofoursym-
| and diversity | of training | samples. |     | For each | sample, | one of | the five |     |     |     |     |     |     |     |
| ------------- | ----------- | -------- | --- | -------- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
metricstagesandabridgestage,incorporatingadditionalconvolutional
transformations,i.e.,unchanged,horizontallyflipped,verticallyflipped,
|     |     |     |     |     |     |     |     | layers at | the deeper | stages. | In each stage | of the encoder, |     | an edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | ------------- | --------------- | --- | ------- |
rotated90degrees,androtated180degrees,wasrandomlyapplied.In
detectionblockisinsertedbetweentheconvolutionalblocks,andadual
thetransferexperiment,weselected100trainingchipsfromeachnew
attentionblockisaddedattheend.Thebridgestageutilizesapyramid
| region. It | is noteworthy | that | we used | all pixels | in  | the testing | area |     |     |     |     |     |     |     |
| ---------- | ------------- | ---- | ------- | ---------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
poolingmoduleformulti-scalefeaturefusion.Itcombinesfeaturesfrom
(“yellowrectangle”inFig.1)forthefinalaccuracyassessment,instead
multiplescales,therebygeneratingglobalcontextknowledgethaten-
ofselectedchips. compassesbothlow-levelandhigh-levelinformation(Zhaoetal.,2017).
|     |     |     |     |     |     |     |     | In lieu of | maximum | pooling, | a convolution | operation | with | the kernel |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | ------------- | --------- | ---- | ---------- |
3

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.2. Theworkflowofthestudy.
sizeof3×3andthestrideof2isusedforthedown-samplingprocessto detectgradientsinthefeaturemapsalongfourdirections(Ranjanand
minimize information loss, while a bilinear interpolation is employed Avasthi, 2023), and subsequently fuses the features in each gradient
fortheup-samplingprocess.Thebelowarethedetailsforfourinnova- directionthroughaconvolutionallayer.Commondeeplearningmodels
tivecomponentswithinREAUNet. oftenlackexpertknowledgeandrelyheavilyondata-drivenlearning.
REAUNetaugmentsthemodelwithtraditionaledgedetectionoperators.
3.1.1. Deepsupervision By leveraging this empirical knowledge, REAUNet bolsters the model
Deepsupervisionisawidelyemployedtechniqueindeeplearning capabilitytoextractsophisticatedsemanticfeaturesfromlimitedsam-
models for edge detection (Liu et al., 2017; Xie and Tu, 2015). This ples.Also,theedgedetectionblockcompensatesforomissionsofedge
approach involves adding supervision signals at hidden layers of a featuresthroughresidualconnections.
neural network, effectively guiding the learning process at multiple
stages. Deep supervision could alleviate the problem of gradient van- 3.1.3. Dualattentionblock
ishing and provide robust regularization of learned features, which is Thedualattentionblock(Fig.3d)integrateschannelattentionand
particularly beneficial for a case of small training data and shallower spatial attention. Each component performs parallel computations of
networks.InourproposedREAUNet,deepsupervisionisintegratedby globalaveragepoolingandglobalmaximumpooling,inspiredbypre-
combining multiple coarse outputs from the predict module with the vious works (Roy et al., 2018; Woo et al., 2018). The benefit of the
refineoutputfromtherefinemodule,whichensuresthatsupervisionis proposedattentionmechanismisthatitexploresthespatial-contextual
applied across different-sized feature maps. By supervising multiple relationship among pixels in addition to interaction among feature
layers,thenetworkcanenhancefeatureregularizationandlearnricher channels.Thisblockenablesthemodeltobetterfocusonareasthatare
featurerepresentations. pronetoerrors,suchastheedgesofagriculturalparcels.
3.1.2. Edgedetectionblock 3.1.4. Refinemodule
Theedgedetectionblock(Fig.3c)wasinsertedintothemiddleof The refine module, inspired by BASNet (Boundary-Aware Salient
each stage to integrate edge gradient information during the feature Network)(Qinetal.,2019),wasimplementedtofurtherenhanceedge
extraction step, so that we could reinforce the ability of recognizing predictionaccuracyofthepredictmodule(Fig.3a).Thepredictmodule
agriculturalparceledges.ThisblockappliesfourdifferentSobelfiltersto generatesacoarsemapwithcommendableregionalaccuracy,yetthere
4

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.3. ThearchitectureoftheproposedREAUNetforagriculturalparceldelineation.Fourinnovativecomponentsarehighlightedastheredcolor:deepsupervision,
edgedetectionblock,dualattentionblock,andrefinedmodule.(Forinterpretationofthereferencestocolorinthisfigurelegend,thereaderisreferredtotheweb
versionofthisarticle.)
| r em a in s | p o te n t i a l f o r e n | h a n c i n g e | d g e q u a l i t y . T h e | r e fi n e m o d u l e s e r ve s |     | ∑   |     |     |     |     |     |
| ----------- | -------------------------- | --------------- | --------------------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
1 N 2 y ⋅̂y
t o re fi n e t h e s e g m e n t a t i o n r e s u l t s b y r e c t i fy i n g o m i s s i o n / c o m m i s s i o n s in LDice =1(cid:0) i i (3)
|     |     |     |     |     |     | N   | i=1y + ̂y |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
t h e c o a rs e m a p . I t o p e r a t e s a s t r a i g h t f o r w a r d r e s i d u a l e n c o d e r - d e c o d e r i i
architecturetolearn theresidualmapbetweentheoutputofthepre- whereyi denotesthebinarygroundtruthlabel, ̂yi representsthepre-
dictmoduleandthegroundtruth.Boththeencoderanddecoderconsist dictedresult,andNsignifiesthetotalnumberofpixels.
of four layers symmetrically, each containing only one convolutional Parcelboundarydelineationisakintoanedgedetectiontask,andthe
layer. distribution of edge pixels and non-edge pixels is typically highly
Finally,weutilizedlabelsfortheagriculturalparcelextentandthe
|                 |              |     |                     |                  | imbalanced. | Accordingly, |     | we employed | a dynamically | weighted | BCE |
| --------------- | ------------ | --- | ------------------- | ---------------- | ----------- | ------------ | --- | ----------- | ------------- | -------- | --- |
| parcel boundary | to construct | two | models respectively | for agricultural |             |              |     |             |               |          |     |
loss,wheretheweightsadapttotheproportionofpositiveandnegative
parcelandboundaries,andthenderivedtheultimateparceldelineation
|     |     |     |     |     | pixels. | In addition, | we integrated | a   | sum-based | loss calculation | mode |
| --- | --- | --- | --- | --- | ------- | ------------ | ------------- | --- | --------- | ---------------- | ---- |
resultbymergingtheextentmaskandtheboundarymask.
insteadofaveraging,therebyamplifyingthelossweightsforthelimited
ThecodesfortheREAUNethavebeenmadepubliclyavailableinhtt
numberofedgesamples.Theboundarylossfunctionwasdefinedas:
ps://github.com/Remote-Sensing-of-Land-Resource-Lab/REAUNet.
∑
|     |     |     |     |     | =     | N w⋅(yi | ⋅loĝyi +(1(cid:0) | )⋅log(1(cid:0) | ̂yi )) |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | ------------------ | -------------- | ------ | --- | --- |
|     |     |     |     |     | Ledge |         |                    | yi             |        |     | (4) |
i=1
| 3.2. Lossfunctionsandtrainingdetails |     |     |     |     | ⎧   |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
⎪⎪⎪⎪⎨
|     |     |     |     |     |     | N n e g a t i v | e = |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
D i ff e r e n t l o s s f u n c t i o n s a re e m p l o y e d f o r p a r c e l e x t e n t t r a i n i n g a n d i f y i 1
|     |     |     |     |     |     | N b a t c h |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
p a r c e l b o u n d a r y t r a i n i n g . T h e s e g m e n t a t i o n o f a g ri c u l tu r a l p a r c e l e x t e n t w= (5)
⎪⎪⎪⎪⎩ α× N
ca n b e v i e w e d a s a s e m a n t i c s e g m e n t a t i o n t a s k . T h e l o s s f u n c t i o n f o r p o si tive i f y = 0
|                 |                         |                   |                               |                             |     | N         | i   |     |     |     |     |
| --------------- | ----------------------- | ----------------- | ----------------------------- | --------------------------- | --- | --------- | --- | --- | --- | --- | --- |
| p a r c e l e x | t e n t c o m b i n e s | a b i n a r y c r | o s s - e n t r o p y ( B C E | ) l o s s L a n d a d i c e |     | b a t c h |     |     |     |     |     |
B C E
| loss LDice                          | to tackle sample | imbalance | and ensure | the stability of the |                                   |             |                |            |             |            |        |
| ----------------------------------- | ---------------- | --------- | ---------- | -------------------- | --------------------------------- | ----------- | -------------- | ---------- | ----------- | ---------- | ------ |
|                                     |                  |           |            |                      | where                             | w refers    | to the weights | calculated | dynamically | based      | on the |
| trainingprocess.Thiscanbedefinedas: |                  |           |            |                      |                                   |             |                |            |             |            | α      |
|                                     |                  |           |            |                      | number                            | of positive | and negative   | samples    | in each     | batch, and | is the |
| =0.5×LBCE                           | +LDice           |           |            |                      |                                   |             |                |            |             |            |        |
| Lextent                             |                  |           |            | (1)                  | samplebalancecoefficientsetto1.1. |             |                |            |             |            |        |
( ) Ourhyperparametertuningprocessfocusesontwocriticalparame-
∑
1 N t er s : t h e l e a rn i n g r at e a n d t h e w e i g h t d e c a y. T h e le ar n i n g r a t e se le c t io n
LBCE =(cid:0) (yi ⋅loĝyi +(1(cid:0) yi )⋅log(1(cid:0) ̂yi )) (2) (cid:0)
N i=1 m e t h o d , r e fe rr e d t o S m i th ( 2 0 1 7 ) , in v o l v e d se t ti ng a r a n g e f r o m 1 0 5 t o
10 (cid:0) 2.Weconducted8epochsoftrainingwithvariouslearningratesand
5

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
thenchosethelearningrateassociatedwiththehighestfinalaccuracyas 3.4. ComparisonwithrepresentativeCNNmodels
theinitiallearningrate.Fig.4(a)indicatesthatthelearningrateof3×
10 (cid:0) 4achievedthehighestaccuracy,whichwasconsideredtheoptimal Inordertoevaluatetheeffectivenessofourmethod,weconducteda
initial learning rate. After determining the initial learning rate, we comparative analysis of eight CNN models specifically designed for
performedanexperimentcomprising100trainingepochs,varyingthree segmentationtasksandagriculturalparceldelineation.Table1presents
(cid:0) 3,10 (cid:0) 4,10 (cid:0) 5).Fig.4(b)showsthatthe
weightdecayparameters(10 thebriefdescriptionsfortheseCNNmodels.
(cid:0) 4achievedthelowestlossvalueduringtraining.Asa
weightdecayof10
result,weemployedtheAdamoptimizerwithaninitiallearningrateof 3.5. Modeltransferabilityexperiment
| (cid:0)  |                    |           | (cid:0)       |           |     |     |     |     |
| -------- | ------------------ | --------- | ------------- | --------- | --- | --- | --- | --- |
| 3 × 10 4 | and a weight decay | of 1 × 10 | 4. The models | underwent |     |     |     |     |
trainingforamaximumof200epochswithabatchsizeof8.Incasesof ToassessthecapabilityofREAUNetbeingappliedtodifferentagri-
themodellossplateauingfor30consecutiveepochs,thelearningrate cultural areas, we conducted a model transferability experiment. We
was reduced by a factor of 0.1. If the validation set loss showed no testedthemodeltrainedfromNLonDKregionforSentinel-2images,
improvement for 50 consecutive epochs, we implemented an early and the model from HT on the TR region for GF-2 images. In this
stoppingtomitigateoverfitting.
experiment,wedefinedthreescenarios:NoTraining(NT)impliesthat
themodel,previouslytrainedinotherregions,wastakentomakepre-
3.3. Post-processing dictionsdirectlyinthenewregion(e.g.,usingthemodeltrainedonNL
datatodelineateparcelsintheDKarea);DirectTraining(DT)trained
Wedesignedapost-processingworkflowtofurtherimprovetheedge themodelmerelyusinglocalsamples;TransferTraining(TT)pretrained
delineation.Thespecificstepswereoutlinedasfollows: a model using data from another region first, followed by continued
trainingwithlocalsamplesfromthenewregion.TheNTscenariocanbe
(1) applieda1-pixelbuffertotheparcelboundaryresults,reducing also viewed as a validation of the model generalizability when con-
| theboundaryinterruptionintheresults; |     |     |     |     | frontedwithanewregion. |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
(2) performedamorphologicalthinningoperationontheboundary Inthenewregionselectedforthetransferexperiment,weoptedfora
resultscorrespondingtothepreviousbuffer; smallareatogeneratetrainingsamples,resultinginapproximately100
(3) utilizedtheparcelextentmaskandtheboundarymasktodelin- ×256
|     |     |     |     |     | samples | of size 256 pixels. | The REAUNetDT | followed the same |
| --- | --- | --- | --- | --- | ------- | ------------------- | ------------- | ----------------- |
eateindividualagriculturalparcelswiththecutoffmethod,and protocol as REAUNet, with a maximum of 200 epochs. On the other
thecutoffthresholdwassetto0.5(WaldnerandDiakogiannis, hand, REAUNetTT was trained for a shorter duration, specifically 20
| 2020);        |               |            |               |            | epochs. |     |     |     |
| ------------- | ------------- | ---------- | ------------- | ---------- | ------- | --- | --- | --- |
| (4) conducted | morphological | processing | on the binary | results to |         |     |     |     |
eliminateholesandsmallisolatedpixels; 3.6. Accuracyassessment
| (5) vectorized | the results | and employed | the Douglas-Peucker | algo- |     |     |     |     |
| -------------- | ----------- | ------------ | ------------------- | ----- | --- | --- | --- | --- |
rithmtoremoveredundantnodes,optimizingtheedgesofagri- Weusedatotalofsixevaluationmetricstoassesstheperformanceof
culturalparcels; model for delineating agricultural parcels from both pixel-based and
(6) detectedandeliminatedover-sharpangles. object-basedperspectives,i.e.,OverallAccuracy(OA),Intersectionover
|     |     |     |     |     | Union | (IoU), F1-score (F1), Global | Over-Classification | (GOC), Global |
| --- | --- | --- | --- | --- | ----- | ---------------------------- | ------------------- | ------------- |
Fig.5exemplifiestheimprovementbroughtbythepost-processing
Under-Classification(GUC)andGlobalTotal-Classification(GTC).The
step. We applied a morphological thinning operation to narrow the pixel-basedmetrics(OA,IoUandF1)weredefinedasfollows:
boundary map and subsequently utilized the cutoff method to isolate TP+TN
OA=
individualagriculturalparcels.Althoughthedeeplearningmodelsuc- TP+FN+FP+TN (6)
| cessfully captured | the boundaries  | ofagricultural | parcels,    | some break-    |     |     |     |     |
| ------------------ | --------------- | -------------- | ----------- | -------------- | --- | --- | --- | --- |
| points persisted   | in the results, | leading to     | irregularly | shaped parcels |     | TP  |     |     |
IoU= (7)
being obtained, as shown in Fig. 5(c). To address this, the Douglas- TP+FP+FN
| Peucker algorithm                                            | and the | over-sharp | angle elimination | algorithm |     |      |     |     |
| ------------------------------------------------------------ | ------- | ---------- | ----------------- | --------- | --- | ---- | --- | --- |
| wereemployedtooptimizethespatialgeometricshapesoftheparcels. |         |            |                   |           |     | 2*TP |     |     |
F1= (8)
2*TP+FP+FN
whereTP,TN,FP,andFNrefertoTruePositive,TrueNegative,False
Hyperparameterselection.(a)Thehighestaccuracywasachievedatalearningrateof3×10 (cid:0)4.(b)Thelowestlossvaluewasobtainedwithaweightdecay
Fig.4.
of10 (cid:0)4.
6

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.5. Modelresultsofparcelboundaries.(a)representsareaNL,(b)representsareaHT,and(c)showstherefinedparcelsformedbythepost-processingmethod.
Positive,andFalseNegative,respectively. crucialroleofmulti-scaledeepsupervisionintheaccuratedelineationof
To better assess spatial accuracy of extracted parcels, we adopted agriculturalparcels.
three object-based accuracy metrics as a complementary evaluation, TofurtherexplorethedecisionprocessofREAUNetandenhancethe
baseduponunder-segmentationandover-segmentationerrors(Lietal., model transparency, we outputted the feature maps of the model at
2023;Yeetal.,2018),whichweredefinedasfollowed: different stages to show how the input images is transformed passing
|     | (   | )   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∑ ( ) t h r o u g h t h e l a y e r s . F i g . 7 (b ) il l u s tr a te s t h e f ea t u r e m a p s f r o m t h e
| GOC= | m OC(Si )×∑ | a r e a S i        |     |     |       |               |                    |              |               |             |               |                        |
| ---- | ----------- | ------------------ | --- | --- | ----- | ------------- | ------------------ | ------------ | ------------- | ----------- | ------------- | ---------------------- |
|      |             |                    |     | (9) | s h a | l l o w a n d | d e e p l a y er s | fo r t h e e | n c o d e r s | t a g e , w | h e r e t h e | b r ig h t p i x e l s |
|      | i=1         | m = a r e a ( Si ) |     |     |       |               |                    |              |               |             |               |                        |
i 1 in d i c a t e t h e p a t te r n s t h e R E A U N e t i s s e e k i n g f o r . S h a ll o w f e a t u r e s
|     | (   | )   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∑ ( E n c o d e r # 1 ) t r a i n s m o s t o f t h e i n fo r m a t i o n p r es e n t i n t h e i m a g e . D e e p
|     | m   | a r e a ( S ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GUC= UC(Si )×∑ i (10) f e a t u r e s ( E n c o d e r # 4 ) , o n t h e o th e r h a n d , a r e h i g h - l e v e l f e a t u r e s f o r
|     | i=1 | m a r e a ( Si ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i = 1 s e e k i n g a n a b s t r a c t r e p r e s e n t a t io n . S o m e h i dd e n c l a s s i n f o r m a ti o n , su c h
∑ ( ) a s t h e i m p er v io u s s u r fa c e ( t h e fo u r t h c o l u m n ) , b e c o m e r e c o g n i z a b l e .
|     | m   | a r e a ( S ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GTC= TC(Si )×∑ i (11) T h e o u t p u t f e a t u r e m a p s fo r t he d e c o d e r p re s e n t a r e v er s i n g t r e n d o f
|     | i=1 | m a r e a ( Si ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i = 1 in c r e a si n g d e t a i l s (F ig . 7 c ) f r o m D e c o d e r # 1 t o D e c o d e r # 5 . B e n e fi t e d
whereSi,i=1,2,⋯,mdenotestheclassifiedparcelsinmodelresults.OC(Si ), from the design of deep supervision, REAUNet will integrate these
UC(Si )andTC(Si )weredefinedas: featuremapsgeneratedfromdifferentscalesandguidetheseinterme-
diatelayerstowardsthedesiredsolution,enablingthemodeltobetter
(S ∩ )
OC(Si )=1(cid:0) are a i O i capturehierarchicalrelationshipsamongparcelfeatures.
|     | (O ) |     |     | (12) |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
a re a i
|                  | ( ∩          | )   |     |     | 4.2. | Comparativeexperiment |     |     |     |     |     |     |
| ---------------- | ------------ | --- | --- | --- | ---- | --------------------- | --- | --- | --- | --- | --- | --- |
| UC(Si )=1(cid:0) | are a S i Oi |     |     |     |      |                       |     |     |     |     |     |     |
(13)
a r e a ( Si )
|     |     |     |     |     |     | The accuracy | assessment | results | for | REAUNet | and | other deep |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------- | --- | ------- | --- | ---------- |
√̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
|     |     |     |     |     | learning | models | were presented |     | in Table | 3.  | The REAUNet | model |
| --- | --- | --- | --- | --- | -------- | ------ | -------------- | --- | -------- | --- | ----------- | ----- |
|     | )2+ | )2  |     |     |          |        |                |     |          |     |             |       |
OC(Si UC(Si (14) c on si st e nt l y ou t p e r f o rm ed th e o t h e r m o d e ls f o r m o s t a c c u ra c y me tri c s :
TC(Si )=
2 in th e N L s t ud y a r e a , R EA UN e t d e m o n st r a te d a n i nc r e a s e o f 2 .0 % in F 1 -
|                   |                                                |     |     |     | score | and a | decrease of | 3.4 % | in GTC compared |     | to the | second-best |
| ----------------- | ---------------------------------------------- | --- | --- | --- | ----- | ----- | ----------- | ----- | --------------- | --- | ------ | ----------- |
| WhereOi,i=1,2,⋯,n | representsthereferenceobjectsinthegroundtruth, |     |     |     |       |       |             |       |                 |     |        |             |
SEANet;intheHTstudyarea,REAUNetexhibiteda0.8%increasein
whichistheparcelclosestindistancetoSi.
|     |     |     |     |     | IoU | and a 2 | % decrease | in GTC | relative | to the | second-best | model, |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | ------ | -------- | ------ | ----------- | ------ |
We usedtheseaccuracymetrics(Eq.6–11)foranablationexperi-
MPSPNet.Fig.8visualizestheagriculturalparceldelineationmapsfrom
| ment and | thefinalaccuracyreport. | The ablationexperimentassessed |     |     |         |      |                   |     |             |          |         |          |
| -------- | ----------------------- | ------------------------------ | --- | --- | ------- | ---- | ----------------- | --- | ----------- | -------- | ------- | -------- |
|          |                         |                                |     |     | various | deep | learning methods. |     | In contrast | to other | models, | our pro- |
theaccuracylossafterremovingeachcomponentoutofthefourinno-
posedmethodnotablyreachedthelowestfalsenegativeerrorsatparcel
vativecomponentsfortheREAUNet,sothatwecouldunderstandthe
|     |     |     |     |     | edges. | Additionally, | REAUNet | proves | effective |     | in minimizing | false |
| --- | --- | --- | --- | --- | ------ | ------------- | ------- | ------ | --------- | --- | ------------- | ----- |
accuracycontributionofindividualcomponent. negativeerrors(theblueregion)incertainregionsoftheHTstudyarea,
|     |     |     |     |     | particularly |     | where parcel | boundaries | are | less evident. |     | Thanks to its |
| --- | --- | --- | --- | --- | ------------ | --- | ------------ | ---------- | --- | ------------- | --- | ------------- |
4. Results powerful edge-awareness, REAUNet achieved excellent extraction re-
sultsinstudyareaswithdifferentdatasources.Itsuccessfullyextracted
4.1. Ablationexperiment
complexanddiverseagriculturalparcelsintheNLregionanddelineated
parcelsofvaryingsizesintheHTregion.ThestrengthofREAUNetliesin
Table2depictstheaccuracyfordifferentsettingsofREAUNetinthe
performingcomplexanddiverseparcelextractionatmultiplescales,and
ablationexperiment.IncomparisontotheoriginalREAUNet,allother
|     |     |     |     |     | its | delineation | results in | these regions | surpass | those | of  | several repre- |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------- | ------- | ----- | --- | -------------- |
modelsettingsexhibitednotablyhigherGUC/GTC,indicatingthefour
sentativemodels.
| components | all contribute | to the final geometric | accuracy. | Fig. 6 |     |     |     |     |     |     |     |     |
| ---------- | -------------- | ---------------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
showcasesthattheREAUNetwithallfourcomponents(thethirdcolumn
“REAUNet”)significantlypresentstheleastfalsenegativeerrorsatthe 4.3. Agriculturalparceldelineationresults
edgesofparcels.Amongthefourmodules,theremovalofdeepsuper-
Fig.9displaystheextractionresultsofREAUNetfortheNLandHT
visionhadthemostpronouncedimpactonaccuracy,highlightingthe
areas,showcasingthesuccessfulmappingofagriculturalparcelsfrom
7

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Table1 parcels,aswellasdense,elongatedparcelsintheNLregion.Fig.9(e)
Therepresentativedeeplearningmethodsforagriculturalparceldelineation. and (f) displayed the results for agricultural parcels with complex
|        |                                   |     |                    | shapes.                                              | Likewise, | in  | the HT | region, | the model | successfully |     | identified |
| ------ | --------------------------------- | --- | ------------------ | ---------------------------------------------------- | --------- | --- | ------ | ------- | --------- | ------------ | --- | ---------- |
| Method | Modeldescription                  |     | Reference          |                                                      |           |     |        |         |           |              |     |            |
|        | •                                 |     |                    | variousagriculturalparcelsofdifferentshapesandsizes. |           |     |        |         |           |              |     |            |
| U-Net  | U-Netconsistsofacontractingpathto |     | (Ronnebergeretal., |                                                      |           |     |        |         |           |              |     |            |
|        | capturecontextandasymmetric       |     | 2015)              |                                                      |           |     |        |         |           |              |     |            |
|        | expandingpaththatenablesprecise   |     | (Kumarand          |                                                      |           |     |        |         |           |              |     |            |
4.4. Modeltransferabilityexperiment
|     | localization; |     | Jayagopal,2021) |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•
Everystepintheexpansivepathisfollowed
byaconcatenationwiththe Table4presentstheaccuracyassessmentforthethreescenariosin
correspondinglycroppedfeaturemapfrom the transferability experiment. The REAUNetTT achieved the highest
thecontractingpath. accuracyandsurpassedthemodeltrainedfromscratchfor200epochs
| RCF | • RCFisanend-to-endconvolutional |     | (Liuetal.,2017) |     |     |     |     |     |     |     |     |     |
| --- | -------------------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bysimplycontinuingtrainingfor20epochsusingonly100localsam-
|     | networkdesignedtoextractedges; |     | (Liuetal.,2019) |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• ples. Fig. 10 shows the resultant maps for these three scenarios.
RCFkeepsfiveconvolutionalstagesin
REAUNetNTachievedthelowestaccuracyandexhibitednumerousfalse
VGG16,andthefeaturemapsfromthe
samestagesareaddedupthenupsampled negativepixels(“theblueregion”),indicatingthatthemodelstruggled
t o g e n e ra te a n ed g e p r o b a bi li tymap; intheseregionswithoutlocalsamples.Moreover,REAUNetTTpresented
•
A f u s io n o ut p ut is o b t a in e d b y ahigheraccuracythanREAUNetDTforbothDKandTR,whichsuggested
concatenatingall5edgeprobabilitymaps
inchanneldimension. thesuperiorityofREAUNetintransferringmodelforanewregion.The
•
MPSPNet MPSPNetincorporatesthreecore (Zhangetal.,2020) transfertrainedmodelincurredatrainingcostoflessthan5minand
exhibitedanotable10–15%improvementinF1overtheoriginalmodel.
structures:ResNetwithdilated
convolution,spatialpyramidaverage
poolingmodule,andfusionoflow-level
5. Discussion
andhigh-levelinformation.
| ResUNet- | • ResUNet-aconsistsofresidualunitswith |     | (Diakogiannisetal., |     |     |     |     |     |     |     |     |     |
| -------- | -------------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a multipleparallelbranchesofatrous 2020) 5.1. Comparisontorepresentativemodels
|     | convolutions,eachwithadifferentdilation |     | (Waldnerand        |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ratetoincreasethereceptivefield;        |     | Diakogiannis,2020) |     |     |     |     |     |     |     |     |     |
• ResUNet-aproducesfouroutputlayers:the OurproposedREAUNetoutperformedallrepresentativemodelsfor
extentmask,theboundaries,thedistance agriculturalparcelextractionthatwereselected.Thereweremainlyfour
mask,andfullreconstructionoftheinput innovationstospecificallyimprovemodelperformance,andtheresults
imageintheHSVcolor.
intheablationexperimentindicatedthatallfourcomponentspositively
| BsiNet | • BsiNetsusesonesingledecodertoproduce |     | (Longetal.,2022) |     |     |     |     |     |     |     |     |     |
| ------ | -------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
contributetothefinalaccuracyoftheagriculturalparcels.Incontrastto
threetypesofinformationmask,boundary,
|     |     |     |     | MPSPNet | (Zhang | et  | al., 2020), | which | incorporates |     | residual | dilated |
| --- | --- | --- | --- | ------- | ------ | --- | ----------- | ----- | ------------ | --- | -------- | ------- |
anddistance;
• SGEattentionmoduleisincorporatedinto convolution and pyramid pooling module, our model integrates an
BsiNettoextractenhancedfeatures, attentionmechanismandmulti-scaledeepsupervision.Thedualatten-
utilisingtheglobalinformationandscaling tion block enables the model to better tackle important regions and
theimportanceofdifferentchannels.
|       |                                         |     |                 | critical | features | of  | the parcels | during | the | feature | extraction | process, |
| ----- | --------------------------------------- | --- | --------------- | -------- | -------- | --- | ----------- | ------ | --- | ------- | ---------- | -------- |
| FRNet | • FRNetisdividedintofourparallelstreams |     | (Xiaetal.,2022) |          |          |     |             |        |     |         |            |          |
enhancingitsadaptabilityinhandlingparcelswithdiverseshapesand
inthehorizontaldirection,i.e.,thefirst
streamwithfullresolutionandthe complexstructures.Deepsupervisionallowsthemodeltodetectvarious
additionalthreewithresolutiondecreased
levelsofedgestructuresfromdifferentscales.Thiscapabilityenablesthe
byhalf;
• capturingofedgestructuralinformationpertainingtobothlocaldetails
Differentparallelstreamsareconnected
andfusedbythemulti-resolutionfusion andtheoverallcontext.Notably,weobservedthatremovingthedeep
unit(MRFU). supervisionofthemodelcausesthemostaccuracylossintheablation
•
RAUNet RAUNetusesResNettocapturehigher- (Caietal.,2023b) experiment.TheattentionmechanismanddeepsupervisioninREAUNet
levelabstractfeaturesintheencoder; empowerittoeffectivelyidentifyagriculturalparcelsofvaryingsizes,
• RAUNetintegratescoarse-andfine-scale
resultinginreducedover-segmentationcomparedtoMPSPNet.
featurestosuppressirrelevantnoiseand
Furthermore,incomparisontoSEANet(Lietal.,2023),whichem-
highlightsalientregionswithagated
attentionmechanisinthedecoder. ployssimilaredge-awareandmulti-scalesegmentationtechniques,we
SEANet • SEANetconsistsoftwomaincomponents (Lietal.,2023) enhanced the accuracy of edge region delineation around parcels by
correspondingtoPRoIandPEoIfeature
|     |     |     |     | integrating |     | the edge | detection | operator |     | into REAUNet | (i.e., | Edge |
| --- | --- | --- | --- | ----------- | --- | -------- | --------- | -------- | --- | ------------ | ------ | ---- |
extraction;
• SEANetconstructsastackofconvolution DetectionBlock).ThisinnovationleveragesfourdifferentSobelopera-
blockstoderiveedgefeaturemapsat torsbaseduponempiricalknowledgetodetectfeaturemapedgesacross
multiplelevels. variousgradients,mitigatingtheimpactofthemorphologyofagricul-
turalparcels.Besides,totackletheissueofincorrectpixelsalongparcel
|              |                      |                     |               | edges, | we incorporated |     | a   | small residual | refine | module | following | the |
| ------------ | -------------------- | ------------------- | ------------- | ------ | --------------- | --- | --- | -------------- | ------ | ------ | --------- | --- |
| two distinct | remote sensing image | sources, Sentinel-2 | and GF-2. The |        |                 |     |     |                |        |        |           |     |
mainmodel.Thedemonstratedeffectivenessoftherefinemoduleinthe
vectorizedagriculturalparcelboundariesinFig.9(c)and(d)revealed
realmofsalientobjectdetectionshowcaseditscapabilitytoefficiently
| that REAUNet | accurately delineates | large, well-organized | agricultural |        |                |     |        |           |       |         |          |          |
| ------------ | --------------------- | --------------------- | ------------ | ------ | -------------- | --- | ------ | --------- | ----- | ------- | -------- | -------- |
|              |                       |                       |              | reduce | classification |     | errors | at target | edges | through | residual | learning |
Table2
Accuracyassessmentintheablationexperiment.ED:theedgedetectionblock.DA:thedualattentionblock.RM:therefinemodule.DS:thedeepsupervision.
|     |     | NL  |     |     |     |     |     |     | HT  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Method
|     | OA  | F1 IoU | GOC GUC | GTC | OA  |     | F1  | IoU | GOC |     | GUC | GTC |
| --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REAUNet 0.9473 0.9498 0.8372 0.1363 0.2148 0.2017 0.9481 0.9454 0.9096 0.1123 0.2234 0.2074
REAUNetnoED 0.9411 0.9398 0.8216 0.1502 0.2347 0.2251 0.9399 0.9425 0.8985 0.1101 0.2770 0.2296
REAUNetnoDA 0.9302 0.8925 0.7948 0.1491 0.2605 0.2360 0.9393 0.9426 0.8984 0.1189 0.2867 0.2337
REAUNetnoRM 0.9402 0.9092 0.8190 0.1605 0.2487 0.2347 0.9386 0.9416 0.8966 0.1160 0.2742 0.2370
REAUNetnoDS 0.9289 0.8877 0.7875 0.1571 0.2858 0.2549 0.9304 0.9326 0.8807 0.1097 0.3181 0.2701
8

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.6. Delineationresultsintheablationexperiment.(a)and(b)representareaNL,while(c)and(d)representareaHT.
(Qinetal.,2019).Thecombinationofempiricalknowledgeandresidual targetregions.Inthemodeltransferabilityexperiment,theunsatisfac-
refinementfurtherenhancesthemodelabilityforedgedelineation,fa- toryresultsachievedbytheNTmodelsuggestedthatitwaschallenging
cilitatesmorepreciseidentificationforambiguouscropedges,thusdi- to obtain good performance when the trained model was applied
minishesmodelerrors. directlytoanunknownregion.Agriculturalparcelsinvariousregions
We also designed a post-processing workflow to optimize the ge- and during different seasons display significant variations in spatial
ometryshapeofparcels.Thepresenceofdifferentcropsinagricultural patternsandspectralfeaturesfromremotesensingimages,presenting
parcelscouldleadtoadjacentareasdisplayingdifferentcolorsinremote variationsintermsoftheshapeandsizeofagriculturalparcels.Inplains
sensing images. This variation poses a challenge for the model in orareaswithmechanizedfarmingoperations,agriculturalparcelstend
distinguishwhetheritisparcelboundaries,oftenresultinginerroneous tobelargeandregular.Incontrast,mountainousandhillyregionsoften
shortboundarylines.Theseerrorscontributetofalsenegativeswithin have smaller, more fragmented parcels. Additionally, the different
agriculturalparcelswhenfusingtheparcelextentandboundaryresults growthstagesofcropsacrossseasonsresultinvaryingspectralfeatures
(Fig.5c).Toaddressthisissue,weusedtheDouglas-Peuckeralgorithm inremotesensingimagesaswell.Forinstance,thegreennesswillshow
andtheover-sharpanglesdetectionandeliminationalgorithmtomiti- notabledifferencesbetweentheearlyandmaturestagesofcropgrowth
gatethesefalsenegatives.Throughthispost-processingapproach,our fromremotesensingimages.Additionally,differentcropspeciesacross
method produced agricultural parcels with a more coherent spatial thetwotimeperiodscanalsoleadtovariationsinboundarydelineation.
geometry. Thisdiscrepancyposesdifficultiesforthemodelwhenconfrontingun-
Inthisstudy,weoptedforconvolutionalneuralnetwork(CNN)as knowndata,whichrequirestheinputsofthenewsamplesrepresenta-
thedeeplearningmodelforagriculturalparceldelineation,achoicethat tive for the geography and the mapping seasons of the images to be
hasdemonstratedsignificantsuccessintherealmofimagesegmenta- classified. However, redrawing labels and reconstructing the training
tion.However,itisnoteworthythatTransformer-basedmethods,orig- model from the scratch could be costly. The model transferability
inally developed for natural language processing (NLP), are gaining experiment simulated three scenarios, i.e., direct model transfer,
popularityinimagesegmentationandhaveshownremarkableresultsin rebuildingfromthescratch,andamixtureofnon-localandlocalsam-
recentyears(Heetal.,2022;Liuetal.,2021b;Vaswanietal.,2017).The ples.TheresultshighlightedthepotentialofREAUNetbeingtransferred
primaryrationaleforselectingCNNistheextensiveuseoflinearlayers toa new regiononlywith asmall numberoflocal samples.This was
and self-attention mechanisms in Transformers, resulting in a larger becausethattheproposedREAUNetleveragedmulti-scaledeepsuper-
number of parameters and slower computation. Conversely, a crucial vision to segment agricultural parcels across various scales, yielding
characteristicofCNNisweightsharing,enablingittoefficientlyreduce commendable extraction results when dealt with parcels of different
the number of parameters when handling multidimensional matrices. sizesinnewregions.Moreover,weintegratedtraditionaledgedetectors
CNNexcelsinextractinglocalfeaturesfromimagesusingconvolutional into the model, enabling a feature extraction guided by the window
kernels,whereasTransformerpossessesthecapabilitytocapturelong- techniqueswhichwasgeneralizedfromnumerouspastcomputervision
rangedependencies. studies. The potential model transferability shown by REAUNet will
hold considerable implications for a large-scale agricultural parcel
mappinginfuture.
5.2. Modeltransferability
Inthepracticalapplicationofthedeeplearningmodel,itfrequently 5.3. Limitations
encountersscenariosinvolvingunknowndata,placinghighdemandson
thetransferabilityofthemodel.However,modelstrainedusingdata The process of extracting agriculturalparcels from remote sensing
from non-targeted regions often fail to exhibit a sound accuracy for imagesnecessitatesthefusionofparcelsegmentationresultswithparcel
9

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.7. Modelfeaturemapsintheencoderanddecoder.(a)ThepredictmoduleofREAUNet.(b)Extractedfeaturemapsfromshallowanddeeplayersintheencoder.
(c)Outputfeaturesofparcelextentandboundariesinthedecoder.
Table3
Accuracyassessmentofdifferentdeeplearningmodelsforparceldelineation.
NL HT
Method
OA F1 IoU GOC GUC GTC OA F1 IoU GOC GUC GTC
U-Net 0.9299 0.9230 0.8305 0.1763 0.2614 0.2557 0.9391 0.9460 0.8979 0.1569 0.2631 0.2566
RCF 0.9130 0.9012 0.7961 0.2005 0.2989 0.2922 0.9372 0.9441 0.8946 0.1912 0.2315 0.2580
MPSPNet 0.9316 0.9289 0.8401 0.1422 0.2176 0.2384 0.9472 0.9533 0.9012 0.1897 0.1908 0.2309
ResUNet-a 0.9304 0.9252 0.8340 0.1931 0.2431 0.2459 0.9411 0.9478 0.9011 0.1503 0.2541 0.2483
BsiNet 0.9253 0.9195 0.8246 0.1680 0.2580 0.2578 0.9318 0.9395 0.8863 0.1954 0.2540 0.2761
FRNet 0.9314 0.9264 0.8359 0.1537 0.2388 0.2446 0.9440 0.9512 0.9076 0.2545 0.3033 0.3239
RAUNet 0.9180 0.9122 0.8132 0.2209 0.2592 0.2754 0.9458 0.9526 0.9035 0.2088 0.2224 0.2586
SEANet 0.9332 0.9304 0.8425 0.1350 0.2277 0.2355 0.9388 0.9466 0.8988 0.1598 0.2228 0.2314
REAUNet 0.9473 0.9498 0.8372 0.1363 0.2148 0.2017 0.9481 0.9454 0.9096 0.1123 0.2234 0.2074
edgeresults.Wechosethesimplestcutoffmethodtomergetwomodel methodtomergetheparcelextentmaskandedgemaskcouldbethekey
results,becauseWaldnerandDiakogiannis(2020)foundthatitachieved tofurtherenhancethedelineationaccuracy.
similarresultstothewatershedapproach.Weobservedthatintheedge We extracted refined agricultural parcels from model predictions
mask, the agricultural parcel edges were represented with varying through a post-processing workflow. However, in some instances, the
probabilities,renderingthedifficultyinselectingasuitablethreshold. edgeprobabilitymapsoutputbythemodelexhibitedlowerprobabilities
Thereisatrade-offbetweenunder-segmentationandover-segmentation due to occlusion or blurring, resulting in a complication for the
errors wherein the choice of thresholds. How to use a better fusion thresholddeterminationontheedgebinarization.Thegeneratedlines
10

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Fig.8. DelineationresultsofREAUNetandotherdeeplearningmodelsinthecomparativeexperiment.(a)and(b)representareaNL,while(c)and(d)represent
areaHT.
Fig.9. Thegeneraldelineationresultsofagriculturalparcelsandvectorizedboundariesin(a)NLand(b)HT,andtheirsubregionswereshowninfrom(c)to(i):(c)
and(i)showsregularparcels,(d)depictsnarrowparcels,and(g)presentsparcelsofdifferentsizes,(e)and(f)showsmountainousregions.
mightendupbeingincompletewithbreakpoints.Ourcurrentapproach complete edges and mitigate the under-segmentation phenomenon in
optstodirectlyremoveshortandisolatedlines,whichmayadvertently thedelineationofagriculturalparcels.
eliminate some incomplete but correct edges. In future research, the Thebiasesindatalabelsmaycausethelossofmodelaccuracy.The
developmentofthebreakpointreconnectionmethodisessentialtoform open-sourcedatasetsmaycontaininconsistenciesinparcelboundaries
11

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Table4
Accuracyassessmentinthemodeltransferabilityexperiment.NT:notraining.DT:directtraining.TT:transfertraining.
| Studyarea | Method    |     | OA     | F1     | IoU    |     | GOC    | GUC    | GTC    |
| --------- | --------- | --- | ------ | ------ | ------ | --- | ------ | ------ | ------ |
| DK        | REAUNetNT |     | 0.7704 | 0.8113 | 0.6615 |     | 0.3925 | 0.4451 | 0.4565 |
|           | REAUNetDT |     | 0.8681 | 0.9028 | 0.7919 |     | 0.1571 | 0.2729 | 0.2599 |
|           | REAUNetTT |     | 0.8887 | 0.9195 | 0.8181 |     | 0.1424 | 0.2460 | 0.2343 |
| TR        | REAUNetNT |     | 0.7134 | 0.7794 | 0.6185 |     | 0.4961 | 0.6380 | 0.5679 |
|           | REAUNetDT |     | 0.8979 | 0.9248 | 0.8602 |     | 0.1403 | 0.1942 | 0.1891 |
|           | REAUNetTT |     | 0.9001 | 0.9270 | 0.8640 |     | 0.1318 | 0.1823 | 0.1781 |
Fig.10. Modelresultsinthemodeltransferabilityexperiment.(a)representsareaDKand(b)representsareaTR.
duetotemporaldiscrepancies,leadingtoinaccuraciesindefiningthe andshapeofextractedparcels,weformulatedapost-processingwork-
exactshapeandsizeofagriculturalparcels.Additionally,theremaybe flowutilizingtheDouglas-Peuckeralgorithmandanover-sharpangle
variability in whether parcel ridges are marked, introducing further detectionandeliminationalgorithm.Comparativeexperimentsrevealed
inconsistencies.Thesedeviationscanaffectthetrainingprocess,making that our proposed model surpassed representative agricultural parcel
it challenging for the model to find the correct fitting direction and extraction CNN models in both thematic and geometric accuracy.
thereby reducing accuracy. To mitigate the influence of data errors, Finally,tofacilitatethesuccessfuldelineationofagriculturalparcelsin
futureeffortscanimplementcollaborativelabelingprocessesinvolving unknownregionsusingtheproposeddeeplearningmodel,wetestedand
multiple individuals tominimize accidentalhuman errors. Employing confirmedthecapabilityofthenewmodelfortransferringpre-modelsto
consensus-based labels can enhance the reliability of identified agri- anewregionwithasmallproportionoflocalsamples.Thisopenedup
culturalparcels.Moreover,integratingsupplementarydatasourcesfor thepossibilityofmappingthedistributionofagriculturalparcelsona
cross-validationpurposesmaybolstertheaccuracyandrobustnessofthe large scale. In conclusion, our proposed algorithm successfully delin-
delineatedagriculturalparcels. eatedtheagriculturalparcelsfromremotesensingimages.Enhancing
We evaluated the model performance in new regions through a theedge-awarenessofthemodelsignificantlyimproveditsaccuracyin
transfer experiment and observed that even a small number of local delineating agricultural parcels, particularly on the parcel edges. The
samples could markedly boost model accuracy. Given the labor- method also demonstrated good generalization results in different re-
intensivesamplelabeling,thereisalwaysanexpectationtoachievea gions with limited local samples, offering a new approach for the
high extraction accuracy with only minimal local samples. However, automaticmappingofagriculturalparcelsatalargespatialscale.
| when deploying | the model | to a new | area, determining | the optimal |     |     |     |     |     |
| -------------- | --------- | -------- | ----------------- | ----------- | --- | --- | --- | --- | --- |
number of local samples for transfer training remains a significant CRediTauthorshipcontributionstatement
challenge,whichcouldbealimitationforourstudy.Ourfutureresearch
will focus on exploring the optimal number of samples for transfer RuiLu:Writing–review&editing,Writing–originaldraft,Visu-
learningtoaddressthisgapandenhancetherobustnessandgeneraliz- alization, Project administration, Methodology, Investigation, Formal
ability of our model. Strategically selecting local samples will signifi- analysis,Datacuration,Conceptualization.YingfanZhang:Writing–
cantlyfacilitatelarge-scalemappingandreducethetimeandresources review&editing,Methodology,Investigation.QitingHuang:Supervi-
requiredforsamplepreparationandmodeltraining. sion,Datacuration.PenghaoZeng:Writing–review&editing.Zhou
– &
|     |     |     |     |     | Shi: Writing | review | editing, | Supervision, Resources, | Funding |
| --- | --- | --- | --- | --- | ------------ | ------ | -------- | ----------------------- | ------- |
6. Conclusion acquisition,Conceptualization.SuYe:Writing–review&editing,Su-
pervision,Conceptualization.
| This study | developed a | novel deep | learning model, | REAUNet, to |     |     |     |     |     |
| ---------- | ----------- | ---------- | --------------- | ----------- | --- | --- | --- | --- | --- |
delineateagriculturalparcelsfromhigh-resolutionremotesensingim-
ages. Four model innovations were ensembled to improve edge- Declarationofcompetinginterest
| awareness, including | the deep | supervision, | the edge | detection block, |     |     |     |     |     |
| -------------------- | -------- | ------------ | -------- | ---------------- | --- | --- | --- | --- | --- |
the dual attention block and the refine module. Sentinel-2 and GF-2 The authors declare that they have noknown competing financial
imagery at different resolutions across four regions were utilized to interestsorpersonalrelationshipsthatcouldhaveappearedtoinfluence
assesstheeffectivenessofparceldelineation.Tooptimizethegeometry theworkreportedinthispaper.
12

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
ˇ
Dataavailability Chetri,T.,Malek,Z.,Bungnamei,K.,Saikia,A.,Sahariah,D.,Narzary,W.,
Danylo,O.,Sturn,T.,Karner,M.,McCallum,I.,Schepaschenko,D.,Moltchanova,E.,
Fraisl,D.,Moorthy,I.,Fritz,S.,2019.Estimatingtheglobaldistributionoffieldsize
Theauthorsdonothavepermissiontosharedata. usingcrowdsourcing.Glob.ChangeBiol.25,174–186.https://doi.org/10.1111/
gcb.14492.
Acknowledgements Li,M.,Long,J.,Stein,A.,Wang,X.,2023.Usingasemanticedge-awaremulti-taskneural
networktodelineateagriculturalparcelsfromremotesensingimages.ISPRSJ.
Photogramm.RemoteSens.200,24–40.https://doi.org/10.1016/j.
Theauthorsareverygratefulforthefinancialsupportprovidedby isprsjprs.2023.04.019.
NationalKeyResearchandDevelopmentProgram(2022YFB3903503), Liu,Y.,Cheng,M.M.,Hu,X.,Wang,K.,Bai,X.,2017.Richerconvolutionalfeaturesfor
edgedetection.In:ProceedingsoftheIEEEconferenceoncomputervisionand
and by the Fundamental Research Funds for the Central Universities patternrecognition,pp.3000–3009.
(226-202400052).Theauthorswouldalsoliketothanktheeditorsand Liu,H.,Luo,J.,Sun,Y.,Xia,L.,Wu,W.,Yang,H.,Hu,X.,Gao,L.,2019.Contour-oriented
anonymous reviewers of the journal for their thorough review and croplandextractionfromhighresolutionremotesensingimageryusingricher
convolutionfeaturesnetwork.In:20198thInternationalConferenceonAgro-
insightful comments that have helped improving the quality of the
Geoinformatics(Agro-Geoinformatics).IEEE,pp.1–6.https://doi.org/10.1109/
paper. Agro-Geoinformatics.2019.8820430.
Liu,Z.,Lin,Y.,Cao,Y.,Hu,H.,Wei,Y.,Zhang,Z.,Lin,S.,Guo,B.,2021.Swin
transformer:Hierarchicalvisiontransformerusingshiftedwindows.In:Proceedings
References
oftheIEEE/CVFinternationalconferenceoncomputervision,pp.10012–10022.
Liu,Y.,Ma,X.,Shu,L.,Hancke,G.P.,Abu-Mahfouz,A.M.,2021a.Fromindustry4.0to
Cai,Y.,Guan,K.,Peng,J.,Wang,S.,Seifert,C.,Wardlow,B.,Li,Z.,2018.Ahigh- agriculture4.0:currentstatus,enablingtechnologies,andresearchchallenges.IEEE
performanceandin-seasonclassificationsystemoffield-levelcroptypesusingtime- Trans.Ind.Inform.17,4322–4334.https://doi.org/10.1109/TII.2020.3003910.
seriesLandsatdataandamachinelearningapproach.RemoteSens.Environ.210, Lobell,D.B.,Thau,D.,Seifert,C.,Engle,E.,Little,B.,2015.Ascalablesatellite-based
35–47.https://doi.org/10.1016/j.rse.2018.02.045. cropyieldmapper.RemoteSens.Environ.164,324–333.https://doi.org/10.1016/j.
Cai,Z.,Hu,Q.,Zhang,X.,Yang,J.,Wei,H.,Wang,J.,Zeng,Y.,Yin,G.,Li,W.,You,L., rse.2015.04.021.
Xu,B.,Shi,Z.,2023a.Improvingagriculturalfieldparceldelineationwithadual Long,J.,Li,M.,Wang,X.,Stein,A.,2022.Delineationofagriculturalfieldsusingmulti-
branchspatiotemporalfusionnetworkbyintegratingmultimodalsatellitedata. taskBsiNetfromhigh-resolutionsatelliteimages.Int.J.Appl.EarthObs.Geoinform.
ISPRSJ.Photogramm.RemoteSens.205,34–49.https://doi.org/10.1016/j. 112,102871https://doi.org/10.1016/j.jag.2022.102871.
isprsjprs.2023.09.021. Lu,Y.,Jenkins,A.,Ferrier,R.C.,Bailey,M.,Gordon,I.J.,Song,S.,Huang,J.,Jia,S.,
Cai,Z.,Wei,H.,Hu,Q.,Zhou,W.,Zhang,X.,Jin,W.,Wang,L.,Yu,S.,Wang,Z.,Xu,B., Zhang,F.,Liu,X.,Feng,Z.,Zhang,Z.,2015.AddressingChina’sgrandchallengeof
Shi,Z.,2023b.Learningspectral-spatialrepresentationsfromVHRimagesforfine- achievingfoodsecuritywhileensuringenvironmentalsustainability.Sci.Adv.1,
scalecroptypemapping:Acasestudyofrice-crayfishfieldextractioninSouth e1400039.https://doi.org/10.1126/sciadv.1400039.
China.ISPRSJ.Photogramm.RemoteSens.199,28–39.https://doi.org/10.1016/j. Pan,Y.,Wang,X.,Zhang,L.,Zhong,Y.,2023.E2EVAP:End-to-endvectorizationof
isprsjprs.2023.03.019. smallholderagriculturalparcelboundariesfromhigh-resolutionremotesensing
Crommelinck,S.,Bennett,R.,Gerke,M.,Yang,M.Y.,Vosselman,G.,2017.Contour imagery.ISPRSJ.Photogramm.RemoteSens.203,246–264.https://doi.org/
DetectionforUAV-BasedCadastralMapping.RemoteSens.9,171.https://doi.org/ 10.1016/j.isprsjprs.2023.08.001.
10.3390/rs9020171. Persello,C.,Tolpekin,V.A.,Bergado,J.R.,deBy,R.A.,2019.Delineationofagricultural
Diakogiannis,F.I.,Waldner,F.,Caccetta,P.,Wu,C.,2020.ResUNet-a:Adeeplearning fieldsinsmallholderfarmsfromsatelliteimagesusingfullyconvolutionalnetworks
frameworkforsemanticsegmentationofremotelysenseddata.ISPRSJ. andcombinatorialgrouping.RemoteSens.Environ.231,111253https://doi.org/
Photogramm.RemoteSens.162,94–114.https://doi.org/10.1016/j. 10.1016/j.rse.2019.111253.
isprsjprs.2020.01.013. Potapov,P.,Turubanova,S.,Hansen,M.C.,Tyukavina,A.,Zalles,V.,Khan,A.,Song,X.-
Estes,L.D.,Ye,S.,Song,L.,Luo,B.,Eastman,J.R.,Meng,Z.,Zhang,Q.,McRitchie,D., P.,Pickens,A.,Shen,Q.,Cortez,J.,2022.Globalmapsofcroplandextentandchange
Debats,S.R.,Muhando,J.,Amukoa,A.H.,Kaloo,B.W.,Makuru,J.,Mbatia,B.K., showacceleratedcroplandexpansioninthetwenty-firstcentury.Nat.Food3,19–28.
Muasa,I.M.,Mucha,J.,Mugami,A.M.,Mugami,J.M.,Muinde,F.W.,Mwawaza,F. https://doi.org/10.1038/s43016-021-00429-z.
M.,Ochieng,J.,Oduol,C.J.,Oduor,P.,Wanjiku,T.,Wanyoike,J.G.,Avery,R.B., Pywell,R.F.,Heard,M.S.,Woodcock,B.A.,Hinsley,S.,Ridding,L.,Nowakowski,M.,
Caylor,K.K.,2022.Highresolution,annualmapsoffieldboundariesforsmallholder- Bullock,J.M.,2015.Wildlife-friendlyfarmingincreasescropyield:evidencefor
dominatedcroplandsatnationalscales.Front.Artif.Intell.4. ecologicalintensification.Proc.R.Soc.BBiol.Sci.282,20151740.https://doi.org/
Garibaldi,L.A.,Carvalheiro,L.G.,Vaissi`ere,B.E.,Gemmill-Herren,B.,Hipo´lito,J.,
10.1098/rspb.2015.1740.
Freitas,B.M.,Ngo,H.T.,Azzu,N.,S´aez,A.,Åstro¨m,J.,An,J.,Blochtein,B.,
Qin,X.,Zhang,Z.,Huang,C.,Gao,C.,Dehghan,M.,Jagersand,M.,2019.BASNet:
Buchori,D.,García,F.J.C.,OliveiradaSilva,F.,Devkota,K.,Ribeiro,M.deF., boundary-awaresalientobjectdetection.In:PresentedattheProceedingsofthe
Freitas,L.,Gaglianone,M.C.,Goss,M.,Irshad,M.,Kasina,M.,Filho,A.J.S.P.,Kiill,L. IEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.7479–7489.
H.P.,Kwapong,P.,Parra,G.N.,Pires,C.,Pires,V.,Rawal,R.S.,Rizali,A.,Saraiva,A. Ranjan,R.,Avasthi,V.,2023.Edgedetectionusingguidedsobelimagefiltering.Wirel.
M.,Veldtman,R.,Viana,B.F.,Witter,S.,Zhang,H.,2016.Mutuallybeneficial Pers.Commun.132,651–677.https://doi.org/10.1007/s11277-023-10628-5.
pollinatordiversityandcropyieldoutcomesinsmallandlargefarms.Science351, Ronneberger,O.,Fischer,P.,Brox,T.,2015.U-Net:Convolutionalnetworksfor
388–391.https://doi.org/10.1126/science.aac7287. biomedicalimagesegmentation.In:Navab,N.,Hornegger,J.,Wells,W.M.,
Godfray,H.C.J.,Beddington,J.R.,Crute,I.R.,Haddad,L.,Lawrence,D.,Muir,J.F., Frangi,A.F.(Eds.),MedicalImageComputingandComputer-AssistedIntervention–
Pretty,J.,Robinson,S.,Thomas,S.M.,Toulmin,C.,2010.Foodsecurity:the MICCAI2015,LectureNotesinComputerScience.SpringerInternationalPublishing,
challengeoffeeding9billionpeople.Science327,812–818.https://doi.org/ Cham,pp.234–241.https://doi.org/10.1007/978-3-319-24574-4_28.
10.1126/science.1185383. Roy,A.G.,Navab,N.,Wachinger,C.,2018.ConcurrentSpatialandChannel‘Squeeze&
Graesser,J.,Ramankutty,N.,2017.DetectionofcroplandfieldparcelsfromLandsat Excitation’inFullyConvolutionalNetworks.In:Frangi,A.F.,Schnabel,J.A.,
imagery.RemoteSens.Environ.201,165–180.https://doi.org/10.1016/j. Davatzikos,C.,Alberola-Lo´pez,C.,Fichtinger,G.(Eds.),MedicalImageComputing
rse.2017.08.027. andComputerAssistedIntervention–MICCAI2018,LectureNotesinComputer
He,K.,Zhang,X.,Ren,S.,Sun,J.,2016.Deepresiduallearningforimagerecognition.In: Science.SpringerInternationalPublishing,Cham,pp.421–429.https://doi.org/
ProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition, 10.1007/978-3-030-00928-1_48.
pp.770–778. Smith,L.N.,2017.Cyclicallearningratesfortrainingneuralnetworks.In:2017IEEE
He,X.,Zhou,Y.,Zhao,J.,Zhang,D.,Yao,R.,Xue,Y.,2022.Swintransformerembedding winterconferenceonapplicationsofcomputervision(WACV),pp.464–472.https://
UNetforremotesensingimagesemanticsegmentation.IEEETrans.Geosci.Remote doi.org/10.48550/arXiv.1506.01186.
Sens.60,1–15.https://doi.org/10.1109/TGRS.2022.3144165. Sun,Y.,Li,Z.-L.,Luo,J.,Wu,T.,Liu,N.,2022.Farmlandparcel-basedcropclassification
Hong,R.,Park,J.,Jang,S.,Shin,H.,Kim,H.,Song,I.,2021.Developmentofaparcel- incloudy/rainymountainsusingSentinel-1andSentinel-2baseddeeplearning.Int.
levellandboundaryextractionalgorithmforaerialimageryofregularlyarranged J.RemoteSens.
agriculturalareas.RemoteSens.13,1167.https://doi.org/10.3390/rs13061167. Taravat,A.,Wagner,M.P.,Bonifacio,R.,Petit,D.,2021.Advancedfullyconvolutional
Huang,Y.,Ye,S.,Xue,J.,Shi,Z.,Wang,F.,2024.Mappingcroppingintensityby networksforagriculturalfieldboundarydetection.RemoteSens.13,722.https://
identifyingbaresoiloccurrencefromSentinel-2timeseries.Comput.Electron.Agric. doi.org/10.3390/rs13040722.
222,109025https://doi.org/10.1016/j.compag.2024.109025. Turker,M.,Kok,E.H.,2013.Field-basedsub-boundaryextractionfromremotesensing
Kuang,W.,Liu,J.,Tian,H.,Shi,H.,Dong,J.,Song,C.,Li,X.,Du,G.,Hou,Y.,Lu,D., imageryusingperceptualgrouping.ISPRSJ.Photogramm.RemoteSens.79,
Chi,W.,Pan,T.,Zhang,S.,Hamdi,R.,Yin,Z.,Yan,H.,Yan,C.,Wu,S.,Li,R., 106–121.https://doi.org/10.1016/j.isprsjprs.2013.02.009.
Yang,J.,Dou,Y.,Wu,W.,Liang,L.,Xiang,B.,Yang,S.,2022.Cropland Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,Ł.,
redistributiontomarginallandsunderminesenvironmentalsustainability.nwab091 Polosukhin,I.,2017.Attentionisallyouneed.In:AdvancesinNeuralInformation
Natl.Sci.Rev.9.https://doi.org/10.1093/nsr/nwab091. ProcessingSystems.CurranAssociates,Inc.
Kumar,S.,Jayagopal,P.,2021.Delineationoffieldboundaryfrommultispectralsatellite Waldner,F.,Diakogiannis,F.I.,2020.Deeplearningonedge:Extractingfieldboundaries
imagesthroughU-Netsegmentationandtemplatematching.Ecol.Inform.64, fromsatelliteimageswithaconvolutionalneuralnetwork.RemoteSens.Environ.
101370https://doi.org/10.1016/j.ecoinf.2021.101370. 245,111741https://doi.org/10.1016/j.rse.2020.111741.
Lesiv,M.,LasoBayas,J.C.,See,L.,Duerauer,M.,Dahlia,D.,Durando,N.,Hazarika,R., Wang,S.,Zhou,Y.,Yang,X.,Li,F.,Wu,T.,Luo,J.,2023.BSNet:Boundary-semantic-
KumarSahariah,P.,Vakolyuk,M.,Blyshchyk,V.,Bilous,A.,Perez-Hoyos,A., fusionnetworkforfarmlandparcelmappinginhigh-resolutionsatelliteimages.
Gengler,S.,Prestele,R.,Bilous,S.,Akhtar,I.ulH.,Singha,K.,Choudhury,S.B.,
13

R.Luetal. International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084
Comput.Electron.Agric.206,107683https://doi.org/10.1016/j. Yuan,X.,Shi,J.,Gu,L.,2021.Areviewofdeeplearningmethodsforsemantic
compag.2023.107683. segmentationofremotesensingimagery.ExpertSyst.Appl.169,114417https://doi.
Woo,S.,Park,J.,Lee,J.-Y.,Kweon,I.S.,2018.CBAM:ConvolutionalBlockAttention org/10.1016/j.eswa.2020.114417.
Module.In:PresentedattheProceedingsoftheEuropeanConferenceonComputer Zabel,F.,Delzeit,R.,Schneider,J.M.,Seppelt,R.,Mauser,W.,V´aclavík,T.,2019.Global
Vision(ECCV),pp.3–19. impactsoffuturecroplandexpansionandintensificationonagriculturalmarketsand
Xia,L.,Zhao,F.,Chen,J.,Yu,L.,Lu,M.,Yu,Q.,Liang,S.,Fan,L.,Sun,X.,Wu,S., biodiversity.Nat.Commun.10,2844.https://doi.org/10.1038/s41467-019-10775-
Wu,W.,Yang,P.,2022.Afullresolutiondeeplearningnetworkforpaddyrice z.
mappingusingLandsatdata.ISPRSJ.Photogramm.RemoteSens.194,91–107. Zhang,H.,Liu,M.,Wang,Y.,Shang,J.,Liu,X.,Li,B.,Song,A.,Li,Q.,2021.Automated
https://doi.org/10.1016/j.isprsjprs.2022.10.005. delineationofagriculturalfieldboundariesfromSentinel-2imagesusingrecurrent
Xie,S.,Tu,Z.,2015.Holistically-nestededgedetection.In:PresentedattheProceedings residualU-Net.Int.J.Appl.EarthObs.Geoinformation105,102557.https://doi.
oftheIEEEInternationalConferenceonComputerVision,pp.1395–1403. org/10.1016/j.jag.2021.102557.
Yan,L.,Roy,D.P.,2014.Automatedcropfieldextractionfrommulti-temporalWeb Zhang,D.,Pan,Y.,Zhang,J.,Hu,T.,Zhao,J.,Li,N.,Chen,Q.,2020.Ageneralized
EnabledLandsatData.RemoteSens.Environ.144,42–64.https://doi.org/10.1016/ approachbasedonconvolutionalneuralnetworksforlargeareacroplandmapping
j.rse.2014.01.006. atveryhighresolution.RemoteSens.Environ.247,111912https://doi.org/
Ye,S.,Pontius,R.G.,Rakshit,R.,2018.Areviewofaccuracyassessmentforobject-based 10.1016/j.rse.2020.111912.
imageanalysis:Fromper-pixeltoper-polygonapproaches.ISPRSJ.Photogramm. Zhao,H.,Shi,J.,Qi,X.,Wang,X.,Jia,J.,2017.PyramidSceneParsingNetwork.In:
RemoteSens.141,137–147.https://doi.org/10.1016/j.isprsjprs.2018.04.002. PresentedattheProceedingsoftheIEEEConferenceonComputerVisionandPattern
Ye,S.,Rogan,J.,Zhu,Z.,Eastman,J.R.,2021.Anear-real-timeapproachformonitoring Recognition,pp.2881–2890.
forestdisturbanceusingLandsattimeseries:stochasticcontinuouschangedetection.
RemoteSens.Environ.252,112167https://doi.org/10.1016/j.rse.2020.112167.
14