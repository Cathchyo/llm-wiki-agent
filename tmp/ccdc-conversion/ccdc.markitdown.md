RemoteSensingofEnvironment144(2014)152–171
ContentslistsavailableatScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Continuous change detection and classification of land cover using all
available Landsat data
⁎
ZheZhu ,CurtisE.Woodcock
CenterforRemoteSensing,DepartmentofEarthandEnvironment,BostonUniversity,675CommonwealthAvenue,Boston,MA02215,USA
a r t i c l e i n f o a b s t r a c t
Articlehistory: AnewalgorithmforContinuousChangeDetectionandClassification(CCDC)oflandcoverusingallavailable
Received25February2013 Landsatdataisdeveloped.Itiscapableofdetectingmanykindsoflandcoverchangecontinuouslyasnewimages
Receivedinrevisedform17January2014 arecollectedandprovidinglandcovermapsforanygiventime.Atwo-stepcloud,cloudshadow,andsnow
Accepted18January2014 maskingalgorithmisusedforeliminating“noisy”observations.Atimeseriesmodelthathascomponentsof
Availableonline11February2014 seasonality,trend,andbreakestimatessurfacereflectanceandbrightnesstemperature.Thetimeseriesmodel
isupdateddynamicallywithnewlyacquiredobservations.Duetothedifferencesinspectralresponseforvarious
Keywords:
kindsoflandcoverchange,theCCDCalgorithmusesathresholdderivedfromallsevenLandsatbands.Whenthe
CCDC
Classification differencebetweenobservedandpredictedimagesexceedsathresholdthreeconsecutivetimes,apixelisiden-
Changedetection tifiedaslandsurfacechange.Landcoverclassificationisdoneafterchangedetection.Coefficientsfromthetime
Timeseries seriesmodelsandtheRootMeanSquareError(RMSE)frommodelestimationareusedasinputtotheRandom
Landcover ForestClassifier(RFC).WeappliedtheCCDCalgorithmtooneLandsatsceneinNewEngland(WRSPath12and
Continuous Row31).Allavailable(atotalof519)Landsatimagesacquiredbetween1982and2011wereused.Arandom
Landsat stratifiedsampledesignwasusedforassessingthechangedetectionaccuracy,with250pixelsselectedwithin
RandomForest areasofpersistentlandcoverand250pixelsselectedwithinareasofchangeidentifiedbytheCCDCalgorithm.
TheaccuracyassessmentshowsthatCCDCresultswereaccuratefordetectinglandsurfacechange,with
producer'saccuracyof98%anduser'saccuraciesof86%inthespatialdomainandtemporalaccuracyof80%.
Landcoverreferencedatawereusedasthebasisforassessingtheaccuracyofthelandcoverclassification.The
landcovermapwith16categoriesresultingfromtheCCDCalgorithmhadanoverallaccuracyof90%.
©2014ElsevierInc.Allrightsreserved.
1.Introduction 1.1.Monitoringlandcoverchangewithremotesensing
Mappingandmonitoringlandcoverhavebeenwidelyrecognizedas ImagesfromtheLandsatseriesofsatellitesareoneofthemostim-
animportantscientificgoal(Anderson,1976;Foody,2002;Friedletal., portantsourcesofdataforstudyingdifferentkindsoflandcoverchange,
2002;Hansen,Defries,Townshend,&Sohlberg,2000;Homer,Huang, suchasdeforestation,agricultureexpansionandintensification,urban
Yang,Wylie,&Coan,2004;Lovelandetal.,2000;Wulderetal.,2008). growth,andwetlandloss(Coppin&Bauer,1996;Galfordetal.,2008;
Landcoverinfluencestheenergybalance,carbonbudget,andhydrolog- Jensen,Rutchey,Koch,&Narumalani,1995;Setoetal.,2002;Woodcock,
icalcycleasmanydifferentphysicalcharacteristicschangeasafunction Macomber,Pax-Lenney,&Cohen,2001),duetotheirlongrecordofcon-
oflandcover,suchasalbedo,emissivity,roughness,photosynthetic tinuousmeasurement,spatialresolution,andnearnadirobservations
capacity,andtranspiration.Landcoverchangecanbenaturaloranthro- (Pflugmacher,Cohen,&Kennedy,2012;Woodcock&Strahler,1987;
pogenic,butwithhumanactivityincreasing,theEarthsurfacehasbeen Wulderetal.,2008).OneofthedrawbacksofLandsatdataistherela-
modifiedsignificantlyinrecentyearsbyvariouskindsoflandcover tivelylowtemporalfrequency.ForeachLandsatsensor,overpassesof
change.Knowledgeoflandcoverandlandcoverchangeisnecessary the same location occur every 16days, and data at this temporal
formodelingtheclimateandbiogeochemistryoftheEarthsystemand frequencyareonlycommonwithintheUnitedStateswherethesensors
formanykindsofmanagementpurposes.Satelliteimageshavelong areturnedonforeveryoverpass.Forotherpartsoftheworld,thefre-
beenusedtoassesstheEarthsurfacebecauseofrepeatedsynoptic quencyofdatacollectionisgenerallyless,dependingonmanyfactors
collectionofconsistentmeasurements(Lambin&Strahler,1994). suchascloudcoverpredictionsandavailabilityofinternationalground
stations(Arvidson,Goward,Gasch,&Williams,2006).Evenforimages
thatarecollected,cloudsreducetheamountofusabledata(Zhang,
Rossow,Lacis,Oinas,&Mishchenko,2004).Therefore,mostchange
⁎ Correspondingauthor.Tel.:+16172336031. detectionalgorithmsusingLandsathaveusedtwodatesofLandsatim-
E-mailaddress:zhuzhe@bu.edu(Z.Zhu). ages(Collins&Woodcock,1996;Coppin,Jonckheere,Nackaerts,Muys,
0034-4257/$–seefrontmatter©2014ElsevierInc.Allrightsreserved.
http://dx.doi.org/10.1016/j.rse.2014.01.011

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 153
&Lambin,2004;Healey,Cohen,Yang,&Krankina,2005;Maseketal., nolandcoverchangeinthetimeintervalbetweenthedifferentimages.
2008;Singh,1989).Thoughthesekindsofalgorithmsarerelativelysim- Thisassumptionisnotalwaysvalid,especiallywhenimagesfromlong
pletoimplement,theyarenotalwaysapplicable.Itmaytakeafew time intervals are used, or for areas that are changing frequently
yearstofindanidealpairofLandsatimagesthatarefreeofclouds, (Rogan,Franklin,&Roberts,2002).Moreover,thelandcovermapspro-
cloudshadows,andsnow(hereafterreferredtoas“clear”)andacquired ducedfromconventionalmethodscannotbeuseddirectlyforidentify-
atthesametimeofyear. inglandcoverchangebecausefrequentlythemagnitudeoftheerrorin
To find change over shorter time intervals, several new change classificationismuchlargerthantheamountoflandcoverchange
detectionalgorithmsusingmanydatesofLandsatimages(typically (Friedletal.,2010;Fuller,Smith,&Devereux,2003).Ifwecompare
oneimageperyear)areappearingintheliterature(Goodwinetal., landcovermapsproducedatdifferenttimesfordetectingchange,the
2008; Hostert, Röder, & Hill, 2003; Huang et al., 2010; Kennedy, errorsfromtheclassificationprocesswillshowupaschangeandthis
Cohen,&Schroeder,2007;Vogelmann,Tolk,&Zhu,2009).However, causes serious problems for places where the sizes of changes are
thesenewlydevelopedalgorithmsstillhavelimitationsrelatedtoselec- small.Therefore,theremotesensingcommunityneedsaclassification
tionofidealLandsatimages.Forexample,tominimizetheinfluencesof algorithmthat:(1)increasesthetimeperiodoverwhichlandcover
phenologyandsunangledifferences,theidealimagesshouldfallwithin mapsremain“current”;(2)worksforareaswheremultiplekindsof
thesameseason.Moreover,thoughtheycanuseimagesthatarepartly landcoverchangeiscommon,and(3)makeslandcovermapscompa-
coveredbyclouds,theystillneedmostoftheimagestobecloud-free.To rablebetweentimesforidentificationofchange.
satisfyalltheserequirements,thebestthesealgorithmscantypically
provide is annual or biennial change results (Huang et al., 2010; 1.3.IntroductiontotheCCDCalgorithm
Kennedyetal.,2007).
Recently,ModerateResolutionImagingSpectroradiometer(MODIS) TheopeningoftheLandsatarchivein2008(Woodcocketal.,2008)
timeseriesdatahavebeenexploredformonitoringvariouskindsof hasledtobigchangesinthewayLandsatimagesarebeingused.Previ-
landcoverchange(Eklundh,Johansson,&Solberg,2009;Galfordetal., ously,asingleLandsatimagewouldcosthundredsofU.S.dollars.To
2008; Jin & Sader, 2005; Lunetta, Knight, Ediriwickrema, Lyon, & minimizecosts,mostresearcherstypicallychosetouseonly afew
Worthy,2006;Roy,Jin,Lewis,&Justice,2005;Verbesselt,Hyndman, cloud-free Landsat images acquired during the growing season for
Newnham,&Culvenor,2010;Xin,Olofsson,Zhu,Tan,&Woodcock, analysis.FollowingfreeaccesstotheLandsatarchive,studiesusing
2012),becauseofitshighertemporalfrequency.Thecoarsespatial lots of Landsat images are appearing (Brooks, Thomas, Wynne, &
resolution of the MODIS data limits its ability for detecting small Coulston, 2012; Goodwin et al., 2008; Hansen et al., 2013; Huang
changes(Jin&Sader,2005),whichiscommonforanthropogenicchang- et al., 2010; Kennedy, Yang, & Cohen, 2010; Melaas, Friedl, & Zhu,
es.Also,issuesofBidirectionalReflectanceDistributionFunction(BRDF) 2013;Vogelmannetal.,2009;Zhu,Woodcock,&Olofsson,2012).In
effects(Schaafetal.,2002),largedifferencesintheprojectedInstanta- this paper, we seek to improve monitoring of land cover and land
neousFieldofView(IFOV)(Xinetal.,2012),andgriddingartifacts coverchangeforaregionincoastalNewEnglandbydevelopingan
(Tanetal.,2006)makecomparisonofmultitemporalMODISimagesdif- approach that uses all available Landsat data. We use all available
ficult.Tomonitorchangesastheyareoccurringandtobeabletoiden- LandsatdatabecausetherearemanyclearobservationsinLandsatim-
tifychangessmallinsize,theremotesensingcommunityneedsan agesthathaveahighpercentageofclouds.Fig.1isacumulativehisto-
algorithmthatusesfinespatialresolutiondatasuchasLandsatand gramofthepercentageofclearobservationsinLandsatimagesasit
usesasmanyobservationsaspossibletodetectlandcoverchangeaccu- relatestocloudcover.Thecloudcoverestimatesarederivedfroma
ratelyandquickly. newlydevelopedFmaskalgorithm(Zhu&Woodcock,2012)forPath
12Row31between1982and2011.Basedonthisinformation,ifwe
1.2.Landcoverclassification onlyuseLandsatimageswithcloudcoverlessthan10%,ashasbeen
commoninthepast,wewouldomitmorethan50%ofthetotalclear
Landcoverclassificationisoneofthemoststudiedtopicsinremote observations.EvenLandsatimageswithmorethan40%cloudcovercon-
sensing,andlandcovermapsprovidethebasisformanyapplications tainalmost20%ofthetotalclearobservations.Theuseofallavailable
likemodelingofcarbonbudgets,managementofforests,andestimation Landsatdatahasopenedadoorformanystudiesthatcouldnotbeimag-
ofcropyield(Jung,Henkel,Herold,&Churkina,2006;Lark&Stafford, inedbefore,suchasthestudyofphenologyatLandsatscales(Melaas
1997;Roganetal.,2010;Wolter,Mladenoft,&Crow,1995).Whileitis etal.,2013)ordetectionofforestdisturbancecontinuouslyathigh
relativelyeasytogeneratealandcovermapfromremotelysensed
data,itisnoteasytomakeitaccurate.Usingmultitemporalimagesas
inputs is reported to help improve classification accuracy (Carrao,
Goncalves,&Caetano,2008;Guerschman,Paruelo,Bella,Giallorenzi,&
Pacin,2003;Wolteretal.,1995;Zhu,Woodcock,Rogan,&Kellndorfer,
2012),especiallyforvegetation,becauseoftheuniquephenological
characteristicsofdifferentvegetationtypes.Toachievehigherclassifica-
tionaccuracy,mostcurrentlandcoverproductsaregeneratedusing
multitemporal images as their inputs (Friedl et al., 2010; Gopal,
Woodcock,&Strahler,1999;Hansenetal.,2000;Homeretal.,2004;
Lovelandetal.,2000;Tucker,Townshend,&Goff,1985).
Theuseofmultitemporalimagesalsocancauseproblemsforcon-
ventional automated classification algorithms. First, they need all
dates of images to be free of clouds to classify every pixel in the
image,whichisoftennotpossible,especiallyforsensorswithrelatively
lowtemporalfrequencylikeLandsat.Forsomecloudylocations,itmay
benecessarytowaitafewyearstogetmultipleLandsatimagesinthe
sameyearwithoutcloudsandsnow.Therefore,mostLandsat-based
land cover maps are produced at the interval of five or ten years,
whichgreatlyreducestheir“currency”.Second,whenmakingland
Fig.1.Percentoftotalclearobservationsvs.cloudcoverpercentintervalbasedonallavail-
covermapswithmultitemporalimages,wetypicallyassumethereis ableLandsatTM/ETM+imagesfrom1982to2011forPath12Row31(NewEngland).

154 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
spatialresolution andhightemporalfrequency(Zhu,Woodcock,& agriculturalfields,andforestclearing;and(3)itisraretofindacloud-
Olofsson,2012). freeLandsatimageinthisstudyarea,makingitanoutstandingplaceto
UsingallavailableTM/ETM+observationsfromLandsat4,5,and7, testtherobustnessofthisnewalgorithm.
wedevelopedanewContinuousChangeDetectionandClassification
(CCDC)algorithmthathelpsminimizetheissuesthatunderminethe
2.2.Landsatdata
moreconventionalchangedetectionandclassificationmethodsmen-
tionedabove.Theuseoftheterm“continuous”herereferstothecapa-
AllavailableLevel1Terrain(corrected)(L1T)LandsatTM/ETM+
bilitytodetectchangedetectioneverytimeanewimageiscollected.Ifit
imagesforWorldwideReferenceSystem(WRS)Path12andRow31
isupdatedasnewimagesarecollected,thentheapproachbeginsto
with cloudcover less than 80% (based on theFmaskresults)were
approachnearreal-timechangedetection.Theuseof“continuous”in
used(Fig.2).Atotalof519imagesfromLandsat4TM(3images),
thenameofthealgorithmalsofollowsfromtheideathatalandcover
Landsat 5 TM (331 images), and Landsat 7 ETM+ (185 images)
mapcanbeproducedforanygiventimewithinthetimeperiodcovered
between1982and2011wereused.Theimagesarefairlyevenlydistrib-
byimages.Oneadditionalnoteisthatthisnewalgorithmisableto
utedthroughouttheyear(Table1),themonthsduringthegrowingsea-
detectmanykindsoflandcoverchange.
son(July,August,andSeptember)havingslightlymoreimagesthanthe
othermonths.
2.Dataandstudyarea
2.3.Landcoverreferencedata
2.1.Studyarea
Landcoverreferencedatacollectedatanygiventime(withinthe
ThestudyareaislocatedincoastalNewEngland,UnitedStates timeperiodcoveredbytheLandsatimages)willworkfortrainingthe
(Fig. 2). Itincludes all of RhodeIsland, as well as much of Eastern CCDCalgorithm.Thelandcoverreferencedatausedinthispaperwere
MassachusettsandpartsofEasternConnecticut.Ithasbeenselected previouslyusedtocalibratetheHEROMassachusettsForestMonitoring
because:(1)itincludesBostonmakingfieldvisitseasy;(2)itincludes Program(MaFoMP)2000landcoverproduct(Roganetal.,2010).They
awidevarietyofenvironmentsandlandcoversthatprovideexamples werecreatedwiththeaidofaerialphotographsandmanyfieldvisits
ofmanyoftheprimarykindsoflandcoverchangeoccurringinthe between2005and2007.Allreferencesiteswere60×60mindimen-
UnitedStates,including:extensiveurbanization(threemajormetro- sion,andweredistributedthroughoutMassachusettstocapturethe
politanareas—Boston,Providence,andWorcester),abandonmentof variabilityinreflectancevalueswithinthestudyarea.Intheoriginal
Fig.2.StudyareafortestingtheCCDCalgorithm.

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
155
Table1
FrequencybymonthofallavailableLandsatdataforthestudyareaatPath12Row31.
Month Jan. Feb. Mar. Apr. May Jun. Jul. Aug. Sept. Oct. Nov. Dec.
| Numberofimages | 41  | 41  | 40  | 41 43 | 43  | 52  | 48  | 52  | 47  | 40  | 31  |
| -------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
data,waterisdividedintotwolandcoverclasses(shallowwaterand method (DuMouchel & O'Brien, 1989; Holland & Welsch, 1977;
deepwater).Tosimplify,wecombinedshallowwateranddeepwater O'Leary,1990;Street,Carroll,&Ruppert,1988)isusedforestimating
intoonelandcoverclass—water.Thereareatotalof8220reference thetimeseriesmodel(Eq.1).TherobustfeatureoftheRIRLSmethod
sitesfor16categoriesoflandcover(Table2). reduces the influence of ephemeral changes, or pixels affected by
clouds,shadows,orsnowthatwerenotidentifiedbyFmask.
3.Methods
|     |     |     |     |     |     |     | (cid:1) | (cid:3) | (cid:1) | (cid:3) | (cid:1) (cid:3) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ------- | --------------- |
|     |     |     |     |     |     |     | 2       | π       | 2 π     |         | 2π              |
T h is s t u dy is a “ p r o to t y p e ” fo r c o n t in u o u s c h a ng e d e t e c t io n a n d ρ^ði;xÞ ¼a þa co s x þb sin x þa cos x
|     |     |     |     |     |     | RIRLS 0;i | 1;i(cid:1) Τ | 1;i | Τ   | 2;i | Ν Τ |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | --- | --- |
clas s ifi ca t i on us in g a ll a v a il a b le L an d s a t d a ta . T es t in g th i s a p p r o a ch f o r (cid:3)
2 π
otherregionswithdifferentenvironmentswillbeafutureresearch þb sin x ð1Þ
|                                                            |                     |             |             |            |        | 2;i | ΝΤ  |     |     |     |     |
| ---------------------------------------------------------- | ------------------- | ----------- | ----------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| direction.                                                 | This CCDC algorithm | has several | components, | including: |        |     |     |     |     |     |     |
| imagepreprocessing,continuouschangedetection,andcontinuous |                     |             |             |            | where, |     |     |     |     |     |     |
landcoverclassification.
Juliandate
x
3.1.Imagepreprocessing
I theithLandsatBand
T numberofdaysperyear(T=365)
| 3.1.1.Atmospherecorrection |     |     |     |     | N   | numberofyearsofLandsatdata |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
coefficientforoverallvaluesfortheithLandsatBand
| Geometricregistrationandatmosphericcorrectionarecriticaltothe |     |     |     |     | a 0,i |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
CCDCalgorithm,astheyfacilitatecomparisonofimagesthroughtime. a ,b coefficientsforintra-annualchangefortheithLandsatBand
1,i 1,i
Inthisresearch,weonlyuseLandsatL1Timagesastheyaremorepre- a ,b coefficientsforinter-annualchangefortheithLandsatBand
2,i 2,i
ciselyregisteredthantheLevel1Systematic(corrected)(L1G)images. ρ^ði;xÞ predictedvaluefortheithLandsatBandatJuliandatex
RIRLS
Atmospheric correction is performed using the Landsat Ecosystem basedonRIRLSfitting.
DisturbanceAdaptiveProcessingSystem(LEDAPS)atmosphericcor-
rectiontool(Maseketal.,2006;Vermoteetal.,1997),inwhichthe
DuetothefactthatcloudsandsnowmakeBand2brighterandcloud
rawDNvaluesareconvertedintoSurfaceReflectance(SR)andBright-
shadowsandsnowmakeBand5darker,weestimatetimeseriesmodels
nessTemperature(BT).
forBand2andBand5.BycomparingtheactualLandsatobservations
andthecorrespondingmodelpredictions,itiscomparativelyeasyto
3.1.2.Screeningofcloud,cloudshadow,andsnow identify any remaining clouds, cloud shadows, snow, and other
Clouds,cloudshadows,andsnowwereinitiallymaskedusinganewly ephemeralchanges(Fig.3).IfanyoftheconditionsinEq.(2)are
developed object-based algorithm called Fmask (Zhu & Woodcock, met,thisobservationisidentifiedasanoutlierandremovedfrom
2012). Though the Fmask algorithm provides relatively accurate furtheranalysis.
masksforclouds,cloudshadows,andsnow,itisnotperfect.Moreover, Themodelestimationstartswhenthereareatotalof15“clear”
thereareotherephemeralchangessuchasthickaerosols,smoke,or determinedbyFmask)observations.Thefirst12arecomparedbetween
floodingthatmayalsogetconfusedwithlandcoverchange.Therefore,
|     |     |     |     |     | observed | and model | predicted | values | to decide | whether | there are |
| --- | --- | --- | --- | --- | -------- | --------- | --------- | ------ | --------- | ------- | --------- |
outliers.Thereasonforpickingthefirst12clearobservationsisthat
theCCDCalgorithmusesasecondsteptofurtherscreenoutliersprevi-
thetimeseriesmodeloftheCCDCalgorithmhas4coefficients(see
ouslymissedbytheFmaskalgorithmbasedonmultitemporalanalysis
oftheLandsatdata(Zhu&Woodcock,inpreparation;Zhu,Woodcock, Section3.2fordetail)and12clearobservations(threetimesthenum-
&Olofsson,2012).Thisapproachfirstestimatesatimeseriesmodel berofcoefficients)helpmakemodelestimationrobustandaccurate.
basedonthe“clear”observationspreviouslyidentifiedbyFmaskand Wedonotperformthemultitemporalcloud,cloudshadow,andsnow
thendetectsoutliersbycomparingmodelestimatesandLandsatobser- screeningalgorithmforthelast3clearobservationsbecausetheCCDC
vations. The Robust Iteratively Reweighted Least Squares (RIRLS) algorithmneedsextraobservationsattheendofthetimeseriesto
Table2
16-categorieslandcoverdescription.
| Class    |     |     | Numberofsites |     |     | Description                                   |     |     |     |     |     |
| -------- | --- | --- | ------------- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
| Orchards |     |     | 234           |     |     | Managedplantationoffruittrees,primarilyapples |     |     |     |     |     |
Managedbogcontainingcranberrybushes,seasonallyflooded
| CranberryBogs    |     |     | 265 |     |     |                                         |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
| Pasture/RowCrops |     |     | 541 |     |     | Openandcultivatedagriculturalgrasslands |     |     |     |     |     |
DeciduousForest 570 Forestedland≥80%broadleaveddeciduouscanopycover
ConiferForest 582 Forestedland≥80%needleleavedevergreencanopycover
ForestlandN20%coniferandb80%deciduouscanopycover
| MixedForest |     |     | 702 |     |     |                              |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
| GolfCourse  |     |     | 486 |     |     | Highlymanagedopengrasslands  |     |     |     |     |     |
| Grassland   |     |     | 502 |     |     | Grasslanddominatedopenspaces |     |     |     |     |     |
LowDensityResidential 511 Residentiallandwithequalpartsimpervioussurface&vegetation
HighDensityResidential 466 Residentiallandminimallyvegetated,N60%impervioussurface
| Commercial/Industrial |     |     | 613  |     |     | Impervioussurface                 |     |     |     |     |     |
| --------------------- | --- | --- | ---- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
| Water                 |     |     | 1088 |     |     | StandingwaterpresentN11months     |     |     |     |     |     |
| Wetland               |     |     | 513  |     |     | Vegetatedlandswithahighwatertable |     |     |     |     |     |
SaltMarsh 436 Tidalsaltwaterrivers/mudflats&surroundingherbaceouscover
| SandQuarry |     |     | 374 |     |     | Sand&gravelminingpits |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
Barelandsparselyvegetated,N60%soilbackground
| BareSoil |     |     | 337 |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

156 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
allowthemodeltorespondtolandsurfacechangesothatchanges andtherequirementofcontinuousmonitoring,theCCDCalgorithm
thatoccurattheendoftheinitialmodelestimationwillnotbeiden- onlyappliesthismultitemporalcloud,cloudshadow,andsnowdetec-
tifiedasoutliers.Thereasonforpicking3clearobservationsisthat tionalgorithmduringthetimeofmodelinitialization(seeSection3.2
theCCDCalgorithmusesthreeconsecutiveobservationstodeter- fordetail).Forobservationsacquiredaftermodelinitialization,only
mine ifa pixel ischanged ornot (see Section 3.3 fordetail) and theFmaskalgorithmisused.
threeclearobservationsareenoughforthetimeseriesmodeltore-
spondtolandsurfacechange.Ifanyofthefirst12pixelsarefound
tobepossiblecloud,cloudshadow,snoworotherephemeralchanges, ρð2;xÞ−ρ^ð2;xÞ RIRLS N0:04 OR ρð5;xÞ−ρ^ð5;xÞ RIRLS b−0:04 ð2Þ
itisremovedfromtheclearpixellist.Duetocomputationallimitations
where,
A x Juliandate
ρ(i,x) ObservedvaluefortheithLandsatBandatJuliandatex.
ρ^ði;xÞ PredictedvaluefortheithLandsatBandatJuliandatex
RIRLS
basedonRIRLSfitting(Eq.1).
Cloud observation 3.2.TheCCDCtimeseriesmodel
Generally,landsurfacechangecanbedividedintothreecategories:
(1) intra-annual change (Fig. 4A),causedby vegetation phenology
drivenbyseasonalpatternsofenvironmentalfactorsliketemperature
andprecipitation;(2)gradualinter-annualchange(Fig.4B),caused
B
A
Snow observation
C
B
Cloud shadow observation
D
C
Snow observation
Fig.3.Illustrationofmultitemporalscreeningofcloud,cloudshadow,andsnow.The
circlesarepixelsidentifiedas“clear”byFmaskandthoselabeledaretheonesfoundby
themultitemporalanalysistobeclouds,cloudshadows,orsnow.Becausecloudsand
snowmakeBand2brighter(Fig.3A&B)whilecloudshadowsandsnowmakeBand5 Fig.4.ThreecategoriesoflandsurfacechangeshowninBand5surfacereflectance:
darker(Fig.3C&D),clouds,cloudshadows,andsnowareeasilyidentifiedbycomparing (1)intra-annualchange(orseasonality)(Fig.4A);(2)inter-annualchange(ortrend)
theactualLandsatobservationswiththemodelpredictions. (Fig.4B);and(3)abruptchange(orbreak)(Fig.4C).

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 157
byclimatevariability,vegetationgrowthorgradualchangeinland A
managementorlanddegradation;and(3)abruptchange(Fig.4C),
causedbydeforestation,floods,fire,insects,urbanizationandsoon.
Therefore,weuseatimeseriesmodelthathascomponentsofseasonal-
ity,trend,andbreaksthatcapturesallthreecategoriesofsurfacechange
(Eq.3).ThemodelcoefficientsareestimatedbytheOrdinaryLeast
Squares(OLS)methodbasedontheremainingclearLandsatobserva-
tions. We use OLS instead of RIRLS simply because it is faster and
moreaccuratewhenallthesignificantoutliershavebeenexcluded.
(cid:1) (cid:3) (cid:1) (cid:3)
ρ^ði;xÞ OLS ¼a 0;i þa 1;i cos 2 Τ π x þb 1;i sin 2 Τ π x þc 1;i x ð3Þ
B
(cid:4) (cid:5)
τ(cid:2)
k−1
bx≤τ(cid:2)
k
where,
x Juliandate
i theithLandsatBand
T numberofdaysperyear(T=365)
a coefficientforoverallvaluefortheithLandsatBand
0,i
a ,b coefficientsforintra-annualchangefortheithLandsatBand
1,i 1,i
c coefficientforinter-annualchangefortheithLandsatBand
1,i
τ⁎
thekthbreakpoints.
k
ρ^ði;xÞ predictedvaluefortheithLandsatBandatJuliandatex. C
OLS
Inthetimeseriesmodel,theoverall value,ormean,fortheith
LandsatBandiscapturedbya .Coefficientsa andb areusedto
0,i 1,i 1,i
estimatetheintra-annualchangescausedbyphenologyandsunangle
differencesfortheithLandsatBand.Theinter-annualchangeforthe
ithLandsatBandiscapturedbyc .Ideally,themorethecoefficients
1,i
included,themoreaccuratethemodelwillbe.However,whenthere
aretoomanycoefficients,themodelmaystarttofittonoise.Fig.5
showstheresultsofthemodelforthedifferentcomponentsofthe
timeseriesmodel.Ifweonlyuseasingleconstantcoefficient(a ),it
0,i
canonlycapturetheoverallreflectanceandalltheintra-andinter-
annualvariabilityislost(Fig.5A).Byaddingtheinter-annualtrend Fig.5.IllustrationoftheOLSfittingresultsbyincludingdifferentcomponentsofthetime
(c ),thetimeseriesmodelisabletocapturethetrends,however,los- seriesmodel.Fig.5Ashowstheresultswhenonlyincludingasingleconstant.Fig.5B
1,i showstheresultsofusingaconstantandaninter-annualtrendinthetimeseries
ingallintra-annualvariability(Fig.5B).Thebestresultcomeswhenall
model.Fig.5Cshowstheresultsofusingallthreecomponents.
threecomponentsareincluded(Fig.5C).
3.3.Continuouschangedetection
Thebasisofourmethodiscomparisonofmodelpredictionswith spectralband(orindex),maybedifficulttoidentifyinotherspectral
clearsatelliteobservationstofindchange.Ideally,asingledatecompar- bands(orindices).Moreover,thethresholdfordefiningchangemay
isonwouldbedefinitivefordetectingchange.However,thereissuffi- alsobedifferentfordifferentkindsoflandcoverchange.Therefore,
cientnoiseinthesystemduetofactorslikeundetectedclouds,cloud theCCDCalgorithmusesallLandsatspectralbandsandadata-driven
shadows,snow,atmospherichaze,smoke,andchangesinsoilwetness threshold(adjustedforeachindividualpixel)todetectmanykindsof
thatwillleadtonumerousfalsepositiveerrorsinchangedetection land cover change. The OLS method (Eq. 3) is applied to all seven
whenusingasingledateforcomparison(Zhu,Woodcock,&Olofsson, LandsatbandsandtheRMSEiscomputedforeachspectralband.The
2012).Whilenoisefactorstendtobeephemeralinnature,landcover difference between observations and model predictions for each
changeismorepersistentthroughtime.TheCCDCalgorithmminimizes LandsatbandisnormalizedbythreetimestheRMSE.Weusethree
ephemeraleffectsbyprocessingasetofdatestogetherasagroupfor timestheRMSEduetothefactthatthespectralsignalsusuallydeviate
identifyinglandcoverchange.Thatis,ifapixelisobservedtochange frommodelpredictionbymorethanthreetimestheRMSEwhenland
inmultipleconsecutiveimages,itismorelikelytobelandcoverchange. coverchangeoccurs.Fig.6illustrateshowthe“threetimestheRMSE”
Basedonpreviousstudies(Zhu,Woodcock,&Olofsson,2012),change criterionisusedfordetectinglandcoverchangeforadeforestation
identifiedinthreesuccessivedatesshowedthebestresults.Therefore, pixel.Whenthereisnolandcoverchange,thenextthreeclearobserva-
pixelsshowingchangeforoneortwoconsecutivetimeswillbeflagged tions are always within the model predicted ranges (±3 × RMSE)
as“possiblechange”andifathirdconsecutivechangeisfound,thepixel (Fig.6A&C).Fig.6Bshowshowchangeisinitiallydetectedbycompar-
isassignedtothe“change”class. ingthenextthreeconsecutiveclearobservationswithmodelpredic-
Todetectonekindoflandcoverchangesuchasforestchange,asin- tions. Fig. 6 only uses one Landsat band (Band 5) to illustrate the
glechangeindexwithafixedthresholdissufficient(Zhu,Woodcock,& algorithm,butallsevenspectralbandsareusedtodetectchange.In
Olofsson,2012).Tofindmanykindsoflandcoverchange,weneedto Fig.7,thesamedeforestationpixelasFig.6isshownandwhendefores-
usemorespectralbands,aslandcoverchangethatisobviousinone tationoccurred,allspectralbandschangedsignificantly.Therefore,the

158 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
A
B
C
Fig.6.ThisfigureillustratesthereasonforusingthethresholdofthreetimestheRMSEforcontinuouschangedetection.Fig.6AshowsthemodelpredictionandthreetimestheRMSE
beforechangeoccurred.Fig.6BshowsthemodelpredictionandthreetimestheRMSEwhenchangeoccurred.Fig.6CshowsthemodelpredictionandthreetimestheRMSEafterchange
occurred.
CCDC algorithm averages the difference between observations and ρ^ði;xÞ predictedvaluefortheithLandsatBandatJuliandatexbased
OLS
model predictions that have been normalized by three times the onOLSfitting(Eq.3).
RMSEforallsevenLandsatbands,andiftheresultislargerthan1for
threeconsecutiveclearobservations,achangeisidentified(Eq.4).
Landcoverchangethatoccurswithinthetimeofmodelinitialization
Otherwise,ifthevaluesforonlyoneortwoconsecutiveobservations (startofthemodelestimation)canbiasthetimeseriesmodelpredictions.
arelargerthan1,itwillberegardedasanephemeralchangeandthe Therefore,ifthereislandcoverchangeduringtheprocessofmodelini-
observationswillbeflaggedasoutliers.TheCCDCalgorithmupdates tialization,theCCDCalgorithmwillremovethefirstclearobservation
thetimeseriesmodelwhennewclearobservationsbecomeavailable, andaddonemoreclearobservationandthisprocesswillcontinueuntil
addingadynamiccharactertotheprocessthatallowsthetimeseries nopossiblechangeisdetectedwithintheinitializationtimeperiod.Asa
toadjustovertime.Eq.(4)providesthedetailsofthelandcoverchange result,eachpixelwillhaveitsownstartdateformodelinitialization
algorithm. Note that the continuous change detection algorithm andthisalsoleadstodifferentstartdatesforthecontinuouschange
assumes that the phenology is consistent for stable land covers, detectionandclassificationprocess.Threeapproachesareusedtodetect
whichmaynotbetrueforsomesemi-aridenvironmentsduetothe changethatmighthaveoccurredduringthetimeperiodcoveredbythe
variationoftheinter-annualdifferences.Furtherstudiesmaybeneces- first12clearobservationsusedformodelinitialization:abnormalslope,
saryifwewanttoexpandtheuseofthisalgorithmtootherpartsofthe abnormalfirstobservation,andabnormallastobservation.
world. Forpixelsofstablelandcover,themagnitudeoftheslopeofthetime
seriesmodelwillberelativelysmall.Iflandcoverchangeoccursduring
thetimeofmodelinitialization(t ),theobservationwillusually
(cid:6) (cid:6) model
1
k
∑k
i¼1
(cid:6)ρði;
3
x
(cid:3)
Þ−
R
ρ^
M
ði
S
;
E
x
i
Þ OLS (cid:6) N1ðthreetimesconsecutivelyÞ ð4Þ d
se
e
r
v
i
i
e
a
s
te
m
m
od
o
e
re
ll
t
a
h
r
a
g
n
er
th
th
re
a
e
n
t
3
im
×
es
R
t
M
he
SE
R
i
M
/t m
S
o
E
d
,
e
m
l .T
a
h
ki
e
n
r
g
ef
t
o
h
r
e
e,
s
t
lo
h
p
e
e
sl
o
o
f
p
t
e
he
of
ti
t
m
he
e
where, timeseriesmodelfortheithBandisnormalizedby3×RMSEi/t
model
(seeEq.5fordetails),andiftheaveragevalueofthenormalizedslope
x Juliandate forallbandsislargerthan1,itwillbedetectedasanabnormalslope,
i theithLandsatband indicatingapossiblechangewithinthemodelinitializationtime.On
k thenumberofLandsatbands theotherhand,iflandcoverchangeoccursatthestartortheendof
ρ(i,x) observedvaluefortheithLandsatBandatJuliandatex modelinitialization,theremaynotbeenoughobservationsaffectedby

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 159
thelandcoverchangetosignificantlyinfluencethemagnitudeofthe canstillbedetectedbycomparingobservationswithmodelpredictions.
slope,buttheymaystillinfluencemodelestimation.Inthiscase,the Therefore,theCCDCalgorithmalsocalculatesthedifferencebetween
CCDCalgorithmcomparesLandsatobservationswithmodelpredictions observationsandmodelpredictionsforthefirstandthelastobserva-
forthefirstandthelastobservationsduringmodelinitialization.Asa tions.Next,thedifferencebetweenobservedandpredictedvaluesfor
fewchangeobservationsattheverybeginningorendofthemodelini- eachLandsatbandisnormalizedbyRMSEi(seeEq.5fordetails),and
tializationperiodwillnotinfluencemodelpredictionsignificantly,they iftheaveragevalueofthenormalizeddifferenceforallLandsatbands
A
B
C
D
E
Fig.7.ThisfigureillustrateshowthesevenLandsatspectralbands(Bands1–7)deviatefromtheiroriginaltrajectorieswhendeforestationoccurred.

160 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
F
G
Fig.7. (continued).
islargerthan1forthefirstorthelastobservation,itwillbeidentifiedas (includingthethermalband)wereusedforthelandcoverclassification.
anabnormalobservation,indicatingpossiblechangewithinthemodel Ingeneral,itisusuallynotrecommendedtoincludethermaldatain
initializationperiod.Assoonasthemodelinitializationisfinished, landcoverclassificationduetoitssensitivitytosubstantiallydifferent
it will be used as the basis for continuous change detection and physicalphenomena.Includingthermal data cancausemoreharm
classification. thangoodinlandcoverclassification.However,theCCDCalgorithmis
abletousethemultitemporalthermaldataintheformofthecoeffi-
1 k ∑k i¼13(cid:3)R (cid:6) (cid:6) M c 1; S i ð E x i = Þ (cid:6) (cid:6) t model N1 OR 1 k ∑k i¼1 (cid:6) (cid:6)ρði;x 3 1 (cid:3) Þ− R ρ^ M ði S ; E x i 1 Þ OLS (cid:6) (cid:6) N1 ð5Þ c v a i b a e r i n l i i a t t t s y io f i o n n r i t o n e v m t e e r p m a e l p r l a e t t e r u a m t r u e p r e i e s r . a r I t n e u m t r h e o , i v s t e r a e d p n p a d r n o i d n ac t t h h e , e m m g p o e e n s r t e a o r tu a f l r t e h p , e a a t s n t h e d o rn r in t s - t t r r e e a r l - m a a t n e v n d a u r t a i o - l
(cid:6) (cid:6)
OR 1 k ∑k i¼1 (cid:6)ρði;x 3 n (cid:3) Þ− R ρ^ M ði S ; E x n Þ OLS (cid:6) N1 s la u n r d fa c c o e v c e h r a c r la a s c s t i e fi r c is a t t i i c o s n. remain,andtheyproveusefulforimproving
i Themainideaofthelandcoverclassificationisthatdifferentland
where, coverclasseswillhavedifferentshapesfortheestimatedtimeseries
models.Fig.8illustratesdifferentestimatedtimeseriesmodelsfor
x Juliandate fourdifferentkindsoflandcoverchangethatoccurredinthestudy
x
1
the Julian date for thefi rst observation during model area.TakingFig.8Aforinstance,byclassifyingthefirsttimeseries
initialization model, the CCDC algorithm is capable of providing a land cover
x n the Julian date for the last observation during model class(forest)forthispixelbetween2001and2003.Similarly,theclassi-
initialization ficationresultsofthesecondtimeseriesmodelprovidethelandcover
i theithLandsatBand class (developed) for this pixel between 2005 and 2006. The gaps
k thenumberofLandsatbands(k=7) inthemiddleoftwomodelsareclassifiedas“disturbed”intheland
RMSEi RootMeanSquareErrorfortheithLandsatBand(Eq.3) covermaps,becausethelargevariabilityinthedataduringthetransi-
T model thetotaltimeusedformodelinitialization tion time prevents model initialization. Note that when forest is
C 1,i coefficientforinter-annualchangefortheithLandsatBand changedtodeveloped,thetimeseriesmodelsshowcompletelydifferent
(Eq.3) shapes,especiallyforBand4andBand6(Fig.8A).ThereductionofBand
ρ(i,x) observedvaluefortheithLandsatBandatJuliandatex 4reflectanceiseasytounderstand:forestreflectsstronglyinBand4
ρ^ði;xÞ OLS predictedvaluefortheithLandsatBandatJuliandatexbased whiledevelopedareasdonot.TheincreaseinBand6ismostlydueto
onOLSfitting(Eq.3).
reducedevapotranspirationandurbanheatislandeffectswhenforest
isconvertedtodeveloped.Whenforestischangedtobarren(Fig.8B),
themostsignificantchangesareobservedinBand5andBand7,asforest
3.4.Continuouslandcoverclassification isusuallylowinSWIRbandsbutbarrenalwayshashighreflectancein
thesespectralbands.Forapixelthathasundergoneachangefromforest
Findinglandcoverchangeisimportant,butitwillbemorebeneficial tograss(Fig.8C),thereisnotmuchdifferenceinthetimeseriesmodels
ifweknowthelandcovercategoriesbeforeandafterchange.Insteadof inthevisiblebands,buttheSWIRandthermalbandsarequitedifferent.
classifyingtheoriginalLandsatimagesasconventionalmethodswould, Forthepixelthatchangedfromforesttoagriculture(Fig.8D),thetime
theCCDCalgorithmusesthecoefficientsoftimeseriesmodelsasthe seriesmodelsoftheNIRandSWIRbandsshowthebiggestdifference.
inputsforlandcoverclassification.Afterthechangedetectionprocess, Theseexamplesillustratethattheinformationcontainedinthetime
eachpixelwillhaveitsowntimeseriesmodelsbeforeandafterany seriesmodelishelpfulforlandcoverclassificationandbyusingthe
changes.Byclassifyingthetimeseriesmodelcoefficients,thisalgorithm coefficientsofthetimeseriesmodelitispossibletoprovideasingle
canprovidealandcovertypefortheentiretimeperiodforeachtime landcoverclassfortheentireperiodwhenchangeisnotspecifically
seriesmodel.TimeseriesobservationsfromallsevenLandsatbands identified.

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 161
A Forest Developed
B Forest Barren
C Forest Grass
D
Forest Agriculture
Fig.8.ExamplesoftheestimatedtimeseriesmodelsforallsevenLandsatbandsforthefourmostcommonlandcoverchangeinthestudyarea.
Fivevariables(ρ;a ;b ;c ;andRMSE)generatedfromtimeseries 35variablesusedastheinputforclassification.Asthereferencedata
1 1 1
modelestimationareusedasinputsforlandcoverclassification.The arecollectedbetween2005and2007,theestimatedcoefficientsofthe
firstvariable(ρ)representstheoverallspectralvalueatthecenterof reference pixels that were not detected to have land cover change
eachtimeseriesmodelforeachLandsatband.Thisoverallvalueis between2005and2007areusedfortrainingtheclassifier.TheRandom
calculatedbyaddingaconstant(a )andaslope(c )multipliedby Forest Classifier (RFC) is used to perform land cover classification
0 1
thetimetothemiddleofthetimeseriesmodel(Eq.6).Thesecond becauseofitsrelativelyhighaccuracyandcomputationalefficiency
and the third variables (a & b ) provide temporal information (Breiman,2001).
1 1
aboutintra-annual(orseason)patterns.Thefourthvariable(c )
1
measures inter-annual differences or trends. The last variable t þt
(RMSE) is calculated during OLS fitting in Eq. (3) and measures
ρðiÞ¼a
0;i
þc
1;i
(cid:3) start
2
end ð6Þ
howwellthetimeseriesmodelfitsthedata.Fig.9showstheaverage
fromreferencesitesforthefivedifferentvariablesfordifferentland
covercategories.Itisclearthatdifferentlandcoversshowquite where,
differentshapesintheplotsofthefivevariables,andthisinforma-
tion is helpful for discriminating land cover types. Considering t start thetime(Juliandate)whenmodelinitializationstarts
thereare7spectralbandsandeachbandhas5variables,thereare t end thetime(Juliandate)whenmodelinitializationends

162 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
A C
B D
E
Fig.9.Thevalueofthefivevariables,ðρ;a1 ;b1 ;c1andRMSE)fordifferentlandcoverclassesbasedonreferencesitesforeachlandcovercategory.
i theithLandsatBand 4.Results
a coefficientforoverallvaluefortheithLandsatBand(Eq.3)
0,i
c coefficient inter-annual change for the ith Landsat Band 4.1.ResultsoftheCCDCalgorithm
0,i
(Eq.3)
ρðiÞ overallspectralvalueatthecenterofeachtimeseriesmodel TheCCDCalgorithmiscapableofprovidinglandcoverchange
fortheithLandsatBand. and classification maps continuously as newly collected Landsat

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 163
Massachusetts
Connecticut
Rhode Island
Fig.10.TwopiecesofLandsatdatausedforillustrationtheCCDCresultsinthestudyarea.Thesmallerone(left)isusedforillustratingtheCCDCresultsinFig.11andthelargerone(right)
isusedforillustratingtheCCDCresultsinFig.12.
imagesbecomeavailable.Weusedaverysmall(5.6km×2.8km) 2011)ofthetimeseries.Thetwoimagesontheright(Fig.12C&D)are
andarelativelylarge(90km×45km)areatoillustratetheresults themostrecentchangedetectionandclassificationmapsattheendof
oftheCCDCalgorithm(Fig.10). thetimeseriesgeneratedbytheCCDCalgorithm.Thiscomprehensive
Fig.11illustratestwo“snapshots”oftheCCDCresultsforthesmaller analysisoflandcoverprovidesboththetiming andnatureofland
pieceofLandsatimage.Fig.11AistheCCDCresultforSeptember2nd, coverchanges.Tosimplifyforillustrationpurposeswecollapsedthe
1988andFig.11BistheCCDCresultforJuly16th,2011.Foreachtime 16-categorieslandcoverclassesinto7-categoriesclasses:forest,wet-
period,thetopthreepanelsconsistofasmallpieceofanewlycollected land,agriculture,barren,water,grass,anddeveloped.Forexample,we
Landsatimage(left),themostrecentlandcoverchangemapatthecor- caneasilyderiveinformationlikeinthepast30yearsthelargestloss
respondingtime(middle),andalandcoverclassificationmapatthe offorestisfromforesttodevelopedandthelargestgainofforestisfrom
sametime(right).Thethreegraphsatthebottomarethetimeseries barrentoforestforthisarea.Itcanalsoprovidenewkindsofinformation
data(Band4)forthethreepixelslocatedinsites1,2,and3thatulti- aboutwhatkindoflandcoverchangeoccurredonayearlybasisforthe
matelyunderwentsomekindsoflandcoverchange.Thatchangethat entirescene.Fig.13illustratestheannualamounts(km2)ofdifferent
occurredatthesepixelsisobviouswhenviewedfromtheperspective kindsofforest-relatedlandcoverchange.Fig.14illustratestheamount
oftheentiretimeseries.Thisapproachallowstheidentificationofthe offorestlossonayearlybasis.NotethatbothFigs.13and14startin
timingofeachchange,aswellasthekindofchange.Whenthetimese- 1986insteadof1982whenfirstLandsatimageisacquired.Thisisbe-
rieshasbeenbuiltforapixelandanalyzedforchange,itispossibleto causetheCCDCalgorithmneedsatleast15clearobservationstoinitial-
usetheestimatedtimeseriesmodelsbetweenthechangestoidentify ize the time series model for continuous change detection and
thelandcover class for thepixel atdifferent time periods.For the classificationandbefore1986mostofthepixelsdonothavemore
pixellocatedatsite1,theestimatedmodelprecedingthechangein than15clearobservations.
1988canbeusedtoclassifythelandcoverfortheentiretimepriorto
thechange.Similarlytheestimatedmodelsubsequenttothechange 4.2.Accuracyassessment
can be used to identify what land cover came after the change in
1988.Theshapeofthetimeseriesmodelcanbeveryhelpfulinland 4.2.1.Accuracyassessmentforchangedetection
coverclassificationwhichisevidentinthetimeseriesgraphsatthebot- AstheCCDCalgorithmiscapableofdetectingchangeathightempo-
tom,asinitiallybothpixelslocatedatsites1and3wereconiferforest ralfrequency,itisdifficulttofindreferencedatathatcanthoroughly
andpixellocatedatsite2wasahardwoodforest,andtheyarereadily assessitsaccuracybothspatiallyandtemporally.Theresimplyarenot
distinguishablebythedifferenceintheamplitudeoftheirtimeseries independentdatasetsavailablethathavebothfinerspatialresolution
inBand4. andhighertemporalfrequencythanLandsatimagesoverthetimeperi-
Fig.12illustratestheCCDCresultsforthelargerpieceofLandsat odcoveredbyLandsat.Toknowwhereandwhenlandcoverchange
data.Thetwoimagesontheleft(Fig.12A&B)aretwoclearLandsatim- occurs,theprimarysourceforreferencedataistheLandsatimages
agesatthebeginning(September17th,1984)andattheend(July16th, themselves(Cohen,Yang,&Kennedy,2010).Highspatialresolution

Landsat surface reflectance Land cover change map Land cover classification map
Bare soil
2009-08-15
Sand Quarry
2006-11-19
Salt Marsh
2004-02-23 Wetland
2001-05-29 Water
Comm/Ind
1998-09-02
High Den Res
1995-12-07 Low Den Res
1993-03-12 Grassland
1990-06-16 Golf Course
Mixed Forest
1987-09-20
Conif Forest
1984-12-24 Decid Forest
1982-03-30 Pasture/Crops
Cranb Bogs
Orchard
Disturbed
4000
1 2000
0
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01
4000
2
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01 N
3 0
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01
imagesfromGoogleEarth(http://earth.google.com/)canhelpmanual data,theirhighspatialresolutionishelpfulindetermininglandcover
interpretationofthelandcoverclasses.Thoughthehighspatialresolu- changeatlongertimeintervals.Arandomstratifiedsampledesign
tionimagescannotprovidethesametemporalfrequencyasLandsat wasusedforassessingthechangedetectionaccuracy.Atotalof500
)401X(
ecnatcelfer
ecafrus
4
dnaB
Landsat surface reflectance Land cover change map Land cover classification map
Bare soil
2009-08-15
Sand Quarry
2006-11-19 Salt Marsh
2004-02-23 Wetland
2001-05-29 Water
Comm/Ind
1998-09-02
High Den Res
1995-12-07 Low Den Res
1993-03-12 Grassland
1990-06-16 Golf Course
Mixed Forest
1987-09-20
Conif Forest
1984-12-24 Decid Forest
1982-03-30 Pasture/Crops
Cranb Bogs
A Orchard
Disturbed
4000
1 2000
0
4000
2
N
3 0 0.5 1 2
Kilometers
1
2
3
B
2000
0
4000
2000 0.5 1 2
0 Kilometers
)401X(
ecnatcelfer
ecafrus
4
dnaB
164 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
1
2
3
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01
2000
0
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01
4000
2000
0
1985-01-01 1990-01-01 1995-01-01 2000-01-01 2005-01-01 2010-01-01
Fig.11.Two“snapshots”ofthesmallerpieceofLandsatdatausedforillustratingtheCCDCresults.PanelAistheCCDCresultsatthebeginning(September2nd,1988)andpanelBisthe
CCDCresultsattheend(July16th,2011)ofthealmost30yearsoftimeseriesdata.Foreachtimeperiod,thetopthreepanelsareasmallpieceofanewlycollectedLandsatimage(left),a
mapshowingthetimingandlocationoflandcoverchangeatthesametime(middle),andthecorrespondinglandcovermap(right).Thethreegraphsatthebottomarethetimeseriesof
Band4surfacereflectanceforthethreepixelsinsites1,2,and3locatedinthecenterofthewhiterectangles.Notethatallthreesitesunderwentlandcoverchange(theystartedasforest)
anditisrelativelyeasytotellwhentheychanged.

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 165
Fig.12.ThelargerpieceofLandsatdatausedforillustratingtheCCDCresults.PanelAisfromtheSeptember17th,1984Landsatimage.PanelBisfromtheJuly16th,2011Landsatimage.
PanelCisthemostrecentlandcoverchangemap.PanelDisthemostrecentlandcoverclassificationmap.
referencepixelswereselected,inwhich250pixelswerefromareas examiningthetimeseriesdataforallsevenbands,itcanbequiteeasy
wherelandcoverwaspersistentthroughoutthetimeoftheanalysis toidentifypixelsthathavechangedandwhenthechangeoccurred.If
(1982–2011)and250pixelswereselectedwithinareaswhereland thereisconfusionindeterminingachangeorwhenitoccurred,we
cover change was identified by the CCDC algorithm. By carefully examinedtheLandsatimagesbeforeandafterthepossible change

166 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
Table3
Theaccuracyassessmentofchangedetectioninthespatialdomain.
Referencedata(spatialdomain)
Changedpixels Stablepixels Total User's(%)
Changedpixels 214 36 250 85.60
Stablepixels 5 245 250 98.00
Total 219 281
Producer's(%) 97.72 87.19 Overall(%) 91.80
moretimesconsecutively;3)lowtemporalfrequencyofthetimeseries
data;and4)verysmallRMSEs.Overfittingmaycauseseriousproblems.
Thoughweareusingsimpletimeseriesmodel,overfittingcanstill
happenifthedataarealwaysmissingforacertaintimeofyearbecause
ofcloudsand/orsnow.InFig.17,overfittingoccurredforBand4atthe
beginningofmodelestimation,duetoconstantsnowcoverduringthe
winterandthisledtoacommissionerrormarkedbytheredcircle.On
theotherhand,ifcloudsaremissedthreeconsecutivetimes,itwill
alsobefalselyidentifiedaschange(Fig.18).Forpixelslocatedatthe
Fig.13.Histogramoftheannualamounts(km2)ofdifferentkindsofforest-relatedland
edgesofLandsatimages,thetemporalfrequencyofthetimeseriesis
coverchangebetween1986and2010.
muchlower,andthiswillreducetheaccuracyofmodelestimation,
whichmayalsoleadtofalselyidentifiedchange(Fig.19).Thelastrea-
timeorusedhighspatialresolutionimagesfromGoogleEarthtohelp
determinewhatwashappeningatthattimeforthatspecificlocation. sonforfalsedetectionofchangeisaverysmallRMSE.SincetheCCDC
Iftherearemultiplechangeswithinonepixel,onlythefirstchangeis algorithm uses the RMSE value for defining the threshold for land
coverchange,whentheRMSEvalueissmall,averyslightchangecaused
usedintheaccuracyassessment.
bytheatmosphereorotherfactorscanbeeasilyconfusedwithland
Theresultsoftheaccuracyassessmentshowproducer'saccuracyof
coverchange.Thisproblemiscommonforpixelsthatarespectrally
97.72%anduser'saccuracyof85.60%forchangedpixels,andoverall
dark,suchaswater(Fig.20).Someoftheseproblemscanbeovercome
accuracyof91.80%(Table3).Therelativeloweruser'saccuracyindi-
byintelligentpost-processingofthedata.Forexample,ifthelandcover
catesmorecommissionerrorsthanomissionerrorsindetectedchanges.
classisthesamebeforeandafterthechangeisidentified,itislikelythat
Ahigherthresholdormoreconsecutiveobservationsmaybetterbal-
theidentifiedchangeisanerror.
ancethecommissionandomissionerrors.
Thetemporal accuracy of change detection was assessed for all
Theomissionerrorsaremostlyduetothefollowingreasons:1)par-
214pixelsintheaccuracyassessmentselectedfromareaswherethe
tiallychangedpixels;and2)changeoccurstooearly,beforethemodel
isinitialized.Thepartiallychangedpixelsarealwaysdifficulttodetect,
algorithmfoundlandcoverchange,andarecorrectlyidentifiedinthe
spatialdomain.Theproportionofthepixelsthathavethesamechange
asthemagnitudeofchangeismostlydependentontheproportionof
timebetweentheCCDCresultsandthereferencedataisreferredtoas
changewithinthatpixel.InFig.15,therewasapartialforestcutaround
the“temporalaccuracy”.Thealgorithmoccasionallyfindschangelater
1998anditisevidentthatafterthatpointintimetheBand5variability
changedsignificantly,butthemagnitudeofthischangeisrelatively thanthereferencedatabutitneverfoundchangeearlierthantherefer-
encedata.Theproportionofthepixelsthathavethesametimeof
small. On the other hand, if change occurred at the beginning of
changebetweenthealgorithmresultsandreferencedatais79.91%
model initialization, the CCDC algorithm was unable to detect any
(Table4).Theproportionofthepixelsthatarefoundtohavechanged
kindofchangeastherearenotenoughobservationstoinitializethe
laterthanthereferencedatabutarewithin32daysofthefirstdate
timeseriesmodel(Fig.16).
whenachangeisobservableis13.08%whichis65.12%ofthetemporal
Thecommissionerrorsmostlyresultfromthefollowingreasons:
1) overfitting of the time series model; 2) clouds missed three or
errors(Table4).Inotherwords,ifweconsiderfindingchangeswithina
monthofthefirstobservabledateis“correct”,thetemporalaccuracyis
ashighas92.99%.
Thetemporalerrorsaremostlyduetothefactthatattheverybegin-
ningofthechange,thepixelmayhaveonlypartiallychanged,andthis
spectralchangeisnotlargeenough(lessthanthreetimestheRMSE)
tobeidentifiedbytheCCDCalgorithm.However,thischangemaybe
lateridentifiedbytheCCDCalgorithmwhenitistotallychanged.In
Fig.21,beforetheredcircle(thechangeidentifiedbytheCCDCalgo-
rithm), there is one observation that slightly deviates from model
predictionthatwasmainlycausedbyapartialforestcut(indicatedby
thegreencircle),butthisdeviationisstillrelativelysmallcomparedto
thenextclearobservationintheredcircle.
Table4
Theaccuracyassessmentofchangedetectioninthetemporaldomain.
Referencedata(temporaldomain)
Same Late≤32days LateN32days Total
Changedpixels 171 28 15 214
Proportion(%) 79.91 13.08 7.01 100.00
Fig.14.Histogramoftheannualamounts(km2)ofnetforestlossbetween1986and2010.

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
167
/laicremmoC=IC,laitnediseRytisneDhgiH=DH,laitnediseRytisneDwoL=DL,dnalssarG=G,esruoCfloG=CG,tseroFdexiM=FM,tseroFrefinoC=FC,tseroFsuoudiceD=FD,sporCwoR/erutsaP=CP,sgoByrrebnarC=BC,sdrahcrO=O:etoN
4.2.2.Accuracyassessmentforclassification
| 59.68 80.99 04.98 73.19 | 10.98 50.58 24.29 99.78 93.87 23.78 | 70.88 94.89 37.29 49.89 68.48 78.58 02.09 |     |     |     |     |
| ----------------------- | ----------------------------------- | ----------------------------------------- | --- | --- | --- | --- |
.esU Thelandcoverreferencedatapreviouslyusedforcontinuousland
coverclassification(introducedinSection2.3)wereusedasthebasis
forassessingtheaccuracyofclassificationfortheCCDCalgorithm.As
41.18
thelandcoverreferencedatawerecollectedbetween2005and2007,
| 33 2 601 41 | 0 93 42 64 05 0 | 95 0 9 0 951 7232 |     |     |     |     |
| ----------- | --------------- | ----------------- | --- | --- | --- | --- |
SB wewill onlyassessthe accuracy oflandcoverclassification at this
specifictimeinterval.Atotalof80%ofthelandcoverreferencedata
wererandomlyselectedtotraintheclassifier,andtheremaining20%
11.19
wereusedtoassessmapaccuracy(Fielding&Bell,1997).Thisprocess
| 0 0 71 0 | 0 51 0 71 2 0 | 411 0 5 0 5362 78 |     |     |     |     |
| -------- | ------------- | ----------------- | --- | --- | --- | --- |
QS was repeated 50 times and the average user's accuracy, average
producer'saccuracy,andaverageoverallclassificationaccuracywere
usedtoassessthelandcoverclassificationaccuracyfortheCCDCalgo-
85.79
0 0 0 0 0 41 0 0 8 0 7 3 24 7892 0 0 rithm.Inthisapproach,eachreferencepixelisusedmanytimesfor
MS
bothtrainingandaccuracyassessment,butneverbothforasingletrial.
Theaverageoftheoverallaccuracyofthelandcoverclassificationwith
|     |     | 70.59 | 16-categoriesis90.20%(Table5),whichisalmostthesameaccuracyas |     |     |     |
| --- | --- | ----- | ------------------------------------------------------------ | --- | --- | --- |
TW 0 0 21 12 0 24 0 0 61 0 0 56 1343 12 0 1 anotherstudyofthesameplaceusingallavailabledimensions(spectral,
temporal,andspatial)ofLandsatdata(Zhu,Woodcock,Rogan,etal.,
2012).Theaverageproducer'sanduser'saccuraciesforthedifferent
|         |              | 80.89              | landcovertypesarealsoquitehigh,withmostlybeingapproximately |     |     |     |
| ------- | ------------ | ------------------ | ----------------------------------------------------------- | --- | --- | --- |
| 0 5 0 0 | 1 02 0 0 0 0 | 0 1138 211 0 31 21 |                                                             |     |     |     |
90%(Table5).ThelargestconfusionsarebetweenMixedForestandCo-
W
niferForest,DeciduousForestandMixedForest,LowDensityResidential
andHighDensityResidential,andLowDensityResidentialandCommer-
75.38
| 0 0 0 9 | 0 37 0 02 662 91 | 8013 0 8 0 561 15 | cial/Industrial(Table5). |     |     |     |
| ------- | ---------------- | ----------------- | ------------------------ | --- | --- | --- |
IC
5.Discussionandconclusions
25.58
0 0 0 0 0 0 0 0 101 4941 631 0 0 0 61 0 Detectionoflandcoverchangeandclassificationaredifficultprob-
DH
lemsinremotesensing.BetteruseofthetemporaldomainofLandsat
datacanimprovebothchangedetectionandlandcoverclassification.
|     |     | 11.48 | Inthisstudy,wedevelopedanewalgorithmforcontinuouschange |     |     |     |
| --- | --- | ----- | ------------------------------------------------------- | --- | --- | --- |
22 0 41 62 8 93 3 19 0882 581 44 15 11 6 5 93 detectionandclassificationathightemporalfrequency.Byusingall
DL
|     |     |     | available Landsat | data, this approach | allows reconstruction | of the |
| --- | --- | --- | ----------------- | ------------------- | --------------------- | ------ |
historyoftheEarthsurfaceintheLandsatTMandETM+era.Models
42.48
estimatedbysinesandcosinescanpredictLandsatobservationsat
| 17 0 39 5 | 0 21 38 7692 711 31 | 16 0 0 0 43 66 |     |     |     |     |
| --------- | ------------------- | -------------- | --- | --- | --- | --- |
anydateassumingthereisnolandcoverchange.TheCCDCalgorithm
| G   |     |     | flagslandcoverchangebydifferencingthepredictedandobserved |     |     |     |
| --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
Landsatdata.Itdeterminesapixelhasexperiencedalandcoverchange
30.98
ifitshows“change”forthreeconsecutivetimes.Theestimatedtime
| 34 8 93 43 | 01 32 0542 901 42 0 | 0 8 1 3 0 0 |     |     |     |     |
| ---------- | ------------------- | ----------- | --- | --- | --- | --- |
CG seriescoefficients(alsoincludingtheRMSEs)wereusedforlandcover
classification.ThereferencedatarevealedthattheCCDCresultswere
.lioSeraB=SB,yrrauQdnaS=QS,hsraMtlaS=MS,dnalteW=TW,retaW=W,lairtsudnI accuratefordetectinglandcoverchange,withproducer'saccuracyof
02.68
97.72%anduser'saccuraciesof85.60%inthespatialdomain,andtem-
| 0 3 0 902 | 134 6864 24 0 12 0 | 0 0 21 0 23 0 |     |     |     |     |
| --------- | ------------------ | ------------- | --- | --- | --- | --- |
FM poralaccuracyof79.91%.TheCCDCclassificationresultsalsoshowed
highoverallaccuracyof90.20%.
|          |                   | 64.98       | TheCCDCalgorithmhasmanyadvantages.Itisfullyautomatedand |     |     |     |
| -------- | ----------------- | ----------- | ------------------------------------------------------- | --- | --- | --- |
| 0 0 0 11 | 3463 973 0 0 43 0 | 0 0 2 0 0 3 |                                                         |     |     |     |
iscapableofmonitoringmanykindsoflandcoverchangeassoonas
FC
newimagesbecomeavailable.Moreover,therearenoempiricalorglob-
althresholdsusedindetectingchange.Thethresholdsaregenerated
|            |               | 87.39          | through theoriginal | observations | and model estimation | which are |
| ---------- | ------------- | -------------- | ------------------- | ------------ | -------------------- | --------- |
| 1 0 3 9163 | 0 631 0 0 0 0 | 0 0 03 0 64 42 |                     |              |                      |           |
doneseparatelyforeachindividualpixel.Inthisstudy,threetimesthe
FD
RMSEisrecommendedforthresholding,butmoresubtlechangescan
becapturediftwotimestheRMSEisused,whichalsoresultinmore
31.88
falsedetectionoflandcoverchange.Thecontinuouscharacterofthe
| 821 2 0553 01 | 0 32 73 06 011 0 | 0 0 63 0 0 27 |     |     |     |     |
| ------------- | ---------------- | ------------- | --- | --- | --- | --- |
monitoringmakesthealgorithmcapableofusingasmanyimagesas
.noitacfiissalcfotnemssessaycaruccaehT CP
possible.Therefore,howfasttheCCDCalgorithmisabletofindchange
|     |     | 24.79 | anditscorrespondinglandcovertypeisprimarilydependentonthe |     |     |     |
| --- | --- | ----- | --------------------------------------------------------- | --- | --- | --- |
0 2512 2 0 0 8 0 11 31 0 0 0 1 0 0 22 frequencyofavailableclearobservations.Thisalgorithmwillimprove
BC
|     |     |     | as the frequency | of images from | sensors like Landsat | increases |
| --- | --- | --- | ---------------- | -------------- | -------------------- | --------- |
(Arvidsonetal.,2006).TheopeningofthearchivefromEarthResources
|     |     | 41.98 | ObservationandScience(EROS)DataCenteristhefirstmajorstep.Data |     |     |     |
| --- | --- | ----- | ------------------------------------------------------------- | --- | --- | --- |
6891 0 531 3 0 1 21 15 23 0 0 0 0 2 0 6 fromtheLandsat8shouldfurtherincreasethefrequencyofavailable
O observations considering the much larger duty cycle for Landsat 8
comparedwithpreviousLandsatsatellites.ThetwoSentinel2A/2B
5elbaT
DH WD MS .orP satellitesareverysimilartoLandsat(Druschetal.,2012).Theyhavea
| O BC CP FD | FC FM CG G DL | IC W QS SB |     |     |     |     |
| ---------- | ------------- | ---------- | --- | --- | --- | --- |
Sun-synchronousorbitat786kmanda10:30a.m.descendingnode,

168 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
Partial forest cut
Fig.15.OmissionerrorinchangedetectionforCCDC:partialforestcutillustratedbytimeseriesBand5surfacereflectance.
Early change
Fig.16.OmissionerrorinchangedetectionforCCDC:changeoccurredtooearlyillustratedbytimeseriesBand5surfacereflectance.
whichisclosetotheLandsatlocaloverpasstime.The13spectralbands tocombineobservationsfromSentinel2A/2BwithLandsatobservations
spanfromthevisibleandtheNIRtotheSWIRandincludeallsixLandsat intheCCDCalgorithm.WithSentinel2Aplannedforlaunchin2014and
bandsandatsimilarspatialresolution.Thoughtherearesomediffer- thesecond(2B)planedforlaunch18monthlater,therewillbe5days
encesinwidthsandlocationsofthespectralbandsandspatialresolu- repeat time for observations at the Equator and 2–3 days at mid-
tionsbetweenLandsatandSentinel2A/2B(Druschetal.,2012),with latitudes (Berger, Moreno, Johannessen, Levelt, & Hanssen, 2012).
somemodificationsoradjustmentsofthealgorithm,itwillbepossible Moreimportantly,theSentineldatapolicyisfreeandopenaccessto
Fig.17.CommissionerrorinchangedetectionforCCDC:overfittingoftimeseriesmodelillustratedbytimeseriesBand4surfacereflectance.Theredcircleindicatestheincorrect
assignmentofchange.
Fig.18.CommissionerrorinchangedetectionforCCDC:cloudsmissedthreetimesconsecutivelyillustratedbytimeseriesBand2surfacereflectance.Theredcircleindicatestheincorrect
assignmentofchange.

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 169
Fig.19.CommissionerrorinchangedetectionforCCDC:lowtemporalfrequencyofthetimeseriesdataillustratedbytimeseriesBand5surfacereflectance.Theredcircleindicatesthe
incorrectassignmentofchange.
Fig.20.CommissionerrorinchangedetectionforCCDC:smallRMSEillustratedbytimeseriesBand5surfacereflectance.Theredcircleindicatestheincorrectassignmentofchange.
users.Inprinciple,anybodycanaccessacquiredSentineldataandthere observationssuchthatwewillbeabletobegintomonitorchangein
isnodifferencebetweenpublic,commercialandscientificuseandbe- nearreal-timeatLandsatscales.
tween European and non-European users (Aschbacher & Milagro- Byusingallavailableobservationsandconsideringeachpixelsepa-
Pérez,2012).BycombiningcombinedwithLandsat7and8,andtwo rately,theCCDCalgorithmcanovercomelimitationslikethefailureof
Sentinel2Aand2B,therewouldbetypically10highresolutionobserva- theScanLineCorrector(SLC)inLandsat7asthescanlinegapsare
tions per month, greatly improving the availability of Landsat-like treatedlikeclouds,cloudshadows,orsnowandonly the available
Fig.21.TemporalerrorinchangedetectionforCCDC:findingchangelaterthanitisobservedinthereferencedata.Theredcircleisthe“first”changedobservationidentifiedbytheCCDC
algorithmandthegreencircleisthefirsttimethechange(apartialforestcut)canbeobservedincloseexaminationoftheimages.
Fig.22.Clearobservations(Band5)fromJun.toSept.andmodelpredictionsforAug.1steveryyearbetween1984and2011.Forestclearingoccurredin2005forthispixel.

170 Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171
clearobservationsareused.Thisapproachallowsuseofimagesfromall References
timesofyearorthatarepartiallycloudy.Italsocanworkinveryhetero-
geneousareasthatarereportedtobeproblematicforsomemethods
Anderson,J.R.(1976).Alanduseandlandcoverclassificationsystemforusewithremote
sensordata,Vol.964.USGovernmentPrintingOffice.
(Huangetal.,2010;Maseketal.,2008).Moreover,theCCDCalgorithm
Arvidson,T.,Goward,S.,Gasch,J.,&Williams,D.(2006).Landsat-7long-termacquisition
doesnotneedtoperformrelativenormalizationforeachimagelike plan:Developmentandvalidation.PhotogrammetricEngineering&RemoteSensing,
manymethods(Huangetal.,2010;Kennedyetal.,2007),asthetimese- 72(10),1137–1146.
Aschbacher,J.,&Milagro-Pérez,M.P.(2012).TheEuropeanEarthmonitoring(GMES)
riesmodelalreadyincludestheeffectsofphenologyandsunangledif- programme:Statusandperspectives.RemoteSensingofEnvironment,120,3–8.
ferences. By using many observations for model estimation, this Berger,M.,Moreno,J.,Johannessen,J.A.,Levelt,P.F.,&Hanssen,R.F.(2012).ESA'ssenti-
algorithmisnotadverselyaffectedbynoiseandthepredicteddata nelmissionsinsupportofEarthsystemscience.RemoteSensingofEnvironment,120,
84–90.
form a more stable basis for comparison with new observations.
Breiman,L.(2001).Randomforests.MachineLearning,45,5–32.
Fig. 22 illustrates the model-predicted Landsat observations at the Brooks,E.B.,Thomas,V.A.,Wynne,R.H.,&Coulston,J.W.(2012).Fittingthe
sametimeofyearandtheoriginalclearLandsatobservationsduring multitemporalcurve:Afourierseriesapproachtothemissingdataproblemin
growingseason(fromJunetoSeptember)throughtheTMandETM+
remotesensinganalysis.GeoscienceandRemoteSensing,50(9),3340–3353.
Carrao,H.,Goncalves,P.,&Caetano,M.(2008).Contributionofmultispectraland
eraforadeforestationpixel.Itisclearthatthemodelpredictedobserva- multitemporalinformationfromMODISimagestolandcoverclassification.Remote
tionsaremuchmorestablecomparedtotheoriginalobservationsand SensingofEnvironment,112(3),986–997.
thisfeatureshouldsignificantlyreducefalsepositiveerrorsinchange Cohen,W.B.,Yang,Z.,&Kennedy,R.(2010).Detectingtrendsinforestdisturbanceand
recoveryusingyearlyLandsattimeseries:2.TimeSync—Toolsforcalibrationand
detection. validation.RemoteSensingofEnvironment,114(12),2911–2924.
Additionally,landcovermapsfromanytimeperiodinthehistoryof Collins,J.B.,&Woodcock,C.E.(1996).Anassessmentofseverallinearchangedetection
theLandsat4–8eracanbegenerated.Morespecifically,thisalgorithm techniquesformappingforestmortalityusingmultitemporalLandsatTMdata.
canalsogeneratemapsoflandcoverchangeoveranyspecifiedtime
RemoteSensingofEnvironment,56,66–77.
Coppin,P.R.,&Bauer,M.E.(1996).Digitalchangedetectioninforestecosystemswith
periodandprovideinformationaboutthelandcovercategoriesbefore remotesensingimagery.RemoteSensingReviews,13(3–4),207–234.
and afterchange occurs by simply differencing thetwo landcover Coppin,P.,Jonckheere,I.,Nackaerts,K.,Muys,B.,&Lambin,E.(2004).Digitalchange
detectionmethodsinecosystemmonitoring:Areview.InternationalJournalof
mapsgeneratedbyCCDCatdifferenttime.Usually,itisverydangerous RemoteSensing,25(9),1565–1596.
tocomparetwolandcovermapsfromtwodifferenttimetofindchange,
Drusch,M.,DelBello,U.,Carlier,S.,Colin,O.,Fernandez,V.,Gascon,F.,etal.(2012).
astheareasoflandcoverchangearerelativelysmallcomparedtothe Sentinel-2:ESA'sopticalhigh-resolutionmissionforGMESoperationalservices.
magnitudeoferrorsinlandcoverclassificationmaps.Thisalgorithm RemoteSensingofEnvironment,120,25–36.
DuMouchel,W.H.,&O'Brien,F.L.(1989).Integratingarobustoptionintoamultiple
avoids this problem when comparing two land cover maps to find regressioncomputingenvironment.ComputerScienceandStatistics:Proceedings
change, as the land cover classification algorithm is based on the ofthe21stSymposiumontheInterface.Alexandria,VAAmericanStatistical
resultsofchangedetection.Moreover,thisalgorithmcanalsoprovide Association.
Eklundh,L.,Johansson,T.,&Solberg,S.(2009).MappinginsectdefoliationinScotspine
informationaboutinter-annualchangesviathetrendcoefficients.Itis
withMODIStime-seriesdata.RemoteSensingofEnvironment,113(7),1566–1573.
possibletoprovidenewlandcovercategoriesthatareuniquetemporal- Fielding,A.H.,&Bell,A.J.F.(1997).Areviewofmethodsfortheassessmentofprediction
ly,forexample,theforestclasscanbeseparatedintogrowingforest, errorsinconservationpresence/absencemodels.EnvironmentalConservation,24(1),
38–49.
matureforest,anddecliningforest.Thiskindofinformationisimportant Foody,G.M.(2002).Statusoflandcoverclassificationaccuracyassessment.Remote
forthestudyofvegetationhealthconditionsandforcarbonmodeling, SensingofEnvironment,80(1),185–201.
butdifficulttoderivefromtheconventionallandcoverclassification Friedl,M.A.,McIver,D.K.,Hodges,J.C.F.,Zhang,X.Y.,Muchoney,D.,Strahler,A.H.,etal.
(2002).GloballandcovermappingfromMODIS:Algorithmsandearlyresults.
methods. RemoteSensingofEnvironment,83(1),287–302.
TheCCDCalgorithmalsohaslimitations.Firstofall,thisalgorithmis Friedl,M.A.,Menashe,D.S.,Tan,B.,Schneider,A.,Ramankutty,N.,Sibley,A.,etal.(2010).
computationallyexpensiveandneedslotsofdatastorage.Justthesurface MODIScollection5globallandcover:Algorithmrefinementsandcharacterizationof
reflectanceandbrightnesstemperaturedatatakesmorethan500giga-
newdatasets.RemoteSensingofEnvironment,114,168–182.
Fuller,R.M.,Smith,G.M.,&Devereux,B.J.(2003).Thecharacterisationandmeasurement
bytesforatotalof519Landsatimages.Thealgorithmupdatesthetimese- oflandcoverchangethroughremotesensing:Problemsinoperationalapplications?
riesmodeleverytimenewobservationsareavailable,whichhasthe InternationalJournalofAppliedEarthObservationandGeoinformation,4(3),243–253.
benefitofmoreaccuratemodelestimation,butalsogreatlyincreases Galford,G.L.,Mustard,J.F.,Melillo,J.,Gendrin,A.,Cerri,C.C.,&Cerri,C.E.P.(2008).
WaveletanalysisofMODIStimeseriestodetectexpansionandintensificationof
thecomputationalload.Second,thisalgorithmrequireshightemporal row-cropagricultureinBrazil.RemoteSensingofEnvironment,112(2),576–587.
frequencyofclearobservations.Forplacesofpersistentsnoworclouds, Goodwin,N.R.,Coops,N.C.,Wulder,M.A.,Gillanders,Schroeder,T.A.,&Nelson,T.(2008).
themodelestimationmaynotbeaccurateastherearenotenoughobser- EstimationofinsectinfestationdynamicsusingatemporalsequenceofLandsatdata.
RemoteSensingofEnvironment,112,3680–3689.
vationstoestimatethetimeseriesmodel.Forextremecases,ifthereare Gopal,S.,Woodcock,C.E.,&Strahler,A.(1999).Fuzzyneuralclassificationofgloballand
lessthan15clearobservations,theCCDCalgorithmwillnotbeabletoini- coverfroma1degreeAVHRRDataSet.RemoteSensingofEnvironment,67,230–243.
tializethetimeseriesmodel.ForplacesoutsideoftheUnitedStatesthis Guerschman,J.P.,Paruelo,J.M.,Bella,C.D.I.,Giallorenzi,M.C.,&Pacin,F.(2003).Land
coverclassificationintheArgentinePampasusingmulti-temporalLandsatTMdata.
problemwillbemorecommon.Third,weassumethatthesimplesinusoi- InternationalJournalofRemoteSensing,24(17),3381–3402.
dalmodelisabletoestimateallkindsoflandcovertypes,whichmaynot Hansen,M.C.,Defries,R.S.,Townshend,J.R.G.,&Sohlberg,R.(2000).Globallandcover
bevalidforlandcovertypesthathavemoreintra-annualvariation,such classification at 1 km spatial resolution using a classification tree approach.
InternationalJournalofRemoteSensing,21(6&7),1331–1364.
asagriculture.Amorecomplextimeseriesmodelisneededifwewant
Hansen,M.C.,Potapov,P.V.,Moore,R.,Hancher,M.,Turubanova,S.A.,Tyukavina,A.,etal.
toapplyittootherpartsoftheworld.Finally,thoughthedata-driven (2013).High-resolutionglobalmapsof21st-centuryforestcoverchange.Science,
thresholdusedinthisalgorithmisabletohandlemanykindsofland 342(6160),850–853.
Healey,S.P.,Cohen,W.B.,Yang,Z.,&Krankina,O.N.(2005).ComparisonofTasseled
coverchangefortheBostonscene,itmayhaveproblemsforplacesthat
Cap-basedLandsatdatastructureforuseinforestdisturbancedetection.Remote
havelargeinter-annualvariations.Forexamplesemi-aridregionsthatex- SensingofEnvironment,97,301–310.
hibithighvariabilityinthetimingofphenologicalprocessesmayprove Holland,P.W.,&Welsch,R.E.(1977).Robustregressionusingiterativelyreweighted
particularlychallenging,asthedatawillfluctuatemoreatsometimesof least-squares.TheoryandMethods,813–827.
Homer,C.,Huang,C.,Yang,L.,Wylie,B.,&Coan,M.(2004).Developmentofa2001
theyearandatthistimeahigherthresholdisneeded.Thresholdsable nationalland-coverdatabasefortheUnitedStates.PhotogrammetricEngineering&
tochangetemporallymayprovidebetteraccuracy. RemoteSensing,70(7),829–840.
Hostert,P.,Röder,Achim,&Hill,J.(2003).Couplingspectralunmixingandtrendanalysis
formonitoringoflong-termvegetationdynamicsinMediterraneanrangelands.
Acknowledgments RemoteSensingofEnvironment,87,183–197.
Huang,C.,Goward,S.N.,Masek,J.G.,Thomas,N.,Zhu,Z.,&Vogelmann,J.E.(2010).An
We gratefully acknowledge the supports of the USGS Landsat automatedapproachforreconstructingrecentforestdisturbancehistoryusing
denseLandsattimeseriesstacks.RemoteSensingofEnvironment,114,183–198.
ScienceTeamProgramforBetterUseoftheLandsatTemporalDomain:
Jensen,J.R.,Rutchey,K.,Koch,M.S.,&Narumalani(1995).Inlandwetlandchange
MonitoringLandCoverType,Condition,andChange. detectionintheevergladeswaterconservationarea2Ausingatimeseriesof

Z.Zhu,C.E.Woodcock/RemoteSensingofEnvironment144(2014)152–171 171
normalized remotely sensed data. Photogrammetric Engineering & Remote Seto,K.C.,Woodcock,C.E.,Song,C.,Huang,X.,Lu,J.,&Kaufmann,R.K.(2002).Monitor-
Sensing,61(2),199–209. ingland-usechangeinthePearlRiverDeltausingLandsatTM.InternationalJournalof
Jin,S.,&Sader,S.A.(2005).MODIStime-seriesimageryforforestdisturbancedetection RemoteSensing,23(10),1985–2004.
andquantificationofpatchsizeeffects.RemoteSensingofEnvironment,99(4), Singh,A.(1989).ReviewArticleDigitalchangedetectiontechniquesusingremotely-
462–470. senseddata.InternationalJournalofRemoteSensing,10(6),989–1003.
Jung,M.,Henkel,K.,Herold,M.,&Churkina,G.(2006).Exploitingsynergiesofgloballand Street,J.O.,Carroll,R.J.,&Ruppert,D.(1988).Anoteoncomputingrobustregression
coverproductsforcarboncyclemodeling.RemoteSensingofEnvironment,101(4), estimatesviaiterativelyreweightedleastsquares.AmericanStatisticalAssociation,
534–553. 42(2),152–154.
Kennedy,R.E.,Cohen,W.B.,&Schroeder,T.A.(2007).Trajectory-basedchangedetection Tan,B.,Woodcock,C.E.,Hu,J.,Zhang,P.,Ozdogan,M.,Huang,D.,etal.(2006).Theimpact
forautomatedcharacterizationofforestdisturbancedynamics.RemoteSensingof ofgriddingartifactsonthelocalspatialpropertiesofMODISdata:Implicationsfor
Environment,110,370–386. validation,compositing,andband-to-bandregistrationacrossresolution.Remote
Kennedy,R.E.,Yang,Z.,&Cohen,W.B.(2010).Detectingtrendsinforestdisturbanceand SensingofEnvironment,105(2),98–114.
recoveryusingyearlyLandsattimeseries:1.LandTrendr—Temporalsegmentation Tucker,C.J.,Townshend,J.R.G.,&Goff,T.E.(1985).Africanland-coverclassificationusing
algorithms.RemoteSensingofEnvironment,114(12),2897–2910. satellitedata.Science,227(4685),369–375.
Lambin,E.F.,&Strahler,A.H.(1994).Change-vectoranalysisinmultitemporalspace:A Verbesselt,J.,Hyndman,R.,Newnham,G.,&Culvenor,D.(2010).Detectingtrendandsea-
tooltodetectandcategorizeland-coverchangeprocessesusinghightemporal- sonalchangesinsatelliteimagetimeseries.RemoteSensingofEnvironment,114(1),
resolutionsatellitedata.RemoteSensingofEnvironment,48,231–244. 106–115.
Lark,R.M.,&Stafford,J.V.(1997).Classificationasafirststepintheinterpretationof Vermote,E.F.,ElSaleous,N.,Justice,C.O.,Kaufman,Y.J.,Privette,J.L.,etal.(1997).Atmo-
temporalandspatialvariationofcropyield.AnnalsofAppliedBiology,130(1), sphericcorrectionofvisibletomiddle-infraredEOS-MODISdataoverlandsurfaces:
111–121. Background,operationalalgorithm,andvalidation.JournalofGeophysicalResearch,
Loveland,T.R.,Reed,B.C.,Brown,J.F.,Ohlen,D.O.,Zhu,Z.,Yang,L.W.M.J.,&Merchant,J. 102,17131–17141.
W.(2000).DevelopmentofagloballandcovercharacteristicsdatabaseandIGBP Vogelmann,J.E.,Tolk,B.,&Zhu,Z.(2009).Monitoringforestchangesinthesouthwestern
DISCoverfrom1kmAVHRRdata.InternationalJournalofRemoteSensing,21(6–7), UnitedStatesusingmultitemporalLandsatdata.RemoteSensingofEnvironment,113,
1303–1330. 1739–1748.
Lunetta,R.S.,Knight,J.F.,Ediriwickrema,J.,Lyon,J.G.,&Worthy,L.D.(2006).Land-cover Wolter,P.I.,Mladenoft,D.S.,&Crow,T.R.(1995).Improvedforestclassificationinthe
changedetectionusingmulti-temporalMODISNDVIdata.RemoteSensingof northern lake states using multi-temporal Landsat imagery. Photogrammetry
Environment,105(2),142–154. Engineering&RemoteSensing,61(9),1129–1143.
Masek,J.G.,Huang,C.,Wolfe,R.,Cohen,W.,Hall,F.,Kutler,J.,etal.(2008).North Woodcock,C.E.,Allen,R.,Anderson,M.,Belward,A.,Bindschadler,R.,Cohen,W.,etal.
AmericanforestdisturbancemappedfromdecadalLandsatrecord.RemoteSensing (2008).FreeaccesstoLandsatimagery.Science,320(5879),1011.
ofEnvironment,112,2914–2926. Woodcock,C.E.,Macomber,S.A.,Pax-Lenney,M.,&Cohen,W.B.(2001).Largeareamon-
Masek,J.G.,Vermote,E.F.,Saleous,N.,Wolfe,R.,Hall,E.F.,Huemmrich,F.,etal.(2006).A itoringoftemperateforestchangeusingLandsatdata:Generalizationacrosssensors,
LandsatsurfacereflectancedatasetforNorthAmerica,1990–2000.Geoscienceand timeandspace.RemoteSensingofEnvironment,78(1–2),194–203.
RemoteSensingLetters,3,68–72. Woodcock,C.E.,&Strahler,A.H.(1987).Thefactorofscaleinremotesensing.Remote
Melaas,E.K.,Friedl,M.A.,&Zhu,Z.(2013).Detectinginterannualvariationindeciduous SensingofEnvironment,21(3),311–332.
broadleafforestphenologyusingLandsatTM/ETM+data.RemoteSensingof Wulder,M.A.,White,J.C.,Goward,S.N.,Masek,J.G.,Irons,J.R.,Herold,M.,etal.(2008).
Environment,132,176–185. Landsatcontinuity:Issuesandopportunitiesforlandcovermonitoring.Remote
O'Leary,D.P.(1990).Robustregressioncomputationusingiterativelyreweightedleast SensingofEnvironment,112(3),955–969.
squares.SocietyforIndustrialandAppliedMathematics,11(3),466–480. Xin,Q.,Olofsson,P.,Zhu,Z.,Tan,B.,&Woodcock,C.E.(2012).Towardsnearreal-time
Pflugmacher,D.,Cohen,W.B.,&EKennedy,R.(2012).UsingLandsat-deriveddisturbance monitoringofforestdisturbancebyfusionofMODISandLandsatdata.Remote
history(1972–2010)topredictcurrentforeststructure.RemoteSensingof SensingofEnvironment,135,234–247.
Environment,122,146–165. Zhang,Y.,Rossow,W.B.,Lacis,A.A.,Oinas,V.,&Mishchenko,M.I.(2004).Calculationof
Rogan,J.,Bumbarger,N.,Kulakowski,D.,Christman,Z.J.,Runfola,D.M.,&Blanchard,S.D. radiativefluxesfromthesurfacetotopofatmospherebasedonISCCPandother
(2010).Improvingforesttypediscriminationwithmixedlifeformclassesusingfuzzy globaldatasets:Refinementsoftheradiativetransfermodelandtheinputdata.
classificationthresholdsinformedbyfieldobservations.CanadianJournalofRemote JournalofGeophysicalResearch,109(19),19105.
Sensing,36(6),699–708. Zhu,Z.,&Woodcock,C.E.(2012).Object-basedcloudandcloudshadowdetectionin
Rogan,J.,Franklin,J.,&Roberts,D.A.(2002).Acomparisonofmethodsformonitoring Landsatimagery.RemoteSensingofEnvironment,118(15),83–94.
multitemporalvegetationchangeusingThematicMapperimagery.RemoteSensing Zhu,Z.,&Woodcock,C.E.(2014).Automatedcloud,cloudshadow,andsnowdetection
ofEnvironment,80,143–156. basedonmultitemporalLandsatdata:Analgorithmdesignedspecificallyformonitoring
Roy,D.P.,Jin,Y.,Lewis,P.E.,&Justice,C.O.(2005).Prototypingaglobalalgorithmfor surfacechange,submittedtoRemoteSensingofEnvironment.
systematicfire-affectedareamappingusingMODIStimeseriesdata.RemoteSensing Zhu,Z.,Woodcock,C.E.,&Olofsson,P.(2012).Continuousmonitoringofforestdisturbance
ofEnvironment,97(2),137–162. usingallavailableLandsatimagery.RemoteSensingofEnvironment,122,75–91.
Schaaf,C.B.,Gao,F.,Strahler,A.H.,Lucht,W.,Li,X.,Tsang,T.,etal.(2002).Firstoper- Zhu,Z.,Woodcock,C.E.,Rogan,J.,&Kellndorfer,J.(2012).Assessmentofspectral,polarimet-
ationalBRDF,albedonadirreflectanceproductsfromMODIS.RemoteSensingof ric,temporal,andspatialdimensionsforurbanandperi-urbanlandcoverclassification
Environment,83(1),135–148. usingLandsatandSARdata.RemoteSensingofEnvironment,117,72–82.