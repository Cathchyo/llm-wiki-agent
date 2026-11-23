---
title: "A near-real-time approach for monitoring forest disturbance using Landsat time series: stochastic continuous change detection"
publication_date: "2020-11-05"
publication_date_precision: "day"
publication_date_basis: "first_online"
journal_issue_year: 2021
doi: "10.1016/j.rse.2020.112167"
source_pdf: "tmp/ccdc/A near-real-time approach for monitoring forest disturbance using Landsat time series- Stochastic continuous change detection.pdf"
source_pdf_pages: 17
converter: "MarkItDown 0.1.5 [pdf]"
date_reference: "原 PDF 首页 Available online"
---

# A near-real-time approach for monitoring forest disturbance using Landsat time series: stochastic continuous change detection

Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

A near-real-time approach for monitoring forest disturbance using Landsat
time series: stochastic continuous change detection

Su Ye a,*, John Rogan a, Zhe Zhu b, J. Ronald Eastman c
a Graduate School of Geography, Clark University, 950 Main Street, Worcester, MA 01610, USA
b Department of Natural Resources and the Environment, University of Connecticut, Storrs, CT 06269, USA
c Clark Labs, Clark University, Worcester, MA 01610, USA

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Time series analysis
Forest disturbance
State space model
Kalman filter
Landsat
Near real-time

Forest  disturbances  greatly  affect  the  ecological  functioning  of  natural  forests.  Timely  information  regarding
extent,  timing  and  magnitude  of  forest  disturbance  events  is  crucial  for  effective  disturbance  management
strategies. Yet, we still lack accurate, near-real-time and high-performance remote sensing tools for monitoring
abrupt and subtle forest disturbances. This study presents a new approach called ‘Stochastic Continuous Change
Detection (S-CCD)’ using a dense Landsat data time series. S-CCD improves upon the ‘COntinuous monitoring of
Land Disturbance (COLD)’ approach by incorporating a mathematical tool called the ‘state space model’, which
treats trends and seasonality as stochastic processes, allowing for modeling temporal dynamics of satellite ob-
servations in a recursive way. The quantitative accuracy assessment is evaluated based on 3782 Landsat-based
disturbance  reference  plots  (30  m)  from  a  probability  sampling  distributed  throughout  the  Conterminous
United  States.  Validation  results  show  that  the  overall  accuracy  (best  F1  score)  of  S-CCD  is  0.793  with  20%
omission  error  and  21%  commission  error,  slightly  higher  than  that  of  COLD  (0.789).  Two  disturbance  sites
respectively associated with wildfire and insect disturbances are used for qualitative map-based analysis. Both
quantitative and qualitative analyses suggest that S-CCD achieves fewer omission errors than COLD for detecting
those disturbances with subtle/gradual spectral change. In addition, S-CCD facilitates a better real-time moni-
toring, benefited by its complete recursive manner and a shorter lag for confirming disturbance than COLD (126
days vs. 166 days for alerting 50% disturbance events), and reached up to ~4.4 times speedup for computation.
This  research  addresses  the  need  for  near-real-time  monitoring  and  large-scale  mapping  of  forest  health  and
offers a new approach for operationally performing change detection tasks from dense Landsat-based time series.

1. Introduction

In the last two decades, linked to the recent elevated air temperature
and prolonged drought, an increase in the occurrence and severity of
forest disturbance has been documented over large parts of the globe
(Dale  et al.,  2001; Seidl et  al., 2017; Turner  et  al., 1998)  for such as
insect outbreak (Kautz et al., 2017; Paritsis and Veblen, 2011),wildfire
(Pechony  and  Shindell,  2010;  Westerling,  2016)  and  drought  (Allen
et al., 2015). Forest disturbance events directly emit carbon to the at-
mosphere through oxidation and decomposition of wood (Masek et al.,
2008), and yield significant impacts on ecosystem services of national
forests such as climate regulation and biological diversity conservation
(Curran and Trigg, 2006). Therefore, it is important to systematically
gather information regarding the extent, timing and magnitude of forest

disturbance  in  an  accurate  and  timely  manner,  enabling  an  early
warning and effective management to prevent further loss of forested
land (Rogan and Mietkiewicz, 2015).

For  decades,  satellite  remote  sensing  has  been  promoted  as  a  key
data source for operational forest monitoring (Pasquarella et al., 2017).
Particularly, the opening of the Landsat archive (Woodcock et al., 2008)
has led to improved opportunities for characterizing forest disturbances
from  a  long-term  and  consistent  Landsat  time  series  (Zhu,  2017).
Compared  to  coarse-resolution  datasets  such  as  Moderate  Resolution
Imaging Spectroradiometer (MODIS, 250–1000 m resolution), Landsat-
based time series are provided in a sufficient temporal length of 40-year
global  record  of  finer-resolution  observations  (30  m)  (Masek  et  al.,
2013).  Therefore,  Landsat  data  are  often  perceived  as  the  best  free-
access  remotely  sensed  data  source  for  resolving  the  full  range  of

* Corresponding author.

E-mail address: sye@clarku.edu (S. Ye).

https://doi.org/10.1016/j.rse.2020.112167
Received 22 March 2020; Received in revised form 14 September 2020; Accepted 26 October 2020

RemoteSensingofEnvironment252(2021)112167Availableonline5November20200034-4257/©2020TheAuthors.PublishedbyElsevierInc.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).S. Ye et al.

disturbance occurrence (Cohen et al., 2017; Cohen et al., 2016; Kennedy
et al., 2014; Ye et al., 2018). Recently, the release of Landsat Analysis
Ready  Data  (ARD)  has  eased  automation  for  monitoring  large-scale
forest disturbances (Dwyer et al., 2018). The Landsat ARD gridded all
available  Landsat-4  and  -5  TM,  Landsat-7  ETM+ and  Landsat-8  OLI/
TIRS  to  an  Albers  Equal  Area  (AEA)  Conic  map  projection,  and  are
consistently  geo-registered  and  atmospherically  corrected,  and  hence
holds the highest level of scientific standards and processing required for
immediate use (Zhu, 2019). The Landsat ARD requires the minimum of
user effort for data preprocessing, greatly facilitating a large-scale and
long-term time series analyses (Dwyer et al., 2018).

A  wealth  of  methodologies  on  satellite-based  time  series  analysis
have  been  developed  for  land  cover  change  detection  and  character-
ization (Kennedy et al., 2010; Verbesselt et al., 2010a; Zhu and Wood-
cock, 2014b; Zhu et al., 2012). These approaches are often categorized
based  upon  their  monitoring  strategies:  offline  or  online  monitoring
(Bullock  et  al.,  2019;  Zhu,  2017).  Offline  monitoring  focuses  on  a
retrospective  analysis  when  the  collection  of  time  series  data  is
completed,  and  seeks  to  reconstruct  forest  disturbance  history.  The
representative approaches for this category include LandTrendr (Ken-
nedy  et  al.,  2010),  DBEST  (Jamali  et  al.,  2015)  and  the  ensemble
approach  (Bullock  et  al.,  2019).  Online  monitoring  is  applied  to  a
practical scenario that the new observations are successively collected
and processed in a timely fashion, and hence can be used for near real-
time monitoring. Representative approaches for online monitoring are
Breaks for Additive Season and Trend Monitor (BFAST Monitor) algo-
rithm  (Verbesselt et al., 2012) and Continuous Change Detection and
Classification (CCDC) (Zhu and Woodcock, 2014b; Zhu et al. (2020)),
though they are also applicable for offline monitoring. The BFAST was
originally  designed  for  temporal  segmentation  of  MODIS-based  time
series  (Verbesselt  et  al.,  2010a),  and  was  later  modified  (BFAST
Monitor) to address near real-time detection for drought-related vege-
tation  disturbance  (Verbesselt  et  al.,  2012).  BFAST  Monitor  is  a  uni-
variate approach that uses a single spectral band or index, while it has
been  reported  that  multiple  bands  or  indices  are  more  preferable
because  forest  disturbance  has  a  multi-spectral  expression  requiring
multi-band inputs (Cohen et al., 2017; Zhu et al. (2020)).

CCDC  is  a  multivariate  time-series  model  that  uses  all  available
Landsat  4–8  data  for  change  characterization  and  land  cover  classifi-
cation (Zhu and Woodcock, 2014b). The CCDC first applies the Fmask
(Zhu and Woodcock, 2012) and Tmask algorithm (Zhu and Woodcock,
2014a)  to  screen  clouds,  cloud  shadows  and  snow,  and  then  build  a
harmonic model for each  spectral band based  on remaining clear ob-
servations. A breakpoint indicative of the timing of the disturbance is
identified when the minimum discrepancy between actual and predicted
reflectance of spectral bands for a monitoring window is greater than a
predefined change threshold (Zhu and Woodcock, 2014b). Recently, an
improved  algorithm  called  ‘COntinuous  Monitoring  of  Land  Dis-
turbance’(COLD) was developed based upon CCDC Zhu et al. (2020).
COLD introduced several improvements such as disturbance extraction,
temporally-adjusted Root Mean Square Error (RMSE), and change an-
gles  for  disturbance  confirmation  Zhu  et  al.  (2020).  An  important
finding for COLD is that using the highest frequency for harmonic model
updates, that is per observation instead of per a time span for the CCDC,
can reduce ~20% commission errors Zhu et al. (2020). Zhu et al. (2020)
tested the performance of COLD using 7200 Landsat time series plots
randomly selected across the conterminous United States, and reported
that the COLD algorithm achieves a higher accuracy than CCDC (~20%
commission and ~ 82% omission, see (Cohen et al., 2017), with 27%
omission and 28% commission error for a variety of land disturbance
types.

However,  while  the  COLD  algorithm  has  achieved  improved  per-
formance for change detection accuracy, there are several issues limiting
its implementation for operational monitoring. First, COLD is compu-
tationally  expensive:  the  original  MATLAB  software  takes  ~5000
computing hours for a Landsat ARD tile (1–3 thousand images) based on

our  tests.  The  high  computational  requirement  imposes  limits  on  the
application of COLD for a wide range of scientific research, especially for
a large-area mapping such as at a state or continental scale. The cause for
the slow speed is due to the per observation updating approach Zhu et al.
(2020). For example, if the time series of a single pixel has 500 clear
observations, COLD needs to re-train the model using the ‘Least Absolute
Shrinkage and Selection Operator’ (LASSO) algorithm for approximately
500  times  to  complete  a  detection  for  this  pixel.  Computational  re-
dundancies arise from reconstructing models from scratch for each new
observation being added to the time series. Second, the former version of
COLD, namely CCDC, was designed to detect abrupt land cover change,
and is less helpful for detecting those disturbances that yield small to
medium spectral change magnitude (Brown et al., 2019; Cohen et al.,
2017;  Zhu  et  al.  (2020)).  A  possible  reason  provided  is  that  CCDC
identifies gradual changes as the slope in the harmonic regression model
as opposed to attributing them to a change on a specific date (Bullock
et al., 2019). Though this issue was alleviated by COLD, it has not been
fully solved yet as evident by the only 60% producer accuracy for the
disturbance category ‘stress’ Zhu et al. (2020). Third, within the current
workflow of COLD, near real-time monitoring is not fully operational
because:  1)  COLD  is  a  memory-intensive  algorithm  which  requires
loading  all  images  to  update  model  coefficients  and  to  calculate
temporally-adjusted RMSE for each new observation; 2) certain steps of
COLD such as minimum RMSE require data inputs collected after the
current monitoring date, which does not satisfy the need of near real-
time  monitoring.  A  recursive  transformation  for  these  steps  can  free
the  system  from  loading  all  historical  images  each  time  for  a  new
observation, greatly improving computational efficiency for a near real-
time scenario.

Currently,  most  operational  near  real-time  products  are  based  on
MODIS system, such as Terra-i (Reymondin et al., 2012) and FORMA
alert  system  (Hammer  et  al.,  2014).  To  our  knowledge,  Global  Land
Analysis and Discovery (GLAD) is the only operational system providing
a  near  real-time  monitoring  of  forested  land  at  a  Landsat-pixel  scale
(Hansen et al., 2016). GLAD applies pre-trained decision trees models to
classify clear observations and labels an alert if two or more out of four
consecutive observations were classified into the disturbance category.
As this product is designed and implemented only for tropical evergreen
forest and no phenological variation is considered in the system (Hansen
et  al.,  2016),  its  performance  is  unknown  yet  for  those  middle/high-
latitude regions where disturbances signals are often spectrally similar
to seasonal leaf drop.

In  this  study,  we  describe  a  new  algorithm  called  ‘Stochastic
Continuous Change Detection’ (S-CCD) that is developed to universally
detect forest disturbance from Landsat time series in a recursive fashion.
S-CCD introduces the state space theory into the current framework of
COLD, aiming to address three objectives: 1) to enhance detection ac-
curacy,  especially  for  those  forest  change  with  small  spectral  change
magnitudes while keeping a low rate for commission errors; 2) to pro-
vide an operational framework for near real-time monitoring; and 3) to
improve  computational  efficiency,  enabling  a  long-term  time  series
analysis for a large-area forest disturbance characterization.

In what follows, we first provide an intuitive explanation for state
space models and the Kalman filter as the mathematical foundation of S-
CCD  (Section  2),  describe  our  S-CCD  algorithm  focusing  on  different
steps with COLD (Section 3), introduce our reference dataset and vali-
dation metrics (Section 4) and exhibit the results for both quantitative
and  qualitative evaluation  (Section 5), and  finally  discuss advantages
and future work for S-CCD (Section 6). Of particular note is that Section
5.3 presents a high-performance software package for both S-CCD and
COLD implemented in C language.

2. State space model and the Kalman filter

The  new  approach  built  upon  the  State  Space  Model  (SSM),  an
established  time-series  mathematical  framework  that  allows  for

RemoteSensingofEnvironment252(2021)1121672S. Ye et al.

modeling a dynamic of observed measurements as being explained by a
vector  of  latent  state  variables.  The  SSM  has  two  foundational  ‘sto-
chastic’ assumptions: 1) observations are formulated as a sum of a sto-
chastic  item  linked  to  the  uncertainty  within  the  data  themselves,
namely ‘observational noise’ (ϵt), and a vector of latent variables called
‘states’ (αt); 2) states which are evolving over time as a stochastic process
with  being  affected  by  a  ‘process  noise’  (ηt).  Different  from  classical
decomposition models such as harmonic regression used in BFAST and
CCDC,  SSM  allows  for  trend  and  cycle  components  to  be  evolving
randomly rather than deterministically (see Fig. 1), hence we called it as
‘Stochastic Continuous Change Detection’.

The  general  Gaussian  SSM  can  be  written  in  the  form  as  below

(Durbin and Koopman, 2012):

Observation equation : yt = Z at + ϵt, ϵt̃N(0, H)

State equation : at+1 = Tat + ηt, ηt̃N(0, Q)

(1)

(2)

Where yt  is the observation at time t, ϵt and ηt are two mutually in-
dependent  random  variables  that  follow  a  normal  distribution  with
mean  0  and  variance  H,  and  variance  Q,  respectively.  Z  is  a  system
matrix in a binary form, which indicates those state items that directly
contribute to the observation. T is a transformation matrix defining how
a state vector evolves over time (mathematical definitions for Q, Z and T
are  detailed in the  appendix). State space  representation is central  to
statistical  treatments  for  structural  time  series  models,  owing  to  its
ability of allowing for structural components to be modeled explicitly by
state  variables  (Brockwell  and  Davis,  2013;  Durbin  and  Koopman,
2012).  Therefore,  SSM  holds  great  promise  for  processing  remote
sensing time series, which are well known for the structure of ‘trend +
cycles’ (Eastman et al., 2013; Verbesselt et al., 2010b; Zhu and Wood-
cock, 2014b).

The  SSM  for  the  state  of  ‘trend’  is  formulated  as  a  random-walk

model:

(cid:0)
μt+1 = μt + ξ, ξ̃N

0, σ2
ξ

)

(3)

Where  ξ  is  a  process  noise  item  for  the  trend.  The  ‘cycle’  process

requires two state variables to define:

ct+1 = ct cos λc + c*

(cid:0)
t sin λc + ωt, ωt̃N

)

0, σ2
ω

t+1 = (cid:0) ct sin λc + c*
c*

t cos λc + ω*

t , ω*

(cid:0)
t ̃N

)

0, σ2
ω*

(4)

(5)

Where λc  is the frequency of the cycle, ωt  and ωt* are independent
process noise items. ct is the primary cycle state, while ct* is an accessory
state variable that is not included for prediction of yt  and only used to
enable  a  recursive  form  of  mathematical  computation  (so  its  corre-
sponding element in Z is 0). For a classic model for ‘trend + annual cycle
+ semi-annual cycle’, the state vector at can therefore be given as [μt, ct,
annual, ct,  annual*, ct,  semi, ct,  semi*].

The Kalman filter is the most common tool providing an operational
treatment for SSM. The Kalman filter was first developed for estimating
real-time trajectory of the spacecraft for the Apollo program (Schmidt,
1981), and was later introduced to other application domains such as the
control  of  linear  systems  (Davis  and  Vinter,  1985)  and  econometric
modeling (Pasricha, 2006). Recently, the Kalman filter was applied to
improve satellite-based time series analysis for applications such as crop
phenology  estimation  (Vicente-Guijalba  et  al.,  2014),  synthetic  NDVI
image generation (Sedano et al., 2014) and near real-time monitoring of
defoliation (Olsson et al., 2016). The Kalman filter is claimed to produce
an optimal estimate in the sense that it always reaches the minimum
mean  square  error,  and  is  capable  of  predicting  measurements  in  a
recursive manner so that new measurements can be immediately pro-
cessed as they arrive (Durbin and Koopman, 2012; Kalman, 1960). As
such, the Kalman filter has great potential for being a fundamental tool
of satellite-based near real-time monitoring.

Fig. 2 explains how the Kalman filter recursively adapts its model
coefficients and prediction. When a new observation, ‘2000-12-27’, is
introduced into the time series, there is a discrepancy between the one-
ahead-step prediction (the solid orange dot) and the new observation
(the green cross) called ‘innovation’. In a Kalman filter, the ‘innovation’
can  be  divided  into  two  components:  1)  observational  noise;  and  2)

Fig. 1. The comparison between a harmonic regression model (A) and a state space model (B) for fitting curves. The harmonic regression model has a rigidity for
consistent coefficients such as intercepts, slope and Fourier coefficients, while the state space model assumes that each component is evolving as a stochastic process
so that the model coefficients vary over time.

RemoteSensingofEnvironment252(2021)1121673S. Ye et al.

Fig. 2. An intuitive explanation of Kalman filter based on a Landsat time series. When a new observation at the date of ‘2000-12-27’ is introduced to the system, the
Kalman filter measures the difference between the actual observation (the green cross at ‘2000-12-27’) and the predicted value (the green dot), namely ‘innovation’.
The fitting curve for the model will be adjusted to align with the optimal estimate for the current states (the ‘blue dot’) by filtering out ‘observational noise’ from
‘innovation’. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

model updates brought by the new observation. The Kalman gain is the
relative  weight  assigned  to  actual  model  updates,  which  can  be  esti-
mated by covariances of states and observational noise. Once the Kal-
man  gain  is  computed,  the  Kalman  filter  will  use  it  to  filter  out
observational noise from the innovation. The new model coefficient can
be then adjusted to align with the remaining part, namely ‘filter states’
(the blue dot), yielding a new fitting curve (the dashed orange line). The
filtered states (or adjusted coefficients) will be used to predict the next
observation.

Vegetation  dynamics  often  exhibit  a  complex  trend,  which  is  not
guaranteed  to  be  adequately  approximated  by  a  single  linear  mode
(Burkett et al., 2005; Zhao et al., 2019). The assumption for stochasti-
cally  varying  states  for  SSM  and  Kalman  filters  avoids  the  rigidity  of
classical  decomposition  that  assumes  the  stationarity  of  linearity  and
seasonality, hence complex dynamics from time-series data are uncov-
ered and more local fluctuations can be captured (Brockwell and Davis,
2013).  The  flexibility  of  dynamic  modeling  directly  leads  to  better
fitness of the model, and hence potentially increases the sensitivity of
the  model  to  subtle  changes  because  change  magnitudes  are  often
calculated relative to measurement of model fitness such as Root Mean
Square  Error  (RMSE).  Other  advantages  of  a  state  space  analysis  for
satellite-based time series include: 1) simple mathematical treatment of
missing  data  (shown  in  Appendix)  which  is  critical  for  dealing  with
satellite-based time series known for its temporal irregularity; 2) explicit
consideration  for  measurement  uncertainties  for  the  noisy  nature  of
remote sensing data; 3) high computational efficiency due to its recur-
sive form.

3. Method

The workflow of S-CCD, which consisted of data preparation, model
initialization and continuous monitoring, is presented in Fig. 3. We used
five  spectral  bands  of  surface  reflectance  products  (green,  red,  NIR,
SWIR1 and SWIR2) as the algorithm inputs because Zhu et al. (2020)
reported that these five spectral inputs alone can achieve the best per-
formance  compared  to  being  combined  with  vegetation  indices.  We
applied  the  same  steps  as  COLD  for  S-CCD  for  data  preparation,  for
which we refer to Section 3.1.1 of Zhu et al. (2020).

3.1. Build initial model

After a clear time series is prepared by Fmask (Zhu and Woodcock,
2012),  initialization  model  window  and  Tmask  (Zhu  and  Woodcock,
2014a), S-CCD needs to seek a stable stage to define a statistical refer-
ence  for  change  identification  which  adopts  the  stability  test  and
‘looking back’ procedure Zhu et al. (2020). The subtle modification for
S-CCD is that we used 18 instead of 12 as the required minimum number
of  clear  observations  for  an  initialization  window  (i.e.,  the  window
defining  a  stable  stage  to  initialize  continuous  modeling):  our  new
approach assumes a fixed structure of ‘trend + annual + semiannual’ for
a time series which can be equivalent to 6-coefficient harmonic model.
The suggested minimum observation window for a LASSO regression is
‘number of coefficients * 3’, hence the minimum observation number is
set as 18. The reason for using a 6-coefficients model instead of a tri-
modal component (8-coefficient model) is discussed in Section 6.

3.2. State space model (SSM) initialization

In S-CCD, an additional step is needed to initialize the parameters
and the structural elements for state space models before the continuous
monitoring  starts.  The  initial  SSM  parameters  include  observational
noise (H), process noise (Q), initial states (a0) and initial covariance (P0).
The parameters H and Q are the two most important SSM parameters,
representing the uncertainty level for observations and each stochastic
process. They are often estimated by maximizing likelihood through a
Quasi-Newton numerical searching algorithm in literature (Durbin and
Koopman, 2012; Helske, 2016). However, after initial tests, we learned
that the Quasi-Newton algorithm was inefficient for processing millions
of  pixel-based  time  series.  To  overcome  the  issue,  we  designed  a  fast
method for estimating H and Q, and a new method for estimating a0 and
P0 based upon initial LASSO regression (this fast procedure was detailed
in Section S1 in the supplementary material).

3.3. Temporally adjusted peek window

Like  all  CCDC-like  approaches,  for  each  newly-collected  clear
observation, S-CCD compares predictions and actual observations based

RemoteSensingofEnvironment252(2021)1121674S. Ye et al.

Fig. 3. The workflow of the proposed Stochastic Continuous Change Detection (S-CCD). Same as the original COntinuous Monitoring of Land Disturbance (COLD),
the workflow consists of three stages: 1) data preparation, 2) model initialization, and 3) continuous monitoring. The different steps between S-CCD and COLD are
highlighted as yellow polygons. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

upon a number of consecutive anomaly observations, called the ‘peek
window’ (Davis et al., 2017). COLD approach determines the number of
consecutive observations via calculating the median revisit days across
the entire time series. If the median revisit days are shorter than normal
Landsat temporal density (16 days), more consecutive observations need
to be included, and the probability threshold that all observations need
to exceed is decreased to compensate Zhu et al. (2020). This approach
requires  an  entire  time  series  to  compute  median  revisit  days.  We
developed a completely online approach for adjusting the peek window
for S-CCD. The number of observations for an temporally-adjusted peek
window  is  defined  as  the  minimum  number  satisfying  1)  minimum
consecutive observations, i.e., consedef; and 2) the minimum temporal
span for a peek window (min_peek_days):

consedef = min

{

x| x ≥ consedef and span(x) ≥ min peek days

}

(6)

The defaulted consecutive number consedef = 6. The min_peek_days is
related to the temporal span for that a disturbance event can yield effects
over the vegetation. If min_peek_days is set to be too long, signals of a
disturbance might be affected by post-disturbance forest regrowth; if too
short, some irrelevant ephemeral changes such as soil moisture change
might be misidentified as disturbance. We explored the algorithm per-
formance by using several min_peek_days below the normal peek window
width (e.g. 60, 70, 80 days). Choosing min_peek_days as 80 days shows
the best result (see Fig. S1 in the supplementary material). The threshold
probability is also adjusted when a peek window chooses a consecutive
observation number larger than consedef, following Eq. S4 in Zhu et al.
(2020).

Another  advantage  of  the  new  peek  window  in  terms  of  COLD
approach  is  making  it  feasible  to  account  for  variability  in  Landsat
observation frequency across not just space, but also time. Time series

RemoteSensingofEnvironment252(2021)1121675S. Ye et al.

segments collected in the early days (e.g. before the launch of Landsat 7
ETM+ on  1999)  often  have  a  lower  temporal  density  than  the  most
recent collections. Large changes in frequency driven by the number of
active sensors aboard Landsat satellites had an influence on the CCDC/
COLD change detection records (Brown et al., 2019): higher detection
rates often occur at higher observation frequency particularly after the
launch  of  Landsat  8  OLI,  including  commission  errors  brought  by
ephemeral  forest  change.  The  new  peek  window  considers  that  the
consecutive number is not fixed throughout the detection for a single
time series and enables an adjustment of consecutive observations based
upon the local temporal density for the peek window, because it defines
the peek window according to the physical attribute of a disturbance
signal, namely lasting days, not satellite observation count.

3.4. Recursive temporally-adjusted RMSE

Squared differences between predictions and observations are used
to evaluate deviation of the current peek window from the ‘stable stage’.
RMSE is used to normalize the square difference, which is critical for
decisions on the occurrence of breakpoints. Considering that RMSE often
exhibits a yearly pattern over the whole time series (Zhu et al., 2015),
the  COLD  algorithm  employs  a  temporally-adjusted  RMSE  that  is
calculated based on the temporally closest 24 observations to the peek
window.  For  operational  near  real-time  monitoring,  this  temporally-
adjusted  RMSE  needs  to  be  re-computed  by  loading  all  images  back
into the model for a new observation. We designed a novel recursive
method based upon two histograms respectively for clear observation
counts (Fig. 4A) and square of RMSE (Fig. 4B) for Days of Year (DOY),
which  eliminates  the  need  of  processing  all  images  for  each  new
observation. Both histograms are defined as a bin width of 6 days, and
61 bins in total. The two histograms keep updating once a new obser-
vation is available. To compute a temporally-adjusted RMSE for a new
observation, S-CCD will start from the bin at the middle date of the peek
window (‘Step 1’ in Fig. 4A), and expand the searching window by an
increment of one bin on the left and the right side each time, until the
window includes ≥ 24 observations (‘Step 3’ in Fig. 4A). The temporal
RMSE is computed as the average RMSE*RMSE of the resultant window
based on the count and the temporal RMSE histogram.

Likewise, to enable near real-time monitoring, we used a dynamic
minimum  RMSE  (or  temporal  lag-1  madogram),  instead  of  a  static
minimum RMSE used in Zhu et al. (2020), to define the minimum value
of RMSE for each band: the madogram is updated each year using all
clear past observations.

Therefore, the new RMSE for S-CCD is computed as (b is bth Landsat

band):

RMSEb = max

(cid:0)

recursive temporal RMSEb, dynamic min RMSEb

)

(7)

For an observation n in a peek window, we define the Standardized
Change  Vector  (SCVn)  as  the  difference  between  its  multispectral
reference and its one-step-ahead predictions relative to RMSE using the
five bands (namely green, red, NIR, SWIR1 and SWIR2):

⎡
⎣yn,1 (cid:0) ̂yn,1
RMSE1

SCV n =

,

yn,2 (cid:0) ̂yn,2
RMSE2

, ⋯

yn,5 (cid:0) ̂yn,5
RMSE5

⎤

⎦

(8)

Similar to the COLD algorithm, the change magnitude (CM) is used as
the indicator of breakpoints, which is calculated as the minimum norm
of SCVn for a peek window. CM follows the Chi-squared distribution with
k degree of freedom Zhu et al. (2020), where k is the number of the used
spectral bands, namely ‘5’. A breakpoint candidate is identified if the CM
meets the condition, where P refers to all observations within the peek
window:

3.5. Confirm change using angular spread

Ephemeral  and  systematic  noise  may  also  lead  to  relatively  large
change  magnitudes  for  all  observations  within  a  peek  window.  The
disturbance signal, however, should have a consistent change direction
for  multispectral surface  reflectance  bands. Therefore, the  time series
model needs to confirm the change from the consistency of change an-
gles  once  the  Chi-squared  distribution  test  is  passed.  COLD  confirms
breaks  using  the  mean  included  angle  between  pairs  of  neighboring
change vectors smaller than 45 degrees. We found that this strategy is
sensitive  to  outliers:  for  example,  if  there  is  an  outlier  in  the  six
consecutive observations, two out of five neighbor pairs will be affected
by this outlier (40% of the candidate angles); if there are two outliers in
a  peek  window,  more  than  half  of  neighbor  pairs  are  biased.  We
designed a new change angle index called ‘angular spread’, referred as
the angle between each standardized change vector for nth observation
(SCVn) and the median standardized change vector (MedSCV). The me-
dian change vector here is used to represent the average of the spectral
response  of  a  disturbance.  Ideally,  the  observations  for  a  disturbance
should concentrate around the median change vector. We define ‘Mean
Angular Spread’  for a peek window (Eq. 10) to represent the average
angular departure of each candidate change vector to medium change
vector. We compared the performance of the mean included angle as 45
degrees (the COLD approach) and the mean angular spread with 30, 45
degree. The best result is achieved by using mean angular spread as 30
degrees (Fig. S2 in the supplementary material). The advantage of ‘Mean
Angular  Spread’  is  that  is  less  sensitive  to  outliers  existing  in  a  peek
window. For example, an outlier only affects a single change angle out of
six angles for a default peek window (16.7% of the candidate angles).
∑conseadj
n=1

Mean Angular Spread =

θ(SCVn,MedSCV ) < 30

◦

1
conseadj

(10)

3.6. Update model using the Kalman filter

For those observations that are identified as being unchanged, non-
consecutive outlier removal will be used with a change probability of
0.99999 (same as Zhu et al. (2020)). If the observation passes the outlier
test,  it  will  be  inputted  to  the  system  to  update  the  model  using  the
Kalman filter (see the Appendix). Instead of rebuilding LASSO regression
each  time,  the  Kalman  filter  has  an  extremely  simple  mathematical
treatment for updating models.

3.7. Disturbance identification

Breakpoints  detected  by  the  above  procedure  are  not  necessarily
associated  with  forest  disturbance,  but  maybe  forest  recovery. As  the
final step, we need to single out those breaks that are related to forest
health decline led by disturbance. A typical forest disturbance will cause
lower NIR, higher Red and higher SWIR values. Such spectral change,
however, might be asynchronous. For example, when a forest is attacked
by mountain pine beetle, the increase of SWIR often occurs first due to
increased water stress, then is the increase of the red band, and finally
the  NIR  band  decreases  owing  to  needle  drop.  Hence,  we  created  an
index  called  ‘disturbance  evidence’  (see  Eq.  11)  based  on  the  medium
Standardized Change Vector (MedSCV, defined in Section 3.5). ‘Distur-
bance evidence’ aims to provide a combined analysis for multiple bands
instead of a single band index. The breaks that are identified as being
disturbance-related  need  to  have  a  disturbance  evidence  larger  than
zero:

Disturbance evidence = MedSCV RED (cid:0) MedSCV NIR + MedSCV SWIR1 > 0

(11)

{

CM = min
n∈P

‖SCV n‖2 }

̃χ2(k) > χ2

threshold(5)

(9)

We compared ‘Disturbance Evidence’ with COLD disturbance extraction
with thresholds 0, (cid:0) 0.01, (cid:0) 0.02, and (cid:0) 0.03. ‘Disturbance Evidence’ had
a higher F1 score than all other COLD disturbance extraction methods at

RemoteSensingofEnvironment252(2021)1121676S. Ye et al.

Fig. 4. The explanation for a recursive calculation of temporal RMSE: the algorithm searches a window that just covers ≥24 observations by an increment of a bin on
both sides in an observational count histogram (Fig. 4A). Once it stops (Step3 in Fig. 4A), the temporal RMSE is computed as the average RMSE*RMSE within the
resultant searching window.

all five thresholds (see Fig. S3 in the supplementary material).

3.8. Disturbance probability

For a scenario of near real-time monitoring, disturbance probability
provides a fuzzy disturbance membership for a newly collected obser-
vation if the occurrence of a disturbance event has not been confirmed.
Unlike GLAD (Hansen et al., 2016), COLD Zhu et al. (2020) and NRT-
CCDC (Tang et al., 2020) which calculates a ratio of current consecu-
tive anomaly observation count (i.e., the observations that has a change
magnitude larger than the threshold) to the total required count, S-CCD
computes  disturbance  probability  as  a  ratio  of  ‘anomaly  days’  to  the
required days for a confirmation (namely min_peek_days), given that the
peek window in S-CCD is defined as natural days, not observation count.
‘Anomaly days’ is defined as the temporal span for current consecutive
anomaly  observations  since  the  last  ‘stable’  observation  (as  days).
Disturbance probability have important implications for early manage-
ment  decision  prior  to  statistically  confirming  a  disturbance  event,
which will be discussed later in Section 5.3.

4. Study area, data and performance evaluation

Our performance evaluation for algorithms consisted of 1) quanti-
tative  accuracy  assessment  against  a  comprehensive  national  forest
disturbance  dataset,  2)  qualitative  evaluation  based  on  large-scale
assessment  for  two  selected  disturbance  sites  and  3)  timeliness  anal-
ysis for their near real-time implementation. For quantitative accuracy
assessment, a benchmark forest disturbance database was chosen that
includes  3782  Landsat-based  forest  plots  across  the  conterminous
United States (US) for which their disturbance timing and types have
been well-interpreted from multiple data resources (Cohen et al., 2016;

Zhu et al. (2020)). These forest plots were separated into 2704 undis-
turbed plots and 1078 disturbance plots with 1413 disturbance occur-
rences in total (some plots have successive disturbance occurrences such
as fire and timber harvest). Among these disturbance occurrence, the
most  causal  agent  of  disturbances  is  harvest  (n  = 903),  followed  by
mechanical (n = 149), stress (n = 141), fire (n = 127), and others (n =
83,  e.g.,  hydrology,  wind,  debris,  land  use  change).  For  a  detailed
description of these disturbance causal agent classes, we refer to (Cohen
et al., 2016). The spatial distribution of Landsat plots labeled as undis-
turbed or the number of disturbance occurrences is shown in Fig. 5. We
randomly selected 50% of the reference samples (1891 Landsat plots) for
algorithm development and parameter calibration. The other 50% of the
reference samples were used as a holdout validation set to evaluate the
comparative performance of S-CCD and COLD.

Considering that different algorithms may have different sensitivities
to disturbance magnitudes based on change probability thresholds, the
omission and commission rates based on a series of change probability,
namely  0.90,  0.925,  0.95,  0.975,  0.99,  were  chosen  for  accuracy
assessment.  The  overall  performance  is  evaluated  using  the  F1  score,
because it provides a balanced assessment for omission and commission
rates. The definition of omission, commission rates and F1 score are the
same as Zhu et al. (2020).

F1 score = 2*

(1 (cid:0) commission)*(1 (cid:0) omission)
2 (cid:0) commission (cid:0) omission

(12)

Qualitative map-based comparisons are performed to compare the
performances of two algorithms for a large-area monitoring. We chose
two Landsat ARD tiles that were respectively affected by fire and insect
disturbance. The fire site sits at the San Juan and Rio Grande National
Forests in southwestern Colorado, where Papoose fire burned 200 km2
of forested in June and July 2013 (Verdin et al., 2013). The burned area

RemoteSensingofEnvironment252(2021)1121677S. Ye et al.

Fig. 5. The spatial distribution of 3782 reference sites, and two Landsat ARD scenes chosen as the study areas. The reference sites include 2704 undisturbed plots
(‘white circles’) and 1078 disturbed plots (red circles), which were collected using a stratified sampling based on the ecoregions across the United States. There are
1413 disturbance occurrences in total, and the disturbance categories were dominated by the disturbance category ‘Harvest’  (63.9%), followed by ‘Mechanical’
(10.5%) and ‘Stress’ (9.9%). Landsat ARD 10/10 is located in the south Colorado including a region where Papoose fire happened in 2013; Landsat ARD 30/6 is
located in the New England, including a site affected by gypsy moth infestation in 2016 and 2017.

was dominated by Engelmann spruce (Picea engelmannii) and Subalpine
fir  (Abies  lasiocarpa)  (Carlson  et  al.,  2017).  Caused  by  lightning,  the
Papoose fire starts on June 19, 2013, spread with a southeast direction,
and  was  considerably  dampened  by  precipitation  on  July  19,  2013
(Cyphers et al., 2019; United States Department of, 2014). All Landsat
ARD images between 1996 and 2019 (25 years) were downloaded for
analysis (ARD Tile Grid 10/10). A fire perimeter map for this specific fire
provided  by  GeoMAC  mapping  application  (https://rmgsc.cr.usgs.
gov/outgoing/GeoMAC/) was used as our reference map. Directed by
United  States  Geological  Survey  (USGS),  GeoMAC  updates  the  fire
perimeter  data  based  upon  inputs  from  incident  intelligence  sources,
GPS data, infrared imagery from satellite platform (Walters et al., 2011),
and provides the most accurate perimeter map for this fire to our best
knowledge.

The second disturbance site was chosen for gypsy moth (Lymantria
dispar)  infestation  in  Southern  New  England,  which  covers  southern
Massachusetts, northeast Connecticut, and northwest Rhode Island. This
is a peri-urban region with 56.7% forest cover (i.e., 34.8% hardwood,
17.8% mixed and 4.1% conifer), and 26.7% developed area and 10.8%
wetlands. This study area contains the locations that experienced from
gypsy moth outbreak that started in 2015, spiked in 2017 (Pasquarella
et al., 2018). A gypsy moth infestation can consume a large quantity of
foliage and sometimes causes a near-total defoliation over a season or
two (Townsend and Eshleman, 2004), but often starts to recover very
soon for the following year, so the change signal is commonly ephemeral
(Vogelmann et al., 2016). In addition, infested stands typically consist of
two or more dominant tree species and are often represented by multi-
aged and multi-sized populations (Hart and Veblen, 2015), making the
detection all the more challenging because of mixed spectral response
from various tree species. All Landsat ARD images for ARD Tile Grid 30/

6 in recent 10 years (2010–2019) were downloaded and preprocessed.
The Aerial Detection Survey (ADS) data1 were used as reference dataset.
The  ADS  data  are  polygon-based  forest  health  maps  from  visually-
defined polygons for a variety of specific insects and disease, annually
reported  by  United  States  Department  of  Agriculture  (USDA).  It  was
reported that the recent ADS (after 2012) reached a high-level agree-
ment  to  ground-collected  reference  data  (4%  omission  and  5%  com-
mission for defoliation damage types) (Coleman et al., 2018). Generally
speaking, in spite of its relatively coarse minimum mapping unit as 5 ha,
the ADS data are a valuable source for indicating spatial distribution for
forest disease at a broad scale (Hart and Veblen, 2015; Preisler et al.,
2012)  and  the  timing  of  disease  occurrence,  especially  for  the  recent
disturbances that occurred after 2012.

To evaluate the timeliness in a scenario of near real-time monitoring,
we applied a metric called as “alert-lag relationship curve” (Tang et al.,
2019). Like most time series algorithms, COLD and S-CCD both require a
confirmation  of  a  disturbance  signal  using  consecutive  observations,
which may cause a lag for alerting disturbance in practice. We defined
the alert lag as a delay between the beginning disturbance date and the
date for confirming the disturbance. In practice, ‘the beginning distur-
bance date’ in this study was estimated as the first Landsat observation
for  a  change  signal  of  forest  disturbance.  Though  the  first  Landsat
observation signaling forest disturbance will not always coincide with
the beginning of disturbance, they are the best resources for estimating
the beginning disturbance date in a consistent way, given that reliable
historical  resources  are  often  missing  for  disturbance-date  response
design. Due to that disturbance timings in our reference dataset were

1  http://www.foresthealth.fs.usda.gov/portal/Flex/IDS

RemoteSensingofEnvironment252(2021)1121678S. Ye et al.

estimaed at an annual time step, we re-interpreted the beginning dates
of the disturbances for randomly-selected 500 disturbance plots (~50%
of the total disturbance plots, 665 disturbance events in total), based on
a  visualization  of  each  plot-based  Landsat  time  series.  An  alert-lag
relationship  curve  was  made  based  upon  this  date-level  reference
dataset  to  explore  and  compare  disturbance  detection  rates,  i.e.,  the
proportion of confirmed reference disturbance events, at different lag
times  in  a  near  real-time  monitoring.  In  addition,  disturbance  proba-
bility  maps,  which  can  potentially  provide  timely  information  on
disturbance  progression  and  mitigating  effects  of  detection  latency,
were outputted for timeliness analysis (see Section 5.3).

5. Results

5.1. Quantitative accuracy assessment

We  tested  COLD  and  S-CCD  against  a  holdout  validation  set  (n  =
1891)  using  the  different  probability  thresholds.  The  omission,  com-
mission and F1 score (see annotation around markers) for each test have
been shown in Fig. 6A. S-CCD outperforms COLD at lower thresholds at
0.90, 0.925 and 0.95 for F1 score, while COLD is slightly better at higher
thresholds at 0.975 and 0.99. The best accuracy they reached are close:
S-CCD  achieve  the  best  performance  as  a  F1  score  of  0.793  (0.95
threshold probability, 20.1% omission and 21.4% commission errors),
while  COLD  reaches  the  best  accuracy  as  F1  score  of  0.789  (0.975
threshold probability, 24.6% omission and 17.2% commission errors).
We also evaluated the performance of S-CCD and COLD against seven
forest  disturbance  categories  with  a  threshold  probability  of  0.95
(Fig. 6B). As Fig. 6B shows, S-CCD and COLD have very close omission
errors  for  ‘Harvest’,  ‘Mechanical’  and  ‘Wind’;  S-CCD  achieved  lower
omission error rate in the disturbance category ‘Stress’ and ‘Fire’, but is
worse in ‘Hydrology’ and ‘Other’. Surprisingly, the two approaches both
have relatively high omission errors for ‘fire’ disturbance, which is often
known for causing large change magnitude from satellite images (Cohen
et al., 2016). The possible explanation can relate to some low-severity/
underground  fire  cases  are  included  in  the  reference  dataset,  which
caused only subtle spectral change magnitude.

5.2. Qualitative analysis

For qualitative comparison, S-CCD and COLD were implemented to
detect  timing  of  forest  disturbances  respectively  for  Papoose  fire  and
gypsy moth infestation. A consistent probability threshold as 0.95 was
applied for both algorithms.

Fig.  7  illustrates  the  detection  results  of  S-CCD  and  COLD  for  the
Papoose  fire  site.  Visually,  COLD  and  S-CCD  exhibit  very  similar
detection results  for abrupt disturbance  categories such as  moderate/
high-severity  fire.  Given  that  this  region  was  heavily  affected  by
spruce  beetle  since  2010  (Hart  and  Veblen,  2015),  we  selected  the
breakpoints only detected in 2013, which is the year for Papoose fire
occurrence,  with  an  assumption  that  most  of  these  breakpoints  are
associated with the fire, not spruce beetle attack for that year. To assess
accuracy of timings for these breakpoints, we outputted month maps for
the breakpoints detected in 2013. The breakpoints as detected mostly
occurred in June and July (see Fig. 7A and B), which are well matched
with the active temporal window of Papoose fire on the historical re-
cords  (Cyphers  et  al.,  2019).  To  further  evaluate  spatial  accuracy  for
damage mapping, we compare two detection maps with GeoMAC fire
perimeter map. GeoMAC contains some commission errors for mapping
fire  damage  areas  that  are  actually  bare  lands  from  High-resolution
Satellite  imagery,  while  COLD  and  S-CCD  both  accurately  labeled
them as ‘no-attack’ (see the example of Fig. 7D, E and F). It is noteworthy
that  Landsat  7  related  scan-line  corrector  (SLC)  artifacts  can  be  both
seen  in  the  two  breakpoint  month  maps,  where  SLC-off  issue  caused
breakpoint dates to be several days to two weeks later (rounded to a
month difference in our maps).

For the gypsy moth scene (Fig. 8), we compared years of breakpoints
detected with Aerial Surveying Detection (ADS) data. Most disturbance
events detected by COLD and S-CCD were concentrated at the deciduous
forest  cover  regions  of  the  2016  NLCD  map.  The  disturbance  years
indicated by two algorithms matched that of the ADS data (primarily the
year of 2016 and 2017). This finding is consistent with the historical
record that a major outbreak began in early summer 2016, led by a series
of  unusually  dry  springs  (2014–2016)  (Pasquarella  et  al.,  2017).
Admittedly, both algorithms yield much fewer affected regions than that

Fig. 6. Quantitative accuracy assessment results of COLD and S-CCD based on a holdout reference sample set (n = 1891). A) depicts omission, commission errors
using a series of probability thresholds as 0.9, 0.925, 0.95, 0.975 and 0.99. The F1 score is used to evaluate the overall accuracy combining omission and commission
errors, annotated around each marker. B) reports the omission errors of COLD and S-CCD for each disturbance category (note that the extremely low error rate for
‘Wind’ is due to that its samples number (n = 13) is too small).

RemoteSensingofEnvironment252(2021)1121679S. Ye et al.

Fig. 7. Qualitative comparison for Papoose fire site (Landsat ARD 10/10) in Southeast Colorado among COLD (A), S-CCD (B) and GeoMAC fire perimeter map (C).
COLD and S-CCD both use the probability threshold as 0.95. The colour for A) and B) denotes the month of breakpoints detected in 2013: the spectrum ranging from
red to blue corresponds to months of breakpoints from January to November; the white are no-attack regions in 2013. D), E) and F) shows an example region that
COLD and S-CCD both accurately delineated a non-attack bare land while GeoMAC over-detected it as fire region. (For interpretation of the references to colour in
this figure legend, the reader is referred to the web version of this article.)

the ADS. Considering that Pasquarella et al. (2017) got the same result
for their study in the Southern New England region, those omission er-
rors might be due to commission errors in aerial sketch mapping. For
comparative analysis, we found that COLD missed some regions affected
by gypsy moth (e.g., the dashed blue circle in Fig. 8A), where S-CCD
identifies most parts of the same region as forest disturbance. The lo-
cations and the disturbance years for extra regions detected by S-CCD
have a general agreement with the ADS data (see the dashed circle in
Fig. 8C), proving that these extra breakpoints detected by S-CCD for this
region are related to forest damage caused by gypsy moth. We further
visualized time series of NIR band for a sample pixel that COLD and S-
CCD got conflicted detection results (Fig. 8F and G), and identified an
occurrence of forest disturbance signal associated with a significant drop
of  NIR  band  within  the  temporal  window  of  gypsy  moth  attack,  and
hence confirmed that the extra breakpoints detected by S-CCD were not
commission errors.

5.3. Timeliness analysis

Fig.  9  depicts  the  alert-lag  relationship  curve  which  indicates  the
general  latency  between  reference  disturbance  occurrence  dates  and
confirmation dates of the algorithms based on 500 date-level reference
plots. The steeper the curve appears to be, the fewer lag time that the

algorithm requires to confirm the occurrence of a disturbance. Gener-
ally,  S-CCD  exhibits  higher  detection  rates  of  disturbance  than  COLD
given the same lag day (steeper curve), indicating that it is practically
faster  for  alerting  disturbance  for  a  scenario  of  near  real-time  moni-
toring;  S-CCD  requires  126  days  to  confirm  50%  of  the  disturbances
(namely 50% detection rate) while COLD needs 166 days. Both curves
plateaued at a detection rate of ~75%, which were caused by that the
two  algorithms  missed  detection  for  a  proportion  of  reference  break-
points. To compare with other MODIS-based near real-time algorithms,
S-CCD requires the same days (i.e., 126 days) to achieve 50% detection
rates  as  NRT-CCDC  which  uses daily  MODIS  observations, but  longer
than  the  days  required  by  Fusion  2  (i.e.,  82  days)  which  combines
Landsat and MODIS daily observations for a disturbance detection (Tang
et al., 2019).

Fig. 10 shows a gradient of disturbance probabilities for an example
of  gypsy-moth-affected  stand  over  a  span  of  ~90  days  since  the  first
disturbance signals were detected. Fig. 10 A) are the breakpoint dates
reported  by  a  complete  S-CCD,  which  shows  that  gypsy-moth  attack
occurs  mostly  at  the  dates  6-2-2016  and  6-18-2016  for  this  region.
Fig. 10 B) –  E) shows an increasing trend of disturbance probabilities
with time going by: the region generally reached over a probability of
0.5 over 30 days since the initial infestation signal (Fig. 10 C); a pro-
portion  of  disturbance  pixels  were  confirmed  (see  ‘light  blue’  pixels)

RemoteSensingofEnvironment252(2021)11216710S. Ye et al.

Fig. 8. Qualitative comparison for gypsy moth site (Landsat ARD 30/6) in Southern New England among COLD (A), S-CCD (B) and the ADS reference map (C). COLD
and S-CCD both use the probability threshold as 0.95. The colour for (A), (B) and (C) denote the disturbance year indicated by each data source: the spectrum ranging
from red to blue corresponds to the years from 2011 to 2018. Fig. 8 D) and E) show an example region that S-CCD can detected out the region that COLD missed gypsy
moth damage. Fig. 8 F) and G) plots NIR time series of a sample pixel positioned at ‘black rectangle’ in D) and E) to confirm the occurrence of forest disturbance for
this region. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

over 60 days (Fig. 10 D); most disturbance pixels got confirmed after 90
days  (Fig.  10E).  The  result  illustrates  that  the  temporal  span  of  a
disturbance signal can be continuously indicated by disturbance prob-
abilities, which allows managers to choose thresholds based on practical
needs.  For  example,  a  gypsy  moth-affected  region  can  be  potentially
determined  by  using  a  low  alerting  threshold  (< 0.5)  combined  with
spatial homogeneity analysis within 30-45 days since its initial symptom

from Landsat time series, which  can help locate early infestation and
mitigate population expansion during its active window.

5.4. Efficiency test and software implementation

We implemented COLD and S-CCD in the high-performance C pro-
gramming  language.  The  C  package  named  ‘S-CCD’  is  downloadable

RemoteSensingofEnvironment252(2021)11216711S. Ye et al.

Fig. 9. The alert-lag table illustrating detection rates as a function of lag time based on 500 date-level reference disturbance plots.

Fig.  10. An  example  of  disturbance  probability  maps  indicating  disturbance  progression  for  the  near  real-time  monitoring.  A)  are  the  breakpoint  dates  from  a
complete detection S-CCD for a forest stand attacked by gypsy moth on June 2016; B) – E) shows a dynamics of disturbance probabilities (represented as red colour
ramp) and confirmed disturbance pixels (light blue) every 30 days since initial attack. F) the reference high-resolution Google imagery. (For interpretation of the
references to colour in this figure legend, the reader is referred to the web version of this article.)

from  https://github.com/SuYe99/s-ccd.  The  software  implemented  a
shared  memory  parallelization  for  COLD  and  S-CCD  under  a  Linux/
MacOS desktop environment, and has been already adapted for a High-
Performance Computing (HPC) environment. It is noteworthy that our
C-based COLD has been 1.5-2.0 times faster than the original MATLAB-
based implementation.

To  test  the  efficiency  for  C-based  COLD  and  S-CCD,  we  used  a
‘dummy’ Landsat ARD scanline which is a standard sample set of 5000
pixel-based time series plots selected from our reference sample set. The
sample set consists of 3782 forest plots and 1218 non-forest plots. To
uncover the effects of monitoring span on the speed, we pruned each
time series into three different lengths of time series records, that is 10

RemoteSensingofEnvironment252(2021)11216712S. Ye et al.

years (2008–2017), 20 years (1998–2017) and 34 years (1984–2017).
The results are summarized in Fig. 11. S-CCD can achieve up to ~4.4
times faster than the C-based COLD (with 34-year time series records).
With the length of records decreasing, the efficiency improvement of S-
CCD over COLD declines, as ~3.5 times at 20-year time series records,
and ~ 1.8 time faster at 10-year time series records. This is because S-
CCD improves efficiency mainly at the step of the model update; a longer
time  series  needs  a  greater  number  for  model  updates  to  complete  a
detection, and hence more significant efficiency improvement made by
S-CCD.  For  a  standard  20-year  Landsat  ARD  time  series,  our  S-CCD
program takes only ~6 min to finish a detection for a 5000-pixel scan-
line, and ~ 500 computing hours for a Landsat ARD scene.

6. Discussion

The quantitative accuracy assessment indicates that the differences
between the best overall accuracy achieved by S-CCD and COLD are only
0.4% (see Fig. 6A, 0.793 v.s. 0.789). The primary reason is that our plot
database is generated from random sampling over a nation-wide region,
for which 63% of the forest disturbances are harvesting activities; the
two  approaches  have  very  similar  performance  for  detecting  strong
spectral  signals  yielded  by  those  disturbances  with  medium-  or  high-
severity and homogeneous tree damages such as harvest disturbances
(omission  errors:  16%  v.s.  16.2%).  Our  map-based  evaluation  for
Papoose fire case supports this conclusion.

S-CCD,  however,  achieved  noticeably  fewer  omission  errors  than
COLD  for  those  lower-magnitude  disturbances  such  as  drought  stress
and low-severity fire (see Fig. 6b). This finding was confirmed by our
qualitative comparison for the case study of gypsy moths. The reason
could be that S-CCD allows for known changes in the structure of the
system  over  time,  and  often  can  achieve  a  better  model  fitting  than

COLD that assumes the rigidity of “linear trend + harmonic cycles”. We
calculated the average RMSE for each band using all our 3782 samples.
The results, as shown in Table 1, indicate that S-CCD has generally lower
average RMSE than COLD for all seven spectral bands other than NIR
and thermal bands (thermal band is not used to compute change mag-
nitudes  for  both  approaches,  and  thereby  has  no  effects  on  break
detection).  As  the  two  approaches  both  evaluated  change  magnitude
relative to the RMSE, the lower RMSE means that S-CCD model is more
sensitive to those low-magnitude spectral changes.

Another obvious advantage of S-CCD is that it is a completely online
monitoring  algorithm,  which  can  be  directly  used  for  near  real-time
forest monitoring. S-CCD improves several steps of COLD and enables
a continuous monitoring in a completely recursive form by using such as
the adjusted peek window, recursive temporal RMSE. More importantly,
the core technique for S-CCD, the Kalman filter, is a powerful real-time
algorithm well known for its high computational efficiency and short-
memory  requirement.  For  COLD,  limited  by  its  manner  for  re-
constructing the model per observation, it requires reading all images
into the system to rebuild harmonic curves for each new observation.
Instead, S-CCD just needs to update those parameter files (e.g., states
and  covariance)  once  the  initialization  is  finished,  which  can  reduce
~95% of data inputs for monitoring each new observation.

We reported lag-alert relationship curves which is designed to assess
timeliness for identifying disturbance events in a near real-time scenario
(see Fig. 9). Fig. 12 illustrates an example that S-CCD needs shorter lag
time to confirm a change based upon a gypsy-moth-affected pixel. The
shorter  lag  is  mainly  attributed  to  the  new  temporally-adjusted  peek
window adopted by S-CCD that defines the peek window as calendar
days, not a fixed observation number as COLD does. COLD employs a
fixed peak window of 12 observations for this case as the median revisit
days is 8 days (see Formula S2 in the supplementary material of Zhu

Fig. 11. The result for the efficiency test based on a dummy Landsat ARD scanline (5000 sample pixels). Each time series are pruned as three versions for time series
records, that is 10 years (2008–2017), 20 years (1998–2017), 34 years (1984–2017). The result shows that the efficiency of S-CCD was increased as the length of time
series increased, and can be up to 4.4 times faster than COLD. The CPU is Intel(R) Core (TM) i7–4790, 3.60GHz.

RemoteSensingofEnvironment252(2021)11216713S. Ye et al.

Table 1
the average RMSE of COLD and S-CCD for each band using 3782 forest samples across the conterminous United States (the bold columns are the two bands that S-CCD
has higher RMSE than COLD).

Band

COLD
S-CCD

Blue

122.682
119.061

Green

117.127
110.761

Red

122.473
118.476

NIR

273.336
279.478

SWIR1

197.937
191.518

SWIR2

151.032
150.098

Thermal

389.227
401.061

Fig. 12. A gypsy-moth example for COLD and S-CCD detecting breakpoints in a near real-time manner. The black line represents the reference disturbance date; the
dash line is the date that this change was confirmed based on consecutive anomaly observations (i.e., peek window). The date difference between the two lines
represents ‘lag time’ when the algorithm is applied to near real-time monitoring. S-CCD shows shorter lag time benefited from its temporally-adjusted peek window
defined as a fixed calendar days.

et al. (2020). When the peek window spans over a period of sparse clear
observations such as June 2016 in this case, the peek window for COLD
has to be extended in order to incorporate enough clear observations.
Differently, S-CCD defines the peek window as the minimum width of 80
calendar days, and hence identified the disturbance roughly one month
earlier  than  that  of  COLD,  regardless  of  temporal  density.  It  is  also
noteworthy that though S-CCD requires an anomaly peek window of at
least  80  days  (min_peek_days)  to  confirm  a  disturbance,  the  outputted
metric of disturbance probability allows for an earlier and more flexible
decision-making  process:  for  example,  Fig.  10  shows  that  the  pixels
homogeneously presented a disturbance probability of 0.5 over 30 days
since the initial gypsy moth attack, making it potentially feasible to yield
a  disturbance  alert  much  earlier  than  80  days  by  applying  different
probability thresholds.

A possible concern is that S-CCD assumes a consistent structure of
time series for trend, annual and semi-annual harmonic items (equal to
6-coefficient harmonic models), while Zhu et al. (2020) suggested using
a  harmonic model  with a  maximum coefficient  as  8,  including trend,
annual,  semi-annual  and  trimodal  harmonic  items  (frequency  = 1/3
year). As such, we tested adding an additional trimodal cycle component
into the presumed time series structure of S-CCD, and found that the best
F1 score decreased from 0.795 to 0.706 for S-CCD (see Fig. S4 in the
supplementary material). In a harmonic regression, trimodal component
can  be  viewed  as  an  additional  modifier  to  annual  and  semi-annual
curves (Eastman et al., 2009). The state space model adopted a totally
different strategy to resolve unexplained variance from annual and semi-
annual curves: the state space model assumes that the trend and sea-
sonality  states  are  evolving  as  time  goes  by  (see  Fig.  2B),  instead  of

following  a  fixed  set  of  harmonic  coefficients,  thus  the  unexplained
variances  can  be ‘ingested’  immediately  by  changes  in  structure  over
time.  Another  reason  might  be  that  we  focus  on  forest  disturbance
detection for this study, while the trimodal component is often found to
be more useful for modeling cropland dynamics.

Admittedly, COLD is designed for detecting/characterizing all types
of land disturbances, not limited to forest disturbances. We tested S-CCD
against a reference dataset for comprehensive land types, and reached a
slightly lower F1 score compared with COLD (0.69 vs 0.71). Our test
shows  that  S-CCD  performs  less  ideal  under  a  highly-fluctuated  envi-
ronment, and is more prone to over-detection due to those ephemeral
changes that have a high change magnitude, such as moisture change for
grassland/bare land and agricultural rotation. To alleviate this issue, our
software package enables users to specify a mask for focused study area,
which  can exclude the regions where  uninterested land change occur
and greatly improve processing efficiency as well. Yet, there is still much
studies that is needed to analyze characteristics of detected breaks and
select breaks only linked to targeted physical processes. Another reason
for the unsatisfactory results is that we often have multiple historical
data  sources  to  confirm  forest  disturbances  such  as  the  ADS  and  the
LANDFIRE products, but reliable references for the other non-forest land
disturbance  are  lacking.  The  quality  of  our  non-forest  land  samples
might affect the final accuracy result. Our future work will be directed
into  1)  modifying  S-CCD  to  accommodate  other  applications  such  as
agricultural shifts and urban expansion, and 2) tuning the algorithm for
the optimal parameters, such as probability threshold and min_peek_days,
for  better  detection  of  targeted  change  agents  and  timely  warning  of
land disturbance.

RemoteSensingofEnvironment252(2021)11216714S. Ye et al.

7. Conclusion

Acknowledgement

We  presented  an  improved  time  series  framework,  Stochastic
Continuous Change Detection (S-CCD), for near real-time forest distur-
bance monitoring. The new approach introduces the state space model
into the current framework for Continuous Monitoring of Land Distur-
bance (COLD), to facilitate a near real-time analytics of forest dynamics
with a  shorter lag time and improve  computational efficiency. S-CCD
provides an accurate mapping for timing and change magnitude of forest
disturbance, and uncovers complex nonlinear dynamics from time series
data.  Most  notably,  S-CCD  can  improve  the  monitoring  for  those  dis-
turbances that induce subtle spectral changes.

Declaration of Competing Interest

We  gratefully  acknowledge  the  support  of  American  Society  of
Photogrammetry  and  Remote  Sensing  (ASPRS)  William  A.  Fisher
Scholarship  and  Albert,  and  Norma  and  Howard  Geller’77  Endowed
Research Awards to Su Ye. This research was partially supported by the
USGS-NASA Landsat Science Team Program for Toward Near Real-time
Monitoring  and  Characterization  of  Landsat  Surface  Change  for  the
Conterminous  US  (140G0119C0008)  to  Zhe  Zhu.  The  content  of  this
document  does  not  necessarily  represent  the  views  or  policies  of  the
Department of the Interior, nor does mention of trade names, commer-
cial  products  or  organizations  imply  endorsement  by  the  U.S.
Government.

None.

Appendix

The system matrices for ‘trend+annual+semi-annual’ time series structural model are defined by

Z = (1, 1, 0, 1, 0)

(

Q = diag

⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣

1

0

0

0

0

T =

ξ, σ2
σ2

ω,annual, σ2

ω*,annual, σ2

ω,semi, σ2

ω*,semi

)

(

0
2π
365.25
(

2π
365.25

cos

(cid:0) sin

(

sin

)

(

cos

)

)

0
2π
365.25

2π
365.25

)

0

0

0

0

0

0

0

0

0

0

cos

(cid:0) sin

(

)

2π
2*365.25
(
2π
2*365.25

(

sin

)

(

cos

)

)

2π
2*365.25
2π
2*365.25

⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦

The Kalman filter recursion for the general Gaussian model of form are

vt,i = yt,i (cid:0) Z at,i

Ft,i = Z Pt,iZT + Hi

Kt,i = Pt,iZT

at|t,i = at,i + Kt,iF(cid:0) 1

t,i vt,i

at+1,i = T at|t,i

Pt+1,i = T

(
Pt,i (cid:0) Kt,iKT

t,iF(cid:0) 1
t,i

)

T T + Qi

(A1)

(A2)

(A3)

(A4)

(A5)

(A6)

(A7)

(A8)

(A9)

Where.
yt,  i: the observation at time t for band i.
vt,  i: the innovation, namely the difference between predicted and actual observations, at time t for band i
Z: the system matrix that determines which items in the state vector are included for the observation
Kt,  i: the Kalman gain which is the relative ratio of being assigned to the model update is from the innovation at time t for band i
Pt,  i: the covariance matrix at time t for band i
at∣t,  i: the filtered states at time t for band i
Ft,  i: the variance of the innovation vt,  i
Qi: the process noise for band i
Hi: the observational noise for band i
For missing observation, there is no innovation vt, i. Therefore, the mathematical treatment for state and covariance matrix updates can be simply

put as
at+1,i = T at|t,i

Pt+1,i = TPt,iT T + Qi

(A10)

(A11)

RemoteSensingofEnvironment252(2021)11216715S. Ye et al.

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.rse.2020.112167.

References

Allen, C.D., Breshears, D.D., McDowell, N.G., 2015. On underestimation of global
vulnerability to tree mortality and forest die-off from hotter drought in the
Anthropocene. Ecosphere 6, 1–55.

Brockwell, P.J., Davis, R.A., 2013. Introduction to Time Series and Forecasting (Springer

Science & Business Media).

Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E.,

Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K.,
Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D.,
Reker, R.R., Rover, J., 2019. Lessons learned implementing an operational
continuous United States national land change monitoring capability: the land
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens.
Environ. 111356.

Bullock, E.L., Woodcock, C.E., Holden, C.E., 2019. Improved change monitoring using an

ensemble of time series algorithms. Remote Sens. Environ. 111165.

Burkett, V.R., Wilcox, D.A., Stottlemyer, R., Barrow, W., Fagre, D., Baron, J., Price, J.,
Nielsen, J.L., Allen, C.D., Peterson, D.L., Ruggerone, G., Doyle, T., 2005. Nonlinear
dynamics in ecosystem response to climatic change: case studies and policy
implications. Ecol. Complex. 2, 357–394.

Carlson, A.R., Sibold, J.S., Assal, T.J., Negr´on, J.F., 2017. Evidence of compounded
disturbance effects on vegetation recovery following high-severity wildfire and
spruce beetle outbreak. PLoS One 12, e0181778.

Cohen, W.B., Yang, Z., Stehman, S.V., Schroeder, T.A., Bell, D.M., Masek, J.G., Huang, C.,
Meigs, G.W., 2016. Forest disturbance across the conterminous United States from
1985–2012: the emerging dominance of forest decline. For. Ecol. Manag. 360,
242–252.

Cohen, W.B., Healey, S.P., Yang, Z., Stehman, S.V., Brewer, C.K., Brooks, E.B.,

Gorelick, N., Huang, C., Hughes, M.J., Kennedy, R.E., 2017. How similar are forest
disturbance maps derived from different Landsat time series algorithms? Forests 8,
98.

Coleman, T.W., Graves, A.D., Heath, Z., Flowers, R.W., Hanavan, R.P., Cluck, D.R.,
Ryerson, D., 2018. Accuracy of aerial detection surveys for mapping insect and
disease disturbances in the United States. For. Ecol. Manag. 430, 321–336.

Curran, L.M., Trigg, S.N., 2006. Sustainability science from space: quantifying forest

disturbance and land-use dynamics in the Amazon. In: Proceedings of the
National Academy of Sciences of the United States of America, 103,
pp. 12663–12664.

Cyphers, L., Mackes, K., Duda, K., 2019. Timber losses from west fork complex fire in

Southwest Colorado. For. Prod. J. 69 (4), 272–277.

Dale, V.H., Joyce, L.A., McNulty, S., Neilson, R.P., Ayres, M.P., Flannigan, M.D.,

Hanson, P.J., Irland, L.C., Lugo, A.E., Peterson, C.J., 2001. Climate change and forest
disturbances. BioScience 51, 723–734.

Davis, M.H.A., Vinter, R.B., 1985. Stochastic models. Stoch. Model. Control 60–99.
Davis, B., Guo, S., Smith, K., 2017. Land Change Monitoring Assessment and Projection

(LCMAP) Python Implementation of Continuous Change Detection (pyccd).
Department of Interior U.S. Geological Survey.

Durbin, J., Koopman, S.J., 2012. Time Series Analysis by State Space Methods: Second

Edition (OUP Oxford).

Dwyer, J., Roy, D., Sauer, B., Jenkerson, C., Zhang, H., Lymburner, L., 2018. Analysis

ready data: enabling analysis of the Landsat archive. Remote Sens. 10.
Eastman, J.R., Sangermano, F., Ghimire, B., Zhu, H., Chen, H., Neeti, N., Cai, Y.,

Machado, E.A., Crema, S.C., 2009. Seasonal trend analysis of image time series. Int.
J. Remote Sens. 30, 2721–2726.

Eastman, J.R., Sangermano, F., Machado, E.A., Rogan, J., Anyamba, A., 2013. Global

trends in seasonality of normalized difference vegetation index (NDVI), 1982–2011.
Remote Sens. 5, 4799–4818.

Hammer, D., Kraft, R., Wheeler, D., 2014. Alerts of forest disturbance from MODIS

imagery. Int. J. Appl. Earth Obs. Geoinf. 33, 1–9.

Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S.,
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
using Landsat data. Environ. Res. Lett. 11, 034008.

Hart, S.J., Veblen, T.T., 2015. Detection of spruce beetle-induced tree mortality using

high-and medium-resolution remotely sensed imagery. Remote Sens. Environ. 168,
134–145.

Helske, J., 2016. KFAS: Exponential Family State Space Models in R. arXiv [stat.CO].
Jamali, S., J¨onsson, P., Eklundh, L., Ard¨o, J., Seaquist, J., 2015. Detecting changes in
vegetation trends using time series segmentation. Remote Sens. Environ. 156,
182–195.

Kalman, R.E., 1960. A new approach to linear filtering and prediction problems. Int. J.

Eng. Trans. A 82, 35–45.

Kautz, M., Meddens, A.J., Hall, R.J., Arneth, A., 2017. Biotic disturbances in northern
hemisphere forests–a synthesis of recent data, uncertainties and implications for
forest monitoring and modelling. Glob. Ecol. Biogeogr. 26, 533–552.

Kennedy, R.E., Yang, Z., Cohen, W.B., 2010. Detecting trends in forest disturbance and
recovery using yearly Landsat time series: 1. LandTrendr—Temporal segmentation
algorithms. Remote Sens. Environ. 114, 2897–2910.

Kennedy, R.E., Andr´efou¨et, S., Cohen, W.B., G´omez, C., Griffiths, P., Hais, M., Healey, S.
P., Helmer, E.H., Hostert, P., Lyons, M.B., Others, 2014. Bringing an ecological view
of change to Landsat-based remote sensing. Front. Ecol. Environ. 12, 339–346.
Masek, J.G., Huang, C., Wolfe, R., Cohen, W., Hall, F., Kutler, J., Nelson, P., 2008. North
American forest disturbance mapped from a decadal Landsat record. Remote Sens.
Environ. 112, 2914–2926.

Masek, J.G., Goward, S.N., Kennedy, R.E., Cohen, W.B., Moisen, G.G., Schleeweis, K.,
Huang, C., 2013. United States Forest disturbance trends observed using Landsat
time series. Ecosystems 16, 1087–1104.

Olsson, P.-O., Lindstr¨om, J., Eklundh, L., 2016. Near real-time monitoring of insect

induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote
Sens. Environ. 181, 42–53.

Paritsis, J., Veblen, T.T., 2011. Dendroecological analysis of defoliator outbreaks on

Nothofagus pumilio and their relation to climate variability in the Patagonian Andes.
Glob. Chang. Biol. 17, 239–253.

Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect

defoliation using Landsat time series. Forests 8, 275.

Pasquarella, V., Elkinton, J.S., Bradley, B.A., 2018. Extensive gypsy moth defoliation in
southern New England characterized using Landsat satellite observations. Biol.
Invasions 20, 3047–3053.

Pasricha, G.K., 2006. Kalman Filter and its Economic Applications.
Pechony, O., Shindell, D.T., 2010. Driving forces of global wildfires over the past

millennium and the forthcoming century. In: Proceedings of the National Academy
of Sciences, 107, pp. 19167–19170.

Preisler, H.K., Hicke, J.A., Ager, A.A., Hayes, J.L., 2012. Climate and weather influences
on spatial temporal patterns of mountain pine beetle populations in Washington and
Oregon. Ecology 93, 2421–2434.

Reymondin, L., Jarvis, A., Perez-Uribe, A., Touval, J., Argote, K., Rebetez, J., Guevara, E.,
Mulligan, M., 2012. A Methodology for near Real-Time Monitoring of Habitat
Change at Continental Scales Using MODIS-NDVI and TRMM (Submitted Remote
Sensing of Environment).

Rogan, J., Mietkiewicz, N., 2015. Land cover change detection. In: Thenkabail, P.S. (Ed.),

Land Resources Monitoring, Modeling, and Mapping with Remote Sensing,
pp. 579–603.

Schmidt, S.F., 1981. The Kalman filter - its recognition and development for aerospace

applications. J. Guid. Control. Dyn. 4, 4–7.

Sedano, F., Kempeneers, P., Hurtt, G., 2014. A Kalman filter-based method to generate

continuous time series of medium-resolution NDVI images. Remote Sens. 6,
12381–12408.

Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Nat. Clim. Chang. 7, 395–402.

Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
monitoring of tropical forest disturbance: new algorithms and assessment
framework. Remote Sens. Environ. 224, 202–218.

Tang, X., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2020. Can VIIRS continue the

legacy of MODIS for near real-time monitoring of tropical forest disturbance?
Remote Sens. Environ. 249, 112024.

Townsend, P.A., Eshleman, K.N., others, 2004. Remote sensing of gypsy moth defoliation

to assess variations in stream nitrogen concentrations. Ecological Applications 14
(2), 504–516.

Turner, M.G., Baker, W.L., Peterson, C.J., Peet, R.K., 1998. Factors influencing

succession: lessons from large, infrequent natural disturbances. Ecosystems 1,
511–523.

Verbesselt, J., Hyndman, R., Newnham, G., Culvenor, D., 2010a. Detecting trend and

seasonal changes in satellite image time series. Remote Sens. Environ. 114, 106–115.

Verbesselt, J., Hyndman, R., Zeileis, A., Culvenor, D., 2010b. Phenological change

detection while accounting for abrupt and gradual trends in satellite image time
series. Remote Sens. Environ. 114, 2970–2980.

Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using

satellite image time series. Remote Sens. Environ. 123, 98–108.

Verdin, K.L., Dupree, J.A., Stevens, M.R., 2013. Postwildfire Debris-Flow Hazard

Assessment of the Area Burned by the 2013 West Fork Fire Complex, Southwestern
Colorado. US Department of the Interior, US Geological Survey.

Vicente-Guijalba, F., Martinez-Marin, T., Lopez-Sanchez, J.M., 2014. Crop phenology
estimation using a multitemporal model and a Kalman filtering strategy. IEEE
Geosci. Remote Sens. Lett. 11, 1081–1085.

Vogelmann, J.E., Gallant, A.L., Shi, H., Zhu, Z., 2016. Perspectives on monitoring gradual
change across the continuity of Landsat sensors using time-series data. Remote Sens.
Environ. 185, 258–270.

Walters, S.P., Schneider, N.J., Guthrie, J.D., 2011. Geospatial Multi-Agency Coordination

(GeoMAC) Wildland Fire Perimeters, 2008 (Data Series).

Westerling, A.L., 2016. Increasing western US forest wildfire activity: sensitivity to
changes in the timing of spring. Philos. Trans. R. Soc. B 371, 20150178.

Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,

Gao, F., Goward, S.N., Helder, D., Helmer, E., 2008. Free access to Landsat imagery.
Science 320 (1011–1011).

RemoteSensingofEnvironment252(2021)11216716S. Ye et al.

Ye, S., Rogan, J., Sangermano, F., 2018. Monitoring rubber plantation expansion using
Landsat data time series and a Shapelet-based approach. ISPRS J. Photogramm.
Remote Sens. 136, 134–143.

Zhao, K., Wulder, M.A., Hu, T., Bright, R., Wu, Q., Qin, H., Li, Y., Toman, E., Mallick, B.,
Zhang, X., Brown, M., 2019. Detecting change-point, trend, and seasonality in
satellite time series data to track abrupt changes and nonlinear dynamics: a Bayesian
ensemble algorithm. Remote Sens. Environ. 232, 111181.

Zhu, Z., 2017. Change detection using landsat time series: a review of frequencies,

Zhu, Z., Woodcock, C.E., 2014a. Automated cloud, cloud shadow, and snow detection in
multitemporal Landsat data: an algorithm designed specifically for monitoring land
cover change. Remote Sens. Environ. 152, 217–234.

Zhu, Z., Woodcock, C.E., 2014b. Continuous change detection and classification of land
cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
Zhu, Z., Woodcock, C.E., Olofsson, P., 2012. Continuous monitoring of forest disturbance

using all available Landsat imagery. Remote Sens. Environ. 122, 75–91.
Zhu, Z., Woodcock, C.E., Holden, C., Yang, Z., 2015. Generating synthetic Landsat

preprocessing, algorithms, and applications. ISPRS J. Photogramm. Remote Sens.
130, 370–384.

images based on all available Landsat data: predicting Landsat surface reflectance at
any given time. Remote Sens. Environ. 162, 67–83.

Zhu, Z., 2019. Science of Landsat analysis ready data. Remote Sens. 11, 2166.
Zhu, Z., Woodcock, C.E., 2012. Object-based cloud and cloud shadow detection in

Landsat imagery. Remote Sens. Environ. 118, 83–94.

Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.

Continuous monitoring of land disturbance based on Landsat time series. Remote
Sens. Environ. 238, 111116.

RemoteSensingofEnvironment252(2021)11216717
