International Journal of Digital Earth
ISSN: 1753-8947 (Print) 1753-8955 (Online) Journal homepage: www.tandfonline.com/journals/tjde20
Self-supervised deep learning for detection
of forest disturbance types in a subtropical
ecosystem using transformer and Sentinel-1 and
Sentinel-2 time series data
Ming Zhang, Guiying Li, Dengsheng Lu, Cong Xu, Haotian Zhao & Dengqiu Li
To cite this article: Ming Zhang, Guiying Li, Dengsheng Lu, Cong Xu, Haotian Zhao & Dengqiu Li
(2025) Self-supervised deep learning for detection of forest disturbance types in a subtropical
ecosystem using transformer and Sentinel-1 and Sentinel-2 time series data, International
Journal of Digital Earth, 18:1, 2537325, DOI: 10.1080/17538947.2025.2537325
To link to this article: https://doi.org/10.1080/17538947.2025.2537325
© 2025 The Author(s). Published by Informa Published online: 22 Jul 2025.
UK Limited, trading as Taylor & Francis
Group
Submit your article to this journal Article views: 2049
View related articles View Crossmark data
Citing articles: 6 View citing articles
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tjde20

INTERNATIONAL JOURNAL OF DIGITAL EARTH
2025, VOL. 18, NO. 1, 2537325
https://doi.org/10.1080/17538947.2025.2537325
Self-supervised deep learning for detection of forest disturbance types in a
subtropical ecosystem using transformer and Sentinel-1 and Sentinel-2
time series data
Ming Zhanga,b, Guiying Lia,b, Dengsheng Lua,b, Cong Xuc, Haotian Zhaoc and Dengqiu Lia,b
aFujian Provincial Key Laboratory for Subtropical Resources and Environment, Fujian Normal University, Fuzhou, People’s Republic
of China; bInstitute of Geography, Fujian Normal University, Fuzhou, People’s Republic of China; cSchool of Forestry, University of
Canterbury, Christchurch, New Zealand
ABSTRACT ARTICLE HISTORY
Accurate and timely detection of forest disturbance types is crucial for evaluating Received 30 October 2024
ecosystem health and global climate stability. Time series remote-sensing data offers Accepted 7 July 2025
valuable spatiotemporal information. However, frequent cloud cover in subtropical
regions disrupts the temporal consistency of optical satellite data. In addition, the KEYWORDS
Forest disturbance types;
impact of different data sources on modeling accuracy and the challenge of acquiring
time series; Sentinel-1/2;
large and labeled datasets for deep learning are considerable obstacles. In this study,
self-supervised deep
a novel positional encoding module was designed to handle the irregular Sentinel-2 learning; Transformer
time series. The Transformer model based on this positional encoding module
effectively fused Sentinel-1 and Sentinel-2 data. Meanwhile, self-supervised learning was
used to address the issue of insufficient samples. The improved Transformer model was
successfully applied to detect clear-cutting and disease disturbances with a F1 score of
0.95. Our results highlighted that appropriate encoding techniques increased the
model’s performance by between 5% and 14%. This research also found that while
Sentinel-2 data alone yields good accuracy, combining Sentinel-1 and Sentinel-2 data
improved model accuracy. The self-supervised learning model achieved higher accuracy
(0.95) than the supervised model (0.86) on a limited data (20% of the training samples)
and exhibited stable accuracy across different training data proportions.
1. Introduction
Subtropical forest ecosystems play a vital role in climate regulation, ecological balance maintenance, and
sustainable economic development (Hethcoat et al. 2021). However, these forests face growing threats from
various disturbance factors, including logging, disease outbreaks, wildfires, and droughts (Bullock, Woodcock,
and Olofsson 2020; Ye et al. 2021). These disturbances significantly impact the forests’ ability to regulate climate
and conserve biodiversity (Caputo et al. 2016; Curran and Trigg 2006). Local economic development is also
affected (Knoke et al. 2023), with the timber industry experiencing substantial losses due to disease-induced
wood quality degradation (Bastit, Brunette, and Montagné-Huck 2023). While some logging practices can
provide economic benefits, illegal logging activities exacerbate forest degradation and can even trigger ecologi-
cal disasters (Tang et al. 2019). Therefore, accurately identifying the type and timing of forest disturbances is
crucial for ensuring forest health and promoting sustainable economic development.
Medium-resolution optical satellite imagery, such as Landsat (Shimizu et al. 2023) and Sentinel-2 (Slagter
et al. 2023), has been widely used for forest disturbance detection due to its convenient acquisition schedule
and extensive temporal archive. However, frequent cloud cover in subtropical regions poses a significant
challenge for developing robust forest disturbance detection algorithms (Verbesselt et al. 2010; M. Zhang
et al. 2024; B. Yang et al. 2022). Clouds introduce long temporal gaps in the time series data, resulting in
irregular time series patterns across years and locations (Slagter et al. 2023; Verhegghen, Eva, and Achard
2015). Conversely, Synthetic Aperture Radar (SAR) data offers all-weather capabilities, making it a valuable
CONTACT Dengqiu Li lidengqiu@fjnu.edu.cn Fujian Provincial Key Laboratory for Subtropical Resources and Environment, Fujian Normal
University, Fuzhou, People’s Republic of China; Institute of Geography, Fujian Normal University, Fuzhou, People’s Republic of China
© 2025 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits
unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this article has been published allow
the posting of the Accepted Manuscript in a repository by the author(s) or with their consent.

2 M. ZHANG ET AL.
alternative (R. Zhang et al. 2024). SAR is sensitive to vegetation canopy structure and growth conditions.
The data with different radar wavelengths and polarization modes can produce differentiated responses
for different disturbance types (Dalponte et al. 2023; Zhao et al. 2022). Sentinel-1 SAR data, in particular,
holds promise for detecting small-scale and short-term disturbances due to its high revisit frequency and
fine spatial resolution (Doblas et al. 2022; Sun et al. 2023; Watanabe et al. 2021; Zhao et al. 2022). However,
SAR images are inherently noisy, and their interpretability can be affected by factors like terrain and surface
moisture (Ballère et al. 2021). To overcome these limitations, leveraging the complementary strengths of
different remote sensing data sources through data fusion is a compelling approach. This has the potential
to improve the accuracy and timeliness of forest disturbance monitoring (Joshi et al. 2016). However, a dee-
per understanding of how different data sources influence detection performance for various disturbance
types remains an area of active research. Further investigation will be crucial for developing optimal
multi-source fusion methods for robust and comprehensive forest disturbance detection in challenging
environments like subtropical regions.
Two primary approaches exist for obtaining the type and spatiotemporal distribution of forest dis-
turbances: two-step attribution and one-step attribution. The two-step method first identifies the dis-
turbance location and boundaries before classifying the disturbance type (Stahl et al. 2023). While
algorithms like LandTrendr, Breaks for Additive Seasonal and Trend (BFAST), and Continuous Change
Detection and Classification (CCDC) can be employed for this initial detection (Mitchell, Rosenqvist,
and Mora 2017), most of these methods are adapted to a single data source and require high-quality
data (Cardille et al. 2022; Morrison et al. 2018). One-step disturbance attribution offers a streamlined
alternative to the two-step approach. It directly classifies forest disturbance types and their spatiotem-
poral distribution from time series data in a single step. Studies suggest that one-step methods achieve
comparable performance to two-step methods (Schroeder et al. 2017). Despite their advantages, one-
step attribution models can be more complex to develop and train compared to two-step methods as
mainstream one-step methods rely on handcrafted features, which can be time-consuming and poten-
tially subjective to extract from time series data (Schroeder et al. 2017). Additionally, they often treat
time series data as independent observations, neglecting the inherent temporal dependencies within
the data (Weerakody et al. 2021).
Advancements in deep learning algorithms, particularly those that can effectively capture the temporal
dependencies in time series data, hold promise for improving the accuracy and robustness of one-step attri-
bution methods (e.g. convolutional neural networks (CNNs), recurrent neural networks (RNNs), convolu-
tional long short-term memory networks (convLSTM)) (He et al. 2024). As research progresses in deep
learning, we can expect further advancements in the accuracy and interpretability of one-step attribution
methods, making them even more valuable tools for forest disturbance detection using remote sensing
data. Deep learning offers a powerful toolbox for analyzing remote sensing data, enabling the extraction
of valuable insights into real-world changes (Ma et al. 2019). Compared to traditional machine learning
methods, deep learning models excel at automatically extracting spatiotemporal features from time series
imagery in an end-to-end manner, eliminating the need for laborious manual feature engineering (Yan
et al. 2022). CNNs, gated RNNs, and Transformers have emerged as effective and accurate solutions for
remote sensing time series modeling tasks (Ben et al. 2018; Dou et al. 2021; Huang et al. 2023; Pelletier,
Webb, and Petitjean 2019; Weerakody et al. 2021; Wen et al. 2023).
However, one of the greatest challenges is its irregularity introduced by cloud cover and precipitation in
optical remote sensing data (B. Yang et al. 2022). Traditional methods such as monthly compositing or
missing value imputation are frequently employed to address irregularities (Marinelli et al. 2023). However,
these approaches tend to obscure the temporal information associated with disturbance events and could
lead to attenuation of disturbance signals. For deep learning methods, irregular time series data also
pose challenges in feature extraction, often resulting in model instability and poor generalizability
(M. Zhang et al. 2024). Several approaches have been explored to address the issue of irregular time series
data including weighted methods based on time interval information and time feature fusion methods (Tar-
asiou, Chavez, and Zafeiriou 2023; B. Yang et al. 2022; M. Zhang et al. 2024). For example, Gao et al. (2019)
assigned weights to observations based on the time interval information. These weights influence the output
of the input and forget gates in Long Short-Term Memory (LSTM) networks, controlling the impact of
observations from different time steps. B. Yang et al. (2022) and Zhu et al. (2017) implemented methods

INTERNATIONAL JOURNAL OF DIGITAL EARTH 3
that incorporate dedicated time gates specifically designed to process temporal information. These gates
extract time features and fuse them with features generated by other network units.
While Transformers are superior in capturing global features of time series, they still face challenges in
encoding temporal information in the presence of irregular remote sensing data (Tarasiou, Chavez, and
Zafeiriou 2023). Currently, Transformer-based methods typically address time series by improving the pos-
itional encoding structure. For instance, utilizing learnable positional encodings or timestamps to replace
standard Transformer positional encodings (Wen et al. 2023). The day of year (DOY) is the mostly used
data to support temporal information for model. It can be used as a part of input data or as positional
encoding to embed into the Transformer model directly (Huang et al. 2023; Tarasiou, Chavez, and Zafeiriou
2023; Yuan and Lin 2021). The enhancement of positional encoding strengthens the Transformer’s ability to
extract temporal features. Positional encoding methods designed for equal-interval sequences (e.g. text
sequence, equal-interval time series) may not be suitable for irregular time series containing timestamp
information. This is because equal-interval sequences maintain fixed element order and relative position
relationships, they use a unified position encoding matrix across different sequences. However, irregular
time series exhibit variable time information, leading to disparities among individual time series. Conse-
quently, further investigation is warranted to design efficient and succinct approaches for constructing pos-
itional encoding adapted to irregular time series.
Deep learning has emerged as a powerful tool for forest disturbance detection, but its success hinges on
the availability of large labeled datasets (Hethcoat et al. 2021). Acquiring such datasets can be a significant
challenge, often requiring expensive field surveys or expert-driven visual interpretation (Xu, Ma, and Zhang
2024). The scarcity of labeled data in many regions can lead to poor generalization performance of deep
learning models due to overfitting. Self-supervised learning offers a promising solution to circumvent
the small sample problem (Xu, Ma, and Zhang 2024). It involves pre-training deep learning models on
vast amounts of unlabeled data, followed by fine-tuning on the task-specific labeled data (Xu, Ma, and
Zhang 2024; Yuan and Lin 2021; X. Yang, Zhang, and Cui 2022). By leveraging the rich information within
unlabeled data, self-supervised learning models can effectively avoid overfitting even when limited labeled
samples are available (Xu, Ma, and Zhang 2024). Among various pre-training techniques, contrastive learn-
ing has become a popular choice (Jung et al. 2022; H. Li et al. 2022). Contrastive learning focuses on learning
generalizable features by minimizing the distance between similar samples (positive pairs) in the feature
space, while maximizing the distance between dissimilar samples (negative pairs) (Chen et al. 2020).
While existing contrastive learning methods using single or multiple images have shown promising results
(X. Li et al. 2022), most lack strategies to explicitly exploit the temporal dimension for sample construction.
This limitation hinders their direct application to time series remote sensing analysis for disturbance detec-
tion. The exploration of contrastive learning for tackling sparse-sample challenges in time series disturbance
detection tasks remains an exciting, under-explored area of research.
Although Transformers excel at extracting features from temporal sequences, they still face the following
challenges when applied to remote sensing time series for forest disturbance detection: (1) Irregular
sampling makes it difficult to encode temporal information accurately; (2) Different disturbance types
exhibited distinct spectral response mechanisms, and the impact of multi-source data on the detection accu-
racy of each disturbance class remained unclear; (3) Acquiring large, well-annotated datasets for forest dis-
turbance detection was highly demanding in terms of both time and resources. To address these gaps, this
study proposed a novel forest disturbance type detection method that leverages multi-source temporal data
and deep learning. The main innovations include:
(1) Enhanced temporal encoding of the Transformer: a time-embedding method was designed for irregular
remote sensing time series, allowing the model to more accurately capture the temporal information of
image sampling.
(2) Multi-source data fusion: optical imagery and SAR data were integrated into a unified detection frame-
work. We systematically evaluated the contribution of each data source to the detection accuracy of
various disturbance types.
(3) Self-supervised pretraining: a contrastive self-supervised learning strategy was introduced to pretrain
the model on unlabeled data. We compared this pretraining approach with conventional supervised
learning to demonstrate its effectiveness in small-sample scenarios.

4 M. ZHANG ET AL.
By addressing these critical aspects, our study endeavors to push the boundaries of forest disturbance
detection, providing valuable insights into how deep learning methodologies can be effectively utilized to
enhance environmental monitoring and management practices.
2. Materials and methodology
2.1. Study area
Due to its complex topography, diverse forest ecosystems, and frequent cloud cover, Pu’er City in southwest
Yunnan Province, China, presents a significant challenge for forest disturbance detection. The study
focused on this region, encompassing two Sentinel-2 tiles (47QPF and 47QQF), to develop a robust
approach to disturbance detection. Pu’er is the largest city in Yunnan and boasts extensive mountainous
terrain accounting for 98.3% of its total area. The subtropical monsoon climate influences the region, result-
ing in an average annual temperature ranging from 15°C to 20.3°C, a frost-free period exceeding 315 days
per year, and annual rainfall varying from 1100 mm to 2780 mm. Pu’er possesses a critical forest area with
forest coverage exceeding 67%, and is positioned as a significant forest product industry base. The region
exhibits distinct zonal vegetation characteristics driven by topography and climate. The dominant forest
types include monsoon evergreen broad-leaved forests (e.g. Castanopsis, Schima superba, and Betula
alnoides) and Simao pine forests. Simao pine forests are predominantly pure stands, mainly distributed
at elevations between 1100 and 1800 m. Additionally, eucalyptus and rubber trees are widely distributed
in Pu’er and serve as the main economic plantation forest. Forest disturbances in Pu’er are predominantly
attributable to human activities, primarily clear-cutting, accompanied by occurrences of forest fires, dis-
eases, and droughts. The specific spatial coverage and corresponding altitude distribution are presented
in Figure 1. To mitigate influence of non-forest area and minimize computational cost, a forest mask
was applied to land cover type data derived from Sentinel-2 image using the random forest algorithm,
with an overall accuracy of 95.03% and a kappa coefficient of 0.90.
2.2. Dataset
2.2.1. Forest disturbance data
Forest disturbance data were collected through field investigations in June, 2022. Three categories were
established for the forest area: no-disturbance, clear-cutting, and disease. For each disturbance event,
detailed geospatial information was recorded, including spatial location, boundaries, and year of occur-
rence. Following data collection, internal quality control procedures were implemented to ensure data
integrity. Samples with missing disturbance type or time information were removed, resulting in a final
Figure 1. Location of the study area and forest disturbance samples. (a) Location of Pu’er city, (b) Study area and distri-
bution of samples.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 5
dataset for further analysis. Subsequently, the samples were partitioned into training and testing datasets at
a ratio of 7:3. These forest disturbance polygons were converted into raster grids to facilitate integration
with Sentinel-1 and Sentinel-2 time series data. The final dataset comprised rasterized disturbance polygons
and time series data for model training and testing (details provided in Table 1).
2.2.2. Sentinel-1 SAR data
This study utilized Sentinel-1 data acquired in Interferometric Wide Swath (IW) mode during satellite
ascents. Level-1 Ground Range Detected (GRD) data products were obtained from Google Earth Engine
(GEE) (Pérez-Cutillas et al. 2023), encompassing two polarizations: Vertical-Vertical (VV) and Vertical-
Horizontal (VH). Monthly mean synthesis was conducted, aggregating data over a span of 12 months
annually, spanning from 2020 to 2022. Subsequently, images were exported from GEE at a resolution of
10 meters. Due to the pre-processing steps applied by the Sentinel-1 Toolbox within GEE (Veci et al.
2017), no additional pre-processing was required.
2.2.3. Sentinel-2 multispectral data
Time series of Sentinel-2 L2A level images were acquired for the period 2020-2022. Images with less than
80% cloud cover were selected. Cloud removal was performed using the cloud probability bands (pixels with
probability exceeding 50% were masked out), and shadows were removed based on the Scene Classification
Layer (SCL). Ten spectral bands were employed in the analysis: three visible bands (Blue, Green, Red), four
red-edge bands (Red Edge 1, 2, 3, 4), one near-infrared band (Near Infrared), and two shortwave infrared
bands (Shortwave Infrared 1, 2). All bands were resampled to a uniform 10-meter resolution using the near-
est neighbor method. Any missing values were replaced by 0. Figure 2 illustrates the distribution of valid
observation values across different Sentinel-2 tiles and years.
2.2.4. Disturbance response characteristics of different data sources
The response characteristics of multi-source data (Sentinel-1 and Sentinel-2) for different disturbance types
were demonstrated using image features, spectral features, and time-series spectral features (Figures 3 and 4).
Table 1. Forest disturbance samples for model training and testing.
Number of polygons in
each year
Disturbance type 2020 2021 2022 Area (km2) Training dataset (number of pixels) Testing dataset (number of pixels)
No-disturbance 149 128 254 23.87 169554 69118
Clear-cutting 89 148 195 19.10 130258 60784
Disease 18 12 41 0.40 2598 1394
Figure 2. Ratio of valid pixels (cloud-free, shadow-free, no missing data) in Sentinel-2 tiles (2020-2022).

6 M. ZHANG ET AL.
Figure 3. Image characteristics of clear-cutting and Simao pine disease for both Sentinel-1 and Sentinel-2 data. (a1) Senti-
nel-2 image before clear-cutting. (a2) Sentinel-2 image after clear-cutting. (a3) Sentinel-1 image before clear-cutting. (a4)
Sentinel-1 image after clear-cutting. (b1) Healthy Simao pine Sentinel-2 image. (b2) Diseased Simao pine Sentinel-2 image.
(b3) Healthy Simao pine Sentinel-1 image. (b4) Diseased Simao pine Sentinel-1 image.
Note: Sentinel-2 images were displayed in a false-color composite using shortwave infrared 1, near infrared, and red bands. Sentinel-1 images were
displayed in combination with VV, VH, and VV.
Images from Sentinel-2 exhibited a clear response to clear-cutting events, as evident from the distinct
boundaries between the cleared area and the undisturbed forest (Figure 3a1-a2). In contrast, Sentinel-1
data appeared to be heavily influenced by factors like terrain, surface roughness, and soil moisture
Figure 4. Spectral characteristics and time-series response of Sentinel-1 data for healthy and diseased Simao pine. (a) Spec-
tral features of Sentinel-1. (b) Spectral features of Sentinel-2. (c) Time series of backscatter coefficient for healthy and dis-
eased Simao pine in VV and VH polarizations.
Note: B02, blue band; B03, green band; B04, red band; B05, red edge 1 band; B06, red edge 2 band; B07, red edge 3 band; B08, near infrared band;
B8A, red edge 4 band; B11, shortwave infrared 1 band; B12, shortwave infrared 2 band.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 7
(Figure 3a3-a4). While some spatial differences could be observed between pre- and post-cutting images,
they lacked clarity in defining the clear-cutting boundary. Additionally, shadows caused by topography hin-
dered the acquisition of accurate disturbance information. Figure 3b1-b4 illustrate image characteristics of
healthy and diseased Simao pine in December 2022. Unlike clear-cutting, disease in Simao pine exhibited
minimal response in Sentinel-1 images, with no discernible difference between disturbed and undisturbed
areas. However, Sentinel-2 images provided clearer distinction.
Figure 4shows the spectral response differences between healthy and diseased Simao pine based on the
samples displayed in Figure 3. Neither of the Sentinel-1 polarization modes (VV and VH) revealed signifi-
cant spectral variations between healthy and diseased trees (Figure 4a). In contrast, Sentinel-2 data showed a
more pronounced spectral difference between healthy and diseased trees, particularly in the red-edge 2,
red-edge 3, near-infrared, and red-edge 4 bands (Figure 4b). Figure 4c depicted the time series curves
for backscatter coefficients of healthy and diseased Simao pine in both VV and VH bands. A weak response
to disease was observed in the VH band, where the backscatter coefficient of healthy pine was generally
lower than that of diseased pine (except for October). There was minimal to no difference in backscatter
coefficient between healthy and diseased pine in the VV band throughout the time series.
2.3. Methodology
Leveraging the standard Transformer as a foundation, this research devised the IRMST (IRregular Multi-
Source Transformer) model by improving the positional encoding structure. This enhancement enabled the
model to effectively capture temporal features inherent in irregular remote sensing time series data. To
explore the impact of multi-source data on detection accuracy of disturbance type, three strategies for differ-
ent data sources were employed, alongside supervised learning techniques, to train the IRMST model.
Finally, we investigated the effectiveness of self-supervised learning in addressing challenges posed by lim-
ited training sample sizes. This investigation involved evaluating the accuracy of the IRMST model under
both supervised and self-supervised learning frameworks, while considering various training sample sizes.
The overall flowchart is shown in Figure 5.
2.3.1. IRMST model: IRregular multi-source time series disturbance detection with transformer
architecture
This study proposed the IRMST model, which leveraged the Transformer architecture to process Sentinel-1/2
time series data for forest disturbance type detection. Transformer architecture has achieved remarkable
success across a wide range of sequence modeling tasks, with its self-attention mechanism serving as the
Figure 5. Flowchart of this study.

8 M. ZHANG ET AL.
core component. Self-attention enables the Transformer to flexibly capture dependencies between any two
positions in the sequence, regardless of their distance. This not only enhances the model’s ability to model
long-range dependencies but also allowed for highly efficient parallel computation. Before self-attention, the
embedding layer maps discrete input data into continuous vector representations, providing rich semantic
information and a uniform input format. This facilitatess task-specific feature learning directly from data.
As self-attention is inherently unaware of sequence order, positional encoding is added to retain positional
information following the embedding layer. Typically implemented via sinusoidal functions, it allows the
model to perceive sequence structure without sacrificing parallelism. However, for remote sensing time
series, standard embeddings and positional encodings often fall short. Such data is characterized by irregu-
lar temporal intervals, seasonality, and domain-specific temporal meanings, which fixed encodings struggle
to capture. Generic embeddings also lack awareness of physical concepts like phenological stages. These
challenges underscore the need for domain-adaptive encoding strategies to better model the temporal com-
plexity of remote sensing data.
(1) Sentinel-2 multispectral time series data feature extraction
Acquiring optical remote sensing data frequently encounters challenges with cloud cover, resulting in
missing values within time series images. Sentinel-2 multispectral data are susceptible to this issue as
well. The observation time of each image plays a crucial role in forest disturbance detection (represented
by Day of Year (DOY) in this study). Conventional Transformers utilize absolute positional encoding,
thereby assigning consistent position information to all input sequences (Vaswani et al. 2017), overlooking
the significant differences in observation times across diverse time series. To fully exploit the time infor-
mation embedded within irregular Sentinel-2 time series, this study discarded static positional encoding
and designed a new learnable encoding method.
Cloud cover and rain can lead to variations in the number of available observations and time series length
for each year. Therefore, the model input was pre-defined to a constant length of 100. Missing values within
shorter time series were filled with zeros. The IRMST model defined each element of the Sentinel-2 time
series as a tuple with two items, encapsulating both time information (t) and observation values (v). By
intricately intertwining the observation value with the observation time, the IRMST model mitigated the
issue of non-uniform time distribution inherent in optical remote sensing time series. The Sentinel-2
time series is represented as:
T ={(t, v)}n (1)
i i i=1
where n denotes the length of the time series, t and v represent observed time and values, respectively.
Figure 6a illustrated the module designed to handle irregular Sentinel-2 time series within the IRMST
model. The time embedding layer and value embedding layer were employed to elevate the feature dimen-
sions of temporal information and observation values, respectively. This amplification aims to enhance the
model’s sensitivity to subtle surface changes. Both time and value embedding were implemented through
feed forward neural network. The time embedding layer mapped timestamps to vectors, while the value
embedding layer mapped the reflectance values of different bands to vectors. These processes can be
expressed mathematically as:
Embedding(x)=ReLU(W x+b )W +b (2)
1 1 2 2
where x is multi-band reflectance v or Day of Year (DOY) t. W and W are weight parameters of the
i i 1 2
embedding layer, and b and b are the bias parameters. The ReLU represents the ReLU activation function,
1 2
which is widely used in feed forward neural networks due to its nonlinear characteristics, sparse activation,
and efficient computing speed (Glorot, Bordes, and Bengio 2011). To enhance the efficiency and stability of
model training, we normalized t and v prior to inputting it into the embedding layer.
To effectively integrate the observation values and their corresponding time information, the feature vec-
tors obtained from both the time and value embedding processes were added together. This yielded a fused
embedding vector (f) that served as the input for subsequent feature extraction stages. The structure of self-
attention layer in feature extraction and fusion stage is identical to that of the default Transformer attention

INTERNATIONAL JOURNAL OF DIGITAL EARTH 9
Figure 6. Architecture of IRMST model.
block. Unlike the standard learnable positional encoding, the IRMST model leveraged the specific DOY
value and learnable parameters within the time embedding module. This design empowered the model
to better adapt to forest disturbance detection tasks and handle the inherent irregularities present in remote
sensing time series data.
(2) Sentinel-1 SAR time series data feature extraction
The Sentinel-1 time series data employed in this study consists of two bands (VV and VH), obtained
through monthly mean compositing of all available images within each month. This process yielded a
fixed annual time series length of 12. In contrast to Sentinel-2 multispectral data, Sentinel-1 SAR data exhib-
ited less susceptibility to cloud cover. The consistent time interval and equal length across different years
and regions for Sentinel-1 SAR data alleviated the need for an additional time information extraction mod-
ule. However, to amplify the variations in backscatter coefficients caused by surface changes, the feature
extraction module for SAR data also incorporated value embedding. We also normalized the backscatter
coefficient data before inputting it to value embedding layer. The value embedding module for Sentinel-
1 data shared the same structure as its counterpart for Sentinel-2 data (Figure 6b). However, their learnable
parameters were independent, allowing the model to capture distinct feature representations for these two
sensor types. Due to the consistent time intervals within the Sentinel-1 time series, the standard Transfor-
mer positional encoding could be directly employed to represent the positional relationships of elements
within the sequence.
(3) Feature fusion and disturbance type classification
To integrate features extracted from Sentinel-1 and Sentinel-2 time series data, the IRMST model
adopted a dual-branch structure with feature-level fusion (Figure 6). The model leveraged separate branches
to process Sentinel-1 and Sentinel-2 data, and the extracted features were ultimately fused before forest dis-
turbance type prediction. The embedding module conducted fundamental encoding operations on pixel-
level Sentinel-1 and Sentinel-2 time series data, processing one year of time series at a time. Subsequently,
the feature extraction module utilized two self-attention layers to extract features from the encoded Senti-
nel-1 and Sentinel-2 time series. Given the significant impact of self-attention layers on feature fusion, the
feature fusion module incorporated two self-attention layers to comprehensively fuse temporal features

10 M. ZHANG ET AL.
from multi-source time series. We experimented with various numbers of attention blocks (8, 6, 4, 2, 1) and
observed no significant overfitting or underfitting when using two blocks. Consequently, we selected two
attention blocks for the feature fusion layer. The disturbance type prediction module comprised two
fully connected layers, facilitating judgments on the disturbance type (no disturbance, clear-cutting, disease,
etc.) of the target pixel based on depth features.
2.3.2. Self-Supervised learning framework for IRMST
To address the issue of limited training data for forest disturbance types, this study proposed a self-super-
vised learning framework based on the IRMST model. This framework leveraged a large amount of
unlabeled multi-source remote sensing time series data to learn more abstract and generalizable features.
Similar to the data input to supervised IRMST model, the input data for self-supervised IRMST are also
multi-source time series. We conducted spatially uniform sampling on all remote sensing data (two tiles,
three years) with a step size of 16, and obtained a total of 2,823,576 multi-source time series samples without
forest disturbance labels.
Self-supervised learning involved two key stages: unsupervised pre-training and supervised fine-tuning
(Figure 7). During the unsupervised pre-training stage, the IRMST model’s backbone network was trained
using contrastive learning on unlabeled multi-source data. This process aimed to develop a robust feature
extractor. The backbone network encompassed the IRMST model’s multi-source data embedding module,
feature extraction module, and feature fusion module. Contrastive learning focused on identifying common
features within the dataset by comparing positive and negative samples. In essence, it aimed to bring the
representations of similar samples (positive pairs) closer together in the feature space, while pushing the
representations of dissimilar samples (negative pairs) further apart. As depicted in Figure 7, the input
data (X) represented the unlabeled multi-source time series from Sentinel-1 and Sentinel-2 sensors. Positive
samples (Xpositive) for a given sample (X) were defined as time series data from different years but with the
same spatial location. Conversely, negative samples (Xnegative) represented time series data from any year but
at a different spatial location compared to the original sample (X). The same network was utilized to extract
features from Xpositive, Xnegative, and X, resulting in corresponding features (Zpositive, Znegative, and Z, respect-
ively). Finally, the model parameters were updated through a contrastive loss function and gradient
backpropagation.
The supervised fine-tuning stage involved replacing the projection head with a classifier (the last two
fully-connected layers in the IRMST model) to create a complete IRMST model incorporating the pre-
trained backbone network. This complete IRMST model was then fine-tuned using labeled disturbance
samples (X ) for the final classification task.
labeled
Figure 7. Self-supervised learning framework for IRMST.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 11
2.4. Experiment setting
2.4.1. Effectiveness of the temporal feature extraction module
To assess the efficacy of the IRMST model’s temporal feature extraction module for Sentinel-2 data, we con-
ducted a comparative experiment evaluating other methods for processing temporal information. Building
on previous studies of Transformer-based remote sensing time series models (Huang et al. 2023; Tarasiou,
Chavez, and Zafeiriou 2023; Yuan and Lin 2021), we employed three additional approaches for temporal
information extraction: (1) No DOY Information (ND): This baseline method entirely discarded temporal
information during model training. (2) DOY as Additional Band (DaB): This approach incorporated DOY
as an extra feature within the input data, effectively increasing the number of Sentinel-2 bands from 10 to 11
(denoted as v’ for the modified input data). It’s important to note that this method used standard modules of
Transformer and did not involve designing a separate model structure specifically for processing temporal
information (Vaswani et al. 2017). (3) DOY as Positional Encoding (DaPE): This method directly encoded
DOY as positional encoding, leveraging this representation to capture the order of observations within the
time series (without employing time embedding) (Zeng et al. 2023). A visual representation of methods DaB
and DaPE was shown in Figure 8.
2.4.2. Effectiveness of multi-source data in the IRMST model
To evaluate the impact of multi-source data on disturbance type detection accuracy, we conducted ablation
experiments using the IRMST model. We trained and tested the model under three data source configur-
ations: (1) Sentinel-1 Time Series Only: This scheme utilized solely Sentinel-1 data for training and testing.
The IRMST model structure was adjusted accordingly by removing the redundant data embedding and fea-
ture extraction modules for Sentinel-2 data. Specifically, Sentinel-2 data embedding module and the two
self-attention layers dedicated to its feature extraction were removed. (2) Sentinel-2 Time Series Only:
This scheme employed only Sentinel-2 data for training and testing. Similar to the previous scenario, the
IRMST model structure was adapted by removing unnecessary components for processing Sentinel-1
data. (3) Combination of Sentinel-1 and Sentinel-2 Time Series: This configuration utilized both Senti-
nel-1 and Sentinel-2 data for a comprehensive analysis. The complete IRMST model structure, as described
earlier, was employed in this setting.
2.4.3. Improvement of self-supervised learning
To quantitatively assess the effectiveness of self-supervised learning for forest disturbance type detection, we
conducted the following comparative experiments: (1) IRMST with supervised learning: The IRMST model
was directly trained on the labeled disturbance samples without any pre-training stage. This served as the
baseline for comparison. (2) IRMST with self-supervised learning: The IRMST model was pre-trained using
the self-supervised learning framework described above. This pre-trained model was then fine-tuned with
Figure 8. Temporal feature extraction methods for comparison. (a) DOY as an additional Sentinel-2 band (DaB); (b) DOY as
positional encoding (DaPE).

12 M. ZHANG ET AL.
labeled disturbance samples for forest disturbance type classification. The performance of both models (self-
supervised and supervised) was evaluated and compared in terms of forest disturbance type detection accu-
racy. (3) Impact of sample size on self-supervised and supervised learning: We divided the available training
data into five subsets representing different sample sizes: 20%, 40%, 60%, 80%, and 100% of the total train-
ing data. For each sample size level, we trained both the self-supervised learning and supervised learning
models using the corresponding subset of training data. The performance of both models was then evalu-
ated on a held-out test set to assess the impact of sample size on detection accuracy. This experiment
allowed us to investigate the benefits of self-supervised learning for improving the generalizability of the
IRMST model, particularly in scenarios with limited labeled training data.
2.4.4. Training details
For supervised training of the IRMST model, the batch size was 128. We employed the Adam optimizer,
with parameters β = 0.9 and β = 0.999. The initial learning rate was set to 1e-5. The Focal Loss function
1 2
(Lin et al. 2017) was used to measure the discrepancy between the predicted and actual class labels. Training
was conducted for 50 epochs, with early stopping implemented to halt the process if the validation loss did
not improve for 5 consecutive epochs. The model training was performed on an NVIDIA Quadro RTX 4000
GPU with 8GB of memory. The self-supervised learning framework included model pre-training and fine-
tuning, with the fine-tuning process using parameters identical to those used in supervised learning frame-
work. During pre-training, the batch size was 512, the learning rate was 1e-4, and we used a contrastive loss
function (Chen et al. 2020). All other parameters were also consistent with the supervised learning
configuration.
2.4.5. Accuracy evaluation
Forest disturbance type detection accuracy was evaluated using a dataset of 310 disturbance samples rep-
resented as polygons. It is important to note that the IRMST model predicted the disturbance type for
individual pixels. Therefore, for each test sample (polygon), a prediction was considered correct only
when the number of correctly classified pixels within the polygon exceeded half of its total area (Linke
et al. 2017). We employed User’s Accuracy (UA), Producer’s Accuracy (PA), and F1 score to assess
the model’s classification performance for each disturbance category (Zhong, Hu, and Zhou 2019). UA
indicates the probability that a pixel classified by the model as belonging to a specific disturbance category
actually belongs to that category. PA represents the probability that a pixel belonging to a particular dis-
turbance category was correctly classified by the model into that category. F1 score is the harmonic mean
of UA and PA, providing a balanced view of model performance. It is particularly useful for evaluating
models on imbalanced datasets, which are common in remote sensing applications where certain disturb-
ance types might be less frequent (Zhong, Hu, and Zhou 2019). The overall F1 score of the model was
calculated as the average F1 score across all disturbance categories. The formula for calculating the overall
F1 score was provided below:
1
􏽘N
F1= F1
i
N
i=1
2∗UA∗PA
F1 = i i
i UA +PA
i i
Where N is the number of disturbance types, and i is the ith disturbance type.
3. Results
3.1. Performance of IRMST on forest disturbance types detection
3.1.1. Evaluation of temporal feature extraction for Sentinel-2 time series
The IRMST model achieved the highest F1 score for each disturbance type, surpassing other methods by a
margin of 5% to 14% (Table 2). Notably, the DaPE method exhibited the lowest accuracy across all dis-
turbance types. This suggested that directly replacing positional encoding with raw time information

INTERNATIONAL JOURNAL OF DIGITAL EARTH 13
Table 2. Accuracy assessment of different methods on temporal feature extraction.
ND DaB DaPE IRMST
Disturbance type UA PA F1 UA PA F1 UA PA F1 UA PA F1
No disturbance 0.96 0.93 0.95 0.95 0.91 0.93 0.96 0.84 0.89 0.98 0.95 0.97
Clear-cutting 0.95 0.98 0.96 0.93 0.97 0.95 0.91 0.97 0.94 0.95 1.00 0.97
Disease 0.78 0.78 0.78 0.74 0.74 0.74 0.50 0.78 0.61 0.95 0.87 0.91
Overall F1 0.90 0.87 0.81 0.95
(DOY) was not an effective approach for extracting temporal features. Interestingly, the model without
any DOY information (ND) outperformed both DaB and DaPE. This indicated that omitting temporal
information altogether could be more effective than using inappropriate methods for extracting temporal
features.
To further illustrate the differences in temporal feature extraction between the four strategies, a repre-
sentative clear-cutting patch was analyzed as an example. Figure 9 presents the multi-band time series
for this patch alongside the attention maps generated by each method. There was a clear decrease in reflec-
tance across multiple bands around the 72nd time step (Figure 9a), signifying the clear-cutting event near
the end of the year. The ND method distributed attention weights across various time steps, lacking specific
focus on the clear-cutting event (Figure 9b1). The DaB method assigned some attention to the time of clear-
cutting, but it dispersed attention weights across other time points (such as around the 50th time step),
suggesting less focused disturbance event (Figure 9b2). The DaPE method exhibited more scattered atten-
tion weights, suggesting an inability to learn effective temporal features (Figure 9b3). The IRMST model
predominantly focused on data near the 72nd time step, with the highest attention weight concentrated
around the 72nd (Figure 9b4). This indicated successful identification of the clear-cutting event. It’s impor-
tant to note that all three methods (DaB, DaPE, and IRMST) assigned high attention weights to positions
after the 76th time step. This arose from a pre-defined input length of 100 for the time series. Sentinel-2 time
series data exhibited varying lengths, and zero padding was applied to those shorter than 100. Consequently,
the data after the 76th time step held no meaningful information, yet these models allocated attention to this
padded region. Notably, the IRMST model exhibited a reduced focus on this area compared to DaB and
DaPE, suggesting a more robust temporal feature extraction module that mitigated this issue. These obser-
vations reinforced the effectiveness of the IRMST model’s temporal feature extraction capabilities. It suc-
cessfully identified the clear-cutting event and demonstrated a more targeted focus on informative time
steps compared to the other methods.
Figure 9. Multi-band time series of a typical clear-cutting sample and attention maps of different models. (a) Sentinel-2
time series of the typical clear-cutting sample. (b1) Attention map of ND. (b2) Attention map of DaB. (b3) Attention
map of DaPE. (b4) Attention map of IRMST.

14  M. ZHANG ET AL.
3.1.2. Impact of multi-source data on disturbance type detection
The influence of multi-source data on disturbance type detection accuracy was evaluated using the IRMST
model  (training  with  supervised  learning)  with  different  data  configurations  (Table  3).  Employing
multi-source data consistently improved IRMST model performance compared to using single-source
data (Sentinel-1 or Sentinel-2). Utilizing only Sentinel-1 time series data at the pixel level resulted in
poor performance. The model trained solely on Sentinel-1 data exhibited a F1 score of just 0.59, indicating
its ineffectiveness for forest disturbance type detection. Adding Sentinel-1 data to Sentinel-2 data yielded
some improvement, particularly for forest disease detection. However, it led to a slight decline in clear-cut-
ting detection compared to using Sentinel-2 data alone.
3.2. Impact of self-supervised learning
3.2.1. Improvement of disturbance type detection accuracy
Table 4summarizes the accuracy metrics achieved by the self-supervised and supervised IRMST models for
each disturbance type. The F1 score obtained through self-supervised learning surpassed that achieved
solely through supervised learning. Specifically, self-supervised learning enhanced the accuracy of the
IRMST model in detecting instances of no-disturbance and clear-cutting. The accuracy for detecting disease
remained comparable to that achieved through supervised learning. To delve deeper into this phenomenon,
a representative no-disturbance sample and the attention distributions from both models were analyzed
through Figure 10. Notably, the self-supervised model’s focus points (DOY 194 and 289) coincided with
cloud-free conditions observed in the images. In contrast, the supervised model focused on time steps
with thin clouds (DOY 89 and 344). It suggested that self-supervised learning could effectively mitigate
the influence of thin clouds on disturbance detection. The supervised model, on the other hand, might
have been misled by subtle changes in spectral data caused by thin clouds, resulting in misclassifications.
3.2.2. Impact of sample size on self-supervised learning and supervised learning
Figure 11 depicts the overall F1 score of the IRMST models under different sample size and training
methods (self-supervised and supervised learning). When dealing with limited training data (20% of all
samples), the self-supervised IRMST model achieved a significantly higher accuracy (0.95) compared to
the supervised model (0.86). This demonstrated the ability of self-supervised learning to mitigate the nega-
tive impact of small sample sizes. As the sample size increased, the accuracy of the supervised learning
model gradually improved. By the time the sample size reached 60%, its accuracy approached that of the
self-supervised model. Furthermore, the self-supervised model’s accuracy remained stable around 0.95
with increasing sample size, indicating its convergence in small sample scenarios. Even with larger sample
sizes (60% to 100%), the self-supervised learning model exhibited slightly higher accuracy compared to the
supervised model. This suggested that self-supervised learning not only alleviated small sample issues but
potentially improved the upper limit of achievable model accuracy.
Table 3. Accuracy assessment of different data sources.
|                  | Sentinel-1 |      |      | Sentinel-2 |      | Sentinel-1 + Sentinel-2 |      |
| ---------------- | ---------- | ---- | ---- | ---------- | ---- | ----------------------- | ---- |
| Disturbance type | UA PA      | F1   | UA   | PA         | F1   | UA PA                   | F1   |
| No disturbance   | 0.75 0.98  | 0.85 | 0.98 | 0.96       | 0.97 | 0.98 0.95               | 0.97 |
| Clear-cutting    | 0.96 0.75  | 0.85 | 0.97 | 0.99       | 0.98 | 0.95 1.00               | 0.97 |
| Disease          | 1.00 0.04  | 0.08 | 0.87 | 0.87       | 0.87 | 0.95 0.87               | 0.91 |
| Overall F1       | 0.59       |      | 0.94 |            |      | 0.95                    |      |
Table 4. Accuracy assessment of self-supervised IRMST and supervised IRMST.
|                | Self-supervised IRMST |      |      |     |      | Supervised IRMST |      |
| -------------- | --------------------- | ---- | ---- | --- | ---- | ---------------- | ---- |
| Type           | UA                    | PA   | F1   |     | UA   | PA               | F1   |
| No disturbance | 0.98                  | 0.98 | 0.98 |     | 0.98 | 0.95             | 0.97 |
| Clear-cutting  | 0.99                  | 1.00 | 0.99 |     | 0.95 | 1.00             | 0.97 |
| Disease        | 0.95                  | 0.87 | 0.91 |     | 0.95 | 0.87             | 0.91 |
| Overall F1     | 0.96                  |      |      |     | 0.95 |                  |      |

INTERNATIONAL JOURNAL OF DIGITAL EARTH 15
Figure 10. Impact of self-supervised learning on mitigating cloud effects in disturbance detection. (a-d) True-color Sentinel-
2 images of a no-disturbance sample at four time steps: (a) DOY 89 (supervised learning focus point) – Thin clouds. (b) DOY
194 (self-supervised learning focus point) – Cloud-free. (c) DOY 289 (self-supervised learning focus point) – Cloud-free. (d)
DOY 344 (supervised learning focus point) – Thin clouds. (e) Sentinel-2 time series reflectance of the no-disturbance sample.
(f) Attention weight distribution of self-supervised and supervised learning models on the no-disturbance time series. The
polygons in images represent the bounding of the selected no-disturbance sample.
Figure 11. Impact of sample size on IRMST model accuracy with self-supervised and supervised learning.
3.3. Spatiotemporal distribution of forest disturbance types
The IRMST model successfully generated a spatiotemporal distribution map of forest disturbance types
across the study area (Figure 12). This map revealed significant variations in the spatial distribution of
clear-cutting events over the investigated years (2020-2022). Clear-cutting activities were primarily concen-
trated in the central and southwestern regions of the study area in 2020, and shifted to the northwestern and

16 M. ZHANG ET AL.
Figure 12. Spatiotemporal distribution map of disturbance types.
Table 5. Forest disturbance area (km²) between 2020 and 2022.
Year Clear-cutting Disease Total
2020 306.09 47.56 353.65
2021 240.97 18.47 259.44
2022 288.71 24.16 312.87
Total 835.77 90.19 925.96
southwestern regions in 2021 and 2022. The map highlighted a more persistent and severe disease disturb-
ance concentrated in the central part of the study area. Additionally, a notable presence of disease disturb-
ance was observed in the northern region during 2020.
Table 5summarized the total forest disturbance area for each year between 2020 and 2022. The total area
affected by disturbances over this period was approximately 925.96 km². No statistically significant trend in
the overall forest disturbance area was observed across the three years. The disturbance area fluctuated
slightly year-to-year, with the largest area (353.65 km²) occurred in 2020 and the smallest (259.44 km²)
in 2021. The area affected by disease disturbance consistently remained lower than the area affected by
clear-cutting across all three years. Similar to the overall trend, the area of both clear-cutting and disease
disturbance peaked in 2020 (306.09 km² for clear-cutting and 47.56 km² for disease) and reached a mini-
mum in 2021 (240.97 km² for clear-cutting and 18.47 km² for disease).
4. Discussions
4.1. Representation of time information in deep learning
Our study highlights the importance of accurately representing time information in forest disturbance
detection algorithms, particularly in the context of irregular time series data affected by cloud cover and
other weather conditions. We adopted a time feature fusion approach, which integrates time information
with other features to improve model performance. Our study innovatively implemented a dedicated mod-
ule specifically designed to extract temporal features based on Transformer. It maps individual observation
times to positional encoding vectors, with the mapping functions being learnable rather than predefined.
Transformer-based architectures for time series analysis typically focus on the design of positional encoding
(Wen et al. 2023). Unlike gated RNNs, these models generally don’t utilize time interval data as direct input
(Tarasiou, Chavez, and Zafeiriou 2023). This might be attributed to the underlying principles of attention

INTERNATIONAL JOURNAL OF DIGITAL EARTH 17
mechanisms employed in Transformers. Their ability to simultaneously focus on global features across
different time steps necessitates absolute time information, such as timestamps. Tarasiou, Chavez, and
Zafeiriou (2023) addressed this by utilizing a learnable lookup table to construct a global mapping between
observation times and positional encoding. However, introducing an additional lookup table can increase
the operational complexity of the model, potentially hindering its practical application. Similar to the idea of
a lookup table, this study also established a mapping from timestamps to feature vectors. However, this
structure is embedded in the IRMST network and can be directly trained end-to-end without the need
for additional lookup tables.
The findings of this study emphasize the crucial role of accurate temporal information representation in
time series analysis for forest disturbance detection. Inappropriate methods for extracting temporal features
can potentially hinder the model’s ability to exploit the inherent temporal patterns within the data. In some
cases, as our results suggest, omitting temporal information altogether might lead to better performance
compared to using an ineffective feature extraction method. Inappropriate temporal feature extraction
methods might misinterpret the irregular distribution of observations caused by missing data as actual tem-
poral patterns. This can lead the model to focus on irrelevant information and hinder its ability to capture
the true underlying temporal dynamics associated with forest disturbances. In addition, introducing com-
plex time feature extraction modules can increase the overall complexity of the model. This can lead to
overfitting, especially when dealing with limited training data. Furthermore, these complex modules
might not be well-suited for capturing the specific temporal characteristics relevant to forest disturbance
detection in the presence of missing data. Investigating hybrid approaches that combine strengths from
both weighted and time feature fusion methods, and exploring alternative methods for incorporating
time information into Transformer-based architectures could be promising direction for future research.
By focusing on appropriate temporal feature extraction methods, future research can potentially lead to
the development of more robust and generalizable models for forest disturbance detection using remote
sensing data, even in scenarios where data is incomplete due to cloud cover or other interfering factors.
The performance of time series feature extraction is also related to the degree of data preprocessing. The
data acquisition and preprocessing workflow in this study is relatively streamlined. We neither deliberately
selected equal-interval sequences nor performed imputation on missing values. Instead, we refined our
model architecture to better address these challenges. Conventional approaches typically selected a fixed
number of images each year to construct datasets and then impute missing values. For example, Marinelli
et al. (2023) generated equal-interval time series through monthly compositing. Although this strategy sim-
plified subsequent algorithm design, imputation inevitably introduced additional errors and may have
obscured genuine forest disturbance signals. In our study, to fully leverage all available remote-sensing
information, we analyzed nearly every accessible Sentinel-2 image over the course of a year. For missing
pixels, we employed the ‘zero-filling’ method. Though this approach may have attenuated disturbance sig-
nals, it preserves the timestamp associated with each image. Even if pixels were missing, the corresponding
temporal label enabled the model to recognize missing-data patterns. Masking missing values could also
reduce the negative impact on disturbance detection, but it disrupted temporal continuity.
4.2. The role of self-supervised learning
High-performance deep learning models often require vast amounts of labeled training data. Unfortunately,
acquiring labeled forest disturbance samples is a time-consuming and laborious process, leading to a scar-
city of suitable data. Self-supervised learning presents a promising solution by enabling the utilization of
unlabeled remote sensing data from the target domain for pretraining deep learning models. This approach
helps extract effective features without the need for extensive manual labeling. Current research on contras-
tive learning in remote sensing primarily focuses on spatial and spectral augmentations (e.g. random crop-
ping, Gaussian noise) (Hou et al. 2022). There is a relative lack of exploration regarding temporal dimension
augmentation (Wang et al. 2022). Xu, Ma, and Zhang (2024) proposed a self-supervised time series crop
mapping method based on Transformers and contrastive learning, demonstrating its potential to alleviate
sample scarcity. Our study used contrastive learning to pretrain IRMST network and treated time series data
from different years but the same spatial location as positive pairs. This strategy aimed to train the model to
minimize the influence of normal interannual dynamic changes (e.g. phenology, weather) on feature

18 M. ZHANG ET AL.
extraction. This approach aligns with the notion that a universal strategy for constructing positive and nega-
tive samples can improve the performance of deep learning models in remote sensing analysis (Zhu et al.
2022). However, it is crucial to acknowledge that different remote sensing applications (e.g. single scene vs.
time series analysis, vegetation vs. hydrology) necessitate task-specific strategies for optimal positive and
negative sample pair definitions.
Beyond addressing sample scarcity, self-supervised learning offers additional advantages for the IRMST
model. Similar to Xu, Ma, and Zhang (2024), our study found that self-supervised pretraining can mitigate
misclassification errors and reduce the impact of cloud pollution pixels on disturbance detection. This
improvement in accuracy can be attributed to several factors, including the increased representativeness
of training samples, expansion of data volume and diversity, and the use of learnable positional encoding
in the IRMST model. Overall, self-supervised learning holds significant promise for improving the perform-
ance of deep learning models in remote sensing applications, including forest disturbance detection.
4.3. The role of SAR data in disturbance detection
The role of SAR data in forest disturbance detection is significant, particularly in regions where optical data
is heavily impacted by cloud coverage. SAR data offers the advantage of being less affected by clouds, mak-
ing it a valuable resource for monitoring forest disturbances. However, SAR data also presents challenges,
such as strong noise that can cause small-scale or weaker forest disturbances to be overlooked (Sun et al.
2023). Previous research has indicated that pixel-level features of single-scene SAR images have limited
effectiveness in detecting deforestation (Hethcoat et al. 2021). Our study further corroborates this
finding by demonstrating that using pixel-level Sentinel-1 time series data alone results in poor detection
performance for forest disturbance types. We also found the detection accuracy of clear-cutting is higher
than for diseases. This result is consistent with the response of Sentinel-1 to different forest disturbance
types, namely, Sentinel-1 has a response to clear-cutting (but the boundary is unclear) and the response
to diseases is very weak.
When fusing Sentinel-1 SAR data with Sentinel-2 multispectral time series, the accuracy of detecting
clear-cutting disturbances decreased, while the accuracy of detecting diseases improved compared to
using only Sentinel-2 data. The potential reason for the limited effectiveness of SAR data in detecting
clear-cutting could be the lack of spatial feature utilization in our proposed method. Clear-cutting events
often lead to drastic changes in surface spatial texture, which SAR data can respond to in visual features
of images. However, without spatial information, SAR data may struggle to accurately detect such disturb-
ances. This is further supported by the work of Hethcoat et al. (2021), who achieved better results by incor-
porating texture analysis from SAR data for high-intensity selective logging detection. Therefore, when
spatial information is disregarded, incorporating SAR data tends to weaken the representativeness of
clear-cutting features extracted from Sentinel-2 time series. Conversely, disease disturbances typically result
in weaker changes in forest spatial texture, but tend to lead to changes in vegetation moisture content
(Cotrozzi 2022). Therefore, a single Sentinel-1 pixel may be beneficial for characterizing disease disturb-
ances, explaining why the addition of Sentinel-1 pixel-level time series improved the detection accuracy
of disease disturbances in our study. However, using only single pixel SAR time series without multispectral
information cannot effectively detect clear-cutting. Extracting and leveraging spatial information from SAR
data is crucial for improving complex disturbance type detection. Deep learning methods can potentially
automate this process, but their effectiveness depends on the availability of high-quality training data.
Self-supervised learning can potentially address challenges related to sample quality for deep learning
models using SAR data. By relying on self-supervised algorithms and proxy tasks, this approach can poten-
tially reduce the training difficulty for spatial feature extractors specifically designed for SAR data.
Improving the performance of SAR data at the algorithm level was crucial, but enhancements at the data
level should not be overlooked either. Different types of SAR data contributed differently to forest disturb-
ance detection. Radar wavelength played a key role: for instance, Dalponte et al. (2023) found that COSMO-
SkyMed (X-band) outperformed Sentinel-1 (C-band) in detecting windthrow events. While C-band is more
sensitive to logging-induced changes, X-band, with its shorter wavelength, captured finer variations in the
canopy surface, making it more responsive to subtle or superficial disturbances. Fusing both types of data
could potentially enhance detection accuracy. However, the framework in Dalponte et al. (2023) struggled

INTERNATIONAL JOURNAL OF DIGITAL EARTH 19
with integrating SAR data of different spatial and temporal resolutions. In contrast, deep learning architec-
tures, equipped with modules like convolution and self-attention, allow for efficient feature-level fusion of
heterogeneous SAR data.
Despite these advantages, SAR-based disturbance detection continues to be challenged by terrain effects.
Topography-induced distortions significantly reduced SAR performance. Terrain correction using a digital
elevation model (DEM) was typically required to mitigate pseudo-changes caused by slope and aspect.
Moreover, polarimetric decomposition methods such as Cloude–Pottier (Cloude and Pottier 2002) could
separate radar backscatter into physically meaningful scattering mechanisms (e.g. volume, surface, and
double-bounce scattering). Leveraging these decomposed components helps distinguish real canopy
changes (caused by disturbances like clear-cutting or insect outbreak) from variations due to terrain,
thereby reducing background noise and improving detection reliability.
4.4. Transferability of the model
Due to significant variations in spectral characteristics and disturbance manifestations across different
regions and time periods, models trained on limited spatial extents or small datasets often experience sub-
stantial declines in detection accuracy when applied to broader, more heterogeneous datasets. When trans-
ferring the IRMST model to other regions, we must account for differences in disturbance types,
environmental conditions, and data availability. Disturbance events such as logging, insect outbreaks,
and windthrows differ in spatial scale, intensity, and temporal progression, which can hinder the general-
izability of learned features. This study considered both clear-cutting and disease, representing abrupt and
gradual disturbances, respectively. The IRMST model performed well in both aspects. This suggests that the
model has the potential to generalize to other abrupt or gradual disturbance types, provided it undergoes
modest fine-tuning.
Beyond disturbance types, natural environmental differences (e.g. vegetation composition and seasonal
dynamics) can also affect model transferability. These factors may cause confusion between natural pheno-
logical changes and actual disturbance signals. Since our study area is located in a subtropical region charac-
terized by evergreen vegetation and an absence of snow, transferring the model to temperate zones would
require particular attention to the effects of deciduous leaf-off periods and snow cover. In such cases,
additional disturbance samples may be necessary to achieve satisfactory detection performance.
4.5. Limitations and future work
Detecting forest disturbance accurately requires precise information regarding both the timing and
types of disturbances. However, obtaining highly specific and accurate disturbance time samples can
be challenging. In this study, due to the difficulty of acquiring such precise time samples, we did not
further subdivide the samples within each year. Nevertheless, our model demonstrates the capability
to capture temporal information effectively by focusing on features corresponding to specific times.
Moreover, while our study focused on detecting clear-cutting and disease disturbance types, it did
not distinguish between insect-induced disturbances and diseases. Recognizing the potential differences
between these types and their respective occurrence times is crucial for comprehensive disturbance
detection. The limited availability of samples further constrained our ability to explore additional dis-
turbance types.
Given that some forest disturbance events were relatively rare, the sample classes became highly imbal-
anced, causing the model to overfit to the minority class. To mitigate this issue, we introduced a focal loss.
Additionally, during data preprocessing, oversampling techniques can be employed to augment the min-
ority class. For instance, random replication or the SMOTE method (Chawla et al. 2002), which generates
new minority-class samples by interpolating within the feature space can increase the sample size. Although
down-sampling methods that reduce the number of majority-class samples randomly or heuristically can
also address class imbalance, they were not appropriate for our study, as they would result in a significant
shrinkage of the overall sample size. On the other hand, the self-supervised learning approach used here
leveraged large amounts of unlabeled data to pretrain the model, thereby further enhancing its robustness
and generalization capability.

20 M. ZHANG ET AL.
The configuration of hyperparameters (e.g. learning rate, network depth, batch size) has a profound
impact on model performance. Improper settings could not only hinder the model’s convergence but
also lead to overfitting or underfitting. To enhance the generalization of the IRMST model, this study
employed cross-validation for evaluation. Our approach also has room for improvement. By incorporating
systematic hyperparameter search methods such as Bayesian optimization, random search, or grid search,
we can further refine our experimental plan and reduce the model’s sensitivity to hyperparameter settings.
Moreover, integrating regularization techniques such as dropout and batch normalization can further
enhance the stability of model convergence.
With the advancement of remote sensing technology, various types of data have been applied to
forest monitoring. For instance, Light Detection and Ranging (LiDAR) technology provides direct infor-
mation on canopy height, forest structure, and vertical stratification. Meanwhile, the sub-meter spatial
resolution of high-resolution Unmanned Aerial Vehicle (UAV) imagery enables the extraction of detailed
surface textures and canopy gap characteristics. Incorporating a multi-scale feature pyramid network to
upgrade the IRMST model can facilitate the fusion of texture and spectral features across different spatial
resolutions, thereby significantly enhancing the model’s ability to capture spatial patterns and
relationships.
Future research may aim to enhance the model’s capability to detect a wider range of forest disturbances.
Our self-supervised IRMST model can be readily applied and tested for detecting additional disturbance
types, thus offering a promising avenue for further research. By incorporating a more diverse dataset of for-
est disturbances, the approach presented in this study can be extended across a broader spatiotemporal
domain. It can also elevate the temporal resolution of disturbance detection to near the revisit frequency
of remote sensing satellites. This not only optimizes forest resource management and enhances economic
returns, but also enables timely identification and prevention of large-scale ecological degradation.
5. Conclusion
Forests in subtropical regions are susceptible to various disturbances like logging and diseases. These
disturbances significantly impacted the health and functionality of forest ecosystems. Accurate identifi-
cation of the types and timing of these disturbances is crucial for maintaining forest ecological security
and for informing decisions related to human societies that depend on these ecosystems. This study
addressed this challenge by proposing a deep learning model, IRMST, for forest disturbance detection
using multi-source remote sensing time series data. The IRMST model incorporated two key advance-
ments: (1) Improved time information encoding: The Transformer architecture within IRMST utilized
an enhanced method for encoding temporal information from the time series data. This improvement
facilitated more accurate extraction of temporal features from Sentinel-2 data, leading to better dis-
turbance detection accuracy. Our findings also emphasized the importance of appropriate time infor-
mation encoding, as ineffective methods can hinder model performance. (2) Self-supervised learning
for robustness: The IRMST model leveraged self-supervised learning for pretraining. This approach
addressed the scarcity of labeled data for forest disturbance detection and enhanced the model’s overall
accuracy and stability. Self-supervised learning also improved the model’s ability to handle noise in the
data, such as thin clouds. Experiments confirmed that self-supervised learning offered superior gener-
alizability, particularly in situations with limited training data, compared to supervised learning
methods alone.
The IRMST model offers a promising approach for accurate forest disturbance detection in subtropical
regions using multi-source remote sensing time series data. In addition, we found that while pixel-level Sen-
tinel-1 data exhibited a less significant response to clear-cutting, it showed a more pronounced response to
diseases. This underscored the importance of utilizing spatial information in SAR data for effective disturb-
ance detection. The findings of this study have significant implications for addressing problems related to
feature extraction from irregular time series and limited disturbance type samples.
Disclosure statement
No potential conflict of interest was reported by the author(s).

INTERNATIONAL JOURNAL OF DIGITAL EARTH 21
Funding
This work was supported by China Scholarship Council [grant number: 202108350057]; National Natural Science
Foundation of China [grant number: 32371865]; National Key R&D Program of China [grant number:
2021YFE0117700-4, 2021YFD2200400102].
Data availability statement
The data that support the findings of this study are available on request from the corresponding author.
References
Ballère, M., A. Bouvet, S. Mermoz, T. L. Toan, T. Koleck, C. Bedeau, M. André, E. Forestier, P. L. Frison, and C.
Lardeux. 2021. “SAR Data for Tropical Forest Disturbance Alerts in French Guiana: Benefit over Optical
Imagery.” Remote Sensing of Environment 252:112159. https://doi.org/10.1016/j.rse.2020.112159.
Bastit, F., M. Brunette, and C. Montagné-Huck. 2023. “Pests, Wind and Fire: A Multi-hazard Risk Review for Natural
Disturbances in Forests.” Ecological Economics 205:107702. https://doi.org/10.1016/j.ecolecon.2022.107702.
Ben, H. A., A. Benoit, P. Lambert, and A. C. Ben. 2018. “3-D Deep Learning Approach for Remote Sensing Image
Classification.” IEEE Transactions on Geoscience and Remote Sensing 56 (8): 4420–4434. https://doi.org/10.1109/
TGRS.2018.2818945.
Bullock, E. L., C. E. Woodcock, and P. Olofsson. 2020. “Monitoring Tropical Forest Degradation Using Spectral
Unmixing and Landsat Time Series Analysis.” Remote Sensing of Environment 238:110968. https://doi.org/10.
1016/j.rse.2018.11.011.
Caputo, J., C. M. Beier, P. M. Groffman, D. A. Burns, F. D. Beall, P. W. Hazlett, and T. E. Yorks. 2016. “Effects of
Harvesting Forest Biomass on Water and Climate Regulation Services: A Synthesis of Long-Term Ecosystem
Experiments in Eastern North America.” Ecosystems 19 (2): 271–283. https://doi.org/10.1007/s10021-015-
9928-z.
Cardille, J. A., E. Perez, M. A. Crowley, M. A. Wulder, J. C. White, and T. Hermosilla. 2022. “Multi-sensor Change
Detection for Within-Year Capture and Labelling of Forest Disturbance.” Remote Sensing of Environment
268:112741. https://doi.org/10.1016/j.rse.2021.112741.
Chawla, N. V., K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer. 2002. “SMOTE: Synthetic Minority Over-sampling
Technique.” Journal of Artificial Intelligence Research 16 (1): 321–357. https://doi.org/10.5555/1622407.
1622416.
Chen, T., S. Kornblith, M. Norouzi, and G. Hinton. 2020. “A Simple Framework for Contrastive Learning of Visual
Representations.” Proceedings of the 37th international conference on machine learning (ICML), Vienna,
Austria, 1597-1607.
Cloude, S. R., and E. Pottier. 2002. “An Entropy Based Classification Scheme for Land Applications of Polarimetric
SAR.” IEEE Transactions on Geoscience and Remote Sensing 35 (1): 68–78. https://doi.org/10.1109/36.551935.
Cotrozzi, L. 2022. “Spectroscopic Detection of Forest Diseases: A Review (1970–2020).” Journal of Forestry Research 33
(1): 21–38. https://doi.org/10.1007/s11676-021-01378-w.
Curran, L. M., and S. N. Trigg. 2006. “Sustainability Science from Space: Quantifying Forest Disturbance and Land-use
Dynamics in the Amazon.” Proceedings of the National Academy of Sciences 103 (34): 12663–12664. https://doi.org/
10.1073/pnas.0605449103.
Dalponte, M., Y. T. Solano-Correa, D. Marinelli, S. Liu, N. Yokoya, and D. Gianelle. 2023. “Detection of Forest
Windthrows with Bitemporal COSMO-SkyMed and Sentinel-1 SAR Data.” Remote Sensing of Environment
297:113787. https://doi.org/10.1016/j.rse.2023.113787.
Doblas, J., M. S. Reis, A. P. Belluzzo, C. B. Quadros, D. R. V. Moraes, C. A. Almeida, L. E. P. Maurano, A. F. A.
Carvalho, S. J. S. Sant’Anna, and Y. E. Shimabukuro. 2022. “DETER-R: An Operational Near-Real Time Tropical
Forest Disturbance Warning System Based on Sentinel-1 Time Series Analysis.” Remote Sensing 14 (15): 3658.
https://doi.org/10.3390/rs14153658.
Dou, P., H. Shen, Z. Li, and X. Guan. 2021. “Time Series Remote Sensing Image Classification Framework Using
Combination of Deep Learning and Multiple Classifiers System.” International Journal of Applied Earth
Observation and Geoinformation 103:102477. https://doi.org/10.1016/j.jag.2021.102477.
Gao, Riqiang, Yuankai Huo, Shunxing Bao, Yucheng Tang, Sanja L. Antic, Emily S. Epstein, Aneri B. Balar, et al. 2019.
“Distanced LSTM: Time-Distanced Gates in Long Short-Term Memory Models for Lung Cancer Detection.”
Machine Learning in Medical Imaging 11861:310–318. https://doi.org/10.1007/978-3-030-32692-0_36.
Glorot, X., A. Bordes, and Y. Bengio. 2011. “Deep Sparse Rectifier Neural Networks.” Proceedings of Machine Learning
Research 15:315–323.
He, H., J. Yan, D. Liang, Z. Sun, J. Li, and L. Wang. 2024. “Time-series Land Cover Change Detection Using Deep
Learning-Based Temporal Semantic Segmentation.” Remote Sensing of Environment 305:114101. https://doi.org/
10.1016/j.rse.2024.114101.

22 M. ZHANG ET AL.
Hethcoat, M. G., J. M. B. Carreiras, D. P. Edwards, R. G. Bryant, and S. Quegan. 2021. “Detecting Tropical Selective
Logging with C-Band SAR Data May Require a Time Series Approach.” Remote Sensing of Environment
259:112411. https://doi.org/10.1016/j.rse.2021.112411.
Hou, S., H. Shi, X. Cao, X. Zhang, and L. Jiao. 2022. “Hyperspectral Imagery Classification Based on Contrastive
Learning.” IEEE Transactions on Geoscience and Remote Sensing 60:1–13. https://doi.org/10.1109/TGRS.2021.
3139099.
Huang, Z., L. Zhong, F. Zhao, J. Wu, H. Tang, Z. Lv, B. Xu, L. Zhou, R. Sun, and R. Meng. 2023. “A Spectral-Temporal
Constrained Deep Learning Method for Tree Species Mapping of Plantation Forests Using Time Series Sentinel-2
Imagery.” ISPRS Journal of Photogrammetry and Remote Sensing 204:397–420. https://doi.org/10.1016/j.isprsjprs.
2023.09.009.
Joshi, Neha, Matthias Baumann, Andrea Ehammer, Rasmus Fensholt, Kenneth Grogan, Patrick Hostert, Martin Jepsen,
et al. 2016. “A Review of the Application of Optical and Radar Remote Sensing Data Fusion to Land use Mapping
and Monitoring.” Remote Sensing 8 (1): 70. https://doi.org/10.3390/rs8010070.
Jung, H., Y. Oh, S. Jeong, C. Lee, and T. Jeon. 2022. “Contrastive Self-supervised Learning with Smoothed
Representation for Remote Sensing.” IEEE Geoscience and Remote Sensing Letters 19:1–5. https://doi.org/10.1109/
LGRS.2021.3069799.
Knoke, T., C. Paul, E. Gosling, I. Jarisch, J. Mohr, and R. Seidl. 2023. “Assessing the Economic Resilience of Different
Management Systems to Severe Forest Disturbance.” Environmental and Resource Economics 84 (2): 343–381.
https://doi.org/10.1007/s10640-022-00719-5.
Li, H., Y. Li, G. Zhang, R. Liu, H. Huang, Q. Zhu, and C. Tao. 2022. “Global and Local Contrastive Self-supervised
Learning for Semantic Segmentation of HR Remote Sensing Images.” IEEE Transactions on Geoscience and
Remote Sensing 60:1–14. https://doi.org/10.1109/TGRS.2022.3147513.
Li, X., D. Shi, X. Diao, and H. Xu. 2022. “SCL-MLNet: Boosting Few-Shot Remote Sensing Scene Classification via Self-
supervised Contrastive Learning.” IEEE Transactions on Geoscience and Remote Sensing 60:1–12. https://doi.org/10.
1109/TGRS.2021.3109268.
Lin, T.-Y., P. Goyal, R. Girshick, K. He, and P. Dollár. 2017. “Focal Loss for Dense Object Detection.” Ieee international
conference on computer vision (ICCV), Venice, Italy, 2999-3007. Institute of Electrical and Electronics Engineers.
Linke, J., M. J. Fortin, S. Courtenay, and R. Cormier. 2017. “High-resolution Global Maps of 21st-Century Annual
Forest Loss: Independent Accuracy Assessment and Application in a Temperate Forest Region of Atlantic
Canada.” Remote Sensing of Environment 188:164–176. https://doi.org/10.1016/j.rse.2016.10.040.
Ma, L., Y. Liu, X. Zhang, Y. Ye, G. Yin, and B. A. Johnson. 2019. “Deep Learning in Remote Sensing Applications: A
Meta-analysis and Review.” ISPRS Journal of Photogrammetry and Remote Sensing 152:166–177. https://doi.org/10.
1016/j.isprsjprs.2019.04.015.
Marinelli, D., M. Dalponte, L. Frizzera, E. Naesset, and D. Gianelle. 2023. “A Method for Continuous sub-annual
Mapping of Forest Disturbances Using Optical Time Series.” Remote Sensing of Environment 299:113852. https://
doi.org/10.1016/j.rse.2023.113852.
Mitchell, A. L., A. Rosenqvist, and B. Mora. 2017. “Current Remote Sensing Approaches to Monitoring Forest
Degradation in Support of Countries Measurement, Reporting and Verification (MRV) Systems for REDD+.”
Carbon Balance and Management 12 (1): 9. https://doi.org/10.1186/s13021-017-0078-9.
Morrison, J., T. P. Higginbottom, E. Symeonakis, M. J. Jones, F. Omengo, S. L. Walker, and B. Cain. 2018. “Detecting
Vegetation Change in Response to Confining Elephants in Forests Using MODIS Time-Series and BFAST.” Remote
Sensing 10 (7): 1075. https://doi.org/10.3390/rs10071075.
Pelletier, C., G. I. Webb, and F. Petitjean. 2019. “Temporal Convolutional Neural Network for the Classification of
Satellite Image Time Series.” Remote Sensing 11 (5): 523. https://doi.org/10.3390/rs11050523.
Pérez-Cutillas, P., A. Pérez-Navarro, C. Conesa-García, D. A. Zema, and J. P. Amado-Álvarez. 2023. “What Is Going on
within Google Earth Engine? A Systematic Review and Meta-analysis.” Remote Sensing Applications: Society and
Environment 29:100907. https://doi.org/10.1016/j.rsase.2022.100907.
Schroeder, T. A., K. G. Schleeweis, G. G. Moisen, C. Toney, W. B. Cohen, E. A. Freeman, Z. Yang, and C. Huang. 2017.
“Testing a Landsat-Based Approach for Mapping Disturbance Causality in U.S. Forests.” Remote Sensing of
Environment 195:230–243. https://doi.org/10.1016/j.rse.2017.03.033.
Shimizu, K., W. Murakami, T. Furuichi, and R. C. Estoque. 2023. “Mapping Land use/Land Cover Changes and Forest
Disturbances in Vietnam Using a Landsat Temporal Segmentation Algorithm.” Remote Sensing 15 (3): 851. https://
doi.org/10.3390/rs15030851.
Slagter, B., J. Reiche, D. Marcos, A. Mullissa, E. Lossou, M. Peña-Claros, and M. Herold. 2023. “Monitoring Direct
Drivers of Small-Scale Tropical Forest Disturbance in near Real-Time with Sentinel-1 and -2 Data.” Remote
Sensing of Environment 295:113655. https://doi.org/10.1016/j.rse.2023.113655.
Stahl, A. T., R. Andrus, J. A. Hicke, A. T. Hudak, B. C. Bright, and A. J. H. Meddens. 2023. “Automated Attribution of
Forest Disturbance Types from Remote Sensing Data: A Synthesis.” Remote Sensing of Environment 285:113416.
https://doi.org/10.1016/j.rse.2022.113416.
Sun, R., F. Zhao, C. Huang, H. Huang, Z. Lu, P. Zhao, X. Ni, and R. Meng. 2023. “Integration of Deep Learning
Algorithms with a Bayesian Method for Improved Characterization of Tropical Deforestation Frontiers Using
Sentinel-1 SAR Imagery.” Remote Sensing of Environment 298:113821. https://doi.org/10.1016/j.rse.2023.113821.

INTERNATIONAL JOURNAL OF DIGITAL EARTH 23
Tang, X., E. L. Bullock, P. Olofsson, S. Estel, and C. E. Woodcock. 2019. “Near Real-Time Monitoring of Tropical Forest
Disturbance: New Algorithms and Assessment Framework.” Remote Sensing of Environment 224:202–218. https://
doi.org/10.1016/j.rse.2019.02.003.
Tarasiou, M., E. Chavez, and S. Zafeiriou. 2023. “ViTs for SITS: Vision Transformers for Satellite Image Time Series.”
2023 ieee/CVF conference on computer vision and pattern recognition (CVPR), Vancouver, BC, Canada. Institute of
Electrical and Electronics Engineers.
Vaswani, A., N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł Kaiser, and I. Polosukhin. 2017. “Attention
Is All You Need.” Proceedings of the 31st international conference on neural information processing systems, Red
Hook, NY, United States. Curran Associates Inc..
Veci, L., J. Lu, M. Foumelis, and M. Engdahl. 2017. “ESA’s Multi-mission Sentinel-1 Toolbox.” EGU General Assembly
Conference Abstracts 19:19398.
Verbesselt, J., R. Hyndman, G. Newnham, and D. Culvenor. 2010. “Detecting Trend and Seasonal Changes in Satellite
Image Time Series.” Remote Sensing of Environment 114 (1): 106–115. https://doi.org/10.1016/j.rse.2009.08.014.
Verhegghen, A., H. Eva, and F. Achard. 2015. “Assessing Forest Degradation from Selective Logging Using Time Series
of Fine Spatial Resolution Imagery in Republic of Congo.” 2015 ieee international geoscience and remote sensing
symposium (IGARSS), Milan, Italy, 2044–2047. Institute of Electrical and Electronics Engineers.
Wang, Y., C. M. Albrecht, N. A. A. Braham, L. Mou, and X. X. Zhu. 2022. “Self-supervised Learning in Remote Sensing: A
Review.” IEEE Geoscience and Remote Sensing Magazine 10 (4): 213–247. https://doi.org/10.1109/MGRS.2022.3198244.
Watanabe, M., C. N. Koyama, M. Hayashi, I. Nagatani, T. Tadono, and A. Shimada. 2021. “Refined Algorithm for
Forest Early Warning System with ALOS-2/PALSAR-2 ScanSAR Data in Tropical Forest Regions.” Remote
Sensing of Environment 265:112643. https://doi.org/10.1016/j.rse.2021.112643.
Weerakody, P. B., K. W. Wong, G. Wang, and W. Ela. 2021. “A Review of Irregular Time Series Data Handling with
Gated Recurrent Neural Networks.” Neurocomputing 441:161–178. https://doi.org/10.1016/j.neucom.2021.02.046.
Wen, Q., T. Zhou, C. Zhang, W. Chen, Z. Ma, J. Yan, and L. Sun. 2023. “Transformers in Time Series: A Survey.”
Proceedings of the thirty-second international joint conference on artificial intelligence (IJCAI), Macao, P.R.
People’s Republic of China, 6778–6786. Morgan Kaufmann.
Xu, Y., Y. Ma, and Z. Zhang. 2024. “Self-supervised pre-training for Large-Scale Crop Mapping Using Sentinel-2 Time Series.”
ISPRS Journal of Photogrammetry and Remote Sensing 207:312–325. https://doi.org/10.1016/j.isprsjprs.2023.12.005.
Yan, J., J. Liu, L. Wang, D. Liang, Q. Cao, W. Zhang, and J. Peng. 2022. “Land-cover Classification with Time-Series
Remote Sensing Images by Complete Extraction of Multiscale Timing Dependence.” IEEE Journal of Selected Topics
in Applied Earth Observations and Remote Sensing 15:1953–1967. https://doi.org/10.1109/JSTARS.2022.3150430.
Yang, B., L. Qin, J. Liu, and X. Liu. 2022. “UTRNet: An Unsupervised Time-Distance-Guided Convolutional Recurrent
Network for Change Detection in Irregularly Collected Images.” IEEE Transactions on Geoscience and Remote
Sensing 60:1–16. https://doi.org/10.1109/TGRS.2022.3174009.
Yang, X., Z. Zhang, and R. Cui. 2022. “TimeCLR: A Self-supervised Contrastive Learning Framework for Univariate
Time Series Representation.” Knowledge-Based Systems 245:108606. https://doi.org/10.1016/j.knosys.2022.108606.
Ye, S., J. Rogan, Z. Zhu, and J. R. Eastman. 2021. “A Near-Real-Time Approach for Monitoring Forest Disturbance
Using Landsat Time Series: Stochastic Continuous Change Detection.” Remote Sensing of Environment
252:112167. https://doi.org/10.1016/j.rse.2020.112167.
Yuan, Y., and L. Lin. 2021. “Self-supervised Pretraining of Transformers for Satellite Image Time Series Classification.”
IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 14:474–487. https://doi.org/10.
1109/JSTARS.2020.3036602.
Zeng, A., M. Chen, L. Zhang, and Q. Xu. 2023. “Are Transformers Effective for Time Series Forecasting?” Proceedings of
the AAAI Conference on Artificial Intelligence 37:11121–11128. https://doi.org/10.1609/aaai.v37i9.26317.
Zhang, M., D. Li, G. Li, and D. Lu. 2024. “Vegetation Classification in a Subtropical Region with Sentinel-2 Time Series
Data and Deep Learning.” Geo-spatial Information Science 28 (1): 145–163. https://doi.org/10.1080/10095020.2024.
2336604.
Zhang, R., W. Zhu, B. Fan, Q. He, J. Zhan, C. Wang, and B. Zhang. 2024. “MB-Net: A Network for Accurately
Identifying Creeping Landslides from Wrapped Interferograms.” International Journal of Applied Earth
Observation and Geoinformation 135:104300. https://doi.org/10.1016/j.jag.2024.104300.
Zhao, F., R. Sun, L. Zhong, R. Meng, C. Huang, X. Zeng, M. Wang, Y. Li, and Z. Wang. 2022. “Monthly Mapping of
Forest Harvesting Using Dense Time Series Sentinel-1 SAR Imagery and Deep Learning.” Remote Sensing of
Environment 269:112822. https://doi.org/10.1016/j.rse.2021.112822.
Zhong, L., L. Hu, and H. Zhou. 2019. “Deep Learning Based Multi-temporal Crop Classification.” Remote Sensing of
Environment 221:430–443. https://doi.org/10.1016/j.rse.2018.11.032.
Zhu, M., J. Fan, Q. Yang, and T. Chen. 2022. “SC-EADNet: A Self-supervised Contrastive Efficient Asymmetric Dilated
Network for Hyperspectral Image Classification.” IEEE Transactions on Geoscience and Remote Sensing 60:1–17.
https://doi.org/10.1109/TGRS.2021.3131152.
Zhu, Y., H. Li, Y. Liao, B. Wang, Z. Guan, H. Liu, and D. Cai. 2017. “What to Do Next: Modeling User Behaviors by
Time-LSTM.” Proceedings of the 26th international joint conference on artificial intelligence, Melbourne, Australia,
3602-3608. AAAI Press.