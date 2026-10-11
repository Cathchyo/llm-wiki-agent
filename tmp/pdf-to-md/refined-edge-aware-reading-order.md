International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Contents lists available at ScienceDirect

International Journal of Applied Earth
Observation and Geoinformation
journal homepage: www.elsevier.com/locate/jag

A refined edge-aware convolutional neural networks for agricultural
parcel delineation
Rui Lu a , Yingfan Zhang a , Qiting Huang b , Penghao Zeng a , Zhou Shi a , Su Ye a, c, *
a

Institute of Agricultural Remote Sensing and Information Technology Application, College of Environmental and Resource Sciences, Zhejiang University, Hangzhou
310058, China
b
Agricultural Science and Technology Information Research Institute, Guangxi Academy of Agricultural Sciences, Nanning 530007, China
c
Key Laboratory of Environment Remediation and Ecological Health, Ministry of Education, College of Environmental Resource Sciences, Zhejiang University, 310058
Hangzhou, China

A R T I C L E I N F O

A B S T R A C T

Keywords:
Agricultural parcels
Convolutional neural networks
Edge detection
Deep supervision
Boundary refinement

Accurate delineation of agricultural parcels is crucial for ensuring food security and implementing precision
agriculture practices. However, one of the primary challenges in parcel delineation revolves around the accurate
extraction of parcel edges due to the diverse morphologies of these parcels. Current deep learning models for
agricultural parcel delineation often produce unclosed or incomplete edges, highlighting the need to enhance the
edge-awareness of the model. In this study, we proposed a refined edge-aware U-Net (REAUNet) to extract accurate agricultural parcel boundaries from Sentinel-2 images and GF-2 images. REAUNet integrates four innovative components for edge enhancement, i.e., the deep supervision, the edge detection block, the dual attention
block and the refine module. The edge detection block and the dual attention block strengthen the ability of
capturing spatial contextual information, and the deep supervision constrains parcel delineation across multiple
scales, and the refine module further refines the parcel edges. Together, these components enhance the edgeawareness of the model, resulting in more accurate agricultural parcel delineation. From the ablation experiment, REAUNet with all four components reached the higher accuracy than the scenarios that only three out of
four components were retained, which suggested that the inclusion of all four components was essential. The
comparative evaluation showed that our proposed model surpassed the representative deep learning models for
both thematic and geomantic accuracy. REAUNet demonstrated an increase of 2.0 % in F1-score and a decrease
of 3.4 % in GTC (Global Total-Classification) compared to the SEANet, and exhibited a 0.8 % increase in IoU and
a 2 % decrease in GTC relative to the MPSPNet. We also assessed the capability of the REAUNet model transferred for a new geographic region, and reported that a pre-train REAUNet model with only a small number of
local samples could achieve a satisfactory accuracy. To conclude, the newly proposed REAUNet model reaches a
high mapping accuracy for delineating agricultural parcels from the high-resolution images. With the powerful
edge-aware capability, REAUNet can effectively utilize limited training samples to transfer a deep learning model
for a new region, facilitating the generation of agricultural parcel products and a large-scale agricultural parcel
mapping in practical applications.

1. Introduction
With global population growth and climate change, food security has
become a significant concern worldwide (Godfray et al., 2010; Lu et al.,
2015). Numerous efforts were made to address various facets of this
challenge, including field yield enhancement (Garibaldi et al., 2016;
Pywell et al., 2015), climate adaptation and risk management (Kuang
et al., 2022), cropping intensity monitoring (Huang et al., 2024),

industrialized agriculture expansion (Liu et al., 2021a). The success of
these efforts is contingent on the availability of highly accurate
geographic information on agricultural parcels (Potapov et al., 2022;
Zabel et al., 2019). Particularly, parcel boundary maps could deliver
fine-scale information on the size, geometry and spatial locations of
agricultural parcel, potentially providing key inputs to the applications
such as parcel size analysis (Estes et al., 2022), crop type mapping (Cai
et al., 2018), crop yield forecasting (Lobell et al., 2015) and natural

* Corresponding author.
E-mail address: su.ye@zju.edu.cn (S. Ye).
https://doi.org/10.1016/j.jag.2024.104084
Received 14 April 2024; Received in revised form 2 August 2024; Accepted 5 August 2024
Available online 16 August 2024
1569-8432/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/bync-nd/4.0/).

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

disaster monitoring (Ye et al., 2021).
While enormous efforts have been made to map agricultural parcel
using satellite-based technology, few datasets are available on agricultural parcel boundaries. The major impediment is that parcel boundaries
tend to intergrade with surrounding vegetation from optical satellite
images, leading to an algorithmic challenge for boundary detection. The
edge detector was widely applied to delineate parcel boundaries by
identifying object edges as discontinuities of image brightness
(Crommelinck et al., 2017; Graesser and Ramankutty, 2017; Turker and
Kok, 2013; Yan and Roy, 2014), but often failed to generate satisfactory
segmentation results (Waldner and Diakogiannis, 2020). An edge detector computes an image gradient using an image filtering/kernel. The
gradient threshold required by the edge detector for identification is
universally unavailable for the whole image. Besides, the parcel sizes
often vary from 0.01 to 100 ha (Waldner and Diakogiannis, 2020),
which poses a knotty challenge on detecting multiscale boundaries. A
delineation of a smaller parcel is more prone to noise against a larger
parcel. As a result, we are often unable to apply one edge detector with a
gradient threshold for parcel segmentation (Crommelinck et al., 2017;
Hong et al., 2021).
To enable a more accurate delineation of crop boundary and extent,
Convolutional Neural Network (CNN) has been widely applied to map
agricultural parcel recently (Persello et al., 2019; Taravat et al., 2021;
Waldner and Diakogiannis, 2020; Zhang et al., 2020). CNN is capable of
learning complex hierarchical contextual features (Yuan et al., 2021),
thereby mapping accurate parcels for various crop types in multiple
scales. Among the various CNN algorithms, they can be broadly categorized into three types: model refinement, multi-modal methods, and
multi-task learning methods. Model refinement primarily aims to
enhance model performance by modifying the model architecture.
Zhang et al. (2020) demonstrated MPSPNet to combine low-level and
high-level information. The low-level information captures edge details
related to object boundaries, while the high-level information learns
long-range spatial dependencies, both of which aid in the recognition of
agricultural parcels. Waldner and Diakogiannis (2020) proposed
ResUNet-a, which incorporates parallel branching atrous convolutions.
This enables multi-scale feature extraction and fusion across different
receptive fields. Pan et al. (2023) proposed the E2EVAP framework to
extract the vertices of each parcel boundary individually, where
semantic-contour interaction and topological loss were used to aggregate foreground features and establish topological relationships. This
approach has multiple directions for model improvement, allowing the
model to focus on different kinds of situations. Multi-modal methods use
multiple data as complementary information to improve parcel extraction accuracy. Cai et al. (2023a) proposed DSTFNet, which integrates
high-resolution images with medium-resolution time-series images. This
model captures spectral dynamics, aiding in the extraction of diverse
agricultural parcels. Sun et al. (2022) combined multi-temporal optical
and SAR remote sensing data to address the limitations of optical data
availability, especially in cloudy and rainy region. This approach compensates for the shortcomings of using a single data source. However, it
can present challenges related to data collection and availability. Multitask learning methods enable the model to simultaneously extract
correlated information, such as parcel extent and parcel edges. Long
et al. (2022) proposed BsiNet with multi-task learning and attention
mechanism to better delineate agricultural parcels. Wang et al. (2023)
introduced BSNet, which employs multitask learning to extract agricultural parcels and their edges, and then fuses these results to produce
the final output. However, multi-task learning is a training approach
that does not alter the model structure and does not inherently enhance
the model ability to better focus on edges.
Despite their impressive accuracy, current deep learning models still
face limitations in delineating agricultural parcels with varying morphologies and complex shapes (Lesiv et al., 2019; Zhang et al., 2021).
Many CNN-based approaches might lose edge information during the
backpropagation process, causing vanishing gradient issue. To tackle

this issue, Li et al. (2023) presented an edge-aware SEANet incorporated
local and global edge semantics at multiple levels to derive more accurate agricultural parcel extraction. While SEANet demonstrated efficacy
in delineating agricultural parcels of diverse shapes and sizes, the
method exhibited certain limitations. Primarily, the proposed edgeaware approach generates edge feature representations by using 1 × 1
convolutions from the scratch which requires considerable training
samples to achieve an acceptable accuracy. Additionally, the extracted
agricultural parcel boundaries were either indistinct or obscured by
surrounding land covers (Li et al., 2023), suggesting more edge refinement needed on the segmentation results.
In this study, our aim was to delineate agricultural parcels with
boundaries that are both precise and geometrically sound, employing a
deep learning model integrated with refined edge-aware methods. We
developed a sematic segmentation neural network, named Refined
Edge-Aware U-Net (REAUNet), to enable an extraction of multi-scale
parcel information and fine-tune parcel edge. REAUNet contains four
innovative components to enhance its ability of delineating parcel
boundaries: the deep supervision, the edge detection block, the dual
attention block and the refine module. Different with the previous work
such as SEANet, REAUNet directly integrates traditional edge detection
operators instead of data-driven tuning, which allows the model to
diminish the reliance on extensive labeled dataset and to reduce the
required volume of local samples for spatial generalization. Finally, the
model performance will be assessed in comparison to other state-of-theart deep learning models. The main contributions are:
(1) developing a refined edge-aware deep learning model to effectively delineate agricultural parcels from remote sensing images;
(2) formulating a post-processing workflow to optimize the geometry
and shape of extracted parcels;
(3) demonstrating the capability for utilizing limited samples to
transfer a trained model for a new region.
2. Study areas and datasets
2.1. Study areas
Four testing sites were selected to evaluate our method (Fig. 1): the
Netherlands (NL), Denmark (DK), and two regions Huantai (HT) and
Tarim River (TR) in China. Two image sources were tested, i.e., 10-m
Sentinel-2 and 1-m Gaofen-2 (GF-2) images. Sentinel-2 images were
acquired from Google Earth Engine (GEE) for the areas NL and DK,
which were preprocessed through atmospheric correction, radiometric
correction, geometric correction, and terrain correction. We chose data
for the year 2022 with cloud cover less than 10 %. A temporal
compositing technique was employed to generate composite data
covering the entire study area based on the mean value. The reference
data for agricultural parcels in NL was available from the Basisregistratie
Gewaspercelen (BRP) (https://www.pdok.nl/introductie/-/article/basi
sregistratie-gewaspercelen-brp-), while corresponding data in DK was
sourced from the European Union Land Parcel Identification System
(LPIS) (https://collections.eurodatacube.com/). The polygons of agricultural parcels in BRP and LPIS were manually created by the agencies.
The other two study regions in China comprised of HT in Shandong
Province, and TR in Xinjiang Province. High-resolution GF-2 images
were obtained respectively on March 2022 for HT, and on September
2022 for TR. The preprocessing steps for GF-2 imagery included atmospheric correction, radiometric calibration, geometric correction, and
PAN sharpening, resulting in the final 1-m resolution multispectral data.
The ground truth parcels for GF-2 imagery were crafted through manual
annotation.
The four regions cover a diversity of agricultural systems. In the NL
area, agricultural parcels are diverse, including well-organized largescale parcels, intensive narrow parcels, and irregular parcels. The main
crops are ornamental crops, potatoes, sugar beet, maize, cereals, and
2

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 1. Overview of four study areas including (a) Netherlands (NL), (b) Denmark (DK), (c) Huantai (HT) and (d) Tarim River (TR). Sentinel-2 images were selected
for (a) NL and (b) DK, and GF-2 images were selected for (c) HT and (d) TR. The data from (b) DK and (d) TR were exclusively used in the transfer experiment. The
red boxes denote the data utilized for training and validation, while the yellow boxes represent the test data. (For interpretation of the references to color in this
figure legend, the reader is referred to the web version of this article.)

onions. While similar to NL with well-organized agricultural parcels, DK
also includes smaller, more irregularly shaped parcels due to its diversified terrain, with barley, wheat, rapeseed, and corn as the primary
crops. These two areas require the model to delineate different patterns
and complex boundaries of agricultural parcels. In the HT area, agricultural parcels vary in size and shape, predominantly cultivated for
wheat and corn with parcels at different sizes. The XJ area features vast
land resources with large agricultural parcels mixed with smaller,
irregular ones. The differences among the four areas highlight the
challenge of calling for model’s versatility and generalizability across
various landscapes.

3. Methods
The workflow of our study is illustrated in Fig. 2. After image preprocessing, we will train the new Refined Edge-Aware U-Net (REAUNet)
model which consisted of four innovative components for an improved
agricultural parcel identification, then apply a post-processing step to
enhance edge delineation, and finally perform a multi-angle accuracy
assessment.
3.1. Refined edge-aware U-Net (REAUNet)
We developed the architecture of our proposed REAUNet based upon
U-Net (Ronneberger et al., 2015) with four innovative components
(Fig. 3). The proposed architecture adopts the ResBlock-34 (He et al.,
2016) as the basic convolutional block (Fig. 3b), and uses 5 × 5 convolutional kernels in some of the convolutional layers of the deep
encoder to expand the receptive field and better capture global information. The model can be divided into two parts: the predict module and
the refine module, with the prediction module serving as the model
backbone. This backbone employs an encoder-decoder structure with
skip connections, enabling the simultaneous capture of high-level global
contexts and low-level detailed features. It is organized into four symmetric stages and a bridge stage, incorporating additional convolutional
layers at the deeper stages. In each stage of the encoder, an edge
detection block is inserted between the convolutional blocks, and a dual
attention block is added at the end. The bridge stage utilizes a pyramid
pooling module for multi-scale feature fusion. It combines features from
multiple scales, thereby generating global context knowledge that encompasses both low-level and high-level information (Zhao et al., 2017).
In lieu of maximum pooling, a convolution operation with the kernel

2.2. Datasets
The training, validation, and testing regions were randomly selected
from the images, as displayed in Fig. 1. The regions designated for
training and validation were cropped into chips with a uniform size of
256*256 pixels and subsequently divided into training and validation
sets using a random 8/2 split. During the training process, a total of
2,287 training chips and 572 validation chips were used in the NL
dataset. The HT dataset consisted of 1,962 training chips and 491 validation chips. We employed data augmentation to enhance the amount
and diversity of training samples. For each sample, one of the five
transformations, i.e., unchanged, horizontally flipped, vertically flipped,
rotated 90 degrees, and rotated 180 degrees, was randomly applied. In
the transfer experiment, we selected 100 training chips from each new
region. It is noteworthy that we used all pixels in the testing area
(“yellow rectangle” in Fig. 1) for the final accuracy assessment, instead
of selected chips.

3

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 2. The workflow of the study.

size of 3 × 3 and the stride of 2 is used for the down-sampling process to
minimize information loss, while a bilinear interpolation is employed
for the up-sampling process. The below are the details for four innovative components within REAUNet.

detect gradients in the feature maps along four directions (Ranjan and
Avasthi, 2023), and subsequently fuses the features in each gradient
direction through a convolutional layer. Common deep learning models
often lack expert knowledge and rely heavily on data-driven learning.
REAUNet augments the model with traditional edge detection operators.
By leveraging this empirical knowledge, REAUNet bolsters the model
capability to extract sophisticated semantic features from limited samples. Also, the edge detection block compensates for omissions of edge
features through residual connections.

3.1.1. Deep supervision
Deep supervision is a widely employed technique in deep learning
models for edge detection (Liu et al., 2017; Xie and Tu, 2015). This
approach involves adding supervision signals at hidden layers of a
neural network, effectively guiding the learning process at multiple
stages. Deep supervision could alleviate the problem of gradient vanishing and provide robust regularization of learned features, which is
particularly beneficial for a case of small training data and shallower
networks. In our proposed REAUNet, deep supervision is integrated by
combining multiple coarse outputs from the predict module with the
refine output from the refine module, which ensures that supervision is
applied across different-sized feature maps. By supervising multiple
layers, the network can enhance feature regularization and learn richer
feature representations.

3.1.3. Dual attention block
The dual attention block (Fig. 3d) integrates channel attention and
spatial attention. Each component performs parallel computations of
global average pooling and global maximum pooling, inspired by previous works (Roy et al., 2018; Woo et al., 2018). The benefit of the
proposed attention mechanism is that it explores the spatial-contextual
relationship among pixels in addition to interaction among feature
channels. This block enables the model to better focus on areas that are
prone to errors, such as the edges of agricultural parcels.

3.1.2. Edge detection block
The edge detection block (Fig. 3c) was inserted into the middle of
each stage to integrate edge gradient information during the feature
extraction step, so that we could reinforce the ability of recognizing
agricultural parcel edges. This block applies four different Sobel filters to

3.1.4. Refine module
The refine module, inspired by BASNet (Boundary-Aware Salient
Network) (Qin et al., 2019), was implemented to further enhance edge
prediction accuracy of the predict module (Fig. 3a). The predict module
generates a coarse map with commendable regional accuracy, yet there
4

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 3. The architecture of the proposed REAUNet for agricultural parcel delineation. Four innovative components are highlighted as the red color: deep supervision,
edge detection block, dual attention block, and refined module. (For interpretation of the references to color in this figure legend, the reader is referred to the web
version of this article.)

remains potential for enhancing edge quality. The refine module serves
to refine the segmentation results by rectifying omission/commissions in
the coarse map. It operates a straightforward residual encoder-decoder
architecture to learn the residual map between the output of the predict module and the ground truth. Both the encoder and decoder consist
of four layers symmetrically, each containing only one convolutional
layer.
Finally, we utilized labels for the agricultural parcel extent and the
parcel boundary to construct two models respectively for agricultural
parcel and boundaries, and then derived the ultimate parcel delineation
result by merging the extent mask and the boundary mask.
The codes for the REAUNet have been made publicly available in htt
ps://github.com/Remote-Sensing-of-Land-Resource-Lab/REAUNet.

LDice = 1 −

i=1

⎧
⎪
Nnegative
⎪
⎪
⎪
⎨ N
batch
w=
⎪ α × Npositive
⎪
⎪
⎪
⎩ Nbatch

Different loss functions are employed for parcel extent training and
parcel boundary training. The segmentation of agricultural parcel extent
can be viewed as a semantic segmentation task. The loss function for
parcel extent combines a binary cross-entropy (BCE) loss LBCE and a dice
loss LDice to tackle sample imbalance and ensure the stability of the
training process. This can be defined as:

LBCE = −

)
(
1 ∑N
(y
y
y
i ⋅log ̂
i + (1 − yi )⋅log(1 − ̂
i) )
i=1
N

(3)

where yi denotes the binary ground truth label, ̂
y i represents the predicted result, and N signifies the total number of pixels.
Parcel boundary delineation is akin to an edge detection task, and the
distribution of edge pixels and non-edge pixels is typically highly
imbalanced. Accordingly, we employed a dynamically weighted BCE
loss, where the weights adapt to the proportion of positive and negative
pixels. In addition, we integrated a sum-based loss calculation mode
instead of averaging, thereby amplifying the loss weights for the limited
number of edge samples. The boundary loss function was defined as:
∑N
(4)
Ledge =
w⋅(yi ⋅loĝ
y i + (1 − yi )⋅log(1 − ̂
yi) )

3.2. Loss functions and training details

Lextent = 0.5 × LBCE + LDice

1 ∑N 2yi ⋅̂
yi
N i=1 yi + ̂
yi

if yi = 1
if yi = 0

(5)

where w refers to the weights calculated dynamically based on the
number of positive and negative samples in each batch, and α is the
sample balance coefficient set to 1.1.
Our hyperparameter tuning process focuses on two critical parameters: the learning rate and the weight decay. The learning rate selection
method, referred to Smith (2017), involved setting a range from 10− 5 to
10− 2. We conducted 8 epochs of training with various learning rates and

(1)
(2)

5

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

then chose the learning rate associated with the highest final accuracy as
the initial learning rate. Fig. 4(a) indicates that the learning rate of 3 ×
10− 4 achieved the highest accuracy, which was considered the optimal
initial learning rate. After determining the initial learning rate, we
performed an experiment comprising 100 training epochs, varying three
weight decay parameters (10− 3, 10− 4, 10− 5). Fig. 4(b) shows that the
weight decay of 10− 4 achieved the lowest loss value during training. As a
result, we employed the Adam optimizer with an initial learning rate of
3 × 10− 4 and a weight decay of 1 × 10− 4. The models underwent
training for a maximum of 200 epochs with a batch size of 8. In cases of
the model loss plateauing for 30 consecutive epochs, the learning rate
was reduced by a factor of 0.1. If the validation set loss showed no
improvement for 50 consecutive epochs, we implemented an early
stopping to mitigate overfitting.

3.4. Comparison with representative CNN models
In order to evaluate the effectiveness of our method, we conducted a
comparative analysis of eight CNN models specifically designed for
segmentation tasks and agricultural parcel delineation. Table 1 presents
the brief descriptions for these CNN models.
3.5. Model transferability experiment
To assess the capability of REAUNet being applied to different agricultural areas, we conducted a model transferability experiment. We
tested the model trained from NL on DK region for Sentinel-2 images,
and the model from HT on the TR region for GF-2 images. In this
experiment, we defined three scenarios: No Training (NT) implies that
the model, previously trained in other regions, was taken to make predictions directly in the new region (e.g., using the model trained on NL
data to delineate parcels in the DK area); Direct Training (DT) trained
the model merely using local samples; Transfer Training (TT) pretrained
a model using data from another region first, followed by continued
training with local samples from the new region. The NT scenario can be
also viewed as a validation of the model generalizability when confronted with a new region.
In the new region selected for the transfer experiment, we opted for a
small area to generate training samples, resulting in approximately 100
samples of size 256 × 256 pixels. The REAUNetDT followed the same
protocol as REAUNet, with a maximum of 200 epochs. On the other
hand, REAUNetTT was trained for a shorter duration, specifically 20
epochs.

3.3. Post-processing
We designed a post-processing workflow to further improve the edge
delineation. The specific steps were outlined as follows:
(1) applied a 1-pixel buffer to the parcel boundary results, reducing
the boundary interruption in the results;
(2) performed a morphological thinning operation on the boundary
results corresponding to the previous buffer;
(3) utilized the parcel extent mask and the boundary mask to delineate individual agricultural parcels with the cutoff method, and
the cutoff threshold was set to 0.5 (Waldner and Diakogiannis,
2020);
(4) conducted morphological processing on the binary results to
eliminate holes and small isolated pixels;
(5) vectorized the results and employed the Douglas-Peucker algorithm to remove redundant nodes, optimizing the edges of agricultural parcels;
(6) detected and eliminated over-sharp angles.

3.6. Accuracy assessment
We used a total of six evaluation metrics to assess the performance of
model for delineating agricultural parcels from both pixel-based and
object-based perspectives, i.e., Overall Accuracy (OA), Intersection over
Union (IoU), F1-score (F1), Global Over-Classification (GOC), Global
Under-Classification (GUC) and Global Total-Classification (GTC). The
pixel-based metrics (OA, IoU and F1) were defined as follows:

Fig. 5 exemplifies the improvement brought by the post-processing
step. We applied a morphological thinning operation to narrow the
boundary map and subsequently utilized the cutoff method to isolate
individual agricultural parcels. Although the deep learning model successfully captured the boundaries of agricultural parcels, some breakpoints persisted in the results, leading to irregularly shaped parcels
being obtained, as shown in Fig. 5(c). To address this, the DouglasPeucker algorithm and the over-sharp angle elimination algorithm
were employed to optimize the spatial geometric shapes of the parcels.

OA =

TP + TN
TP + FN + FP + TN

(6)

IoU =

TP
TP + FP + FN

(7)

2*TP
2*TP + FP + FN

(8)

F1 =

where TP, TN, FP, and FN refer to True Positive, True Negative, False

Fig. 4. Hyperparameter selection. (a) The highest accuracy was achieved at a learning rate of 3 × 10− 4. (b) The lowest loss value was obtained with a weight decay
of 10− 4.
6

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 5. Model results of parcel boundaries. (a) represents area NL, (b) represents area HT, and (c) shows the refined parcels formed by the post-processing method.

Positive, and False Negative, respectively.
To better assess spatial accuracy of extracted parcels, we adopted
three object-based accuracy metrics as a complementary evaluation,
based upon under-segmentation and over-segmentation errors (Li et al.,
2023; Ye et al., 2018), which were defined as followed:
)
∑m (
area(Si )
GOC =
OC(Si ) × ∑m
(9)
i=1
i=1 area(Si )
GUC =
GTC =

∑m (
i=1

∑m (
i=1

area(Si )
UC(Si ) × ∑m
i=1 area(Si )

area(Si )
TC(Si ) × ∑m
i=1 area(Si )

crucial role of multi-scale deep supervision in the accurate delineation of
agricultural parcels.
To further explore the decision process of REAUNet and enhance the
model transparency, we outputted the feature maps of the model at
different stages to show how the input images is transformed passing
through the layers. Fig. 7(b) illustrates the feature maps from the
shallow and deep layers for the encoder stage, where the bright pixels
indicate the patterns the REAUNet is seeking for. Shallow features
(Encoder #1) trains most of the information present in the image. Deep
features (Encoder #4), on the other hand, are high-level features for
seeking an abstract representation. Some hidden class information, such
as the impervious surface (the fourth column), become recognizable.
The output feature maps for the decoder present a reversing trend of
increasing details (Fig. 7c) from Decoder #1 to Decoder #5. Benefited
from the design of deep supervision, REAUNet will integrate these
feature maps generated from different scales and guide these intermediate layers towards the desired solution, enabling the model to better
capture hierarchical relationships among parcel features.

)
(10)

)
(11)

where Si,i=1,2,⋯,m denotes the classified parcels in model results. OC(Si ),
UC(Si ) and TC(Si ) were defined as:
OC(Si ) = 1 −

area(Si ∩ Oi )
area(Oi )

(12)

UC(Si ) = 1 −

area(Si ∩ Oi )
area(Si )

(13)

√̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
OC(Si )2 + UC(Si )2
TC(Si ) =
2

4.2. Comparative experiment
The accuracy assessment results for REAUNet and other deep
learning models were presented in Table 3. The REAUNet model
consistently outperformed the other models for most accuracy metrics:
in the NL study area, REAUNet demonstrated an increase of 2.0 % in F1score and a decrease of 3.4 % in GTC compared to the second-best
SEANet; in the HT study area, REAUNet exhibited a 0.8 % increase in
IoU and a 2 % decrease in GTC relative to the second-best model,
MPSPNet. Fig. 8 visualizes the agricultural parcel delineation maps from
various deep learning methods. In contrast to other models, our proposed method notably reached the lowest false negative errors at parcel
edges. Additionally, REAUNet proves effective in minimizing false
negative errors (the blue region) in certain regions of the HT study area,
particularly where parcel boundaries are less evident. Thanks to its
powerful edge-awareness, REAUNet achieved excellent extraction results in study areas with different data sources. It successfully extracted
complex and diverse agricultural parcels in the NL region and delineated
parcels of varying sizes in the HT region. The strength of REAUNet lies in
performing complex and diverse parcel extraction at multiple scales, and
its delineation results in these regions surpass those of several representative models.

(14)

Where Oi,i=1,2,⋯,n represents the reference objects in the ground truth,
which is the parcel closest in distance to Si .
We used these accuracy metrics (Eq. 6–11) for an ablation experiment and the final accuracy report. The ablation experiment assessed
the accuracy loss after removing each component out of the four innovative components for the REAUNet, so that we could understand the
accuracy contribution of individual component.
4. Results
4.1. Ablation experiment
Table 2 depicts the accuracy for different settings of REAUNet in the
ablation experiment. In comparison to the original REAUNet, all other
model settings exhibited notably higher GUC/GTC, indicating the four
components all contribute to the final geometric accuracy. Fig. 6
showcases that the REAUNet with all four components (the third column
“REAUNet”) significantly presents the least false negative errors at the
edges of parcels. Among the four modules, the removal of deep supervision had the most pronounced impact on accuracy, highlighting the

4.3. Agricultural parcel delineation results
Fig. 9 displays the extraction results of REAUNet for the NL and HT
areas, showcasing the successful mapping of agricultural parcels from
7

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Table 1
The representative deep learning methods for agricultural parcel delineation.

parcels, as well as dense, elongated parcels in the NL region. Fig. 9(e)
and (f) displayed the results for agricultural parcels with complex
shapes. Likewise, in the HT region, the model successfully identified
various agricultural parcels of different shapes and sizes.

Method

Model description

Reference

U-Net

• U-Net consists of a contracting path to
capture context and a symmetric
expanding path that enables precise
localization;
• Every step in the expansive path is followed
by a concatenation with the
correspondingly cropped feature map from
the contracting path.
• RCF is an end-to-end convolutional
network designed to extract edges;
• RCF keeps five convolutional stages in
VGG16, and the feature maps from the
same stages are added up then upsampled
to generate an edge probability map;
• A fusion output is obtained by
concatenating all 5 edge probability maps
in channel dimension.
• MPSPNet incorporates three core
structures: ResNet with dilated
convolution, spatial pyramid average
pooling module, and fusion of low-level
and high-level information.
• ResUNet-a consists of residual units with
multiple parallel branches of atrous
convolutions, each with a different dilation
rate to increase the receptive field;
• ResUNet-a produces four output layers: the
extent mask, the boundaries, the distance
mask, and full reconstruction of the input
image in the HSV color.
• BsiNets uses one single decoder to produce
three types of information mask, boundary,
and distance;
• SGE attention module is incorporated into
BsiNet to extract enhanced features,
utilising the global information and scaling
the importance of different channels.
• FRNet is divided into four parallel streams
in the horizontal direction, i.e., the first
stream with full resolution and the
additional three with resolution decreased
by half;
• Different parallel streams are connected
and fused by the multi-resolution fusion
unit (MRFU).
• RAUNet uses ResNet to capture higherlevel abstract features in the encoder;
• RAUNet integrates coarse- and fine-scale
features to suppress irrelevant noise and
highlight salient regions with a gated
attention mechanis in the decoder.
• SEANet consists of two main components
corresponding to PRoI and PEoI feature
extraction;
• SEANet constructs a stack of convolution
blocks to derive edge feature maps at
multiple levels.

(Ronneberger et al.,
2015)
(Kumar and
Jayagopal, 2021)

RCF

MPSPNet

ResUNeta

BsiNet

FRNet

RAUNet

SEANet

4.4. Model transferability experiment
Table 4 presents the accuracy assessment for the three scenarios in
the transferability experiment. The REAUNetTT achieved the highest
accuracy and surpassed the model trained from scratch for 200 epochs
by simply continuing training for 20 epochs using only 100 local samples. Fig. 10 shows the resultant maps for these three scenarios.
REAUNetNT achieved the lowest accuracy and exhibited numerous false
negative pixels (“the blue region”), indicating that the model struggled
in these regions without local samples. Moreover, REAUNetTT presented
a higher accuracy than REAUNetDT for both DK and TR, which suggested
the superiority of REAUNet in transferring model for a new region. The
transfer trained model incurred a training cost of less than 5 min and
exhibited a notable 10–15 % improvement in F1 over the original model.

(Liu et al., 2017)
(Liu et al., 2019)

(Zhang et al., 2020)

5. Discussion

(Diakogiannis et al.,
2020)
(Waldner and
Diakogiannis, 2020)

5.1. Comparison to representative models
Our proposed REAUNet outperformed all representative models for
agricultural parcel extraction that were selected. There were mainly four
innovations to specifically improve model performance, and the results
in the ablation experiment indicated that all four components positively
contribute to the final accuracy of the agricultural parcels. In contrast to
MPSPNet (Zhang et al., 2020), which incorporates residual dilated
convolution and pyramid pooling module, our model integrates an
attention mechanism and multi-scale deep supervision. The dual attention block enables the model to better tackle important regions and
critical features of the parcels during the feature extraction process,
enhancing its adaptability in handling parcels with diverse shapes and
complex structures. Deep supervision allows the model to detect various
levels of edge structures from different scales. This capability enables the
capturing of edge structural information pertaining to both local details
and the overall context. Notably, we observed that removing the deep
supervision of the model causes the most accuracy loss in the ablation
experiment. The attention mechanism and deep supervision in REAUNet
empower it to effectively identify agricultural parcels of varying sizes,
resulting in reduced over-segmentation compared to MPSPNet.
Furthermore, in comparison to SEANet (Li et al., 2023), which employs similar edge-aware and multi-scale segmentation techniques, we
enhanced the accuracy of edge region delineation around parcels by
integrating the edge detection operator into REAUNet (i.e., Edge
Detection Block). This innovation leverages four different Sobel operators based upon empirical knowledge to detect feature map edges across
various gradients, mitigating the impact of the morphology of agricultural parcels. Besides, to tackle the issue of incorrect pixels along parcel
edges, we incorporated a small residual refine module following the
main model. The demonstrated effectiveness of the refine module in the
realm of salient object detection showcased its capability to efficiently
reduce classification errors at target edges through residual learning

(Long et al., 2022)

(Xia et al., 2022)

(Cai et al., 2023b)

(Li et al., 2023)

two distinct remote sensing image sources, Sentinel-2 and GF-2. The
vectorized agricultural parcel boundaries in Fig. 9(c) and (d) revealed
that REAUNet accurately delineates large, well-organized agricultural

Table 2
Accuracy assessment in the ablation experiment. ED: the edge detection block. DA: the dual attention block. RM: the refine module. DS: the deep supervision.
Method
REAUNet
REAUNetnoED
REAUNetnoDA
REAUNetnoRM
REAUNetnoDS

NL

HT

OA

F1

IoU

GOC

GUC

GTC

OA

F1

IoU

GOC

GUC

GTC

0.9473
0.9411
0.9302
0.9402
0.9289

0.9498
0.9398
0.8925
0.9092
0.8877

0.8372
0.8216
0.7948
0.8190
0.7875

0.1363
0.1502
0.1491
0.1605
0.1571

0.2148
0.2347
0.2605
0.2487
0.2858

0.2017
0.2251
0.2360
0.2347
0.2549

0.9481
0.9399
0.9393
0.9386
0.9304

0.9454
0.9425
0.9426
0.9416
0.9326

0.9096
0.8985
0.8984
0.8966
0.8807

0.1123
0.1101
0.1189
0.1160
0.1097

0.2234
0.2770
0.2867
0.2742
0.3181

0.2074
0.2296
0.2337
0.2370
0.2701

8

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 6. Delineation results in the ablation experiment. (a) and (b) represent area NL, while (c) and (d) represent area HT.

(Qin et al., 2019). The combination of empirical knowledge and residual
refinement further enhances the model ability for edge delineation, facilitates more precise identification for ambiguous crop edges, thus diminishes model errors.
We also designed a post-processing workflow to optimize the geometry shape of parcels. The presence of different crops in agricultural
parcels could lead to adjacent areas displaying different colors in remote
sensing images. This variation poses a challenge for the model in
distinguish whether it is parcel boundaries, often resulting in erroneous
short boundary lines. These errors contribute to false negatives within
agricultural parcels when fusing the parcel extent and boundary results
(Fig. 5c). To address this issue, we used the Douglas-Peucker algorithm
and the over-sharp angles detection and elimination algorithm to mitigate these false negatives. Through this post-processing approach, our
method produced agricultural parcels with a more coherent spatial
geometry.
In this study, we opted for convolutional neural network (CNN) as
the deep learning model for agricultural parcel delineation, a choice that
has demonstrated significant success in the realm of image segmentation. However, it is noteworthy that Transformer-based methods, originally developed for natural language processing (NLP), are gaining
popularity in image segmentation and have shown remarkable results in
recent years (He et al., 2022; Liu et al., 2021b; Vaswani et al., 2017). The
primary rationale for selecting CNN is the extensive use of linear layers
and self-attention mechanisms in Transformers, resulting in a larger
number of parameters and slower computation. Conversely, a crucial
characteristic of CNN is weight sharing, enabling it to efficiently reduce
the number of parameters when handling multidimensional matrices.
CNN excels in extracting local features from images using convolutional
kernels, whereas Transformer possesses the capability to capture longrange dependencies.

target regions. In the model transferability experiment, the unsatisfactory results achieved by the NT model suggested that it was challenging
to obtain good performance when the trained model was applied
directly to an unknown region. Agricultural parcels in various regions
and during different seasons display significant variations in spatial
patterns and spectral features from remote sensing images, presenting
variations in terms of the shape and size of agricultural parcels. In plains
or areas with mechanized farming operations, agricultural parcels tend
to be large and regular. In contrast, mountainous and hilly regions often
have smaller, more fragmented parcels. Additionally, the different
growth stages of crops across seasons result in varying spectral features
in remote sensing images as well. For instance, the greenness will show
notable differences between the early and mature stages of crop growth
from remote sensing images. Additionally, different crop species across
the two time periods can also lead to variations in boundary delineation.
This discrepancy poses difficulties for the model when confronting unknown data, which requires the inputs of the new samples representative for the geography and the mapping seasons of the images to be
classified. However, redrawing labels and reconstructing the training
model from the scratch could be costly. The model transferability
experiment simulated three scenarios, i.e., direct model transfer,
rebuilding from the scratch, and a mixture of non-local and local samples. The results highlighted the potential of REAUNet being transferred
to a new region only with a small number of local samples. This was
because that the proposed REAUNet leveraged multi-scale deep supervision to segment agricultural parcels across various scales, yielding
commendable extraction results when dealt with parcels of different
sizes in new regions. Moreover, we integrated traditional edge detectors
into the model, enabling a feature extraction guided by the window
techniques which was generalized from numerous past computer vision
studies. The potential model transferability shown by REAUNet will
hold considerable implications for a large-scale agricultural parcel
mapping in future.

5.2. Model transferability
In the practical application of the deep learning model, it frequently
encounters scenarios involving unknown data, placing high demands on
the transfer ability of the model. However, models trained using data
from non-targeted regions often fail to exhibit a sound accuracy for

5.3. Limitations
The process of extracting agricultural parcels from remote sensing
images necessitates the fusion of parcel segmentation results with parcel
9

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 7. Model feature maps in the encoder and decoder. (a) The predict module of REAUNet. (b) Extracted feature maps from shallow and deep layers in the encoder.
(c) Output features of parcel extent and boundaries in the decoder.
Table 3
Accuracy assessment of different deep learning models for parcel delineation.
Method
U-Net
RCF
MPSPNet
ResUNet-a
BsiNet
FRNet
RAUNet
SEANet
REAUNet

NL

HT

OA

F1

IoU

GOC

GUC

GTC

OA

F1

IoU

GOC

GUC

GTC

0.9299
0.9130
0.9316
0.9304
0.9253
0.9314
0.9180
0.9332
0.9473

0.9230
0.9012
0.9289
0.9252
0.9195
0.9264
0.9122
0.9304
0.9498

0.8305
0.7961
0.8401
0.8340
0.8246
0.8359
0.8132
0.8425
0.8372

0.1763
0.2005
0.1422
0.1931
0.1680
0.1537
0.2209
0.1350
0.1363

0.2614
0.2989
0.2176
0.2431
0.2580
0.2388
0.2592
0.2277
0.2148

0.2557
0.2922
0.2384
0.2459
0.2578
0.2446
0.2754
0.2355
0.2017

0.9391
0.9372
0.9472
0.9411
0.9318
0.9440
0.9458
0.9388
0.9481

0.9460
0.9441
0.9533
0.9478
0.9395
0.9512
0.9526
0.9466
0.9454

0.8979
0.8946
0.9012
0.9011
0.8863
0.9076
0.9035
0.8988
0.9096

0.1569
0.1912
0.1897
0.1503
0.1954
0.2545
0.2088
0.1598
0.1123

0.2631
0.2315
0.1908
0.2541
0.2540
0.3033
0.2224
0.2228
0.2234

0.2566
0.2580
0.2309
0.2483
0.2761
0.3239
0.2586
0.2314
0.2074

edge results. We chose the simplest cutoff method to merge two model
results, because Waldner and Diakogiannis (2020) found that it achieved
similar results to the watershed approach. We observed that in the edge
mask, the agricultural parcel edges were represented with varying
probabilities, rendering the difficulty in selecting a suitable threshold.
There is a trade-off between under-segmentation and over-segmentation
errors wherein the choice of thresholds. How to use a better fusion

method to merge the parcel extent mask and edge mask could be the key
to further enhance the delineation accuracy.
We extracted refined agricultural parcels from model predictions
through a post-processing workflow. However, in some instances, the
edge probability maps output by the model exhibited lower probabilities
due to occlusion or blurring, resulting in a complication for the
threshold determination on the edge binarization. The generated lines
10

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Fig. 8. Delineation results of REAUNet and other deep learning models in the comparative experiment. (a) and (b) represent area NL, while (c) and (d) represent
area HT.

Fig. 9. The general delineation results of agricultural parcels and vectorized boundaries in (a) NL and (b) HT, and their subregions were shown in from (c) to (i): (c)
and (i) shows regular parcels, (d) depicts narrow parcels, and (g) presents parcels of different sizes, (e) and (f) shows mountainous regions.

might end up being incomplete with breakpoints. Our current approach
opts to directly remove short and isolated lines, which may advertently
eliminate some incomplete but correct edges. In future research, the
development of the breakpoint reconnection method is essential to form

complete edges and mitigate the under-segmentation phenomenon in
the delineation of agricultural parcels.
The biases in data labels may cause the loss of model accuracy. The
open-source datasets may contain inconsistencies in parcel boundaries
11

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Table 4
Accuracy assessment in the model transferability experiment. NT: no training. DT: direct training. TT: transfer training.
Study area

Method

OA

F1

IoU

GOC

GUC

GTC

DK

REAUNetNT
REAUNetDT
REAUNetTT
REAUNetNT
REAUNetDT
REAUNetTT

0.7704
0.8681
0.8887
0.7134
0.8979
0.9001

0.8113
0.9028
0.9195
0.7794
0.9248
0.9270

0.6615
0.7919
0.8181
0.6185
0.8602
0.8640

0.3925
0.1571
0.1424
0.4961
0.1403
0.1318

0.4451
0.2729
0.2460
0.6380
0.1942
0.1823

0.4565
0.2599
0.2343
0.5679
0.1891
0.1781

TR

Fig. 10. Model results in the model transferability experiment. (a) represents area DK and (b) represents area TR.

due to temporal discrepancies, leading to inaccuracies in defining the
exact shape and size of agricultural parcels. Additionally, there may be
variability in whether parcel ridges are marked, introducing further
inconsistencies. These deviations can affect the training process, making
it challenging for the model to find the correct fitting direction and
thereby reducing accuracy. To mitigate the influence of data errors,
future efforts can implement collaborative labeling processes involving
multiple individuals to minimize accidental human errors. Employing
consensus-based labels can enhance the reliability of identified agricultural parcels. Moreover, integrating supplementary data sources for
cross-validation purposes may bolster the accuracy and robustness of the
delineated agricultural parcels.
We evaluated the model performance in new regions through a
transfer experiment and observed that even a small number of local
samples could markedly boost model accuracy. Given the laborintensive sample labeling, there is always an expectation to achieve a
high extraction accuracy with only minimal local samples. However,
when deploying the model to a new area, determining the optimal
number of local samples for transfer training remains a significant
challenge, which could be a limitation for our study. Our future research
will focus on exploring the optimal number of samples for transfer
learning to address this gap and enhance the robustness and generalizability of our model. Strategically selecting local samples will significantly facilitate large-scale mapping and reduce the time and resources
required for sample preparation and model training.

and shape of extracted parcels, we formulated a post-processing workflow utilizing the Douglas-Peucker algorithm and an over-sharp angle
detection and elimination algorithm. Comparative experiments revealed
that our proposed model surpassed representative agricultural parcel
extraction CNN models in both thematic and geometric accuracy.
Finally, to facilitate the successful delineation of agricultural parcels in
unknown regions using the proposed deep learning model, we tested and
confirmed the capability of the new model for transferring pre-models to
a new region with a small proportion of local samples. This opened up
the possibility of mapping the distribution of agricultural parcels on a
large scale. In conclusion, our proposed algorithm successfully delineated the agricultural parcels from remote sensing images. Enhancing
the edge-awareness of the model significantly improved its accuracy in
delineating agricultural parcels, particularly on the parcel edges. The
method also demonstrated good generalization results in different regions with limited local samples, offering a new approach for the
automatic mapping of agricultural parcels at a large spatial scale.
CRediT authorship contribution statement
Rui Lu: Writing – review & editing, Writing – original draft, Visualization, Project administration, Methodology, Investigation, Formal
analysis, Data curation, Conceptualization. Yingfan Zhang: Writing –
review & editing, Methodology, Investigation. Qiting Huang: Supervision, Data curation. Penghao Zeng: Writing – review & editing. Zhou
Shi: Writing – review & editing, Supervision, Resources, Funding
acquisition, Conceptualization. Su Ye: Writing – review & editing, Supervision, Conceptualization.

6. Conclusion
This study developed a novel deep learning model, REAUNet, to
delineate agricultural parcels from high-resolution remote sensing images. Four model innovations were ensembled to improve edgeawareness, including the deep supervision, the edge detection block,
the dual attention block and the refine module. Sentinel-2 and GF-2
imagery at different resolutions across four regions were utilized to
assess the effectiveness of parcel delineation. To optimize the geometry

Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
12

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Data availability

Chetri, T., Malek, Ž., Bungnamei, K., Saikia, A., Sahariah, D., Narzary, W.,
Danylo, O., Sturn, T., Karner, M., McCallum, I., Schepaschenko, D., Moltchanova, E.,
Fraisl, D., Moorthy, I., Fritz, S., 2019. Estimating the global distribution of field size
using crowdsourcing. Glob. Change Biol. 25, 174–186. https://doi.org/10.1111/
gcb.14492.
Li, M., Long, J., Stein, A., Wang, X., 2023. Using a semantic edge-aware multi-task neural
network to delineate agricultural parcels from remote sensing images. ISPRS J.
Photogramm. Remote Sens. 200, 24–40. https://doi.org/10.1016/j.
isprsjprs.2023.04.019.
Liu, Y., Cheng, M.M., Hu, X., Wang, K., Bai, X., 2017. Richer convolutional features for
edge detection. In: Proceedings of the IEEE conference on computer vision and
pattern recognition, pp. 3000–3009.
Liu, H., Luo, J., Sun, Y., Xia, L., Wu, W., Yang, H., Hu, X., Gao, L., 2019. Contour-oriented
cropland extraction from high resolution remote sensing imagery using richer
convolution features network. In: 2019 8th International Conference on AgroGeoinformatics (Agro-Geoinformatics). IEEE, pp. 1–6. https://doi.org/10.1109/
Agro-Geoinformatics.2019.8820430.
Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., Guo, B., 2021. Swin
transformer: Hierarchical vision transformer using shifted windows. In: Proceedings
of the IEEE/CVF international conference on computer vision, pp. 10012–10022.
Liu, Y., Ma, X., Shu, L., Hancke, G.P., Abu-Mahfouz, A.M., 2021a. From industry 4.0 to
agriculture 4.0: current status, enabling technologies, and research challenges. IEEE
Trans. Ind. Inform. 17, 4322–4334. https://doi.org/10.1109/TII.2020.3003910.
Lobell, D.B., Thau, D., Seifert, C., Engle, E., Little, B., 2015. A scalable satellite-based
crop yield mapper. Remote Sens. Environ. 164, 324–333. https://doi.org/10.1016/j.
rse.2015.04.021.
Long, J., Li, M., Wang, X., Stein, A., 2022. Delineation of agricultural fields using multitask BsiNet from high-resolution satellite images. Int. J. Appl. Earth Obs. Geoinform.
112, 102871 https://doi.org/10.1016/j.jag.2022.102871.
Lu, Y., Jenkins, A., Ferrier, R.C., Bailey, M., Gordon, I.J., Song, S., Huang, J., Jia, S.,
Zhang, F., Liu, X., Feng, Z., Zhang, Z., 2015. Addressing China’s grand challenge of
achieving food security while ensuring environmental sustainability. Sci. Adv. 1,
e1400039. https://doi.org/10.1126/sciadv.1400039.
Pan, Y., Wang, X., Zhang, L., Zhong, Y., 2023. E2EVAP: End-to-end vectorization of
smallholder agricultural parcel boundaries from high-resolution remote sensing
imagery. ISPRS J. Photogramm. Remote Sens. 203, 246–264. https://doi.org/
10.1016/j.isprsjprs.2023.08.001.
Persello, C., Tolpekin, V.A., Bergado, J.R., de By, R.A., 2019. Delineation of agricultural
fields in smallholder farms from satellite images using fully convolutional networks
and combinatorial grouping. Remote Sens. Environ. 231, 111253 https://doi.org/
10.1016/j.rse.2019.111253.
Potapov, P., Turubanova, S., Hansen, M.C., Tyukavina, A., Zalles, V., Khan, A., Song, X.P., Pickens, A., Shen, Q., Cortez, J., 2022. Global maps of cropland extent and change
show accelerated cropland expansion in the twenty-first century. Nat. Food 3, 19–28.
https://doi.org/10.1038/s43016-021-00429-z.
Pywell, R.F., Heard, M.S., Woodcock, B.A., Hinsley, S., Ridding, L., Nowakowski, M.,
Bullock, J.M., 2015. Wildlife-friendly farming increases crop yield: evidence for
ecological intensification. Proc. R. Soc. B Biol. Sci. 282, 20151740. https://doi.org/
10.1098/rspb.2015.1740.
Qin, X., Zhang, Z., Huang, C., Gao, C., Dehghan, M., Jagersand, M., 2019. BASNet:
boundary-aware salient object detection. In: Presented at the Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 7479–7489.
Ranjan, R., Avasthi, V., 2023. Edge detection using guided sobel image filtering. Wirel.
Pers. Commun. 132, 651–677. https://doi.org/10.1007/s11277-023-10628-5.
Ronneberger, O., Fischer, P., Brox, T., 2015. U-Net: Convolutional networks for
biomedical image segmentation. In: Navab, N., Hornegger, J., Wells, W.M.,
Frangi, A.F. (Eds.), Medical Image Computing and Computer-Assisted Intervention –
MICCAI 2015, Lecture Notes in Computer Science. Springer International Publishing,
Cham, pp. 234–241. https://doi.org/10.1007/978-3-319-24574-4_28.
Roy, A.G., Navab, N., Wachinger, C., 2018. Concurrent Spatial and Channel ‘Squeeze &
Excitation’ in Fully Convolutional Networks. In: Frangi, A.F., Schnabel, J.A.,
Davatzikos, C., Alberola-López, C., Fichtinger, G. (Eds.), Medical Image Computing
and Computer Assisted Intervention – MICCAI 2018, Lecture Notes in Computer
Science. Springer International Publishing, Cham, pp. 421–429. https://doi.org/
10.1007/978-3-030-00928-1_48.
Smith, L.N., 2017. Cyclical learning rates for training neural networks. In: 2017 IEEE
winter conference on applications of computer vision (WACV), pp. 464–472. https://
doi.org/10.48550/arXiv.1506.01186.
Sun, Y., Li, Z.-L., Luo, J., Wu, T., Liu, N., 2022. Farmland parcel-based crop classification
in cloudy/rainy mountains using Sentinel-1 and Sentinel-2 based deep learning. Int.
J. Remote Sens.
Taravat, A., Wagner, M.P., Bonifacio, R., Petit, D., 2021. Advanced fully convolutional
networks for agricultural field boundary detection. Remote Sens. 13, 722. https://
doi.org/10.3390/rs13040722.
Turker, M., Kok, E.H., 2013. Field-based sub-boundary extraction from remote sensing
imagery using perceptual grouping. ISPRS J. Photogramm. Remote Sens. 79,
106–121. https://doi.org/10.1016/j.isprsjprs.2013.02.009.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł.,
Polosukhin, I., 2017. Attention is all you need. In: Advances in Neural Information
Processing Systems. Curran Associates, Inc.
Waldner, F., Diakogiannis, F.I., 2020. Deep learning on edge: Extracting field boundaries
from satellite images with a convolutional neural network. Remote Sens. Environ.
245, 111741 https://doi.org/10.1016/j.rse.2020.111741.
Wang, S., Zhou, Y., Yang, X., Li, F., Wu, T., Luo, J., 2023. BSNet: Boundary-semanticfusion network for farmland parcel mapping in high-resolution satellite images.

The authors do not have permission to share data.
Acknowledgements
The authors are very grateful for the financial support provided by
National Key Research and Development Program (2022YFB3903503),
and by the Fundamental Research Funds for the Central Universities
(226-202400052). The authors would also like to thank the editors and
anonymous reviewers of the journal for their thorough review and
insightful comments that have helped improving the quality of the
paper.
References
Cai, Y., Guan, K., Peng, J., Wang, S., Seifert, C., Wardlow, B., Li, Z., 2018. A highperformance and in-season classification system of field-level crop types using timeseries Landsat data and a machine learning approach. Remote Sens. Environ. 210,
35–47. https://doi.org/10.1016/j.rse.2018.02.045.
Cai, Z., Hu, Q., Zhang, X., Yang, J., Wei, H., Wang, J., Zeng, Y., Yin, G., Li, W., You, L.,
Xu, B., Shi, Z., 2023a. Improving agricultural field parcel delineation with a dual
branch spatiotemporal fusion network by integrating multimodal satellite data.
ISPRS J. Photogramm. Remote Sens. 205, 34–49. https://doi.org/10.1016/j.
isprsjprs.2023.09.021.
Cai, Z., Wei, H., Hu, Q., Zhou, W., Zhang, X., Jin, W., Wang, L., Yu, S., Wang, Z., Xu, B.,
Shi, Z., 2023b. Learning spectral-spatial representations from VHR images for finescale crop type mapping: A case study of rice-crayfish field extraction in South
China. ISPRS J. Photogramm. Remote Sens. 199, 28–39. https://doi.org/10.1016/j.
isprsjprs.2023.03.019.
Crommelinck, S., Bennett, R., Gerke, M., Yang, M.Y., Vosselman, G., 2017. Contour
Detection for UAV-Based Cadastral Mapping. Remote Sens. 9, 171. https://doi.org/
10.3390/rs9020171.
Diakogiannis, F.I., Waldner, F., Caccetta, P., Wu, C., 2020. ResUNet-a: A deep learning
framework for semantic segmentation of remotely sensed data. ISPRS J.
Photogramm. Remote Sens. 162, 94–114. https://doi.org/10.1016/j.
isprsjprs.2020.01.013.
Estes, L.D., Ye, S., Song, L., Luo, B., Eastman, J.R., Meng, Z., Zhang, Q., McRitchie, D.,
Debats, S.R., Muhando, J., Amukoa, A.H., Kaloo, B.W., Makuru, J., Mbatia, B.K.,
Muasa, I.M., Mucha, J., Mugami, A.M., Mugami, J.M., Muinde, F.W., Mwawaza, F.
M., Ochieng, J., Oduol, C.J., Oduor, P., Wanjiku, T., Wanyoike, J.G., Avery, R.B.,
Caylor, K.K., 2022. High resolution, annual maps of field boundaries for smallholderdominated croplands at national scales. Front. Artif. Intell. 4.
Garibaldi, L.A., Carvalheiro, L.G., Vaissière, B.E., Gemmill-Herren, B., Hipólito, J.,
Freitas, B.M., Ngo, H.T., Azzu, N., Sáez, A., Åström, J., An, J., Blochtein, B.,
Buchori, D., García, F.J.C., Oliveira da Silva, F., Devkota, K., Ribeiro, M. de F.,
Freitas, L., Gaglianone, M.C., Goss, M., Irshad, M., Kasina, M., Filho, A.J.S.P., Kiill, L.
H.P., Kwapong, P., Parra, G.N., Pires, C., Pires, V., Rawal, R.S., Rizali, A., Saraiva, A.
M., Veldtman, R., Viana, B.F., Witter, S., Zhang, H., 2016. Mutually beneficial
pollinator diversity and crop yield outcomes in small and large farms. Science 351,
388–391. https://doi.org/10.1126/science.aac7287.
Godfray, H.C.J., Beddington, J.R., Crute, I.R., Haddad, L., Lawrence, D., Muir, J.F.,
Pretty, J., Robinson, S., Thomas, S.M., Toulmin, C., 2010. Food security: the
challenge of feeding 9 billion people. Science 327, 812–818. https://doi.org/
10.1126/science.1185383.
Graesser, J., Ramankutty, N., 2017. Detection of cropland field parcels from Landsat
imagery. Remote Sens. Environ. 201, 165–180. https://doi.org/10.1016/j.
rse.2017.08.027.
He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep residual learning for image recognition. In:
Proceedings of the IEEE conference on computer vision and pattern recognition,
pp. 770–778.
He, X., Zhou, Y., Zhao, J., Zhang, D., Yao, R., Xue, Y., 2022. Swin transformer embedding
UNet for remote sensing image semantic segmentation. IEEE Trans. Geosci. Remote
Sens. 60, 1–15. https://doi.org/10.1109/TGRS.2022.3144165.
Hong, R., Park, J., Jang, S., Shin, H., Kim, H., Song, I., 2021. Development of a parcellevel land boundary extraction algorithm for aerial imagery of regularly arranged
agricultural areas. Remote Sens. 13, 1167. https://doi.org/10.3390/rs13061167.
Huang, Y., Ye, S., Xue, J., Shi, Z., Wang, F., 2024. Mapping cropping intensity by
identifying bare soil occurrence from Sentinel-2 time series. Comput. Electron. Agric.
222, 109025 https://doi.org/10.1016/j.compag.2024.109025.
Kuang, W., Liu, J., Tian, H., Shi, H., Dong, J., Song, C., Li, X., Du, G., Hou, Y., Lu, D.,
Chi, W., Pan, T., Zhang, S., Hamdi, R., Yin, Z., Yan, H., Yan, C., Wu, S., Li, R.,
Yang, J., Dou, Y., Wu, W., Liang, L., Xiang, B., Yang, S., 2022. Cropland
redistribution to marginal lands undermines environmental sustainability. nwab091
Natl. Sci. Rev. 9. https://doi.org/10.1093/nsr/nwab091.
Kumar, S., Jayagopal, P., 2021. Delineation of field boundary from multispectral satellite
images through U-Net segmentation and template matching. Ecol. Inform. 64,
101370 https://doi.org/10.1016/j.ecoinf.2021.101370.
Lesiv, M., Laso Bayas, J.C., See, L., Duerauer, M., Dahlia, D., Durando, N., Hazarika, R.,
Kumar Sahariah, P., Vakolyuk, M., Blyshchyk, V., Bilous, A., Perez-Hoyos, A.,
Gengler, S., Prestele, R., Bilous, S., Akhtar, I. ul H., Singha, K., Choudhury, S.B.,

13

R. Lu et al.

International Journal of Applied Earth Observation and Geoinformation 133 (2024) 104084

Comput. Electron. Agric. 206, 107683 https://doi.org/10.1016/j.
compag.2023.107683.
Woo, S., Park, J., Lee, J.-Y., Kweon, I.S., 2018. CBAM: Convolutional Block Attention
Module. In: Presented at the Proceedings of the European Conference on Computer
Vision (ECCV), pp. 3–19.
Xia, L., Zhao, F., Chen, J., Yu, L., Lu, M., Yu, Q., Liang, S., Fan, L., Sun, X., Wu, S.,
Wu, W., Yang, P., 2022. A full resolution deep learning network for paddy rice
mapping using Landsat data. ISPRS J. Photogramm. Remote Sens. 194, 91–107.
https://doi.org/10.1016/j.isprsjprs.2022.10.005.
Xie, S., Tu, Z., 2015. Holistically-nested edge detection. In: Presented at the Proceedings
of the IEEE International Conference on Computer Vision, pp. 1395–1403.
Yan, L., Roy, D.P., 2014. Automated crop field extraction from multi-temporal Web
Enabled Landsat Data. Remote Sens. Environ. 144, 42–64. https://doi.org/10.1016/
j.rse.2014.01.006.
Ye, S., Pontius, R.G., Rakshit, R., 2018. A review of accuracy assessment for object-based
image analysis: From per-pixel to per-polygon approaches. ISPRS J. Photogramm.
Remote Sens. 141, 137–147. https://doi.org/10.1016/j.isprsjprs.2018.04.002.
Ye, S., Rogan, J., Zhu, Z., Eastman, J.R., 2021. A near-real-time approach for monitoring
forest disturbance using Landsat time series: stochastic continuous change detection.
Remote Sens. Environ. 252, 112167 https://doi.org/10.1016/j.rse.2020.112167.

Yuan, X., Shi, J., Gu, L., 2021. A review of deep learning methods for semantic
segmentation of remote sensing imagery. Expert Syst. Appl. 169, 114417 https://doi.
org/10.1016/j.eswa.2020.114417.
Zabel, F., Delzeit, R., Schneider, J.M., Seppelt, R., Mauser, W., Václavík, T., 2019. Global
impacts of future cropland expansion and intensification on agricultural markets and
biodiversity. Nat. Commun. 10, 2844. https://doi.org/10.1038/s41467-019-10775z.
Zhang, H., Liu, M., Wang, Y., Shang, J., Liu, X., Li, B., Song, A., Li, Q., 2021. Automated
delineation of agricultural field boundaries from Sentinel-2 images using recurrent
residual U-Net. Int. J. Appl. Earth Obs. Geoinformation 105, 102557. https://doi.
org/10.1016/j.jag.2021.102557.
Zhang, D., Pan, Y., Zhang, J., Hu, T., Zhao, J., Li, N., Chen, Q., 2020. A generalized
approach based on convolutional neural networks for large area cropland mapping
at very high resolution. Remote Sens. Environ. 247, 111912 https://doi.org/
10.1016/j.rse.2020.111912.
Zhao, H., Shi, J., Qi, X., Wang, X., Jia, J., 2017. Pyramid Scene Parsing Network. In:
Presented at the Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition, pp. 2881–2890.

14

