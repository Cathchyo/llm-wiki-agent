Remote Sensing of Environment 331 (2025) 115034
Contents lists available at ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse
Strategic sampling for training a semantic segmentation model in
operational mapping: Case studies on cropland parcel extraction
Rui Lua,b, Ronghua Liaoa,b, Ran Mengc,d, Yingchu Hua,b, Yi Zhaob, Yan Guoe,
Yingfan Zhanga,b, Zhou Shia,b, Su Yea,b,*
aState Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China
bInstitute of Agricultural Remote Sensing and Information Technology Application, College of Environmental and Resource Sciences, Zhejiang University, Hangzhou
310058, China
cArtificial Intelligence Research Institute, Faculty of Computing, Harbin Institute of Technology, Harbin 150008, China
dNational Key Laboratory of Smart Farm Technologies and Systems, Harbin 150008, China
eInstitute of Agricultural Information Technology, Henan Academy of Agricultural Sciences, Zhengzhou 450002, China
A R T I C L E I N F O A B S T R A C T
Editor: Marie Weiss Semantic segmentation of remotely sensed images has become increasingly popular for a wide range of natural
resource and urban application, yielding promising results. To an operational semantic segmentation mapping
Keywords: project, having more samples generally enables the model to better extract target features, achieving higher
Semantic segmentation accuracies. However, annotating remote sensing image samples for model training is a time-consuming and
Deep learning
labor-intensive process. Strategic sampling aims to minimize the efforts in collecting new training samples for a
Training samples
mapping project, which has been not well studied yet for semantic segmentation. To approach this topic, we
Balanced sampling
employed a hybrid way for combining meta-analysis and case studies to investigate the best practices for stra-
Transfer strategy
tegic sampling. Three factors relating to strategic sampling will be investigated: sample size, distribution and
transferring methods. We first reviewed 334 recently published papers that adopted semantic segmentation for
operational mapping projects to summarize the current status of training sample design from various mapping
scenarios. Subsequently, we constructed a large dataset of over 12,000 high-quality annotated image patches for
cropland parcel mapping across five study sites, and evaluated various sampling strategies using a baseline
segmentation model. We also proposed a novel balanced sampling method, which leveraged patch-based entropy
and edge complexity to classify sample diversity. Our findings revealed that (1) both meta-analysis and the case
studies suggested that ~4 % of the total mapping patches were the optimal training sample size under random
sampling, i.e., the minimum size to reach accuracy saturation; (2) compared to random sampling, the newly
proposed balanced sampling was superior due to its decreasing the required sample size from ~4 % to 2.5 % of
the total patches in mapped areas; (3) sample transfer and model transfer present identical performance for
relaxing the average local sample demand from 2.5 % to 0.5 % of total patches, with sample transfer being
slightly more accurate than model transfer (Global Total-Classification errors: 0.298 vs 0.308). This study offers a
heuristic framework for applying strategic sampling in semantic segmentation, providing valuable practical
guidance for implementing deep learning in an operational scenario.
1. Introduction 2024; Zhang et al., 2023), and land cover mapping (Li et al., 2020;
Zhang et al., 2019). Benefited from the capability of learning intricate
Semantic segmentation of remotely sensed images, i.e., assigning a spatial and temporal patterns, semantic segmentation often surpasses
category to each pixel in an image based upon state-of-art deep learning traditional machine learning tasks particularly for mapping diverse and
models, have become the leading approach for a wide range of surveying nuanced geographic features (Ma et al., 2019; Reichstein et al., 2019;
tasks including agricultural field extraction (Persello et al., 2019; Yuan et al., 2020; Persello et al., 2022). It is widely acknowledged that a
Waldner and Diakogiannis, 2020), urban sprawl detection (Kim et al., larger training dataset could provide better exposure for various
* Corresponding author at: State Key Laboratory of Soil Pollution Control and Safety, Zhejiang University, Hangzhou 310058, China.
E-mail address: su.ye@zju.edu.cn(S. Ye).
https://doi.org/10.1016/j.rse.2025.115034
Received 19 May 2025; Received in revised form 10 September 2025; Accepted 14 September 2025
Available online 20 September 2025
0034-4257/© 2025 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
geographic patterns of different scenarios to reduce the chances of to random or proportional sampling (i.e., assigning training samples in
overfitting from outliers as well as to enhance the generalization to proportion to the area of each class), whereas it possibly suffers a lower
unseen data (Yu et al., 2018; Bergen et al., 2019; Yuan et al., 2021; Grift overall accuracy (Colditz, 2015; Nguyen et al., 2020; Zhou et al., 2020).
et al., 2024). However, unlike popular image label databases in the For example, Du et al. (2015) developed a voting-distribution ranked
computer vision domain (e.g., ImageNet, COCO) (Deng et al., 2009; Lin rule, which averaged multiple reliable voting distributions for each class
et al., 2014), the training datasets are often not universally available for to determine weights and increased the representation of minority
semantic segmentation of remotely sensed images, not only because classes. However, existing studies on balanced sampling methods are
local geographic patterns are commonly too complicated to be repre- primarily based on pixel-level samples. In the context of semantic seg-
sented by a single dataset, but also owing to the rarity of a universal land mentation, there is no straightforward method for assigning sample
category system (e.g., agricultural fields are defined differently among numbers when using an image patch as the sampling unit, as it consists
different regions) (Reichstein et al., 2019). As a result, remote sensing of multiple categories. This makes it challenging to directly apply
professionals are frequently required to manually generate as many new balanced sampling to a semantic-segmentation task. As a result, pro-
image patches as possible for mapping projects (Kattenborn et al., 2021), fessionals often resort to random sampling of image patches (Boschetti
calling for considerable annotation efforts and budgets. It is essential for et al., 2016; Stehman et al., 2022), which can lead to poor performance
prioritizing a smaller, more representative training sample set, partic- for minority classes in imbalanced datasets and generate redundant
ularly when the mapping region is large and acquiring training data is samples for easily identifiable categories. Hence, there is a need for
expensive. proposing a new balanced sampling strategy tailored for patch-based
Strategic sampling is a group of techniques for minimizing the efforts samples to guide sample selection for the semantic segmentation tasks.
in collecting new training samples while keeping the accuracy uncom- Besides sampling design, another approach for strategic sampling is
promised (Brown, 2006). Traditionally, in pixel-based classification, leveraging global samples (i.e., samples collected from the entire
previous discussions on strategic sampling surround sample size (Foody geographic region) to reduce the need for newly collected samples from
et al., 2006; Zhu et al., 2016; Ramezan et al., 2021; Rajput et al., 2023), a specific mapping region, i.e., local samples. Model transfer is such an
and the distribution of samples across categories (Foody and Mathur, approach that takes advantage of a pre-trained model from a large-scale
2006; Jin et al., 2014; Mellor et al., 2015). Inadequate sample size would dataset and fine-tunes it for a new targeted mapping region (Ma et al.,
suffer from an underfitting of training data and fail to cover full 2024; Pan and Yang, 2010; Zhao, 2017; Zhu et al., 2021). Model transfer
geographic variability. Though increasing sample size generally could unfreezes the last layers of the base model and only adjusts the higher-
enhance the performance, the accuracy curve may cease to increase after order feature representation using the new local samples, thereby
a certain sample size (Heydari and Mountrakis, 2018). The ideal sample reducing the need for large amounts of training dataset. For example,
size is the minimum number of samples required to achieve a plateau in Wieland et al. (2023)applied a model transfer approach, enabling a pre-
accuracy curves, balancing annotation costs with model performance. trained model to identify water bodies in remote sensing data from
While some literature suggests using a sample size of 10–30 times the different sources. Alternatively, it is also common for transferring local
number of features for a classifier (Piper, 1992; Van Niel et al., 2005), it samples to a global training dataset and then building a completely new
is more reasonable to determine the sample number by considering the deep learning model from the scratch, i.e., sample transfer (Brown et al.,
total area to be mapped, as it reflects landscape variability and the 2020; Zhang et al., 2024). Sample transfer is more frequently applied in
complexity of the classification scene (Stehman and Wickham, 2011; large-scale remote sensing mapping. For example, Brown et al. (2020)
Olofsson et al., 2014). As such, Zhu et al. (2016)tested the training pixel employed training data selected from a 3 by 3 tile window where the
number from 2500 to 25,000 for land cover classification of a single central tile was the tile to be classified. Zhang et al. (2024)also com-
Landsat scene based on a random-forest classifier, and reported that the bined the local samples from the center tile and the global samples from
accuracy stopped increasing when the training set exceeded 20,000 its neighborhood tiles to build a classifier for the center tile. Compared
pixels, i.e., ~0.1 % of a Landsat tile. However, existing researches on to model transfer, sample transfer allows for adjusting the weights of all
optimal sample size have primarily focused on pixel-based samples. layers, offering greater flexibility to adapt to a new mapping region.
Different from pixel-based sampling scheme that traditional machine However, it often comes with higher computational costs due to the
learning techniques mostly fall within, training samples for deep need to train a new model from scratch. To our knowledge, no studies
learning are mostly based upon small sub-images, i.e., image patches. ever comparatively reported their performances and new local samples
For each image patch, the pixels are labeled as the classes of interest, and required for the two transfer methods.
the number and shapes of land-cover classes are inherently variable. The Aiming to minimize the effort required to collect new training
different nature between image patches and pixel samples limits a direct patches, this study will explore different strategic sampling configura-
knowledge transfer for sample selection from traditional machine tions and identify the best training sample selection practices for se-
learning to deep learning. In contrast to the relatively simpler model mantic segmentation, using a hybrid approach of meta-analysis and case
architecture of traditional classifiers (e.g., random forest, support vector studies. In this study, a sample refers to an image patch used for training
machine), semantic segmentation enables a better generalization by the semantic segmentation model (specifically, a 256 × 256-pixel
stacking multiple convolutional and pooling layers with more model image). Sampling denotes the process of selecting patches to construct
hyperparameters, thereby often requiring a larger sample size. Chen the training dataset. In this study, the sample size is defined as the
et al. (2024)suggested that in geographically similar regions, approxi- relative training patch number, which is measured as the patches
mately one-tenth of the data might be sufficient to train a CNN model selected for training divided by the total patches to be mapped. This
effectively. However, their study did not assess the impact of varying measurement helps eliminating the influence of varying image sizes and
sample sizes on model accuracy, and whether one-tenth represented an differences in the spatial resolution of remote sensing data. Three key
optimal sample size remained unknown. To our knowledge, most pre- factors in the training sample selection process were primarily investi-
vious semantic segmentation studies determined the training patch gated: sample size, sample distribution, and transfer methods. To
number based on subjective judgment or the annotation budget. It still address various semantic segmentation cases, we first performed a meta-
lacks a heuristic to quickly estimate an economic sample size for a tar- analysis on 334 journal articles between 2015 and 2024, covering a
geted mapping region without sensitivity tests. broad range of mapping themes. This analysis summarized the general
The choice of sample distribution answers the question for how to status on sample size, sample distribution, and transferring methods for
assign the sample numbers to different classes. The literature consis- semantic segmentation. Second, through five case studies of cropland
tently reports that balanced sampling (i.e., an equal number of samples parcel mapping, we created a large open-access training dataset con-
per class) helps prevent model bias toward the majority class, compared sisted of over 12,000 high-quality labeled patches, and then evaluated
2

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
different sampling practices concerning sample size, distribution and
transferring methods based upon a baseline semantic segmentation
model. Cropland parcel mapping is often considered as a challenging
task owing to their complex parcel forms, diversified spectral charac-
teristics, and incontiguous boundaries intergraded with surrounding
vegetation (Masoud et al., 2020; Estes et al., 2022; Lu et al., 2024),
influenced by factors such as crop type, growth stage, soil conditions,
and environmental variables. This makes cropland parcel mapping an
ideal application for testing the performance of different training sample
selection strategies for deep learning. In the past studies, various sample
configurations have been adopted to deploy semantic segmentation for
extracting parcel boundaries (Waldner and Diakogiannis, 2020; Turko-
glu et al., 2021; Cai et al., 2023; Pan et al., 2023), which echoed the lack
of standardized criteria for selecting training samples. To compare the
effectiveness of different sampling practices, we will analyze the point at
which the error curve first flattens with increasing numbers of input Fig. 1. Year of journals for the 334 referred articles for the meta-analysis.
samples. An optimal method should minimize the number of training
samples needed without compromising model performance. By outputs through post-processing, our focus was on the accuracy of the
combining meta-analysis and case studies, this work aims to provide a raster-based cropland parcel representations generated by the model.
heuristic solution for strategic sampling that achieves the most cost-
effective training sample selection. More specifically, we will answer 2.2.1. Study sites
the three following questions: We selected five typical study sites in China (Fig. 2), including Xin-
jiang (XJ), Jilin (JL), Guangxi (GX), Hubei (HB), and Zhejiang (ZJ).
(1) How many training samples in minimum are required when the Table 1summarizes the diverse characteristics of the agricultural sys-
model accuracy saturates for semantic segmentation? tems across the study sites, which represent a range of scenarios for
(2) What is the most effective way for distributing training samples in extracting cropland parcels from high-resolution remote sensing images.
the form of image patches? These study sites were selected to capture the diversity of cropland
(3) What is comparative performance for model and sample transfer systems, ranging from large-scale mechanized fields to smallholder-
in term of mitigating local sample demand? based parcels, to demonstrate the generalizability of the proposed
sample selection methods.
2. Datasets and study sites
2.2.2. Satellite images
2.1. Meta-analysis data collection For each study area, we selected a scene of Gaofen-2 (GF-2) high-
resolution imagery. The GF-2 satellite contains a panchromatic sensor
Given by a vast body of current literature on semantic segmentation, with 1-m resolution and a multispectral sensor with 4-m resolution,
we focused on three top remote sensing journals, i.e., Remote Sensing of covering a swath of 45 km with a revisiting cycle within 5 days (Chen
Environment (RSE), ISPRS Journal of Photogrammetry and Remote Sensing et al., 2022; Tong et al., 2020). The GF-2 data can be retrieved at htt
(ISPRS P&RS), International Journal of Applied Earth Observation and ps://data.cresda.cn. All images were acquired in 2022, during the
Geoinformation (JAG), and two data-based journals, i.e., Scientific Data period between crop harvest and early growth. This timing facilitated
(SD) and Earth System Science Data (ESSD). We did not include the their distinction from surrounding features such as grasslands, and also
technical journals such as IEEE Transactions on Geoscience and Remote allowed field roads to be clearly visible (Cheng et al., 2020). The pre-
Sensing (TGRS), as their articles primarily focused on algorithm inno- processing steps of images included radiometric calibration, atmosphere
vation rather than land-cover mapping. Their evaluated algorithms were correction, and geometric correction. We applied the Gram-Schmidt
based on benchmark labeling datasets (e.g., Semantic Labeling Chal- Pan-Sharpening method for image fusion by resampling multispectral
lenge datasets (Pastorino et al., 2022)), making it difficult to infer in- images with a high-resolution panchromatic image, resulting in 1-m
formation about the total patches to be mapped. Only studies that images with four multispectral bands, i.e., blue, green, red, and near-
provided the final segmentation map for their entire study area were infrared.
considered for sample size demand, calculated as the proportion of the
training sample patches relative to the total patches in the mapping 2.2.3. Labeled patch dataset
extent, namely training patch proportion. We performed an initial We generated a large number of high-quality labeled image patches
search in the Science Direct (https://www.sciencedirect.com/) or Web for testing sampling strategies. Each GF-2 image was divided into 256 ×
of Science (https://webofscience.clarivate.cn/) database for each jour- 256 pixel patches (Li et al., 2023; Waldner and Diakogiannis, 2020).
nal using the keyword “semantic segmentation” with a year range From each study site, approximately 20 % of the patches were randomly
specification of “2015–2024” and an exclusion of “Review articles” selected, resulting in around 2500 patches per site and 12,500 patches in
(search date: Dec. 10, 2024). As a result, we obtained 334 journal arti- total. A team of experienced remote sensing experts manually annotated
cles (RSE: 27; ISPRS P&RS: 168; JAG: 117; SD: 19; ESSD: 3, see Fig. 1). all crop field boundaries within each patch through visual interpreta-
The complete list of the selected articles was given in Section S1 of the tion, dedicating over 1000 working hours to the annotation process. The
Supplementary Material. The year-over-year increase in publications labeled patches were then evenly split into two pools: a training sample
highlighted the growing prominence of remote sensing semantic seg- pool (10 % of total patches), used to generate various sampling con-
mentation as a research focus (Fig. 1). figurations, and a testing sample pool (10 %), used to independently
assess model accuracy across different sampling strategies.
2.2. Case study sites and data We have released the labeled image patches (China’s Crop Parcel
Training Dataset, CCPTD) as a potential benchmark dataset for future
We selected cropland parcel mapping as a case study to address the study, which is publicly available at https://doi.org/10.5281/zenodo
sample selection problem in remote sensing semantic segmentation .16595511.
tasks. Since vector parcel boundaries could be derived from raster
3

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 2. The study sites with various agricultural characteristics. (a) Their locations in China. (b)-(f) The 1-m GF-2 imagery and cropland parcel examples for the five
case study sites.
2.2.4. Land cover data number of total patches to be mapped, sampling distribution approach, and
We used the China Land Cover Dataset (CLCD) (Yang and Huang, transferring method. The attribute number of training patches refers to the
2021) as a priori of cropland percentage for the newly proposed samples used for model training, whereas number of total patches to be
balanced sampling approach. The CLCD products were made through mapped represents the total number of patches covering the entire
feeding temporal metrics derived from Landsat images into a random mapping area. The training patch proportion, calculated as the ratio be-
forest classifier, with a reported overall accuracy of 79.3 %. The CLCD tween these two attributes, was used as an indicator of the training
dataset provides 30-m annual land-cover products from 1990 to 2022 sample size relative to the total mapping area. Table 2 describes ten
for China, composed of nine land-cover classes including cropland. The attributes that we recorded for the 334 articles. We conducted a statis-
CLCD data of the year 2022 (Fig. 1a) was selected and aligned with the tical analysis based on ten sampling-related attributes to summarize the
GF-2 images to estimate cropland proportion for each image patch. The current status of sampling strategies in practical remote sensing map-
CLCD dataset are publicly available at https://zenodo.org/records ping using semantic segmentation. This meta-analysis offers valuable
/8176941. insights into the sampling practices reported across the literature. While
our case study focuses on a typical application, the meta-analysis en-
3. Methods ables us to examine sample selection strategies across a broader spec-
trum of remote sensing applications. This broader perspective not only
3.1. Meta-analysis methodology provides a more comprehensive understanding of real-world sampling
approaches but also helps assess the generalizability of the findings
We recorded six sampling-related attributes for the 334 articles, derived from our case studies.
including mapping theme, number of categories, number of training patches, Of note is that many studies did not report specific information on
4

R. Lu et al.                                                                                                                                                                                            R  e m   o  t e   S  e n  s i n  g    o f   E  n  v  i r o  n m   e  n t 331 (2025) 115034
Table 1
Five case study sites for cropland parcel extraction to test performance of different sample configurations (“total patches to be mapped” denotes the total number of
samples resulting from dividing the entire imagery into image patches).
Study  Region Image size  Total patches  Acquisition  Agricultural system types Descriptions
| sites |     | (pixels) | to be mapped |     | date |     |     |     |     |
| ----- | --- | -------- | ------------ | --- | ---- | --- | --- | --- | --- |
XJ Northwestern  45,605 × 14,939 09/15/2022 Mechanized large-scale  The croplands are large and situated in flat terrain, characterized by
China 33,853 agriculture highly mechanized agricultural practices. The main crops include
cotton and wheat, primarily grown in a single season.
JL Northeastern  48,883 × 15,998 03/28/2022 Northeast Plains  Croplands are evenly distributed across plain landscapes, with large-
China 34,607 agricultural system scale monoculture practices. Common crops include maize, soybean,
and rice, predominantly cultivated in a single season.
37,770 ×
GX Southwestern  14,981 03/12/2022 Smallholder fragmented  The region is mountainous, with small, irregular, and fragmented
China 39,527 agriculture croplands. Typical crops include sugarcane, rice, and fruits, mostly
grown in two seasons under smallholder management.
37,914 ×
HB Central China 8917 10/23/2022 Mixed plain and  Croplands in this region are distributed across varied topography,
24,832 mountain agriculture including plains and mountainous areas. Main crops are rice, wheat,
and rapeseed, cultivated in both single and double cropping systems.
ZJ Eastern China 35,362 × 12,728 12/14/2022 Smallholder agriculture  Croplands are fragmented and scattered, with abundant water
34,542 with abundant water  supporting rice, wheat, oilseed rape and vegetables. The fields are
|     |     |     |     |     | systems |     | managed by smallholders, with both single and double cropping  |     |     |
| --- | --- | --- | --- | --- | ------- | --- | -------------------------------------------------------------- | --- | --- |
systems practiced.
of training patches was reported but the total number of patches was
Table 2  missing, we estimated the latter by dividing the total number of pixels in
Ten attributes for the reviewed articles. the mapping area by the size of a training patch. If the total number of
| ID Attributes |     | Definition |     | Values |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
pixels was not provided, we calculated it using the reported mapping
1 Journal Published journal of the  area and the spatial resolution of the remote sensing imagery. Studies
paper lacking all these information were excluded from the sample size
| 2 Year |     | Year of publication |     |     |     |     |     |     |     |
| ------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
statistics.
| 3 Mapping theme |     | Object of remote sensing  |     | 1) Land cover；    |     |     |     |     |     |
| --------------- | --- | ------------------------- | --- | ----------------- | --- | --- | --- | --- | --- |
|                 |     | semantic segmentation     |     | 2) Agricultural;  |     |     |     |     |     |
|                 |     | mapping                   |     | 3) Forest;        |     |     |     |     |     |
3.2. Case study design
4) Impervious surface;
5) Water body;
|              |     |                               |     | 6) Disaster; 7) Others |     | 3.2.1. | Deep learning model |     |     |
| ------------ | --- | ----------------------------- | --- | ---------------------- | --- | ------ | ------------------- | --- | --- |
| 4 Number of  |     | Count of distinct classes to  |     |                        |     |        |                     |     |     |
Our study employed ResUNet-a model (Diakogiannis et al., 2020), an
| categories |     | be segmented in the  |     |     |     |     |     |     |     |
| ---------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
established deep learning model for cropland parcel extraction, which
semantic segmentation
task has shown superior performance in past studies (Waldner and Dia-
5 Number of  Number of patches  kogiannis, 2020; Jong et al., 2022; Li et al., 2023). Its structure was
training patches selected for model  presented in Fig. 3. ResUNet-a is a deep learning model built upon the
training UNet architecture (Ronneberger et al., 2015), featured by a symmetric
| 6 Number of total  |     | Number of patches to be  |     |     |     |     |     |     |     |
| ------------------ | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
encoder-decoder structure with skip connections between correspond-
| patches to be  |     | mapped for a semantic-  |     |     |     |     |     |     |     |
| -------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
ing stages. This design enhances the model ability to capture contextual
| mapped |     | segmentation task |     |     |     |     |     |     |     |
| ------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
7 Training patch  The proportion of training  information while maintaining fine-scale details. The core design of
proportion patches over the total  ResUNet-a is the ResBlock-a module (Fig. 3b) that integrates multiple
patches to be mapped
parallel atrous convolutions within residual block. The atrous convolu-
| 8 Sampling  |     | The sample distribution  |     | 1) Random: samples are  |     |     |     |     |     |
| ----------- | --- | ------------------------ | --- | ----------------------- | --- | --- | --- | --- | --- |
distribution  strategy of the training  selected randomly;  tional branches with different dilation rates perform feature extraction
approach samples 2) Balanced: samples are  at  various  receptive  fields,  improving  identification  of  targets  at
selected to ensure equal  different scales and locations. To enhance the model performance,
representation across
ResUNet-a employs a pyramid scene parsing pooling (PSP pooling) layer
classes;
between the encoder and decoder, as well as before the output layer, and
3) Systematic: samples are
then applies a multi-task learning to achieve more accurate cropland
selected based on a
predefined selection rule;  parcel extraction by leveraging the constraints between related tasks.
4) No information We employed the Tanimoto distance as the loss function during the
9 Transferring  Transferring strategy used  1) Direct use of an existing  training stage to aid in model convergence while maintaining a balance
| method |     | when validating model  |     | model;  |     |     |     |     |     |
| ------ | --- | ---------------------- | --- | ------- | --- | --- | --- | --- | --- |
across multiple tasks (Waldner and Diakogiannis, 2020). Tanimoto loss,
|     |     | transfer capabilities or  |     | 2) Sample transfer: model  |     |     |     |     |     |
| --- | --- | ------------------------- | --- | -------------------------- | --- | --- | --- | --- | --- |
mapping in other regions is trained using a mix of  a variant of Dice loss, focuses on maximizing the overlap between pre-
local and global samples;  dicted and true labels in segmentation tasks. It provides smoother
3) Model transfer: model is
gradient changes during optimization, leading to more stable conver-
pretrained with global
gence (Diakogiannis et al., 2020). This results in better boundary ac-
samples and then fine-
tuned with local samples;  curacy and overall segmentation quality, particularly in improving the
4) No transfer shape of parcels. The Tanimoto distance loss function is defined as:
| 10 Comments |     | Other situations       |     |     |     |         |                   |               |      |
| ----------- | --- | ---------------------- | --- | --- | --- | ------- | ----------------- | ------------- | ---- |
|             |     |                        |     |     |     | ̃(p,l)= | T(p,l)+T(1(cid:0) | p,1(cid:0) l) |      |
|             |     | encountered in         |     |     |     | T       |                   |               | (1)  |
|             |     | information extraction |     |     |     |         | 2                 |               |      |
with
∑
t h e   n u m b e r   o f  t r a i n i n g   p a t c h e s   o r   t o t a l   m a p p in g  p a t c h e s .  I f   t h e   n u m b e r   (p li )
|     |     |     |     |     |     | T(p,l)=∑ | (cid:0) i )i | ∑   |     |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- |
o f  t r a i n i n g   p a t c h e s   w a s   u n a v a i l a b l e ,   t h e   s t u d y   w a s   e x c l u d e d   f r o m   th e   2+li 2 (cid:0) (pili ) (2)
|                    |                            |                           | –                |                         |                             |     | i pi | i   |     |
| ------------------ | -------------------------- | ------------------------- | ---------------- | ----------------------- | --------------------------- | --- | ---- | --- | --- |
| s a m p l e   s iz | e   s t a t i s t i c s  ( | i . e . ,   a t t r i b u | t e s  5 7   i n |   T a b l e   2 ) .   W | h e n   t h e   n u m b e r |     |      |     |     |
5

R. Lu et al.                                                                                                                                                                                            R  e m   o  t e   S  e n  s i n  g    o f   E  n  v  i r o  n m   e  n t 331 (2025) 115034
Fig. 3. Graphic explanation for ResUNet-a model (Diakogiannis et al., 2020). (a) The overview of the ResUNet-a architecture. (b) The ResBlock-a module that
integrates residual connection and parallel atrous convolutions with different dilation rates. (c) PSP pooling layer.
√̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
where p presents the probability map output by the model, and l rep-
|     |     |     |     |     | SO (i)2+ | SU (i)2 |     |     |
| --- | --- | --- | --- | --- | -------- | ------- | --- | --- |
r es e n ts   t h e  c o r r e s p o n d i n g  s a m p l e   l a b e l .   F o r  m u lti-task learning, we used  ST (i)= (5)
2
| th e  a v e r a | g e   o f  t h e   lo s s   fu | n c t io n s   f o r   a l l |   ta s k s:   |     |     |             |     |     |
| --------------- | ------------------------------ | ---------------------------- | ------------- | --- | --- | ----------- | --- | --- |
|                 | T ̃ (p,l)+T                    | ̃ (p,l)+T                    | ̃ (p,l)       |     | are | a (R ∩ Pi ) |     |     |
̃ (p,l)= extent bounda ry distance (3)  SO (i)=1(cid:0) i (6)
| T MTL |     |     |     |     |     | a( )     |     |     |
| ----- | --- | --- | --- | --- | --- | -------- | --- | --- |
|       |     | 3   |     |     |     | a re R i |     |     |
We used the AdamW optimizer (Loshchilov and Hutter, 2019) with a
are a (R ∩ Pi )
|     |  × (cid:0) 5 |     |     |     | (i)=1(cid:0) | i   |     |     |
| --- | ------------ | --- | --- | --- | ------------ | --- | --- | --- |
w e i g h t  d e c ay  o f   1 1 0 .  T h e   m a x im u m   n u m b e r  o f t r a i n in g   e p o c h s   w a s   SU a( ) (7)
|                   |                             |                            | × (cid:0) 4          |                                |     | a re P i |     |     |
| ----------------- | --------------------------- | -------------------------- | -------------------- | ------------------------------ | --- | -------- | --- | --- |
| s e t  t o  2 0 0 | ,  w it h   a n  in it ia l |  l e a r n i ng   ra te  o | f  1   1 0 . A f t e | r  1 0 0   e p o c h s ,  th e |     |          |     |     |
learning rate decayed to 10 % of the initial value, resulting in a learning
rate of 1 ×10 (cid:0) 5 for the remaining 100 epochs. The batch size was set to  where Ri denotes the reference parcels in ground truth, Pi denotes the
predicted parcels in model results, n represents the parcel number, SO is
16 during training.
the over-segmentation error, and SU is the under-segmentation error.
We generated the GTC curve along with increasing sample sizes. The
3.2.2. Performance evaluation
best sample size was identified when the GTC curve just reached the
In this study, we chose the GTC (Global Total-Classification) to
level-off point, which was defined as the first sample size reaching 95 %
evaluate the accuracy of deep learning models with different sampling
|     |     |     |     |     | of the maximum accuracy, i.e., 1(cid:0) |     | 0.95×(1(cid:0) GTCmin | ), following the  |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --------------------- | ----------------- |
configuration. GTC is an object-based evaluation metric that compre-
practice for the semi-variogram in geostatistics (Chen and Gong, 2004;
hensively assesses over-segmentation and under-segmentation errors in
Garrigues et al., 2008). Given that the GTC typically decreases with an
model predictions, making it well-suited for assessing both the geo- increasing number of training samples and eventually will be stabilized,
metric and thematic accuracy of parcel segmentation tasks (Li et al.,  its trend is analogous to an inverted semi-variogram curve, where the
2023; Zhao et al., 2025). GTC is formulated as follows:
( ) point of stabilization at which GTC first levels off corresponds to sill.
| ∑   |     | ( ) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
n (i)×∑ a r e a P i U n li k e   sig n i fi c a n c e   t e s ti n g  m e th o d s   (C o l li n s   e t   a l. ,   2 0 2 0 ;   F o o d y   e t  a l . ,
| GTC= | ST  |     |     | (4)  |     |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
i=1 n a r e a ( Pi ) 20 0 6 ) ,  w h ic h   i d e n t if y   p r e -d efi n e d  s a m p l e   si z e s   o r   a c c u r a c y   t h re s h o l d s ,
|     |     | i = 1 |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- |
the variogram-based method enables us to pinpoint the exact point when
with
the error curve first flattens out, even when the number of samples at
that point is not predetermined. The Y value of the level-off point reflects
the minimum GTC (i.e., the best model performance), while its X value is
6

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
the minimum required sample size to reach the optimal sample size for category. Also, focusing solely on categorical attributes overlooked the
the best balance between the accuracy and the annotation costs. The morphological complexity of the geographic features. For this study, we
smaller X value of the level-off point indicates the less sample patches proposed a new stratified sampling to balance the training patch selec-
required to reach the best model performance. tion, hereafter named as balanced sampling. We defined training strata
To validate our findings, we conducted the same curve-based anal- based upon two patch-based features: thematic entropy (H) and edge
ysis using the F₁-score, another widely used performance metric for se- complexity (E). Thematic entropy captures the amount of information
mantic segmentation in the literature (the results were shown in the related to the categorical composition within each patch, while edge
Supplementary Material). In addition, we will perform a visual compar- complexity quantifies the structural intricacy of object boundaries.
ative evaluation of parcel maps generated under different sampling Together, these two features characterize training patches from com-
configurations to confirm the accuracy of the model achieved by the plementary perspectives, i.e., thematic and morphological measure-
selected best sampling strategy. ment. Entropy calculation requires external data that provide prior
knowledge about the class distribution, whereas edge complexity can be
3.2.3. Experiment setup derived directly using edge detection algorithms, without the need for
To answer three research questions for this study, we designed three additional input data.
sub-experiments respectively for training size, sample distribution and Fig. 5illustrates the process of the proposed balanced sampling. The
transferring method (Fig. 4): thematic entropy reflects the variation of map categories, and the patch
with low entropy has more uniform pixel labels. We derived a rough
3.2.3.1. Training size. For each study site, we established a series of estimation of the cropland percentage from a prior crop product (i.e., the
training sample sets using the proportions of training patches out of the CLCD product), which often exists for most remote sensing applications,
total patches in mapping areas, with a step size of 0.2 % for the range and then calculated the thematic entropy (H) using the following
from 0 % to 1 %, and a step size of 1 % for the range from 1 % to 10 %. formula:
We assessed the GTC curves under two sample distribution approaches, ∑n
i.e., the random sampling and the newly proposed balanced sampling H=(cid:0) PilogPi (8)
(see “sample distribution”). Their optimal training size was determined as i=1
the X value of the level-off point of their GTC curve.
where n presents the number of categories to be classified, and P denotes
the proportion of each category. Based on the geographic coordinates of
3.2.3.2. Sample distribution. Sampling design in machine learning can
each training sample, the corresponding area in the land-cover product
generally be divided into three categories: random sampling, stratified
was identified to obtain land-cover data for that sample. Even though
sampling (i.e. balanced sampling), and systematic sampling (Olofsson
the spatial resolutions of the two datasets differ, aligning them by
et al., 2014). Systematic sampling is inherently rule-based and context-
sample extent ensures that the land-cover data can still capture the
dependent, making it difficult to evaluate comparatively. Therefore, we
proportion of cropland within the sample region. Edge complexity refers
will test the other two sample distribution approaches, random sampling
to the level of detail or intricacy in the boundaries (edges) of objects
and stratified sampling for semantic segmentation. Existing stratified
within an image. We computed edge complexity by calculating edge
sampling methods for semantic segmentation studies often used arbi-
length after applying the Canny edge detection algorithm (Turker and
trary definition for patch-based stratum. For example, Qurratulain et al.
Kok, 2013). We divided each feature into three groups using quantile-
(2023) interpreted the majority category for each training patch and
based thresholds, resulting in nine strata for the image patches with
then assigned higher weights for those patches dominated by minority
two features. These strata represented different cropland patterns. For
Fig. 4. The experiment design for exploring best practices for the three key factors of strategic sampling for semantic segmentation: 1) training size, 2) sample
distribution, and 3) transferring method.
7

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 5. The process of the proposed balanced sampling. The balanced sampling defines nine strata by two-dimensional measurements, i.e., thematic entropy and edge
complexity, and then assigns training patches to each stratum using quantile-based thresholds. HH: High thematic entropy. MH: Medium thematic entropy. LH: Low
thematic entropy. HE: High edge complexity. ME: Medium edge complexity. LE: Low edge complexity.
example, “low entropy – low edge complexity” corresponded to large- 4. Results
scale industrial cropland or non-agricultural areas with clean edges,
while “high entropy – high edge complexity” referred to complex re- 4.1. Meta-analysis results
gions where scattered, small-scale croplands were interwoven with non-
cropland backgrounds. The newly proposed balanced sampling will Fig. 6 summarizes the meta-analysis on sematic segmentation for
assign an equivalent number of training patches to each stratum, remote sensing applications. For sample size, 102 out of the 334 articles
ensuring a high diversity of training patches, based upon the hypothesis provided explicit information on the proportion of training patches over
that the more diversified and representative sample patches could the total mapping area (Fig. 6a). The training patch proportion for se-
reduce the demand of the total training samples needed. We will test the mantic segmentation concentrated on either very small (“0–1 %”) or
random and proposed balanced sampling, and compare the differences very large sample sizes (“>20 %”), with a median of 4.2 % total patches.
of level-off point location for the two approaches. We identified that the distribution strategies for semantic segmentation
The code script for our proposed balanced sampling method is were dominated by random sampling which was adopted by more than
publicly available at https://github.com/Remote-Sensing-of-Land-Re half of the studies (51.1 %) (Fig. 6b). Some articles employed systematic
source-Lab/Training-Sample-Selection. sampling methods by formulating specific rules to mitigate this imbal-
ance caused by random sampling (Chen et al., 2020). A very small
3.2.3.3. Transferring methods. Based on the optimal training size and proportion of studies (5.2 %) adopted a balanced sampling approach
distribution strategy, we created the sample set for each site. To evaluate (Descals et al., 2021; Liu et al., 2023; He et al., 2024; Zhao et al., 2024).
data and model transfer performance, we designated and rotated one of For example, Zhao et al. (2024)used stratified sampling, categorizing
the five study sites as the local sample pool, with all samples from the samples by time and changes in areas, selecting 300 training samples for
remaining four sites serving as the global pool. This allowed for sample each category to avoid imbalanced sampling. For transferring methods
transfer and model transfer to be applied and assessed five times, each (Fig. 6c), only 7.9 % of the articles adopted either model or sample
time using a different site as the testing region. For each site, we transfer to reduce sample annotation efforts, while 27.0 % of the articles
incrementally increased the training patch number from the local sam- chose the direct use of the model trained from somewhere else. This
ple pool from 0 to 3.0 %, generated a series of semantic segmentation highlighted that the transferring method was still an emerging topic that
models from applying different transferring methods for the mixture of required in-depth investigation. In general, model transfer was more
the subsets of the local pool and the global pool. We compared three commonly used (5.9 %) than sample transfer (2.0 %). Sample transfer
approaches: no transfer, sample transfer, and model transfer. No transfer was employed mainly for a large-scale mapping (e.g., Zhou and Weng,
refers to training a model from scratch at the target site without any 2024). Moreover, a variety of mapping themes were identified (Fig. 6d),
transfer strategy, using the previously described balanced sampling including “impervious surfaces” (26.7 %), “land cover” (25.1 %), and
method to select training samples. Sample transfer involves combining “agriculture” (10.0 %), which reflected a wide range of mapping themes
local and global samples to form a new training set for training a deep in our survey to identify current states of strategic sampling.
learning model. Model transfer, by contrast, follows a transfer learning Lastly, among the articles reporting training patch proportion, bi-
paradigm, where a pre-trained model is adapted to the target domain. nary classification tasks were slightly more common than multi-class
This approach entails training a pre-trained model using global samples, classification tasks (Fig. 6e). The binary classification tasks in remote
after which the encoder parameters are frozen and only the decoder sensing semantic segmentation included the extraction of ground objects
parameters are fine-tuned using local samples from the specific site to be such as buildings (Zhou and Weng, 2024), cropland parcels (Waldner
tested. Specifically, the pre-trained model was first trained using global and Diakogiannis, 2020), and water bodies (Hertel et al., 2023), while
samples for 1000 rounds, and then fine-tuned on local samples for 100 multi-class classification tasks mainly focused on the land cover classi-
rounds. During fine-tuning, the encoder parameters were kept frozen, fication (Xiong et al., 2024) and crop type classification (Cai et al.,
and the decoder parameters were updated using a learning rate of 10 (cid:0) 5. 2024). Surprisingly, we found no obvious correlations between the
We applied the same GTC curve as the evaluation tool for the compar- training patch proportion and the category number to be classified
ative performance of the two transferring methods based upon an out-of- (Fig. 6f). The median training patch proportion in binary classification
bag testing sample set. The better transferring method should require studies was even higher than that in multi-classification studies, indi-
fewer local samples to reach its GTC level-off point. cating that the increase of category number did not necessarily lead to
the increase of training samples.
8

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 6. Results of the meta-analysis after extracting information from the selected papers. (a) Distribution and statistical analysis of training patch proportion, (b)
sample distribution, (c) transferring method, (d) mapping theme, (e) class types, and (f) training patch proportions across different categories.
4.2. Case study results sampling. The XJ study area required the fewest training samples due to
its relatively simple parcel morphology, characterized by large, regu-
4.2.1. Training size and sample distribution larly shaped cropland parcels. Overall, the results suggested that the
Fig. 7presents the GTC curves with increasing training size using the proposed balanced sampling method generally required fewer sample
newly proposed balanced and random sampling methods for five case patches to train a satisfactory model compared to random sampling.
studies of cropland parcel mapping. As the number of training sample Table 3summarizes the minimum training patch proportion for the
patches increased, the GTC value gradually decreased until they levelled level-off point and its corresponding GTC value, highlighting the supe-
off, with the dashed line indicating where the level-off point, i.e., 1(cid:0) riority of the proposed balanced sampling method. The optimal training
0.95×(1(cid:0) GTCmin ), was first reached. For most study sites, the GTC for patch proportion for random sampling (3.3 %) was lower than the
balanced sampling (blue curve) reached the level-off point earlier than average training size summarized from the meta-analysis (4.2 %, see
for random sampling (orange curve), as indicated by the blue dashed Fig. 6a). Compared to the random sampling method, the proposed
line on the x-axis being to the left of the orange dashed line. The distance balanced sampling strategy reduced the required training patch pro-
between the two dashed lines on the x-axis reflected the difference in the portion from 3.3 % to 2.5 %, resulting in a reduction of approximately
minimum required training patch proportion between the two sampling 25 % in sample annotation workload. Despite fewer samples used for
schemes. In the XJ and GX study areas, the differences in required model training, the balanced sampling achieved the level-off GTC
sample size between the two sampling methods were relatively small. almost identical to random sampling on average (0.257 vs. 0.267).
This was attributed to the geographically consistent morphological Fig. 8 confirms our findings from the predicted parcel maps using
patterns of cropland parcels in the remote sensing images, which two sampling strategies with their optimal sample sizes. The random
resulted in a limited level of sample imbalance even under random sampling method used 3.3 % of the total patches for training, while the
9

R. Lu et al.                                                                                                                                                                                            R  e m   o  t e   S  e n  s i n  g    o f   E  n  v  i r o  n m   e  n t 331 (2025) 115034
Fig. 7. Impacts of training sample size and distribution on model accuracy across five study areas. The blue line represents the proposed balanced sampling and the
orange line represents the random sampling. The dashed line at the y-axis indicates the first point when GTC levels off. The dashed line at the x-axis represents the
proportion of total patches as training sizes for the level-off point. The closer to the origin means the less samples needed to reach the level-off point. XJ: Xinjiang; JL:
Jilin; GX: Guangxi; HB: Hubei; ZJ: Zhejiang. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of
this article.)
Table 3
The minimum training patch proportion when GTC reaches the level-off point and its corresponding GTC value for the five study sites. XJ: Xinjiang; JL: Jilin; GX:
Guangxi; HB: Hubei; ZJ: Zhejiang.
| Sample distribution | XJ JL | GX HB | ZJ Average |
| ------------------- | ----- | ----- | ---------- |
Minimum training patch proportion (%) for the level-off GTC Random sampling 0.9 3.3. 3.7 4.7 4.0 3.3
| Balanced sampling | 0.8 2.5 | 3.5 2.9 | 2.6 2.5 |
| ----------------- | ------- | ------- | ------- |
Level-off GTC Random sampling 0.150 0.280 0.345 0.312 0.250 0.267
| Balanced sampling | 0.148 0.274 | 0.335 0.307 | 0.222 0.257 |
| ----------------- | ----------- | ----------- | ----------- |
10

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 8. Cropland parcel extraction results using 3.3 % training samples selected by random sampling and 2.5 % by balanced sampling. XJ: Xinjiang; JL: Jilin; GX:
Guangxi; HB: Hubei; ZJ: Zhejiang.
balanced sampling method used only 2.5 %. Both methods achieved 4.2.3. Implications of training sample size for parcel products
comparable performance in delineating cropland parcels, as visually Fig. 10illustrates the cropland parcel extraction results based on full-
observed from predictions. Despite using approximately 25 percentage scene imagery from the JL and ZJ study sites. We conducted experiments
of fewer training samples, the balanced sampling strategy produced using the balanced sampling strategy under three training patch pro-
result maps that were nearly identical to those generated by the random portion scenarios: sparse (0.5 %), optimal (2.5 %), and excessive (10.0
sampling method. We chose the balanced sampling with its optimal %) of the total patches to be mapped. The model trained with 0.5 % of
training sample size (2.5 % of total patches in mapped areas) as the best the data exhibited noticeable omission errors and poor boundary
configuration for the next stage of the transferring test. extraction. In contrast, the outputs from the 2.5 % and 10.0 % training
sizes were visually similar, indicating that increasing the sample size
4.2.2. Transferring methods beyond the optimal level provided no substantial improvement. We
Fig. 9and Table 4compare the GTC error curves and level-off points further evaluated key parcel-level statistics for each scenario, i.e., the
for three strategies: sample transfer, model transfer, and training solely number of cropland parcels, average parcel area, and total cropland
with local samples (i.e., no transfer). When the number of local training area. The results for the 2.5 % and 10.0 % cases displayed highly
samples was limited, both transfer-based methods yielded lower GTC consistent patterns, reinforcing the conclusion that their mapping
errors than the no-transfer approach, benefiting from the inclusion of quality was comparable.
global samples. However, as the volume of local training data increased,
the performance of the no-transfer model gradually surpassed that of 4.2.4. Summary
both transfer strategies. This suggested that in data-rich scenarios, Fig. 11 summarizes the results where optimal components were
transfer methods might introduce conflicting information between systematically added for strategic sampling to analyze how their addi-
global and local samples, ultimately reducing segmentation accuracy. tion impacted the required sample sizes and GTC values. It started from a
The average local training patch proportion required to reach the random sampling of image patches which averagely required 3.3 % of
level-off point was 0.5 % for both sample and model transfer, only one- total patches in mapped areas as training sample size to reach the GTC
fifth of the requirement under the no transfer strategy, which reached level-off point. The preferred distribution strategy, the newly proposed
the level-off at 2.5 %. However, this efficiency came with a trade-off: balanced sampling, could reduce the number of samples required for
both transfer methods resulted in higher average level-off GTC values semantic segmentation model training from 3.3 % to 2.5 %, and also
(0.298 for sample transfer and 0.308 for model transfer) compared to no slightly reduced GTC errors (0.267 vs 0.258). Sample transfer would
transfer (0.257). This implied that while transfer strategies were ad- greatly reduce the local training sample demand, resulting in 0.5 % of
vantageous in low-data settings, they might slightly compromise accu- total patches in mapped areas as the final local sample size, although it
racy due to the inclusion of out-of-region global samples. caused the GTC to increase from 0.258 to 0.298. We recommend using
Between the two transfer approaches, sample transfer achieved balanced sampling generally. However, when the cost of sample anno-
slightly better model performance than model transfer (0.298 vs. 0.308), tation is prohibitively high, applying sample transfer could significantly
despite their same optimal sample sizes. This might be attributed to the reduce annotation workload, albeit with a slight decrease in accuracy.
fact that sample transfer trained the model from scratch, allowing better Besides, we applied the same analysis procedure based upon F1-score
integration of local and global data, whereas model transfer fine-tuned curve. The results were almost the same as using the GTC curve
only the decoder parameters of a pre-trained model, potentially (balanced vs. random sampling: 2.5 % vs. 3.5% % for minimum required
limiting its adaptability. training area; sample vs. model transfer: 0.6 % vs. 0.7 % for optimal
training patch proportion). For the details, please refer to Section S2 of
11

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 9. Impacts of local training size and transferring method on model accuracy for five study sites. The local training patch proportion represents the proportion of
patches selected for training from the site to be mapped over the total patches of the same site. The dashed line on the y-axis indicates the level-off point that first
reaches 95 % of the maximum accuracy. The dashed line on the x-axis represents the minimum number of local samples required for the model to reach the level-off
point. No transfer requires much higher sample size to reach its level-off point than sample and model transfer. XJ: Xinjiang; JL: Jilin; GX: Guangxi; HB: Hubei;
ZJ: Zhejiang.
Table 4
The minimum local training sample size and its level-off GTC value for different transferring methods. XJ: Xinjiang; JL: Jilin; GX: Guangxi; HB: Hubei; ZJ: Zhejiang.
Transfer strategy XJ JL GX HB ZJ Average
Minimum training patch proportion (%) for level-off GTC No transfer 0.8 2.5 3.5 2.9 2.6 2.5
Sample transfer 0.5 0.4 0.5 0.4 0.5 0.5
Model transfer 0.5 0.4 0.5 0.5 0.4 0.5
Level-off GTC No transfer 0.148 0.274 0.335 0.307 0.222 0.257
Sample transfer 0.192 0.311 0.370 0.347 0.268 0.298
Model transfer 0.202 0.317 0.384 0.355 0.282 0.308
the Supplementary Material. performance while still requiring resources for annotation and storage.
Admittedly, the “best” sample size is not a one-size-fits-all scenario. A
5. Discussion variety of factors, beyond the total patches to be mapped, influence the
optimal size of the training dataset, including geographic variability of
5.1. Training size the target, image resolution, and seasonal fluctuations. Our study pro-
vides an important heuristic to quickly determine the optimal sample
The meta-analysis of various semantic segmentation applications size that strikes the balance between sample size and model perfor-
and case studies on cropland parcel mapping consistently demonstrated mance, serving as a powerful tool for initiating operational mapping
that approximately 4 % of the total patches were the optimal training projects with minimal upfront data. It would allow for more informed
size when the most commonly used patch-based sampling scheme, decision-making, especially in time-sensitive or resource-constrained
random sampling, was applied. The training size directly impacts the projects where preliminary tests might not be feasible.
costs in terms of sample annotation, as larger datasets require more The meta-analysis revealed an unusual pattern in which most studies
labeled examples, often leading to higher manual effort or the need for utilized either less than 1 % or more than 20 % of available data as
automated labeling tools. Additionally, redundant sample prepara- training samples (Fig. 6a). This bimodal distribution may be explained
tion—where duplicate or overly similar data is included—can unnec- by two main factors. First, in many existing studies, the size of the
essarily inflate the budget, as it fails to provide aids in improving model training dataset is primarily constrained by data acquisition and
12

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 10. Effects of different training sample sizes on regional mapping. Taking (a) JL and (b) ZJ study sites as examples, cropland parcel extraction results based on
remote sensing imagery were presented using sparse (0.5 %), optimal (2.5 %), and excessive (10.0 %) training sample proportions. The number of cropland parcels,
average parcel area, and total cropland area within the image extent were summarized.
13

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Fig. 11. Comparison of the results for random sampling, balanced sampling, and sample transfer. (a) The local sample size required to reach GTC level-off point as
the proportion of the total patches to be mapped. (b) The level-off GTC values for the minimum local sample size.
annotation costs, rather than determined by the number of target clas- sampling specifically for image patches, which distributed the even
ses. Consequently, there is no consistent correlation between the num- sample number into several patch strata defined by object edges and
ber of training samples and the number of classification categories categorical proportion from a priori map. From five case studies (Fig. 7),
reported in the literature. Second, current semantic segmentation re- we observed that the new balanced-sampling approach generally
searches tend to follow two distinct directions: few-shot learning, which reached the accuracy level-off point earlier than random sampling, and
focuses on model performance with minimal labeled data, and large- reduced the sample size demand from 3.3 % to 2.5 % of the total mapped
scale training, which relies on extensive annotated datasets. This region. Also, the balanced sampling reached a slightly lower level-off
divergence has contributed to the clustering of studies at both extremes GTC error (0.257 vs. 0.267), as such diversity-based sampling captures
of the sample size spectrum. The emergence of this pattern underscores the variance in the data and prevents overfitting to a specific region of
the absence of standardized guidelines for determining training sample the feature space. It is simple to expand balanced sampling for multi-
sizes in remote sensing applications, highlighting the relevance and class scenarios in terms of various patch-based deep-learning applica-
necessity of our investigation. tions. Therefore, the new balanced sampling is recommended for future
In multi-class classification scenarios, it has been suggested that the practice of strategic sampling.
training sample size should increase proportionally with the number of The proposed balanced sampling method relies on existing land
categories to ensure adequate representation for each class (Foody et al., cover products to obtain categorical proportion priors. Our meta-
2006). However, our meta-analysis did not reveal clear evidence sup- analysis revealed that most mapping themes, such as impervious sur-
porting this assumption in the context of semantic segmentation. In faces, land cover, agriculture, forest, and water bodies, were well sup-
contrast, we observed that binary classification tasks tended to utilize a ported by existing remote sensing products. Cases where no prior
larger proportion of training samples than multi-class tasks (Fig. 6f). information is available are relatively rare. For specific applications
This trend likely reflects the fact that the most influential factor deter- lacking such products (e.g., disaster mapping or greenhouse extraction),
mining sample size is the available annotation resources, rather than the users can either rely on the single indicator of edge complexity or adopt
number of target categories. Given that binary classification tasks typi- a fallback strategy by randomly selecting approximately 4 % of the total
cally involve simpler and less time-consuming labeling processes, they samples. While this may increase data preparation costs or introduce
can accommodate more training samples within the same annotation some sampling bias, the negative impacts could be minimal, thereby
budget. A rigorous assessment of the relationship between the number of preserving the overall practicality of the method even in the absence of
categories and the required training sample size with an assumption on prior data. The accuracy of the existing products is another possible
unlimited annotation resources would be excessively complex and falls factor for compromising the effectiveness of the balanced sampling
beyond the scope of this study. Future research is needed to determine through affecting the estimate of categorial proportion for patch-based
whether optimal training sample sizes scale proportionally with the entropy. However, it is important to note that the entropy calculation
number of categories in semantic segmentation tasks. For example, if relies solely on the pixel quantity of each class, rather than the precise
2.5 % of the total image patches are sufficient for a balanced binary spatial distribution. Therefore, the use of an existing land cover product,
classification task, a seven-class task might require approximately 8.8 % even one with moderate spatial accuracy or a coarser resolution, re-
of the patches for training (2.5 % / 2 ×7 =8.8 %). This hypothesis, mains an effective strategy for guiding sample selection, provided that
however, remains to be empirically validated. the quantity errors are not excessively high.
5.2. Sample distribution 5.3. Transferring method
Random sampling is the dominant approach for generating training Transferring methods have demonstrated their superiority for
image patches for semantic segmentation in past studies. More than half reducing sample preparation, but only were used in 7.9 % of the past
of the studies used random sampling from our meta-analysis, owing to semantic segmentation studies from our meta-analysis. Our case studies
its simplicity and ease of implementation. However, random sampling showed that the model transfer and the sample transfer presented an
can lead to repetitive or highly similar patches, which do not add much equal performance for decreasing the demand of the local samples from
new information to the model and could cause certain classes to be 2.5 % to 0.5 %, only a quarter of the optimal sample number when no
underrepresented. We proposed the new diversity-based balanced transfer was applied. Sample transfer exhibited a slightly lower GTC
14

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
error (0.298 vs 0.308), benefiting from its process of rebuilding the specific segmentation objectives, landscape characteristics, and data
model from scratch with more flexibility in tuning the weights of all sources. A more rigorous way would be to visualize the learning curve
hidden layers, making it the preferred approach for this study. Sample where increasing the dataset size yields diminishing improvements in
transfer is ideal when a large amount of labeled data is available in the model performance and then to pinpoint the optimal dataset size that
source domain, but needs to be transferred to a target domain where just makes the performance plateau. Nevertheless, to find this optimal
data is sparse—a common scenario in remote sensing applications. size, it would require the professionals to annotate the unnecessary
However, if the source and target domains are too dissimilar in terms of sample patches to evaluate the sample size much larger than the level-off
data distributions, feature types, or underlying structures, the trans- point. Our recommendations, i.e., balanced sampling using 2.5 % of the
ferred samples may not be as effective, potentially resulting in poor total mapping region or sample/model transfer using 0.5 %, offer an
generalization. On the other hand, model transfer leverages the gener- important baseline for users to test the optimal sample size for their own
alization capabilities of a model that has already learned to detect basic applications. These findings are especially valuable for time-sensitive or
features from a large dataset, considerably reducing training time and resource-constrained projects, where conducting a full parameter
computational resources. However, its performance heavily depends on sensitivity analysis may not be feasible.
the quality of the pre-trained model. If a pre-trained model has been
built with a large, representative dataset and computational resources 6. Conclusion
are limited, model transfer is recommended because it significantly re-
duces computation costs. In other situations, particularly when global This study combined meta-analysis on 334 papers from various
samples from similar domains are available, sample transfer is preferred remote sensing applications and case studies of cropland parcel extrac-
due to the higher accuracy achieved by developing a deep learning tion to explore the best practices for strategic sampling for semantic
model from the scratch. segmentation, mainly focusing on three key factors: training size, sam-
ple distribution and transferring methods. The meta-analysis and case
5.4. Generalizability studies both identified ~4 % of the total mapping patches is the optimal
training size. The patch-based balanced sampling newly proposed in this
We used cropland parcel extraction as a case study to investigate study, which takes account of category entropy and edge complexity,
strategic sampling approaches for remote sensing semantic segmenta- could further decrease the sample demand to 2.5 %, compared to
tion tasks. As a representative semantic segmentation challenge, crop- random sampling which was adopted in over half of the papers in our
land parcel extraction involves substantial variation in parcel size, survey. While transferring methods were only used in 7.9 % of the pa-
shape, and spectral characteristics across regions, making it broadly pers, our case studies showed that sample and model transfer could
reflective of the complexities faced in many segmentation applications. considerably reduce the required local sample size from 2.5 % (i.e., the
The five study areas selected for this analysis are distributed across sample demand for balanced sampling) to 0.5 % of the total mapping
diverse geographic regions of China, each exhibiting distinct landscapes patches, with sample transfer being slightly more accurate than model
and agricultural systems. For example, the XJ region is characterized by transfer (GTC errors: 0.298 vs 0.308). This finding suggests transferring
mechanized agriculture, resulting in large, regularly shaped parcels, methods have great potential for decreasing the amount of new training
whereas the GX region, located in the hilly terrain of southwestern dataset, despite the decreased model performance. By leveraging both
China, is dominated by smallholder farming, producing fragmented and the meta-analysis and the representative case study of cropland parcel
irregular parcels (Fig. 2). Our experiments demonstrated that the pro- extraction, our strategic sampling recommendations have the potential
posed balanced sampling approach consistently reduced annotation to be generalized to other remote sensing mapping tasks. Targeted on an
effort compared to conventional random sampling across all five re- operational mapping project based upon semantic segmentation, this
gions, highlighting its broad applicability. study will provide important guidance to minimize the cost of training
To ensure comparability across different spatial resolutions, training data collection while maintaining or even improving model’s accuracy.
sample size was measured as the proportion of training patches rather
than absolute pixel counts. Also, the strategy was specifically designed CRediT authorship contribution statement
for regional mapping tasks, where geographic and cropland character-
istics tended to be relatively homogeneous, minimizing generalization Rui Lu: Writing – review & editing, Writing – original draft, Visu-
issues. For large-scale mapping efforts, we recommend first performing alization, Software, Methodology, Data curation, Conceptualization.
geographic stratification and then applying the strategic sampling Ronghua Liao: Validation, Methodology, Investigation. Ran Meng:
method within each sub-region to construct effective training datasets. Writing – review & editing, Validation, Supervision. Yingchu Hu:
It is important to note that evaluating strategic sampling across all Methodology, Investigation. Yi Zhao: Methodology, Investigation. Yan
possible segmentation tasks within a single study is nearly impossible. Guo: Validation, Conceptualization. Yingfan Zhang: Writing – review
To address this limitation, we conducted a meta-analysis encompassing & editing, Visualization. Zhou Shi: Supervision, Funding acquisition,
a broader range of remote sensing applications. This meta-analysis Conceptualization. Su Ye: Writing – review & editing, Visualization,
reviewed sample selection practices across various classification tasks, Supervision, Project administration, Funding acquisition, Data curation,
including impervious surface mapping, land cover classification, and Conceptualization.
agricultural monitoring. Over half of the studies employed random
sampling, with a median training sample proportion of approximately 4 Declaration of competing interest
% (Fig. 6). In our case study, the optimal training sample proportion
under random sampling was 3.3 %, which was slightly lower but closely The authors declare that they have no known competing financial
aligned with the meta-analysis result. This strong consistency between interests or personal relationships that could have appeared to influence
the meta-analysis and our case study suggested that the conclusions the work reported in this paper.
drawn from our study could be generalizable to other semantic seg-
mentation tasks. While the meta-analysis offered limited insight into the Acknowledgement
comparative performance of different sampling strategies and transfer
learning methods, our local experiments addressed these two critical The authors are very grateful for the financial support provided by
issues using one of the most representative segmentation tasks, i.e., National Key Research and Development Program of China
cropland parcel extraction. (2023YFD1900100), National Natural Science Foundation of China
Admittedly, the optimal sample size may vary depending on the (U24A20575), and National Key Research and Development Program of
15

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
China (2022YFB3903503). The authors would also like to thank the Du, S., Zhang, F., Zhang, X., 2015. Semantic classification of urban buildings combining
editors and anonymous reviewers of the journal for their thorough re- VHR image and GIS data: an improved random forest approach. ISPRS J.
Photogramm. Remote Sens. 105, 107–119. https://doi.org/10.1016/j.
view and insightful comments that have helped improving the quality of isprsjprs.2015.03.011.
the paper. Estes, L.D., Ye, S., Song, L., Luo, B., Eastman, J.R., Meng, Z., Zhang, Q., McRitchie, D.,
Debats, S.R., Muhando, J., Amukoa, A.H., Kaloo, B.W., Makuru, J., Mbatia, B.K.,
Muasa, I.M., Mucha, J., Mugami, A.M., Mugami, J.M., Muinde, F.W., Mwawaza, F.
Appendix A. Supplementary data
M., Ochieng, J., Oduol, C.J., Oduor, P., Wanjiku, T., Wanyoike, J.G., Avery, R.B.,
Caylor, K.K., 2022. High resolution, annual maps of field boundaries for smallholder-
Supplementary data to this article can be found online at https://doi. dominated croplands at National Scales. Front. Artif. Intell. 4.
Foody, G.M., Mathur, A., 2006. The use of small training sets containing mixed pixels for
org/10.1016/j.rse.2025.115034.
accurate hard image classification: training on mixed spectral responses for
classification by a SVM. Remote Sens. Environ. 103, 179–189. https://doi.org/
Data availability 10.1016/j.rse.2006.04.001.
Foody, G.M., Mathur, A., Sanchez-Hernandez, C., Boyd, D.S., 2006. Training set size
requirements for the classification of a specific class. Remote Sens. Environ. 104,
I have shared the link to my data and code in the manuscript. 1–14. https://doi.org/10.1016/j.rse.2006.03.004.
Garrigues, S., Allard, D., Baret, F., Morisette, J., 2008. Multivariate quantification of
landscape spatial heterogeneity using variogram models. Remote Sens. Environ. 112,
References
216–230. https://doi.org/10.1016/j.rse.2007.04.017.
Grift, J., Persello, C., Koeva, M., 2024. CadastreVision: a benchmark dataset for cadastral
Bergen, K.J., Johnson, P.A., de Hoop, M.V., Beroza, G.C., 2019. Machine learning for boundary delineation from multi-resolution earth observation images. ISPRS J.
data-driven discovery in solid earth geoscience. Science 363, eaau0323. https://doi. Photogramm. Remote Sens. 217, 91–100. https://doi.org/10.1016/j.
org/10.1126/science.aau0323. isprsjprs.2024.08.005.
Boschetti, L., Stehman, S.V., Roy, D.P., 2016. A stratified random sampling design in He, H., Yan, J., Liang, D., Sun, Z., Li, J., Wang, L., 2024. Time-series land cover change
space and time for regional to global scale burned area product validation. Remote detection using deep learning-based temporal semantic segmentation. Remote Sens.
Sens. Environ. 186, 465–478. https://doi.org/10.1016/j.rse.2016.09.016. Environ. 305, 114101. https://doi.org/10.1016/j.rse.2024.114101.
Brown, A., 2006. Strategic sampling. In: Hurford, C., Schneider, M. (Eds.), Monitoring Hertel, V., Chow, C., Wani, O., Wieland, M., Martinis, S., 2023. Probabilistic SAR-based
Nature Conservation in Cultural Habitats: A Practical Guide and Case Studies. water segmentation with adapted Bayesian convolutional neural network. Remote
Springer, Netherlands, Dordrecht, pp. 43–54. https://doi.org/10.1007/1-4020- Sens. Environ. 285, 113388. https://doi.org/10.1016/j.rse.2022.113388.
3757-0_5. Heydari, S.S., Mountrakis, G., 2018. Effect of classifier selection, reference sample size,
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E., reference class distribution and scene heterogeneity in per-pixel classification
Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z., Pengra, B.W., Smith, K., accuracy using 26 Landsat sites. Remote Sens. Environ. 204, 648–658. https://doi.
Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D., org/10.1016/j.rse.2017.09.035.
Reker, R.R., Rover, J., 2020. Lessons learned implementing an operational Jin, H., Stehman, S.V., Mountrakis, G., 2014. Assessing the impact of training sample
continuous United States national land change monitoring capability: the land selection on accuracy of an urban classification: a case study in Denver, Colorado.
change monitoring, assessment, and projection (LCMAP) approach. Remote Sens. Int. J. Remote Sens. 35, 2067–2081. https://doi.org/10.1080/
Environ. Time Ser. Anal. High Spat. Resol. Imag. 238, 111356. https://doi.org/ 01431161.2014.885152.
10.1016/j.rse.2019.111356. Jong, M., Guan, K., Wang, S., Huang, Y., Peng, B., 2022. Improving field boundary
Cai, Z., Hu, Q., Zhang, X., Yang, J., Wei, H., Wang, J., Zeng, Y., Yin, G., Li, W., You, L., delineation in ResUNets via adversarial deep learning. Int. J. Appl. Earth Obs.
Xu, B., Shi, Z., 2023. Improving agricultural field parcel delineation with a dual Geoinf. 112, 102877. https://doi.org/10.1016/j.jag.2022.102877.
branch spatiotemporal fusion network by integrating multimodal satellite data. Kattenborn, T., Leitloff, J., Schiefer, F., Hinz, S., 2021. Review on convolutional neural
ISPRS J. Photogramm. Remote Sens. 205, 34–49. https://doi.org/10.1016/j. networks (CNN) in vegetation remote sensing. ISPRS J. Photogramm. Remote Sens.
isprsjprs.2023.09.021. 173, 24–49. https://doi.org/10.1016/j.isprsjprs.2020.12.010.
Cai, Z., Xu, B., Yu, Q., Zhang, X., Yang, J., Wei, H., Li, S., Song, Q., Xiong, H., Wu, H., Kim, J., Kim, D., Jun, H.-J., Heo, J.-P., 2024. The detection of residential developments
Wu, W., Shi, Z., Hu, Q., 2024. A cost-effective and robust mapping method for in urban areas: exploring the potentials of deep-learning algorithms. Comput.
diverse crop types using weakly supervised semantic segmentation with sparse point Environ. Urban. Syst. 107, 102053. https://doi.org/10.1016/j.
samples. ISPRS J. Photogramm. Remote Sens. 218, 260–276. https://doi.org/ compenvurbsys.2023.102053.
10.1016/j.isprsjprs.2024.09.017. Li, W., Dong, R., Fu, H., Wang, J., Yu, L., Gong, P., 2020. Integrating Google earth
Chen, Q., Gong, P., 2004. Automatic variogram parameter extraction for textural imagery with Landsat data to improve 30-m resolution land cover mapping. Remote
classification of the panchromatic IKONOS imagery. IEEE Trans. Geosci. Remote Sens. Environ. 237, 111563. https://doi.org/10.1016/j.rse.2019.111563.
Sens. 42, 1106–1115. https://doi.org/10.1109/TGRS.2004.825591. Li, M., Long, J., Stein, A., Wang, X., 2023. Using a semantic edge-aware multi-task neural
Chen, T.-H.K., Qiu, C., Schmitt, M., Zhu, X.X., Sabel, C.E., Prishchepov, A.V., 2020. network to delineate agricultural parcels from remote sensing images. ISPRS J.
Mapping horizontal and vertical urban densification in Denmark with Landsat time- Photogramm. Remote Sens. 200, 24–40. https://doi.org/10.1016/j.
series from 1985 to 2018: a semantic segmentation solution. Remote Sens. Environ. isprsjprs.2023.04.019.
251, 112096. https://doi.org/10.1016/j.rse.2020.112096. Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dolla´r, P.,
Chen, L., Letu, H., Fan, M., Shang, H., Tao, J., Wu, L., Zhang, Y., Yu, C., Gu, J., Zhang, N., Zitnick, C.L., 2014. Microsoft COCO: Common objects in context. In: Fleet, D.,
Hong, J., Wang, Z., Zhang, T., 2022. An introduction to the Chinese high-resolution Pajdla, T., Schiele, B., Tuytelaars, T. (Eds.), Computer Vision – ECCV 2014. Springer
earth observation system: Gaofen-1~7 civilian satellites. J. Remote Sens. 2022. International Publishing, Cham, pp. 740–755. https://doi.org/10.1007/978-3-319-
https://doi.org/10.34133/2022/9769536. 10602-1_48.
Chen, T.-H.K., Kincey, M.E., Rosser, N.J., Seto, K.C., 2024. Identifying recurrent and Liu, S., Chen, L., Zhang, L., Hu, J., Fu, Y., 2023. A large-scale climate-aware satellite
persistent landslides using satellite imagery and deep learning: a 30-year analysis of image dataset for domain adaptive land-cover semantic segmentation. ISPRS J.
the Himalaya. Sci. Total Environ. 922, 171161. https://doi.org/10.1016/j. Photogramm. Remote Sens. 205, 98–114. https://doi.org/10.1016/j.
scitotenv.2024.171161. isprsjprs.2023.09.007.
Cheng, T., Ji, X., Yang, G., Zheng, H., Ma, J., Yao, X., Zhu, Y., Cao, W., 2020. DESTIN: a Loshchilov, I., Hutter, F., 2019. Decoupled Weight Decay Regularization. https://doi.
new method for delineating the boundaries of crop fields by fusing spatial and org/10.48550/arXiv.1711.05101.
temporal information from WorldView and planet satellite imagery. Comput. Lu, R., Zhang, Y., Huang, Q., Zeng, P., Shi, Z., Ye, S., 2024. A refined edge-aware
Electron. Agric. 178, 105787. https://doi.org/10.1016/j.compag.2020.105787. convolutional neural networks for agricultural parcel delineation. Int. J. Appl. Earth
Colditz, R.R., 2015. An evaluation of different training sample allocation schemes for Obs. Geoinf. 133, 104084. https://doi.org/10.1016/j.jag.2024.104084.
discrete and continuous land cover classification using decision tree-based Ma, L., Liu, Y., Zhang, X., Ye, Y., Yin, G., Johnson, B.A., 2019. Deep learning in remote
algorithms. Remote Sens 7, 9655–9681. https://doi.org/10.3390/rs70809655. sensing applications: a meta-analysis and review. ISPRS J. Photogramm. Remote
Collins, L., McCarthy, G., Mellor, A., Newell, G., Smith, L., 2020. Training data Sens. 152, 166–177. https://doi.org/10.1016/j.isprsjprs.2019.04.015.
requirements for fire severity mapping using Landsat imagery and random forest. Ma, Y., Chen, S., Ermon, S., Lobell, D.B., 2024. Transfer learning in environmental
Remote Sens. Environ. 245, 111839. https://doi.org/10.1016/j.rse.2020.111839. remote sensing. Remote Sens. Environ. 301, 113924. https://doi.org/10.1016/j.
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., Fei-Fei, L., 2009. ImageNet: a large-scale rse.2023.113924.
hierarchical image database. In: Presented at the 2009 IEEE Conference on Computer Masoud, K.M., Persello, C., Tolpekin, V.A., 2020. Delineation of agricultural field
Vision and Pattern Recognition, pp. 248–255. https://doi.org/10.1109/ boundaries from Sentinel-2 images using a novel super-resolution contour detector
CVPR.2009.5206848. based on fully convolutional networks. Remote Sens 12, 59. https://doi.org/
Descals, A., Wich, S., Meijaard, E., Gaveau, D.L.A., Peedell, S., Szantoi, Z., 2021. High- 10.3390/rs12010059.
resolution global map of smallholder and industrial closed-canopy oil palm Mellor, A., Boukir, S., Haywood, A., Jones, S., 2015. Exploring issues of training data
plantations. Earth Syst. Sci. Data 13, 1211–1231. https://doi.org/10.5194/essd-13- imbalance and mislabelling on random forest performance for large area land cover
1211-2021. classification using the ensemble margin. ISPRS J. Photogramm. Remote Sens. 105,
Diakogiannis, F.I., Waldner, F., Caccetta, P., Wu, C., 2020. ResUNet-a: a deep learning 155–168. https://doi.org/10.1016/j.isprsjprs.2015.03.014.
framework for semantic segmentation of remotely sensed data. ISPRS J. Nguyen, L.H., Joshi, D.R., Clay, D.E., Henebry, G.M., 2020. Characterizing land cover/
Photogramm. Remote Sens. 162, 94–114. https://doi.org/10.1016/j. land use from multiple years of Landsat and MODIS time series: a novel approach
isprsjprs.2020.01.013. using land surface phenology modeling and random forest classifier. Remote Sens.
16

R. Lu et al. R e m o t e S e n s i n g o f E n v i r o n m e n t 331 (2025) 115034
Environ. Time Ser. Anal. High Spat. Resol. Imag. 238, 111017. https://doi.org/ Van Niel, T.G., McVicar, T.R., Datt, B., 2005. On the relationship between training
10.1016/j.rse.2018.12.016. sample size and data dimensionality: Monte Carlo analysis of broadband multi-
Olofsson, P., Foody, G.M., Herold, M., Stehman, S.V., Woodcock, C.E., Wulder, M.A., temporal classification. Remote Sens. Environ. 98, 468–480. https://doi.org/
2014. Good practices for estimating area and assessing accuracy of land change. 10.1016/j.rse.2005.08.011.
Remote Sens. Environ. 148, 42–57. https://doi.org/10.1016/j.rse.2014.02.015. Waldner, F., Diakogiannis, F.I., 2020. Deep learning on edge: extracting field boundaries
Pan, S.J., Yang, Q., 2010. A survey on transfer learning. IEEE Trans. Knowl. Data Eng. 22, from satellite images with a convolutional neural network. Remote Sens. Environ.
1345–1359. https://doi.org/10.1109/TKDE.2009.191. 245, 111741. https://doi.org/10.1016/j.rse.2020.111741.
Pan, Y., Wang, X., Zhang, L., Zhong, Y., 2023. E2EVAP: end-to-end vectorization of Wieland, M., Martinis, S., Kiefl, R., Gstaiger, V., 2023. Semantic segmentation of water
smallholder agricultural parcel boundaries from high-resolution remote sensing bodies in very high-resolution satellite and aerial images. Remote Sens. Environ.
imagery. ISPRS J. Photogramm. Remote Sens. 203, 246–264. https://doi.org/ 287, 113452. https://doi.org/10.1016/j.rse.2023.113452.
10.1016/j.isprsjprs.2023.08.001. Xiong, S., Zhang, X., Lei, Y., Tan, G., Wang, H., Du, S., 2024. Time-series China urban
Pastorino, M., Moser, G., Serpico, S.B., Zerubia, J., 2022. Semantic segmentation of land use mapping (2016–2022): an approach for achieving spatial-consistency and
remote-sensing images through fully convolutional neural networks and hierarchical semantic-transition rationality in temporal domain. Remote Sens. Environ. 312,
probabilistic graphical models. IEEE Trans. Geosci. Remote Sens. 60, 1–16. https:// 114344. https://doi.org/10.1016/j.rse.2024.114344.
doi.org/10.1109/TGRS.2022.3141996. Yang, J., Huang, X., 2021. The 30 m annual land cover dataset and its dynamics in China
Persello, C., Tolpekin, V.A., Bergado, J.R., de By, R.A., 2019. Delineation of agricultural from 1990 to 2019. Earth Syst. Sci. Data 13, 3907–3925. https://doi.org/10.5194/
fields in smallholder farms from satellite images using fully convolutional networks essd-13-3907-2021.
and combinatorial grouping. Remote Sens. Environ. 231, 111253. https://doi.org/ Yu, H., Yang, Z., Tan, L., Wang, Y., Sun, W., Sun, M., Tang, Y., 2018. Methods and
10.1016/j.rse.2019.111253. datasets on semantic segmentation: a review. Neurocomputing 304, 82–103. https://
Persello, C., Wegner, J.D., Ha¨nsch, R., Tuia, D., Ghamisi, P., Koeva, M., Camps-Valls, G., doi.org/10.1016/j.neucom.2018.03.037.
2022. Deep learning and earth observation to support the sustainable development Yuan, Q., Shen, H., Li, T., Li, Z., Li, S., Jiang, Y., Xu, H., Tan, W., Yang, Q., Wang, J.,
goals: current approaches, open challenges, and future opportunities. IEEE Geosci. Gao, J., Zhang, L., 2020. Deep learning in environmental remote sensing:
Remote Sens. Mag. 10, 172–200. https://doi.org/10.1109/MGRS.2021.3136100. achievements and challenges. Remote Sens. Environ. 241, 111716. https://doi.org/
Piper, J., 1992. Variability and bias in experimentally measured classifier error rates. 10.1016/j.rse.2020.111716.
Pattern Recogn. Lett. 13, 685–692. https://doi.org/10.1016/0167-8655(92)90097- Yuan, X., Shi, J., Gu, L., 2021. A review of deep learning methods for semantic
J. segmentation of remote sensing imagery. Expert Syst. Appl. 169, 114417. https://
Qurratulain, S., Zheng, Z., Xia, J., Ma, Y., Zhou, F., 2023. Deep learning instance doi.org/10.1016/j.eswa.2020.114417.
segmentation framework for burnt area instances characterization. Int. J. Appl. Earth Zhang, C., Sargent, I., Pan, X., Li, H., Gardiner, A., Hare, J., Atkinson, P.M., 2019. Joint
Obs. Geoinf. 116, 103146. https://doi.org/10.1016/j.jag.2022.103146. deep learning for land cover and land use classification. Remote Sens. Environ. 221,
Rajput, D., Wang, W.-J., Chen, C.-C., 2023. Evaluation of a decided sample size in 173–187. https://doi.org/10.1016/j.rse.2018.11.014.
machine learning applications. BMC Bioinformatics 24, 48. https://doi.org/ Zhang, Q., Zhang, Z., Xu, N., Li, Y., 2023. Fully automatic training sample collection for
10.1186/s12859-023-05156-9. detecting multi-decadal inland/seaward urban sprawl. Remote Sens. Environ. 298,
Ramezan, C.A., Warner, T.A., Maxwell, A.E., Price, B.S., 2021. Effects of training set size 113801. https://doi.org/10.1016/j.rse.2023.113801.
on supervised machine-learning land-cover classification of large-area high- Zhang, X., Zhao, T., Xu, H., Liu, W., Wang, J., Chen, X., Liu, L., 2024. GLC_FCS30D: the
resolution remotely sensed data. Remote Sens 13, 368. https://doi.org/10.3390/ first global 30&thinsp;m land-cover dynamics monitoring product with a fine
rs13030368. classification system for the period from 1985 to 2022 generated using dense-time-
Reichstein, M., Camps-Valls, G., Stevens, B., Jung, M., Denzler, J., Carvalhais, N., series Landsat imagery and the continuous change-detection method. Earth Syst. Sci.
Prabhat, 2019. Deep learning and process understanding for data-driven earth Data 16, 1353–1381. https://doi.org/10.5194/essd-16-1353-2024.
system science. Nature 566, 195–204. https://doi.org/10.1038/s41586-019-0912-1. Zhao, W., 2017. Research on the deep learning of the small sample data based on transfer
Ronneberger, O., Fischer, P., Brox, T., 2015. U-net: Convolutional networks for learning. AIP Conf. Proc. 1864, 020018. https://doi.org/10.1063/1.4992835.
biomedical image segmentation. In: Navab, N., Hornegger, J., Wells, W.M., Zhao, W., Lyu, R., Zhang, Jinming, Pang, J., Zhang, Jianming, 2024. A fast hybrid
Frangi, A.F. (Eds.), Medical Image Computing and Computer-Assisted Intervention – approach for continuous land cover change monitoring and semantic segmentation
MICCAI 2015. Lecture Notes in Computer Science. Springer International Publishing, using satellite time series. Int. J. Appl. Earth Obs. Geoinf. 134, 104222. https://doi.
Cham, pp. 234–241. https://doi.org/10.1007/978-3-319-24574-4_28. org/10.1016/j.jag.2024.104222.
Stehman, S.V., Wickham, J.D., 2011. Pixels, blocks of pixels, and polygons: choosing a Zhao, H., Wu, B., Zhang, M., Long, J., Tian, F., Xie, Y., Zeng, H., Zheng, Z., Ma, Z.,
spatial unit for thematic accuracy assessment. Remote Sens. Environ. 115, Wang, M., Li, J., 2025. A large-scale VHR parcel dataset and a novel hierarchical
3044–3055. https://doi.org/10.1016/j.rse.2011.06.007. semantic boundary-guided network for agricultural parcel delineation. ISPRS J.
Stehman, S.V., Mousoupetros, J., McRoberts, R.E., Næsset, E., Pengra, B.W., Xing, D., Photogramm. Remote Sens. 221, 1–19. https://doi.org/10.1016/j.
Horton, J.A., 2022. Incorporating interpreter variability into estimation of the total isprsjprs.2025.01.034.
variance of land cover area estimates under simple random sampling. Remote Sens. Zhou, Y., Weng, Q., 2024. Building up a data engine for global urban mapping. Remote
Environ. 269, 112806. https://doi.org/10.1016/j.rse.2021.112806. Sens. Environ. 311, 114242. https://doi.org/10.1016/j.rse.2024.114242.
Tong, X.-Y., Xia, G.-S., Lu, Q., Shen, H., Li, S., You, S., Zhang, L., 2020. Land-cover Zhou, Q., Tollerud, H., Barber, C., Smith, K., Zelenak, D., 2020. Training data selection
classification with high-resolution remote sensing images using transferable deep for annual land cover classification for the land change monitoring, assessment, and
models. Remote Sens. Environ. 237, 111322. https://doi.org/10.1016/j. projection (LCMAP) initiative. Remote Sens 12, 699. https://doi.org/10.3390/
rse.2019.111322. rs12040699.
Turker, M., Kok, E.H., 2013. Field-based sub-boundary extraction from remote sensing Zhu, Z., Gallant, A.L., Woodcock, C.E., Pengra, B., Olofsson, P., Loveland, T.R., Jin, S.,
imagery using perceptual grouping. ISPRS J. Photogramm. Remote Sens. 79, Dahal, D., Yang, L., Auch, R.F., 2016. Optimizing selection of training and auxiliary
106–121. https://doi.org/10.1016/j.isprsjprs.2013.02.009. data for operational land cover classification for the LCMAP initiative. ISPRS J.
Turkoglu, M.O., D’Aronco, S., Perich, G., Liebisch, F., Streit, C., Schindler, K., Wegner, J. Photogramm. Remote Sens. 122, 206–221. https://doi.org/10.1016/j.
D., 2021. Crop mapping from image time series: deep learning with multi-scale label isprsjprs.2016.11.004.
hierarchies. Remote Sens. Environ. 264, 112603. https://doi.org/10.1016/j. Zhu, W., Braun, B., Chiang, L.H., Romagnoli, J.A., 2021. Investigation of transfer
rse.2021.112603. learning for image classification and impact on training sample size. Chemom. Intell.
Lab. Syst. 211, 104269. https://doi.org/10.1016/j.chemolab.2021.104269.
17