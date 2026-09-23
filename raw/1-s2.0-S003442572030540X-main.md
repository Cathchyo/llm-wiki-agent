RemoteSensingofEnvironment252(2021)112167
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
A near-real-time approach for monitoring forest disturbance using Landsat
time series: stochastic continuous change detection
Su Yea,*, John Rogana, Zhe Zhub, J. Ronald Eastmanc
aGraduate School of Geography, Clark University, 950 Main Street, Worcester, MA 01610, USA
bDepartment of Natural Resources and the Environment, University of Connecticut, Storrs, CT 06269, USA
cClark Labs, Clark University, Worcester, MA 01610, USA
A R T I C L E I N F O A B S T R A C T
Keywords: Forest disturbances greatly affect the ecological functioning of natural forests. Timely information regarding
Time series analysis extent, timing and magnitude of forest disturbance events is crucial for effective disturbance management
Forest disturbance strategies. Yet, we still lack accurate, near-real-time and high-performance remote sensing tools for monitoring
State space model
abrupt and subtle forest disturbances. This study presents a new approach called ‘Stochastic Continuous Change
Kalman filter
Detection (S-CCD)’ using a dense Landsat data time series. S-CCD improves upon the ‘COntinuous monitoring of
Landsat
Near real-time Land Disturbance (COLD)’ approach by incorporating a mathematical tool called the ‘state space model’, which
treats trends and seasonality as stochastic processes, allowing for modeling temporal dynamics of satellite ob-
servations in a recursive way. The quantitative accuracy assessment is evaluated based on 3782 Landsat-based
disturbance reference plots (30 m) from a probability sampling distributed throughout the Conterminous
United States. Validation results show that the overall accuracy (best F1 score) of S-CCD is 0.793 with 20%
omission error and 21% commission error, slightly higher than that of COLD (0.789). Two disturbance sites
respectively associated with wildfire and insect disturbances are used for qualitative map-based analysis. Both
quantitative and qualitative analyses suggest that S-CCD achieves fewer omission errors than COLD for detecting
those disturbances with subtle/gradual spectral change. In addition, S-CCD facilitates a better real-time moni-
toring, benefited by its complete recursive manner and a shorter lag for confirming disturbance than COLD (126
days vs. 166 days for alerting 50% disturbance events), and reached up to ~4.4 times speedup for computation.
This research addresses the need for near-real-time monitoring and large-scale mapping of forest health and
offers a new approach for operationally performing change detection tasks from dense Landsat-based time series.
1. Introduction disturbance in an accurate and timely manner, enabling an early
warning and effective management to prevent further loss of forested
In the last two decades, linked to the recent elevated air temperature land (Rogan and Mietkiewicz, 2015).
and prolonged drought, an increase in the occurrence and severity of For decades, satellite remote sensing has been promoted as a key
forest disturbance has been documented over large parts of the globe data source for operational forest monitoring (Pasquarella et al., 2017).
(Dale et al., 2001; Seidl et al., 2017; Turner et al., 1998) for such as Particularly, the opening of the Landsat archive (Woodcock et al., 2008)
insect outbreak (Kautz et al., 2017; Paritsis and Veblen, 2011),wildfire has led to improved opportunities for characterizing forest disturbances
(Pechony and Shindell, 2010; Westerling, 2016) and drought (Allen from a long-term and consistent Landsat time series (Zhu, 2017).
et al., 2015). Forest disturbance events directly emit carbon to the at- Compared to coarse-resolution datasets such as Moderate Resolution
mosphere through oxidation and decomposition of wood (Masek et al., Imaging Spectroradiometer (MODIS, 250–1000 m resolution), Landsat-
2008), and yield significant impacts on ecosystem services of national based time series are provided in a sufficient temporal length of 40-year
forests such as climate regulation and biological diversity conservation global record of finer-resolution observations (30 m) (Masek et al.,
(Curran and Trigg, 2006). Therefore, it is important to systematically 2013). Therefore, Landsat data are often perceived as the best free-
gather information regarding the extent, timing and magnitude of forest access remotely sensed data source for resolving the full range of
* Corresponding author.
E-mail address: sye@clarku.edu (S. Ye).
https://doi.org/10.1016/j.rse.2020.112167
Received 22 March 2020; Received in revised form 14 September 2020; Accepted 26 October 2020
Availableonline5November2020
0034-4257/© 2020 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license
(http://creativecommons.org/licenses/by-nc-nd/4.0/).

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
disturbance occurrence (Cohen et al., 2017; Cohen et al., 2016; Kennedy our tests. The high computational requirement imposes limits on the
et al., 2014; Ye et al., 2018). Recently, the release of Landsat Analysis application of COLD for a wide range of scientific research, especially for
Ready Data (ARD) has eased automation for monitoring large-scale a large-area mapping such as at a state or continental scale. The cause for
forest disturbances (Dwyer et al., 2018). The Landsat ARD gridded all the slow speed is due to the per observation updating approach Zhu et al.
available Landsat-4 and -5 TM, Landsat-7 ETM+ and Landsat-8 OLI/ (2020). For example, if the time series of a single pixel has 500 clear
TIRS to an Albers Equal Area (AEA) Conic map projection, and are observations, COLD needs to re-train the model using the ‘Least Absolute
consistently geo-registered and atmospherically corrected, and hence Shrinkage and Selection Operator’ (LASSO) algorithm for approximately
holds the highest level of scientific standards and processing required for 500 times to complete a detection for this pixel. Computational re-
immediate use (Zhu, 2019). The Landsat ARD requires the minimum of dundancies arise from reconstructing models from scratch for each new
user effort for data preprocessing, greatly facilitating a large-scale and observation being added to the time series. Second, the former version of
long-term time series analyses (Dwyer et al., 2018). COLD, namely CCDC, was designed to detect abrupt land cover change,
A wealth of methodologies on satellite-based time series analysis and is less helpful for detecting those disturbances that yield small to
have been developed for land cover change detection and character- medium spectral change magnitude (Brown et al., 2019; Cohen et al.,
ization (Kennedy et al., 2010; Verbesselt et al., 2010a; Zhu and Wood- 2017; Zhu et al. (2020)). A possible reason provided is that CCDC
cock, 2014b; Zhu et al., 2012). These approaches are often categorized identifies gradual changes as the slope in the harmonic regression model
based upon their monitoring strategies: offline or online monitoring as opposed to attributing them to a change on a specific date (Bullock
(Bullock et al., 2019; Zhu, 2017). Offline monitoring focuses on a et al., 2019). Though this issue was alleviated by COLD, it has not been
retrospective analysis when the collection of time series data is fully solved yet as evident by the only 60% producer accuracy for the
completed, and seeks to reconstruct forest disturbance history. The disturbance category ‘stress’ Zhu et al. (2020). Third, within the current
representative approaches for this category include LandTrendr (Ken- workflow of COLD, near real-time monitoring is not fully operational
nedy et al., 2010), DBEST (Jamali et al., 2015) and the ensemble because: 1) COLD is a memory-intensive algorithm which requires
approach (Bullock et al., 2019). Online monitoring is applied to a loading all images to update model coefficients and to calculate
practical scenario that the new observations are successively collected temporally-adjusted RMSE for each new observation; 2) certain steps of
and processed in a timely fashion, and hence can be used for near real- COLD such as minimum RMSE require data inputs collected after the
time monitoring. Representative approaches for online monitoring are current monitoring date, which does not satisfy the need of near real-
Breaks for Additive Season and Trend Monitor (BFAST Monitor) algo- time monitoring. A recursive transformation for these steps can free
rithm (Verbesselt et al., 2012) and Continuous Change Detection and the system from loading all historical images each time for a new
Classification (CCDC) (Zhu and Woodcock, 2014b; Zhu et al. (2020)), observation, greatly improving computational efficiency for a near real-
though they are also applicable for offline monitoring. The BFAST was time scenario.
originally designed for temporal segmentation of MODIS-based time Currently, most operational near real-time products are based on
series (Verbesselt et al., 2010a), and was later modified (BFAST MODIS system, such as Terra-i (Reymondin et al., 2012) and FORMA
Monitor) to address near real-time detection for drought-related vege- alert system (Hammer et al., 2014). To our knowledge, Global Land
tation disturbance (Verbesselt et al., 2012). BFAST Monitor is a uni- Analysis and Discovery (GLAD) is the only operational system providing
variate approach that uses a single spectral band or index, while it has a near real-time monitoring of forested land at a Landsat-pixel scale
been reported that multiple bands or indices are more preferable (Hansen et al., 2016). GLAD applies pre-trained decision trees models to
because forest disturbance has a multi-spectral expression requiring classify clear observations and labels an alert if two or more out of four
multi-band inputs (Cohen et al., 2017; Zhu et al. (2020)). consecutive observations were classified into the disturbance category.
CCDC is a multivariate time-series model that uses all available As this product is designed and implemented only for tropical evergreen
Landsat 4–8 data for change characterization and land cover classifi- forest and no phenological variation is considered in the system (Hansen
cation (Zhu and Woodcock, 2014b). The CCDC first applies the Fmask et al., 2016), its performance is unknown yet for those middle/high-
(Zhu and Woodcock, 2012) and Tmask algorithm (Zhu and Woodcock, latitude regions where disturbances signals are often spectrally similar
2014a) to screen clouds, cloud shadows and snow, and then build a to seasonal leaf drop.
harmonic model for each spectral band based on remaining clear ob- In this study, we describe a new algorithm called ‘Stochastic
servations. A breakpoint indicative of the timing of the disturbance is Continuous Change Detection’ (S-CCD) that is developed to universally
identified when the minimum discrepancy between actual and predicted detect forest disturbance from Landsat time series in a recursive fashion.
reflectance of spectral bands for a monitoring window is greater than a S-CCD introduces the state space theory into the current framework of
predefined change threshold (Zhu and Woodcock, 2014b). Recently, an COLD, aiming to address three objectives: 1) to enhance detection ac-
improved algorithm called ‘COntinuous Monitoring of Land Dis- curacy, especially for those forest change with small spectral change
turbance’(COLD) was developed based upon CCDC Zhu et al. (2020). magnitudes while keeping a low rate for commission errors; 2) to pro-
COLD introduced several improvements such as disturbance extraction, vide an operational framework for near real-time monitoring; and 3) to
temporally-adjusted Root Mean Square Error (RMSE), and change an- improve computational efficiency, enabling a long-term time series
gles for disturbance confirmation Zhu et al. (2020). An important analysis for a large-area forest disturbance characterization.
finding for COLD is that using the highest frequency for harmonic model In what follows, we first provide an intuitive explanation for state
updates, that is per observation instead of per a time span for the CCDC, space models and the Kalman filter as the mathematical foundation of S-
can reduce ~20% commission errors Zhu et al. (2020). Zhu et al. (2020) CCD (Section 2), describe our S-CCD algorithm focusing on different
tested the performance of COLD using 7200 Landsat time series plots steps with COLD (Section 3), introduce our reference dataset and vali-
randomly selected across the conterminous United States, and reported dation metrics (Section 4) and exhibit the results for both quantitative
that the COLD algorithm achieves a higher accuracy than CCDC (~20% and qualitative evaluation (Section 5), and finally discuss advantages
commission and ~ 82% omission, see (Cohen et al., 2017), with 27% and future work for S-CCD (Section 6). Of particular note is that Section
omission and 28% commission error for a variety of land disturbance 5.3 presents a high-performance software package for both S-CCD and
types. COLD implemented in C language.
However, while the COLD algorithm has achieved improved per-
formance for change detection accuracy, there are several issues limiting 2. State space model and the Kalman filter
its implementation for operational monitoring. First, COLD is compu-
tationally expensive: the original MATLAB software takes ~5000 The new approach built upon the State Space Model (SSM), an
computing hours for a Landsat ARD tile (1–3 thousand images) based on established time-series mathematical framework that allows for
2

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
modeling a dynamic of observed measurements as being explained by a Where ξ is a process noise item for the trend. The ‘cycle’ process
vector of latent state variables. The SSM has two foundational ‘sto- requires two state variables to define:
chastic’ assumptions: 1) observations are formulated as a sum of a sto- (cid:0) )
chastic item linked to the uncertainty within the data themselves, c t+1 =c t cosλ c +c* t sinλ c +ω t ,ω t ̃N 0,σ2 ω (4)
n
‘s
a
ta
m
te
e
s
ly
’ (
‘
α
o
t
b
);
s e
2
r
)
v
s
a
ta
ti
t
o
e
n
s
a
w
l
h
n
i
o
c
i
h
s e
a
’
r e
(ϵ
e
t)
v
,
o
a
l
n
vi
d
n
a
g o
v
v
e
e
ct
r
o
t
r
im
of
e
l
a
a
s
t e
a
n
s
t
t o
v
c
a
h
r
a
ia
s
b
ti
l
c
e s
p r
c
o
a
c
ll
e
e
s
d
s c* t+1 = (cid:0) c t sinλ c +c* t cosλ c +ω* t ,ω* t ̃N
(cid:0)
0,σ2 ω*
)
(5)
with being affected by a ‘process noise’ (η t). Different from classical Where λ c is the frequency of the cycle, ω t and ω t* are independent
decomposition models such as harmonic regression used in BFAST and process noise items. ct is the primary cycle state, while ct* is an accessory
CCDC, SSM allows for trend and cycle components to be evolving state variable that is not included for prediction of yt and only used to
randomly rather than deterministically (see Fig. 1), hence we called it as enable a recursive form of mathematical computation (so its corre-
‘Stochastic Continuous Change Detection’. sponding element in Z is 0). For a classic model for ‘trend +annual cycle
The general Gaussian SSM can be written in the form as below +semi-annual cycle’, the state vector at can therefore be given as [μ t,ct,
(Durbin and Koopman, 2012): annual,ct, annual*,ct, semi,ct, semi*].
Observationequation:y t =Za t +ϵ t ,ϵ t ̃N(0,H) (1) The Kalman filter is the most common tool providing an operational
treatment for SSM. The Kalman filter was first developed for estimating
Stateequation:a t+1 =Ta t +η t ,η t ̃N(0,Q) (2) real-time trajectory of the spacecraft for the Apollo program (Schmidt,
1981), and was later introduced to other application domains such as the
Where yt is the observation at time t, ϵ t and η t are two mutually in- control of linear systems (Davis and Vinter, 1985) and econometric
dependent random variables that follow a normal distribution with
modeling (Pasricha, 2006). Recently, the Kalman filter was applied to
mean 0 and variance H, and variance Q, respectively. Z is a system
improve satellite-based time series analysis for applications such as crop
matrix in a binary form, which indicates those state items that directly
phenology estimation (Vicente-Guijalba et al., 2014), synthetic NDVI
contribute to the observation. T is a transformation matrix defining how
image generation (Sedano et al., 2014) and near real-time monitoring of
a state vector evolves over time (mathematical definitions for Q, Z and T
defoliation (Olsson et al., 2016). The Kalman filter is claimed to produce
are detailed in the appendix). State space representation is central to
an optimal estimate in the sense that it always reaches the minimum
statistical treatments for structural time series models, owing to its
mean square error, and is capable of predicting measurements in a
ability of allowing for structural components to be modeled explicitly by
recursive manner so that new measurements can be immediately pro-
state variables (Brockwell and Davis, 2013; Durbin and Koopman,
cessed as they arrive (Durbin and Koopman, 2012; Kalman, 1960). As
2012). Therefore, SSM holds great promise for processing remote
such, the Kalman filter has great potential for being a fundamental tool
sensing time series, which are well known for the structure of ‘trend +
of satellite-based near real-time monitoring.
cycles’ (Eastman et al., 2013; Verbesselt et al., 2010b; Zhu and Wood-
Fig. 2 explains how the Kalman filter recursively adapts its model
cock, 2014b). coefficients and prediction. When a new observation, ‘2000-12-27’, is
The SSM for the state of ‘trend’ is formulated as a random-walk
introduced into the time series, there is a discrepancy between the one-
model:
ahead-step prediction (the solid orange dot) and the new observation
(cid:0) )
μ t+1 =μ t +ξ,ξ̃N 0,σ2 ξ (3) (the green cross) called ‘innovation’. In a Kalman filter, the ‘innovation’
can be divided into two components: 1) observational noise; and 2)
Fig. 1. The comparison between a harmonic regression model (A) and a state space model (B) for fitting curves. The harmonic regression model has a rigidity for
consistent coefficients such as intercepts, slope and Fourier coefficients, while the state space model assumes that each component is evolving as a stochastic process
so that the model coefficients vary over time.
3

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 2. An intuitive explanation of Kalman filter based on a Landsat time series. When a new observation at the date of ‘2000-12-27’ is introduced to the system, the
Kalman filter measures the difference between the actual observation (the green cross at ‘2000-12-27’) and the predicted value (the green dot), namely ‘innovation’.
The fitting curve for the model will be adjusted to align with the optimal estimate for the current states (the ‘blue dot’) by filtering out ‘observational noise’ from
‘innovation’. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
model updates brought by the new observation. The Kalman gain is the 3.1. Build initial model
relative weight assigned to actual model updates, which can be esti-
mated by covariances of states and observational noise. Once the Kal- After a clear time series is prepared by Fmask (Zhu and Woodcock,
man gain is computed, the Kalman filter will use it to filter out 2012), initialization model window and Tmask (Zhu and Woodcock,
observational noise from the innovation. The new model coefficient can 2014a), S-CCD needs to seek a stable stage to define a statistical refer-
be then adjusted to align with the remaining part, namely ‘filter states’ ence for change identification which adopts the stability test and
(the blue dot), yielding a new fitting curve (the dashed orange line). The ‘looking back’ procedure Zhu et al. (2020). The subtle modification for
filtered states (or adjusted coefficients) will be used to predict the next S-CCD is that we used 18 instead of 12 as the required minimum number
observation. of clear observations for an initialization window (i.e., the window
Vegetation dynamics often exhibit a complex trend, which is not defining a stable stage to initialize continuous modeling): our new
guaranteed to be adequately approximated by a single linear mode approach assumes a fixed structure of ‘trend +annual +semiannual’ for
(Burkett et al., 2005; Zhao et al., 2019). The assumption for stochasti- a time series which can be equivalent to 6-coefficient harmonic model.
cally varying states for SSM and Kalman filters avoids the rigidity of The suggested minimum observation window for a LASSO regression is
classical decomposition that assumes the stationarity of linearity and ‘number of coefficients * 3’, hence the minimum observation number is
seasonality, hence complex dynamics from time-series data are uncov- set as 18. The reason for using a 6-coefficients model instead of a tri-
ered and more local fluctuations can be captured (Brockwell and Davis, modal component (8-coefficient model) is discussed in Section 6.
2013). The flexibility of dynamic modeling directly leads to better
fitness of the model, and hence potentially increases the sensitivity of 3.2. State space model (SSM) initialization
the model to subtle changes because change magnitudes are often
calculated relative to measurement of model fitness such as Root Mean In S-CCD, an additional step is needed to initialize the parameters
Square Error (RMSE). Other advantages of a state space analysis for and the structural elements for state space models before the continuous
satellite-based time series include: 1) simple mathematical treatment of monitoring starts. The initial SSM parameters include observational
missing data (shown in Appendix) which is critical for dealing with noise (H), process noise (Q), initial states (a0) and initial covariance (P0).
satellite-based time series known for its temporal irregularity; 2) explicit The parameters H and Q are the two most important SSM parameters,
consideration for measurement uncertainties for the noisy nature of representing the uncertainty level for observations and each stochastic
remote sensing data; 3) high computational efficiency due to its recur- process. They are often estimated by maximizing likelihood through a
sive form. Quasi-Newton numerical searching algorithm in literature (Durbin and
Koopman, 2012; Helske, 2016). However, after initial tests, we learned
3. Method that the Quasi-Newton algorithm was inefficient for processing millions
of pixel-based time series. To overcome the issue, we designed a fast
The workflow of S-CCD, which consisted of data preparation, model method for estimating H and Q, and a new method for estimating a0 and
initialization and continuous monitoring, is presented in Fig. 3. We used P0 based upon initial LASSO regression (this fast procedure was detailed
five spectral bands of surface reflectance products (green, red, NIR, in Section S1 in the supplementary material).
SWIR1 and SWIR2) as the algorithm inputs because Zhu et al. (2020)
reported that these five spectral inputs alone can achieve the best per-
3.3. Temporally adjusted peek window
formance compared to being combined with vegetation indices. We
applied the same steps as COLD for S-CCD for data preparation, for
Like all CCDC-like approaches, for each newly-collected clear
which we refer to Section 3.1.1 of Zhu et al. (2020).
observation, S-CCD compares predictions and actual observations based
4

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 3. The workflow of the proposed Stochastic Continuous Change Detection (S-CCD). Same as the original COntinuous Monitoring of Land Disturbance (COLD),
the workflow consists of three stages: 1) data preparation, 2) model initialization, and 3) continuous monitoring. The different steps between S-CCD and COLD are
highlighted as yellow polygons. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
upon a number of consecutive anomaly observations, called the ‘peek The defaulted consecutive number consedef =6. The min_peek_days is
window’ (Davis et al., 2017). COLD approach determines the number of related to the temporal span for that a disturbance event can yield effects
consecutive observations via calculating the median revisit days across over the vegetation. If min_peek_days is set to be too long, signals of a
the entire time series. If the median revisit days are shorter than normal disturbance might be affected by post-disturbance forest regrowth; if too
Landsat temporal density (16 days), more consecutive observations need short, some irrelevant ephemeral changes such as soil moisture change
to be included, and the probability threshold that all observations need might be misidentified as disturbance. We explored the algorithm per-
to exceed is decreased to compensate Zhu et al. (2020). This approach formance by using several min_peek_days below the normal peek window
requires an entire time series to compute median revisit days. We width (e.g. 60, 70, 80 days). Choosing min_peek_days as 80 days shows
developed a completely online approach for adjusting the peek window the best result (see Fig. S1 in the supplementary material). The threshold
for S-CCD. The number of observations for an temporally-adjusted peek probability is also adjusted when a peek window chooses a consecutive
window is defined as the minimum number satisfying 1) minimum observation number larger than consedef, following Eq. S4 in Zhu et al.
consecutive observations, i.e., consedef; and 2) the minimum temporal (2020).
span for a peek window (min_peek_days): Another advantage of the new peek window in terms of COLD
{ } approach is making it feasible to account for variability in Landsat
conse def =min x|x≥conse def andspan(x)≥min peek days (6) observation frequency across not just space, but also time. Time series
5

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
segments collected in the early days (e.g. before the launch of Landsat 7 3.5. Confirm change using angular spread
ETM+ on 1999) often have a lower temporal density than the most
recent collections. Large changes in frequency driven by the number of Ephemeral and systematic noise may also lead to relatively large
active sensors aboard Landsat satellites had an influence on the CCDC/ change magnitudes for all observations within a peek window. The
COLD change detection records (Brown et al., 2019): higher detection disturbance signal, however, should have a consistent change direction
rates often occur at higher observation frequency particularly after the for multispectral surface reflectance bands. Therefore, the time series
launch of Landsat 8 OLI, including commission errors brought by model needs to confirm the change from the consistency of change an-
ephemeral forest change. The new peek window considers that the gles once the Chi-squared distribution test is passed. COLD confirms
consecutive number is not fixed throughout the detection for a single breaks using the mean included angle between pairs of neighboring
time series and enables an adjustment of consecutive observations based change vectors smaller than 45 degrees. We found that this strategy is
upon the local temporal density for the peek window, because it defines sensitive to outliers: for example, if there is an outlier in the six
the peek window according to the physical attribute of a disturbance consecutive observations, two out of five neighbor pairs will be affected
signal, namely lasting days, not satellite observation count. by this outlier (40% of the candidate angles); if there are two outliers in
a peek window, more than half of neighbor pairs are biased. We
designed a new change angle index called ‘angular spread’, referred as
3.4. Recursive temporally-adjusted RMSE
the angle between each standardized change vector for nth observation
Squared differences between predictions and observations are used
(SCVn) and the median standardized change vector (MedSCV). The me-
to evaluate deviation of the current peek window from the ‘stable stage’. dian change vector here is used to represent the average of the spectral
response of a disturbance. Ideally, the observations for a disturbance
RMSE is used to normalize the square difference, which is critical for
should concentrate around the median change vector. We define ‘Mean
decisions on the occurrence of breakpoints. Considering that RMSE often
Angular Spread’ for a peek window (Eq. 10) to represent the average
exhibits a yearly pattern over the whole time series (Zhu et al., 2015),
angular departure of each candidate change vector to medium change
the COLD algorithm employs a temporally-adjusted RMSE that is
vector. We compared the performance of the mean included angle as 45
calculated based on the temporally closest 24 observations to the peek
degrees (the COLD approach) and the mean angular spread with 30, 45
window. For operational near real-time monitoring, this temporally-
degree. The best result is achieved by using mean angular spread as 30
adjusted RMSE needs to be re-computed by loading all images back
degrees (Fig. S2 in the supplementary material). The advantage of ‘Mean
into the model for a new observation. We designed a novel recursive
Angular Spread’ is that is less sensitive to outliers existing in a peek
method based upon two histograms respectively for clear observation
window. For example, an outlier only affects a single change angle out of
counts (Fig. 4A) and square of RMSE (Fig. 4B) for Days of Year (DOY),
six angles for a default peek window (16.7% of the candidate angles).
which eliminates the need of processing all images for each new
o
6
b
1
s
b
er
in
v
s
a t
i
i
n
o n
t
.
o t
B
a
o
l.
t h
T h
h
e
is t
t
o
w
g
o
r a
h
m
is
s
t o
a
g
re
ra
d
m
e
s
fi n
ke
e
e
d
p
a
u
s
p
a
d
b
a
i
t
n
in
w
g
i
o
d
n
th
c e
o f
a
6
n e
d
w
ay
o
s,
b
a
se
n
r
d
-
MeanAngularSpread=
con
1
se adj
∑ c
n
o
=
n
1
seadjθ(SCVn,MedSCV )<30◦ (10)
vation is available. To compute a temporally-adjusted RMSE for a new
observation, S-CCD will start from the bin at the middle date of the peek
3.6. Update model using the Kalman filter
window (‘Step 1’ in Fig. 4A), and expand the searching window by an
increment of one bin on the left and the right side each time, until the
For those observations that are identified as being unchanged, non-
window includes ≥24 observations (‘Step 3’ in Fig. 4A). The temporal
consecutive outlier removal will be used with a change probability of
RMSE is computed as the average RMSE*RMSE of the resultant window
0.99999 (same as Zhu et al. (2020)). If the observation passes the outlier
based on the count and the temporal RMSE histogram.
test, it will be inputted to the system to update the model using the
Likewise, to enable near real-time monitoring, we used a dynamic
Kalman filter (see the Appendix). Instead of rebuilding LASSO regression
minimum RMSE (or temporal lag-1 madogram), instead of a static
each time, the Kalman filter has an extremely simple mathematical
minimum RMSE used in Zhu et al. (2020), to define the minimum value
treatment for updating models.
of RMSE for each band: the madogram is updated each year using all
clear past observations.
3.7. Disturbance identification
Therefore, the new RMSE for S-CCD is computed as (b is bth Landsat
band):
Breakpoints detected by the above procedure are not necessarily
(cid:0) )
RMSE b =max recursive temporal RMSE b ,dynamic min RMSE b (7) associated with forest disturbance, but maybe forest recovery. As the
final step, we need to single out those breaks that are related to forest
For an observation n in a peek window, we define the Standardized health decline led by disturbance. A typical forest disturbance will cause
Change Vector (SCVn) as the difference between its multispectral lower NIR, higher Red and higher SWIR values. Such spectral change,
reference and its one-step-ahead predictions relative to RMSE using the however, might be asynchronous. For example, when a forest is attacked
five bands (namely green, red, NIR, SWIR1 and SWIR2): by mountain pine beetle, the increase of SWIR often occurs first due to
⎡ ⎤
increased water stress, then is the increase of the red band, and finally
SCV n =⎣ y n R ,1 M (cid:0) S ̂ E y n 1 ,1, y n R ,2 M (cid:0) S ̂ E y n 2 ,2,⋯ y n R ,5 M (cid:0) S ̂ E y n 5 ,5 ⎦ (8) t in h d e e N x I c R a l b le a d n d ‘ d d is e t c u r r e b a a s n e c s e o e w vi i d n e g n c t e o ’ n (s e e e e d l E e q d . r 1 o 1 p ) . b H a e s n e c d e , o n w e t h c e r e m at e e d d i u a m n
Standardized Change Vector (MedSCV, defined in Section 3.5). ‘Distur-
Similar to the COLD algorithm, the change magnitude (CM) is used as bance evidence’ aims to provide a combined analysis for multiple bands
the indicator of breakpoints, which is calculated as the minimum norm instead of a single band index. The breaks that are identified as being
of SCVn for a peek window. CM follows the Chi-squared distribution with disturbance-related need to have a disturbance evidence larger than
k degree of freedom Zhu et al. (2020), where k is the number of the used zero:
spectral bands, namely ‘5’. A breakpoint candidate is identified if the CM
Disturbanceevidence=MedSCV (cid:0) MedSCV +MedSCV >0
meets the condition, where P refers to all observations within the peek RED NIR SWIR1
window: (11)
{ }
CM=m n∈ i P n ‖SCV n ‖2 ̃χ2(k)>χ2 threshold (5) (9) W wi e t h c o th m re p s a h r o ed ld s ‘D 0 i , s t (cid:0) ur 0 b . a 0 n 1 c , e (cid:0) E 0 v . i 0 d 2 e , n a ce n ’ d w (cid:0) it 0 h . 0 C 3 O . L ‘D D i s d tu is r t b u a r n b c a e n E c v e i d e e x n tr c a e’ c t h io ad n
a higher F1 score than all other COLD disturbance extraction methods at
6

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 4. The explanation for a recursive calculation of temporal RMSE: the algorithm searches a window that just covers ≥24 observations by an increment of a bin on
both sides in an observational count histogram (Fig. 4A). Once it stops (Step3 in Fig. 4A), the temporal RMSE is computed as the average RMSE*RMSE within the
resultant searching window.
all five thresholds (see Fig. S3 in the supplementary material). Zhu et al. (2020)). These forest plots were separated into 2704 undis-
turbed plots and 1078 disturbance plots with 1413 disturbance occur-
3.8. Disturbance probability rences in total (some plots have successive disturbance occurrences such
as fire and timber harvest). Among these disturbance occurrence, the
For a scenario of near real-time monitoring, disturbance probability most causal agent of disturbances is harvest (n = 903), followed by
provides a fuzzy disturbance membership for a newly collected obser- mechanical (n =149), stress (n =141), fire (n =127), and others (n =
vation if the occurrence of a disturbance event has not been confirmed. 83, e.g., hydrology, wind, debris, land use change). For a detailed
Unlike GLAD (Hansen et al., 2016), COLD Zhu et al. (2020) and NRT- description of these disturbance causal agent classes, we refer to (Cohen
CCDC (Tang et al., 2020) which calculates a ratio of current consecu- et al., 2016). The spatial distribution of Landsat plots labeled as undis-
tive anomaly observation count (i.e., the observations that has a change turbed or the number of disturbance occurrences is shown in Fig. 5. We
magnitude larger than the threshold) to the total required count, S-CCD randomly selected 50% of the reference samples (1891 Landsat plots) for
computes disturbance probability as a ratio of ‘anomaly days’ to the algorithm development and parameter calibration. The other 50% of the
required days for a confirmation (namely min_peek_days), given that the reference samples were used as a holdout validation set to evaluate the
peek window in S-CCD is defined as natural days, not observation count. comparative performance of S-CCD and COLD.
‘Anomaly days’ is defined as the temporal span for current consecutive Considering that different algorithms may have different sensitivities
anomaly observations since the last ‘stable’ observation (as days). to disturbance magnitudes based on change probability thresholds, the
Disturbance probability have important implications for early manage- omission and commission rates based on a series of change probability,
ment decision prior to statistically confirming a disturbance event, namely 0.90, 0.925, 0.95, 0.975, 0.99, were chosen for accuracy
which will be discussed later in Section 5.3. assessment. The overall performance is evaluated using the F1 score,
because it provides a balanced assessment for omission and commission
4. Study area, data and performance evaluation rates. The definition of omission, commission rates and F1 score are the
same as Zhu et al. (2020).
Our performance evaluation for algorithms consisted of 1) quanti- (1(cid:0) commission)*(1(cid:0) omission)
tative accuracy assessment against a comprehensive national forest F1score=2* 2(cid:0) commission(cid:0) omission (12)
disturbance dataset, 2) qualitative evaluation based on large-scale
assessment for two selected disturbance sites and 3) timeliness anal- Qualitative map-based comparisons are performed to compare the
ysis for their near real-time implementation. For quantitative accuracy performances of two algorithms for a large-area monitoring. We chose
assessment, a benchmark forest disturbance database was chosen that two Landsat ARD tiles that were respectively affected by fire and insect
includes 3782 Landsat-based forest plots across the conterminous disturbance. The fire site sits at the San Juan and Rio Grande National
United States (US) for which their disturbance timing and types have Forests in southwestern Colorado, where Papoose fire burned 200 km2
been well-interpreted from multiple data resources (Cohen et al., 2016; of forested in June and July 2013 (Verdin et al., 2013). The burned area
7

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 5. The spatial distribution of 3782 reference sites, and two Landsat ARD scenes chosen as the study areas. The reference sites include 2704 undisturbed plots
(‘white circles’) and 1078 disturbed plots (red circles), which were collected using a stratified sampling based on the ecoregions across the United States. There are
1413 disturbance occurrences in total, and the disturbance categories were dominated by the disturbance category ‘Harvest’ (63.9%), followed by ‘Mechanical’
(10.5%) and ‘Stress’ (9.9%). Landsat ARD 10/10 is located in the south Colorado including a region where Papoose fire happened in 2013; Landsat ARD 30/6 is
located in the New England, including a site affected by gypsy moth infestation in 2016 and 2017.
was dominated by Engelmann spruce (Picea engelmannii) and Subalpine 6 in recent 10 years (2010–2019) were downloaded and preprocessed.
fir (Abies lasiocarpa) (Carlson et al., 2017). Caused by lightning, the The Aerial Detection Survey (ADS) data1 were used as reference dataset.
Papoose fire starts on June 19, 2013, spread with a southeast direction, The ADS data are polygon-based forest health maps from visually-
and was considerably dampened by precipitation on July 19, 2013 defined polygons for a variety of specific insects and disease, annually
(Cyphers et al., 2019; United States Department of, 2014). All Landsat reported by United States Department of Agriculture (USDA). It was
ARD images between 1996 and 2019 (25 years) were downloaded for reported that the recent ADS (after 2012) reached a high-level agree-
analysis (ARD Tile Grid 10/10). A fire perimeter map for this specific fire ment to ground-collected reference data (4% omission and 5% com-
provided by GeoMAC mapping application (https://rmgsc.cr.usgs. mission for defoliation damage types) (Coleman et al., 2018). Generally
gov/outgoing/GeoMAC/) was used as our reference map. Directed by speaking, in spite of its relatively coarse minimum mapping unit as 5 ha,
United States Geological Survey (USGS), GeoMAC updates the fire the ADS data are a valuable source for indicating spatial distribution for
perimeter data based upon inputs from incident intelligence sources, forest disease at a broad scale (Hart and Veblen, 2015; Preisler et al.,
GPS data, infrared imagery from satellite platform (Walters et al., 2011), 2012) and the timing of disease occurrence, especially for the recent
and provides the most accurate perimeter map for this fire to our best disturbances that occurred after 2012.
knowledge. To evaluate the timeliness in a scenario of near real-time monitoring,
The second disturbance site was chosen for gypsy moth (Lymantria we applied a metric called as “alert-lag relationship curve” (Tang et al.,
dispar) infestation in Southern New England, which covers southern 2019). Like most time series algorithms, COLD and S-CCD both require a
Massachusetts, northeast Connecticut, and northwest Rhode Island. This confirmation of a disturbance signal using consecutive observations,
is a peri-urban region with 56.7% forest cover (i.e., 34.8% hardwood, which may cause a lag for alerting disturbance in practice. We defined
17.8% mixed and 4.1% conifer), and 26.7% developed area and 10.8% the alert lag as a delay between the beginning disturbance date and the
wetlands. This study area contains the locations that experienced from date for confirming the disturbance. In practice, ‘the beginning distur-
gypsy moth outbreak that started in 2015, spiked in 2017 (Pasquarella bance date’ in this study was estimated as the first Landsat observation
et al., 2018). A gypsy moth infestation can consume a large quantity of for a change signal of forest disturbance. Though the first Landsat
foliage and sometimes causes a near-total defoliation over a season or observation signaling forest disturbance will not always coincide with
two (Townsend and Eshleman, 2004), but often starts to recover very the beginning of disturbance, they are the best resources for estimating
soon for the following year, so the change signal is commonly ephemeral the beginning disturbance date in a consistent way, given that reliable
(Vogelmann et al., 2016). In addition, infested stands typically consist of historical resources are often missing for disturbance-date response
two or more dominant tree species and are often represented by multi- design. Due to that disturbance timings in our reference dataset were
aged and multi-sized populations (Hart and Veblen, 2015), making the
detection all the more challenging because of mixed spectral response
from various tree species. All Landsat ARD images for ARD Tile Grid 30/
1 http://www.foresthealth.fs.usda.gov/portal/Flex/IDS
8

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
estimaed at an annual time step, we re-interpreted the beginning dates 5.2. Qualitative analysis
of the disturbances for randomly-selected 500 disturbance plots (~50%
of the total disturbance plots, 665 disturbance events in total), based on For qualitative comparison, S-CCD and COLD were implemented to
a visualization of each plot-based Landsat time series. An alert-lag detect timing of forest disturbances respectively for Papoose fire and
relationship curve was made based upon this date-level reference gypsy moth infestation. A consistent probability threshold as 0.95 was
dataset to explore and compare disturbance detection rates, i.e., the applied for both algorithms.
proportion of confirmed reference disturbance events, at different lag Fig. 7 illustrates the detection results of S-CCD and COLD for the
times in a near real-time monitoring. In addition, disturbance proba- Papoose fire site. Visually, COLD and S-CCD exhibit very similar
bility maps, which can potentially provide timely information on detection results for abrupt disturbance categories such as moderate/
disturbance progression and mitigating effects of detection latency, high-severity fire. Given that this region was heavily affected by
were outputted for timeliness analysis (see Section 5.3). spruce beetle since 2010 (Hart and Veblen, 2015), we selected the
breakpoints only detected in 2013, which is the year for Papoose fire
5. Results occurrence, with an assumption that most of these breakpoints are
associated with the fire, not spruce beetle attack for that year. To assess
5.1. Quantitative accuracy assessment accuracy of timings for these breakpoints, we outputted month maps for
the breakpoints detected in 2013. The breakpoints as detected mostly
We tested COLD and S-CCD against a holdout validation set (n = occurred in June and July (see Fig. 7A and B), which are well matched
1891) using the different probability thresholds. The omission, com- with the active temporal window of Papoose fire on the historical re-
mission and F1 score (see annotation around markers) for each test have cords (Cyphers et al., 2019). To further evaluate spatial accuracy for
been shown in Fig. 6A. S-CCD outperforms COLD at lower thresholds at damage mapping, we compare two detection maps with GeoMAC fire
0.90, 0.925 and 0.95 for F1 score, while COLD is slightly better at higher perimeter map. GeoMAC contains some commission errors for mapping
thresholds at 0.975 and 0.99. The best accuracy they reached are close: fire damage areas that are actually bare lands from High-resolution
S-CCD achieve the best performance as a F1 score of 0.793 (0.95 Satellite imagery, while COLD and S-CCD both accurately labeled
threshold probability, 20.1% omission and 21.4% commission errors), them as ‘no-attack’ (see the example of Fig. 7D, E and F). It is noteworthy
while COLD reaches the best accuracy as F1 score of 0.789 (0.975 that Landsat 7 related scan-line corrector (SLC) artifacts can be both
threshold probability, 24.6% omission and 17.2% commission errors). seen in the two breakpoint month maps, where SLC-off issue caused
We also evaluated the performance of S-CCD and COLD against seven breakpoint dates to be several days to two weeks later (rounded to a
forest disturbance categories with a threshold probability of 0.95 month difference in our maps).
(Fig. 6B). As Fig. 6B shows, S-CCD and COLD have very close omission For the gypsy moth scene (Fig. 8), we compared years of breakpoints
errors for ‘Harvest’, ‘Mechanical’ and ‘Wind’; S-CCD achieved lower detected with Aerial Surveying Detection (ADS) data. Most disturbance
omission error rate in the disturbance category ‘Stress’ and ‘Fire’, but is events detected by COLD and S-CCD were concentrated at the deciduous
worse in ‘Hydrology’ and ‘Other’. Surprisingly, the two approaches both forest cover regions of the 2016 NLCD map. The disturbance years
have relatively high omission errors for ‘fire’ disturbance, which is often indicated by two algorithms matched that of the ADS data (primarily the
known for causing large change magnitude from satellite images (Cohen year of 2016 and 2017). This finding is consistent with the historical
et al., 2016). The possible explanation can relate to some low-severity/ record that a major outbreak began in early summer 2016, led by a series
underground fire cases are included in the reference dataset, which of unusually dry springs (2014–2016) (Pasquarella et al., 2017).
caused only subtle spectral change magnitude. Admittedly, both algorithms yield much fewer affected regions than that
Fig. 6. Quantitative accuracy assessment results of COLD and S-CCD based on a holdout reference sample set (n =1891). A) depicts omission, commission errors
using a series of probability thresholds as 0.9, 0.925, 0.95, 0.975 and 0.99. The F1 score is used to evaluate the overall accuracy combining omission and commission
errors, annotated around each marker. B) reports the omission errors of COLD and S-CCD for each disturbance category (note that the extremely low error rate for
‘Wind’ is due to that its samples number (n =13) is too small).
9

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 7. Qualitative comparison for Papoose fire site (Landsat ARD 10/10) in Southeast Colorado among COLD (A), S-CCD (B) and GeoMAC fire perimeter map (C).
COLD and S-CCD both use the probability threshold as 0.95. The colour for A) and B) denotes the month of breakpoints detected in 2013: the spectrum ranging from
red to blue corresponds to months of breakpoints from January to November; the white are no-attack regions in 2013. D), E) and F) shows an example region that
COLD and S-CCD both accurately delineated a non-attack bare land while GeoMAC over-detected it as fire region. (For interpretation of the references to colour in
this figure legend, the reader is referred to the web version of this article.)
the ADS. Considering that Pasquarella et al. (2017) got the same result algorithm requires to confirm the occurrence of a disturbance. Gener-
for their study in the Southern New England region, those omission er- ally, S-CCD exhibits higher detection rates of disturbance than COLD
rors might be due to commission errors in aerial sketch mapping. For given the same lag day (steeper curve), indicating that it is practically
comparative analysis, we found that COLD missed some regions affected faster for alerting disturbance for a scenario of near real-time moni-
by gypsy moth (e.g., the dashed blue circle in Fig. 8A), where S-CCD toring; S-CCD requires 126 days to confirm 50% of the disturbances
identifies most parts of the same region as forest disturbance. The lo- (namely 50% detection rate) while COLD needs 166 days. Both curves
cations and the disturbance years for extra regions detected by S-CCD plateaued at a detection rate of ~75%, which were caused by that the
have a general agreement with the ADS data (see the dashed circle in two algorithms missed detection for a proportion of reference break-
Fig. 8C), proving that these extra breakpoints detected by S-CCD for this points. To compare with other MODIS-based near real-time algorithms,
region are related to forest damage caused by gypsy moth. We further S-CCD requires the same days (i.e., 126 days) to achieve 50% detection
visualized time series of NIR band for a sample pixel that COLD and S- rates as NRT-CCDC which uses daily MODIS observations, but longer
CCD got conflicted detection results (Fig. 8F and G), and identified an than the days required by Fusion 2 (i.e., 82 days) which combines
occurrence of forest disturbance signal associated with a significant drop Landsat and MODIS daily observations for a disturbance detection (Tang
of NIR band within the temporal window of gypsy moth attack, and et al., 2019).
hence confirmed that the extra breakpoints detected by S-CCD were not Fig. 10 shows a gradient of disturbance probabilities for an example
commission errors. of gypsy-moth-affected stand over a span of ~90 days since the first
disturbance signals were detected. Fig. 10 A) are the breakpoint dates
reported by a complete S-CCD, which shows that gypsy-moth attack
5.3. Timeliness analysis
occurs mostly at the dates 6-2-2016 and 6-18-2016 for this region.
Fig. 10 B) – E) shows an increasing trend of disturbance probabilities
Fig. 9 depicts the alert-lag relationship curve which indicates the
with time going by: the region generally reached over a probability of
general latency between reference disturbance occurrence dates and
0.5 over 30 days since the initial infestation signal (Fig. 10 C); a pro-
confirmation dates of the algorithms based on 500 date-level reference
portion of disturbance pixels were confirmed (see ‘light blue’ pixels)
plots. The steeper the curve appears to be, the fewer lag time that the
10

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 8. Qualitative comparison for gypsy moth site (Landsat ARD 30/6) in Southern New England among COLD (A), S-CCD (B) and the ADS reference map (C). COLD
and S-CCD both use the probability threshold as 0.95. The colour for (A), (B) and (C) denote the disturbance year indicated by each data source: the spectrum ranging
from red to blue corresponds to the years from 2011 to 2018. Fig. 8 D) and E) show an example region that S-CCD can detected out the region that COLD missed gypsy
moth damage. Fig. 8 F) and G) plots NIR time series of a sample pixel positioned at ‘black rectangle’ in D) and E) to confirm the occurrence of forest disturbance for
this region. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
over 60 days (Fig. 10 D); most disturbance pixels got confirmed after 90 from Landsat time series, which can help locate early infestation and
days (Fig. 10E). The result illustrates that the temporal span of a mitigate population expansion during its active window.
disturbance signal can be continuously indicated by disturbance prob-
abilities, which allows managers to choose thresholds based on practical
5.4. Efficiency test and software implementation
needs. For example, a gypsy moth-affected region can be potentially
determined by using a low alerting threshold (< 0.5) combined with
We implemented COLD and S-CCD in the high-performance C pro-
spatial homogeneity analysis within 30-45 days since its initial symptom gramming language. The C package named ‘S-CCD’ is downloadable
11

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Fig. 9. The alert-lag table illustrating detection rates as a function of lag time based on 500 date-level reference disturbance plots.
Fig. 10. An example of disturbance probability maps indicating disturbance progression for the near real-time monitoring. A) are the breakpoint dates from a
complete detection S-CCD for a forest stand attacked by gypsy moth on June 2016; B) – E) shows a dynamics of disturbance probabilities (represented as red colour
ramp) and confirmed disturbance pixels (light blue) every 30 days since initial attack. F) the reference high-resolution Google imagery. (For interpretation of the
references to colour in this figure legend, the reader is referred to the web version of this article.)
from https://github.com/SuYe99/s-ccd. The software implemented a To test the efficiency for C-based COLD and S-CCD, we used a
shared memory parallelization for COLD and S-CCD under a Linux/ ‘dummy’ Landsat ARD scanline which is a standard sample set of 5000
MacOS desktop environment, and has been already adapted for a High- pixel-based time series plots selected from our reference sample set. The
Performance Computing (HPC) environment. It is noteworthy that our sample set consists of 3782 forest plots and 1218 non-forest plots. To
C-based COLD has been 1.5-2.0 times faster than the original MATLAB- uncover the effects of monitoring span on the speed, we pruned each
based implementation. time series into three different lengths of time series records, that is 10
12

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
years (2008–2017), 20 years (1998–2017) and 34 years (1984–2017). COLD that assumes the rigidity of “linear trend +harmonic cycles”. We
The results are summarized in Fig. 11. S-CCD can achieve up to ~4.4 calculated the average RMSE for each band using all our 3782 samples.
times faster than the C-based COLD (with 34-year time series records). The results, as shown in Table 1, indicate that S-CCD has generally lower
With the length of records decreasing, the efficiency improvement of S- average RMSE than COLD for all seven spectral bands other than NIR
CCD over COLD declines, as ~3.5 times at 20-year time series records, and thermal bands (thermal band is not used to compute change mag-
and ~ 1.8 time faster at 10-year time series records. This is because S- nitudes for both approaches, and thereby has no effects on break
CCD improves efficiency mainly at the step of the model update; a longer detection). As the two approaches both evaluated change magnitude
time series needs a greater number for model updates to complete a relative to the RMSE, the lower RMSE means that S-CCD model is more
detection, and hence more significant efficiency improvement made by sensitive to those low-magnitude spectral changes.
S-CCD. For a standard 20-year Landsat ARD time series, our S-CCD Another obvious advantage of S-CCD is that it is a completely online
program takes only ~6 min to finish a detection for a 5000-pixel scan- monitoring algorithm, which can be directly used for near real-time
line, and ~ 500 computing hours for a Landsat ARD scene. forest monitoring. S-CCD improves several steps of COLD and enables
a continuous monitoring in a completely recursive form by using such as
6. Discussion the adjusted peek window, recursive temporal RMSE. More importantly,
the core technique for S-CCD, the Kalman filter, is a powerful real-time
The quantitative accuracy assessment indicates that the differences algorithm well known for its high computational efficiency and short-
between the best overall accuracy achieved by S-CCD and COLD are only memory requirement. For COLD, limited by its manner for re-
0.4% (see Fig. 6A, 0.793 v.s. 0.789). The primary reason is that our plot constructing the model per observation, it requires reading all images
database is generated from random sampling over a nation-wide region, into the system to rebuild harmonic curves for each new observation.
for which 63% of the forest disturbances are harvesting activities; the Instead, S-CCD just needs to update those parameter files (e.g., states
two approaches have very similar performance for detecting strong and covariance) once the initialization is finished, which can reduce
spectral signals yielded by those disturbances with medium- or high- ~95% of data inputs for monitoring each new observation.
severity and homogeneous tree damages such as harvest disturbances We reported lag-alert relationship curves which is designed to assess
(omission errors: 16% v.s. 16.2%). Our map-based evaluation for timeliness for identifying disturbance events in a near real-time scenario
Papoose fire case supports this conclusion. (see Fig. 9). Fig. 12 illustrates an example that S-CCD needs shorter lag
S-CCD, however, achieved noticeably fewer omission errors than time to confirm a change based upon a gypsy-moth-affected pixel. The
COLD for those lower-magnitude disturbances such as drought stress shorter lag is mainly attributed to the new temporally-adjusted peek
and low-severity fire (see Fig. 6b). This finding was confirmed by our window adopted by S-CCD that defines the peek window as calendar
qualitative comparison for the case study of gypsy moths. The reason days, not a fixed observation number as COLD does. COLD employs a
could be that S-CCD allows for known changes in the structure of the fixed peak window of 12 observations for this case as the median revisit
system over time, and often can achieve a better model fitting than days is 8 days (see Formula S2 in the supplementary material of Zhu
Fig. 11. The result for the efficiency test based on a dummy Landsat ARD scanline (5000 sample pixels). Each time series are pruned as three versions for time series
records, that is 10 years (2008–2017), 20 years (1998–2017), 34 years (1984–2017). The result shows that the efficiency of S-CCD was increased as the length of time
series increased, and can be up to 4.4 times faster than COLD. The CPU is Intel(R) Core (TM) i7–4790, 3.60GHz.
13

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Table 1
the average RMSE of COLD and S-CCD for each band using 3782 forest samples across the conterminous United States (the bold columns are the two bands that S-CCD
has higher RMSE than COLD).
Band Blue Green Red NIR SWIR1 SWIR2 Thermal
COLD 122.682 117.127 122.473 273.336 197.937 151.032 389.227
S-CCD 119.061 110.761 118.476 279.478 191.518 150.098 401.061
Fig. 12. A gypsy-moth example for COLD and S-CCD detecting breakpoints in a near real-time manner. The black line represents the reference disturbance date; the
dash line is the date that this change was confirmed based on consecutive anomaly observations (i.e., peek window). The date difference between the two lines
represents ‘lag time’ when the algorithm is applied to near real-time monitoring. S-CCD shows shorter lag time benefited from its temporally-adjusted peek window
defined as a fixed calendar days.
et al. (2020). When the peek window spans over a period of sparse clear following a fixed set of harmonic coefficients, thus the unexplained
observations such as June 2016 in this case, the peek window for COLD variances can be ‘ingested’ immediately by changes in structure over
has to be extended in order to incorporate enough clear observations. time. Another reason might be that we focus on forest disturbance
Differently, S-CCD defines the peek window as the minimum width of 80 detection for this study, while the trimodal component is often found to
calendar days, and hence identified the disturbance roughly one month be more useful for modeling cropland dynamics.
earlier than that of COLD, regardless of temporal density. It is also Admittedly, COLD is designed for detecting/characterizing all types
noteworthy that though S-CCD requires an anomaly peek window of at of land disturbances, not limited to forest disturbances. We tested S-CCD
least 80 days (min_peek_days) to confirm a disturbance, the outputted against a reference dataset for comprehensive land types, and reached a
metric of disturbance probability allows for an earlier and more flexible slightly lower F1 score compared with COLD (0.69 vs 0.71). Our test
decision-making process: for example, Fig. 10 shows that the pixels shows that S-CCD performs less ideal under a highly-fluctuated envi-
homogeneously presented a disturbance probability of 0.5 over 30 days ronment, and is more prone to over-detection due to those ephemeral
since the initial gypsy moth attack, making it potentially feasible to yield changes that have a high change magnitude, such as moisture change for
a disturbance alert much earlier than 80 days by applying different grassland/bare land and agricultural rotation. To alleviate this issue, our
probability thresholds. software package enables users to specify a mask for focused study area,
A possible concern is that S-CCD assumes a consistent structure of which can exclude the regions where uninterested land change occur
time series for trend, annual and semi-annual harmonic items (equal to and greatly improve processing efficiency as well. Yet, there is still much
6-coefficient harmonic models), while Zhu et al. (2020) suggested using studies that is needed to analyze characteristics of detected breaks and
a harmonic model with a maximum coefficient as 8, including trend, select breaks only linked to targeted physical processes. Another reason
annual, semi-annual and trimodal harmonic items (frequency = 1/3 for the unsatisfactory results is that we often have multiple historical
year). As such, we tested adding an additional trimodal cycle component data sources to confirm forest disturbances such as the ADS and the
into the presumed time series structure of S-CCD, and found that the best LANDFIRE products, but reliable references for the other non-forest land
F1 score decreased from 0.795 to 0.706 for S-CCD (see Fig. S4 in the disturbance are lacking. The quality of our non-forest land samples
supplementary material). In a harmonic regression, trimodal component might affect the final accuracy result. Our future work will be directed
can be viewed as an additional modifier to annual and semi-annual into 1) modifying S-CCD to accommodate other applications such as
curves (Eastman et al., 2009). The state space model adopted a totally agricultural shifts and urban expansion, and 2) tuning the algorithm for
different strategy to resolve unexplained variance from annual and semi- the optimal parameters, such as probability threshold and min_peek_days,
annual curves: the state space model assumes that the trend and sea- for better detection of targeted change agents and timely warning of
sonality states are evolving as time goes by (see Fig. 2B), instead of land disturbance.
14

S. Ye et al.                                                                                                                                                                                            R  e  m  o  t e  S  e  n s  i n g   o  f  E  n v  i r o  n  m  e  n t252(2021)112167
| 7. Conclusion  |     |     |     |     |     |     |     | Acknowledgement  |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
We  presented  an  improved  time  series  framework,  Stochastic  We gratefully acknowledge the support of American Society of
Continuous Change Detection (S-CCD), for near real-time forest distur- Photogrammetry  and  Remote  Sensing  (ASPRS)  William  A.  Fisher
Scholarship and Albert, and Norma and Howard Geller’77 Endowed
bance monitoring. The new approach introduces the state space model
into the current framework for Continuous Monitoring of Land Distur- Research Awards to Su Ye. This research was partially supported by the
bance (COLD), to facilitate a near real-time analytics of forest dynamics  USGS-NASA Landsat Science Team Program for Toward Near Real-time
with a shorter lag time and improve computational efficiency. S-CCD  Monitoring and Characterization of Landsat Surface Change for the
provides an accurate mapping for timing and change magnitude of forest  Conterminous US (140G0119C0008) to Zhe Zhu. The content of this
disturbance, and uncovers complex nonlinear dynamics from time series  document does not necessarily represent the views or policies of the
data. Most notably, S-CCD can improve the monitoring for those dis- Department of the Interior, nor does mention of trade names, commer-
turbances that induce subtle spectral changes.  cial  products  or  organizations  imply  endorsement  by  the  U.S.
Government.
Declaration of Competing Interest
None.
Appendix
The system matrices for ‘trend+annual+semi-annual’ time series structural model are defined by
Z=(1,1,0,1,0)
(A1)
|        | (           |           |         | )       |          |     |          |     |        |
| ------ | ----------- | --------- | ------- | ------- | -------- | --- | -------- | --- | ------ |
|        | σ2 ,σ2      | ,σ2       | ,σ2 ,σ2 |         |          |     |          |     |        |
| Q=diag | ω,annual    |           | ω,semi  |         |          |     |          |     | (A2)   |
|        | ξ           | ω*,annual |         | ω*,semi |          |     |          |     |        |
| ⎡      |             |           |         |         |          |     |          | ⎤   |        |
| 1      | 0           |           | 0       |         | 0        |     | 0        |     |        |
|        | (           | )         | (       | )       |          |     |          |     |        |
| ⎢ ⎢    |             |           |         |         |          |     |          | ⎥ ⎥ |        |
| ⎢      |             | 2π        | 2π      |         |          |     |          | ⎥   |        |
| ⎢ 0    | cos         |           | sin     |         | 0        |     | 0        | ⎥   |        |
| ⎢      | 365.25      |           | 365.25  |         |          |     |          | ⎥   |        |
| ⎢      | (           | )         | (       | )       |          |     |          | ⎥   |        |
| ⎢      |             |           |         |         |          |     |          | ⎥   |        |
| ⎢      |             | 2π        | 2π      |         |          |     |          | ⎥   |        |
| ⎢0     | (cid:0) sin |           | cos     |         | 0        |     | 0        | ⎥   |        |
| T=⎢    | 365.25      |           | 365.25  |         |          |     |          | ⎥   | (A3)   |
| ⎢      |             |           |         |         | (        | )   | (        | ) ⎥ |        |
| ⎢      |             |           |         |         | 2π       |     | 2π       | ⎥   |        |
| ⎢      |             |           |         |         |          |     |          | ⎥   |        |
| ⎢0     | 0           |           | 0       | cos     |          | sin |          | ⎥   |        |
| ⎢      |             |           |         |         | 2*365.25 |     | 2*365.25 | ⎥   |        |
| ⎢      |             |           |         |         | (        | )   | (        | ) ⎥ |        |
| ⎢      |             |           |         |         | 2π       |     | 2π       | ⎥   |        |
| ⎣      |             |           |         | (cid:0) |          |     |          | ⎦   |        |
| 0      | 0           |           | 0       | sin     |          | cos |          |     |        |
|        |             |           |         |         | 2*365.25 |     | 2*365.25 |     |        |
The Kalman filter recursion for the general Gaussian model of form are
| v =y (cid:0) | Za   |     |     |     |     |     |     |     | (A4)   |
| ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | ------ |
| t,i t,i      | t,i  |     |     |     |     |     |     |     |        |
| F =ZP        | ZT+H |     |     |     |     |     |     |     | (A5)   |
| t,i          | t,i  | i   |     |     |     |     |     |     |        |
| K t,i =P t,i | ZT   |     |     |     |     |     |     |     | (A6)   |
(cid:0)
| a t|t,i =a t,i | +K t,i F | 1v t,i |     |     |     |     |     |     | (A7)   |
| -------------- | -------- | ------ | --- | --- | --- | --- | --- | --- | ------ |
t ,i
| a t+1,i =Ta | t|t,i       |                 |      |     |     |     |     |     | (A8)   |
| ----------- | ----------- | --------------- | ---- | --- | --- | --- | --- | --- | ------ |
|             | (           |                 | )    |     |     |     |     |     |        |
| P =T        | P (cid:0) K | K T F (cid:0) 1 | TT+Q |     |     |     |     |     | (A9)   |
| t+1,i       | t,i         | t,i t ,i t ,i   | i    |     |     |     |     |     |        |
Where.
yt, i: the observation at time t for band i.
vt, i: the innovation, namely the difference between predicted and actual observations, at time t for band i
Z: the system matrix that determines which items in the state vector are included for the observation
Kt, i: the Kalman gain which is the relative ratio of being assigned to the model update is from the innovation at time t for band i
Pt, i: the covariance matrix at time t for band i
at∣t, i: the filtered states at time t for band i
Ft, i: the variance of the innovation vt, i
Qi: the process noise for band i
Hi: the observational noise for band i
For missing observation, there is no innovation vt, i. Therefore, the mathematical treatment for state and covariance matrix updates can be simply
put as
| a t+1,i =Ta | t|t,i |     |     |     |     |     |     |     | (A10)   |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | ------- |
TT+Q
| P t+1,i =TP | t,i | i   |     |     |     |     |     |     | (A11)  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
15

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi.org/10.1016/j.rse.2020.112167.
References Kennedy, R.E., Andr´efou¨et, S., Cohen, W.B., Go´mez, C., Griffiths, P., Hais, M., Healey, S.
P., Helmer, E.H., Hostert, P., Lyons, M.B., Others, 2014. Bringing an ecological view
of change to Landsat-based remote sensing. Front. Ecol. Environ. 12, 339–346.
Allen, C.D., Breshears, D.D., McDowell, N.G., 2015. On underestimation of global
Masek, J.G., Huang, C., Wolfe, R., Cohen, W., Hall, F., Kutler, J., Nelson, P., 2008. North
vulnerability to tree mortality and forest die-off from hotter drought in the
American forest disturbance mapped from a decadal Landsat record. Remote Sens.
Anthropocene. Ecosphere 6, 1–55. Environ. 112, 2914–2926.
Brockwell, P.J., Davis, R.A., 2013. Introduction to Time Series and Forecasting (Springer
Science & Business Media). Masek, J.G., Goward, S.N., Kennedy, R.E., Cohen, W.B., Moisen, G.G., Schleeweis, K.,
Huang, C., 2013. United States Forest disturbance trends observed using Landsat
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E., time series. Ecosystems 16, 1087–1104.
Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K., Olsson, P.-O., Lindstro¨m, J., Eklundh, L., 2016. Near real-time monitoring of insect
Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D.,
induced defoliation in subalpine birch forests with MODIS derived NDVI. Remote
Reker, R.R., Rover, J., 2019. Lessons learned implementing an operational Sens. Environ. 181, 42–53.
continuous United States national land change monitoring capability: the land
Paritsis, J., Veblen, T.T., 2011. Dendroecological analysis of defoliator outbreaks on
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens.
Nothofagus pumilio and their relation to climate variability in the Patagonian Andes.
Environ. 111356. Glob. Chang. Biol. 17, 239–253.
Bullock, E.L., Woodcock, C.E., Holden, C.E., 2019. Improved change monitoring using an
Pasquarella, V., Bradley, B., Woodcock, C., 2017. Near-real-time monitoring of insect
ensemble of time series algorithms. Remote Sens. Environ. 111165.
defoliation using Landsat time series. Forests 8, 275.
Burkett, V.R., Wilcox, D.A., Stottlemyer, R., Barrow, W., Fagre, D., Baron, J., Price, J.,
Pasquarella, V., Elkinton, J.S., Bradley, B.A., 2018. Extensive gypsy moth defoliation in
Nielsen, J.L., Allen, C.D., Peterson, D.L., Ruggerone, G., Doyle, T., 2005. Nonlinear
southern New England characterized using Landsat satellite observations. Biol.
dynamics in ecosystem response to climatic change: case studies and policy Invasions 20, 3047–3053.
implications. Ecol. Complex. 2, 357–394.
Carlson, A.R., Sibold, J.S., Assal, T.J., Negro´n, J.F., 2017. Evidence of compounded Pasricha, G.K., 2006. Kalman Filter and its Economic Applications.
Pechony, O., Shindell, D.T., 2010. Driving forces of global wildfires over the past
disturbance effects on vegetation recovery following high-severity wildfire and
millennium and the forthcoming century. In: Proceedings of the National Academy
spruce beetle outbreak. PLoS One 12, e0181778. of Sciences, 107, pp. 19167–19170.
Cohen, W.B., Yang, Z., Stehman, S.V., Schroeder, T.A., Bell, D.M., Masek, J.G., Huang, C.,
Preisler, H.K., Hicke, J.A., Ager, A.A., Hayes, J.L., 2012. Climate and weather influences
Meigs, G.W., 2016. Forest disturbance across the conterminous United States from
on spatial temporal patterns of mountain pine beetle populations in Washington and
1985–2012: the emerging dominance of forest decline. For. Ecol. Manag. 360, Oregon. Ecology 93, 2421–2434.
242–252.
Reymondin, L., Jarvis, A., Perez-Uribe, A., Touval, J., Argote, K., Rebetez, J., Guevara, E.,
Cohen, W.B., Healey, S.P., Yang, Z., Stehman, S.V., Brewer, C.K., Brooks, E.B.,
Mulligan, M., 2012. A Methodology for near Real-Time Monitoring of Habitat
Gorelick, N., Huang, C., Hughes, M.J., Kennedy, R.E., 2017. How similar are forest
Change at Continental Scales Using MODIS-NDVI and TRMM (Submitted Remote
disturbance maps derived from different Landsat time series algorithms? Forests 8,
Sensing of Environment).
98.
Rogan, J., Mietkiewicz, N., 2015. Land cover change detection. In: Thenkabail, P.S. (Ed.),
Coleman, T.W., Graves, A.D., Heath, Z., Flowers, R.W., Hanavan, R.P., Cluck, D.R.,
Land Resources Monitoring, Modeling, and Mapping with Remote Sensing,
Ryerson, D., 2018. Accuracy of aerial detection surveys for mapping insect and pp. 579–603.
disease disturbances in the United States. For. Ecol. Manag. 430, 321–336.
Schmidt, S.F., 1981. The Kalman filter - its recognition and development for aerospace
Curran, L.M., Trigg, S.N., 2006. Sustainability science from space: quantifying forest applications. J. Guid. Control. Dyn. 4, 4–7.
disturbance and land-use dynamics in the Amazon. In: Proceedings of the
Sedano, F., Kempeneers, P., Hurtt, G., 2014. A Kalman filter-based method to generate
National Academy of Sciences of the United States of America, 103,
continuous time series of medium-resolution NDVI images. Remote Sens. 6,
pp. 12663–12664. 12381–12408.
Cyphers, L., Mackes, K., Duda, K., 2019. Timber losses from west fork complex fire in
Seidl, R., Thom, D., Kautz, M., Martin-Benito, D., Peltoniemi, M., Vacchiano, G., Wild, J.,
Southwest Colorado. For. Prod. J. 69 (4), 272–277.
Ascoli, D., Petr, M., Honkaniemi, J., 2017. Forest disturbances under climate change.
Dale, V.H., Joyce, L.A., McNulty, S., Neilson, R.P., Ayres, M.P., Flannigan, M.D., Nat. Clim. Chang. 7, 395–402.
Hanson, P.J., Irland, L.C., Lugo, A.E., Peterson, C.J., 2001. Climate change and forest
Tang, X., Bullock, E.L., Olofsson, P., Estel, S., Woodcock, C.E., 2019. Near real-time
disturbances. BioScience 51, 723–734.
monitoring of tropical forest disturbance: new algorithms and assessment
Davis, M.H.A., Vinter, R.B., 1985. Stochastic models. Stoch. Model. Control 60–99. framework. Remote Sens. Environ. 224, 202–218.
Davis, B., Guo, S., Smith, K., 2017. Land Change Monitoring Assessment and Projection
Tang, X., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2020. Can VIIRS continue the
(LCMAP) Python Implementation of Continuous Change Detection (pyccd).
legacy of MODIS for near real-time monitoring of tropical forest disturbance?
Department of Interior U.S. Geological Survey.
Remote Sens. Environ. 249, 112024.
Durbin, J., Koopman, S.J., 2012. Time Series Analysis by State Space Methods: Second
Townsend, P.A., Eshleman, K.N., others, 2004. Remote sensing of gypsy moth defoliation
Edition (OUP Oxford).
to assess variations in stream nitrogen concentrations. Ecological Applications 14
Dwyer, J., Roy, D., Sauer, B., Jenkerson, C., Zhang, H., Lymburner, L., 2018. Analysis (2), 504–516.
ready data: enabling analysis of the Landsat archive. Remote Sens. 10.
Turner, M.G., Baker, W.L., Peterson, C.J., Peet, R.K., 1998. Factors influencing
Eastman, J.R., Sangermano, F., Ghimire, B., Zhu, H., Chen, H., Neeti, N., Cai, Y.,
succession: lessons from large, infrequent natural disturbances. Ecosystems 1,
Machado, E.A., Crema, S.C., 2009. Seasonal trend analysis of image time series. Int. 511–523.
J. Remote Sens. 30, 2721–2726.
Verbesselt, J., Hyndman, R., Newnham, G., Culvenor, D., 2010a. Detecting trend and
Eastman, J.R., Sangermano, F., Machado, E.A., Rogan, J., Anyamba, A., 2013. Global seasonal changes in satellite image time series. Remote Sens. Environ. 114, 106–115.
trends in seasonality of normalized difference vegetation index (NDVI), 1982–2011.
Verbesselt, J., Hyndman, R., Zeileis, A., Culvenor, D., 2010b. Phenological change
Remote Sens. 5, 4799–4818.
detection while accounting for abrupt and gradual trends in satellite image time
Hammer, D., Kraft, R., Wheeler, D., 2014. Alerts of forest disturbance from MODIS series. Remote Sens. Environ. 114, 2970–2980.
imagery. Int. J. Appl. Earth Obs. Geoinf. 33, 1–9.
Verbesselt, J., Zeileis, A., Herold, M., 2012. Near real-time disturbance detection using
Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S., satellite image time series. Remote Sens. Environ. 123, 98–108.
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
Verdin, K.L., Dupree, J.A., Stevens, M.R., 2013. Postwildfire Debris-Flow Hazard
using Landsat data. Environ. Res. Lett. 11, 034008.
Assessment of the Area Burned by the 2013 West Fork Fire Complex, Southwestern
Hart, S.J., Veblen, T.T., 2015. Detection of spruce beetle-induced tree mortality using
Colorado. US Department of the Interior, US Geological Survey.
high-and medium-resolution remotely sensed imagery. Remote Sens. Environ. 168,
Vicente-Guijalba, F., Martinez-Marin, T., Lopez-Sanchez, J.M., 2014. Crop phenology
134–145.
estimation using a multitemporal model and a Kalman filtering strategy. IEEE
J H a e m ls a k l e i , , J S . . , , 2 Jo¨ 0 n 1 s 6 s . o K n F , A P S ., : E E k x l p u o n n d e h n , t L ia ., l A Fa rd m o¨ i , l y J . S , t S a e t a e q S u p i a st c , e J M ., o 2 d 0 e 1 l 5 s . in D e R te . c a t r i X n i g v c [ h st a a n t. g C e O s ] i . n Geosci. Remote Sens. Lett. 11, 1081–1085.
Vogelmann, J.E., Gallant, A.L., Shi, H., Zhu, Z., 2016. Perspectives on monitoring gradual
vegetation trends using time series segmentation. Remote Sens. Environ. 156,
change across the continuity of Landsat sensors using time-series data. Remote Sens.
182–195.
Environ. 185, 258–270.
Kalman, R.E., 1960. A new approach to linear filtering and prediction problems. Int. J.
Walters, S.P., Schneider, N.J., Guthrie, J.D., 2011. Geospatial Multi-Agency Coordination
Eng. Trans. A 82, 35–45.
(GeoMAC) Wildland Fire Perimeters, 2008 (Data Series).
Kautz, M., Meddens, A.J., Hall, R.J., Arneth, A., 2017. Biotic disturbances in northern
Westerling, A.L., 2016. Increasing western US forest wildfire activity: sensitivity to
hemisphere forests–a synthesis of recent data, uncertainties and implications for
changes in the timing of spring. Philos. Trans. R. Soc. B 371, 20150178.
forest monitoring and modelling. Glob. Ecol. Biogeogr. 26, 533–552.
Woodcock, C.E., Allen, R., Anderson, M., Belward, A., Bindschadler, R., Cohen, W.,
Kennedy, R.E., Yang, Z., Cohen, W.B., 2010. Detecting trends in forest disturbance and
Gao, F., Goward, S.N., Helder, D., Helmer, E., 2008. Free access to Landsat imagery.
recovery using yearly Landsat time series: 1. LandTrendr—Temporal segmentation Science 320 (1011–1011).
algorithms. Remote Sens. Environ. 114, 2897–2910.
16

S. Ye et al. R e m o t e S e n s i n g o f E n v i r o n m e n t252(2021)112167
Ye, S., Rogan, J., Sangermano, F., 2018. Monitoring rubber plantation expansion using Zhu, Z., Woodcock, C.E., 2014a. Automated cloud, cloud shadow, and snow detection in
Landsat data time series and a Shapelet-based approach. ISPRS J. Photogramm. multitemporal Landsat data: an algorithm designed specifically for monitoring land
Remote Sens. 136, 134–143. cover change. Remote Sens. Environ. 152, 217–234.
Zhao, K., Wulder, M.A., Hu, T., Bright, R., Wu, Q., Qin, H., Li, Y., Toman, E., Mallick, B., Zhu, Z., Woodcock, C.E., 2014b. Continuous change detection and classification of land
Zhang, X., Brown, M., 2019. Detecting change-point, trend, and seasonality in cover using all available Landsat data. Remote Sens. Environ. 144, 152–171.
satellite time series data to track abrupt changes and nonlinear dynamics: a Bayesian Zhu, Z., Woodcock, C.E., Olofsson, P., 2012. Continuous monitoring of forest disturbance
ensemble algorithm. Remote Sens. Environ. 232, 111181. using all available Landsat imagery. Remote Sens. Environ. 122, 75–91.
Zhu, Z., 2017. Change detection using landsat time series: a review of frequencies, Zhu, Z., Woodcock, C.E., Holden, C., Yang, Z., 2015. Generating synthetic Landsat
preprocessing, algorithms, and applications. ISPRS J. Photogramm. Remote Sens. images based on all available Landsat data: predicting Landsat surface reflectance at
130, 370–384. any given time. Remote Sens. Environ. 162, 67–83.
Zhu, Z., 2019. Science of Landsat analysis ready data. Remote Sens. 11, 2166. Zhu, Z., Zhang, J., Yang, Z., Aljaddani, A.H., Cohen, W.B., Qiu, S., Zhou, C., 2020.
Zhu, Z., Woodcock, C.E., 2012. Object-based cloud and cloud shadow detection in Continuous monitoring of land disturbance based on Landsat time series. Remote
Landsat imagery. Remote Sens. Environ. 118, 83–94. Sens. Environ. 238, 111116.
17