|     |     |     |     | Conditional |     | Neural |     | Processes |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- |
MartaGarnelo1 DanRosenbaum1 ChrisJ.Maddison1 TiagoRamalho1 DavidSaxton1 MurrayShanahan12
|     |     |     |     | YeeWhyeTeh1 |     | DaniloJ.Rezende1 |     | S.M.AliEslami1 |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
Abstract
|                                           |     |     |     |     |     |     |     |           | y 1 y 2 | y 3 |     | y 4 y 5 | y 6 | …   |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- | --- | ------- | --- | --- |
| Deepneuralnetworksexcelatfunctionapproxi- |     |     |     |     |     |     |     | ataD    a |         |     |     |         |     |     |
|                                           |     |     |     |     |     |     |     |           | f f     | f   |     | f f     | f   |     |
mation,yettheyaretypicallytrainedfromscratch
for each new function. On the other hand, x 1 x 2 x 3 x 4 x 5 x 6 …
| Bayesian                          |         | methods, | such      | as Gaussian | Processes |       |     |                           |              |     |     |         |     |     |
| --------------------------------- | ------- | -------- | --------- | ----------- | --------- | ----- | --- | ------------------------- | ------------ | --- | --- | ------- | --- | --- |
|                                   |         |          |           |             |           |       |     |                           | Observations |     |     | Targets |     |     |
| (GPs),                            | exploit | prior    | knowledge | to          | quickly   | infer |     |                           |              |     |     |         |     |     |
| theshapeofanewfunctionattesttime. |         |          |           |             | YetGPs    |       |     |  gninraeL desivrepuS    b | g            |     |     |         |     |     |
arecomputationallyexpensive,anditcanbehard
|                                          |     |             |         |     |            |     |     |     |     |     |     | y 4 y 5 | y 6 | …   |
| ---------------------------------------- | --- | ----------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
| to design                                |     | appropriate | priors. | In  | this paper | we  |     |     |     |     |     |         |     |     |
| proposeafamilyofneuralmodels,Conditional |     |             |         |     |            |     |     |     | y y | y   |     | g g     | g   |     |
|                                          |     |             |         |     |            |     |     |     | 1 2 | 3   |     |         |     |     |
NeuralProcesses(CNPs),thatcombinethebene-
|             |     |                                 |     |     |     |     |     |     | x x | x   |     | x x | x   | …   |
| ----------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fitsofboth. |     | CNPsareinspiredbytheflexibility |     |     |     |     |     |     | 1 2 | 3   |     | 4 5 | 6   |     |
ofstochasticprocessessuchasGPs,butarestruc-
|     |     |     |     |     |     |     |     |     | Train |     |     | Predict |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------- | --- | --- |
turedasneuralnetworksandtrainedviagradient
| descent. | CNPs | make | accurate | predictions |     | after |     |     | r 1 r 2 | r 3 |     |     |     |     |
| -------- | ---- | ---- | -------- | ----------- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- |
observingonlyahandfuloftrainingdatapoints,
|                                             |     |     |     |     |     |     |     | ledoM ruO    c | h h | h   | a   | y y | y   | …   |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
| yetscaletocomplexfunctionsandlargedatasets. |     |     |     |     |     |     |     |                |     |     |     | 4 5 | 6   |     |
Wedemonstratetheperformanceandversatility
|     |     |     |     |     |     |     |     |     | y y | y   | r   | g g | g   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | 1 2 | 3   |     |     |     |     |
oftheapproachonarangeofcanonicalmachine
learningtasks,includingregression,classification x x x x x x …
|     |     |     |     |     |     |     |     |     | 1 2 | 3   |     | 4 5 | 6   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andimagecompletion.
|     |     |     |     |     |     |     |                     |     | Observe | Aggregate |          | Predict |                  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | --------- | -------- | ------- | ---------------- | --- |
|     |     |     |     |     |     |     | Figure1.Conditional |     |         | Neural    | Process. | a)      | Data description |     |
1.Introduction
b)Trainingregimeofconventionalsuperviseddeeplearningmod-
elsc)Ourmodel.
| Deep neural | networks |          | have    | enjoyed remarkable |          | success    |     |     |     |     |     |     |     |     |
| ----------- | -------- | -------- | ------- | ------------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| in recent   | years,   | but they | require | large              | datasets | for effec- |     |     |     |     |     |     |     |     |
ofthesecanbeframedasfunctionapproximationgivena
| tivetraining(Lakeetal.,2017;Garneloetal.,2016).    |     |     |     |     |     | One |                          |     |     |                     |     |     |     |       |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------- | --- | --- | --- | ----- |
|                                                    |     |     |     |     |     |     | finitesetofobservations. |     |     | Consideradataset{(x |     |     | ,y  | )}n−1 |
| waytomitigatethisdataefficiencyproblemistoapproach |     |     |     |     |     |     |                          |     |     |                     |     |     | i   | i i=0 |
learningintwophases. Thefirstphaselearnsthestatistics ofninputsx ∈X andoutputsy ∈Y. Assumethatthese
|     |     |     |     |     |     |     |                       |     | i   |      | i                      |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ---- | ---------------------- | --- | --- | --- |
|     |     |     |     |     |     |     | representevaluationsy |     |     | =f(x | )ofsomeunknownfunction |     |     |     |
of a generic domain, drawing on a large training set, but i i
withoutcommittingtoaspecificlearningtaskwithinthat f : X → Y,whichmaybefixedorarealizationofsome
|     |     |     |     |     |     |     | randomfunction. |     | Asupervisedlearningalgorithmreturns |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
domain. Thesecondphaselearnsafunctionforaspecific
|     |     |     |     |     |     |     | an approximating |     | function |     | g : X | → Y or | a distribution |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | --- | ----- | ------ | -------------- | --- |
task,butdoessousingonlyasmallnumberofdatapoints
by exploiting the domain-wide statistics already learned. oversuchfunctions. Theaimistominimizealossbetween
f andg ontheentirespaceX,butinpracticetheroutine
Meta-learningwithneuralnetworksisoneexampleofthis
approach(Wangetal.,2016;Reedetal.,2017). is evaluated on a finite set of observations that are held-
|     |     |     |     |     |     |     | out | (making | them effectively |     | unlabelled). |     | We call | these |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | ------------ | --- | ------- | ----- |
Forexample,considersupervisedlearningproblems. Many unlabelleddatapointstargets(seefigure1). Classification,
1DeepMind,London,UK2ImperialCollegeLondon,London, regression,dynamicsmodeling,andimagegenerationcan
allbecastinthisframework.
UK.Correspondenceto:MartaGarnelo<garnelo@google.com>.
|             |        | 35th |               |            |     |            | One | approach | to supervised |     | problems | is to | randomly | ini- |
| ----------- | ------ | ---- | ------------- | ---------- | --- | ---------- | --- | -------- | ------------- | --- | -------- | ----- | -------- | ---- |
| Proceedings | of the |      | International | Conference |     | on Machine |     |          |               |     |          |       |          |      |
tializeaparametricfunctionganewforeachnewtaskand
Learning,Stockholm,Sweden,PMLR80,2018.Copyright2018
spendthebulkofcomputationonacostlyfittingphase.Prior
bytheauthor(s).

ConditionalNeuralProcesses
informationthatapractitionermayhaveaboutf isspecified Bayesianapproaches,theydonotimplementBayesianin-
viathearchitectureofg,thelossfunction,orthetraining ferencedirectlyanditisnotnecessarilytruethatthecondi-
details. This approach encompasses most of deep super- tionaldistributionswillbeconsistentwithrespecttosome
visedlearning. Sincetheextentofpriorknowledgethatcan priorprocess. However,theabilitytoextractpriorknowl-
beexpressedinthiswayisrelativelylimited,andlearning edgedirectlyfromtrainingdatatiedwithscalabilityattest
cannot be shared between different tasks, the amount of timecanbeofequalorgreaterimportance.
trainingrequiredislarge,anddeeplearningmethodstend
| tofailwhentrainingdataisnotplentiful. |     |     |     | 2.Model |     |     |     |
| ------------------------------------- | --- | --- | --- | ------- | --- | --- | --- |
Anotherapproachistotakeaprobabilisticstanceandspec-
2.1.StochasticProcesses
ifyadistributionoverfunctions,knownasstochasticpro-
cesses; Gaussian Processes (GPs) are an example (Ras- Consider a set O = {(x ,y )}n−1 ⊂ X × Y of pairs
i i i=0
mussen&Williams,2004). Onthisview,apractitioner’s x ∈ X y ∈ Y
|     |     |     |     | of inputs | i and outputs | i   | and another set |
| --- | --- | --- | --- | --------- | ------------- | --- | --------------- |
}n+m−1
priorknowledgeaboutf iscapturedinthedistributionalas- T ={x ⊂X ofunlabelledpoints. Wecallthese
|     |     |     |     | i i=n |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
sumptionsaboutthepriorprocessandlearningcorresponds thesetofobservationsandtargets,respectively. Weassume
toBayesianinferenceoverthefunctionalspaceconditioned thattheoutputsarearealizationofthefollowingprocess;let
on the observed values. In the GP example, assumptions P beaprobabilitydistributionoverfunctionsf :X →Y,
onthesmoothnessoff arecapturedaprioriviaaparamet- formallyknownasastochasticprocess1,thenforf ∼ P,
rickernelfunction,andgistakentobearandomfunction sety =f(x ). P definesajointdistributionovertheran-
|     |     |     |     | i   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
distributedaccordingtothepredictiveposteriordistribution. domvariables{f(x )}n+m−1,andthereforeaconditional
i i=0
Unfortunately,suchBayesianapproachesquicklybecome
distributionP(f(T)|O,T);ourtaskistopredicttheoutput
computationallyintractableasthedatasetordimensionality valuesf(x)foreveryx∈T givenO.
grows(Snelson&Ghahramani,2006).
Asamotivatingexample,considerarandom1-dimensional
Inthisworkweproposeafamilyofmodelsthatrepresent function f ∼ P defined on the real line (i.e., X := R,
solutionstothesupervisedproblem,andanend-to-endtrain- Y := R). O wouldconstitutenobservationsoff’svalue
ingapproachtolearningthem,thatcombineneuralnetworks y at different locations x on the real line. Given these
|     |     |     |     | i   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
withfeaturesreminiscentofGaussianProcesses. Wecall observations, we are interested in predicting f’s value at
thisfamilyofmodelsConditionalNeuralProcesses(CNPs),
|     |     |     |     | new locations | on the real line. | A classic | assumption to |
| --- | --- | --- | --- | ------------- | ----------------- | --------- | ------------- |
as an allusion to the fact that they define conditional dis- makeonP isthatallfinitesetsoffunctionevaluationsof
tributionsoverfunctionsgivenasetofobservations. The f are jointly Gaussian distributed. This class of random
dependenceofaCNPontheobservationsisparametrized functionsareknownasGaussianProcesses(GPs). Inthis
byaneuralnetworkthatisinvariantunderpermutationsof case,thepredictivedistributionP(f(T)|O,T)hasasimple
| itsinputs. | WefocusonarchitecturesthatscaleasO(n+m) |     |     |     |     |     |     |
| ---------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
analyticformdefinedbypriorassumptionsonthepairwise
at test time, where n,m are the number of observations correlationstructure(specifiedviaakernelfunction). The
andtargets,respectively. InitsmostbasicformaCNPem- framework of stochastic processes is appealing, because
bedseachobservation, aggregatestheseembeddingsinto Bayesruleallowsonetoreasonconsistentlyaboutthepre-
afurtherembeddingoffixeddimensionwithasymmetric dictivedistributionoverf imposedbyobservingOunder
aggregator,andconditionsthefunctiongontheaggregate asetofprobabilisticassumptions. Thisallowsthemodel
embedding; see Figure 1 for a schematic representation. to be data efficient, an uncommon characteristic in most
CNPsaretrainedbysamplingarandomdatasetandfollow- deeplearningmodels. However,inpractice,itisdifficultto
ingagradientsteptomaximizetheconditionallikelihood
designappropriatepriorsandmostinterestingexamplesof
ofarandomsubsetoftargetsgivenarandomobservation stochasticprocessesarecomputationallyexpensive,scaling
set. ThisencouragesCNPstoperformwellacrossavariety poorly with n and m. This includes GPs which scale as
| ofsettings,i.e.                 | n(cid:28)morn(cid:29)m. |                    |     | O((n+m)3). |     |     |     |
| ------------------------------- | ----------------------- | ------------------ | --- | ---------- | --- | --- | --- |
| Thispaperisstructuredasfollows. |                         | InSection2weintro- |     |            |     |     |     |
2.2.ConditionalNeuralProcesses(CNPs)
duceConditionalNeuralProcesses,proposeourimplemen-
tation,anddescribehowtheycanbetrainedefficientlyusing
|          |                          |            |              | As an alternative | we propose | Conditional | Neural Pro- |
| -------- | ------------------------ | ---------- | ------------ | ----------------- | ---------- | ----------- | ----------- |
| standard | deep learning libraries. | In Section | 3 we discuss |                   |            |             |             |
cesses(CNPs),modelsthatdirectlyparametrizeconditional
relatedwork,particularlyBayesianandmeta-learningap- stochasticprocesseswithoutimposingconsistencywithre-
| proaches. | InSection4weapplyCNPstoseveraldomains, |     |     |     |     |     |     |
| --------- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
1P isameasuretraditionallydefinedastheextensionofaset
includingregression,classificationandimagecompletion,
|           |                    |                         |        | ofconsistentmeasuresonfinitecollectionsoff(x |                                              |     | )forx ∈X. |
| --------- | ------------------ | ----------------------- | ------ | -------------------------------------------- | -------------------------------------------- | --- | --------- |
| comparing | its benefits to    | classical approaches.   | We em- |                                              |                                              |     | i i       |
|           |                    |                         |        | WeoverloadP                                  | forthemarginalandconditionaldensitiesofthese |     |           |
| phasize   | that although CNPs | share some similarities | with   |                                              |                                              |     |           |
measures.

ConditionalNeuralProcesses
specttosomepriorprocess. CNPsparametrizedistributions O = {(x ,y )}N ⊂ O,thefirstN elementsofO. We
|     |     |     |     |     |     |     |     | N   | i i | i=0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
overf(T)givenadistributedrepresentationofOoffixed minimizethenegativeconditionallogprobability
| dimensionality. |     | Bydoingsowegiveupthemathematical |     |     |     |     |     |     |     |                     |     |     |                    |
| --------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------ |
|                 |     |                                  |     |     |     |     |     |     |     | (cid:104) (cid:104) |     |     | (cid:105)(cid:105) |
guaranteesassociatedwithstochasticprocesses,tradingthis L(θ)=−E E logQ ({y }n−1|O ,{x }n−1)
|     |     |     |     |     |     |     |     |     | f∼P | N   | θ i i=0 | N i i=0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- |
offforfunctionalflexibilityandscalability.
(4)
|                                                   |     |     |     |     |     |     |     | Thus,thetargetsitscoresQ |     |     | onincludeboththeobserved |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- |
| Specifically,givenasetofobservationsO,aCNPisacon- |     |     |     |     |     |     |     |                          |     |     | θ                        |     |     |
ditionalstochasticprocessQ thatdefinesdistributionsover andunobservedvalues. Inpractice,wetakeMonteCarlo
θ
|                |     |                                         |                                  |     |     |     |     | estimatesofthegradientofthislossbysamplingf |     |     |     | andN. |     |
| -------------- | --- | --------------------------------------- | -------------------------------- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | ----- | --- |
| f(x)forinputsx |     | ∈                                       | T. θ istherealvectorofallparame- |     |     |     |     |                                             |     |     |     |       |     |
| tersdefiningQ. |     | Inheritingfromthepropertiesofstochastic |                                  |     |     |     |     |                                             |     |     |     |       |     |
Thisapproachshiftstheburdenofimposingpriorknowl-
processes,weassumethatQ θ isinvarianttopermutations edge from an analytic prior to empirical data. This has
| of O and         | T.  | If O(cid:48),T(cid:48) | are permutations |     | of                           | O and | T, re- |                                                    |     |            |                |             |     |
| ---------------- | --- | ---------------------- | ---------------- | --- | ---------------------------- | ----- | ------ | -------------------------------------------------- | --- | ---------- | -------------- | ----------- | --- |
|                  |     |                        |                  |     |                              |       |        | the advantage                                      | of  | liberating | a practitioner | from having | to  |
| spectively,thenQ |     | (f(T)|O,T)             |                  | =   | Q (f(T(cid:48))|O,T(cid:48)) |       | =      |                                                    |     |            |                |             |     |
|                  |     | θ                      |                  |     | θ                            |       |        | specifyananalyticformfortheprior,whichisultimately |     |            |                |             |     |
(f(T)|O(cid:48),T).
Q θ Inthiswork,wegenerallyenforceper- intendedtosummarizetheirempiricalexperience. Still,we
| mutation | invariance |     | with respect | to  | T by assuming |     | a fac- |                   |     |                                   |     |     |     |
| -------- | ---------- | --- | ------------ | --- | ------------- | --- | ------ | ----------------- | --- | --------------------------------- | --- | --- | --- |
|          |            |     |              |     |               |     |        | emphasizethattheQ |     | arenotnecessarilyaconsistentsetof |     |     |     |
|          |            |     |              |     |               | Q   |        |                   |     | θ                                 |     |     |     |
tored structure. Specifically, we consider θ s that factor conditionalsforallobservationsets,andthetrainingroutine
(cid:81)
| Q (f(T)|O,T)= |     |     | Q     | (f(x)|O,x). |     | Intheabsence |     |                       |     |     |            |     |     |
| ------------- | --- | --- | ----- | ----------- | --- | ------------ | --- | --------------------- | --- | --- | ---------- | --- | --- |
| θ             |     |     | x∈T θ |             |     |              |     | doesnotguaranteethat. |     |     | Insummary, |     |     |
ofassumptionsonoutputspaceY,thisistheeasiestwayto
| ensureavalidstochasticprocess. |     |     |     | Still,thisframeworkcan |     |     |     |      |          |             |              |                |     |
| ------------------------------ | --- | --- | --- | ---------------------- | --- | --- | --- | ---- | -------- | ----------- | ------------ | -------------- | --- |
|                                |     |     |     |                        |     |     |     | 1. A | CNP is a | conditional | distribution | over functions |     |
beextendedtonon-factoreddistributions,weconsidersuch
trainedtomodeltheempiricalconditionaldistributions
amodelintheexperimentalsection.
|     |     |     |     |     |     |     |     | offunctionsf |     | ∼P. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
ThedefiningcharacteristicofaCNPisthatitconditionson
Oviaanembeddingoffixeddimensionality. Inmoredetail, 2. ACNPispermutationinvariantinOandT.
weusethefollowingarchitecture,
3. ACNPisscalable,achievingarunningtimecomplex-
r =h (x ,y ) ∀(x ,y )∈O (1) ity of O(n + m) for making m predictions with n
|     |     | i θ | i i | i   | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observations.
|     | r   | =r ⊕r | ⊕...r |         | ⊕r  |     | (2) |                                                    |     |     |     |     |     |
| --- | --- | ----- | ----- | ------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | 1     | 2     | n−1     | n   |     |     |                                                    |     |     |     |     |     |
|     | φ   | =g (x | ,r)   | ∀(x )∈T |     |     | (3) |                                                    |     |     |     |     |     |
|     |     | i θ   | i     | i       |     |     |     | Withinthisspecificationofthemodeltherearestillsome |     |     |     |     |     |
→Rdandg :X×Rd →Reareneural aspectsthatcanbemodifiedtosuitspecificrequirements.
| whereh | θ :X×Y |     |     | θ   |     |     |     |     |     |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theexactimplementationofh,forexample,canbeadapted
networks,⊕isacommutativeoperationthattakeselements
|                                            |     |     |     |     |     |     |     | to the data | type. | For low | dimensional | data the encoder |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | ----------- | ---------------- | --- |
| inRdandmapsthemintoasingleelementofRd,andφ |     |     |     |     |     |     | are |             |       |         |             |                  |     |
i
|                |     |      |       |         |     |        |         | can be implemented |     | as  | an MLP, whereas | for inputs | with |
| -------------- | --- | ---- | ----- | ------- | --- | ------ | ------- | ------------------ | --- | --- | --------------- | ---------- | ---- |
| parametersforQ |     | (f(x | )|O,x | )=Q(f(x |     | )|φ ). | Depend- |                    |     |     |                 |            |      |
θ i i i i largerdimensionsandspatialcorrelationsitcanalsoinclude
ingonthetaskthemodellearnstoparametrizeadifferent
convolutions.Finally,inthesetupdescribedthemodelisnot
| outputdistribution. |     | Thisarchitectureensurespermutation |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
abletoproduceanycoherentsamples,asitlearnstomodel
invarianceandO(n+m)scalingforconditionalprediction.
|                   |        |     |                                    |                     |     |     |     | only a factored | prediction |            | of the mean | and the variances, |      |
| ----------------- | ------ | --- | ---------------------------------- | ------------------- | --- | --- | --- | --------------- | ---------- | ---------- | ----------- | ------------------ | ---- |
| Wenotethat,sincer |        |     | ⊕...⊕r                             | canbecomputedinO(1) |     |     |     |                 |            |            |             |                    |      |
|                   |        | 1   |                                    | n                   |     |     |     |                 |            |            |             |                    |      |
|                   |        |     |                                    |                     |     |     |     | disregarding    | the        | covariance | between     | target points.     | This |
| fromr             | ⊕...⊕r |     | ,thisarchitecturesupportsstreaming |                     |     |     |     |                 |            |            |             |                    |      |
1 n−1 is a result of this particular implementation of the model.
observationswithminimaloverhead.
Onewaywecanobtaincoherentsamplesisbyintroducing
Forregressiontasksweuseφ toparametrizethemeanand a latent variable that we can sample from. We carry out
i
varianceφ =(µ ,σ 2)ofaGaussiandistributionN(µ ,σ 2) some proof-of-concept experiments on such a model in
|                                   | i   | i i                        |     |     |                    |                | i i |               |     |     |     |     |     |
| --------------------------------- | --- | -------------------------- | --- | --- | ------------------ | -------------- | --- | ------------- | --- | --- | --- | --- | --- |
| foreveryx                         | i ∈ | T. Forclassificationtasksφ |     |     |                    | i parametrizes |     | section4.2.3. |     |     |     |     |     |
| thelogitsoftheclassprobabilitiesp |     |                            |     |     | overthecclassesofa |                |     |               |     |     |     |     |     |
c
| categoricaldistribution. |     |     | Inmostofourexperimentswetake |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.Relatedresearch
| a 1 ⊕...⊕a | n   | tobethemeanoperation(a |     |     | 1   | +...+a | n )/n. |     |     |     |     |     |     |
| ---------- | --- | ---------------------- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
3.1.GaussianProcesses
2.3.TrainingCNPs
|     |     |     |     |     |     |     |     | The goal | of our | research | is to incorporate | ideas from | GP  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ----------------- | ---------- | --- |
WetrainQ byaskingittopredictOconditionedonaran- inference into a NN training regime to overcome certain
θ
domlychosensubsetofO. Thisgivesthemodelasignal drawbacksofboth. Thereareanumberofpapersthatad-
of the uncertainty over the space X inherent in the dis- dress some of the same issues within the GP framework.
tribution P given a set of observations. More precisely, Scaling issues with GPs have been addressed by sparse
let f ∼ P, O = {(x ,y )}n−1 be a set of observations, GPs(Snelson&Ghahramani,2006),whileovercomingthe
|     |     |     | i i i=0 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N ∼ uniform[0,...,n−1]. We condition on the subset limitedexpressivityresultingfromfunctionalrestrictions

ConditionalNeuralProcesses
is the motivation for Deep GPs (Damianou & Lawrence, othergenerativemodelstheneuralstatisticianlearnstoesti-
2013;Salimbeni&Deisenroth,2017). TheauthorsofDeep matethedensityoftheobserveddatabutdoesnotallowfor
Kernellearning(Wilsonetal.,2016),alsocombineideas targetedsamplingatwhatwehavebeenreferringtoasinput
fromDLandGPs. Theirmodel,however,remainscloserto positionsx . Instead,onecanonlygeneratei.i.d. samples
i
GPsastheneuralnetworkisusedtolearnmoreexpressive from the estimated density. Finally, the latent variant of
kernelsthatarethenusedwithinaGP. CNPcanalsobeseenasanapproximatedamortizedversion
ofBayesianDL(Gal&Ghahramani,2016;Blundelletal.,
3.2.Meta-Learning 2015;Louizosetal.,2017;Louizos&Welling,2017)
Deeplearningmodelsaregenerallymorescalableandare
4.ExperimentalResults
| very successful                     | at learning | features and                 | prior knowledge |     |     |     |     |     |
| ----------------------------------- | ----------- | ---------------------------- | --------------- | --- | --- | --- | --- | --- |
| fromthedatadirectly.                |             | Howevertheytendtobelessflex- |                 |     |     |     |     |     |
| iblewithregardstoinputsizeandorder. |             |                              | Additionally,in |     |     |     |     |     |
generaltheyonlyapproximateonefunctionasopposedto
| distributionsoverfunctions. |                  | Meta-learningapproachesad- |                |     |     |     |     |     |
| --------------------------- | ---------------- | -------------------------- | -------------- | --- | --- | --- | --- | --- |
| dress the                   | latter and share | our core motivations.      | Recently       |     |     |     |     |     |
| meta-learning               | has been         | applied to a wide          | range of tasks |     |     |     |     |     |
likeRL(Wangetal.,2016;Finnetal.,2017)orprogram
induction(Devlinetal.,2017).
Oftenmeta-learningalgorithmsareimplementedasdeep
generativemodelsthatlearntodofew-shotestimationsof
| theunderlyingdensityofthedata. |     | Onewayofachieving |     |     |     |     |     |     |
| ------------------------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- |
thisisbyupdatingexistingmodelslikePixelCNN(vanden
Oordetal.,2016)andaugmentingthemwithattentionmech-
anisms(Reedetal.,2017)orincludingamemoryunitina
| VAEmodel(Bornscheinetal.,2017). |     | Anothersuccessful |     |     |     |     |     |     |
| ------------------------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
latentvariableapproachistoexplicitlyconditiononsome
| contextduringinference(J.Rezendeetal.,2016). |     |     | Given |     |     |     |     |     |
| -------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
thegenerativenatureofthesemodelstheyareusuallyap-
pliedtoimagegenerationtasks,butmodelsthatincludea
conditioningclass-variablecanbeusedforclassificationas
well.
| Classification | itself is               | another common | task in meta- |     |     |     |     |     |
| -------------- | ----------------------- | -------------- | ------------- | --- | --- | --- | --- | --- |
| learning.      | Few-shot classification | algorithms     | usually rely  |     |     |     |     |     |
onsomedistancemetricinfeaturespacetocomparetarget
| images to            | the observations | provided (Koch                 | et al., 2015), |     |     |     |     |     |
| -------------------- | ---------------- | ------------------------------ | -------------- | --- | --- | --- | --- | --- |
| (Santoroetal.,2016). |                  | Matchingnetworks(Vinyalsetal., |                |     |     |     |     |     |
2016;Bartunov&Vetrov,2016)arecloselyrelatedtoCNPs.
Intheircasefeaturesofsamplesarecomparedwithtarget
featuresusinganattentionkernel. Atahigherlevelonecan Figure2.1-D Regression. Regression results on a 1-D curve
interpretthismodelasaCNPwheretheaggregatorisjust (blackline)using5(leftcolumn)and50(rightcolumn)context
theconcatenationoverallinputsamplesandthedecoderg points(blackdots). Thefirsttworowsshowthepredictedmean
andvariancefortheregressionofasingleunderlyingkernelfor
| containsanexplicitlydefineddistancekernel. |     |     | Inthissense |     |     |     |     |     |
| ------------------------------------------ | --- | --- | ----------- | --- | --- | --- | --- | --- |
GPs(red)andCNPs(blue).Thebottomrowshowsthepredictions
matchingnetworksareclosertoGPsthantoCNPs,since
ofCNPsforacurvewithswitchingkernelparameters.
theyrequirethespecificationofadistancekernelthatCNPs
learnfromthedatainstead.Inaddition,asMNscarryoutall-
to-allcomparisonstheyscalewithO(n×m),althoughthey
4.1.FunctionRegression
canbemodifiedtohavethesamecomplexityofO(n+m)
AsafirstexperimentwetestCNPontheclassical1Dre-
asCNPs(Snelletal.,2017).
|     |     |     |     | gression | task that is used | as a common | baseline | for GPs. |
| --- | --- | --- | --- | -------- | ----------------- | ----------- | -------- | -------- |
AmodelthatisconceptuallyverysimilartoCNPs(andin Wegeneratetwodifferentdatasetsthatconsistoffunctions
particularthelatentvariableversion)isthe“neuralstatis-
|     |     |     |     | generatedfromaGPwithanexponentialkernel. |     |     | Inthefirst |     |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | ---------- | --- |
tician” paper (Edwards & Storkey, 2016) and the related dataset we use a kernel with fixed parameters, and in the
variationalhomoencoder(Hewittetal.,2018). Aswiththe seconddatasetthefunctionswitchesatsomerandompoint

ConditionalNeuralProcesses
Figure3.Pixel-wiseimageregressiononMNIST.Left:Twoexamplesofimageregressionwithvaryingnumbersofobservations.We
providethemodelwith1,40,200and728contextpoints(toprow)andquerytheentireimage.Theresultingmean(middlerow)and
variance(bottomrow)ateachpixelpositionisshownforeachofthecontextimages.Right:modelaccuracywithincreasingnumberof
observationsthatareeitherchosenatrandom(blue)orbyselectingthepixelwiththehighestvariance(red).
onthereallinebetweentwofunctionseachsampledwith 4.2.ImageCompletion
differentkernelparameters.
|     |     | We consider | image | completion | as a | regression task | over |
| --- | --- | ----------- | ----- | ---------- | ---- | --------------- | ---- |
AteverytrainingstepwesampleacurvefromtheGP,select functionsineitherf :[0,1]2 →[0,1]forgrayscaleimages,
|     |     | :[0,1]2 | →[0,1]3forRGBimages. |     |     |     |     |
| --- | --- | ------- | -------------------- | --- | --- | --- | --- |
asubsetofnpoints(x i ,y i )asobservations,andasubsetof orf Theinputxisthe
points(x ,y )astargetpoints. Usingthemodeldescribed 2Dpixelcoordinatesnormalizedto[0,1]2,andtheoutput
t t
| inFigure1,theobservedpointsareencodedusingathree |     | y            |           |           |     |               |     |
| ------------------------------------------------ | --- | ------------ | --------- | --------- | --- | ------------- | --- |
|                                                  |     | is eitherthe | grayscale | intensity | or  | avectorof the | RGB |
layerMLP encoderhwitha 128 dimensionaloutput rep- intensitiesofthecorrespondingpixel. Forthiscompletion
resentation r . The representations are aggregated into a taskweuseexactlythesamemodelarchitectureasfor1D
i
1 (cid:80)
single representation r = r i which is concatenated functionregression(withtheexceptionofmakingthelast
n
to x and passed to a decoder g consisting of a five layer layer3-dimensionalforRGB).
t
MLP.ThedecoderoutputsaGaussianmeanandvariance
|                        |                             | WetestCNPontwodifferentdatasets: |     |     |     | theMNISThand- |     |
| ---------------------- | --------------------------- | -------------------------------- | --- | --- | --- | ------------- | --- |
| forthetargetoutputsyˆ. | t Wetrainthemodeltomaximize |                                  |     |     |     |               |     |
writtendigitdatabase(LeCunetal.,1998)andlarge-scale
thelog-likelihoodofthetargetpointsusingtheAdamopti-
CelebFacesAttributes(CelebA)dataset(Liuetal.,2015).
mizer(Kingma&Ba,2014).
|     |     | Themodelandtrainingprocedurearethesameforboth: |     |     |     |     | at  |
| --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
Twoexamplesoftheregressionresultsobtainedforeach eachstepweselectanimagefromthedatasetandpicka
of the datasets are shown in Figure 2. We compare the subsetofthepixelsasobservations. Conditionedonthese,
modeltothepredictionsgeneratedbyaGPwiththecorrect themodelistrainedtopredictthevaluesofallthepixelsin
hyperparameters,whichconstitutesanupperboundonour theimage(includingtheonesithasbeenconditionedon).
performance. AlthoughthepredictiongeneratedbytheGP Likein1Dregression,themodeloutputsaGaussianmean
is smoother than the CNP’s prediction both for the mean andvarianceforeachpixelandisoptimizedwithrespect
andvariance,themodelisabletolearntoregressfromafew
|     |     | to the log-likelihood |     | of the | ground-truth | image. | It is im- |
| --- | --- | --------------------- | --- | ------ | ------------ | ------ | --------- |
contextpointsforboththefixedkernelsandswitchingker- portanttopointoutthatwechooseimagesasourdataset
nels. Asthenumberofcontextpointsgrows,theaccuracy becausetheyconstituteacomplex2-Dfunctionthatiseasy
of the model improves and the approximated uncertainty toevaluatevisually, nottocomparetogenerativemodels
| ofthemodeldecreases. | Crucially,weseethemodellearns | benchmarks. |     |     |     |     |     |
| -------------------- | ----------------------------- | ----------- | --- | --- | --- | --- | --- |
toestimateitsownuncertaintygiventheobservationsvery
| accurately. Nonethelessitprovidesagoodapproximation |     | 4.2.1.MNIST |     |     |     |     |     |
| --------------------------------------------------- | --- | ----------- | --- | --- | --- | --- | --- |
thatincreasesinaccuracyasthenumberofcontextpoints
|     |     | We first | test CNP | on the MNIST | dataset | and use | the test |
| --- | --- | -------- | -------- | ------------ | ------- | ------- | -------- |
increases.
|     |     | settoevaluateitsperformance. |     |     | AsshowninFigure3athe |     |     |
| --- | --- | ---------------------------- | --- | --- | -------------------- | --- | --- |
Furthermorethemodelachievessimilarlygoodperformance model learns to make good predictions of the underlying
ontheswitchingkerneltask. Thistypeofregressiontask digitevenforasmallnumberofcontextpoints. Crucially,
isnottrivialforGPswhereasinourcaseweonlyhaveto whenconditionedonlyononenon-informativecontextpoint
changethedatasetusedfortraining.
(e.g. ablackpixelontheedge)themodel’spredictioncorre-
|     |     | spondstotheaverageoverallMNISTdigits. |     |     |     | Asthenumber |     |
| --- | --- | ------------------------------------- | --- | --- | --- | ----------- | --- |

ConditionalNeuralProcesses
| of context                         | points increases | the predictions | become           | more |     |     |     |     |     |
| ---------------------------------- | ---------------- | --------------- | ---------------- | ---- | --- | --- | --- | --- | --- |
| similartotheunderlyinggroundtruth. |                  |                 | Thisdemonstrates |      |     |     |     |     |     |
themodel’scapacitytoextractdatasetspecificpriorknowl-
edge. Itisworthmentioningthatevenwithacompleteset
| of observations | the model | does not achieve | pixel-perfect |     |     |     |     |     |     |
| --------------- | --------- | ---------------- | ------------- | --- | --- | --- | --- | --- | --- |
reconstruction,aswehaveabottleneckattherepresentation
level.
SincethisimplementationofCNPreturnsfactoredoutputs,
| the best prediction | it can | produce given | limited | context |     |     |     |     |     |
| ------------------- | ------ | ------------- | ------- | ------- | --- | --- | --- | --- | --- |
informationistoaverageoverallpossiblepredictionsthat
| agree with | the context. | An alternative | to this | is to add |     |     |     |     |     |
| ---------- | ------------ | -------------- | ------- | --------- | --- | --- | --- | --- | --- |
latentvariablesinthemodelsuchthattheycanbesampled
conditionedonthecontexttoproducepredictionswithhigh
| probabilityinthedatadistribution. |     | Weconsiderthismodel |     |     |     |     |     |     |     |
| --------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Figure5.Flexibleimagecompletion.Incontrasttostandardcon-
laterinsection4.2.3.
ditionalmodels,CNPscanbedirectlyconditionedonobserved
Animportantaspectofthemodelisitsabilitytoestimate
pixelsinarbitrarypatterns,evenoneswhichwereneverseenin
| theuncertaintyoftheprediction. |     | Asshowninthebottom |     |     |     |     |     |     |     |
| ------------------------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
thetrainingset.Similarly,themodelcanpredictvaluesforpixel
rowofFigure3a,asweaddmoreobservations,thevariance coordinatesthatwereneverincludedinthetrainingset,likesub-
shifts from being almost uniformly spread over the digit pixelvaluesindifferentresolutions.Thedottedwhitelineswere
addedforclarityaftergeneration.
positionstobeinglocalizedaroundareasthatarespecific
| totheunderlyingdigit,specificallyitsedges. |     |     | Beingableto |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
modeltheuncertaintygivensomecontextcanbehelpfulfor
4.2.2.CELEBA
| manytasks.                         | Oneexampleisactiveexploration,wherethe |     |              |     |         |              |                   |           |     |
| ---------------------------------- | -------------------------------------- | --- | ------------ | --- | ------- | ------------ | ----------------- | --------- | --- |
| modelhasachoiceoverwheretoobserve. |                                        |     | Wetestthisby |     |         |              |                   |           |     |
|                                    |                                        |     |              |     | We also | apply CNP to | CelebA, a dataset | of images | of  |
comparingthepredictionsofCNPwhentheobservations
|     |     |     |     |     | celebrity | faces, and report | performance | obtained | on the |
| --- | --- | --- | --- | --- | --------- | ----------------- | ----------- | -------- | ------ |
arechosenaccordingtouncertainty(i.e.thepixelwiththe
|     |     |     |     |     | testset. AsshowninFigure4ourmodelisabletocapture |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
highestvarianceateachstep),versusrandompixels(Fig-
|     |     |     |     |     | the complex | shapes and | colours of this | dataset with | pre- |
| --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | ------------ | ---- |
ure3b). Thismethodisaverysimplewayofdoingactive
dictionsconditionedonlessthan10%ofthepixelsbeing
exploration,butitalreadyproducesbetterpredictionresults
|     |     |     |     |     | alreadyclosetogroundtruth. |     | Asbefore,givenfewcontext |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | ------------------------ | --- | --- |
thanselectingtheconditioningpointsatrandom. points the model averages over all possible faces, but as
thenumberofcontextpairsincreasesthepredictionscap-
tureimage-specificdetailslikefaceorientationandfacial
|     |     |     |     |     | expression. | Furthermore,asthenumberofcontextpoints |                 |           |        |
| --- | --- | --- | --- | --- | ----------- | -------------------------------------- | --------------- | --------- | ------ |
|     |     |     |     |     | increases   | the variance is                        | shifted towards | the edges | in the |
image.
AnimportantaspectofCNPsdemonstratedinFigure5,is
|     |     |     |     |     | its flexibility | not only in | the number | of observations | and |
| --- | --- | --- | --- | --- | --------------- | ----------- | ---------- | --------------- | --- |
targetsitreceivesbutalsowithregardstotheirinputvalues.
ItisinterestingtocomparethispropertytoGPsononehand,
andtotrainedgenerativemodels(vandenOordetal.,2016;
Gregoretal.,2015)ontheotherhand.
Thefirsttypeofflexibilitycanbeseenwhenconditioningon
subsetsthatthemodelhasnotencounteredduringtraining.
Considerconditioningthemodelononehalfoftheimage,
|     |     |     |     |     | foxexample. | Thisforcesthemodeltonotonlypredictpixel |     |     |     |
| --- | --- | --- | --- | --- | ----------- | --------------------------------------- | --- | --- | --- |
Figure4.Pixel-wise image completion on CelebA. Two exam- valuesaccordingtosomestationarysmoothnesspropertyof
theimages,butalsoaccordingtoglobalspatialproperties,
plesofCelebAimageregressionwithvaryingnumbersofobser-
vations.Weprovidethemodelwith1,10,100and1000context e.g. symmetryandtherelativelocationofdifferentpartsof
points(toprow)andquerytheentireimage.Theresultingmean faces.Asseeninthefirstrowofthefigure,CNPsareableto
(middlerow)andvariance(bottomrow)ateachpixelpositionis
|     |     |     |     |     | capturethoseproperties. |     | AGPwithastationarykernelcan- |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | ---------------------------- | --- | --- |
shownforeachofthecontextimages.
notcapturethis,andintheabsenceofobservationswould
reverttoitsmean(themeanitselfcanbenon-stationarybut

ConditionalNeuralProcesses
capturetheuncertainty,thisfactoredmodelpreventsusfrom
obtainingcoherentsamplesovermultipletargets.
ConsidertheMNISTexperimentinFigure3,conditioned
|     |     |     |     | onasmallnumberofobservations. |     |     | Ratherthanpredicting |     |
| --- | --- | --- | --- | ----------------------------- | --- | --- | -------------------- | --- |
onlythemeanofalldigits,sometimesweneedamodelthat
canbeusedtosampledifferentcoherentimagesofallthe
possibledigitsconditionedontheobservations.
GPscandothisbecausetheycontainaparametrickernel
predictingthecovariancebetweenallthepointsintheob-
|                                                  |     |     |     | servationsandtargets.                  |     | ThisformsamultivariateGaussian |     |           |
| ------------------------------------------------ | --- | --- | --- | -------------------------------------- | --- | ------------------------------ | --- | --------- |
|                                                  |     |     |     | whichcanbeusedtocoherentlydrawsamples. |     |                                |     | Inorderto |
| Figure6.Imagecompletionwithalatentvariablemodel. |     |     | The |                                        |     |                                |     |           |
maintainthispropertyinatrainedmodel,oneapproachisto
latentvariablescapturetheglobaluncertainty,allowingthesam- trainthemodeltopredictaGPkernel(Wilsonetal.,2016).
plingofdifferentcoherentimageswhichconformtotheobser- Howeverthedifficultyistheneedtoback-propagatethrough
vations. Asthenumberofobservationsincreases,uncertaintyis
|     |     |     |     | the sampling | which involves | a   | large matrix | inversion (or |
| --- | --- | --- | --- | ------------ | -------------- | --- | ------------ | ------------- |
reducedandthesamplesconvergetoasingleestimate.
someapproximationofit).
|     |     |     |     |     | RandomContext |     | OrderedContext |     |
| --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- |
usuallythiswouldnotbeenoughtocapturetheinteresting
| properties). |     |     |     | #   | 10 100      | 1000  | 10    | 100 1000    |
| ------------ | --- | --- | --- | --- | ----------- | ----- | ----- | ----------- |
|              |     |     |     | kNN | 0.215 0.052 | 0.007 | 0.370 | 0.273 0.007 |
Inaddition,themodelisflexiblewithregardstothetarget
input values. This means, e.g., we can query the model GP 0.247 0.137 0.001 0.257 0.220 0.002
|                |                 |                  |           | CNP | 0.039 0.016 | 0.009 | 0.057 | 0.047 0.021 |
| -------------- | --------------- | ---------------- | --------- | --- | ----------- | ----- | ----- | ----------- |
| at resolutions | it has not seen | during training. | We take a |     |             |       |       |             |
modelthathasonlybeentrainedusingpixelcoordinatesof
aspecificresolution,andpredictattesttimesubpixelvalues
Table1.Pixel-wisemeansquarederrorforallofthepixelsinthe
fortargetsbetweentheoriginalcoordinates. Asshownin image completion task on the CelebA data set with increasing
Figure5,withoneforwardpasswecanquerythemodelat numberofcontextpoints(10,100,1000).Thecontextpointsare
choseneitheratrandomororderedfromthetop-leftcornertothe
| differentresolutions. | WhileGPsalsoexhibitthistypeof |     |     |     |     |     |     |     |
| --------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
flexibility,itisnotthecasefortrainedgenerativemodels, bottom-right.WithfewercontextpointsCNPsoutperformkNNs
whichcanonlypredictvaluesforthepixelcoordinateson andGPs.InadditionCNPsperformwellregardlessoftheorderof
thecontextpoints,whereasGPsandkNNsperformworsewhen
whichtheyweretrained.Inthissense,CNPscapturethebest
thecontextisordered.
ofbothworlds–itisflexibleinregardstotheconditioning
andpredictiontask,andhasthecapacitytoextractdomain
knowledgefromatrainingset.
|     |     |     |     | In contrast, | the approach | we use | is to | simply add latent |
| --- | --- | --- | --- | ------------ | ------------ | ------ | ----- | ----------------- |
We compare CNPs quantitatively to two related models: variablesztoourdecoderg,allowingourmodeltocapture
kNNsandGPs. AsshowninTable4.2.3CNPsoutperform global uncertainty. In order to generate a coherent sam-
thelatterwhennumberofcontextpointsissmall(empiri- ple,wecomputetherepresentationrfromtheobservations,
callywhenhalfoftheimageorlessisprovidedascontext). whichparametrizesaGaussiandistributionoverthelatentsz.
Whenthemajorityoftheimageisgivenascontextexact zisthensampledonceandusedtogeneratethepredictions
| methodslikeGPsandkNNwillperformbetter. |     |     | Fromtheta- |                |                                      |     |     |     |
| -------------------------------------- | --- | --- | ---------- | -------------- | ------------------------------------ | --- | --- | --- |
|                                        |     |     |            | foralltargets. | Togetadifferentcoherentsamplewedrawa |     |     |     |
blewecanalsoseethattheorderinwhichthecontextpoints newsamplefromthelatentszandrunthedecoderagainfor
areprovidedislessimportantforCNPs,sinceprovidingthe alltargets. SimilartothestandardVAE(Kingma&Welling,
context points in order from top to bottom still results in 2013;Rezendeetal.,2014)wetrainthismodelbyoptimiz-
goodperformance. BothinsightspointtothefactthatCNPs ingavariationallowerboundofthelog-likelihood,using
learnadata-specific‘prior’thatwillgenerategoodsamples aconditionalGaussianpriorp(z|O)thatisconditionedon
evenwhenthenumberofcontextpointsisverysmall. theobservations,andaGaussianposteriorp(z|O,T)thatis
alsoconditionedonthetargetpoints.
4.2.3.LATENTVARIABLEMODEL
|     |     |     |     | We apply | this model | to MNIST | and CelebA | (Figure 6). |
| --- | --- | --- | --- | -------- | ---------- | -------- | ---------- | ----------- |
Themainmodelweusethroughoutthispaperisafactored Weusethesamemodelsasbefore,butweconcatenatethe
model that predicts the mean and variance of the target representationrtoavectoroflatentvariableszofsize64
outputs. Althoughwehaveshownthatthemeanisbyitself (forCelebAweusebiggermodelswherethesizesofrand
ausefulprediction,andthatthevarianceisagoodwayto z are 1024 and 128 respectively). For both the prior and

ConditionalNeuralProcesses
posteriormodels,weusethreelayeredMLPsandaverage 5-wayAcc 20-wayAcc
Runtime
| theiroutputs. | Weemphasizethatthedifferencebetweenthe |     |     |     |     |     |        |               |        |     |
| ------------- | -------------------------------------- | --- | --- | --- | --- | --- | ------ | ------------- | ------ | --- |
|               |                                        |     |     |     |     |     | 1-shot | 5-shot 1-shot | 5-shot |     |
priorandposterioristhattheprioronlyseestheobserved
pixels,whiletheposteriorseesboththeobservedandthe MANN 82.8% 94.9% - - O(nm)
targetpixels. Whensamplingfromthismodelwithasmall MN 98.1% 98.9% 93.8% 98.5%
O(nm)
|     |     |     |     |     |     |     | 95.3% | 98.5% 89.9% | 96.8% |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ----- | --- |
number of observed pixels, we get coherent samples and CNP O(n+m)
| we see that | thevariability | of the | datasets | is captured. | As  |     |     |     |     |     |
| ----------- | -------------- | ------ | -------- | ------------ | --- | --- | --- | --- | --- | --- |
themodelisconditionedonmoreandmoreobservations, Table2.ClassificationresultsonOmniglot.Resultsonthesame
the variability of the samples drops and they eventually taskforMANN(Santoroetal.,2016), andmatchingnetworks
convergetoasinglepossibility.
(MN)(Vinyalsetal.,2016)andCNP.
4.3.Classification
tionsarethenconcatenatedtoformthefinalrepresentation.
Finally,weapplythemodeltoone-shotclassificationusing
Giventhatboththesizeoftheclass-specificrepresentations
theOmniglotdataset(Lakeetal.,2015)(seeFigure7foran and the number of classes are constant, the size of the fi-
overviewofthetask). Thisdatasetconsistsof1,623classes nalrepresentationisstillconstantandthustheO(n+m)
| ofcharactersfrom50differentalphabets. |     |     |     | Eachclasshas |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
runtimestillholds.
| only 20 | examples and | as such | this dataset | is particularly |     |     |     |     |     |     |
| ------- | ------------ | ------- | ------------ | --------------- | --- | --- | --- | --- | --- | --- |
TheresultsoftheclassificationaresummarizedinTable2.
| suitableforfew-shotlearningalgorithms. |     |     |     | Asin(Vinyals |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
et al., 2016) we use 1,200 randomly selected classes as CNPsachievehigheraccuracythanmodelsthataresignif-
icantlymorecomplex(likeMANN).WhileCNPsdonot
| our training | set and the | remainder | as our | testing data | set. |     |     |     |     |     |
| ------------ | ----------- | --------- | ------ | ------------ | ---- | --- | --- | --- | --- | --- |
Inadditionweaugmentthedatasetfollowingtheprotocol beatstateoftheartforone-shotclassificationouraccuracy
|                                 |     |     |                      |     |     | values are            | comparable. | Crucially,           | we reach | those values |
| ------------------------------- | --- | --- | -------------------- | --- | --- | --------------------- | ----------- | -------------------- | -------- | ------------ |
| describedin(Santoroetal.,2016). |     |     | Thisincludescropping |     |     |                       |             |                      |          |              |
|                                 |     |     |                      |     |     | using a significantly |             | simpler architecture | (three   | convolu-     |
theimagefrom32×32to28×28,applyingsmallrandom
translationsandrotationstotheinputs,andalsoincreasing tionallayersfortheencoderandathree-layerMLPforthe
decoder)andwithalowerruntimeofO(n+m)attesttime
| the number | of classes | by rotating | every | character | by 90 |     |     |     |     |     |
| ---------- | ---------- | ----------- | ----- | --------- | ----- | --- | --- | --- | --- | --- |
asopposedtoO(nm).
| degreesanddefiningthattobeanewclass. |     |     |     | Wegenerate |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
thelabelsforanN-wayclassificationtaskbychoosingN
| randomclassesateachtrainingstepandarbitrarilyassigning |           |     |     |     |     | 5.Discussion |     |     |     |     |
| ------------------------------------------------------ | --------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| thelabels0,...,N                                       | −1toeach. |     |     |     |     |              |     |     |     |     |
InthispaperwehaveintroducedConditionalNeuralPro-
cesses,amodelthatisbothflexibleattesttimeandhasthe
|     |     |     |     |     |     | capacitytoextractpriorknowledgefromtrainingdata. |     |     |     | We  |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
havedemonstrateditsabilitytoperformavarietyoftasks
includingregression,classificationandimagecompletion.
WecomparedCNPstoGaussianProcessesononehand,and
deeplearningmethodsontheother,andalsodiscussedthe
relationtometa-learningandfew-shotlearning.
ItisimportanttonotethatthespecificCNPimplementations
|     |     |     |     |     |     | described here | are just | simple proofs-of-concept |     | and can |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | ------------------------ | --- | ------- |
besubstantiallyextended,e.g.byincludingmoreelaborate
architecturesinlinewithmoderndeeplearningadvances.
Tosummarize,thisworkcanbeseenasasteptowardslearn-
Figure7.One-shot Omniglot classification. At test time the inghigh-levelabstractions,oneofthegrandchallengesof
modelispresentedwithalabelledexampleforeachclass, and contemporarymachinelearning. Functionslearnedbymost
outputstheclassificationprobabilitiesofanewunlabelledexample. conventionaldeeplearningmodelsaretiedtoaspecific,con-
Themodeluncertaintygrowswhenthenewexamplecomesfrom
|     |     |     |     |     |     | strainedstatisticalcontextatanystageoftraining. |     |     |     | Atrained |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | -------- |
anun-observedclass.
CNPismoregeneral,inthatitencapsulatesthehigh-level
|     |     |     |     |     |     | statisticsofafamilyoffunctions. |     |     | Assuchitconstitutesa |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | -------------------- | --- |
Giventhattheinputpointsareimages, wemodifythear- high-levelabstractionthatcanbereusedformultipletasks.
chitectureoftheencoderhtoincludeconvolutionlayersas Infutureworkwewillexplorehowfarthesemodelscan
mentionedinsection2. Inadditionweonlyaggregateover helpintacklingthemanykeymachinelearningproblems
inputsofthesameclassbyusingtheinformationprovided thatseemtohingeonabstraction,suchastransferlearning,
bytheinputlabel. Theaggregatedclass-specificrepresenta- meta-learning,anddataefficiency.

ConditionalNeuralProcesses
Acknowledgements Kingma,D.P.andBa,J. Adam: Amethodforstochastic
|     |     |     |     |     |     | optimization. |     | arXivpreprintarXiv:1412.6980,2014. |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------------------- | --- | --- | --- |
WewouldliketothankShakirMohamed,FabioViola,Oriol
Vinyals,IreneGarnelo,DanielBurgess,KevinMcKeeand Kingma,D.P.andWelling,M. Auto-encodingvariational
| Ellen Clancy | for insightful | discussions | and | being | pretty |        |                                    |     |     |     |     |
| ------------ | -------------- | ----------- | --- | ----- | ------ | ------ | ---------------------------------- | --- | --- | --- | --- |
|              |                |             |     |       |        | bayes. | arXivpreprintarXiv:1312.6114,2013. |     |     |     |     |
cool.
|     |     |     |     |     |     | Koch,G.,Zemel,R.,andSalakhutdinov,R. |     |     |     | Siameseneural |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ------------- | --- |
|     |     |     |     |     |     | networksforone-shotimagerecognition. |     |     |     | InICMLDeep    |     |
References
LearningWorkshop,volume2,2015.
| Bartunov,                                 | S. and Vetrov, | D. P. Fast | adaptation | in genera- |       |          |                    |     |         |            |       |
| ----------------------------------------- | -------------- | ---------- | ---------- | ---------- | ----- | -------- | ------------------ | --- | ------- | ---------- | ----- |
|                                           |                |            |            |            |       | Lake, B. | M., Salakhutdinov, |     | R., and | Tenenbaum, | J. B. |
| tivemodelswithgenerativematchingnetworks. |                |            |            |            | arXiv |          |                    |     |         |            |       |
Human-levelconceptlearningthroughprobabilisticpro-
preprintarXiv:1612.02192,2016.
|     |     |     |     |     |     | graminduction. |     | Science,350(6266):1332–1338,2015. |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------------------------------- | --- | --- | --- |
Blundell,C.,Cornebise,J.,Kavukcuoglu,K.,andWierstra,
Lake,B.M.,Ullman,T.D.,Tenenbaum,J.B.,andGersh-
| D. Weightuncertaintyinneuralnetworks. |     |     |     | arXivpreprint |     |      |                                            |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------------- | --- | ---- | ------------------------------------------ | --- | --- | --- | --- |
|                                       |     |     |     |               |     | man, | S.J. Buildingmachinesthatlearnandthinklike |     |     |     |     |
arXiv:1505.05424,2015.
|                                                |           |                |     |             |     | people.                                    | BehavioralandBrainSciences,40,2017. |     |     |     |           |
| ---------------------------------------------- | --------- | -------------- | --- | ----------- | --- | ------------------------------------------ | ----------------------------------- | --- | --- | --- | --------- |
| Bornschein,                                    | J., Mnih, | A., Zoran, D., | and | J. Rezende, | D.  |                                            |                                     |     |     |     |           |
|                                                |           |                |     |             |     | LeCun,Y.,Bottou,L.,Bengio,Y.,andHaffner,P. |                                     |     |     |     | Gradient- |
| Variationalmemoryaddressingingenerativemodels. |           |                |     |             | In  |                                            |                                     |     |     |     |           |
|                                                |           |                |     |             |     | basedlearningappliedtodocumentrecognition. |                                     |     |     |     | Proceed-  |
AdvancesinNeuralInformationProcessingSystems,pp.
ingsoftheIEEE,86(11):2278–2324,1998.
3923–3932,2017.
|                           |              |                        |     |              |     | Liu,Z.,Luo,P.,Wang,X.,andTang,X. |        |       |                | Deeplearningface |     |
| ------------------------- | ------------ | ---------------------- | --- | ------------ | --- | -------------------------------- | ------ | ----- | -------------- | ---------------- | --- |
| Damianou,A.andLawrence,N. |              | Deepgaussianprocesses. |     |              |     |                                  |        |       |                |                  |     |
|                           |              |                        |     |              |     | attributes                       | in the | wild. | In Proceedings | of International |     |
| In Artificial             | Intelligence | and Statistics,        |     | pp. 207–215, |     |                                  |        |       |                |                  |     |
ConferenceonComputerVision(ICCV),December2015.
2013.
|          |                              |            |             |              |     | Louizos, | C. and          | Welling, | M. Multiplicative | normalizing |       |
| -------- | ---------------------------- | ---------- | ----------- | ------------ | --- | -------- | --------------- | -------- | ----------------- | ----------- | ----- |
| Devlin,  | J., Bunel, R. R.,            | Singh, R., | Hausknecht, | M.,          | and |          |                 |          |                   |             |       |
|          |                              |            |             |              |     | flows    | for variational |          | bayesian neural   | networks.   | arXiv |
| Kohli,P. | Neuralprogrammeta-induction. |            |             | InAdvancesin |     |          |                 |          |                   |             |       |
preprintarXiv:1703.01961,2017.
NeuralInformationProcessingSystems,pp.2077–2085,
2017.
Louizos,C.,Ullrich,K.,andWelling,M.Bayesiancompres-
Edwards,H.andStorkey,A. Towardsaneuralstatistician. sionfordeeplearning.InAdvancesinNeuralInformation
ProcessingSystems,pp.3290–3300,2017.
2016.
|                                |                     |         |                     |     |       | Rasmussen,C.E.andWilliams,C.K. |     |     |                             | Gaussianprocesses |     |
| ------------------------------ | ------------------- | ------- | ------------------- | --- | ----- | ------------------------------ | --- | --- | --------------------------- | ----------------- | --- |
| Finn,C.,Abbeel,P.,andLevine,S. |                     |         | Model-agnosticmeta- |     |       |                                |     |     |                             |                   |     |
|                                |                     |         |                     |     |       | inmachinelearning.             |     |     | InAdvancedlecturesonmachine |                   |     |
| learning                       | for fast adaptation | of deep | networks.           |     | arXiv |                                |     |     |                             |                   |     |
preprintarXiv:1703.03400,2017. learning,pp.63–71.Springer,2004.
Gal,Y.andGhahramani,Z. Dropoutasabayesianapprox- Reed, S., Chen, Y., Paine, T., Oord, A. v. d., Eslami, S.,
|          |                                          |     |     |     |     | J.Rezende,D.,Vinyals,O.,anddeFreitas,N. |     |     |     |     | Few-shot |
| -------- | ---------------------------------------- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | -------- |
| imation: | Representingmodeluncertaintyindeeplearn- |     |     |     |     |                                         |     |     |     |     |          |
ing. Ininternationalconferenceonmachinelearning,pp. autoregressivedensityestimation: Towardslearningto
| 1050–1059,2016. |     |     |     |     |     | learndistributions. |     | 2017. |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ------------------- | --- | ----- | --- | --- | --- |
Garnelo,M.,Arulkumaran,K.,andShanahan,M. Towards Rezende,D.J.,Mohamed,S.,andWierstra,D. Stochastic
backpropagationandapproximateinferenceindeepgen-
| deep | symbolic reinforcement | learning. |     | arXiv preprint |     |     |     |     |     |     |     |
| ---- | ---------------------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:1609.05518,2016. erativemodels. arXivpreprintarXiv:1401.4082,2014.
Gregor,K.,Danihelka,I.,Graves,A.,Rezende,D.J.,and Salimbeni,H.andDeisenroth,M. Doublystochasticvari-
Wierstra,D. Draw: Arecurrentneuralnetworkforimage ational inference for deep gaussian processes. In Ad-
|             |                                     |     |     |     |     | vances | in Neural | Information | Processing | Systems, |     |
| ----------- | ----------------------------------- | --- | --- | --- | --- | ------ | --------- | ----------- | ---------- | -------- | --- |
| generation. | arXivpreprintarXiv:1502.04623,2015. |     |     |     |     |        |           |             |            |          | pp. |
4591–4602,2017.
Hewitt,L.,Gane,A.,Jaakkola,T.,andTenenbaum,J.B.The
variationalhomoencoder: Learningtoinferhigh-capacity Santoro,A.,Bartunov,S.,Botvinick,M.,Wierstra,D.,and
generativemodelsfromfewexamples. 2018. Lillicrap,T. One-shotlearningwithmemory-augmented
|             |                |             |     |           |     | neuralnetworks. |     | arXivpreprintarXiv:1605.06065,2016. |     |     |     |
| ----------- | -------------- | ----------- | --- | --------- | --- | --------------- | --- | ----------------------------------- | --- | --- | --- |
| J. Rezende, | D., Danihelka, | I., Gregor, | K., | Wierstra, | D., |                 |     |                                     |     |     |     |
etal. One-shotgeneralizationindeepgenerativemodels. Snell,J.,Swersky,K.,andZemel,R. Prototypicalnetworks
In International Conference on Machine Learning, pp. forfew-shotlearning. InAdvancesinNeuralInformation
| 1521–1529,2016. |     |     |     |     |     | ProcessingSystems,pp.4080–4090,2017. |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |

ConditionalNeuralProcesses
| Snelson,E.andGhahramani,Z. |                               | Sparsegaussianprocesses |     |     |
| -------------------------- | ----------------------------- | ----------------------- | --- | --- |
| usingpseudo-inputs.        | InAdvancesinneuralinformation |                         |     |     |
processingsystems,pp.1257–1264,2006.
vandenOord,A.,Kalchbrenner,N.,Espeholt,L.,Vinyals,
| O.,Graves,A.,etal. | Conditionalimagegenerationwith |     |     |     |
| ------------------ | ------------------------------ | --- | --- | --- |
| pixelcnndecoders.  | InAdvancesinNeuralInformation  |     |     |     |
ProcessingSystems,pp.4790–4798,2016.
Vinyals,O.,Blundell,C.,Lillicrap,T.,Wierstra,D.,etal.
| Matchingnetworksforoneshotlearning. |     |     | InAdvancesin |     |
| ----------------------------------- | --- | --- | ------------ | --- |
NeuralInformationProcessingSystems,pp.3630–3638,
2016.
| Wang, J. | X., Kurth-Nelson, | Z., Tirumala, | D., Soyer, | H., |
| -------- | ----------------- | ------------- | ---------- | --- |
Leibo,J.Z.,Munos,R.,Blundell,C.,Kumaran,D.,and
| Botvinick, | M. Learning | to reinforcement | learn. | arXiv |
| ---------- | ----------- | ---------------- | ------ | ----- |
preprintarXiv:1611.05763,2016.
| Wilson, A.G.,       | Hu, Z., Salakhutdinov,             |     | R., andXing, | E.P. |
| ------------------- | ---------------------------------- | --- | ------------ | ---- |
| Deepkernellearning. | InArtificialIntelligenceandStatis- |     |              |      |
tics,pp.370–378,2016.