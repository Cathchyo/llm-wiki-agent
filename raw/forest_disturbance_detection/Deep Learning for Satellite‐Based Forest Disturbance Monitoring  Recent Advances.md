Wiley Interdisciplinary Reviews: Data Mining and
Knowledge Discovery
ADVANCED REVIEW OPEN ACCESS
Deep Learning for Satellite- Based Forest Disturbance
Monitoring: Recent Advances and Challenges
Carolina Natel1 | Christoph Molnar2 | Ricardo Dalagnol3 | Peer Nowack4
1Institute of Meteorology and Climate Research - Atmospheric Environmental Research, Karlsruhe Institute of Technology, Garmisch- Partenkirchen,
Germany | 2Independent Researcher, Munich, Germany | 3CTrees, Pasadena, California, USA | 4Institute of Theoretical Informatics, Karlsruhe Institute
of Technology, Karlsruhe, Germany
Correspondence: Carolina Natel (carolina.moura@kit.edu)
Received: 15 November 2025 | Revised: 16 April 2026 | Accepted: 19 April 2026
Chief Editor: Witold Pedrycz
ABSTRACT
Climate change and land use pressures are intensifying forest disturbances in many world regions, as reflected in the increas-
ing frequency and severity of wildfires, widespread drought- induced tree mortality, and extensive forest degradation. Hence,
spatially explicit and timely information on disturbances is essential for safeguarding the ecological integrity and societal value
of both managed and natural forest ecosystems. Satellite- based remote sensing has long been central to forest monitoring, and
recent advances in deep learning (DL) are further enhancing the extraction of information from remotely sensed data, thereby
improving the accuracy and scalability in detecting, mapping, and attributing disturbance events. Such applications range from
mapping logging activities and delineating burned areas to the complex task of classifying disturbances into different agents such
as pests, fire, and logging. Despite this progress, DL- based approaches also face significant challenges, including the demand for
large annotated training datasets and limited generalization, which might hinder their integration into operational monitoring
frameworks. Addressing these barriers will require interdisciplinary collaboration that bridges algorithmic innovation with
domain knowledge. This review synthesizes recent advances in DL- based forest disturbance research, situates them within the
broader landscape of traditional remote sensing methods, and highlights emerging innovations with the potential to overcome
current limitations. We conclude with perspectives on key research priorities for advancing the role of DL in global forest distur-
bance monitoring.
1 | Introduction sequestration, local and global climate regulation, maintenance
of the hydrological cycle, and biodiversity conservation (Thom
Forests are dynamic systems shaped by natural disturbances and Seidl 2016). Understanding and monitoring the causes, ex-
such as wildfires, storms, and insect outbreaks, which play a tent, and frequency of forest disturbances is therefore crucial for
crucial role in maintaining biodiversity, promoting ecosystem assessing their current and potential future impacts. Improved
renewal, and driving landscape heterogeneity (Seidl et al. 2017). disturbance information can guide conservation efforts, enable
However, disturbance regimes are changing at a pace unmatched timely interventions (e.g., through deforestation alerts), and fa-
in the instrumental and historical record, driven by both anthro- cilitate reporting for global commitments such as the Reduce
pogenic climate change and, increasingly, by land management Emissions from Deforestation and forest Degradation (REDD+)
(Altman et al. 2024; Seidl et al. 2017; Turner and Seidl 2023). framework, thereby informing evidence- based strategies to
This threatens not only forest ecosystem functioning, but sustain and enhance forest resilience (Kacic et al. 2023; Dixon
also the essential services forests provide—including carbon et al. 2023; Schleeweis et al. 2020).
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium,
provided the original work is properly cited.
© 2026 The Author(s). WIREs Data Mining and Knowledge Discovery published by Wiley Periodicals LLC.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026; 16:e70096 1 of 24
https://doi.org/10.1002/widm.70096

The application of remote sensing to forest monitoring has al- demonstrated to not only effectively detect disturbances (Kong
ready provided substantial information on global trends in et al. 2018), but also classify forest disturbance agents (Du
the frequency, size, and severity of forest disturbances (Senf et al. 2023) and map ecological responses such as standing dead-
and Seidl 2020; Wulder et al. 2019). However, several data and wood (Schiefer et al. 2023). Nevertheless, there is a significant
methodological challenges persist that constrain its useful- gap between the forefront of DL research and its practical use
ness at regional and global scales (Altman et al. 2024). Using in forest applications. Adapting these techniques to forest moni-
satellite imagery to detect disturbances is not a trivial task, toring requires not only extensive research, but also a concerted,
especially in the case of low- severity and very small size tree interdisciplinary effort between remote sensing, forestry and
cover changes, as the data usually contain a mix of informa- ML researchers.
tion on phenological variations, ‘real’ disturbances and noise,
which can be hard to distinguish (Du et al. 2023; Ouaknine Given the diversity of processes encompassed by the term “for-
et al. 2025). Disturbance detection is further influenced by est disturbance monitoring”, we clarify our conceptual scope in
sensor characteristics, particularly spatial and temporal resolu- Figure 1. In this review, forest disturbance refers to discrete or
tion (Hirschmugl et al. 2017). Spatial resolution determines the progressive events that disrupt the structure, composition, or
minimum detectable disturbance size and the ability to resolve functioning of forest ecosystems, thereby altering environmen-
fine- scale spatial patterns, whereas temporal resolution might tal conditions and resource availability (FAO 2004). Figure 1
influence the detectability of gradual events, or those followed distinguishes between disturbance agents, their ecological re-
by quick canopy recovery (Reiche et al. 2021). Moreover, some sponses, and long- term forest trajectories following disturbance.
forest disturbances might be concealed by the forest canopy Natural disturbance agents include biotic drivers (e.g., insect
(e.g., understory fires, selective logging) and are therefore not infestations, diseases, and animal damage) and abiotic drivers
directly visible to optical sensors, or they manifest as subtle (e.g., wildfire, windthrow, and drought), whereas anthropogenic
canopy changes that fall below detection thresholds due to spa- disturbances include activities such as legal and illegal logging
tial or temporal resolution limits (Mitchell et al. 2017). Beyond and other forest management practices. Disturbance agents
these resolution- related constraints, traditional detection algo- rarely act in isolation; most events arise from interacting drivers
rithms are becoming increasingly inadequate given both the that can amplify overall impacts (Rogers 1996). Some distur-
volume and higher resolution of satellite data now available, and bances occur abruptly, while others unfold gradually, for exam-
the increasing complexity of contemporary forest disturbances ple through multi- year tree mortality caused by water stress,
and degradation (Hirschmugl et al. 2017). Methods such as the insects, or pathogens (Perbet et al. 2024). These agents trigger
LandTrendr (Kennedy et al. 2010) are widely used for detecting ecological responses such as canopy damage or loss, defoliation,
disturbances, but they typically detect only the largest event in and tree mortality, ranging from localized, non- stand- replacing
a time series rather than multiple events, often rely on a single events to landscape- scale tree cover loss (Dalagnol et al. 2023).
vegetation index (Qiu et al. 2023), and are difficult to generalize Satellite observations primarily detect these structural or phys-
across different ecosystems without recalibration of parameters iological responses as changes in canopy condition or spectral
(Wu, Huang, et al. 2025). These limitations highlight the need signals. Over longer time scales, these responses may lead to
for more flexible and powerful approaches capable of learning different forest trajectories. Importantly, forest disturbance does
directly from data, integrating multiple sources of information, not necessarily imply ecological loss or permanent land- cover
and adapting to diverse disturbance regimes. change, as forests can recover following disturbance events.
When impacts persist but the land remains classified as forest,
Deep learning (DL), a sub- class of machine learning (ML), has the process is referred to as forest degradation, defined as a sus-
become an invaluable tool in the field of remote sensing (Ball tained reduction in structural attributes, biomass, canopy cover,
et al. 2017). The recent rapid adoption of DL methods in this or ecological function. In contrast, deforestation denotes a semi-
field has been made possible due to improvements in computing permanent or permanent conversion of forest to non- forest land
hardware (e.g., high- performance GPUs), cloud computing, and use. The definitions illustrated in Figure 1 are applied consis-
the increased availability of (preprocessed) open data, which to- tently throughout this review.
gether enable the analysis of large amounts of long- term Earth
imagery (Kattenborn et al. 2021). While DL cannot overcome By examining the recent literature on DL- based forest moni-
constraints imposed by sensor resolution, it offers several ad- toring, this study aims to identify current research gaps and
vantages over traditional methods, particularly regarding better future trends in both methods and datasets becoming avail-
use of the spatial and temporal information available in satel- able to inform the development of more effective tools for
lite datasets (Reichstein et al. 2019). A key advantage lies in monitoring forest ecosystems under changing disturbance re-
its ability to automatically learn meaningful features directly gimes. This work builds upon previous reviews that looked at
from raw data and to build hierarchical feature representations the use of DL in remote sensing (Zhu et al. 2017), and CNNs
that increase in complexity with deeper network layers, rather for vegetation remote sensing (Kattenborn et al. 2021), by both
than relying on manually engineered features (Li et al. 2018). providing a deeper focus on disturbance- related applications,
In addition, they can incorporate spatial context beyond per- and by incorporating emerging DL architectures that show
pixel analysis through architectures such as Convolutional strong potential for advancing this field. Unlike systematic
Neural Networks (CNNs) and simultaneously capture spatial reviews, this work adopts a perspective- driven approach that
and temporal dynamics using models like transformers and synthesizes recent progress in forest disturbance research
ConvLSTMs. Their applications in forest disturbance span a while drawing on DL studies to identify algorithms with po-
broad spectrum of tasks, including classification, segmenta- tential for disturbance monitoring. We focused on satellite im-
tion and object detection (Zhang et al. 2016). They have been agery with high to moderate spatial and temporal resolution
2 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FIGURE 1 | Key terms used in forest disturbance monitoring, illustrating the progression from disturbance agents to ecological responses, and
long- term forest trajectories.
(∼3–30 m, monthly to annual observations) because data at 2015. Sentinel- 2 offers 13 spectral bands ranging from 10 to 60 m
this scale is widely available from operational satellite mis- spatial resolution, and 2–5 days revisit cycles depending on the
sions and well suited for large- scale forest monitoring. This latitude, allowing more detailed characterization of vegetation
resolution range balances spatial detail with broad areal cov- status and change (Senf 2022; Drusch et al. 2012). Sentinel- 2
erage, offering up to global extent, relatively consistent data has enabled the detection of smaller scale disturbances, such
acquisition, and long- term openly accessible archives that en- as the tracking of selective logging activities, previously unde-
able retrospective analyses, despite occasional observational tectable in coarser Landsat imagery (Slagter et al. 2023; Grabska
gaps (e.g., due to cloud cover) (Md Jelas et al. 2024). To ensure et al. 2020).
reproducibility and broad applicability, we prioritized studies
using free and open datasets. In exceptional cases, studies that Beyond passive sensors, radar technology has become espe-
did not fully meet these criteria were included due to their cially relevant for regions with frequent cloud cover, such
high relevance to the topic. as the tropics, because it operates independently of sun-
light and can penetrate clouds. ESA's Sentinel- 1 Synthetic
<
Aperture Radar (SAR), for instance, with 10- m resolution,
2 | Traditional Satellite- Based Forest Disturbance supports near- real time disturbance alerts in the Congo
Monitoring Basin (Reiche et al. 2021) and monthly forest harvest map-
ping (Zhao et al. 2022). Concurrently, LiDAR technology
Satellite- based Earth Observation enables standardized, large- uses laser pulses to penetrate canopies and enables detailed
scale, and high- temporal- resolution monitoring of forest dy- measurements of canopy height, gap size, vegetation density
namics (Hislop et al. 2020), providing a powerful alternative to and three- dimensional maps of forest structure (Senf 2022).
time- specific, plot- based forest data collection (Nesha et al. 2021; LiDAR has been applied to monitoring disturbances from
Sebald et al. 2021). A major milestone in satellite- based forest hurricanes and fires, and biomass change, as well as map-
monitoring came in 2008, when the United States Geological ping biodiversity and habitat distribution (Senf 2022; St. Peter
Survey (USGS) made the entire Landsat archive freely avail- et al. 2021; Kattenborn et al. 2021). Although high acquisition
able. This global, 30- m imagery enabled for the first time the costs have historically limited coverage, LiDAR is becoming
systematic detection of long- term trends in deforestation, as well more accessible through missions such as NASA's Global
as the integration into operational forest monitoring systems, Ecosystem Dynamics Investigation (GEDI). GEDI is installed
such as the Global Forest Change (GFC) (Hansen et al. 2013; on the International Space Station (ISS) which has an equato-
Senf and Seidl 2020). Capabilities were expanded further with rial orbit that ranges from approximately 51.6 degrees north
the European Space Agency (ESA)'s Copernicus program, par- and south in latitude. While its temporal and spatial cover-
ticularly with the launch of the Sentinel- 2 satellite mission in age is limited, integrating GEDI with imagery from Landsat
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 3 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FIGURE 2 | Overview of spectral- based change detection algorithms. (A) Threshold method: disturbance detected when vegetation index drops
below predefined threshold. (B) Trajectory segmentation: piecewise linear or polynomial segmentation function identifies breakpoints. (C) Trajectory
fitting: statistical deviations from fitted model indicate disturbances.
or Sentinel- 2 enables wall- to- wall forest structure mapping threshold methods (Figure 2A), trajectory segmentation meth-
(Potapov et al. 2021; Lang et al. 2023; Burns et al. 2024). ods (Figure 2B), and time- series decomposition or trajectory fit-
Furthermore, recent and upcoming satellite missions are ting methods (Figure 2C).
expanding opportunities for biomass and canopy structure
monitoring, such as ESA's Biomass Earth Explorer mission, Threshold- based methods, such as the Vegetation Change
launched in 2025, which is expected to further improve global Tracker (VCT), use a user- defined threshold to separate real
biomass estimation by using SAR to measure tree height and changes from other spectral variations caused by factors like
volume. Together, these sensor technologies provide comple- geometric misregistration, seasonality, or changes in illumi-
mentary perspectives on forest change and structure. nation (Kennedy et al. 2007). These methods are effective
for detecting sudden, pixel- level disturbances, but they often
Translating these satellite data into useful information or bio- struggle to capture gradual changes and can be difficult to
physical quantities requires several preprocessing steps, includ- apply consistently across ecosystems, since suitable thresholds
ing radiometric, geometric and atmospheric corrections, which vary with species composition and local conditions (Huang
aim to remove sensor- and atmosphere- related noise, ensure et al. 2009; Hilker et al. 2009). Trajectory segmentation meth-
spatial consistency, and retain only reliable surface reflectance ods address some of these limitations by dividing a time series
observations (Shah et al. 2025). Following preprocessing, spec- into segments that represent periods of stability or change.
tral enhancement steps such as the calculation of vegetation They fit simple linear or polynomial models to VI data, iden-
indices (VIs), including the Normalized Difference Vegetation tifying change when the slope or residuals shift sharply be-
Index (NDVI), the Enhanced Vegetation Index (EVI) and the tween segments. A widely used approach is the LandTrendr
Normalized Burned Ratio (NBR), have long served as a cor- (Landsat- based Detection of Trends in Disturbance and
nerstone for information retrieval. These indices are computed Recovery) (Kennedy et al. 2010), which pinpoints both the
using specific spectral bands that better highlight vegetation timing and magnitude of forest disturbance and recovery.
health and condition (Senf 2022). By analyzing temporal series Time- series decomposition methods, such as BFAST (Breaks
of VIs, algorithms can detect anomalies from long- term patterns, for Additive Season and Trend), take a different approach
revealing shifts that might indicate disturbances (Pasquarella by separating long- term trends, seasonal patterns, and noise
et al. 2017). A variety of algorithms have been developed for within a signal (Verbesselt et al. 2012). When new obser-
time- series change detection based on spectral- temporal prop- vations deviate significantly from this modeled baseline, a
erties. They can be broadly categorized into three main groups: change is flagged. Related statistical models include CCDC
4 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

(Zhu and Woodcock 2014), COLD (Zhu et al. 2020), and SCCD models offer pretrained architectures that can be fine- tuned for
(Ye et al. 2021), which fit continuous or harmonic functions to forest applications under a smaller data volume; and generative
long- term satellite data. The choice of algorithm usually de- AI can synthesize or augment scarce training data.
pends on the type of disturbance. Threshold- based methods
are limited to capturing abrupt events, whereas segmentation
and decomposition methods enable superior detection of more 3.1 | Spatiotemporal Models
gradual or subtle changes (Schleeweis et al. 2020). While these
spectral- based approaches are relatively simple and require Recurrent neural networks (RNNs), particularly LSTMs, have
little reference data, they have a number of limitations. They been widely used to model long- range temporal dependencies
typically rely on a single VI, making them sensitive to sensor in environmental time series (Natel et al. 2022; Kong et al. 2018;
differences, atmospheric effects, and seasonal variation. In Schiefer et al. 2023) and have proven their reliability over time.
addition, their need for frequent, cloud- free imagery restricts However, the emergence of transformers, with their paralleliz-
their use in areas or periods with limited data availability able self- attention mechanism and superior handling of long-
(Parra and Simard 2023). term dependencies—avoiding the vanishing gradient issues
that can affect LSTMs—is rapidly surpassing LSTM- based ap-
Moreover, classification- based algorithms, including classical proaches in performance (Beck et al. 2024). In parallel, convolu-
ML models such as RFs and support vector machines (SVMs), tional architectures (LeCun and Bengio 1998) have also shown
are increasingly used. These methods can combine information comparable or superior performance in sequential tasks (Bai
from multiple sensors, spectral bands, and auxiliary data, allow- et al. 2018), while simultaneously being able to exploit spatial
ing them to capture more complex disturbance patterns under patterns. Although a range of LSTM architectures is being con-
varying environmental conditions, since these become part of stantly developed to overcome their typical limitations, such
the predictors. They also enable the detection of multiple dis- as ConvLSTM (Shi et al. 2015), xLSTM (Beck et al. 2024), and
turbance events per pixel, in contrast to many spectral- based Vision- LSTM (Alkin et al. 2024), it is expected that models that
methods that typically detect only the largest event (Viana- Soto are inherently more suitable for spatiotemporal analysis will
and Senf 2025). become more important in forest disturbance research in the
coming years.
3 | Deep Learning for Forest Disturbance CNNs have demonstrated exceptional effectiveness in seman-
Monitoring tic segmentation tasks, learning to distinguish between differ-
ent classes and objects using extensive training data (Boulila
DL has become a cornerstone in many scientific fields, owing et al. 2024). They employ convolutional kernels to exploit spatial
to its capacity to approximate highly complex, non- linear func- and temporal structure (e.g., in the case of 3D CNNs). These ker-
tions; its end- to- end learning paradigm that obviates the need for nels operate over small neighborhoods—inspired by receptive
handcrafted features; its modular architecture, which enables fields in vision—allowing the network to learn multi- pixel pat-
model customization for specific tasks; and its ability to gener- terns instead of independent weights for each feature (LeCun
ate compact internal representations (embeddings) that can be and Bengio 1998; Szegedy et al. 2016). The combination of many
transferred across tasks or fine- tuned for domain- specific ap- kernels in the depth dimension of a layer and the stacking of
plications (Molnar 2022). These methods offer particular value many such convolutional layers in a CNN architecture expands
in Earth System Science, where processes are governed by com- the receptive field and yields a hierarchy of features, from sim-
plex spatial and temporal dependencies (Reichstein et al. 2019). ple edges and textures in early layers to complex spatial ar-
Vegetation succession, disturbance, and recovery unfold across rangements in deeper ones (Szegedy et al. 2015; He et al. 2016;
scales in space and time (Foster et al. 1998), requiring models Kattenborn et al. 2021). This capacity to capture local- to- global
that can represent both short- and long- range dependencies. patterns holds particular promise for detecting subtle forest
Advanced DL architectures are specifically designed to capture changes and attributing disturbances by incorporating con-
such relationships, allowing them to learn correlations across textual information that can help classification. Among CNN-
space (e.g., neighboring pixels using CNNs or vision transform- based architectures, the U- Net (Ronneberger et al. 2015) has
ers (Dosovitskiy et al. 2020)) and time (e.g., sequences in time become particularly prominent in forest monitoring. Its en-
series with Long Short- term Memory (LSTM) (Hochreiter and coder–decoder structure combines a contracting path that ex-
Schmidhuber 1997) or transformers (Vaswani et al. 2017)) di- tracts context with an expansive path that restores resolution,
rectly from data. aided by skip connections that preserve fine details. U- Nets have
been applied to track tropical forest cover change with high ac-
In this review, we highlight advances in spatiotemporal DL curacy (Zhao et al. 2022; Dalagnol et al. 2023) and monitoring
models that integrate two- dimensional spatial maps with tem- reforestation in degraded landscapes (Andresini et al. 2024).
poral sequences, enabling modeling of dynamic forest change
processes. We also examine and discuss emerging AI para- Vision transformer architectures (Vaswani et al. 2017;
digms—including representation learning through embed- Dosovitskiy et al. 2020) also represent a major advance in
dings, foundation models, and generative AI, which might help modeling spatiotemporal data (Du et al. 2023). Earlier RNN-
advance the field by improving model generalization, scalabil- based methods were limited by sequential information flow
ity, or—following a data- centric view—simply the quality and and vanishing gradients, which constrained their ability to
quantity of training data. Embeddings can capture transfer- capture long- range dependencies and hindered paralleliza-
able representations of spectral–temporal patterns; foundation tion. While LSTMs and GRUs mitigated some of these issues
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 5 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

through gating mechanisms and memory cells, they remain across many applications, acquiring such large labeled datasets,
inherently sequential and are still susceptible to vanishing particularly for forest disturbances, remains challenging due
gradient problems due to the sequential nature of their com- to the high cost and labor- intensive nature of data annotation
putations. Transformer architectures, in contrast, allow for (Wang, Albrecht, et al. 2022). To overcome data limitation is-
efficient parallelization by employing attention mechanisms. sues, recent research has increasingly focused on weakly super-
The self- attention mechanism computes dependencies in an vised learning paradigms, which leverage unlabeled or partially
input sequence, being able to integrate information across an labeled data to enhance model performance. These approaches
entire image (Boulila et al. 2024), regardless of position, and it include self- supervised, semi- supervised, few- shot, and zero-
helps the model to learn context and long- range dependencies shot learning methods (Zhou 2018; Gui et al. 2024) (Figure 3),
by weighting the importance of each element within the input offering practical solutions for forest monitoring tasks where
sequence. Early applications of transformer architectures in labeled data are limited.
forest disturbance research demonstrate clear promise and
mark a broader shift toward models that can capture com- Self- supervised learning (SSL) and semi- supervised learning
plex spatiotemporal dependencies. Collectively, recent studies for example, leverage large amounts of unlabeled data to im-
show that self- attention models can outperform traditional prove representation learning. In SSL (Figure 3A), models are
change- detection methods (Du et al. 2023) and convolutional pretrained on unlabeled data using pretext tasks that gener-
approaches (Kaselimi et al. 2023), particularly for subtle or ate pseudo- labels automatically, before being fine- tuned on
underrepresented disturbance classes (Schiller et al. 2024; labeled datasets (Gui et al. 2024). Several SSL approaches can
Du et al. 2023). While most transformer- based applications to be employed, including generative, contrastive, and predictive
date in forest monitoring have relied only on self- attention, methods (Ziv and LeCun 2024). Generative methods learn to re-
cross- attention mechanisms also hold potential for multi- construct input data, contrastive methods learn to maximize the
modal data fusion—linking features across complementary similarity between semantically identical inputs (positive pairs),
data sources such as Sentinel- 1 SAR and Sentinel- 2 imagery while minimizing the similarity between different inputs (nega-
to improve cloud- shadow handling and disturbance detection tive pairs), and predictive methods learn to predict self- generated
(Nagrani et al. 2021). Cross- attention mechanisms can cap- labels (Wang, Albrecht, et al. 2022). The best technique to be
ture how elements in a source sequence relate to elements in used as well as the definition of the pretext task requires ex-
a target sequence. pert knowledge. After pretraining using a pretext task on large
unlabeled satellite imagery, the learned representations can be
The reviewed studies indicate a trend toward spatiotemporal fine- tuned with limited labeled data for downstream tasks such
models that are more flexible and data- efficient like transform- as disturbance detection and mapping (Kuzu et al. 2024). Semi-
ers than classical ML methods or purely statistical models. Yet, supervised approaches (Figure 3B) refer to the combination of a
challenges remain regarding transferability of these models to small amount of labeled data and a large amount of unlabeled
global scales (see Section 4.3). It is also worth mentioning that data to train models, using techniques such as generative model-
approaches that merge the strengths of different DL architec- ing, low- density separation, or graph- based propagation (Olivier
tures are a common practice in the field of ML, for example, by et al. 2006). In forest monitoring, these strategies have been ap-
integrating convolutional elements in transformer models to plied to tasks such as deforestation classification using active
enhance the overall effectiveness of vision transformers (Wu learning (Dallaqua et al. 2018) and forest fire segmentation from
et al. 2021; Zhang and Zhang 2023) and other methodological unmanned aerial vehicles (UAV) imagery, where SSL with data
advances to address computational costs and optimization of augmentation improved performance relative to classic methods
DL models. Benchmark datasets for wildfire modeling have en- despite limited labels (Wang, Fan, et al. 2022). A hybrid graph-
abled systematic comparisons of DL models of varying complex- based SSL method combined with an expert system have also
ity, with results suggesting that simpler architectures are often achieved high accuracy in vegetation mapping from Sentinel- 2
sufficient to capture fire disturbance patterns (e.g., comparing in comparison to a supervised approach (Layegh et al. 2022), and
LSTMs and ConvLSTMS, or vanilla transformers to more ad- more recently, Chen et al. (2025) proposed a semi- supervised
vanced transformer architectures) (Kondylatos et al. 2022; Di boundary segmentation network (BS- GAN) to reduce depen-
Giuseppe et al. 2025; Becker et al. 2026). This could be related dency on labeled data, achieving superior accuracy and general-
to data quality issues, in which increasing modeling complex- ization capabilities compared to existing segmentation networks
ity does not necessarily lead to performance improvements (Di for remote sensing imagery, which could help address the com-
Giuseppe et al. 2025). However, going beyond off- the- shelf DL mon scarcity of labeled data in disturbance mapping tasks.
models, and following up close DL innovations is essential to
bring the forest disturbance research up to date with state- of- the- Weakly supervised semantic segmentation (WSSS) (Figure 3D)
art AI solutions, and ultimately leading to new breakthroughs. relaxes the requirement for pixel- wise segmentation mask
labels by exploiting coarser annotations such as image- level
classification labels (e.g., only indicate presence/absence of
3.2 | Strategies for Machine Learning With an object class, not its location) (Jonnarth and Felsberg 2022).
Limited Labeled Data This is particularly relevant for forest disturbance models,
as ground observations at plot scale (e.g., National Forest
Supervised DL methods typically require large labeled datasets. Inventory point- based) usually cannot be perfectly aligned
These methods develop predictive models by training on datasets with satellite imagery, and image- level labels could be used
in which each sample is associated with a known ground- truth to train segmentation models without pixel- level annotation.
value or label. While they have achieved impressive success These approaches reduce annotation cost by using algorithms
6 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FIGURE 3 | Overview of weakly supervised learning approaches, including (A) self- supervised, (B) semi- supervised, (C) zero- shot, (D) weakly
supervised semantic segmentation, and (E) few- shot learning.
such as Class Activation Maps (CAMs) (Zhou et al. 2016), at- accurate predictions even with very limited labeled data. Metric
tention mechanisms, and multi- instance learning, to infer learning approaches, such as Siamese networks, have been par-
fine segmentation details from coarse signals. For instance, ticularly successful in forest applications. A Siamese network
CAMs can reflect the most discriminative location of an learns a distance metric (or similarity function) by process-
image, serving as pseudo- labels that guide the training of a ing pairs of inputs through identical subnetworks with shared
subsequent segmentation network (Lai et al. 2021). Several weights to produce embeddings, then computing a distance
studies demonstrate that WSSS can be a cost- effective alterna- between them (Chicco 2021). Training optimizes the network
tive for large- scale surveys where detailed (semantic) labeling to minimize the distance between embeddings of similar pairs
is impractical or unavailable (Illarionova et al. 2021; Moraes and maximize it for dissimilar pairs, often using contrastive loss
et al. 2025; Wang et al. 2020). Moreover, even when accu- functions (Hosseiny et al. 2023). For example, FSL has been ap-
rate labels are available, weak supervised learning can act as plied to detect invasive and native species in the mid- Atlantic
a form of regularization, helping to prevent the model from rainforest from UAV- based imagery (Gevaert et al. 2025), and
overfitting. image- based plant species identification with small datasets
(Figueroa- Mata and Mata- Montero 2020). Similarly, few- shot
Few- shot learning (FSL) (Figure 3E) addresses the challenge semantic segmentation has enabled cross- biome generalization,
of training with only a handful of labeled samples per class. It with models trained on tropical forests successfully adapted to
achieves this by leveraging prior knowledge from large amounts temperate forests (Puthumanaillam and Verma 2023).
of related data, learning generalizable feature representations
that can be quickly adapted to new classes from just a few ex- Zero- shot learning (ZSL) (Figure 3C) takes this one step further
amples. Using the N- way K- shot framework, a model is trained by enabling classification of categories for which no labeled ex-
to classify data across N classes (the “N- way”) using only K la- amples exist. For example, a model trained to recognize common
beled examples per class (the “K- shot”). Models are trained to tree species in a forest could identify a new, previously unseen
generalize from a small support set to a larger query set. The species based on descriptions of its characteristics, such as leaf
key idea is that the model learns to compare new examples with morphology and bark texture (Praveena et al. 2024) without
previously seen examples in a learned embedding space or to ever having been shown labeled examples of that species. This
adapt its parameters quickly through meta- learning, enabling allows the model to generalize to entirely new classes without
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 7 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FIGURE 4 | Overview of how (A) embeddings and (B) geospatial foundation models can be used in downstream tasks. Embeddings are the repre-
sentations produced by a model, that is, vectors of numbers that compress the content of an image into a machine- readable form. These can be used
as input features to downstream models. Geospatial foundation models are pretrained models that learn these representations from large- scale Earth
observation data and often output embeddings as one of their main products. They can also serve as base models for fine- tuning on downstream
tasks.
additional labeled data. ZSL methods transfer semantic knowl- information in a lower- dimensional and structured form, em-
edge through attribute- based learning or embedding spaces, beddings have the potential to supplant conventional image
linking known to unseen classes (Wang et al. 2019). composites and manually engineered features such as spectral
indices or harmonic models. This representation can enable
more accurate differentiation between disturbance classes and
3.3 | Embedding Models improve model generalization.
Embedding models (Figure 4A) can transform raw satellite im- The efficacy of embedding models for monitoring forest distur-
agery into compact, structured, and analysis- ready numerical bance critically depends on their handling of temporal dynam-
representations. These embeddings encode latent features—un- ics. Models that explicitly encode temporal information (e.g.,
derlying spatial and spectral patterns that are not directly observ- Tollefson (2025)) can be directly used as features to train su-
able in the raw data—into dense numerical vectors. Such deep pervised change detection algorithms. In this case, disturbance
features provide a powerful and flexible foundation for a wide events can be identified by quantifying the dissimilarity be-
range of downstream ML applications (Liu et al. 2025), includ- tween embedding vectors of the same location at different times.
ing similarity search, change detection, automatic clustering, This approach allows not only for the identification of changes,
and classification, often achieving high accuracy with signifi- but also the tracking of disturbance and recovery dynamics.
cantly less labeled training data. By extracting task- relevant Unsupervised clustering of embeddings, in turn, can assist in
8 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

attributing specific disturbance types. Moreover, embeddings et al. (2025) demonstrated that fine- tuning Presto in a small
can summarize patterns related to vegetation structure and dataset of tree species outperforms the classic hand- defined har-
other spatial characteristics associated with distinct disturbance monic features for classification by a large margin of up to 10%.
processes—for example, linear boundaries indicative of clearcut Similarly, FoMo- Net integrates a wide range of spectral bands
or circular burn scars typical of wildfires. and sensors to serve as a flexible backbone for global forest mon-
itoring (Bountos et al. 2025). Fine- tuning such pretrained GFMs
Recent years have seen the development of several promi- on smaller, labeled forest disturbance datasets offers a promis-
nent models, such as Clay (2025), AlphaEarth Foundations ing pathway toward developing robust and generalizable models
(Tollefson 2025), and SatCLIP (Klemmer et al. 2025). These for detecting and characterizing forest change.
models are typically trained using SSL on vast corpora of sat-
ellite imagery and other georeferenced data. A key advantage
of embeddings is that they are user- friendly, that is, they can be 3.5 | Generative Artificial Intelligence
downloaded just like remote sensing data. AlphaEarth foun-
dations for example, offers global, precomputed embeddings at Generative models that are able to produce text, images, video,
10- m resolution for the period 2017–2024, providing an imme- and other data modalities have already been incorporated
diately usable data product. This “analysis- ready” characteris- in several fields (Choi et al. 2017; Ziegler et al. 2022; Dunn
tic means they circumvent the need for extensive preprocessing et al. 2019), and recently have also been explored for ecology
of satellite images, such as atmospheric correction and cloud (Rafiq et al. 2025). These models generate new data that pre-
masking, or the precomputation of VIs. Embeddings can also be serve the statistical patterns and properties of the underlying
learned by fusing data from multiple sensors—such as Sentinel- 1 training distributions.
C- Band SAR, Sentinel- 2 and Landsat multi- spectral observa-
tions, and GEDI canopy height metrics—effectively condensing In forest monitoring, two applications are especially promising.
multi- source information into a unified, easy- to- use representa- First, data augmentation can address data scarcity by generating
tion. The recently proposed TESSERA embeddings for example, synthetic samples that complement limited real- world datasets
outperforms state- of- the- art methods across very specific forest (Hennessy et al. 2021). Generative adversarial networks (GANs)
monitoring tasks, such as estimating canopy height, mapping and diffusion models can create image- like data to represent
above- ground biomass, identifying fire scars and evaluating rare or underrepresented forest disturbance events. Second,
agroforestry stocking indices (Feng et al. 2025). large language models (LLMs), such as GPT- 4, can expand ac-
cess to unstructured forest- relevant information from sources
including research papers, news reports, and government bulle-
3.4 | Foundation Models tins. For example, Castro et al. (2024) demonstrated that GPT- 4
can identify relevant documents, extract geographical refer-
Foundation models (Figure 4B) are large- scale neural net- ences, infer coordinates, and return structured outputs from
works typically trained on multiple data modalities, such as species distribution texts. Similar approaches have been applied
text, images, and structured data, using SSL. This exposure to extract disease- report data (Gougherty and Clipp 2024) and to
to diverse datasets enhances their generalization capacity, en- retrieve information on invertebrate pests and their controllers
abling strong performance on a wide range of downstream from research abstracts (Scheepens et al. 2024) and other eco-
tasks that were not seen during training (Li et al. 2023). While logical data from written texts (Edwards et al. 2022; Scheepens
computer vision models pretrained on datasets like ImageNet et al. 2024). Applied to forest monitoring, this capacity could
(Deng et al. 2009), such as the Segment Anything Model (SAM) facilitate the acquisition of auxiliary data to enrich ML train-
(Kirillov et al. 2023), indicate potential for remote sensing appli- ing, or for instance generating weak labels for satellite images.
cations (Osco et al. 2023), geospatial foundation models (GFMs) Moreover, emerging work suggests that generative models could
extend this paradigm by leveraging vast, unlabeled remote sens- contribute to uncertainty quantification by estimating label
ing data, from individual sensors to multi- satellite archives, confidence or sampling alternative interpretations of ambigu-
to learn task- agnostic representations of the Earth's surface ous cases (Shu and Farimani 2024; Price et al. 2025), further
(Jakubik et al. 2025). This domain- specific training allows them improving the robustness of forest monitoring pipelines.
to capture the unique spectral, spatial, and temporal patterns
found in satellite imagery, leading to superior performance in
remote sensing tasks. For instance, the Prithvi GFM (Jakubik 4 | Current Forest Monitoring Challenges and
et al. 2023), trained on harmonized Landsat and Sentinel- 2 Deep Learning Opportunities
data, has demonstrated stronger generalization than special-
ized U- Net models over(fitted) on small datasets for a range of 4.1 | Detecting Disturbances of Varying Severity
Earth observation tasks (e.g., wildfire scar segmentation, multi-
temporal crop segmentation etc.). This is a rapidly evolving field, Forest disturbances span a wide gradient of severity, which largely
with many new GFMs being developed to address remote sens- determines their detectability from satellite observations. Large-
ing challenges more effectively (Smith et al. 2025; Wu, Zhang, scale, stand- replacing disturbances, such as high- severity wild-
et al. 2025; Xiao et al. 2025; Tollefson 2025). The Presto model fires, windstorms, and clear- cut harvests, are characterized by the
(Pretrained Remote Sensing Transformer) (Tseng et al. 2023), abrupt death and removal of most or all trees within a forest stand
for example, is trained on data from multiple sensors yet remains (Acil et al. 2025). These events produce strong and often persistent
lightweight enough for deployment in compute- constrained spectral signals, reliably detectable using moderate- resolution
environments while maintaining high performance. Ishikawa satellite imagery (e.g., Landsat at 30 m). Given the strength and
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 9 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

persistence of these signals, a range of methods have been success- distinguish disturbance signals from seasonal variability or noise,
fully applied to their detection. Trajectory- based methods such leading to frequent under- detection (Zhang et al. 2021), recent prog-
as LandTrendr (Kennedy et al. 2010) remain widely used, and ress in both data availability and analytical methods is beginning
classification- based approaches (e.g., RFs) offer the added ability to close this gap. In terms of data, fusing Landsat and Sentinel- 2
to identify multiple disturbance events within a single time se- imagery has been shown to increase the spatial resolution and im-
ries. More recently, DL models applied to Landsat data have been prove the accuracy of detecting smaller- scale disturbance events
shown to outperform traditional methods (Du et al. 2023; Perbet (Zhang et al. 2021). Furthermore, combining passive sensors with
et al. 2024), enabling not only the mapping of disturbance years radar data, such as Sentinel- 1 SAR, improves monitoring robust-
but also the attribution of disturbance types. ness under cloudy conditions, because radar can penetrate clouds,
offering a critical advantage (Reiche et al. 2021; Zhao et al. 2022).
At the other end of this severity gradient, detecting low- severity Commercial satellites, such as PlanetScope with imagery at 3–5 m
disturbances via remote sensing is considerably more challeng- resolution imagery, now enable for near- monthly tracking of selec-
ing. These events remove only a small fraction of trees or cause tive logging before rapid canopy recovery obscures the disturbance
gradual stress, leaving the canopy largely intact. Examples event (Reiche et al. 2021). Figure 5, which illustrates logging road
include selective logging, minor insect or disease outbreaks, expansion followed by selective logging visible as small canopy
low- intensity surface fires, or progressive tree mortality from gaps, highlights both the spatiotemporal patterns that DL models
droughts. Such disturbances produce only subtle spectral sig- can exploit and the need for high temporal resolution imagery to
nals, often smaller than the pixel size of moderate- resolution capture disturbances quickly obscured by vegetation regrowth.
satellite sensors, and may be quickly obscured by regrowth
(Dalagnol et al. 2023). Persistent cloud cover in tropical regions DL pipelines applied to high- resolution Norway's International
further complicates monitoring. Although low- severity distur- Climate and Forests Initiative (NICFI) satellite data have suc-
bances are relatively small, they are important because their cessfully mapped both rapid and subtle land cover changes across
effects accumulate over time, influencing forest structure, bio- Brazil at 3–5 m resolution (Wagner et al. 2023). Additionally, U-
diversity, and the balance of carbon sinks and sources. Early Net architectures trained on PlanetScope imagery (4.22 m) have
detection also helps track ecosystem health and supports timely proven effective for identifying and attributing specific distur-
management actions, such as adaptive measures aimed at main- bance drivers, including logging, fire, and road development
taining the forest's carbon sink potential (Ferretto et al. 2025). (Dalagnol et al. 2023). Sentinel- 2's 10 m imagery has also been
shown to detect illegal logging without the need for manually
A large body of research has been conducted in an attempt to derived VIs when paired with DL methods (Schiller et al. 2024).
map selective logging and other small- scale disturbances (Asner
et al. 2010; Matricardi et al. 2007, 2020; Shimabukuro et al. 2014). Table 1 synthesizes how disturbance at different severity trans-
While conventional approaches that rely on VIs struggle to late into data and modeling requirements. For high- severity
FIGURE 5 | Monthly PlanetScope imagery (3 m spatial resolution) showing logging road expansion in January, February, March, followed by
selective logging in September and October, and rapid canopy closure in November. Circles indicate canopy openings after logging in October, and
canopy closure within 1 or 2 months in November. Source: Figure from Reiche et al. (2021), https:// doi. org/ 10. 1088/ 1748- 9326/ abd0a8. Licensed un-
der CC BY 4.0: https://c reati vecom mons.o rg/l icens es/b y/4.0 /.
10 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 19424795, 2026, 2, Downloaded from https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096 by Readcube-Labtiva, Wiley Online Library on [15/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     |     |     |     | selbairav etamilC − |  rof lartcepsrepyH − |
| --- | --- | --- | --- | --- | ------------------- | -------------------- |
/atad yrallicnA
|     |  yduolc rof RAS − |     |              |  noitategev dna |                 |              |
| --- | ----------------- | --- | ------------ | --------------- | --------------- | ------------ |
|     | sepyt atad        |     |  RADiL/RAS − |                 | erutsiom lioS − |              |
|     |                   |     |  erutxet rof |                 |                 | sserts tnalp |
erutcurts
snoiger
.seitinutroppo LD dna atad dna skcenelttob tnerruc ,stnemeriuqer noituloser atad ,serutangis lartceps rieht ,ytireves yb segnellahc noitceted ecnabrutsid tserof fo yrammuS    |    1 ELBAT
 laropmet dna txetnoc
/seitinutroppo LD
|     |   -itlum rof sledom |                    |  laitaps rof sledom |     |                             |  dna sremrofsnart |
| --- | ------------------- | ------------------ | ------------------- | --- | --------------------------- | ----------------- |
|     | serutcetihcra       |  emit ni noitceted |                     |     |                             |                   |
|     |  laropmetoitapS −   |  ssalc dna tneve   |  laropmetoitapS −   |     |  laropmetoitapS −           |                   |
|     |                     |                    |                     |     | noitatnemges  ,.g.e( sledom | )sMTSLvnoC        |
 rof teN -U −
gnikcart
seires
 ni tneve tsegral ylnO −
|                 |                                                |                                    |     |  noitarapes tluciffiD − |  noitarapes tluciffiD − |     |
| --------------- | ---------------------------------------------- | ---------------------------------- | --- | ----------------------- | ----------------------- | --- |
|  dohtem tnerruC |                                                |  elgnis no ecnaileR −              |     |                         |                         |     |
|                 | skcenelttob  erutpac tonnaC − stneve tnerrucer | xedni noitategev  ecnabrutsid oN − |     | /ygolonehp morf         | /ygolonehp morf         |     |
 lexip -bus rooP −
|     |     | seires emit | noitubirtta |     |     |     |
| --- | --- | ----------- | ----------- | --- | --- | --- |
ytivitisnes
|     |     |     |     | esion |     | esion |
| --- | --- | --- | --- | ----- | --- | ----- |
 laropmeT
|     | launnA |     | ylhtnoM |     | ylhtnoM |     |
| --- | ------ | --- | ------- | --- | ------- | --- |
.ser
|     |     |     | )m 01 < ,.g.e( hgiH |     | )m 01 < ,.g.e( hgiH |     |
| --- | --- | --- | ------------------- | --- | ------------------- | --- |
.ser laitapS
 etaredoM )m 03 ,.g.e(
egnahc lartceps gnortS −
|     | erutangis epacsdnal |                      | spag yponac lexip -buS − |     |     |                       |
| --- | ------------------- | -------------------- | ------------------------ | --- | --- | --------------------- |
|     |                     | sehctap suougitnoC − |                          |     |     | enilced evissergorP − |
 dna lartcepS
 eltbuSyrtemoeg  yponac laudarG −
|     |  yponac tpurbA − |     |  noitarud -trohS − |     | egnahc lartceps | snrettap yhctaP − |
| --- | ---------------- | --- | ------------------ | --- | --------------- | ----------------- |
noitarolocsid
 ralugerrI −
sgninepo
lavomer
 ,mrotsdniW
|          |             |                      |                    |     |  ,thguorD |  ,noitatsefni |
| -------- | ----------- | -------------------- | ------------------ | --- | --------- | ------------- |
|  lacipyT |  tuc -raelc |  ,tsevrah erif egral |  evitceleS gniggol |     |           | negohtap      |
|          | stnega      |                      |                    |     |  tcesni   |               |
scitsiretcarahc tnevE
|     |     |     | etercsid elacs -llamS |     | laudarg elacs -llamS |     |
| --- | --- | --- | --------------------- | --- | -------------------- | --- |
gnicalper -dnats
/elacs -egraL
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 11 of 24

 19424795, 2026, 2, Downloaded from https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096 by Readcube-Labtiva, Wiley Online Library on [15/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
disturbances, increasing model complexity often yields limited  There are, however, several attribution challenges. In Table 2,
additional benefit, as the signal is already strong and well cap- we summarize these open challenges, highlighting current bot-
tured by existing methods. By contrast, detecting low- severity  tlenecks in data and methods, and describe how DL and emerg-
disturbances requires both finer spatial resolution and higher  ing AI approaches can help address them.
temporal sampling to resolve sub- pixel canopy openings and
short- lived signals. Moreover, such data improvements alone are
insufficient. Fully exploiting these data requires DL models that  4.2.1   |   Separation of Disturbance Agents
can capture spatial context and temporal persistence, particu-
larly for disturbances that unfold more gradually over time such  Different disturbance agents can produce highly similar spec-
as selective logging and from droughts. tral and landscape signatures in satellite imagery, making at-
tribution inherently difficult. Automated approaches relying
on a single spectral index tend to produce higher omission and
4.2   |   Attributing Forest Disturbances commission errors. To address this, studies have explored in-
tegrating temporal, landscape, and topographic features into
Attributing disturbances in forest monitoring involves identi- classification models (Li et al. 2022), alongside incorporating
fying and assigning causal agents to observed changes in eco- multiple spectral bands and indices to improve disturbance at-
systems. These agents may be natural, such as wind- throws,  tribution. Additional auxiliary variables, such as tree species oc-
wildfires, or pathogen outbreaks, or anthropogenic, such as tim- currence, may further enhance the classification of disturbance
ber harvests. Understanding why disturbances occur and what  agents (Schroeder et al. 2017). Nevertheless, fine- scale attribu-
their effects are is crucial for supporting targeted management  tion of small- scale disturbances such as wind, stress classes,
responses and policy development that target the resilience of  and bark beetle damage remains difficult (Sebald et al. 2021;
forests and their sustained ecosystem services. Schroeder et al. 2017).
TABLE 2    |    Summary of key challenges in forest disturbance attribution from remote sensing, including current methodological bottlenecks and
emerging deep learning opportunities.
|           |             | Current data and   | Data strategies and  |
| --------- | ----------- | ------------------ | -------------------- |
| Challenge | Description | method bottlenecks | DL opportunities     |
Separation of disturbance agents − Similar spectral/ − Heavy reliance on spectral  − Multi- modal DL fusion
|     | structural signatures    | indices                        | (optical, SAR, LiDAR,  |
| --- | ------------------------ | ------------------------------ | ---------------------- |
|     | across agents            | − Limited discrimination of    | hyperspectral)         |
|     | − Difficult attribution  | agents with similar spectral/  | − Attention- based     |
|     | from imagery alone       | landscape signatures           | models                 |
|     |                          | − Limited radar/hyperspectral  | − Spatial–temporal     |
|     |                          | integration                    | models                 |
− Embeddings
− Integration of ancillary
environmental data
Standardization in disturbance agent  − Inconsistent schemes  − No harmonized taxonomy − Domain adaptation/
classification schemes across studies/ − Incompatible label schemes transfer learning
|     | regions          | − Varying spatial resolutions | − Weakly supervised  |
| --- | ---------------- | ----------------------------- | -------------------- |
|     | − Limited        | − Lack of global reference    | learning             |
|     | comparability    | datasets                      | − Ontology matching/ |
|     | between datasets |                               | label harmonization  |
Resource-i ntensive labeling − Field surveys  − Expensive manual  − Active learning for
|     | required for training/  | interpretation               | sample prioritization |
| --- | ----------------------- | ---------------------------- | --------------------- |
|     | validation              | − Spatial bias toward        | − Self-s upervised    |
|     | − High collection cost  | accessible areas             | learning              |
|     | and effort              | − Rare agents                | − Synthetic data      |
|     |                         | underrepresented             | generation            |
|     |                         | − Spatial/temporal mismatch  | − Citizen science/    |
|     |                         | in field data                | pseudo-l abeling      |
Compound and novel disturbance  − Single- agent  − Single dominant- agent  − Temporal models
types assumptions often  labeling and modeling − Multi-l abel
|     | invalid | − Poor representation of       | classification      |
| --- | ------- | ------------------------------ | ------------------- |
|     |         | interacting drivers            | − Causal inference  |
|     |         | − Limited disturbance history  | frameworks          |
in ground truth
12 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026

A promising direction is the combination of high- resolution et al. 2023). Similarly, the construction of roads in the middle of
imagery with spatiotemporal DL models that enable fine- scale forests, followed by forest gaps, might indicate logging activities
attribution by capturing spatial cues that might help distinguish because these roads are used for timber transport. Conversely,
between different disturbance types. Figure 6 illustrates spatial burned rings point to disturbance by fire (Figure 6C), with dif-
patterns in imagery that these models can exploit. For instance, ferent reflectances indicating different times of the disturbance.
patterns such as the presence of trails, log decks, and gaps are
usually associated with degradation by logging (Figure 6A) More broadly, spatial configuration offers valuable informa-
and provide contextual cues that U- Net architectures can use tion for attribution. Harvesting events are often characterized
to differentiate logging from other disturbance types (Dalagnol by regular geometric shapes associated with commodity- driven
FIGURE 6 | Spatial cues in remote sensing imagery that support spatiotemporal deep learning models for forest disturbance segmentation and
attribution. The figure illustrates key spatial patterns associated with: (A) degradation from logging (e.g., trails, log decks, canopy gaps), (B) logging-
road expansion followed by selective logging, this panel also illustrates phenomena variability, in which the same disturbance type can manifest with
markedly different spatial signatures in different regions—from the regular geometric patterns in A (Mato Grosso, Brazil) to the diffuse patches of
selective logging visible in the June 2019 image (Acre, Brazil), and (C) fire impacts at different stages of regeneration, including characteristic burn
rings. Source: Planet NICFI imagery with 4.77 m resolution.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 13 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

deforestation or managed forestry operations. In contrast, natu- temporal mismatches. Active learning can help prioritize high-
ral disturbances tend to produce irregularly shaped patches, such value sampling locations, while self- supervised learning allows
as those resulting from wind throws or insect outbreaks. These models to leverage large volumes of unlabeled satellite time se-
spatial characteristics can be modeled using spatiotemporal DL, ries. Synthetic data generation, citizen science integration, and
which can also track gradual canopy loss from insect or drought pseudo- labeling from existing disturbance maps offer further
stress (Gnilke and Sanders 2022). However, it is important to avenues to reduce dependence on costly field campaigns.
note that region- specific practices can complicate attribution.
In the Brazilian Amazon, trails with tree- fall gaps and nearby
logging decks serve as recognizable spatial cues (Dalagnol 4.2.4 | Interacting and Compound Disturbances
et al. 2023), however, these patterns may not transfer to other
tropical regions as shown in Figure 6A,B. Distinguishing legal Disturbances increasingly occur as interacting or cascading
from illegal harvesting is another challenge. Sometimes, attri- events, in which agents occur sequentially or concurrently
bution is based on the presence of sharp, structured boundaries, and produce combined effects that cannot be attributed to a
which are assumed to indicate legal clear- cuts. However, low- single agent (Kleinman et al. 2019). Such interactions involve
impact or selective logging, though legal, can be misclassified both amplifying and dampening feedback, resulting in distur-
as either natural disturbances or illegal logging because of the bance responses that differ fundamentally from isolated events
similar spatial patterns (Dalagnol et al. 2023). (Krawchuk et al. 2020). For example, insect- induced changes in
fuel structure can either increase or decrease fire burn sever-
Refining the attribution of forest disturbances will require a ity depending on outbreak timing and characteristics (Meigs
dual focus: the development and adoption of high- quality ref- et al. 2016), and salvage logging may reduce fuel loads and
erence datasets, and the application of advanced DL algorithms lower fire intensity, though effects vary with management prac-
capable of leveraging both spatial patterns and temporal dynam- tices (Kleinman et al. 2019). These cascading processes blur
ics. However progress in this field remains constrained by the the boundaries between conventional disturbance categories,
availability of labeled training data. Large, standardized data- as observed changes often reflect the combined influence of
sets covering diverse disturbance types are scarce (Schleeweis multiple interacting drivers. Traditional classification frame-
et al. 2020), and the lack of consistent labeling standards contin- works, which typically assume a single dominant causal agent,
ues to limit comparability across regions (see also Section 5.4). are therefore poorly suited to capturing such dynamics, and
While emerging data- efficient DL paradigms (Section 3.2) can training datasets rarely capture disturbance histories or causal
help reduce the dependence on large labeled datasets, they chains. Temporal models that track disturbance progression and
should be understood as complementary tools that improve data recovery, multi- label classification for compound events, and
efficiency rather than substitutes for sustained efforts to expand the integration of ancillary datasets (e.g., logging permits, road
and standardize high- quality labeled reference data. networks) can help address these limitations. Incorporating
landscape context and disturbance history into DL frameworks
provides models with information on preconditioning factors
4.2.2 | Standardization in Disturbance Agent that shape subsequent disturbance responses. Causal inference
Classification Schemes approaches offer a complementary pathway by explicitly testing
the direction and magnitude of causal relationships and distin-
There is currently no homogenization in how disturbance agents guishing direct from indirect effects, they enable more robust
are classified and reported (Hislop et al. 2020). Some datasets inference about underlying drivers even when multiple distur-
apply broad categorical schemes such as “biotic vs. abiotic”, as bances co- occur (Schroeder et al. 2017). When combined with
in the FAO or Montreal Process frameworks (Process 2015), spatiotemporal DL, causal models can constrain predictions to
while others distinguish more detailed agents such as fire, har- ecologically plausible pathways and reduce spurious associa-
vest, uprooting, and breakage (Senf et al. 2020). These divergent tions driven by confounding factors.
classification systems hinder comparability across studies and
regions and often fail to capture compound or novel disturbance
types. To address this, domain adaptation and transfer learning 4.3 | Building Models That Can Generalize Across
can be used to align models trained under different classifica- World Regions
tion schemes, while weakly supervised learning and ontology
matching offer pathways to harmonize heterogeneous or par- Novel, scalable methods are required to transform the ever-
tially labeled datasets. increasing amount of raw satellite data into actionable knowl-
edge for global forest monitoring applications. However,
scaling DL approaches from local studies to global forest
4.2.3 | Limited Labeled Data monitoring remains a major model generalization challenge.
This issue is associated with the training data distribution,
Disturbance attribution often relies on ground- based field sur- which typically only covers a specific geographic location,
veys to both label datasets for ML training and validate mod- species composition, sensor, and/or spatial scale (Ouaknine
els. Acquiring such data is typically resource- intensive and et al. 2025). Models trained on limited or biased forest data
spatially constrained, limiting applicability for large- scale tend to perform poorly on data that differs from that used
analyses. Field plots are often biased toward accessible areas, during training. This data- centric challenge is compounded
rare disturbance agents are underrepresented, and geolocating by a methodological legacy. Much progress in change detec-
field observations to pixel- level imagery introduces spatial and tion has historically been built on statistical models, and this
14 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

legacy continues to shape how domain scientists design and annotations. Higher label quality can be attained through expert
validate DL models, commonly applying models to small re- interpretations, the implementation of confidence levels based
gions and using only a small set of data. Under a data- hungry on the consensus among annotators, and the exclusion of sam-
DL modeling paradigm, this hinders achieving maximum ples with low confidence from the final training dataset.
potential. For instance, studies have successfully applied DL
with high accuracy for deforestation detection in specific con- In parallel to costly manual interpretation of imagery, two
texts, such as the Brazilian Amazon (Bragagnolo et al. 2021) complementary data streams have also emerged as a valuable
or Germany (Schiller et al. 2024). However, these models are approach for large- scale geospatial data collection and bench-
typically validated within a single geographic setting, raising mark dataset creation, (a) citizen science, and (b) unstructured
concerns about their broader transferability. A model trained textual data sources. Citizen science is a term used to describe
for tropical forests is unlikely to perform well in boreal or tem- scientific research conducted with active participation from
perate contexts without retraining, and generalization even to members of the general public, who are often nonprofessional
new areas within the same biome but in a different country volunteers. Citizen science has been used, for instance, to moni-
is not guaranteed (Schiller et al. 2024). Furthermore, many tor tropical deforestation, in which volunteers analyze and clas-
studies focus narrowly on a single disturbance agent, further sify remote sensing images (da Luz et al. 2014), and the labeled
limiting broad applicability (Du et al. 2023). data has been further integrated into ML classifiers (Dallaqua
et al. 2019). Unstructured textual information constitutes a sec-
To help overcome these generalization barriers, large- scale and ond emerging source of complementary data. LLMs can facil-
globally representative benchmarks such as the ForTy dataset itate the extraction of relevant disturbance information from
(Jiang and Neumann 2025) for forest types are emerging as im- scientific publications, news reports, government bulletins, and
portant resources. By providing diverse training data across re- other text corpora. Such information can be used either to match
gions and forest types, these initiatives offer a pathway toward geographically referenced disturbance descriptions to unlabeled
building models that are not only locally accurate but also ro- satellite imagery, thereby generating weak labels at the image
bust and generalizable for global forest monitoring and a range level, or to augment input features with georeferenced ecolog-
of targets. The use of additional spatial encoding and context ical or socioeconomic variables that enrich the training data.
characterizing location- specific features, as well as GFMs fine- Together, these approaches may substantially improve the effi-
tuned to various downstream applications, seems particularly ciency of satellite- data annotation and ultimately provide more
promising routes forward to learn more effectively across wide- informative inputs for model development.
ranging Earth observational datasets (see also Section 3.4).
To make significant progress in the development of more gener-
alizable models capable of scaling to diverse geographic regions
5 | Practical Guidance and Future Outlook and forest types, it is imperative that researchers adopt open sci-
ence and FAIR (Findable, Accessible, Interoperable, Reusable)
This section provides practitioners with practical advice by sum- data principles (Wilkinson et al. 2016) when generating and cu-
marizing the lessons learned from the reviewed studies and out- rating training datasets. Making data openly accessible under
lining future research directions for advancing DL- based forest clear licenses in FAIR repositories will allow the broader sci-
monitoring using Earth observations. entific community to build upon existing efforts, increase the
diversity and volume of training data available, and reduce
redundant efforts. It is equally important to develop common
5.1 | Training Data Generation and Curation standards for data labeling. This will ensure that disturbance
types and class definitions are harmonized across studies.
The effectiveness of DL applications depends critically on high- The adoption of more homogeneous and hierarchical labeling
quality labeled training data, which remains a major bottleneck schemes would facilitate the merging or comparison of datasets
in forest disturbance applications. A multi- step approach for cre- at various levels of detail on shared classification levels. This en-
ating reference data to train and validate models is described in hancement would significantly improve the interoperability and
Du et al. (2023). First, an initial land cover mask is used to con- long- term value of the datasets.
strain the sampling domain (e.g., forest vs. non- forest). Within
forests, sampling points are then randomly generated, while
maintaining a minimum spatial separation between points to 5.2 | DL- Based Forest Monitoring Workflow
reduce spatial autocorrelation. Each sample then undergoes
manual interpretation with the aid of high- resolution imagery A typical workflow for supervised DL in forest disturbance
and spectral time series for that point to classify its historical monitoring is presented in Figure 7. The first step is defining the
status, including the timing and causal agent of any change prediction task, such as a binary (e.g., disturbed vs. undisturbed)
events. In order to create reusable and relevant datasets, it is or multi- class classification (e.g., distinguishing disturbance
recommended that attention be paid to selecting appropriate agents). Satellite image time series are then acquired, typically
classes. This is necessary to avoid ambiguous or overly broad from multispectral sensors such as Landsat and Sentinel- 2,
classes that cannot be reused in further studies. For instance, radar systems such as Sentinel- 1, or through a combination of
it is preferable to label “beetle attack” instead of a generic “bi- multiple sensors, often accessed via centralized platforms such
otic disturbance” (see also Section 5.4). Digital platforms such as as Google Earth Engine (Gorelick et al. 2017). Next, data prepro-
Collect Earth Online (Saah et al. 2019) can be used to streamline cessing steps are performed. Although recent work suggests that
the process of data labeling, thereby enhancing the efficacy of self- attention and recurrent architectures can outperform CNNs
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 15 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

FIGURE 7 | Conceptual workflow for supervised deep learning in forest disturbance monitoring. Steps within dashed rectangles are optional.
when trained directly on raw satellite time- series (i.e., with- optical imagery to capture forest mortality patterns (Agersborg
out precomputing VIs) (Rußwurm and Körner 2020; Schiller et al. 2022) or integrating GEDI LiDAR with Landsat time se-
et al. 2024), preprocessing steps such as atmospheric correction ries to expand canopy change data to the global scale (Lang
and automated cloud filtering remain a standard practice in the et al. 2023). Data fusion enriches the spectral and structural in-
field (Du et al. 2023; Dalagnol et al. 2023; Schiller et al. 2024), formation available to DL models while mitigating challenges
and continue to play an important role in improving DL model such as cloud contamination, sensor failure, and seasonal data
performance (Rußwurm and Körner 2020). Nonetheless, fea- gaps (Du et al. 2023). Recent missions such as BIOMASS and
ture engineering can still be beneficial when training data are NISAR will further expand the available data, particularly im-
scarce or when simpler/shallower network architectures are portant to address challenges related to estimating logging in-
used. To mitigate limited sample sizes, data augmentation tech- tensities and carbon losses.
niques such as cropping, rotation, flipping, or noise injection are
widely employed (Chen et al. 2023). In addition, exploring gener- After data preparation, DL models are trained and evaluated to
ative AI to synthesize training samples, and weakly supervised estimate their expected performance on unseen data. Recent
learning to improve model performance under limited reference literature highlights the advantages of fine- tuning GFMs for
data represent promising research directions. The inclusion of downstream tasks, rather than training task- specific models
ancillary variables as input features, such as topography (e.g., from scratch, particularly due to the small data volume on forest
slope, elevation), forest type, or socioeconomic indicators, may disturbances. Following model training, rigorous evaluation is
provide additional contextual information that purely spectral essential to avoid misleading conclusions. In geospatial appli-
inputs may lack, potentially improving disturbance attribution, cations, the design- based approach by Olofsson et al. (2014) is
and overall model performance and transferability. However, widely recommended, advocating probability- based sampling to
their added value remain under- investigated. Furthermore, in- obtain an independent test set and thus more reliable accuracy
corporating precomputed embeddings offers an additional ave- estimates than random data splits. Standard reporting includes
nue for capturing spatiotemporal dependencies and enhancing overall accuracy, precision, recall, F1- score, and area under the
model generalization across scales, or simply achieving higher ROC curve, along with user's and producer's accuracy, area es-
performance even when using a small volume of training data. timates, and uncertainty intervals. Because forest disturbances
Finally, following advances in other fields (Allen et al. 2025), are often rare, class imbalance must be explicitly addressed.
integrating complementary remote sensing modalities is ex- Accuracy alone can be misleading if a model predicts “no dis-
pected to become increasingly important in forest monitoring turbance” for all pixels in a dataset with only 1% disturbed area.
workflows. Multispectral data provide rich spectral informa- In such cases, metrics sensitive to minority classes, such as the
tion on vegetation condition, radar offers structural and all- F1- score or class- weighted measures, should be preferred. The
weather sensitivity, and LiDAR contributes three- dimensional choice of metrics depends on the application's tolerance for er-
canopy metrics. Recent studies have demonstrated the advan- rors—for instance, high recall may be prioritized for early defor-
tages of multi- modal fusion, for example, combining SAR and estation alerts to minimize false negatives, while high precision
16 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

may be more relevant for stable forest monitoring to avoid false fanciest model, we recommend starting with the state- of-
alarms. the art model for a targeted task, for instance using simpler
spatiotemporal models rather than the latest developed
Spatial autocorrelation introduces an additional challenge in model (e.g., a “vanilla” transformer before a Temporal
DL model validation. If training and test samples are spatially Fusion Transformer (Lim et al. 2021)).
dependent, model performance may be systematically over-
4. Leverage model feedback during annotation: False pos-
estimated. To mitigate this bias, approaches such as spatial
itives and false negatives often reveal annotation errors.
blocking, distance buffers, or spatial cross- validation are recom-
Active learning approaches—iteratively refining training
mended (Roberts et al. 2017; Brenning 2023; Ploton et al. 2020).
data with model feedback—can substantially improve
The optimal validation design depends on the prediction goal—
accuracy.
whether retrospective mapping or forecasting—and should be
selected carefully. When using k- fold cross- validation, hyperpa- 5. Adopt a phased approach to model deployment: Begin with
rameter tuning must be performed within each fold to prevent local detection, then scale spatially, and finally extend tem-
data leakage, a detail often neglected in performance reporting. porally while monitoring error accumulation and retrain-
Comprehensive evaluation should also assess model plausibility ing needs. A practical workflow involves three stages: (i)
and interpretability, and these aspects are increasingly exam- ensuring the model can detect the target disturbance lo-
ined (Natel et al. 2025; Becker et al. 2026). Ecological valida- cally, (ii) scaling inference to the full study area while re-
tion, for example, by verifying that predicted spatial patterns ducing false positives by incorporating additional training
and feature importance align with known disturbance pro- labels for disturbance- absent conditions, and (iii) extend-
cesses and biophysical principles, strengthens model credibil- ing the model temporally to evaluate whether the rate of
ity (Steger et al. 2015). For a sustainable operational use, active false positives remains acceptable or requires retraining.
learning and feedback mechanisms should be implemented to
maintain model accuracy and ensure that performance meets
operational requirements. Finally, transparent communication 5.4 | Benchmarks, Standardization
of uncertainty is essential. Probabilistic outputs, entropy maps, and Reproducibility
bootstrapping, or conformal prediction methods can be used
to quantify and visualize uncertainty, helping end users un- Large- scale and spatially explicit databases of forest distur-
derstand the confidence and limitations associated with model bances will become essential to train and evaluate global- scale
predictions. DL models that perform well across environmental settings
and forest types. Standardizing annotation protocols, data for-
mats, and evaluation metrics reduces methodological variabil-
5.3 | Lessons for Practitioners ity and facilitates objective comparisons between studies and
algorithms. Well- curated benchmarks also alleviate redundant
From the reviewed applications, several overarching lessons preprocessing, allowing researchers to focus on algorithmic in-
emerged for building robust and generalizable DL- based forest novation rather than data harmonization. Furthermore, they
disturbance models, which are summarized below: allow the recognition of persistent challenges—such as distin-
guishing subtle or overlapping disturbances and generalizing
1. Training data availability is critical: DL models are data- across biomes—that remain obscured when models are trained
hungry. Before investing in complex architectures, prac- on localized datasets.
titioners should evaluate whether sufficient labeled data
exist at the desired spatial and temporal resolution. For For Earth observation products such as Landsat, model evaluation
example, dividing the study area by patch size helps esti- often relies on two major disturbance benchmarks—LandTrendr
mate whether hundreds to thousands of training patches and Global Forest Change (GFC) (Kennedy et al. 2010; Hansen
can be obtained. If such data are unavailable and unfea- et al. 2013; Du et al. 2023). More recent benchmark datasets for
sible to create, simpler pixel- based models may be more forest disturbances include the global forest disturbance data-
appropriate. To compensate for small data volume, the use set (GFD) (Wang et al. 2025), which includes 11 disturbance
of embeddings (Section 3.3), learning under limited data types, the European Forest Disturbance Atlas (Viana- Soto and
strategies (Section 3.2), and pretrained models or GFMs Senf 2025), including disturbance agent and disturbance sever-
(Section 3.4) could be explored. ity, and the Tropical Moist Forest dataset (TMF) (Vancutsem
et al. 2021). At national and regional scales, initiatives such
2. Minimal feature engineering is often sufficient: Unlike
as Brazil's DETER, SIMEX, and MapBiomas Fire complement
classical ML approaches such as RFs, DL models can learn
these global datasets, alongside various disturbance- specific
feature representations directly from imagery, instead of
datasets such as for winds (Forzieri et al. 2020). However, the
relying for instance on precomputed VIs. A promising av-
lack of unified disturbance definitions, harmonized spatial–
enue is including embeddings as features in the training temporal resolutions, and transparent labeling standards limits
process. Basic preprocessing steps like cloud masking or
comparability across these datasets. Lessons from other remote
temporal interpolation still remain important though.
sensing domains—such as BigEarthNet (Sumbul et al. 2021),
3. The best model is not always the fanciest: More complex Sen12MS (Schmitt et al. 2019), Sen4AgriNet (Sykas et al. 2021),
architectures do not guarantee success. More important is and CropHarvest (Tseng et al. 2021)—exemplify the role of
a clear understanding of the ecological target and the avail- comprehensive benchmarks in driving advances in model-
ability of well- curated training data. Before jumping to the ing development. Emerging efforts such as FORTY (Jiang and
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 17 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Neumann 2025), which is a benchmark dataset for forest type, wider range of forest- related changes, impacts, and potential ac-
and FoMo (Bountos et al. 2025), which compiles several data- tions to enhance forest resilience—for example, susceptibility to
sets to build a foundation model, serve as a robust resource for disturbances such as spruce bark beetle outbreaks, windthrow,
training and evaluating ML models and could be expanded for and root rot (Lämås et al. 2023). However, the reviewed meth-
forest disturbance research. Another promising example is the ods presented in this paper do not automatically translate into
deadtrees.earth initiative (Mosig et al. 2026), which is an open useful tools to practitioners, which often require accessible and
access community effort to share labeled aerial and satellite interpretable tools rather than raw model outputs. Bridging the
data on tree mortality to help ensure robust training data for ML gap between research prototypes and operational applications
models. Efforts of this kind, combining high- resolution imagery, requires not only methodological advances but also participa-
consistent labeling, and global geographic coverage, represent tory design involving end users (Xu and Jiang 2025). Engaging
an important example for future initiatives aimed at advancing forestry agencies, conservation organizations, and local com-
spatiotemporal monitoring of forest disturbances. munities ensures that models address real- world needs—from
timber harvest oversight to carbon credit verification—and
Additionally, reproducibility continues to pose a significant chal- can be embedded within established management systems
lenge. According to Paulino et al. (2024), fewer than 10% of for- (Paulino et al. 2024). Furthermore, explainable AI (xAI) tech-
est disturbance detection studies currently share their datasets niques can strengthen user trust by clarifying how DL models
publicly, which severely limits external validation and cumu- reach their conclusions, thereby supporting informed decision-
lative progress. To address this, the community must converge making. Therefore, we highlight that much progress in trans-
toward FAIR- compliant data- sharing standards. Implementing lating scientific DL models into operational monitoring systems
interoperable metadata frameworks, shared ontologies, and will be required. Further research should emphasize usability,
consistent disturbance taxonomies would enable reproducible transparency, and integration within existing decision- support
workflows and ultimately accelerate the pace of methodologi- workflows. Interactive web platforms that combine DL- based
cal advances. Developing a web- based platform that facilitates disturbance maps with ancillary data—such as topography, ref-
external data contributions to curate open access databases in a erence imagery, and uncertainty layers—illustrate this principle
consistent form, for example by accepting labeled data uploads by enabling users to validate, interpret, and act upon model out-
according to certain common standards, would be a promising puts. Finally, consistent and transparent guidelines for assess-
path forward (Fassnacht et al. 2024). ing and communicating map accuracy remain essential, as both
producers and users must be able to evaluate and convey the re-
liability of derived products (Olofsson et al. 2014).
5.5 | From Scientific Models to Practitioner Tools
Estimating the extent of forest disturbances and identifying their 6 | Conclusion
agents are fundamental to monitoring forest change. These tasks
inform decision- making in forest management, risk assessment, The rapid expansion of satellite Earth observation has created
policy development, and carbon accounting aimed at reducing unprecedented opportunities for automated and scalable ap-
greenhouse gas emissions. Recent studies emphasize the need proaches to forest monitoring. Despite growing interest in DL,
for improved quantification of disturbances and uncertainties, current research has yet to fully leverage its capabilities to de-
including the integration of novel large- scale and long- term velop models that are both generalizable and effective at detect-
datasets on ecosystem disturbances, to enhance global carbon ing low- severity disturbances and attributing them to specific
cycle models (Forkel et al. 2019; Pugh et al. 2019). Disturbances causal agents.
remain one of the least certain components of the global for-
est carbon cycle. Moreover, over recent decades, various forest In this review, we have examined AI and DL opportunities for
management paradigms have emerged—such as sustainable forest disturbance monitoring, while also highlighting key lim-
timber management, multiple- use forestry, ecosystem manage- itations and challenges that practitioners must be aware of when
ment, sustainable forest management, and climate- smart for- building and validating these systems. Although state- of- the- art
estry. Forest management practices altering forest composition, models have achieved notable success in segmenting disturbance
for instance, can significantly influence carbon turnover rates areas and analyzing temporal patterns through spatiotemporal
(Ferretto et al. 2025), yet their effects remain poorly documented methods, the field remains constrained by a predominant focus
due to limited supporting data. on localized, single- disturbance studies, often restricted to a few
disturbance agents, and by reliance on data- rich regions. These
Decision Support Systems (DSS)—computer- based platforms limitations significantly reduce model transferability across di-
that integrate data with modeling and analytical tools—have long verse forest ecosystems and disturbance types. We have identi-
supported forest managers, but most address very narrow, well- fied three primary technical avenues with promise to address
defined problems. Looking ahead, DSS must evolve into more limitations regarding disturbance detection, attribution, and the
general, multifunctional systems capable of tackling emerging scarcity of training data: (a) spatiotemporal architectures, (b)
disturbance regimes driven by the combined effects of climate embeddings and GFMs, and (c) learning approaches designed
change, forest management practices, and the growing demand for limited labeled data.
for multiple forest ecosystem services. The increasing availabil-
ity of high- resolution data combined with advanced DL methods Moreover, the path forward requires a shift in research direction
presents an opportunity to make these systems more valuable toward large- scale, multi- disturbance models. Several critical
for forest owners and managers by helping them understand a gaps must be addressed to achieve this goal. First, the field needs
18 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

standardized benchmark datasets that encompass a variety of Altman, J., P. Fibich, V. Trotsiuk, and N. Altmanova. 2024. “Global
disturbance agents across different ecosystems. To complement Pattern of Forest Disturbances and Its Shift Under Climate Change.”
Science of the Total Environment 915: 170117.
current efforts, citizen science and LLMs could be explored to
expand ground- truth data collection. Second, approaches such Andresini, G., A. Appice, and D. Malerba. 2024. “A Deep Semantic
as SSL should be explored to mitigate data scarcity in underrep- Segmentation Approach to Map Forest Tree Dieback in Sentinel- 2
resented regions. Third, closer collaboration between DL experts Data.” IEEE Journal of Selected Topics in Applied Earth Observations
and Remote Sensing 17: 17075–17086. https:// doi. org/ 10. 1109/ JSTARS.
and remote sensing and forest researchers is essential to develop
2024.3 460981.
algorithms capable of handling the complex data characteristics
of forest disturbances. Finally, the forest monitoring research Asner, G. P., S. R. Loarie, and U. Heyder. 2010. “Combined Effects
of Climate and Land- Use Change on the Future of Humid Tropical
community is urged to prioritize a transparent, FAIR- compliant
Forests.” Conservation Letters 3, no. 6: 395–403.
data sharing that will not only accelerate scientific progress but
also foster the development of generalizable DL models that can Bai, S., J. Z. Kolter, and V. Koltun. 2018. “An Empirical Evaluation
of Generic Convolutional and Recurrent Networks for Sequence
effectively support global forest monitoring goals.
Modeling.” arXiv Preprint arXiv:1803.01271.
These developments are particularly critical given the growing Ball, J. E., D. T. Anderson, and C. S. Chan. 2017. “Comprehensive
impacts of climate and land- use change on global forests, where Survey of Deep Learning in Remote Sensing: Theories, Tools, and
Challenges for the Community.” Journal of Applied Remote Sensing
understanding disturbance regimes is vital for maintaining car-
11, no. 4: 42609.
bon sequestration capacity and other forest ecosystem services.
Beck, M., K. Pöppel, M. Spanring, et al. 2024. “Xlstm: Extended Long
Short- Term Memory.” Advances in Neural Information Processing
Systems 37: 107547–107603.
Author Contributions
Becker, P., C. N. de Moura, and P. J. Nowack. 2026. “Assessing and
Christoph Molnar: writing – review and editing. Peer Nowack: writ- Explaining Temporal Deep Learning Models for Wildfire Danger
ing – review and editing. Ricardo Dalagnol: writing – review and ed- Prediction.” In Assessing and Explaining Temporal Deep Learning
iting. Carolina Natel: conceptualization, writing – review and editing, Models for Wildfire Danger Prediction, vol. 2, 15014. Machine Learning:
writing – original draft, investigation. Earth.
Boulila, W., H. Ghandorh, S. Masood, et al. 2024. “A Transformer- Based
Acknowledgments Approach Empowered by a Self- Attention Technique for Semantic
Segmentation in Remote Sensing.” Heliyon 10, no. 8: e29396.
The authors thank Professor Dr. Almut Arneth for valuable comments
provided in the first draft of this manuscript. The Planet NICFI data Bountos, N. I., A. Ouaknine, I. Papoutsis, and D. Rolnick. 2025.
used in Figure 7 were accessed through Level- 2 partnership with “Fomo: Multi- Modal, Multi- Scale and Multi- Task Remote Sensing
the NICFI program. Open Access funding enabled and organized by Foundation Models for Forest Monitoring.” In Proceedings of the
Projekt DEAL. AAAI Conference on Artificial Intelligence, vol. 39, 27858–27868.
AAAI.
Funding Bragagnolo, L., R. V. Da Silva, and J. M. V. Grzybowski. 2021. “Amazon
Forest Cover Change Mapping Based on Semantic Segmentation by
C.N. acknowledges the support by the Karlsruhe Institute of Technology
U- Nets.” Ecological Informatics 62: 101279. https:// doi. org/ 10. 1016/j.
through the Young Investigator Group Preparation Program.
ecoinf. 2021. 101279.
Brenning, A. 2023. “Spatial Machine- Learning Model Diagnostics: A
Conflicts of Interest
Model- Agnostic Distance- Based Approach.” International Journal of
The authors declare no conflicts of interest. Geographical Information Science 37, no. 3: 584–606.
Burns, P., C. R. Hakkenberg, and S. J. Goetz. 2024. “Multi- Resolution
Data Availability Statement Gridded Maps of Vegetation Structure From Gedi.” Scientific Data 11,
no. 1: 881.
Data sharing not applicable to this article as no datasets were generated
or analysed during the current study. Castro, A., J. Pinto, L. Reino, P. Pipek, and C. Capinha. 2024. “Large
Language Models Overcome the Challenges of Unstructured Text Data
in Ecology.” Ecological Informatics 82: 102742.
References
Chen, L., W. Jing, Y. Xie, E. Chen, and X. Zhang. 2023. “Discriminative
Acil, N., J. P. Sadler, C. Senf, S. Suvanto, and T. A. M. Pugh. 2025. Feature Constraints via Supervised Contrastive Learning for Few-
“Landscape Patterns in Stand- Replacing Disturbances Across the Shot Forest Tree Species Classification Using Airborne Hyperspectral
World's Forests.” Nature Sustainability 8, no. 1: 86–98. Images.” Remote Sensing of Environment 295: 113710. https:// doi. org/ 10.
1016/j. rse. 2023. 113710.
Agersborg, J. A., L. T. Luppino, S. N. Anfinsen, and J. U. Jepsen. 2022.
“Toward Targeted Change Detection With Heterogeneous Remote Chen, Y., Z. Yang, L. Zhang, and W. Cai. 2025. “A Semi- Supervised
Sensing Images for Forest Mortality Mapping.” Canadian Journal of Boundary Segmentation Network for Remote Sensing Images.”
Remote Sensing 48, no. 6: 826–848. https:// doi. org/ 10. 1080/ 07038 992. Scientific Reports 15: 2007. https://d oi.o rg/1 0.1 038/s 41598 -0 25-
2022.2 135497. 85125- 9 .
Alkin, B., M. Beck, K. Pöppel, S. Hochreiter, and J. Brandstetter. 2024. Chicco, D. 2021. “Siamese Neural Networks: An Overview.” Artificial
“Vision- Lstm: Xlstm as Generic Vision Backbone.” arXiv Preprint Neural Networks. Methods in Molecular Biology, edited by H. Cartwright,
arXiv:2406.04303. vol. 2190, 73–94. Humana.
Allen, A., S. Markou, W. Tebbutt, et al. 2025. “End- To- End Data- Driven Choi, E., S. Biswal, B. Malin, J. Duke, W. F. Stewart, and J. Sun. 2017.
Weather Prediction.” Nature 641, no. 8065: 1172–1179. “Generating Multi- Label Discrete Patient Records Using Generative
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 19 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Adversarial Networks.” In Machine Learning for Healthcare Conference, Forkel, M., M. Drüke, M. Thurner, et al. 2019. “Constraining Modelled
286–305. PMLR. Global Vegetation Dynamics and Carbon Turnover Using Multiple
Satellite Observations.” Scientific Reports 9, no. 1: 18757.
Clay. Clay- foundation/model. 2025. “Clay Foundation.” https:// github.
com/ Clay- found ation/ model. Forzieri, G., M. Pecchi, M. Girardello, et al. 2020. “A Spatially Explicit
Database of Wind Disturbances in European Forests Over the Period
da Luz, E. F. P., R. S. Felipe, D. L. Correa, F. G. González, and F. M.
2000–2018.” Earth System Science Data 12, no. 1: 257–276.
Ramos. 2014. “The Forestwatchers: A Citizen Cyberscience Project for
Deforestation Monitoring in the Tropics.” Human Computation 1, no. Foster, D. R., D. H. Knight, and J. F. Franklin. 1998. “Landscape Patterns
2: 137–145. and Legacies Resulting From Large, Infrequent Forest Disturbances.”
Ecosystems 1, no. 6: 497–510.
Dalagnol, R., F. H. Wagner, L. S. Galvão, et al. 2023. “Mapping Tropical
Forest Degradation With Deep Learning and Planet Nicfi Data.” Remote Gevaert, C. M., A. A. Pedro, K. Ou, et al. 2025. “Explainable Few- Shot
Sensing of Environment 298: 113798. Learning Workflow for Detecting Invasive and Exotic Tree Species.”
Scientific Reports 15: 23238.
Dallaqua, F. B. J. R., F. A. Faria, and A. L. Fazenda. 2018. “Active
Learning Approaches for Deforested Area Classification.” In 2018 31st Gnilke, A., and T. G. M. Sanders. 2022. “Distinguishing Abrupt and
SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI), Gradual Forest Disturbances With Modis- Based Phenological Anomaly
48–55. IEEE. https:// doi. org/ 10. 1109/ SIBGR API. 2018. 00013 . Series.” Frontiers in Plant Science 13: 863116.
Dallaqua, F. B. J. R., Á. L. Fazenda, and F. A. Faria. 2019. “Foresteyes Gorelick, N., M. Hancher, M. Dixon, S. Ilyushchenko, D. Thau, and
Project: Can Citizen Scientists Help Rainforests?” In 2019 15th R. Moore. 2017. “Google Earth Engine: Planetary- Scale Geospatial
International Conference on eScience (eScience), 18–27. IEEE. Analysis for Everyone.” Remote Sensing of Environment 202: 18–27.
Deng, J., W. Dong, R. Socher, L.- J. Li, K. Li, and L. Fei- Fei. 2009.
Gougherty, A. V., and H. L. Clipp. 2024. “Testing the Reliability of an
“Imagenet: A Large- Scale Hierarchical Image Database.” In 2009
AI- Based Large Language Model to Extract Ecological Information
IEEE Conference on Computer Vision and Pattern Recognition, 248–
From the Scientific Literature.” npj Biodiversity 3: 13.
255. Ieee.
Grabska, E., P. Hawryło, and J. Socha. 2020. “Continuous Detection
Di Giuseppe, F., J. McNorton, A. Lombardi, and F. Wetterhall.
of Small- Scale Changes in Scots Pine Dominated Stands Using Dense
2025. “Global Data- Driven Prediction of Fire Activity.” Nature
Sentinel- 2 Time Series.” Remote Sensing 12, no. 8: 1298.
Communications 16, no. 1: 2918.
Gui, J., T. Chen, J. Zhang, et al. 2024. “A Survey on Self- Supervised
Dixon, D. J., Y. Zhu, C. F. Brown, and Y. Jin. 2023. “Satellite Detection Learning: Algorithms, Applications, and Future Trends.” IEEE
of Canopy- Scale Tree Mortality and Survival From California Wildfires
Transactions on Pattern Analysis and Machine Intelligence 46, no. 12:
With Spatio- Temporal Deep Learning.” Remote Sensing of Environment
9052–9071.
298: 113842. https:// doi. org/ 10. 1016/j. rse. 2023. 113842.
Hansen, M. C., P. V. Potapov, R. Moore, et al. 2013. “High- Resolution
Dosovitskiy, A., L. Beyer, A. Kolesnikov, et al. 2020. “An Image Is Global Maps of 21st- Century Forest Cover Change.” Science 342, no.
Worth 16 × 16 Words: Transformers for Image Recognition at Scale.” In
6160: 850–853. https:// doi. org/ 10. 1126/ scien ce. 1244693. International Conference on Learning Representations (ICLR).
He, K., X. Zhang, S. Ren, and J. Sun. 2016. “Deep Residual Learning for
Drusch, M., U. Del Bello, S. Carlier, et al. 2012. “Sentinel- 2: ESA'S
Image Recognition.” In Proceedings of the IEEE Conference on Computer
Optical High- Resolution Mission for GMES Operational Services.”
Vision and Pattern Recognition, 770–778. IEEE.
Remote Sensing of Environment 120: 25–36. https:// doi. org/ 10. 1016/j.
rse. 2011. 11. 026. Hennessy, A., K. Clarke, and M. Lewis. 2021. “Generative Adversarial
Network Synthesis of Hyperspectral Vegetation Data.” Remote Sensing
Du, B., Z. Yuan, Y. Bo, and Y. Zhang. 2023. “A Combined Deep Learning
13, no. 12: 2243.
and Prior Knowledge Constraint Approach for Large- Scale Forest
Disturbance Detection Using Time Series Remote Sensing Data.” Hilker, T., M. A. Wulder, N. C. Coops, et al. 2009. “A New Data
Remote Sensing 15, no. 12: 2963. Fusion Model for High Spatial- and Temporal- Resolution Mapping of
Forest Disturbance Based on Landsat and Modis.” Remote Sensing of
Dunn, K. W., F. Chichen, D. J. Ho, et al. 2019. “Deepsynth: Three-
Environment 113, no. 8: 1613–1627.
Dimensional Nuclear Segmentation of Biological Images Using Neural
Networks Trained With Synthetic Data.” Scientific Reports 9: 18295. Hirschmugl, M., H. Gallaun, M. Dees, et al. 2017. “Methods for Mapping
Forest Disturbance and Degradation From Optical Earth Observation
Edwards, T., C. B. Jones, and P. Corcoran. 2022. “Identifying Wildlife
Data: A Review.” Current Forestry Reports 3, no. 1: 32–45.
Observations on Twitter.” Ecological Informatics 67: 101500.
FAO. 2004. “Global Forest Resources Assessment Update 2005: Terms Hislop, S., A. Haywood, S. Jones, M. Soto- Berelov, A. Skidmore, and
and Definitions.” T. H. Nguyen. 2020. “A Satellite Data Driven Approach to Monitoring
and Reporting Fire Disturbance and Recovery Across Boreal and
Fassnacht, F. E., J. C. White, M. A. Wulder, and E. Næsset. 2024. Temperate Forests.” International Journal of Applied Earth Observation
“Remote Sensing in Forestry: Current Challenges, Considerations and and Geoinformation 87: 102034.
Directions.” Forestry: An International Journal of Forest Research 97, no.
1: 11–37. Hochreiter, S., and J. Schmidhuber. 1997. “Long Short- Term Memory.”
Neural Computation 9, no. 8: 1735–1780.
Feng, Z., C. Atzberger, S. Jaffer, et al. 2025. “Tessera: Precomputed Fair
Global Pixel Embeddings for Earth Representation and Analysis.” arXiv Hosseiny, B., M. Mahdianpari, M. Hemati, A. Radman, F.
Preprint arXiv:2506.20380. Mohammadimanesh, and J. Chanussot. 2023. “Beyond Supervised
Learning in Remote Sensing: A Systematic Review of Deep Learning
Ferretto, A., P. Anthoni, T. A. M. Pugh, et al. 2025. “The Impact of
Approaches.” IEEE Journal of Selected Topics in Applied Earth
Changing Forest Composition in Europe- Longest Carbon Turnover Observations and Remote Sensing 17: 1035–1052.
Time in Unmanaged and Broadleaved Deciduous Forests.” PLoS One
20, no. 10: e0334118. Huang, C., S. N. Goward, K. Schleeweis, N. Thomas, J. G. Masek, and Z.
Zhu. 2009. “Dynamics of National Forests Assessed Using the Landsat
Figueroa- Mata, G., and E. Mata- Montero. 2020. “Using a Convolutional
Record: Case Studies in Eastern United States.” Remote Sensing of
Siamese Network for Image- Based Plant Species Identification With
Environment 113, no. 7: 1430–1442.
Small Datasets.” Biomimetics 5, no. 1: 8.
20 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Illarionova, S., A. Trekin, V. Ignatiev, and I. Oseledets. 2021. “Tree Kong, Y.- L., Q. Huang, C. Wang, J. Chen, J. Chen, and D. He. 2018.
Species Mapping on Sentinel- 2 Satellite Imagery With Weakly “Long Short- Term Memory Neural Networks for Online Disturbance
Supervised Classification and Object- Wise Sampling.” Forests 12, no. Detection in Satellite Image Time Series.” Remote Sensing 10, no. 3:
10: 1413. 452.
Ishikawa, T., C. Bonannella, B. J. W. Lerink, and M. Rußwurm. Krawchuk, M. A., G. W. Meigs, J. M. Cartwright, et al. 2020. “Disturbance
2025. “Deep Pre- Trained Time Series Features for Tree Species Refugia Within Mosaics of Forest Fire, Drought, and Insect Outbreaks.”
Classification in the Dutch Forest Inventory.” arXiv preprint Frontiers in Ecology and the Environment 18, no. 5: 235–244.
arXiv:2508.18829.
Kuzu, R. S., O. Antropov, M. Molinier, C. O. Dumitru, S. Saha, and X.
Jakubik, J., R. Sujit, C. E. Phillips, et al. 2023. “Foundation Models X. Zhu. 2024. “Forest Disturbance Detection via Self- Supervised and
for Generalist Geospatial Artificial Intelligence.” arXiv preprint Transfer Learning With Sentinel- 1&2 Images.” IEEE Journal of Selected
arXiv:2310.18660. Topics in Applied Earth Observations and Remote Sensing 17: 4751–4767.
Jakubik, J., F. Yang, B. Blumenstiel, et al. 2025. “Terramind: Large- Lai, L., J. Chen, H. Huang, and W. Qingyao. 2021. “Exploring a Cam-
Scale Generative Multimodality for Earth Observation.” arXiv Preprint Based Approach for Weakly Supervised Fire Detection Task.” In 2021
arXiv:2504.11171. IEEE International Conference on e- Business Engineering (ICEBE), 134–
138. IEEE.
Jelas, I. M., M. A. Zulkifley, M. Abdullah, and M. Spraggon. 2024.
“Deforestation Detection Using Deep Learning- Based Semantic Lämås, T., L. Saengstuvall, K. Öhman, et al. 2023. “The Multi-
Segmentation Techniques: A Systematic Review.” Frontiers in Forests Faceted Swedish Heureka Forest Decision Support System: Context,
and Global Change 7: 1300060. https://d oi.o rg/1 0.3 389/f fgc.2 024. Functionality, Design, and 10 Years Experiences of Its Use.” Frontiers in
1300060. Forests and Global Change 6: 1163105.
Jiang, Y., and M. Neumann. 2025. “Not Every Tree Is a Forest: Lang, N., W. Jetz, K. Schindler, and J. D. Wegner. 2023. “A High-
Benchmarking Forest Types From Satellite Remote Sensing.” In Resolution Canopy Height Model of the Earth.” Nature Ecology &
International Geoscience and Remote Sensing Symposium—IGARSS, Evolution 7, no. 11: 1778–1789.
vol. 2025. IGARSS.
Layegh, N. F., R. Darvishzadeh, A. K. Skidmore, C. Persello, and N.
Jonnarth, A., and M. Felsberg. 2022. “Importance Sampling Cams Krüger. 2022. “Integrating Semi- Supervised Learning With an Expert
for Weakly- Supervised Segmentation.” In ICASSP 2022–2022 IEEE System for Vegetation Cover Classification Using Sentinel- 2 and
International Conference on Acoustics, Speech and Signal Processing RapidEye Data.” Remote Sensing 14, no. 15: 3605. https:// doi. org/ 10.
(ICASSP), 2639–2643. IEEE. 3390/ rs141 53605.
Kacic, P., F. Thonfeld, U. Gessner, and C. Kuenzer. 2023. “Forest LeCun, Y., and Y. Bengio. 1998. “Convolutional Networks for Images,
Structure Characterization in Germany: Novel Products and Analysis Speech, and Time Series.” In The Handbook of Brain Theory and Neural
Based on GEDI, Sentinel- 1 and Sentinel- 2 Data.” Remote Sensing 15, no. Networks, edited by M. A. Arbib. MIT Press.
8: 1969. https:// doi. org/ 10. 3390/ rs150 81969 . Li, W., H. Lee, S. Wang, C.- Y. Hsu, and S. T. Arundel. 2023. “Assessment
Kaselimi, M., A. Voulodimos, I. Daskalopoulos, N. Doulamis, and of a New Geoai Foundation Model for Flood Inundation Mapping.” In
A. Doulamis. 2023. “A Vision Transformer Model for Convolution- Proceedings of the 6th ACM SIGSPATIAL International Workshop on AI
Free Multilabel Classification of Satellite Imagery in Deforestation for Geographic Knowledge Discovery, 102–109. ACM.
Monitoring.” IEEE Transactions on Neural Networks and Learning Li, Y., X. Xiao, W. Zhenzi, H. Fan, X. Tong, and J. Liu. 2022. “A Forest
Systems 34, no. 7: 3299–3307. https:// doi. org/ 10. 1109/ TNNLS. 2022. Type- Specific Threshold Method for Improving Forest Disturbance
3144791. and Agent Attribution Mapping.” GIScience & Remote Sensing 59, no.
Kattenborn, T., J. Leitloff, F. Schiefer, and S. Hinz. 2021. “Review on 1: 1624–1642.
Convolutional Neural Networks (CNN) in Vegetation Remote Sensing.” Li, Y., H. Zhang, X. Xue, Y. Jiang, and Q. Shen. 2018. “Deep Learning for
ISPRS Journal of Photogrammetry and Remote Sensing 173: 24–49. Remote Sensing Image Classification: A Survey.” Wiley Interdisciplinary
https:// doi. org/ 10. 1016/j. isprs jprs. 2020. 12. 010. Reviews: Data Mining and Knowledge Discovery 8, no. 6: e1264.
Kennedy, R. E., W. B. Cohen, and T. A. Schroeder. 2007. “Trajectory- Lim, B., S. Ö. Arık, N. Loeff, and T. Pfister. 2021. “Temporal Fusion
Based Change Detection for Automated Characterization of Forest Transformers for Interpretable Multi- Horizon Time Series Forecasting.”
Disturbance Dynamics.” Remote Sensing of Environment 110, no. 3: International Journal of Forecasting 37, no. 4: 1748–1764.
370–386.
Liu, Y., X. Wang, Y. Wang, et al. 2025. “Representation Learning for
Kennedy, R. E., Z. Yang, and W. B. Cohen. 2010. “Detecting Trends in Geospatial Data.” Annals of GIS 31, no. 4: 557–583.
Forest Disturbance and Recovery Using Yearly Landsat Time Series: 1.
Matricardi, E. A. T., D. L. Skole, M. A. Cochrane, M. Pedlowski, and
Landtrendr—Temporal Segmentation Algorithms.” Remote Sensing of
W. Chomentowski. 2007. “Multi- Temporal Assessment of Selective
Environment 114, no. 12: 2897–2910.
Logging in the Brazilian Amazon Using Landsat Data.” International
Kirillov, A., E. Mintun, N. Ravi, et al. 2023. “Segment Anything.” In Journal of Remote Sensing 28, no. 1: 63–82.
Proceedings of the IEEE/CVF International Conference on Computer
Matricardi, E. A. T., D. L. Skole, O. B. Costa, M. A. Pedlowski, J. H.
Vision, 4015–4026. IEEE.
Samek, and E. P. Miguel. 2020. “Long- Term Forest Degradation
Kleinman, J. S., J. D. Goode, A. C. Fries, and J. L. Hart. 2019. “Ecological Surpasses Deforestation in the Brazilian Amazon.” Science 369, no.
Consequences of Compound Disturbances in Forest Ecosystems: A 6509: 1378–1382.
Systematic Review.” Ecosphere 10, no. 11: e02962.
Meigs, G. W., H. S. J. Zald, J. L. Campbell, W. S. Keeton, and R. E.
Klemmer, K., E. Rolf, C. Robinson, L. Mackey, and M. Rußwurm. 2025. Kennedy. 2016. “Do Insect Outbreaks Reduce the Severity of Subsequent
“Satclip: Global, General- Purpose Location Embeddings With Satellite Forest Fires?” Environmental Research Letters 11, no. 4: 045008.
Imagery.” Proceedings of the AAAI Conference on Artificial Intelligence
Mitchell, A. L., A. Rosenqvist, and B. Mora. 2017. “Current Remote
39: 4347–4355.
Sensing Approaches to Monitoring Forest Degradation in Support of
Kondylatos, S., I. Prapas, M. Ronco, et al. 2022. “Wildfire Danger Countries Measurement, Reporting and Verification (MRV) Systems for
Prediction and Understanding With Deep Learning.” Geophysical REDD+.” Carbon Balance and Management 12: 1–22. https:// doi. org/ 10.
Research Letters 49: e2022GL099368. 1186/ s1302 1- 017- 0078- 9.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 21 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Molnar, C. 2022. Modeling Mindset: The Many Cultures of Learning Ploton, P., F. Mortier, M. Réjou- Méchain, et al. 2020. “Spatial Validation
From Data. Independently published. Reveals Poor Predictive Performance of Large- Scale Ecological
Mapping Models.” Nature Communications 11, no. 1: 4540.
Montréal Process. 2015. “The Montréal Process Criteria and Indicators
for the Conservation and Sustainable Management of Temperate and Potapov, P., X. Li, A. Hernandez- Serna, et al. 2021. “Mapping Global
Boreal Forests. Montreal Process Liaison Office.” In A Framework to Forest Canopy Height Through Integration of GEDI and Landsat Data.”
Diagnose Barriers to Climate Change Adaptation, edited by S. Moser and Remote Sensing of Environment 253: 112165. https:// doi. org/ 10. 1016/j.
J. Ekstrom, vol. 107, 22026–22031. Proceedings of the National Academy rse.2 020.1 12165.
of Sciences of the United States of America. https:// www. montr ealpro.
Praveena, K., R. J. Anandhi, S. Gupta, A. Jain, A. Kumar, and A. M.
Moraes, D., M. L. Campagnolo, and M. Caetano. 2025. “A Weakly Saud. 2024. “Application of Zero- Shot Learning in Computer Vision
Supervised and Self- Supervised Learning Approach for Semantic for Biodiversity Conservation Through Species Identification and
Segmentation of Land Cover in Satellite Images With National Forest Tracking.” In 2024 International Conference on Trends in Quantum
Inventory Data.” Remote Sensing 17(4):711: 711. Computing and Emerging Business Technologies, 1–6. IEEE. https:// doi.
org/1 0.1 109/T QCEBT 59414.2 024.1 0545030.
Mosig, C., J. Vajna- Jehle, M. D. Mahecha, et al. 2026. “Deadtrees.
Earth—An Open- Access and Interactive Database for Centimeter- Scale Price, I., A. Sanchez- Gonzalez, F. Alet, et al. 2025. “Probabilistic
Aerial Imagery to Uncover Global Tree Mortality Dynamics.” Remote Weather Forecasting With Machine Learning.” Nature 637, no. 8044:
Sensing of Environment 332: 115027. 84–90.
Nagrani, A., S. Yang, A. Arnab, A. Jansen, C. Schmid, and C. Sun. 2021. Pugh, T. A. M., M. Lindeskog, B. Smith, et al. 2019. “Role of Forest
“Attention Bottlenecks for Multimodal Fusion.” Advances in Neural Regrowth in Global Carbon Sink Dynamics.” Proceedings of the
Information Processing Systems 34: 14200–14213. National Academy of Sciences 116, no. 10: 4382–4387.
Natel, C., D. M. Belda, P. Anthoni, N. Haß, S. Rabin, and A. Arneth. Puthumanaillam, G., and U. Verma. 2023. “Texture Based Prototypical
2025. “Emulating Grid- Based Forest Carbon Dynamics Using Machine Network for Few- Shot Semantic Segmentation of Forest Cover:
Learning: An Lpj- Guess v4. 1.1 Application.” Geoscientific Model Generalizing for Different Geographical Regions.” Neurocomputing
Development 18, no. 14: 4317–4333. 538: 126201. https:// doi. org/ 10. 1016/j. neucom. 2023. 03. 062.
Natel, C., J. S. de Moura, and D. H. M. Detzel. 2022. “Evaluating the Qiu, D., Y. Liang, R. Shang, and J. M. Chen. 2023. “Improving
Long Short- Term Memory (Lstm) Network for Discharge Prediction Landtrendr Forest Disturbance Mapping in China Using Multi-
Under Changing Climate Conditions.” Hydrology Research 53, no. 5: Season Observations and Multispectral Indices.” Remote Sensing 15,
657–667. no. 9: 2381.
Nesha, K., M. Herold, V. De Sy, et al. 2021. “An Assessment of Data Rafiq, K., S. Beery, M. S. Palmer, Z. Harchaoui, and B. Abrahms. 2025.
Sources, Data Quality and Changes in National Forest Monitoring “Generative Ai as a Tool to Accelerate the Field of Ecology.” Nature
Capacities in the Global Forest Resources Assessment 2005–2020.” Ecology & Evolution 9, no. 3: 378–385.
Environmental Research Letters 16, no. 5: 54029. https:// doi. org/ 10. 1088/ Reiche, J., A. Mullissa, B. Slagter, et al. 2021. “Forest Disturbance Alerts
1748- 9326/ abd81b. for the Congo Basin Using Sentinel- 1.” Environmental Research Letters
Olivier, C., S. Bernhard, and Z. Alexander. 2006. “A Discussion of Semi- 16, no. 2: 024005.
Supervised Learning and Transduction.” In Semi-S upervised Learning, Reichstein, M., G. Camps- Valls, B. Stevens, et al. 2019. “Deep Learning
edited by O. Chapelle, B. Scholkopf, and A. Zien, 473–478. MIT Press. and Process Understanding for Data- Driven Earth System Science.”
https:// doi. org/ 10. 7551/ mitpr ess/ 97802 62033 589. 003. 0025. Nature 566, no. 7743: 195–204.
Olofsson, P., G. M. Foody, M. Herold, S. V. Stehman, C. E. Woodcock, Roberts, D. R., V. Bahn, S. Ciuti, et al. 2017. “Cross- Validation Strategies
and M. A. Wulder. 2014. “Good Practices for Estimating Area and for Data With Temporal, Spatial, Hierarchical, or Phylogenetic
Assessing Accuracy of Land Change.” Remote Sensing of Environment Structure.” Ecography 40, no. 8: 913–929. https:// doi. org/ 10. 1111/ ecog.
148: 42–57. 02881 .
Osco, L. P., W. Qiusheng, E. L. De Lemos, et al. 2023. “The Segment Rogers, P. 1996. Disturbance Ecology and Forest Management: A Review
Anything Model (SAM) for Remote Sensing Applications: From Zero of the Literature. US Department of Agriculture.
to One Shot.” International Journal of Applied Earth Observation and
Geoinformation 124: 103540. https:// doi. org/ 10. 1016/j. jag. 2023. 103540. Ronneberger, O., P. Fischer, and T. Brox. 2015. “U- Net: Convolutional
Networks for Biomedical Image Segmentation.” In Medical Image
Ouaknine, A., T. Kattenborn, E. Laliberté, and D. Rolnick. 2025. Computing and Computer- Assisted Intervention—MICCAI 2015, ed-
“Openforest: A Data Catalog for Machine Learning in Forest ited by N. Navab, J. Hornegger, W. M. Wells, and A. F. Frangi, 234–241.
Monitoring.” Environmental Data Science 4: e15. Springer International Publishing.
Parra, A., and M. Simard. 2023. “Evaluation of Tree- Growth Rate in the Rußwurm, M., and M. Körner. 2020. “Self- Attention for Raw Optical
Laurentides Wildlife Reserve Using GEDI and Airborne- LiDAR Data.” Satellite Time Series Classification.” ISPRS Journal of Photogrammetry
Remote Sensing 15, no. 22: 5352. https:// doi. org/ 10. 3390/ rs152 25352 . and Remote Sensing 169: 421–435.
Pasquarella, V. J., B. A. Bradley, and C. E. Woodcock. 2017. “Near- Real- Saah, D., G. Johnson, B. Ashmall, et al. 2019. “Collect Earth: An Online
Time Monitoring of Insect Defoliation Using Landsat Time Series.” Tool for Systematic Reference Data Collection in Land Cover and Use
Forests 8, no. 8: 275. https:// doi. org/ 10. 3390/ f8080275. Applications.” Environmental Modelling & Software 118: 166–171.
Paulino, E. R., M. Schlerf, A. Roeder, J. Stoffels, and T. Udelhoven. 2024. Scheepens, D., J. Millard, M. Farrell, and T. Newbold. 2024. “Large
“Forest Disturbance Characterization in the Era of Earth Observation Language Models Help Facilitate the Automated Synthesis of
Big Data: A Mapping Review.” International Journal of Applied Earth Information on Potential Pest Controllers.” Methods in Ecology and
Observation and Geoinformation 128: 103755. Evolution 15, no. 7: 1261–1273.
Perbet, P., L. Guindon, J.- F. Côté, and M. Béland. 2024. “Evaluating Schiefer, F., S. Schmidtlein, A. Frick, et al. 2023. “UAV- Based Reference
Deep Learning Methods Applied to Landsat Time Series Subsequences Data for the Prediction of Fractional Cover of Standing Deadwood
to Detect and Classify Boreal Forest Disturbances Events: The From Sentinel Time Series.” ISPRS Open Journal of Photogrammetry
Challenge of Partial and Progressive Disturbances.” Remote Sensing of and Remote Sensing 8: 100034. https:// doi. org/ 10. 1016/j. ophoto. 2023.
Environment 306: 114107. 100034.
22 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Schiller, C., J. Költzow, S. Schwarz, F. Schiefer, and F. E. Fassnacht. 2024. Sumbul, G., A. De Wall, T. Kreuziger, et al. 2021. “Bigearthnet- Mm: A
“Forest Disturbance Detection in Central Europe Using Transformers Large- Scale, Multimodal, Multilabel Benchmark Archive for Remote
and Sentinel- 2 Time Series.” Remote Sensing of Environment 315: Sensing Image Classification and Retrieval [Software and Data Sets].”
114475. https:// doi. org/ 10. 1016/j. rse. 2024. 114475. IEEE Geoscience and Remote Sensing Magazine 9, no. 3: 174–180.
Schleeweis, K. G., G. G. Moisen, T. A. Schroeder, et al. 2020. “US Sykas, D., I. Papoutsis, and D. Zografakis. 2021. “Sen4agrinet: A
National Maps Attributing Forest Change: 1986–2010.” Forests 11: Harmonized Multi- Country, Multi- Temporal Benchmark Dataset for
653. Agricultural Earth Observation Machine Learning Applications.” In
2021 IEEE International Geoscience and Remote Sensing Symposium
Schmitt, M., L. H. Hughes, C. Qiu, and X. X. Zhu. 2019. “Sen12ms:
IGARSS, 5830–5833. IEEE.
A Curated Dataset of Georeferenced Multi- Spectral Sentinel- 1/2
Imagery for Deep Learning and Data Fusion.” In ISPRS Annals of the Szegedy, C., W. Liu, Y. Jia, et al. 2015. “Going Deeper With Convolutions.”
Photogrammetry, Remote Sensing and Spatial Information Sciences, In Proceedings of the IEEE Conference on Computer Vision and Pattern
vol. IV- 2/W7, 153–160. ISPRS. https://d oi.o rg/1 0.5 194/i sprs- a nnal Recognition, 1–9. IEEE.
s- IV- 2- W7- 153- 2019.
Szegedy, C., V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna. 2016.
Schroeder, T. A., K. G. Schleeweis, G. G. Moisen, et al. 2017. “Testing “Rethinking the Inception Architecture for Computer Vision.” In
a Landsat- Based Approach for Mapping Disturbance Causality in Us Proceedings of the IEEE Conference on Computer Vision and Pattern
Forests.” Remote Sensing of Environment 195: 230–243. Recognition, 2818–2826. IEEE.
Sebald, J., C. Senf, and R. Seidl. 2021. “Human or Natural? Landscape Thom, D., and R. Seidl. 2016. “Natural Disturbance Impacts on
Context Improves the Attribution of Forest Disturbances Mapped Ecosystem Services and Biodiversity in Temperate and Boreal Forests.”
From Landsat in Central Europe.” Remote Sensing of Environment 262: Biological Reviews 91, no. 3: 760–781.
112502.
Tollefson, J. 2025. “Google Ai Model Creates Maps of Earth ‘at Any
Seidl, R., D. Thom, M. Kautz, et al. 2017. “Forest Disturbances Under Place and Time’.” Nature 644: 313–314.
Climate Change.” Nature Climate Change 7, no. 6: 395–402.
Tseng, G., R. Cartuyvels, I. Zvonkov, M. Purohit, D. Rolnick, and H.
Senf, C. 2022. “Seeing the System From Above: The Use and Potential of
Kerner. 2023. “Lightweight, Pre- Trained Transformers for Remote
Remote Sensing for Studying Ecosystem Dynamics.” Ecosystems 25, no. Sensing Timeseries.” In Proceedings of the NeurIPS 2023 Workshop on
8: 1719–1737. https:// doi. org/ 10. 1007/ s1002 1- 022- 00777 - 2. Tackling Climate Change With Machine Learning: Blending New and
Senf, C., A. Buras, C. S. Zang, A. Rammig, and R. Seidl. 2020. “Excess Existing Knowledge Systems. NeurIPS. https://w ww.c limat echan ge.a i/
Forest Mortality Is Consistently Linked to Drought Across Europe. papers/ neuri ps2023/ 87.
Nature.” Communications 11, no. 1: 6200. https:// doi. org/ 10. 1038/ s4146
Tseng, G., I. Zvonkov, C. L. Nakalembe, and H. Kerner. 2021.
7- 020- 19924 - 1.
“Cropharvest: A Global Dataset for Crop- Type Classification.” In Thirty-
Senf, C., and R. Seidl. 2020. “Mapping the Forest Disturbance Regimes Fifth Conference on Neural Information Processing Systems Datasets and
of Europe.” Nature Sustainability 4, no. 1: 63–70. https:// doi. org/ 10. Benchmarks Track (Round 2). NeurIPS.
1038/s 41893 -0 20-0 0609- y . Turner, M. G., and R. Seidl. 2023. “Novel Disturbance Regimes and
Shah, M., M. S. Raval, and S. Divakaran. 2025. “A Systematic Review Ecological Responses.” Annual Review of Ecology, Evolution, and
on Deep Learning for Atmospheric Correction of Satellite Images.” Systematics 54, no. 1: 63–83. https:// doi. org/ 10. 1146/ annur ev- ecols ys-
Archives of Computational Methods in Engineering 33: 4059–4089. 11042 1- 101120.
Shi, X., Z. Chen, H. Wang, D.- Y. Yeung, W.- K. Wong, and W.- c. Woo. Vancutsem, C., A. Frédéric, J.- F. Pekel, et al. 2021. “Long- Term (1990–
2015. “Convolutional Lstm Network: A Machine Learning Approach for 2019) Monitoring of Forest Cover Changes in the Humid Tropics.”
Precipitation Nowcasting.” Advances in Neural Information Processing Science Advances 7, no. 10: eabe1603.
Systems 28: 1–9.
Vaswani, A., N. Shazeer, N. Parmar, et al. 2017. “Attention Is All You
Shimabukuro, Y. E., R. Beuchle, R. C. Grecchi, and F. Achard. 2014. Need.” Advances in Neural Information Processing Systems 30: 1–11.
“Assessment of Forest Degradation in Brazilian Amazon due to Selective
Verbesselt, J., A. Zeileis, and M. Herold. 2012. “Near Real- Time
Logging and Fires Using Time Series of Fraction Images Derived From
Disturbance Detection Using Satellite Image Time Series.” Remote
Landsat Etm+ Images.” Remote Sensing Letters 5, no. 9: 773–782.
Sensing of Environment 123: 98–108.
Shu, D., and A. B. Farimani. 2024. “Zero- Shot Uncertainty
Viana- Soto, A., and C. Senf. 2025. “The European Forest Disturbance Quantification Using Diffusion Probabilistic Models.” arXiv Preprint
Atlas: A Forest Disturbance Monitoring System Using the Landsat
arXiv:2408.04718.
Archive.” Earth System Science Data 17, no. 6: 2373–2404. https:// doi.
Slagter, B., J. Reiche, D. Marcos, et al. 2023. “Monitoring Direct Drivers org/ 10. 5194/ essd- 17- 2373- 2025.
of Small- Scale Tropical Forest Disturbance in Near Real- Time With
Wagner, F. H., R. Dalagnol, C. H. L. Silva- Junior, et al. 2023. “Mapping
Sentinel- 1 and - 2 Data.” Remote Sensing of Environment 295: 113655.
Tropical Forest Cover and Deforestation With Planet Nicfi Satellite
Smith, M., L. Fleming, J. Geach, R. Roberts, F. Kalaitzis, and J. Banister. Images and Deep Learning in Mato Grosso State (Brazil) From 2015 to
2025. “Dargana: Fine- Tuning Earthpt for Dynamic Tree Canopy 2021.” Remote Sensing 15, no. 2: 521.
Mapping From Space.” In ICLR 2025 Workshop on Tackling Climate
Change With Machine Learning. ICLR. https://w ww.c limat echan ge.a i/ Wang, J., X. Fan, X. Yang, T. Tjahjadi, and Y. Wang. 2022. “Semi-
papers/ iclr2 025/ 11. Supervised Learning for Forest Fire Segmentation Using UAV Imagery.”
Forests 13, no. 10: 1573. https:// doi. org/ 10. 3390/ f1310 1573.
St. Peter, J., J. Drake, P. Medley, and V. Ibeanusi. 2021. “Forest Structural
Estimates Derived Using a Practical, Open- Source Lidar- Processing Wang, L., S. Liu, W. Song, J. Zhang, and S. Ding. 2025. “Global High-
Workflow.” Remote Sensing 13, no. 23: 4763. https:// doi. org/ 10. 3390/ Resolution Forest Disturbance Type Dataset.” Earth System Science
rs1323 4763 . Data Discussions 1–23: 2025.
Steger, S., R. Bell, H. Petschko, and T. Glade. 2015. “Evaluating the Wang, S., W. Chen, S. M. Xie, G. Azzari, and D. B. Lobell. 2020. “Weakly
Effect of Modelling Methods and Landslide Inventories Used for Supervised Deep Learning for Segmentation of Remote Sensing
Statistical Susceptibility Modelling.” In Engineering Geology for Society Imagery.” Remote Sensing 12, no. 2: 207.
and Territory- Volume 2: Landslide Processes, 201–204. Springer.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026 23 of 24
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Wang, W., V. W. Zheng, H. Yu, and C. Miao. 2019. “A Survey of Zero- Shot Zhu, Z., J. Zhang, Z. Yang, et al. 2020. “Continuous Monitoring of
Learning: Settings, Methods, and Applications.” ACM Transactions on Land Disturbance Based on Landsat Time Series.” Remote Sensing of
Intelligent Systems and Technology 10, no. 2: 1–37. https:// doi. org/ 10. Environment 238: 111116.
1145/ 3293318.
Ziegler, J. D., S. Subramaniam, M. Azzarito, O. Doyle, P. Krusche, and
Wang, Y., C. M. Albrecht, N. A. A. Braham, L. Mou, and X. X. Zhu. T. Coroller. 2022. “Multi- Modal Conditional Gan: Data Synthesis in
2022. “Self- Supervised Learning in Remote Sensing: A Review.” IEEE the Medical Domain.” In NeurIPS 2022 Workshop on Synthetic Data for
Geoscience and Remote Sensing Magazine 10, no. 4: 213–247. Empowering ML Research. NeurIPS.
Wilkinson, M. D., M. Dumontier, I. J. J. Aalbersberg, et al. 2016. Ziv, R. S., and Y. LeCun. 2024. “To Compress or Not to Compress—Self-
“The Fair Guiding Principles for Scientific Data Management and Supervised Learning and Information Theory: A Review.” Entropy 26,
Stewardship.” Scientific Data 3, no. 1: 1–9. no. 3: 252.
Wu, H., B. Xiao, N. Codella, et al. 2021. “Cvt: Introducing Convolutions
to Vision Transformers.” In Proceedings of the IEEE/CVF International
Conference on Computer Vision, 22–31. IEEE.
Wu, K., Y. Zhang, R. Lixiang, et al. 2025. “A Semantic- Enhanced Multi-
Modal Remote Sensing Foundation Model for Earth Observation.”
Nature Machine Intelligence 7: 1235–1249.
Wu, N., L. Huang, M. Zhang, Y. Dou, K. Mo, and J. Liu. 2025. “Remote
Sensing Detection of Forest Changes in the South Ridge Corridor and an
Attribution Analysis.” Forests 16, no. 2: 205.
Wulder, M. A., T. R. Loveland, D. P. Roy, et al. 2019. “Current Status
of Landsat Program, Science, and Applications.” Remote Sensing of
Environment 225: 127–147.
Xiao, A., W. Xuan, J. Wang, et al. 2025. “Foundation Models for Remote
Sensing and Earth Observation: A Survey.” IEEE Geoscience and Remote
Sensing Magazine 13: 297–324.
Xu, Z., and D. Jiang. 2025. “AI- Powered Plant Science: Transforming
Forestry Monitoring, Disease Prediction, and Climate Adaptation.”
Plants 14, no. 11: 1626.
Ye, S., J. Rogan, Z. Zhu, and J. R. Eastman. 2021. “A Near- Real- Time
Approach for Monitoring Forest Disturbance Using Landsat Time
Series: Stochastic Continuous Change Detection.” Remote Sensing of
Environment 252: 112167.
Zhang, L., L. Zhang, and B. Du. 2016. “Deep Learning for Remote
Sensing Data: A Technical Tutorial on the State of the Art.” IEEE
Geoscience and Remote Sensing Magazine 4, no. 2: 22–40. https:// doi.
org/ 10. 1109/ MGRS. 2016. 2540798.
Zhang, X., and Y. Zhang. 2023. “Conv- Pvt: A Fusion Architecture of
Convolution and Pyramid Vision Transformer.” International Journal
of Machine Learning and Cybernetics 14, no. 6: 2127–2136.
Zhang, Y., F. Ling, X. Wang, et al. 2021. “Tracking Small- Scale Tropical
Forest Disturbances: Fusing the Landsat and Sentinel- 2 Data Record.”
Remote Sensing of Environment 261: 112470. https:// doi. org/ 10. 1016/j.
rse.2 021.1 12470.
Zhao, F., R. Sun, L. Zhong, et al. 2022. “Monthly Mapping of Forest
Harvesting Using Dense Time Series Sentinel- 1 SAR Imagery and Deep
Learning.” Remote Sensing of Environment 269: 112822. https:// doi. org/
10. 1016/j. rse. 2021. 112822.
Zhou, B., A. Khosla, A. Lapedriza, A. Oliva, and A. Torralba. 2016.
“Learning Deep Features for Discriminative Localization.” In
Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, 2921–2929. IEEE.
Zhou, Z.- H. 2018. “A Brief Introduction to Weakly Supervised Learning.”
National Science Review 5, no. 1: 44–53.
Zhu, X. X., D. Tuia, L. Mou, et al. 2017. “Deep Learning in Remote
Sensing: A Comprehensive Review and List of Resources.” IEEE
Geoscience and Remote Sensing Magazine 5, no. 4: 8–36. https:// doi. org/
10. 1109/ MGRS. 2017. 2762307.
Zhu, Z., and C. E. Woodcock. 2014. “Continuous Change Detection and
Classification of Land Cover Using All Available Landsat Data.” Remote
Sensing of Environment 144: 152–171.
24 of 24 Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2026
19424795,
2026,
2,
Downloaded
from
https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.70096
by
Readcube-Labtiva,
Wiley
Online
Library
on
[15/10/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License