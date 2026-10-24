International Journal of Digital Earth
ISSN: 1753-8947 (Print) 1753-8955 (Online) Journal homepage: www.tandfonline.com/journals/tjde20
Manifold embeddings achieve comparable
performance with multispectral imagery for time-
series based land disturbance detection
Mengyao Li, Jianbo Qi, Su Ye & Qiao Wang
To cite this article: Mengyao Li, Jianbo Qi, Su Ye & Qiao Wang (2025) Manifold embeddings
achieve comparable performance with multispectral imagery for time-series based
land disturbance detection, International Journal of Digital Earth, 18:1, 2523481, DOI:
10.1080/17538947.2025.2523481
To link to this article: https://doi.org/10.1080/17538947.2025.2523481
© 2025 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 01 Jul 2025.
Submit your article to this journal
Article views: 1152
View related articles
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tjde20

INTERNATIONAL JOURNAL OF DIGITAL EARTH
2025, VOL. 18, NO. 1, 2523481
https://doi.org/10.1080/17538947.2025.2523481
Manifold embeddings achieve comparable performance with
multispectral imagery for time-series based land disturbance
detection
Mengyao Lia, Jianbo Qia, Su Yeb and Qiao Wanga
aAdvanced Interdisciplinary Institute of Satellite Applications, Beijing Normal University, Beijing, People’s
Republic of China; bCollege of Environmental and Resource Sciences, Zhejiang University, Hangzhou,
People’s Republic of China
ABSTRACT ARTICLE HISTORY
Dense long-term time series multispectral imagery is crucial for Received 26 January 2025
monitoring Earth’s surface and detecting disturbances in near-real- Accepted 15 June 2025
time. However, the massive storage requirements of such data pose
significant challenges. Dimensionality reduction techniques have KEYWORDS
Land disturbances detection;
been widely applied in remote sensing to address the curse of
time-series; dimension
dimensionality, yet achieving lossless recovery of multispectral data
reduction; anomaly
across global locations and varying surface conditions remains detection; manifold learning
difficult. Additionally, it is unclear whether reduced features retain
temporal continuity and can integrate effectively with time series
algorithms for disturbance detection. This study leverages Uniform
Manifold Approximation and Projection (UMAP) for multispectral
dimensionality reduction, trained on Harmonized Landsat Sentinel-2
(HLS) imagery. The resulting manifold embeddings are applied to
the Continuous Change Detection and Classification (CCDC)
algorithm for land disturbance detection. Two key findings emerge:
(1) We developed a general UMAP-based dimensionality reduction
model that works across global seasons, with manifold embeddings
preserving time series coherence and exhibiting stable value ranges.
(2) The embeddings achieved comparable performance to full-
spectrum multispectral data in image prediction and disturbance
detection with CCDC. This research highlights the potential of
manifold learning to efficiently store and process dense satellite
imagery while maintaining the ability to detect diverse land
disturbances.
1. Introduction
1.1. Background
In recent years, terrestrial remote sensing observation has undergoing a paradigm shift
from change detection to remote sensing monitoring (Woodcock et al. 2020). The
CONTACT Jianbo Qi jianboqi@bnu.edu.cn Faculty of Geographical Science, Innovation Research Center of
Satellite Application (IRCSA), State Key Laboratory of Remote Sensing Science, Beijing Normal University, Beijing 100875,
People’s Republic of China
© 2025 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/
licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly
cited. The terms on which this article has been published allow the posting of the Accepted Manuscript in a repository by the
author(s) or with their consent.

2 M. LI ET AL.
availability of dense time series remote sensing data has significantly advanced the devel-
opment of earth observation technologies (Suh, Zhu, and Zhao 2024). A series of
methods based on dense time series data has become a crucial means for monitoring
surface disturbances. These methods have been widely applied in monitoring wildfires
(Fotakidis et al. 2023), floods (Damle and Yalcin 2007), pest outbreaks (Ye et al.
2021), deforestation (Bullock, Woodcock, and Olofsson 2020), agricultural expansion
(Zabel et al. 2019), and construction changes (Suh, Zhu, and Zhao 2024). Compared
to change detection algorithms based on two temporal phases, methods utilizing dense
time series data offer the advantage of continuous Earth monitoring, enabling more
timely and effective detection.
However, dense time series data requires substantial data storage and incurs high
computational costs. For instance, processing a Landsat ARD image using the COLD
algorithm requires 1000–3000 h, and storing the time series imagery requires 0.5–2 tera-
bytes (Zhu et al. 2020). Such demands present a substantial barrier to achieving continu-
ous surveillance and prompt detection of extensive surface disturbances. Looking ahead,
an increasing number of satellites with higher spectral resolutions and an expanded range
of spectral bands are slated for launch. For instance, the Landsat Next mission, planned
for launch in late 2030/early 2031, will boast an impressive 26 spectral bands (Wulder
et al. 2022). The proliferation of data intensifies the challenges associated with the
all-bands approach to land disturbance detection. Therefore, it is imperative to simplify
vast amounts of time series multispectral data while minimizing data loss to accommo-
date various types of complex surfaces.
Currently, most studies focus on the continuous monitoring of specific types of sur-
faces, which can be achieved by selecting sensitive bands or constructing specific indices
(Bullock, Woodcock, and Olofsson 2020; Deng and Zhu 2020; Ye et al. 2021). However,
the Earth’s surface is highly complex, with significant variations in the sensitive wave-
length ranges of different land cover types. Thus, employing full-spectrum multispectral
data for disturbance detection is crucial. Developing a multispectral dimensionality
reduction model suitable for a variety of complex global surfaces, capable of achieving
lossless compression and recovery of any spectrum, is key to addressing this issue.
Can current dimensionality reduction techniques attain this objective? Do the reduced
features maintain continuity within the time series? Are they applicable for disturbance
detection in complex substrates? What is the efficacy of such detection? These questions
remain unanswered.
1.2. Related work
Dimensionality reduction methods. These methods yield a reduced set of features that
encapsulate the full spectral information, thereby offering a more efficient alternative
to analyzing each individual spectral band. Numerous advanced dimensionality
reduction techniques are now available, including linear methods like Principal
Component Analysis (PCA) (Maćkiewicz and Ratajczak 1993), Linear Discriminant
Analysis (LDA) (Xanthopoulos, Pardalos, and Trafalis 2013), Independent Component
Analysis (ICA) (Comon 1994), and nonlinear methods like Locally Linear Embedding
(LLE) (Roweis and Saul 2000), t-distributed Stochastic Neighbor Embedding (t-SNE)
(Maaten 2008), Auto-Encoder (Rumelhart, Hinton, and Williams 1988), UMAP

INTERNATIONAL JOURNAL OF DIGITAL EARTH 3
(McInnes, Healy, and Melville 2018), though their comparative performance for being
applied to time series analysis is still unknown. These techniques can condense extensive
spectral information into a more manageable space while effectively preserving the orig-
inal data, especially the nonlinear methods. Utilizing these compressed features in time
series model construction obviates the need to select specific bands or indices for
different land cover types and significantly reduces data storage requirements and com-
putational costs. UMAP, a high-dimensional clustering technique based on manifold
learning developed in recent years, stands out among dimensionality reduction algor-
ithms due to its lossless compression capabilities and rapid computation speed
(Allaoui, Kherfi, and Cheriet 2020). It has been widely applied across various fields,
achieving exceptional results (Ali et al. 2019; Becht et al. 2019; Dorrity et al. 2020; Yu
et al. 2023). In the realm of remote sensing, UMAP has been utilized for characterizing
spectral blending spaces, adept at capturing nuanced spectral differentiations among land
cover categories (Small and Sousa 2022; Sousa and Small 2022). As a nonlinear dimen-
sionality reduction technique, UMAP offers significant advantages over PCA and t-SNE
for compressing multispectral data in time-series analysis. PCA, constrained by its linear
projection, can only capture global variance directions and thus often misses complex,
nonlinear spectral relationships. t-SNE, while highly effective at preserving local neigh-
borhood structure, incurs substantial computational cost and breaks global topology,
hindering its use on large datasets. In contrast, UMAP efficiently preserves both local
neighborhoods and the overall manifold topology in a single low-dimensional embed-
ding, while achieving significantly faster runtimes than t-SNE (Becht et al. 2019). More-
over, unlike PCA and t-SNE – which require scene-specific transformations (PCA via
per-scene eigenvectors; t-SNE via affinity graphs with no built-in out-of-sample
method) – UMAP learns a single mapping that generalizes directly to any new multispec-
tral image without recalculating parameters or storing per-image coefficients. This
unified, reusable model, together with UMAP’s high computational efficiency, makes it
ideally suited for large-scale, long-term remote sensing workflows that demand stable,
scalable, and repeatable spectral compression and reconstruction. This unified, reusable
model, together with UMAP’s high computational efficiency, makes it ideally suited for
large-scale, long-term remote sensing workflows that demand stable, scalable, and repea-
table spectral compression and reconstruction. Moreover, it ensures the comparability of
features across different images, which is crucial for preserving temporal patterns.
Although Autoencoders offer powerful nonlinear dimensionality reduction capabilities,
their optimization is primarily driven by reconstruction accuracy, which often leads to
representations that emphasize overall data fidelity rather than discriminative features
relevant to spectral variation. Moreover, the latent features extracted by Autoencoders
frequently lack physical interpretability. In contrast, UMAP is designed to preserve the
nonlinear structural relationships among spectral bands, enabling the compression of
high-dimensional multispectral data into a few compact and representative components.
This not only reduces dimensionality but also retains key information more relevant to
change dynamics. Therefore, this study adopts UMAP for the compression and recon-
struction of multispectral data, which is subsequently integrated with time-series analysis
for effective disturbance detection.
Time series methods for land disturbance detection. The central objective of land dis-
turbance monitoring via satellite time series analysis is to develop models that capture the

4 M. LI ET AL.
natural variability and trend of the Earth’s surface. In the past decades, many time
series-based methods to detect land disturbances has been developed, with representa-
tives including Breaks For Additive Seasonal and Trend (BFAST) (Verbesselt et al.
2010), LandTrendr (Kennedy, Yang, and Cohen 2010), long short-term memory
(LSTM) (Graves and Alex 2012), CCDC (Zhu and Woodcock 2014b), Continuous
Monitoring of Land Disturbance (COLD) (Zhu et al. 2020), Stochastic Continuous
Change Detection (S-CCD) (Ye, Rogan, Zhu, and Eastman 2021), Object-based Con-
tinuous Monitoring of Land Disturbance (OB-COLD) (Ye, Zhu, and Cao 2023) and
other deep learning-based methods (Mao et al. 2024; Haixu He et al. 2024). BFAST
and LandTrendr are capable of identifying disturbances in historical data, but they
lack predictive capabilities and cannot perform timely online disturbance detection.
LSTM captures long-term dependencies and complex patterns for prediction and
real-time detection but faces high computational complexity, tuning challenges, and
reduced performance with very long sequences. CCDC utilizes harmonic models
derived from dense time series satellite data to depict natural surface fluctuations,
thereby adeptly monitoring long-term land cover changes. Its forecasting abilities
facilitate real-time updates and seamless online surveillance. The other algorithms
are improvements derived from CCDC, offering enhancements in accuracy, timeliness,
and object-oriented analysis.
1.3. Contribution
The central question this paper endeavors to explore is whether reduced features can
optimally preserve original information and temporal patterns. Additionally, it examines
whether these features have the potential to supplant multispectral data for time series
analysis and surface disturbance detection, thereby streamlining the monitoring
process. To address this issue, the paper undertakes the following tasks:
(1) A general multispectral dimensionality reduction model was trained based on
UMAP, demonstrating strong spectral recovery and generalization capabilities. Mul-
tispectral projections from any location, time, or type globally exhibit stable shapes
and structures within this low-dimensional manifold space. This ensures that
embeddings derived from any image projection are comparable, maintaining tem-
poral continuity in reduced features obtained from images at different times. The
time series embeddings retain temporal patterns, avoiding uncertainty in the value
ranges of reduced features across different images;
(2) The manifold embeddings were applied to a time series algorithm (specifically the
CCDC algorithm in this study) for predicting images across arbitrary seasons and
detecting four different types of surface disturbances. The results indicate that the
low-dimensional manifold embeddings hold significant potential to replace full-
spectrum multispectral data in dense time series analysis.
1.4. Outline
This paper is structured as follows: Section 2 outlines the methods employed in this
study; Section 3 presents the data used in the research, and the two-dimensional manifold

INTERNATIONAL JOURNAL OF DIGITAL EARTH 5
space representing global surface spectra, evaluating the predictive capacity of UMAP
embeddings in conjunction with the time series algorithm CCDC, and the disturbance
detection capabilities of the manifold embeddings both qualitatively and quantitatively;
Section 4 discusses the robustness and interpretability of the embedding space, demon-
strates two UMAP embeddings perform on par with higher-dimensional embeddings,
analyzes the contributions of each UMAP embedding within the time series, and articu-
lates the advantages and limitations of the proposed method; finally, Section 5 summar-
izes the findings of this study.
2. Methodology
The flowchart of this study is shown in Figure 1. Our method was divided into the follow-
ing three steps. Firstly, each time-series multispectral image is projected into the two-
dimensional manifold space using the UMAP model trained on globally representative
land surface spectra dataset, i.e. UMAP_TRAIN, constructing two new time series of the
transformed features (Section 2.1). Next, we apply the CCDC algorithm to build stable
curves for the time series of the two features, facilitating feature prediction at any given
time point (Section 2.2). The UMAP model reconstructs the multi-spectral image at the
current time based on the predicted two features. The reconstructed multi-spectral
image is considered to represent the current state of the land surface. Finally, comparisons
Figure 1. The workflow of the proposed method. Our method was divided into three steps. For step 1,
the UMAP model is trained using globally typical spectra, and the manifold spatial features of two time
series are projected from multispectral images. For step 2, the features at detection time are predicted
by CCDC, and the multispectral image is reconstructed through UMAP inverse projection. For step 3,
disturbances are detected by comparing simulated and real images.

6  M. LI ET AL.
are made between the input image to be detected and its reconstructed counterpart across
multiple spectral bands to monitor disturbances (Section 2.3).
2.1. UMAP for dimension reduction
UMAP is a nonlinear dimensionality reduction algorithm that incorporates advanced
mathematical theories including Riemannian geometry and topological algebra. It is
founded on three assumptions about the data: (1). the data is uniformly distributed on
Riemannian manifold; (2). the Riemannian metric is or can be approximated as locally
constant; (3). the manifold is locally connected. The implementation of UMAP mainly
involves the following three steps:
(1) A function is formulated to depict the relationship between two points in a high-
dimensional space, e.g. 6 bands form a 6-dimensional space, as shown in the follow-
ing equation:
d(x, x)− r
i j i
|     | −   |     |     | (1)  |
| --- | --- | --- | --- | ---- |
s
|     | p =e | i   |     |     |
| --- | ---- | --- | --- | --- |
j|i
􏽐
|     |     | pij |     | (2)  |
| --- | --- | --- | --- | ---- |
k=2 i
|     | p =p +p | − p ·p      |     | (3)  |
| --- | ------- | ----------- | --- | ---- |
|     | ij i|j  | j|i i|j j|i |     |      |
where p represents the joint probability of points i and j being neighbors in the high-
ij
dimensional space. x and x represent two points in the high-dimensional space that
| i   | j   |     |     |     |
| --- | --- | --- | --- | --- |
may be neighbors. p j|i  represents the probability of sample point j occurring given
sample point i. d(x, x) represents the distance between sample points i and j. r is
| i j |     |     |     | i   |
| --- | --- | --- | --- | --- |
the distance from point i to its nearest neighbors. s is determined by k, where k
i
indicates how many points in high-dimensional space point i can be neighbors
with. By adjusting k, the optimal s can be determined. d(x, x) can be set to any
|     | i   | i   | j   |     |
| --- | --- | --- | --- | --- |
distance function.
(2) A  function  is  formulated  to  depict  the  relationship  between  two  points  in  a
low-dimensional space, as shown in the following equation:
􏼨
2
|           | − 1       | 1, y − y ≤min      | dist      |      |
| --------- | --------- | ------------------ | --------- | ---- |
| q =(1+a(y | − y)2b) ≈ | i j                |           | (4)  |
| ij        | i j       | − − 2−             |           |      |
|           |           | e yi y j min dist, | otherwise |      |
where q ij  represents the joint probability of points i andj being neighbors in low-
dimensional space. y and y represent two points in low-dimensional space that may
| i   | j   |     |     |     |
| --- | --- | --- | --- | --- |
be neighbors. Parameters a and b can be adjusted to determine the clustering of data
in low-dimensional space. However, in practical applications, min dist is the hyperpara-
meter that users adjust to determine the clustering of data.
(3) Stochastic gradient descent is employed for parameter optimization to make p and
ij
q as close as possible. The loss function is utilized, defined as follows:
ij

INTERNATIONAL JOURNAL OF DIGITAL EARTH 7
􏼔 􏼒 􏼓 􏼒 􏼓􏼕
􏽐􏽐 p (X) 1− p (X)
C(X,Y)= p ij (X)log q ij (Y) +(1− p ij (X))log 1− q ij (Y) (5)
i j ij ij
where C(X,Y) represents the value of the cross-entropy loss function. X and Y represent
the distances between two points in high-dimensional and low-dimensional space,
respectively. p (X) and q (Y) represent the probabilities of two points becoming neigh-
ij ij
bors in high-dimensional and low-dimensional space, respectively.
In this study, we utilized UMAP to achieve a streamlined spectral representation,
effectively minimizing data storage requirements and computational costs. A UMAP
model was trained using the UMAP_TRAIN dataset, which contains ten thousand ran-
domly selected typical spectra derived from HLS images of 227 scenes. Subsequently, we
projected all the time series of multispectral images through the trained model into two
UMAP features. These two features’ time series, replacing the multispectral time series,
are used for CCDC forecasting.
2.2. CCDC for time series prediction
The CCDC algorithm (Zhu and Woodcock 2014b) is used for time series forecasting.
Firstly, the time series of surface reflectance (SR) images are processed into continuous
and clear observations by filtering out clouds and shadows using the Function of mask
(FMASK) (Zhu, Wang, and Woodcock 2015) and MultiTemporal mask (TMASK)
(Zhu and Woodcock 2014a) algorithms. It is worth noting that FMASK employed the
QA band, while TMASK’s input of the green and SWIR2 bands was substituted with
two UMAP features in this paper. Next, the full CCDC model (Zhu et al. 2015) is
used to fit the time series observations and predict the reflectance or features at any
given moment. The function is as follows:
􏼒 􏼓 􏼒 􏼓 􏼒 􏼓
2p 2p 4p
ˆp(i,x) =a +a cos x +b sin x +a cos x
0,i 1,i 1,i 2,i
T T T
􏼒 􏼓 􏼒 􏼓 􏼒 􏼓
4p 6p 6p (6)
+b sin x +a cos x +b sin x +c x
2,i 3,i 3,i 1,i
T T T
{τ∗ ,x≤τ∗}
k− 1 k
where x is Julian date. i is the ith HLS band ((i=1, 2, 3, 4, 5, and 6)) or features. T is
number of days per year (T = 365.25). a coefficient for overall value for the ith HLS
0,i
band or UMAP features. a and b are coefficients for intra-annual change. a and
1,i 1,i 2,i
b are coefficients for intra-annual bimodal change. a and b are coefficients for
2,i 3,i 3,i
intra-annual trimodal change. c is coefficient for inter-annual change (slope). τ∗ is
1,i k
the kth break points. ˆp(i,x) represents predicted value for the ith Landsat Band or
UAMP features at x Julian date. The model can effectively capture both the multimode
intra-annual cycles (harmonic coefficients) and the inter-annual trend (a constant and
slope term). Least absolute shrinkage and selection operator (LASSO) is used to fit the
function. The full model requires at least 24 observations to be initialized, and the
total time span must exceed one year.
For the thresholds to detect disturbances, the CCDC algorithm considers that the sum
of the squares of the normalized changes deviates follows a chi-square distribution with

8 M. LI ET AL.
degrees of freedom equal to the number of bands used for detection. The threshold for
determining disturbances is defined by the following formula (Zhu et al. 2020):
􏼒 􏼓
􏽐n r − r􏽢 2
i i ≏x2(n).x2 (7)
RMSE 0.99
i=1 i
where i represents the input band, while n represents the total number of bands. In this
study, n is 6. r and r􏽢is the observed value and predicted value for ith HLS band. RMSE
i i i
represents the root mean square error between the full model and the observed value for
the ith band. We adopted the default change magnitude threshold, i.e. x2 , for our
0.99
CCDC comparative experiments.
In this study, we employed CCDC for image forecasting to achieve our objective: uti-
lizing historical spectral data as a knowledge base to synthesize images at any given time
that conform to the natural dynamics of the Earth’s surface. Following the initial prepro-
cessing of the time-series images for each study area, we reduced the dimensionality of
the multi-band time series images by projecting them into two UMAP feature time
series images, thereby optimizing storage efficiency.
2.3. Land disturbance detection
To identify land disturbance events, we utilized the fitted CCDC model to forecast two
UMAP feature images at the desired time point. Given the constraint of a limited number
of UMAP features for statistical analysis, i.e. two features, formula (7) was not directly
employed to identify disturbances. Instead, we projected the two predicted UMAP fea-
tures back into the original 6-band space to reconstruct a synthetic image for the
specific time of interest. This synthetic image represents the expected land dynamics
at that time, assuming no disturbances had occurred. Subsequently, we identified dis-
turbances by comparing the observed 6-band image with the synthetic one. A disturb-
ance event is detected when the difference between the observed and synthetic images
exceeds a threshold defined by the following equation:
⎧
⎪ ⎪ ⎪ ⎨0, 1
􏽘n
|b
i
− 􏽢 b
i
|,t
n
P = i (8)
disturbance ⎪ ⎪ ⎪ ⎩1, 1 􏽘n |b − 􏽢 b|≥t
i i
n
i
where P signifies whether the pixel represents land disturbance. A value of 0
disturbance
means no land disturbance occurred at the pixel, while a value of 1 indicates land disturb-
ance. i represents the input band, while n represents the total number of bands. In this
study, n is 6. b represents the pixel values from the ith band of the actual imagery,
i
􏽢
while b represents the pixel values from the ith band of the synthetic imagery. t rep-
i
resents reflectance threshold for determining whether land disturbance has occurred
in this study. The default value for t is 0.04. The choice of such threshold has been
justified and detailed in supplementary material. It is important to note that clouds
will not be identified as disturbances; instead, they are filtered out using the Quality
Assessment (QA) band of the HLS data. Furthermore, in this study, we confirmed a dis-
turbance event based on a single observation, necessitating the setting of the ‘conse’

INTERNATIONAL JOURNAL OF DIGITAL EARTH 9
parameter to 1 within the CCDC code. The source code, including this parameter setting,
can be accessed at https://code.usgs.gov/lcmap/pyccd.
2.4. Accuracy assessment
In this study, we first evaluated the UMAP model by comparing the reconstructed reflec-
tance spectra with the observed ones, which assess the accuracy of UMAP projection and
back-projection processes, ensuring that the UAMP features keep the all-band infor-
mation. The metrics used for this evaluation are the coefficient of determination R2
and the root mean square error (RMSE).
􏽐
(y − 􏽢y) 2
R2 =1− 􏽐 i i (9)
(y − ̅y)2
i
􏽲����������������
􏽘
1
RMSE= (y − 􏽢y) 2 (10)
i i
n
where y are the observed values, 􏽢y are the predicted values, and ̅y is the mean of the
i i
observed values. n is the number of observations.
In this study, quantitatively assess the precision of the proposed method in disturb-
ance detection, we visually interpreted 1400 sample points across five study areas, cover-
ing a total area of approximately 20000 square kilometers. The principle for validating
pixel samples is as follows: in areas with extensive disturbances, we generate a higher
number of random validation samples to ensure the collection of an adequate quantity
of disturbance examples. Due to the broader reach of flood and wildfire-affected
regions, 400 samples were allocated to each, while the smaller areas impacted by land-
slides and construction received 100 samples each. Furthermore, within each region,
we applied stratified random sampling across both disturbed and undisturbed areas.
We vectorized the disturbed regions. The area of undisturbed regions is more extensive
than that of disturbed regions, so among the 1400 samples, 1070 correspond to undis-
turbed surfaces, while 330 pertain to disturbed areas. This paper calculates five
metrics: precision, recall, false alarm rate, F1-score, and accuracy. The formulas are as
follows:
TP
Precision= (11)
TP+FP
TP
Recall= (12)
TP+FN
FP
falsealarm= (13)
FP+TN
2·Precision·Recall
F1= (14)
Precision+Recall
TP+TN
A= (15)
TP+TN+FP+FN

10 M. LI ET AL.
where TP represents true positives, FP represents false positives, FN represents false
negatives, and TN represents true negatives.
3. Experimental results and analysis
3.1. Data and pre-processing
3.1.1. Dataset for embedding training
To establish a globally robust spectral manifold space, we compiled an image dataset that
encompassed a diverse range of land surface types, covering all inhabited continents
during all meteorological seasons. Since our study relies on dense time series analysis,
we therefore utilized the Harmonized Landsat and Sentinel-2 (HLS) image dataset,
which provides higher temporal resolution and satisfactory spatial resolution compared
with the with the use of either Sentinel-2 or Landsat imagery in isolation. We selected
locations and seed values identical to the study of Michael Schmitt et al. (2019), where
a curated SEN12MS dataset was built. Finally, we compiled a total of 227 HLS images:
55 for spring scenes, 58 for summer scenes, 75 for fall scenes, and 39 for winter
scenes. Each image spans an area of roughly 12000 square kilometers. The locations of
the images for the four seasons are depicted in Figure 2. Figure 3displays representative
image scenes and the corresponding sampling points selected within each scene.
Two sets of spectral data were extracted from these images, each containing ten
thousand spectra. Through experimentation, we determined that this quantity was
optimal for training our model (detailed in 3.2). The first set of spectral dataset, called
UMAP_TRAIN, was randomly sampled from cloud-free regions of high-quality
images, ensuring that the proportions of spectra for various land cover types match
their actual distribution on the Earth’s surface. This strategy is considered to better rep-
resent the land surface, and this dataset was used to train the UMAP model. The second
dataset, called UMAP_VAL, was extracted through manual interpretation of different
land cover types. In total, we interpreted 2052 spectra for developed areas, 2123
Figure 2. Locations of 227 HLS images for extracting land surface spectra in each season, 55 for spring
scenes, 58 for summer scenes, 75 for fall scenes, and 39 for winter scenes. Four selected sites for
anomaly monitoring of land disturbance events in this study.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 11
Figure 3. Examples of HLS images with points representing the locations where spectra were
extracted. Five types of spectra were extracted in total: developed land, bare land, farmland, veg-
etation, and water.
spectra for farmland, 1953 spectra for bare land, 3079 spectra for vegetation, and 1532
spectra for water. We followed these rules to extract spectra for each land surface: Devel-
oped areas primarily included impermeable surfaces like roads and building rooftops;
Bare land included exposed natural surfaces like rocks, sandy areas, and soil without veg-
etation; Farmland included both cultivated and uncultivated agricultural land; Veg-
etation includes all land surfaces with vegetation signals, excluding farmland; Water
bodies included both inland and near-shore waters. In this paper, the first dataset was
used to train the UMAP model, while the second dataset was used to evaluate perform-
ance of the UMAP model.
3.1.2. Dataset for disturbance detection
To validate the proposed disturbance detection method, we chose five influential disturb-
ance events across the world, including three natural disasters and one human-induced
land surface modification. These events include flooding (which occurred in early
November 2021 in parts of British Columbia, Canada, and Washington State, USA),
wildfires (which occurred in August 2021 in California, USA, and in January 2020 on
Kangaroo Island in South Australia), landslides (which occurred in July 2019 in
Guizhou Province, China), and construction (which took place in March 2022 in
Hebei Province, China). We used HLS images with dense time series for disturbance
detection and processed all historical image tiles from the past three years for each of

12 M. LI ET AL.
the five aforementioned study areas. The HLS dataset comprises two subsets: L30 and
S30, each with distinct band ranges. We selected the bands common to both sensors
for disturbance detection.
3.2. Embedding space of global multispectral data
Figure 4 shows the embedding effect of UMAP_VAL and UMAP_TRAIN onto the
model trained with UMAP_TRAIN. The parameter settings for model training are
provided in the supplementary material. The gray points in the figure correspond to
projections from the UMAP_TRAIN, while the colored points, distinguished by
various land cover types, reflect projections from the UMAP_VAL. The overlap
between projections from two entirely distinct multispectral datasets attests to the
ability of our trained UMAP model to represent a wide range of global spectral
types within this two-dimensional space. In this two-dimensional manifold space,
spectra from various global land cover types exhibit stable shapes and structures.
The distinct clustering of different land cover types demonstrates that the low-dimen-
sional manifold space preserves the characteristics of land surface in high-dimensional
space. The low-dimensional space still retains the ability to distinguish various land
cover types. However, various land cover types still exhibit mixing. Cropland and veg-
etation are significantly mixed due to their similar spectral characteristics. Cropland
and bare soil also show substantial mixing, primarily because fallow cropland shares
spectral features with soil. In our visual interpretation, fallow cropland is categorized
within cropland. Soil, bare rock, and unused land are collectively classified as bare soil.
Moreover, bare soil is significantly mixed with developed areas, as certain streets and
rooftops exhibit spectral characteristics similar to bare soil. In essence, the manifold
space we have constructed exhibits stable topological structures, allowing spectra
from various global types to be projected onto this space and undergo lossless recon-
struction. In other words, this model can effectively condense HLS multispectral data
into two dimensions, and this process is entirely reliable. Moreover, these two features
reveal the differences between land cover types and their transitions, providing
mechanistic insights. They are optimal indicators for detecting surface disturbances.
Figure 5 showcases the performance of spectral projections from various land cover
types onto a two-dimensional manifold space using models trained with different
quantities of spectra. Models trained with different quantities of spectra vary in
size. When the number of spectra used to train the model is fewer than 10000, the
morphology of spectra projected onto a two-dimensional space differs from that of
models trained with more than 10000 spectra. When trained with more than 10000
spectra, the model consistently projects spectra into a stable two-dimensional space,
maintaining a form that is simply mirrored horizontally. The model’s size increases
with the growing number of spectra used in training. Taking into account both the
stability and size of the model, we ultimately chose the model trained with 10000
spectra.
Figure 6 shows the reconstruction performance of the UMAP embedding trained in
this study on various types of spectra. The figure illustrates that irrespective of the spec-
trum type, our trained model can nearly flawlessly reconstruct the original multiband
spectra using only two UMAP embeddings.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 13
Figure 4. (a) The morphology of the UMAP_TRAIN and the UMAP_VAL for different land cover types in
two-dimensional manifold space. (b) – (f) respectively represent the morphology of vegetation, water,
farmland, bare land, and developed areas in two-dimensional manifold space.
3.3. Performance of UMAP embeddings in CCDC
Figure 7 illustrates the synthetic images predicted using two UMAP embeddings, com-
pared with the corresponding real images. The first case study showcases a region in
Guizhou, China, characterized by a subtropical monsoon climate, featuring distinct
seasons. There are discernible seasonal fluctuations in vegetation growth. The second
case study showcases a region in western Washington state, United States, characterized
by a temperate maritime climate. The area experiences stable temperatures and precipi-
tation year-round, with mostly cloudy and rainy weather and consistent vegetation cover.

14 M. LI ET AL.
Figure 5. The performance of spectral projections from various land cover types onto the two-dimen-
sional manifold space using models trained with different quantities of spectra. The models are
trained using 1000, 5000, 10000, 50000, 100000, and 1000000 spectra, respectively. The other par-
ameters are configured with ‘min_dist’ set to 0.8 and ‘n_neighbors’ set to 8. The two-dimensional
manifold space represented on the brown axes is projected by the model used in this study,
trained with 10000 spectra.
Figure 6. The reconstruction performance of the UMAP embedding trained in this study on various
types of spectra.
Our synthetic images achieve a striking resemblance to authentic imagery and CCDC
adeptly simulates areas where the seasonal variations in vegetation are less pronounced.
In essence, CCDC skillfully models the temporal patterns of UMAP features in time

INTERNATIONAL JOURNAL OF DIGITAL EARTH 15
Figure 7. The comparison between synthetic images generated by the method proposed in this
article and authentic images captured across four seasons. Example 1: Location in Guizhou, China
– False-color representation. Example 2: Location in Washington State, USA – True-color represen-
tation. The labels in the top-right corner of the images represent Julian dates, indicating the year
and the day of this year. Due to cloud interference, the authentic images displayed may represent
images captured a few days prior to or following the dates of the synthetic images.
series and achieves relatively accurate predictions. The predicted features can be faith-
fully restored to the original bands through the UMAP model, precisely forecasting
imagery regardless of the season or land cover type. Combining CCDC with UMAP
offers a significant advantage in time series forecasting: it operates on just two features
derived from the data, rather than across all spectral bands. This approach substantially
reduces both storage and computational demands, making it particularly beneficial for
applications involving extensive long-term time series imagery. The storage requirement
has been reduced from six bands to two. and the computation time has also been
significantly reduced. For a time series of 370 points, the average time to predict two
UMAP feature bands is 0.0195 s, while predicting all bands requires 0.0620 s. The time
needed to predict all six bands of an image is approximately 3.2 times that required to
predict just two bands.

16 M. LI ET AL.
Figure 8shows the fitting performance between the values predicted directly by CCDC
for each band and the values for each band reconstructed from UMAP embeddings pre-
dicted using CCDC. A total of 500000 pixels from the four study areas were used for
fitting. According to our validation results, UMAP exhibited commendable reconstruc-
tion accuracy for the two short-wave infrared bands, the green band, and the red band,
with slightly diminished performance for the near-infrared and blue bands. Overall, the
band values directly predicted by CCDC and those reconstructed from the UMAP feature
values predicted by CCDC exhibit a high degree of correlation and minimal error. The R2
values are all above 0.7, and the RMSE remains below 0.04.
3.4. Accuracy of disturbance detection
Using the method outlined in our paper, we detected disturbances in the five study areas
by analyzing time-series HLS images captured over the three years leading up to the
event. To ensure a balanced distribution of disturbed and undisturbed areas for reliable
random point sampling during validation, the size of each study area was determined
based on the spatial extent of the disturbance, ranging from approximately 60–12000
square kilometers. For example, landslides typically affect small regions, requiring
smaller validation areas, whereas wildfires and floods often cover large areas, necessitat-
ing broader spatial coverage. Each selected region comprised approximately 300 satellite
images to support time series analysis. Figure 9presents the pre – and post-disturbance
HLS images, the reconstructed post-disturbance images and the disturbance map
detected by the proposed method for the five cases. The synthetic images perform well
Figure 8. Comparison of reflectance values obtained from direct CCDC predictions and CCDC-pre-
dicted UMAP feature reconstructions. (a–f) Performance of two methods in reflectance synthesis of
blue, green, red, NIR, SWIR1 and SWIR2.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 17
Figure 9. Land disturbance mapping for five cases by the proposed method in this paper. The first
column presents clear image obtained before the disturbance, taken closest in time to the disturb-
ance’s occurrence. The second column shows clear image obtained after the disturbance, taken
closest in time to the disturbance’s occurrence. The third column presents synthetic images of the
same day as the second column, reconstructed using historical image features through the method-
ology proposed in this paper. The fourth column shows the mapping of land disturbance. The red
areas are the identified disturbances. The dashed boxes in the second and fourth columns indicate
the areas affected by the disturbance. The labels in the bottom left corner of the images in the
first three columns represent the Julian date, indicating the year and the day within that year.
whether displayed in true color or false color. In certain cloudy and rainy areas, like Case
3, clear images are difficult to obtain. Due to the considerable time gap between the clear-
est image obtained prior to the disturbance and the image at the time of detection, there’s
a substantial difference in vegetation coverage. Traditional change detection methods are

18  M. LI ET AL.
Table 1. The algorithm accuracy comparison for the two methods.
| Disturbance Detection with   | Disturbance Detection with   |      |
| ---------------------------- | ---------------------------- | ---- |
| Manifold Embeddings          | All Multispectral Bands      |      |
| Precision                    | 0.66                         | 0.54 |
| Recall                       | 0.56                         | 0.81 |
| False alarm                  | 0.09                         | 0.22 |
| F1-score                     | 0.61                         | 0.65 |
| Accuracy                     | 0.83                         | 0.77 |
inadequate for precise disturbance identification. Synthetic images, forecasted based on
historical trends, successfully predict the surface conditions during disturbance occur-
rence. While some instances of over-detection persist in the disturbance identification
results, they primarily involve small, fragmented patches.
Table 1. illustrates the accuracy of both methods. The precision and false alarm rate of
CCDC with manifold embeddings are superior to those with all bands; however, the
recall rate is lower when using manifold embeddings. This indicates that using manifold
embeddings compromises a certain degree of recall in order to mitigate the false alarm
rate. Overall,  the F1-score  and accuracy are similar,  indicating that both methods
perform comparably in disturbance detection. This indicates that using manifold embed-
dings maintains detection accuracy even with fewer spectral bands, significantly reducing
redundant data storage and unnecessary computation time. Neither all bands nor mani-
fold embeddings achieved high precision in disturbance detection, as we used only a
single observation, indicating near-real-time monitoring. This accuracy represents the
normal level for near-real-time detection using the CCDC algorithm. To improve pre-
cision, increasing the frequency of observations is recommended (Ye, Zhu, and Suh
2024). Figure 10 illustrates the performance of these two methods across two examples.
Figure 10. (a) and (e) depict authentic HLS images of two distinct disturbance scenes. (a) depicts a
false-color representation of a fire scene, while (b) shows a true-color representation of a flood
scene. (b) and (f) depict synthetic images of two distinct disturbance scenes by the proposed
method. (c) and (g) are disturbance maps generated using the proposed method in this article. (d)
and (h) are disturbance maps generated by the CCDC algorithm using only one time step to identify
disturbances in this article.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 19
From Figure 10, it is evident that for certain regions, employing the CCDC algorithm
with only a single observation for disturbance detection may inevitably lead to issues
of over-identification. Thus, multiple consecutive observations are considered necessary.
The manifold embeddings method shows slightly fewer instances of over-identification,
suggesting the potential to reduce the required number of observations for effective dis-
turbance detection in the future, enabling a more efficient implementation.
4. Discussion
4.1. Robustness and interpretability of embedding space
In this study, we endeavor to develop a robust spectral compression model that can project
spectra from any global region, at any time, and of any type into a low-dimensional space
while enabling their precise reconstruction. This approach aims to minimize data storage
requirements. In the realm of remote sensing, traditional dimensionality reduction tech-
niques include PCA, Tasseled Cap Transformation, and Minimum Noise Fraction
(MNF). PCA projects high-dimensional data into a lower-dimensional space by transform-
ing the coordinate system, resulting in low-dimensional features with minimal correlation.
This ensures that a few components can encapsulate the majority of the information con-
tained in the high-dimensional data. PCA can be interpreted as a linear model that per-
forms the transformation between high-dimensional and low-dimensional data.
However, the limitations of PCA are as follows: (1) It necessitates dimensionality reduction
for the entire image, rendering the independent transformation of individual pixels unfea-
sible. PCA is unable to produce a universally applicable model independent of the current
input data, leading to limited flexibility. (2) Each feature is uninterpretable and contains a
different amount of information. Thus, pixels from different times and regions are not
inherently comparable, making PCA unsuitable for time series analysis (Dong and Qin
2018). The tasseled cap transformation reduces dimensionality by converting multispectral
data into a few physically meaningful components using fixed coefficients. While it serves
as a universal linear transformation model for the same sensor, its conversion relationships
are excessively simplistic and uniform. Furthermore, the number of transformed com-
ponents is still substantial, offering no substantial advantage over using the original multi-
spectral data for time series disturbance detection.
In addition to traditional dimensionality reduction methods, deep learning models
such as Autoencoders (Hinton and Salakhutdinov 2006) can be trained to achieve dimen-
sionality reduction for multispectral data, incorporating both linear and nonlinear trans-
formation factors within the model. Its limitation is that it compresses spectra
aggressively, yielding low-dimensional features that lack physical meaning. UMAP, on
the other hand, is a dimensionality reduction technique based on manifold learning. It
can not only train a general model to compress spectra of any type, time, or region
with effective reconstruction of the original spectra but also produce UMAP features
that have physical significance. Figure 11 illustrates that when projecting any two
images with complex surface cover types into a two-dimensional manifold space, the
scatter points not only fall within the same range but also retain a similar overall distri-
bution. Dividing these scatter points into several regions reveals that the points in each
region correspond to pixels of the same land cover type in the images. Thus, we conclude

20 M. LI ET AL.
Figure 11. (a) and (d) are two arbitrary images with complex land cover types. All pixels from these
images are projected into a two-dimensional manifold space, as shown in (b) and (e). (b) and (e) are
divided into several regions, and the scatter points in these regions correspond to pixel locations in
the images, as illustrated in (c) and (f).
that while individual UMAP features lack the tangible physical meaning of tasseled cap
transformation features, pairs of UMAP features can collectively represent different types
of land cover. Land cover types can be represented by the coordinate positions of two
UMAP features.
4.2. Evaluating the optimal UMAP dimension
Figure 12presents the results of disturbance detection using different numbers of UMAP
embeddings. To minimize the storage required for time series analysis, the multispectral
data were compressed into two UMAP embeddings. Despite this aggressive reduction,
the two embeddings are sufficient for effective disturbance detection, showing performance
comparable to that of using three, four, or five embeddings. Whether in the reconstructed
multispectral images from prediction or in the disturbance maps, the two UMAP embed-
dings even achieve results comparable to those obtained with five embeddings.
4.3. Contribution of UMAP embeddings in CCDC
While UMAP features faithfully reconstruct reflectance across various spectral bands,
their ability to maintain temporal patterns is equally vital for land surface characteriz-
ation. Therefore, we investigated how time-series UMAP features perform within the
CCDC algorithm. Figure 13 illustrates the performance of the CCDC model on the
time series of each band in HLS data and each UMAP feature. In fact, the fitting

INTERNATIONAL JOURNAL OF DIGITAL EARTH 21
Figure 12. The two images in the first row represent the most recent observation before the fire and
the first available observation after the fire. The seven-digit numbers on the right indicate the date of
acquisition, with the first four digits representing the year and the last three digits indicating the day
of the year (DOY). The four images in the second row are multispectral reconstructions obtained by
performing time series prediction using UMAP embeddings reduced to 2, 3, 4, and 5 dimensions,
respectively. These represent predicted post-fire conditions. The four images in the third row show
the disturbance detection results based on UMAP embeddings reduced to 2, 3, 4, and 5 dimensions.
performance of CCDC varies across different bands, with discrepancies even in the
breakpoints of the fitting. Overall, the detected breakpoint positions and total count
are fixed, with certain breakpoints detectable in some bands while absent in others.
The two compressed UMAP features also exhibit performance similar to these bands.
From numerous experiments, we observed that the temporal continuity of UMAP
embedding 1 (UMAP1) is slightly inferior, resulting in a higher error rate in detecting
breakpoint positions, whereas UMAP embedding 2 (UMAP2) performs significantly
better. This is attributed to another phenomenon we discovered: UMAP1 primarily
reflects the overall trend changes in the time series, whereas UMAP2 provides a more
detailed characterization of intra-annual variations. Overall, Both UMAP1 and
UMAP2 demonstrate relatively good temporal continuity. Overall, despite UMAP1
and UMAP2 being derived from the nonlinear compression of various bands, they
retain temporal continuity and are well-suited to the CCDC.

22 M. LI ET AL.
Figure 13. The curve fitting of the CCDC model to the time series observations of the six HLS data
bands – Blue, Green, Red, NIR, SWIR1, and SWIR2 – as well as the two UMAP features. The scatter
points represent the time series observations, which are categorized into five types based on the
QA band of the HLS data: clear observations, water, shadow, snow, and clouds. Shadow and cloud
data are excluded from the curve fitting process. The black curve represents the curve fitted by
CCDC. The gray vertical lines indicate where the curve breaks.
4.4. Advantages and extensions
Using a UMAP model trained on globally representative spectra, HLS multispectral data
is compressed into two-dimensional manifold features. Experiments have shown that the
manifold features of any projected remote sensing image exhibit stable shapes and struc-
tures within the two-dimensional manifold space. This provides the theoretical

INTERNATIONAL JOURNAL OF DIGITAL EARTH 23
foundation for the comparability of features following multispectral image dimensional-
ity reduction. Only when the features of different projected remote sensing images are
comparable can they be reliably used for time series analysis. Manifold features have
been proven to perform excellently in predictions and disturbance detection based on
time series algorithm. Moreover, for disturbance detection targeting a specific land
type, certain bands or indices can still yield impressive results. However, this approach
lacks generalizability and cannot address all disturbance types. Different land features
vary greatly in their sensitive wavelength ranges within the electromagnetic spectrum.
For a single type of land surface, disturbance detection can be achieved by selecting
the corresponding sensitive bands or constructing specific indices, which reduces dimen-
sionality and storage space. However, this approach cannot accommodate the complex
conditions of real-world surfaces. Therefore, dimensionality reduction methods that
retain as much of the original spectral information as possible offer a greater advantage.
Indeed, the more abundant the spectral bands and the denser the time series in remote
sensing imagery, the more conspicuous the advantages of our UMAP model become, sig-
nifying its broad and promising applications. Especially in the realm of hyperspectral
remote sensing, the high dimensionality of data hampers the extensive utilization of
hyperspectral imagery (Bioucas-Dias et al. 2013). Previous studies have compared the
efficacy of various techniques for reducing the dimensionality of hyperspectral data
and their application in hyperspectral classification. The findings reveal that, when com-
pared with PCA, LDA, t-SNE, ICA, LLE, and other methods of dimensionality reduction,
UMAP demonstrates superior precision and swifter processing. In the realm of hyper-
spectral image classification, it adeptly preserves the overarching features of images (Li
et al. 2022). In the domain of time-series hyperspectral imagery, our algorithm holds pro-
found significance, serving essential roles in target surveillance, disturbance detection,
species invasion monitoring, plant phenotyping, and the assessment of wood moisture
content and microbial decay in food through ‘hyperspectral videos’.
4.5. Limitations
In this study, we chose HLS imagery for the experiments due to its denser time series,
which lends itself well to continuous Earth observation and disturbance detection.
However, this choice limits the UMAP model’s full potential for lossless compression.
Only six bands in HLS imagery support disturbance detection, resulting in a relatively
low compression ratio. With more spectrally diverse remote sensing data, our UMAP
model would better showcase its capabilities, achieving a more pronounced compression
effect. This paper uses HLS imagery as an example to demonstrate that compression
using the UMAP model can produce stable manifold spaces, with comparable features
suitable for time series analysis.
5. Conclusion
To assess whether reduced features could replace multispectral data for time series analy-
sis and surface disturbance detection, this study combines the advanced nonlinear
dimensionality reduction algorithm UMAP with the time series algorithm CCDC to
detect surface disturbance. First, we developed a manifold model for dimensionality

24 M. LI ET AL.
reduction, suitable for multispectral data of any land surface type, demonstrating robust
stability and interpretability. Next, we applied the manifold embeddings within CCDC
for disturbance detection, achieving accuracy comparable to that of full-band data.
Based on the results and analyses, we made a few conclusions as follows: (1) Using mani-
fold embeddings for disturbance detection streamlines the process while achieving
optimal accuracy; (2) We no longer need to meticulously select sensitive bands or
indices for specific applications or land cover types. The manifold features retain excel-
lent multispectral properties and temporal patterns, making them fully adaptable to
various disturbance detection scenarios; (3) Our approach offers promising potential,
particularly with more comprehensive spectral data and denser time series.
Acknowledgement
The authors appreciate the editors and anonymous reviewers for their valuable suggestions.
Geolocation information statement
The geolocation data in this article is authentic and sourced from actual measurements.
Author contributions
Conceptualization, M.L. and J.Q.; Data curation, M.L.; Formal analysis, M.L.; Funding acquisition,
Q.W.; Investigation, Q.W.; Methodology, M.L., S.Y. and J.Q.; Project administration, Q.W.;
Resources, Q.W.; Software, M.L.; Supervision, Q.W.; Validation, M.L.; Visualization, M.L.;
Writing – original draft, M.L.; Writing – review and editing, M.L., J.Q. and S.Y. All authors
have read and agreed to the published version of the manuscript.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work was supported by the National Natural Science Foundation of China (grant number
42192580 and 42192581)
Data availability statement
The data of this study are available from the corresponding author upon reasonable request.
References
Ali, Mohammed, Mark W. Jones, Xianghua Xie, and Mark Williams. 2019. “TimeCluster:
Dimension Reduction Applied to Temporal Data for Visual Analytics.” The Visual Computer
35 (6): 1013–1026.
Allaoui, Mebarka, Mohammed Lamine Kherfi, and Abdelhakim Cheriet. 2020. “Considerably
Improving Clustering Algorithms Using UMAP Dimensionality Reduction Technique: A
Comparative Study.” In Image and Signal Processing, edited by Abderrahim El Moataz, Driss

INTERNATIONAL JOURNAL OF DIGITAL EARTH 25
Mammass, Alamin Mansouri, and Fathallah Nouboud, 317–325. Cham: Springer International
Publishing. https://doi.org/10.1007/978-3-030-51935-3_34.
Becht, Etienne, Leland McInnes, John Healy, Charles-Antoine Dutertre, Immanuel W. H. Kwok,
Lai Guan Ng, Florent Ginhoux, and Evan W. Newell. 2019. “Dimensionality Reduction for
Visualizing Single-Cell Data Using UMAP.” Nature Biotechnology 37 (1): 38–44. https://doi.
org/10.1038/nbt.4314.
Bioucas-Dias, Jose M., Antonio Plaza, Gustavo Camps-Valls, Paul Scheunders, Nasser Nasrabadi,
and Jocelyn Chanussot. 2013. “Hyperspectral Remote Sensing Data Analysis and Future
Challenges.” IEEE Geoscience and Remote Sensing Magazine 1 (2): 6–36. https://doi.org/10.
1109/MGRS.2013.2244672.
Bullock, Eric L., Curtis E. Woodcock, and Pontus Olofsson. 2020. “Monitoring Tropical Forest
Degradation Using Spectral Unmixing and Landsat Time Series Analysis.” Remote Sensing of
Environment Time Series Analysis with High Spatial Resolution Imagery, 238:110968. https://
doi.org/10.1016/j.rse.2018.11.011.
Comon, Pierre. 1994. “Independent Component Analysis, a New Concept?” Signal Processing,
Higher Order Statistics 36 (3): 287–314. https://doi.org/10.1016/0165-1684(94)90029-9.
Damle, Chaitanya, and Ali Yalcin. 2007. “Flood Prediction Using Time Series Data Mining.”
Journal of Hydrology 333 (2): 305–316. https://doi.org/10.1016/j.jhydrol.2006.09.001.
Deng, Chengbin, and Zhe Zhu. 2020. “Continuous Subpixel Monitoring of Urban Impervious
Surface Using Landsat Time Series.” Remote Sensing of Environment 238:110929. https://doi.
org/10.1016/j.rse.2018.10.011.
Dong, Yining, and S. Joe Qin. 2018. “A Novel Dynamic PCA Algorithm for Dynamic Data
Modeling and Process Monitoring.” Journal of Process Control, Big Data: Data Science for
Process Control and Operations 67:1–11. https://doi.org/10.1016/j.jprocont.2017.05.002.
Dorrity, Michael W., Lauren M. Saunders, Christine Queitsch, Stanley Fields, and Cole Trapnell.
2020. “Dimensionality Reduction by UMAP to Visualize Physical and Genetic Interactions.”
Nature Communications 11 (1): 1537. https://doi.org/10.1038/s41467-020-15351-4.
Fotakidis, Vangelis, Irene Chrysafis, Giorgos Mallinis, and Nikos Koutsias. 2023. “Continuous
Burned Area Monitoring Using Bi-Temporal Spectral Index Time Series Analysis.”
International Journal of Applied Earth Observation and Geoinformation 125:103547. https://
doi.org/10.1016/j.jag.2023.103547.
Graves, Alex, and Graves Alex. 2012. “Long Short-Term Memory.” Supervised Sequence Labelling
with Recurrent Neural Networks, 37–45.
He, Haixu, Jining Yan, Dong Liang, Zhongchang Sun, Jun Li, and Lizhe Wang. 2024. “Time-Series
Land Cover Change Detection Using Deep Learning-Based Temporal Semantic Segmentation.”
Remote Sensing of Environment 305:114101. https://doi.org/10.1016/j.rse.2024.114101.
Hinton, Geoffrey E., and Ruslan R. Salakhutdinov. 2006. “Reducing the Dimensionality of Data
with Neural Networks.” Science 313 (5786): 504–507.
Kennedy, Robert E., Zhiqiang Yang, and Warren B. Cohen. 2010. “Detecting Trends in Forest
Disturbance and Recovery Using Yearly Landsat Time Series: 1. LandTrendr — Temporal
Segmentation Algorithms.” Remote Sensing of Environment 114 (12): 2897–2910. https://doi.
org/10.1016/j.rse.2010.07.008.
Li, Hongda, Jian Cui, Xinle Zhang, Yongqi Han, and Liying Cao. 2022. “Dimensionality Reduction
and Classification of Hyperspectral Remote Sensing Image Feature Extraction.” Remote Sensing
14 (18): 4579. https://doi.org/10.3390/rs14184579.
Maaten, Lvd. 2008. “Visualizing Data Using T-SNE.” Journal of Machine Learning Research 9 (11):
2579.
Maćkiewicz, Andrzej, and Waldemar Ratajczak. 1993. “Principal Components Analysis (PCA).”
Computers & Geosciences 19 (3): 303–342. https://doi.org/10.1016/0098-3004(93)90090-R.
Mao, Yin, Qiuhua He, Jianlong Li, and Bin Yang. 2024. “TACD: A Novel 3-D Swin Transformer
with Enhanced Feature Aggregation for Change Detection in Image Time Series.” IEEE
Transactions on Geoscience and Remote Sensing 62:1–16. https://doi.org/10.1109/TGRS.2024.
3496994.

26 M. LI ET AL.
McInnes, Leland, John Healy, and James Melville. 2018. “UMAP: Uniform Manifold
Approximation and Projection for Dimension Reduction.” https://arxiv.org/abs/1802.03426v3.
Roweis, Sam T., and Lawrence K. Saul. 2000. “Nonlinear Dimensionality Reduction by Locally
Linear Embedding.” Science 290 (5500): 2323–2326.
Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams. 1988. “(1986) Learning Internal
Representations by Error Propagation, Parallel Distributed Processing: Explorations in the
Microstructures of Cognition.” In edited by D. E. Rumelhart, and J. L. McClelland, Vol. I,
318–362. Cambridge, MA: MIT Press. https://doi.org/10.7551/mitpress/4943.003.0128.
Schmitt, Michael, Lloyd Haydn Hughes, Chunping Qiu, and Xiao Xiang Zhu. 2019. “SEN12MS –
A Curated Dataset of Georeferenced Multi-Spectral Sentinel-1/2 Imagery for Deep Learning
and Data Fusion.” http://arxiv.org/abs/1906.07789.
Small, Christopher, and Daniel Sousa. 2022. “The Sentinel 2 MSI Spectral Mixing Space.” Remote
Sensing 14 (22): 5748. https://doi.org/10.3390/rs14225748.
Sousa, Daniel, and Christopher Small. 2022. “Joint Characterization of Sentinel-2 Reflectance:
Insights from Manifold Learning.” Remote Sensing 14 (22): 5688. https://doi.org/10.3390/
rs14225688.
Suh, Ji Won, Zhe Zhu, and Yongquan Zhao. 2024. “Monitoring Construction Changes Using
Dense Satellite Time Series and Deep Learning.” Remote Sensing of Environment 309:114207.
https://doi.org/10.1016/j.rse.2024.114207.
Verbesselt, Jan, Rob Hyndman, Glenn Newnham, and Darius Culvenor. 2010. “Detecting Trend
and Seasonal Changes in Satellite Image Time Series.” Remote Sensing of Environment 114
(1): 106–115. https://doi.org/10.1016/j.rse.2009.08.014.
Woodcock, Curtis E., Thomas R. Loveland, Martin Herold, and Marvin E. Bauer. 2020.
“Transitioning from Change Detection to Monitoring with Remote Sensing: A Paradigm
Shift.” Remote Sensing of Environment, Time Series Analysis with High Spatial Resolution
Imagery 238:111558. https://doi.org/10.1016/j.rse.2019.111558.
Wulder, Michael A., David P. Roy, Volker C. Radeloff, Thomas R. Loveland, Martha C. Anderson,
David M. Johnson, Sean Healey, et al. 2022. “Fifty Years of Landsat Science and Impacts.”
Remote Sensing of Environment 280:113195. https://doi.org/10.1016/j.rse.2022.113195.
Xanthopoulos, Petros, Panos M. Pardalos, and Theodore B. Trafalis. 2013. “Linear Discriminant
Analysis.” Robust Data Mining, 27–33.
Ye, Su, John Rogan, Zhe Zhu, Todd J. Hawbaker, Sarah J. Hart, Robert A. Andrus, Arjan J. H.
Meddens, Jeffrey A. Hicke, J. Ronald Eastman, and Dominik Kulakowski. 2021. “Detecting
Subtle Change from Dense Landsat Time Series: Case Studies of Mountain Pine Beetle and
Spruce Beetle Disturbance.” Remote Sensing of Environment 263:112560. https://doi.org/10.
1016/j.rse.2021.112560.
Ye, Su, Zhe Zhu, and Guofeng Cao. 2023. “Object-Based Continuous Monitoring of Land
Disturbances from Dense Landsat Time Series.” Remote Sensing of Environment 287:113462.
https://doi.org/10.1016/j.rse.2023.113462.
Ye, Su, Zhe Zhu, and Ji Won Suh. 2024. “Leveraging Past Information and Machine Learning to
Accelerate Land Disturbance Monitoring.” Remote Sensing of Environment 305:114071. https://
doi.org/10.1016/j.rse.2024.114071.
Yu, Teng-To, Chun-Yuan Chen, Tai-Hsi Wu, and Yu-Chen Chang. 2023. “Application of High-
Dimensional Uniform Manifold Approximation and Projection (UMAP) to Cluster Existing
Landfills on the Basis of Geographical and Environmental Features.” Science of the Total
Environment 904:167013. https://doi.org/10.1016/j.scitotenv.2023.167013.
Zabel, Florian, Ruth Delzeit, Julia M. Schneider, Ralf Seppelt, Wolfram Mauser, and Tomáš
Václavík. 2019. “Global Impacts of Future Cropland Expansion and Intensification on
Agricultural Markets and Biodiversity.” Nature Communications 10 (1): 2844. https://doi.org/
10.1038/s41467-019-10775-z.
Zhu, Zhe, Shixiong Wang, and Curtis E. Woodcock. 2015. “Improvement and Expansion of the
Fmask Algorithm: Cloud, Cloud Shadow, and Snow Detection for Landsats 4–7, 8, and
Sentinel 2 Images.” Remote Sensing of Environment 159:269–277.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 27
Zhu, Zhe, and Curtis E. Woodcock. 2014a. “Automated Cloud, Cloud Shadow, and Snow
Detection in Multitemporal Landsat Data: An Algorithm Designed Specifically for
Monitoring Land Cover Change.” Remote Sensing of Environment 152:217–234.
Zhu, Zhe, and Curtis E. Woodcock. 2014b. “Continuous Change Detection and Classification of
Land Cover Using All Available Landsat Data.” Remote Sensing of Environment 144:152–171.
https://doi.org/10.1016/j.rse.2014.01.011.
Zhu, Zhe, Curtis E. Woodcock, Christopher Holden, and Zhiqiang Yang. 2015. “Generating
Synthetic Landsat Images Based on All Available Landsat Data: Predicting Landsat Surface
Reflectance at Any Given Time.” Remote Sensing of Environment 162:67–83. https://doi.org/
10.1016/j.rse.2015.02.009.
Zhu, Zhe, Junxue Zhang, Zhiqiang Yang, Amal H. Aljaddani, Warren B. Cohen, Shi Qiu, and
Congliang Zhou. 2020. “Continuous Monitoring of Land Disturbance Based on Landsat
Time Series.” Remote Sensing of Environment, Time Series Analysis with High Spatial
Resolution Imagery 238:111116. https://doi.org/10.1016/j.rse.2019.03.009.