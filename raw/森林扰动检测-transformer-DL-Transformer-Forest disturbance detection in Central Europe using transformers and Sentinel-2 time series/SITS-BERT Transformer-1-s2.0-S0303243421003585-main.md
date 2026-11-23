InternationalJournalofAppliedEarthObservationsandGeoinformation106(2022)102651
Contents lists available at ScienceDirect
International Journal of Applied Earth
Observations and Geoinformation
journal homepage: www.elsevier.com/locate/jag
SITS-Former: A pre-trained spatio-spectral-temporal representation model
for Sentinel-2 time series classification
Yuan Yuana,b,1, Lei Linc,1, Qingshan Liub,*, Renlong Hangb, Zeng-Guang Zhoud
aSchool of Geographic and Biologic Information, Nanjing University of Posts and Telecommunications, Nanjing 210023, China
bSchool of Computer and Software, Nanjing University of Information Science and Technology, Nanjing 210044, China
cXiaomi AI Lab, Xiaomi Inc., Beijing 100085, China
dKey Laboratory of Quantitative Remote Sensing Information Technology, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100094,
China
A R T I C L E I N F O A B S T R A C T
Keywords: Sentinel-2 images provide a rich source of information for a variety of land cover, vegetation, and environmental
Pre-training monitoring applications due to their high spectral, spatial, and temporal resolutions. Recently, deep learning-
satellite image time series (SITS) based classification of Sentinel-2 time series becomes a popular solution to vegetation classification and land
Self-supervised learning
cover mapping, but it often demands a large number of manually annotated labels. Improving classification
Sentinel-2
performance with limited labeled data is still a challenge in many real-world remote sensing applications. To
Transformer
address label scarcity, we present SITS-Former (SITS stands for Satellite Image Time Series and Former stands for
Transformer), a pre-trained representation model for Sentinel-2 time series classification. SITS-Former adopts a
Transformer encoder as the backbone and takes time series of image patches as input to learn spatio-spectral-
temporal features. According to the principles of self-supervised learning, we pre-train SITS-Former on
massive unlabeled Sentinel-2 time series via a missing-data imputation proxy task. Given an incomplete time
series with some patches being masked randomly, the network is asked to regress the central pixels of these
masked patches based on the residual ones. By doing so, the network can capture high-level spatial and temporal
dependencies from the data to learn discriminative features. After pre-training, the network can adapt the
learned features to a target classification task through fine-tuning. As far as we know, this is the first study that
exploits self-supervised learning for patch-based representation learning and classification of SITS. We quanti-
tatively evaluate the quality of the learned features by transferring them on two crop classification tasks, showing
that SITS-Former outperforms state-of-the-art approaches and yields a significant improvement (2.64%~3.30%
in overall accuracy) over the purely supervised model. The proposed model provides an effective tool for SITS-
related applications as it greatly reduces the burden of manual labeling. The source code will be released at htt
ps://github.com/linlei1214/SITS-Former upon publication.
1. Introduction a single sensor. Owing to these improvements, Sentinel-2 time series can
capture rapid variations in plant phenology with much better detail,
With the successive launches of the twin satellites from the Sentinel- opening the door for a variety of applications related to land cover,
2 mission, it is feasible to access optical Earth Observation (EO) data at vegetation, and environmental monitoring (Misra et al., 2020; Phiri
much higher temporal and finer spatial resolutions than in the past. The et al., 2020; Solano-Correa et al., 2020).
Multi-Spectral Instrument (MSI) onboard each satellite provides 13 The interest in Sentinel-2 time series for vegetation and land cover
spectral bands with spatial resolutions ranging from 10 m to 60 m. The mapping has gained increasing popularity in recent years. Some early
rapid revisit interval of 5 days with the satellite constellation increases studies extended methods for mono-temporal classification by extract-
the opportunity of acquiring cloud-free images over a geographical area, ing features from each image and then applying classical machine
making it possible to build dense Satellite Image Time Series (SITS) from learning classifiers (e.g., Support Vector Machine (SVM) and Random
* Corresponding author.
E-mail address: qsliu@nuist.edu.cn (Q. Liu).
1 Y. Yuan and L. Lin contributed equally to this work as first authors.
https://doi.org/10.1016/j.jag.2021.102651
Received 12 August 2021; Received in revised form 23 November 2021; Accepted 10 December 2021
Availableonline17December2021
1569-8432/©2021TheAuthors.PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Forest (RF)) to multi-temporal features (Eudes Gbodjo et al., 2020; Feng Transformer), a modification of SITS-BERT for patch-based Sentinel-2
et al., 2019; Sheeren et al., 2016). However, these methods suffer from time series classification. SITS-Former uses a simple yet powerful
two drawbacks. First, they consider SITS as a collection of independent Transformer encoder as the backbone and takes time series of image
images while ignoring temporal correlations between images (Inter- patches as input to learn spatio-spectral-temporal features. Based on the
donato et al., 2019). Second, the concatenation of multi-temporal fea- principles of self-supervised learning, we develop a novel proxy task to
tures generally leads to high dimensionality, which results in the “curse pre-train SITS-Former without human annotation. Given a time series of
of dimensionality” problem (Pelletier et al., 2017). Other early studies image patches (centered at an analyzed pixel) with some patches being
incorporated phenological information extracted from the spectral tra- masked, the network is made to regress the central pixels of these
jectory of each pixel, such as spectral statistics (Lebourgeois et al., masked patches based on the remaining ones. We hypothesize that the
2017), phenological parameters (do Nascimento Bendini et al., 2019; features learned in thus a way can capture subtle differences between
Shahrabi et al., 2020), curve fitting coefficients (Zhu and Woodcock, various plant species. After pre-training, the network can easily adapt
2014), etc. However, these hand-crafted features provide limited addi- the learned features to a target classification task through fine-tuning. As
tional discriminative information, and their robustness is heavily far as we know, this is the first attempt at self-supervised learning in
affected by the selected curve fitting functions and time-series smooth- patch-based representation learning using SITS.
ing techniques. The main contributions of this paper are summarized as follows.
Over recent years, deep learning approaches have achieved much
success for SITS classification. Unlike traditional methods, deep learning (1) We propose a hybrid deep learning architecture to learn spatio-
approaches can learn discriminative features automatically without spectral-temporal features from Sentinel-2 time series.
manual feature selection. Among these methods, Recurrent Neural (2) We first introduce self-supervised learning to patch-based SITS
Networks (RNNs, e.g., Long Short-Term Memory (LSTM), Gated classification to address label scarcity.
Recurrent Unit (GRU)) (Ienco et al., 2017; Sun et al., 2019; Yuan et al., (3) We carried out extensive experiments on two large-scale datasets
2020), Convolutional Neural Networks (Pelletier et al., 2019; Zhong and demonstrated the effectiveness of our method.
et al., 2019), and Transformers (or self-attention networks) (Rußwurm
and Ko¨rner, 2020; Yuan and Lin, 2021) have been employed for pixel- 2. Related work
based SITS classification. Several recent studies also suggest devel-
oping patch-based classification methods for Sentinel-2 time series 2.1. Self-supervised learning
(Benedetti et al., 2018; Garnot et al., 2019; Li et al., 2020b; Rußwurm
and Ko¨rner, 2018), owing to the importance of spatial information in The general pipeline of self-supervised learning is to first pre-train a
identifying certain land-cover/plant types. For example, fruit trees are network on massive unlabeled data and then fine-tune it on a few labels
typically regularly spaced. Hence, image texture helps to distinguish related to a target task. Pre-training is the process of learning features
orchards from natural forests. Despite the efforts, making full use of the via pre-defined proxy tasks, while fine-tuning refers to the process of
abundant information provided by Sentinel-2 time series is still a chal- updating the model parameters to solve a given task. Currently, this
lenge in remote sensing. unsupervised-pre-training +supervised-fine-tuning pipeline has domi-
The recent success in deep learning-based SITS classification comes nated NLP and shown powerful skills (Devlin et al., 2019). Self-
at the expense of increasing the complexity of network architectures. supervised methods have also started to flourish recently in CV and
Both the number of network layers and neurons per layer in state-of-the- achieved remarkable performance that even match that of purely su-
art models are increasing. Training such models usually relies on mil- pervised methods on standard benchmarks (Chen et al., 2020).
lions of labeled samples, which are almost always unavailable in remote The key components of an effective self-supervised method are proxy
sensing applications. When labeled data is scarce, deep neural networks tasks, which should allow networks to learn high-level abstract repre-
are very prone to overfitting, which tend to memorize the data, sentations (Kolesnikov et al., 2019). In general, a proxy task is designed
including the inevitable bias and noise in the training set, rather than in such a way that predicts any part of the input from other parts in some
generalize the principles underlying the data. For this reason, an over- form (Qiu et al., 2020). In NLP, some effective proxy tasks include
fitted network that performs perfectly on the training set performs language modeling, masked language modeling, next sentence predic-
poorly on unseen data. Although some useful regularization strategies tion, sentence order prediction, etc. In CV, proxy tasks are more diverse
(such as dropout (Srivastava et al., 2014), data augmentation (Perez and and still increasing (Jing and Tian, 2020). Visual information used for
Wang, 2017), and normalization (Ioffe and Szegedy, 2015; Lei Ba et al., self-supervision includes spatial context structures, colors, multi-mode
2016)) can reduce overfitting in deep learning models, they still cannot correspondences, temporal contiguity between video frames, etc.
solve this problem from the root cause. Despite these achievements, research and applications of self-
Self-supervised learning has drawn lots of attention in the past few supervised learning in remote sensing have just begun. Recent studies
years due to its encouraging performance in representation learning explored the use of self-supervised learning in addressing tasks such as
with fewer labels (Liu et al., 2021). The main idea of self-supervised image registration (Wang et al., 2018), change detection (Dong et al.,
learning is to make neural networks extract general-purpose features 2020; Saha et al., 2020), scene classification (Tao et al., 2020; Zhao
from unlabeled data by designing proxy tasks for networks to solve. et al., 2020b), and image classification (Li et al., 2021; Vincenzi et al.,
These proxy tasks are formulated by leveraging the inherent structure of 2021; Yue et al., 2021). However, these approaches have been restricted
the data as supervision (Jing and Tian, 2020; Kolesnikov et al., 2019). In to analyzing a single image or bi-temporal images without considering
the past few years, self-supervised learning has achieved dramatic suc- temporal information. In contrast, our study focuses on learning spatial
cess in Natural Language Processing (NLP) (Qiu et al., 2020) and and temporal features from time series of satellite images, facilitating
Computer Vision (CV) (Jing and Tian, 2020) domains. However, few downstream tasks such as vegetation classification and land cover
studies try to exploit the notion of self-supervised learning for SITS mapping.
analysis. We proposed the first pre-trained representation model called
SITS-BERT (Bidirectional Encoder Representations from Transformers) 2.2. SITS classification
for Sentinel-2 time series classification in a previous study (Yuan and
Lin, 2021), which has shown encouraging performance. However, SITS- We briefly review popular deep learning models for SITS classifica-
BERT was still pixel-based and did not take advantage of spatial tion, namely, CNNs, RNNs, Transformers, and their combinations.
information. CNN has been extensively studied in a variety of remote sensing
To address these issues, we present SITS-Former (Former stands for applications, such as multispectral/hyperspectral image classification
2

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
(Hang et al., 2020; Hang et al., 2021; Zhang et al., 2018), scene classi- pixel to be classified). The size of the patches is 5 ×5. Therefore, Oi is a
fication (Anwer et al., 2018; Cheng et al., 2018), image segmentation 3D tensor of size (10 ×5 ×5). ti represents the acquisition time of Oi,
(Waldner and Diakogiannis, 2020), object detection (Cheng et al., which is expressed as the Julian date (i.e., Day Of Year (DOY)). The
2016), etc. Pelletier et al. (2019) introduced Temporal Convolutional length of time series can be different due to irregular sampling.
Neural Networks (TempCNNs) for SITS-based crop mapping, where
convolutions are operated in the time domain to capture structures of
3.1. Architecture of SITS-Former
spectral profiles. Ji et al. (2018) applied 3D-CNNs on multi-temporal
images to extract spatio-temporal-combined representations.
SITS-Former comprises two modules, i.e., an image patch embedding
RNN is another commonly used architecture for processing sequen-
module and a Transformer encoder module (Fig. 2). The image patch
tial data. Ienco et al. (2017) introduced LSTM for SITS-based land cover
classification. Rußwurm and Ko¨rner (2017) adopted a similar network embedding module operates on all the patches independently to learn
inner-patch spatio-spectral features; it transforms an input time series
for vegetation development modeling, except that the inputs were flat-
tened local image patches. Wang et al. (2019) utilized a Bidirectional
into a set of corresponding embedding vectors {E1 ,⋯,EN }. The Trans-
former encoder module enables interactions between the patches to
LSTM (Bi-LSTM) network to aggregate the temporal information from
learn temporal relations amongst different timesteps; it takes the
both past and future contexts. Several hybrid convolutional and recur-
embedding vectors as input and transforms them into their temporal-
rent architectures have also been developed for SITS analysis (Garnot
et al., 2019; Interdonato et al., 2019; Rußwurm and Ko¨rner, 2018). context-enriched representations {T1 ,⋯,TN }.
Image patch embedding module: The image patch embedding
Transformer was introduced by Vaswani et al. (2017) and has since
become state-of-the-art in NLP. In contrast to RNNs that operate
module aims to transform each input tuple 〈Oi ,ti 〉into a single embed-
sequence elements one at a time recursively, Transformers operate on all
ding vector Ei, which is the sum of two vectors of the same dimension: a
learnable spatio-spectral embedding vector (SSEV) denoted by
elements in parallel and model the influence each element has on
another by assigning attention scores (Minaee et al., 2021). Trans-
SSEV(Oi ), and a pre-defined positional encoding vector (PEV) denoted
formers overcome the difficulty of RNNs for remembering long-term
by PEV(ti ).
temporal dependencies and allow for more parallelization. Rußwurm SSEV is produced by processing each input patch with a lightweight
and Ko¨rner (2020) carried out comprehensive experiments to evaluate network (Fig. 3). The network is composed of two 3-Dimensional Con-
volutional (Conv3D) layers (32 filters with 5 ×3 ×3 kernel size in the
the performance of several deep learning models for SITS classification,
first layer, and 64 filters with 3 ×3 ×3 kernel size in the second layer), a
showing that Transformers and RNNs outperform TempCNNs in
flatting layer, and a Fully Connected (FC) layer with 256 hidden nodes.
handling noisy raw Sentinel-2 time series. Yuan and Lin (2021) found
Each Conv3D layer is followed by a Rectified Linear Unit (ReLU) acti-
that Transformers are more robust to overfitting than RNNs and
vation function to inject nonlinearity and a Batch Normalization (BN)
TempCNNs with limited training samples. Li et al. (2020b) developed a
layer to enable faster and more stable training (Ioffe and Szegedy, 2015).
CNN-Transformer hybrid architecture for crop classification.
Compared to CNN-Transformer (Li et al., 2020b), we use 3D-CNNs
In summary, the existing methods extract features either in the time
instead of traditional 2D-CNNs to exploit inter-band correlation and
domain or in the spatio-temporal domains. In contrast, SITS-Former is
local image structures simultaneously.
designed to capture multi-dimensional dependencies from the data in
PEV encodes the acquisition time of an image, allowing the network
spectral, spatial, and temporal domains simultaneously.
to cope with irregularly sampled time series and align dates from
different years. In general, PEV can be either fixed or learnable. In this
3. Methods
study, we adopt the sinusoidal positional encoding technique (Vaswani
et al., 2017) to calculate PEV. A pre-defined vector is assigned to each
In this study, we use all spectral bands at 10 ~ 20 m resolutions of
DOY and no extra parameter is introduced.
Sentinel-2 images. The images are pre-processed to Bottom-Of- ⎧ ( )
A
Fi
t
g
m
.
o
1
s p
il
h
lu
er
s
e
tr a
(
t
B
e
O
s
A
th
)
e
r e
c
fl
o
e
n
c
s
t
t
a
r
n
u
c
c
e
ti o
w
n
i t
o
h
f
a
a
n
n
e
im
qu
a
a
g
l
e
r
p
es
a
o
tc
lu
h
t i
t
o
im
n
e
fo
s
r
e r
a
i
l
e
l
s
b
.
a
O
n
n
d
l
s
y
. ⎪⎪⎪⎨sin
100
t i
00D k
,ifp=2k
n
c
p
l
a
o
o
t
i
u
c
se
h
d
-
s
f
i
,
r
s
e
s
e
n
e
l
o
i
p
m
w
a
i
,
t
n
c
o
a
h
r
t
e
e
s
s
h
d
a
a
f
d
r
r
o
e
o
m
w
u
s
s
a
e
a
d
t
c
i
.
c
m
o
I
e
r
f
d
s
a
i
e
n
r
p
g
ie
a
t
s
t
o
.
c h
L
th
e
c
e
t
o
x
s
n
c
=
t
e
a
n
i
{
e
n
x
s
c
1
l
,
n
a
⋯
o
ss
i
,
i
s
x
fi
y
N
c
}
a
p
t
i
b
i
x
o
e
e
n
l
a
s
m
n
s
a
a
u
p
n
c
,
n
h
t
u
h
a
a
e
s
l
PE(t i ) p = ⎪⎪⎪⎩cos (
100
t
i
00D k
)
,ifp=2k+1
(1)
time series of N timesteps, where each element is a tuple xi = 〈Oi ,ti 〉. Oi where PE(ti ) p represents the pth element of PEV; k is an auxiliary
represents the ith local image patch centered at an analyzed pixel (the variable indicating the parity of p.
Fig. 1. Illustration of an image patch time series {〈Oi ,ti 〉}, where Oi is the ith image patch centered at an analyzed pixel (colored in red) and ti is the acquisition time.
(For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
3

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Fig. 2. SITS-Former is composed of two modules: an image patch embedding module (marked with a red rectangle) and a Transformer encoder module (marked with
a blue rectangle). The image patch embedding module is shared across different timesteps. (For interpretation of the references to colour in this figure legend, the
reader is referred to the web version of this article.)
Fig. 3. Illustration of the spatio-spectral embedding network.
Transformer encoder module: We adopt a multi-layer Transformer fine-tuning (or classification) stage (Fig. 4). Apart from an additional
encoder to integrate the temporal contextual information into the output module, SITS-Former is used in both stages as a shared feature
patches’ representations. The basic building blocks of a Transformer extractor, which allows the well-learned features during pre-training to
encoder are multi-head self-attention layers. Each layer is composed of be transferred to a target task.
multiple identical sub-layers called heads. In each head, an attention Self-supervised pre-training stage: Our objective is to learn
matrix is calculated by the scaled dot-product of a query matrix (Q) and discriminative features from unlabeled data without resorting to any
a key matrix (V) multiplying with a value matrix (V). The Q, K, and V human annotation. We design a novel proxy task that trains the network
matrices of each head are obtained by processing the sequence elements to complete the missing part of an input time series. We refer to this task
with different FC layers. The mathematical description of the multi-head as “missing-data imputation”. Suppose we are given a set of unlabeled
attention mechanism is: annual time series of image patches. For each time series, a certain
( ) proportion of patches are randomly replaced with a special padding
QKT
Attention(Q,K,V)=softmax √̅̅̅̅ V (2) matrix [MASK]before feeding it to the network. The padding matrix is of
D
the same dimension as the original patches and is shared between all
masked timesteps. The elements of [MASK]are randomnumbers from a
MultiHead(Q,K,V)=Concat(head ,⋯,head )
1 H
normal distribution. The training objective requires recovering the
(cid:0) )
wherehead i =Attention QW i Q,KW i K,VW i V . (3) a a n cq a u ly is z i e t d io n p i d x a e t l e s s a (F t ig a . l l 4 ) t . h B e y m th a i s s k m ed e a t n im s, e t s h t e e p n s e t c w o o n r d k i t h io a n s e t d o l o e n a rn t h t e h i e r
where H is the number of heads; WQ, WK, WV are learnable weight spatiotemporal contextual relations between the patches to fill in the
i i i
matrices belonging to each head. missing content. In our implementation, 15% of patches in each time
series are masked, which are selected randomly for each training epoch
to increase the difficulty of this task.
{ }
3.2. Pre-training of SITS-Former Formally, given an unlabeled pre-training set x (1),⋯,x(m) of m
[ ]
samples. Let v(s)= v (s),⋯,v (s) be the reflectance time series associated
In this section, we propose a novel framework for applying SITS- 1 N
Former to an interested classification task. The proposed framework with the analyzed pixel of sample x(s). We use a single FC layer to map
includes two stages: a self-supervised pre-training stage and a supervised
4

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Fig. 4. The proposed framework consists of a self-supervised pre-training stage and a supervised fine-tuning (classification) stage. In the pre-training stage, general
features are learned from unlabeled Sentinel-2 time series by training SITS-Former to solve a pre-defined proxy task. Afterward, in the fine-tuning stage, the learned
parameters can be further transferred to a specific SITS classification task as a pre-trained model to improve performance and prevent overfitting.
[ ]
the outputs of SITS-Former (i.e., T(s) = T (s),⋯,T (s) ) into predictions, 4. Research data
1 N
and use the L2 distance between the predictions and targets at all
4.1. Study areas
masked positions as the loss function:
∑m (cid:0) ) A common practice in self-supervised learning is to verify the quality
L = M(s)⊙ v(s)(cid:0) W p T(s) 2 . (4) of the learned features by solving a downstream task. Here, we
s=1
concentrated our analysis on crop classification in two study sites (each
where Wp is a learnable weight matrix; M(s) is a binary vector cor- 100 ×100 km2, Fig. 5). The first study area was located in the City of
responding to x(s), with its element of 1 indicating a timestep being Fresno, California, from Sentinel-2 tile T11SKA. The elevation ranges
masked and 0 indicating non-masked; ⊙ represents the element-wise from 40 m to 2000 m. This area has a Mediterranean climate with mild,
product; ‖∙‖
2
represents l2-norm. wet winters and hot, dry summers. The second study site was located on
The basic idea behind this task is to make neural networks emulate the boundary between Missouri and Arkansas, from Sentinel-2 tile
human inductive reasoning. For example, for a crop classification task, T15SYA. The elevation ranges from 60 m to 270 m. This area has a
experienced human analysts only need a few images taken during the humid subtropical climate with cold to mild winters and hot, humid
growing season to identify crop types, benefiting from their prior summers. The crop types in both areas are very diverse, and there are
knowledge about plant appearance and growth patterns. Similarly, if a differences between the two regions in climate, topography, and plant
network can discover meaningful spatiotemporal patterns related to the species. Therefore, they can fully verify the effectiveness and general-
processes of vegetation growth and seasonality from massive unlabeled ization performance of our model.
data, it is possible to match an unseen time series with these patterns
even if the vegetation type is not yet known. Moreover, the knowledge 4.2. Data preparation
accumulated through pre-training may aid the acquisition of new
knowledge, such as plants that do not exist in the pre-training set, We downloaded Sentinel-2A/B images with cloud coverage lower
because some morphological (like plant spacing and ridge spacing), than 10% and pre-processed them into Level-2A products using the
phenological (such as sowing, emergence, tasseling, maturation, and Sen2Cor plugin and the Sentinel Application Platform (SNAP).
harvest), and spectral characteristics are shared among various species. To construct a pre-training set, we collected 216 images during 2018
Note that we neither regress the entire time series nor reconstruct the to 2019 from three tiles: T11SKA, T10SEJ, and T10SFH (Fig. 6, Table 1),
whole masked patches. On one hand, time series regression is a much which are located in the Central Valley of California. The plant species in
easier task than missing-data imputation since most sequence elements this region are extremely rich, making it a good training ground for self-
are known. On the other hand, we want the network to focus on an supervised learning (Yuan and Lin, 2021). A pre-training sample was
analyzed pixel instead of trivial texture statistics. generated by the following steps. We first cropped small patches from
Data augmentation is an effective technique to help networks learn the images over the same tile at an interval of 20 rows/columns, and
invariant features and avoid overfitting. We adopt three data augmen- then arranged the patches centered at the same pixel into time series.
tation strategies to generate more training samples: scale, flip, and The patches was of size 5 × 5 at a resolution of 10 m or 20 m after
rotation. Specifically, scale indicates resampling patches to 10 m or 20 m resampling. There was no overlap between adjacent patches, ensuring
while keeping the size of the patches unchanged (the corresponding area the difference between two samples large enough. Time series with less
on the Earth’s surface is not equal). Flip indicates flipping images hor- than 10 timesteps were excluded. Finally, there were around 1.66
izontally or vertically. Rotation means that images are rotated clockwise million unlabeled samples in the pre-training set.
by 0◦, 90◦, 180◦, or 270◦. The same augmentation technique is applied to For method evaluation, we collected 45 images and 26 images
all patches in a time series. captured during 2019 in each study area, respectively. The 2019 Crop-
Supervised fine-tuning stage: After pre-training, an additional land Data Layer (CDL) (Boryan et al., 2011) and its corresponding
classification module, which is randomly initialized, is added on top of confidence layer (Liu et al., 2004) were used as reference data to collect
SITS-Former. We adopt a simple classification module, which is formed samples. CDL data have been widely used as benchmarks for crop
by a max-pooling layer and a single FC layer. The outputs of SITS-Former classification due to their high quality (Li et al., 2020a; Sun et al., 2019;
at all timesteps are first pooled along the temporal dimension and then Zhao et al., 2020a). We resampled the Sentinel-2 images and the refer-
linearly projected for label prediction. When dealing with a specific task, ence data to 10 m to make them consistent. Then we used the same
we directly load the pre-trained weights of SITS-Former and then fine- sampling strategy to extract image patch time series, and labeled each
tune the entire model end-to-end on task-related data via standard su- time series with the crop type of the patch’s central pixel. To avoid the
pervised learning. adverse effects of noisy labels, a qualified sample should meet the
following conditions. First, more than 50% of the pixels in the entire
5

Y. Yuan et al.                                                                                                                              I n  t e  r n  a t i o  n  a  l  J o  u  r n  a  l o  f  A   p p  l i e d   E  a  r t h   O  b  s e  r v  a t i o  n   a  n d   G   e o  i n f  o r  m  a  t i o  n 106(2022)102651
Fig. 5. Location of the two study sites: (a) California, (b) Missouri. The background images are 2019 Cropland Data Layer (CDL) maps.
Table 2
Number of samples collected from each study site.
| Study  Crop type  | Number of  | Percentage of   | Total number  |
| ----------------- | ---------- | --------------- | ------------- |
| area              | samples    | each class (%)  | of samples    |
| California  Corn  | 3888       | 1.2             | 324,450       |
| Cotton            | 25,014     | 7.7             |               |
| Winter            | 2310       | 0.7             |               |
Wheat
| Alfalfa    | 14,860   | 4.6   |     |
| ---------- | -------- | ----- | --- |
| Tomatoes   | 13,191   | 4.1   |     |
| Grapes     | 66,984   | 20.6  |     |
| Citrus     | 11,886   | 3.7   |     |
| Almonds    | 54,462   | 16.8  |     |
| Walnuts    | 14,578   | 4.5   |     |
| Developed  | 1746     | 0.5   |     |
| Forest     | 3396     | 1.0   |     |
| Grass/     | 77,112   | 23.8  |     |
Pasture
| Pistachios      | 35,023    | 10.8   |          |
| --------------- | --------- | ------ | -------- |
| Missouri  Corn  | 45,264    | 11.6   | 391,026  |
| Cotton          | 83,917    | 21.5   |          |
| Rice            | 56,589    | 14.5   |          |
| Soybeans        | 116,656   | 29.8   |          |
| Fallow          | 14,264    | 3.6    |          |
| Open Water      | 5933      | 1.5    |          |
| Developed       | 1347      | 0.3    |          |
| Forest          | 43,051    | 11.0   |          |
Fig. 6. Location of the Sentinel-2 tiles (marked with red rectangles) used for  Grass/  2071   0.5
constructing the pre-training set. (For interpretation of the references to colour  Pasture
| Woody  | 21,934   | 5.6   |     |
| ------ | -------- | ----- | --- |
in this figure legend, the reader is referred to the web version of this article.)
Wetlands
Table 1  networks, while the validation set was used for hyper-parameter opti-
The elaborate information of the Sentinel-2 images used for pre-training.
mization. The best-performing model on the validation set was used for
Sentinel-2  Number of images (cloud  Top 5 major crops
accuracy assessment. To simulate real situations of label scarcity, we
tile  cover less than 10%)
randomly drew 100 labeled samples per class to construct the training
T11SKA  41 in 2018, 45 in 2019  Almonds, Grapes, Cotton,  and validation sets independently and then assigned all remaining
Pistachio, Alfalfa  samples to the test set. As a result, for the first study site (California), the
T10SEJ  30 in 2018, 38 in 2019  Rice, Almonds, Walnuts,
training and validation sets each contained 1300 samples, and the test
Tomatoes, Winter Wheat
set contained 323,150 samples. For the second study site (Missouri), the
T10SFH  39 in 2018, 23 in 2019  Alfalfa, Grapes, Walnuts, Corn,
Winter Wheat   training and validation sets each contained 1000 samples, and the test
set contained 390,026 samples. These test sets were hard to classify
because their class distributions were highly imbalanced.
patch should have the same label as the central pixel. Second, the
classification confidences of these pixels should be higher than 80%.
Finally, time series with less than 3 timesteps were discarded. Table 2
summarizes the number of samples selected from each study site.
The labeled samples were further divided into training, validation,
and test sets. The training set was used for training (or fine-tuning)
6

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
5. Results removing the use of positional encoding (SITS-FormerwithoutPE), (3)
using a BERT-style learnable positional encoding (SITS-Former-
5.1. Experimental settings and evaluation metrics learnablePE) (Devlin et al., 2019). Tables 4-5 report the results on both
datasets.
In our experiments, we compared SITS-Former with five competing We observe that SITS-Former globally outperforms its variants
methods. We employed RF as a traditional machine learning baseline without BN or PEV in terms of AA and Kappa coefficient. The AA
owing to its superiority for dealing with high-dimensional data (Pelletier decrease caused by removing BN is 0.51% and 1.02% on the test set for
et al., 2016). Besides, we selected four advanced deep learning models each dataset, respectively. Similarly, the AA decrease caused by
that have shown promising results for SITS classification: SITS-BERT removing PEV is 1.36% and 0.74%, respectively. These results confirm
(Yuan and Lin, 2021), CNN-Transformer (Li et al., 2020b), Convolu- that both batch normalization and positional encoding play positive
tional Recurrent Neural Network (ConvRNN) (Rußwurm and Ko¨rner, roles in our model. We also observe that using a learnable PEV instead of
2018), and DUal view Point deep Learning architecture for time series a fixed one does not bring significant improvement in accuracy. On the
classificatiOn (DuPLO) (Interdonato et al., 2019). For CNN-Transformer, contrary, all evaluation metrics obtained by SITS-FormerlearnablePE on
ConvRNN, and DuPLO, we made the input and output consistent with both validation sets are lower than those obtained by SITS-Former. This
our model. For RF and SITS-BERT, the input was the reflectance time may be because the lengths of annual satellite time series are short, so
series of the analyzed pixel. the use of learnable positional encodings cannot significantly affect the
For RF, we selected the best tree number in range (100, 200, 300, result, but may increase the risk of overfitting. This founding is consis-
400, 500). For ConvRNN, we utilized a Bi-GRU network with 256 hidden tent with Wang and Chen (2020), who found that fixed sinusoidal po-
states and 3 ×3 kernel size in each layer. For DuPLO and SITS-BERT, we sitional encoding method performs perfectly on short sequences.
adopted the same configurations as the authors suggested. For CNN-
Transformer, we adopted an architecture similar to SITS-Former but 5.3. Comparison with state-of-the-art methods
replacing 3D-CNNs with 2D-CNNs. As seen from Table 3, the model size
of SITS-Former is similar to SITS-BERT and CNN-Transformer, while The classification accuracy of all competing methods is reported in
much smaller than ConvRNN and DuPLO. Using the design choices Tables 6-7. Regarding non-pre-trained models, SITS-Former achieves
discussed above, SITS-Former saves around 82% of DuPLO’s the best performance in most cases. Specifically, SITS-Former and CNN-
parameters. Transformer perform equally well on the test sets, while the former
For SITS-Former, we first pre-trained it for 200 epochs and then fine- outperforms the latter on both validation sets. In addition, the pre-
tuned it on task data for 30 epochs. Adam optimizer (Kingma and Ba, trained SITS-Former performs the best among all the comparison
2014) with a batch size of 128 was used for both pre-training and fine- methods on both datasets, followed by the pre-trained CNN-Trans-
tuning. In the pre-training stage, the initial learning rate was set to 1e-4. former. Both of them yield remarkable improvements over their non-
The learning rate warmed up over the first 10 epochs and then decayed pre-trained counterparts. Specifically, for SITS-Former, the accuracy
by gamma every epoch. The value of gamma was set to 0.99. To avoid gains brought by pre-training are 3.30% OA / 3.04% AA on the Cali-
overfitting, dropout was applied to the output of all layers of SITS- fornia test set, and 2.64% OA / 3.29% AA on the Missouri test set. For
Former with a dropout rate of 0.1. We also trained all the competing CNN-Transformer, the accuracy gains brought by pre-training are 3.10%
models from scratch for 200 epochs with a learning rate of 1e-4. In order OA / 2.81% AA on the California test set, and 3.14% OA / 3.11% AA on
to objectively evaluate the quality of the pre-trained model, we also the Missouri test set.
considered the pre-trained versions of SITS-BERT (Yuan and Lin, 2021) In order to verify whether pre-training significantly improves the
and CNN-Transformer, where CNN-Transformer was pre-trained in the classification performance, we performed the one-way ANalysis Of
same way as SITS-Former. In all experiments, data augmentation was VAriance (ANOVA) test on the results of five random runs reported in
performed on the training sets. Tables 6-7 to evaluate the null hypothesis, i.e., whether pre-training a
We adopted three evaluation metrics to quantify the classification model does not affect the final classification accuracy. This test pro-
performance of different methods: Overall Accuracy (OA), Average duced a p-value for each evaluation metric. Metrics with p-values less
Accuracy (AA), and Kappa coefficient. OA and Kappa coefficient reflect than 0.05 were considered significant, meaning that the null hypothesis
the quality of classification in terms of quantity and consistency was rejected. As shown in Table 8, the p-values associated with all
respectively, while AA reflects the average performance in all classes. evaluations metrics on both datasets are extremely low. These results
Besides, we adopted the F1-score to quantify the classification accuracy support our hypothesis that SITS classification tasks can greatly benefit
of each class (Rußwurm and Ko¨rner, 2020). All the results were averaged from self-supervised pre-training when there is insufficient labeled data,
over five random data splits. even if the pre-training data and task data come from different data
distributions, just like the case of Missouri.
5.2. Ablation study We further investigate the performance of different methods on each
class. The per-class F1-scores obtained by all competing methods on test
We first analyze the impact of each component of SITS-Former on the sets are reported in Tables 9 and 10. The corresponding confusion
classification accuracy by comparing it with three variants: (1) matrices are visualized in Figs. 7 and 8. The confusion matrices are
removing the use of batch normalization (SITS-FormerwithoutBN), (2) normalized by row, whose diagonal elements represent producer’s ac-
curacy. We observe that the pre-trained SITS-Former achieves higher F1-
Table 3 scores on almost all classes over its non-pre-trained counterpart. For the
Number of trainable parameters of different deep learning models for the California dataset, the pre-trained SITS-Former achieves the highest F1-
California dataset. scores on 8 out of 13 classes. The highest performance gains induced by
Model Number of parameters (million) pre-training are observed on winter wheat, developed, walnuts, and
pistachios with an improvement of 4.64%~11% F1-score. Similarly, for
SITS-BERT 2.4
the Missouri dataset, the pre-trained SITS-Former achieves the highest
CNN-Transformer 2.5
SITS-Former 2.5 F1-scores on 7 out of 10 classes. The highest performance gains are
ConvRNN 10.2 observed on developed, grass/pasture, and woody wetlands with an
DuPLO 14.1 improvement of 5.29%~9.40% F1-score.
Except for DuPLO, the number of parameters of other models are inde- In general, it is difficult to distinguish between permanent crops such
pendent of the input length. as grape vineyards and nut trees (such as walnuts, almonds, and
7

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Table 4
Accuracy assessment for the California dataset considering different variants of SITS-Former.
Study area Model Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
California SITS-FormerwithoutBN 87.33 ±0.30 87.33 ±0.30 0.8628 ±0.0032 85.55 ±0.39 86.66 ±0.18 0.8335 ±0.0042
SITS-FormerwithoutPE 86.38 ±0.76 86.38 ±0.76 0.8517 ±0.0100 84.49 ±0.42 85.81 ±0.27 0.8217 ±0.0048
SITS-FormerlearnablePE 87.51 ±0.35 87.51 ±0.35 0.8647 ±0.0037 85.56 ±0.37 87.22 ±0.30 0.8339 ±0.0041
SITS-Former 88.41 ±0.80 88.41 ±0.80 0.8744 ±0.0086 85.53 ±0.47 87.17 ±0.42 0.8339 ±0.0049
Best results are highlighted in bold.
Note: On the validation set, OA is equal to AA.
Table 5
Accuracy assessment for the Missouri dataset considering different variants of SITS-Former.
Study area Model Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
Missouri SITS-FormerwithoutBN 88.23 ±0.53 88.23 ±0.53 0.8693 ±0.0059 89.87 ±0.42 86.42 ±0.39 0.8786 ±0.0049
SITS-FormerwithoutPE 87.27 ±0.62 87.27 ±0.62 0.8585 ±0.0069 89.48 ±0.49 86.70 ±0.35 0.8742 ±0.0057
SITS-FormerlearnablePE 87.13 ±0.48 87.13 ±0.48 0.8570 ±0.0053 89.73 ±0.47 87.31 ±0.15 0.8773 ±0.0055
SITS-Former 88.50 ±0.50 88.50 ±0.50 0.8722 ±0.0055 90.54 ±0.40 87.44 ±0.16 0.8868 ±0.0046
Table 6
Accuracy assessment considering different competing methods on the California dataset.
Method Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
RF 84.26 ±0.45 84.26 ±0.45 0.8294 ±0.0049 82.91 ±0.44 84.17 ±0.34 0.8034 ±0.0049
SITS-BERT 85.61 ±0.06 85.61 ±0.06 0.8442 ±0.0007 83.65 ±1.14 84.38 ±0.17 0.8118 ±0.0125
ConvRNN 84.31 ±0.33 84.31 ±0.33 0.8300 ±0.0036 81.46 ±0.39 82.82 ±0.28 0.7871 ±0.0042
DuPLO 86.51 ±0.70 86.51 ±0.70 0.8539 ±0.0076 84.50 ±0.25 86.20 ±0.19 0.8219 ±0.0027
CNN-Transformer 87.87 ±0.36 87.87 ±0.36 0.8686 ±0.0039 85.57 ±0.75 87.07 ±0.56 0.8336 ±0.0084
SITS-Former 88.41 ±0.80 88.41 ±0.80 0.8744 ±0.0086 85.53 ±0.47 87.17 ±0.42 0.8339 ±0.0049
SITS-BERTpretrained 89.59 ±0.50 89.59 ±0.50 0.8872 ±0.0055 87.88 ±0.08 89.12 ±0.25 0.8603 ±0.0010
CNN-Transformerpretrained 90.51 ±0.04 90.51 ±0.04 0.8972 ±0.0004 88.67 ±0.31 89.88 ±0.25 0.8693 ±0.0036
SITS-Formerpretrained 90.69 ±0.29 90.69 ±0.29 0.8992 ±0.0031 88.83 ±0.26 90.21 ±0.12 0.8806 ±0.0150
The model with subscript ’pretrained’ means that the model has been pre-trained.
Table 7
Accuracy assessment considering different competing methods on the Missouri dataset.
Method Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
RF 86.00 ±0.71 86.00 ±0.71 0.8444 ±0.0079 87.98 ±0.45 86.15 ±0.10 0.8569 ±0.0051
SITS-BERT 83.37 ±0.56 83.37 ±0.56 0.8152 ±0.0062 87.38 ±0.33 83.25 ±0.37 0.8487 ±0.0040
ConvRNN 85.83 ±0.54 85.83 ±0.54 0.8426 ±0.0060 85.87 ±0.14 83.88 ±0.89 0.8316 ±0.0018
DuPLO 87.43 ±1.36 87.43 ±1.36 0.8604 ±0.0151 89.21 ±0.28 86.69 ±0.19 0.8711 ±0.0032
CNN-Transformer 88.43 ±0.21 88.43 ±0.21 0.8715 ±0.0023 89.88 ±0.47 87.59 ±0.09 0.8793 ±0.0054
SITS-Former 88.50 ±0.50 88.50 ±0.50 0.8722 ±0.0055 90.54 ±0.40 87.44 ±0.16 0.8868 ±0.0046
SITS-BERTpretrained 89.60 ±0.43 89.60 ±0.43 0.8844 ±0.0048 92.16 ±0.28 89.44 ±0.35 0.9061 ±0.0032
CNN-Transformerpretrained 91.00 ±0.65 91.00 ±0.65 0.9000 ±0.0072 93.02 ±0.23 90.70 ±0.10 0.9163 ±0.0027
SITS-Formerpretrained 91.33 ±0.66 91.33 ±0.66 0.9037 ±0.0074 93.18 ±0.32 90.73 ±0.12 0.9184 ±0.0039
Table 8
Results of the one-way ANOVA significance test. Tests are conducted between the pre-trained and non-pre-trained models of SITS-Former and CNN-Transformer.
Method California Missouri
OA AA Kappa OA AA Kappa
CNN-Transformer 5.821e-03 2.858e-03 5.426e-03 1.035e-03 4.703e-06 9.459e-04
SITS-Former 4.308e-07 6.021e-04 1.380e-02 1.883e-03 1.812e-05 1.729e-03
pistachios) due to their similar growth patterns: vegetation vigor in mid- agricultural practices (Zhong et al., 2011). We also find that many
spring and defoliation in late-summer. The spectral trajectories of these developed pixels are incorrectly classified as winter wheat and grass/
crops mainly depend on phenological shifts, which are mostly influ- pasture, resulting in low F1-scores on these classes. This is because
enced by stable local climate and regional factors rather than developed is a mixed land-use type formed by merging four types of
8

InternationalJournalofAppliedEarthObservationandGeoinformation106(2022)102651
developed land, i.e., open space, low, medium, and high intensity.
Hence, the large misclassification may come from the heterogeneity
within the class and the existence of urban green spaces. Overall, the
pronounced improvements on these indiscernible pairs (e.g., grapes-
almonds-pistachios, developed-grass/pasture) provide evidence that
the discriminative ability of features learned through pre-training is
greatly improved.
5.4. Evaluation of pre-trained features of SITS-Former
In this set of experiments, we evaluate the quality of features learned
by the pre-trained SITS-Former without fine-tuning. We directly fed the
features extracted by the pre-trained SITS-Former to a RF classifier and
then optimized the classifier on task data (the pre-trained parameters of
SITS-Former were frozen). In this case, features were only learned from
unlabeled data without introducing task-specific priors. We call this
approach ‘RF(SITS-Formerpretrained)’. In the controlled experiments, we
used a randomly initialized SITS-Former as the feature extractor and
also trained a RF classifier on task data. We call this approach ‘RF(SITS-
Formerrandom)’. In addition, we directly applied a RF classifier to the
concatenation of flattened image patches over the whole time series as
the baseline (RF-baseline). Tables 11 and 12 report the accuracy eval-
uation results on each dataset and Tables 13 and 14 present the per-class
F1-scores on test sets. The corresponding confusion matrices are depic-
ted in Figs. 9–10.
For both datasets, RF(SITS-Formerpretrained) performs significantly
better than the other two competing methods. Specifically, RF(SITS-
Formerpretrained) outperforms the RF baseline by 3.53% OA / 2.79% AA
on the California dataset, and 0.54% OA / 1.33% AA on the Missouri
dataset. The performance gain on the Missouri dataset is less than that
achieved on the California dataset, owning to the difference in data
distribution between the pre-training data and the task data. The F1-
scores of almost all classes have improved using pre-trained features,
including classes that rarely appear in the pre-training set, such as
soybeans and woody wetlands. These results indicate that the proposed
self-supervised pre-training method can extract high-quality features
with good transfer performance. However, the untuned model (RF(SITS-
Formerpretrained)) lags behind the fully fine-tuned model (SITS-Former-
pretrained) shown in Tables 6 and 7 with a gap of 2%~4% OA, implying
that fine-tuning is critical to improving the performance of pre-trained
models on downstream tasks.
5.5. Effect of varying the number of labels
We also investigate the effect of pre-training as the number of labeled
samples increases. We trained or fine-tuned each model using varied
number of labels from 100 to 1000 per class and a fixed validation set of
1000 samples per class, and then tested all remaining labeled samples.
The results are averaged over five random seeds (Fig. 11).
We observe that the pre-trained SITS-Former obviously outperforms
all the non-pre-trained models in all cases. On the Missouri dataset, the
OA achieved by the pre-trained SITS-Former with 100 labels is compa-
rable to that of its non-pre-trained counterpart achieved with 500 labels.
Moreover, the AA achieved by the pre-trained SITS-Former with 100
labels even surpasses those of all the non-pre-trained models using 1000
labels. Among all the pre-trained models, the performance of SITS-
Former is consistently better than SITS-BERT and slightly better than
CNN-Transformer in most cases, showing that SITS-Former can better
exploit the rich information of Sentinel-2 time series.
It is also notable that the accuracy gains brought by pre-training
decrease gradually as labeled data grow. Training with 100 labels, the
pre-trained SITS-Former yields a performance gain of 2.20%~2.91% OA
and 2.66%~3.53% AA over its non-pre-trained counterpart. In contrast,
the performance gain using 1000 labels decreases to 0.11%~0.60% OA
and 1.01%~1.22% AA, which is still considerable but lower than the
difference observed with fewer labels. These results indicate that
9
9
elbaT
.sdohtem
gnitepmoc
tnereffid
gniredisnoc
tesatad
ainrofilaC
eht
rof
)%(
erocs-1F
ssalc-reP
soihcatsiP
/ssarG
tseroF
depoleveD
stunlaW
sdnomlA
surtiC
separG
seotamoT
aflaflA
taehWretniW
nottoC
nroC
dohteM
erutsaP
45.08
40.09
17.78
41.05
08.77
77.58
80.08
01.18
53.39
22.58
94.93
94.29
77.58
FR
33.08
87.09
22.58
77.84
10.57
56.58
29.97
86.18
05.39
13.58
98.54
80.49
91.08
TREB-STIS
35.77
95.98
53.68
58.64
85.37
61.58
18.77
10.97
31.29
23.28
16.24
78.19
94.77
NNRvnoC
71.68
88.19
08.78
23.05
08.77
94.58
44.18
85.18
28.29
42.58
84.45
26.39
48.58
OLPuD
34.58
22.29
34.29
32.35
39.77
92.68
90.48
16.28
25.49
15.58
06.25
96.49
94.88
remrofsnarT-NNC
56.68
04.19
13.09
37.05
50.97
14.68
93.48
72.48
22.49
74.78
37.84
68.49
07.78
remroF-STIS
80.09
99.29
99.98
22.75
42.18
58.88
15.88
15.68
55.49
12.09
30.25
34.59
31.78
deniarterpTREB-STIS
98.98
26.39
83.09
62.95
47.28
70.98
61.88
85.68
85.59
20.19
11.26
30.69
01.98
deniarterpremrofsnarT-NNC
92.19
67.39
67.09
75.95
69.58
16.88
10.78
98.68
89.59
07.19
37.95
60.69
23.78
deniarterpremroF-STIS
Y. Yuan et al.

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Table 10
Per-class F1-score (%) for the Missouri dataset considering different competing methods.
Method Corn Cotton Rice Soybeans Fallow OpenWater Developed Forest Grass/Pasture WoodyWetlands
RF 93.00 93.70 94.31 89.83 75.05 89.81 41.52 89.68 68.60 84.50
SITS-BERT 92.15 89.97 92.51 88.22 78.02 91.86 44.55 90.70 64.86 81.41
ConvRNN 90.62 87.93 94.83 86.67 76.78 84.48 41.33 90.25 66.70 79.94
DuPLO 93.11 94.87 94.72 91.59 78.09 89.02 44.84 90.50 70.50 82.72
CNN-Transformer 95.72 94.63 96.57 92.79 80.96 94.82 44.48 89.85 70.89 81.94
SITS-Former 95.93 94.67 96.63 93.40 84.13 95.68 46.28 90.50 71.25 81.82
SITS-BERTpretrained 96.39 96.26 97.00 94.54 84.33 95.20 54.08 92.09 75.80 85.22
CNN-Transformerpretrained 97.22 96.99 97.58 95.16 86.16 95.96 54.20 93.06 76.01 88.11
SITS-Formerpretrained 97.33 97.34 97.55 95.45 86.39 96.31 55.68 92.46 77.62 87.11
Fig. 7. Confusion matrices obtained on the California dataset by different comparison methods: (a) RF, (b) SITS-BERT, (c) ConvRNN, (d) DuPLO, (e) CNN-
Transformer, (f) SITS-Former, (g) pre-trained SITS-BERT, (h) pre-trained CNN-Transformer, (i) pre-trained SITS-Former.
10

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Fig. 8. Confusion matrices obtained on the Missouri dataset by different comparison methods: (a) RF, (b) SITS-BERT, (c) ConvRNN, (d) DuPLO, (e) CNN-
Transformer, (f) SITS-Former, (g) pre-trained SITS-BERT, (h) pre-trained CNN-Transformer, (i) pre-trained SITS-Former.
Table 11
Accuracy evaluation of pre-trained features of SITS-Former on the California dataset.
Method Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
RF-baseline 84.90 ±0.24 84.90 ±0.24 0.8364 ±0.0026 83.26 ±0.55 84.77 ±0.36 0.8075 ±0.0061
RF(SITS-Formerrandom) 66.54 ±0.83 66.54 ±0.83 0.6375 ±0.0090 65.57 ±1.76 66.90 ±1.44 0.6092 ±0.0189
RF(SITS-Formerpretrained) 87.95 ±0.19 87.95 ±0.19 0.8695 ±0.0021 86.79 ±0.23 87.56 ±0.11 0.8476 ±0.0027
classification tasks can benefit from pre-training even with a plenty of 5.6. Processing speed
labeled data, but the performance gains decrease as labeled data
increase. We compare the processing speed of SITS-Former with other
competing methods under the same experimental configuration
(Table 15). To be fair, only patch-based methods were compared.
11

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Table 12
Accuracy evaluation of pre-trained features of SITS-Former on the Missouri dataset.
Method Validation set Test set
OA (%) AA (%) Kappa OA (%) AA (%) Kappa
RF-baseline 86.93 ±0.63 86.93 ±0.63 0.8548 ±0.0070 88.62 ±0.34 86.69 ±0.22 0.8644 ±0.0039
RF(SITS-Formerrandom) 64.23 ±1.65 64.23 ±1.65 0.6026 ±0.0184 60.46 ±2.00 64.36 ±1.20 0.5427 ±0.0212
RF(SITS-Formerpretrained) 88.17 ±0.33 88.17 ±0.33 0.8685 ±0.0037 89.16 ±0.30 88.02 ±0.16 0.8710 ±0.0035
Table 13
Per-class F1-score (%) evaluation of pre-trained features of SITS-Former on the California dataset.
Method Corn Cotton WinterWheat Alfalfa Tomatoes Grapes Citrus Almonds Walnuts Developed Forest Grass/ Pistachios
Pasture
RF-baseline 84.58 92.46 38.72 85.20 92.15 81.07 80.12 85.79 80.07 51.51 88.68 90.49 81.28
RF(SITS- 37.56 78.20 27.47 71.98 64.65 65.55 48.98 66.74 48.31 43.08 77.91 79.77 61.35
Formerrandom)
RF(SITS- 77.74 93.27 58.44 88.85 94.08 83.97 86.65 87.91 80.72 56.56 90.49 93.54 87.63
Formerpretrained)
Table 14
Per-class F1-score (%) evaluation of pre-trained features of SITS-Former on the Missouri dataset.
Method Corn Cotton Rice Soybeans Fallow OpenWater Developed Forest Grass/Pasture Woody
Wetlands
RF-baseline 92.93 94.66 93.64 90.47 76.10 86.23 42.82 90.60 73.44 84.99
RF(SITS-Formerrandom) 76.28 75.61 56.28 49.10 35.09 65.75 18.25 76.68 44.27 65.62
RF(SITS-Formerpretrained) 96.05 94.42 95.85 91.07 69.79 96.88 44.64 91.68 74.26 86.07
Fig. 9. Confusion matrices obtained on the California dataset by (a) RF-baseline, (b) RF(SITS-Formerpretrained), (c) RF(SITS-Formerrandom).
Fig. 10. Confusion matrices obtained on the Missouri dataset by (a) RF-baseline, (b) RF(SITS-Formerpretrained), (c) RF(SITS-Formerrandom).
12

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Fig. 11. Accuracy evaluations of different comparison methods using varied number of labels. The first line shows the results on the California dataset, and the
second line shows the results on the Missouri dataset: (a)(d) OA, (b)(e) AA, (c)(f) Kappa coefficient.
The advantages of SITS-Former are as follows. First, SITS-Former
Table 15
allows for the integration of spatial, spectral, and temporal informa-
The number of samples processed per second.
tion of Sentinel-2 time series, and is more computationally efficient
Model Samples per second compared to RNN-based models. In addition, benefitting from pre-
ConvRNN 190 training, SITS-Former effectively alleviates the demand for enough
DuPLO 352 labeled data and significantly improves the performance on label-scarce
CNN-Transformer 385 SITS classification tasks. There are also other types of approaches to
SITS-Former 384
address the issue of insufficient labels, including weakly supervised
learning (Ienco et al., 2020; Wang et al., 2020), semi-supervised learning
Compared to RNN-based models (ConvRNN and DuPLO), (Solano-Correa et al., 2019), knowledge distillation (Bazzi et al., 2020),
Transformer-based models (SITS-Former and CNN-Transformer) are etc. The proposed self-supervised pre-training method in this study can
computationally more efficient. The processing speed of SITS-Former is be used as a complementary tool to the existing approaches to ease the
almost equivalent to that of CNN-Transformer, indicating that the use of burden of data annotation.
3D convolutions will not cause a significant drop in efficiency. Another However, as a patch-based model, SITS-Former needs to process
interesting finding is that the pre-trained model converges to an optimal every pixel individually at inference time, which is very time-consuming
solution much faster than a non-pre-trained one (Fig. 12). The optimal when mapping large areas. It is necessary to develop end-to-end models
number of epochs for fine-tuning SITS-Former is 17 on average, while for semantic segmentation of SITS, such as in Garnot and Landrieu
training the same model from scratch needs at least twice as many (2021), in which all pixels are labeled at once. However, semantic
epochs. These facts underline that the pre-trained SITS-Former is more segmentation models also rely on sufficient labeled data to learn pixel
suitable for handling large-scale datasets. classification and spatial arrangement between classes (Interdonato
et al., 2019). Designing effective self-supervised proxy tasks for training
6. Discussion such models is challenging and we leave this to future work.
In this paper, we proposed a pre-trained deep learning model called 7. Conclusion
SITS-Former to classify Sentinel-2 time series, which has shown prom-
ising results for crop classification in two experimental areas. In this study, we introduced SITS-Former, which is the first pre-
13

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Fig. 12. The first line shows the learning curves of (a) pre-trained SITS-Former and (b) non-pre-trained SITS-Former on the California dataset. The second line shows
the learning curves of (c) pre-trained SITS-Former and (d) non-pre-trained SITS-Former on the Missouri dataset.
trained representation model for patch-based SITS classification. SITS- Acknowledgments
Former is pre-trained on large-scale unlabeled Sentinel-2 time series in
a self-supervised manner. It can be easily adapted to a downstream This research was supported by the National Natural Science Foun-
classification task through fine-tuning. Extensive experiments show that dation of China (Grant No. 41901356, 61906096, 41701512) and by the
SITS-Former outperforms state-of-the-art approaches and offers signifi- Natural Science Foundation of Jiangsu Province under Grant
cant improvements over traditional supervised models, especially when BK20180786.
labeled data is scarce. We hope that SITS-Former will make deep
learning more accessible to SITS-related applications as it greatly re- References
duces the burden of manual labeling.
Several aspects still need to be explored. For instance, we consider Anwer, R.M., Khan, F.S., van de Weijer, J., Molinier, M., Laaksonen, J., 2018. Binary
patterns encoded convolutional neural networks for texture recognition and remote
extensions of SITS-Former to fuse Sentinel-1 and Sentinel-2 data as sensing scene classification. ISPRS J. Photogram. Remote Sens. 138, 74–85. https://
exciting future work. It is also important to explore better proxy tasks to doi.org/10.1016/j.isprsjprs.2018.01.023.
learn more effective representations. Bazzi, H., Ienco, D., Baghdadi, N., Zribi, M., Demarez, V., 2020. Distilling Before Refine:
Spatio-Temporal Transfer Learning for Mapping Irrigated Areas Using Sentinel-1
Time Series. IEEE Geosci. Remote Sens. Lett. 17 (11), 1909–1913.
8. Author statement Benedetti, P., Ienco, D., Gaetano, R., Ose, K., Pensa, R.G., Dupuy, S., 2018. M3Fusion: A
Deep Learning Architecture for Multiscale Multimodal Multitemporal Satellite Data
Fusion. IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens. 11, 4939–4949.
We declare that this manuscript is original, has not been published
https://doi.org/10.1109/Jstars.2018.2876357.
before and is not currently being considered for publication elsewhere. Boryan, C., Yang, Z., Mueller, R., Craig, M., 2011. Monitoring US agriculture: the US
We confirm that the manuscript has been read and approved by all the Department of Agriculture, National Agricultural Statistics Service, Cropland Data
authors and that there are no other persons who satisfied the criteria for Layer Program. Geocarto Int 26 (5), 341–358. https://doi.org/10.1080/
10106049.2011.562309.
authorship but are not listed. We further confirm that the order of au- Chen, T., Kornblith, S., Norouzi, M., Hinton, G., 2020. A Simple Framework for
thors listed in the manuscript has been approved by all of us. Contrastive Learning of Visual Representations, 37th International Conference on
Machine Learning. International Machine Learning Society (IMLS), Virtual, Online,
pp. 1575-1585.
Declaration of Competing Interest
Cheng, G., Yang, C., Yao, X., Guo, L., Han, J., 2018. When Deep Learning Meets Metric
Learning: Remote Sensing Image Scene Classification via Learning Discriminative
The authors declare that they have no known competing financial CNNs. IEEE Trans. Geosci. Remote Sens. 56 (5), 2811–2821.
Cheng, G., Zhou, P., Han, J., 2016. Learning Rotation-Invariant Convolutional Neural
interests or personal relationships that could have appeared to influence
Networks for Object Detection in VHR Optical Remote Sensing Images. IEEE Trans.
the work reported in this paper. Geosci. Remote Sens. 54 (12), 7405–7415.
14

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Devlin, J., Chang, M.-W., Lee, K., Toutanova, K., 2019. BERT: Pre-training of Deep time series over large areas. Remote Sens. Environ. 187, 156–168. https://doi.org/
Bidirectional Transformers for Language Understanding, 2019 Conference of the 10.1016/j.rse.2016.10.010.
North American Chapter of the Association for Computational Linguistics: Human Pelletier, C., Valero, S., Inglada, J., Champion, N., Marais Sicre, C., Dedieu, G., 2017.
Language Technologies. Association for Computational Linguistics (ACL), Effect of Training Class Label Noise on Classification Performances for Land Cover
Minneapolis, MN, United states, pp. 4171-4186. Mapping with Satellite Image Time Series. Remote Sens. 9 (2), 173. https://doi.org/
do Nascimento Bendini, H., Garcia Fonseca, L.M., Schwieder, M., Sehn Ko¨rting, T., 10.3390/rs9020173.
Rufin, P., Del Arco Sanches, I., Leita˜o, P.J., Hostert, P., 2019. Detailed agricultural Pelletier, C., Webb, G., Petitjean, F., 2019. Temporal Convolutional Neural Network for
land classification in the Brazilian cerrado based on phenological information from the Classification of Satellite Image Time Series. Remote Sens. 11 (5), 523. https://
dense satellite image time series. Int. J. Appl. Earth Obs. Geoinf. 82, 101872. https:// doi.org/10.3390/rs11050523.
doi.org/10.1016/j.jag.2019.05.005. Perez, L., Wang, J., 2017. The Effectiveness of Data Augmentation in Image Classification
Dong, H., Ma, W., Wu, Y., Zhang, J., Jiao, L., 2020. Self-Supervised Representation using Deep Learning. arXiv e-prints, arXiv:1712.04621.
Learning for Remote Sensing Image Change Detection Based on Temporal Prediction. Phiri, D., Simwanda, M., Salekin, S., Nyirenda, V., Murayama, Y., Ranagalage, M., 2020.
Remote Sens. 12 (11), 1868. https://doi.org/10.3390/rs12111868. Sentinel-2 Data for Land Cover/Use Mapping: A Review. Remote Sens. 12 (14),
Eudes Gbodjo, Y.J., Ienco, D., Leroux, L., 2020. Toward Spatio-Spectral Analysis of 2291. https://doi.org/10.3390/rs12142291.
Sentinel-2 Time Series Data for Land Cover Mapping. IEEE Geosci. Remote Sens. Qiu, XiPeng, Sun, TianXiang, Xu, YiGe, Shao, YunFan, Dai, N., Huang, XuanJing, 2020.
Lett. 17 (2), 307–311. Pre-trained models for natural language processing: A survey. Sci. China Technol.
Feng, S., Zhao, J., Liu, T., Zhang, H., Zhang, Z., Guo, X., 2019. Crop Type Identification Sci. 63 (10), 1872–1897. https://doi.org/10.1007/s11431-020-1647-3.
and Mapping Using Machine Learning Algorithms and Sentinel-2 Time Series Data. Rußwurm, M., Ko¨rner, M., 2017. Temporal Vegetation Modelling Using Long Short-Term
IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens. 12 (9), 3295–3306. Memory Networks for Crop Identification from Medium-Resolution Multi-spectral
Garnot, V.S., Landrieu, L., 2021. Panoptic Segmentation of Satellite Image Time Series Satellite Images. In: Proceedings of the 30th IEEE Conference on Computer Vision
with Convolutional Temporal Attention Networks. In: Proceedings of the IEEE/CVF and Pattern Recognition Workshops, pp. 1496–1504. https://doi.org/10.1109/
International Conference on Computer Vision (ICCV), pp. 4872–4881. CVPRW.2017.193.
Garnot, V.S., Landrieu, L., Giordano, S., Chehata, N., 2019. In: Time-Space Tradeoff in Rußwurm, M., Ko¨rner, M., 2018. Multi-Temporal Land Cover Classification with
Deep Learning Models for Crop Classification on Satellite Multi-Spectral Image Time Sequential Recurrent Encoders. ISPRS Int. J. Geo-Inform. 7 (4), 129. https://doi.org/
Series. IEEE, Yokohama, Japan, pp. 6247–6250. https://doi.org/10.1109/ 10.3390/ijgi7040129.
IGARSS.2019.8900517. Rußwurm, M., Ko¨rner, M., 2020. Self-attention for raw optical Satellite Time Series
Hang, R., Li, Z., Ghamisi, P., Hong, D., Xia, G., Liu, Q., 2020. Classification of Classification. ISPRS J. Photogram. Remote Sens. 169, 421–435. https://doi.org/
Hyperspectral and LiDAR Data Using Coupled CNNs. IEEE Trans. Geosci. Remote 10.1016/j.isprsjprs.2020.06.006.
Sens. 58 (7), 4939–4950. Saha, S., Bovolo, F., Bruzzone, L., 2020. Change Detection in Image Time-Series Using
Hang, R., Li, Z., Liu, Q., Ghamisi, P., Bhattacharyya, S.S., 2021. Hyperspectral Image Unsupervised LSTM. IEEE Geosci. Remote Sens. Lett. 1–5 https://doi.org/10.1109/
Classification With Attention-Aided CNNs. IEEE Trans. Geosci. Remote Sens. 59 (3), lgrs.2020.3043822.
2281–2293. Salehi Shahrabi, H., Ashourloo, D., Moeini Rad, A., Aghighi, H., Azadbakht, M.,
Ienco, D., Eudes Gbodjo, Y.J., Interdonato, R., Gaetano, R., 2020. Attentive Weakly Nematollahi, H., 2020. Automatic silage maize detection based on phenological rules
Supervised land cover mapping for object-based satellite image time series data with using Sentinel-2 time-series dataset. Int. J. Remote Sens. 41 (21), 8406–8427.
spatial interpretation. arXiv e-prints, arXiv:2004.14672. https://doi.org/10.1080/01431161.2020.1779377.
Ienco, D., Gaetano, R., Dupaquier, C., Maurel, P., 2017. Land Cover Classification via Sheeren, D., Fauvel, M., Josipovi´c, V., Lopes, M., Planque, C., Willm, J., Dejoux, J.-F.,
Multitemporal Spatial Data by Deep Recurrent Neural Networks. IEEE Geosci. 2016. Tree Species Classification in Temperate Forests Using Formosat-2 Satellite
Remote Sens. Lett. 14 (10), 1685–1689. Image Time Series. Remote Sens. 8 (9), 734. https://doi.org/10.3390/rs8090734.
Interdonato, R., Ienco, D., Gaetano, R., Ose, K., 2019. DuPLO: A DUal view Point deep Solano-Correa, Y.T., Bovolo, F., Bruzzone, L., 2019. In: A Semi-Supervised Crop-Type
Learning architecture for time series classificatiOn. ISPRS J. Photogram. Remote Classification Based on Sentinel-2 NDVI Satellite Image Time Series And
Sens. 149, 91–104. https://doi.org/10.1016/j.isprsjprs.2019.01.011. Phenological Parameters. IEEE, Yokohama, Japan, pp. 457–460. https://doi.org/
Ioffe, S., Szegedy, C., 2015. Batch Normalization: Accelerating Deep Network Training by 10.1109/IGARSS.2019.8897922.
Reducing Internal Covariate Shift, p. arXiv Preprint arXiv:1502.03167. Solano-Correa, Y.T., Bovolo, F., Bruzzone, L., Fernandez-Prieto, D., 2020. A Method for
Ji, S., Zhang, C., Xu, A., Shi, Y., Duan, Y., 2018. 3D Convolutional Neural Networks for the Analysis of Small Crop Fields in Sentinel-2 Dense Time Series. IEEE Trans.
Crop Classification with Multi-Temporal Remote Sensing Images. Remote Sens. 10 Geosci. Remote Sens. 58 (3), 2150–2164.
(2), 75. https://doi.org/10.3390/rs10010075. Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., Salakhutdinov, R., 2014.
Jing, L., Tian, Y., 2020. Self-supervised Visual Feature Learning with Deep Neural Dropout: A Simple Way to Prevent Neural Networks from Overfitting. J. Mach.
Networks: A Survey. IEEE Trans Pattern Anal Mach Intell 43 (11), 4037–4058. Learn. Res. 15, 1929–1958.
https://doi.org/10.1109/TPAMI.2020.2992393. Sun, Z., Di, L., Fang, H., 2019. Using long short-term memory recurrent neural network
Kingma, D.P., Ba, J., 2014. Adam: A method for stochastic optimization, arXiv preprint in land cover classification on Landsat and Cropland data layer time series. Int. J.
arXiv:1412.6980. Remote Sens. 40 (2), 593–614. https://doi.org/10.1080/01431161.2018.1516313.
Kolesnikov, A., Zhai, X.H., Beyer, L., 2019. Revisiting Self-Supervised Visual Tao, C., Qi, J., Lu, W., Wang, H., Li, H., 2020. Remote Sensing Image Scene Classification
Representation Learning, Proceedings of the IEEE Conference on Computer Vision With Self-Supervised Paradigm Under Limited Labeled Samples. IEEE Geosci.
and Pattern Recognition (CVPR), pp. 1920-1929 DOI: 10.1109/Cvpr.2019.00202. Remote Sens. Lett. 1–5 https://doi.org/10.1109/LGRS.2020.3038420.
Lebourgeois, V., Dupuy, S., Vintrou, E ´ ., Ameline, M., Butler, S., B´egu´e, A., 2017. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.,
A Combined Random Forest and OBIA Classification Scheme for Mapping Polosukhin, I., 2017. Attention Is All You Need. In: 31st Annual Conference on
Smallholder Agriculture at Different Nomenclature Levels Using Multisource Data Neural Information Processing Systems, pp. 5999–6009.
(Simulated Sentinel-2 Time Series, VHRS and DEM). Remote Sens. 9 (3), 259. Vincenzi, S., Porrello, A., Buzzega, P., Cipriano, M., Fronte, P., Cuccu, R., Ippoliti, C.,
https://doi.org/10.3390/rs9030259. Conte, A., Calderara, S., 2021. The color out of space: learning self-supervised
Lei Ba, J., Kiros, J.R., Hinton, G.E., 2016. Layer Normalization. arXiv e-prints, arXiv: representations for Earth Observation imagery. In: Proceedings of the 25th
1607.06450. International Conference on Pattern Recognition, pp. 3034–3041. https://doi.org/
Li, H., Zhang, C.e., Zhang, S., Atkinson, P.M., 2020a. Crop classification from full-year 10.1109/ICPR48806.2021.9413112.
fully-polarimetric L-band UAVSAR time-series using the Random Forest algorithm. Waldner, F., Diakogiannis, F.I., 2020. Deep learning on edge: Extracting field boundaries
Int. J. Appl. Earth Obs. Geoinf. 87, 102032. https://doi.org/10.1016/j. from satellite images with a convolutional neural network. Remote Sens. Environ.
jag.2019.102032. 245, 111741. https://doi.org/10.1016/j.rse.2020.111741.
Li, W.Y., Chen, H., Shi, Z.W., 2021. Semantic Segmentation of Remote Sensing Images Wang, H., Zhao, X., Zhang, X., Wu, D., Du, X., 2019. Long Time Series Land Cover
With Self-Supervised Multitask Representation Learning. IEEE J. Sel. Topics Appl. Classification in China from 1982 to 2015 Based on Bi-LSTM Deep Learning. Remote
Earth Observ. Remote Sens. 14, 6438–6450. https://doi.org/10.1109/ Sens. 11 (14), 1639. https://doi.org/10.3390/rs11141639.
Jstars.2021.3090418. Wang, M.o., Wang, J., Chen, L.i., 2020. Mapping Paddy Rice Using Weakly Supervised
Li, Z., Chen, G., Zhang, T., 2020b. A CNN-Transformer Hybrid Approach for Crop Long Short-Term Memory Network with Time Series Sentinel Optical and SAR
Classification Using Multitemporal Multisensor Images. IEEE J. Sel. Topics Appl. Images. Agriculture 10 (10), 483. https://doi.org/10.3390/agriculture10100483.
Earth Observ. Remote Sens. 13, 847–858. Wang, S., Quan, D., Liang, X., Ning, M., Guo, Y., Jiao, L., 2018. A deep learning
Liu, W., Gopal, S., Woodcock, C.E., 2004. Uncertainty and Confidence in Land Cover framework for remote sensing image registration. ISPRS J. Photogram. Remote Sens.
Classification Using a Hybrid Classifier Approach. Photogramm Eng Remote Sensing 145, 148–164. https://doi.org/10.1016/j.isprsjprs.2017.12.012.
70 (8), 963–971. Wang, Y.A., Chen, Y.N., 2020. What Do Position Embeddings Learn? An Empirical Study
Liu, X., Zhang, F., Hou, Z., Mian, L., Wang, Z., Zhang, J., Tang, J., 2021. Self-supervised of Pre-Trained Language Model Positional Encoding. In: Proceedings of the 2020
Learning: Generative or Contrastive. IEEE Transactions on Knowledge and Data Conference on Empirical Methods in Natural Language Processing, pp. 6840–6849.
Engineering 1–1. https://doi.org/10.1109/tkde.2021.3090866. Yuan, Y., Lin, L., 2021. Self-Supervised Pretraining of Transformers for Satellite Image
Minaee, S., Kalchbrenner, N., Cambria, E., Nikzad, N., Chenaghlu, M., Gao, J., 2021. Time Series Classification. IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens. 14,
Deep Learning–based Text Classification. ACM Comput Surv 54 (3), 1–40. https:// 474–487.
doi.org/10.1145/3439726. Yuan, Y., Lin, L., Huo, L.-Z., Kong, Y.-L., Zhou, Z.-G., Wu, B., Jia, Y., 2020. Using An
Misra, G., Cawkwell, F., Wingler, A., 2020. Status of Phenological Research Using Attention-Based LSTM Encoder–Decoder Network for Near Real-Time Disturbance
Sentinel-2 Data: A Review. Remote Sens. 12 (17), 2760. https://doi.org/10.3390/ Detection. IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens. 13, 1819–1832.
rs12172760. Yue, J., Fang, L., Rahmani, H., Ghamisi, P., 2021. Self-Supervised Learning With
Pelletier, C., Valero, S., Inglada, J., Champion, N., Dedieu, G., 2016. Assessing the Adaptive Distillation for Hyperspectral Image Classification. IEEE Trans. Geosci.
robustness of Random Forests to map land cover with high resolution satellite image Remote Sens. 60, 1–13. https://doi.org/10.1109/TGRS.2021.3057768.
15

Y. Yuan et al. I n t e r n a t i o n a l J o u r n a l o f A p p l i e d E a r t h O b s e r v a t i o n a n d G e o i n f o r m a t i o n 106(2022)102651
Zhang, M., Li, W., Du, Q., 2018. Diverse Region-Based CNN for Hyperspectral Image Zhong, L., Hawkins, T., Biging, G., Gong, P., 2011. A phenology-based approach to map
Classification. IEEE Trans. Image Process 27 (6), 2623–2634. crop types in the San Joaquin Valley. California. Int. J. Remote Sens. 32 (22),
Zhao, W., Qu, Y., Chen, J., Yuan, Z., 2020a. Deeply synergistic optical and SAR time 7777–7804. https://doi.org/10.1080/01431161.2010.527397.
series for crop dynamic monitoring. Remote Sens. Environ. 247, 111952. https:// Zhong, L.H., Hu, L.N., Zhou, H., 2019. Deep learning based multi-temporal crop
doi.org/10.1016/j.rse.2020.111952. classification. Remote Sens. Environ. 221, 430–443. https://doi.org/10.1016/j.
Zhao, Z., Luo, Z.e., Li, J., Chen, C., Piao, Y., 2020b. When Self-Supervised Learning Meets rse.2018.11.032.
Scene Classification: Remote Sensing Scene Classification Based on a Multitask Zhu, Z., Woodcock, C.E., 2014. Continuous change detection and classification of land
Learning Framework. Remote Sens. 12 (20), 3276. https://doi.org/10.3390/ cover using all available Landsat data. Remote Sens. Environ. 144, 152–171. https://
rs12203276. doi.org/10.1016/j.rse.2014.01.011.
16