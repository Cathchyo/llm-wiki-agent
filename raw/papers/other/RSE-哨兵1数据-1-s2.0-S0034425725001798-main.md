Remote Sensing of Environment 325 (2025) 114775

Contents lists available at ScienceDirect

Remote Sensing of Environment

journal homepage: www.elsevier.com/locate/rse

A vision foundation model-based method for large-scale forest disturbance
mapping using time series Sentinel-1 SAR data

Yuping Tian a, Feng Zhao a,*, Ran Meng b,c, Rui Sun d, Yuan Zhang a, Yanyan Shen d, Bin Wang a,
Jie Liu b,c, Mingze Li a,*
a Key Laboratory of Sustainable Forest Ecosystem Management-Ministry of Education/College of Forestry, Northeast Forestry University, Harbin 150040, China
b Artificial Intelligence Research Institute, Faculty of Computing, Harbin Institute of Technology, Harbin 150006, China
c State Key Lab of Smart Farm Technologies and Systems, Harbin Institute of Technology, Harbin 150080, China
d College of Resources and Environment, Huazhong Agricultural University, Wuhan 430070, China

A R T I C L E  I N F O

A B S T R A C T

Editor name: Dr. Marie Weiss

Keywords:
Pan-tropical deforestation
Image segmentation
C-band SAR
Large-scale model transfer
Improved greedy sampling

Accurate and timely forest disturbance mapping at large-scale is crucial for ecosystem protection and manage-
ment. Sentinel-1 SAR data, with its all-weather capability and fine spatial-temporal resolutions, offers unique
advantages for timely mapping of  forest disturbance. Although deep learning models have been used for this
purpose, they still struggle to fully exploit Sentinel-1 data’s potential due to challenges in extracting multi-scale
features and capturing context in complex landscape patterns. The advent of vision foundation models like the
Segment Anything Model (SAM) offer new possibilities to improve large-scale forest disturbance mapping with
Sentinel-1 data. However, trained with natural images, SAM had difficulty processing speckle noises in SAR and
recognizing intricate forest disturbance patterns; additionally, challenges remained in developing model transfer
strategies  and  improving  model  efficiency  for  large-scale  applications.  To  address  these  issues,  we  propose
SAMSR, a SAM-based framework adapted for forest disturbance mapping using time series Sentinel-1 data by
adding CNN branches and cross-branch attention modules to enhance fine spatial details. Firstly, we evaluated
SAMSR’s  performances  against  SAM,  U-Net  and  DeepLabv3+ at  four  global  disturbance  hotspots  with  large
variations in environmental conditions (Rondˆonia in Brazil, Guangxi in China, California in USA, and Hainan in
China). Then, we test the model’s transferability using fine-tuned transfer learning to identify the best transfer
strategy and explore the potential of active learning to further enhance model efficiency. The results indicated
that the SAMSR (IoU 0.50–0.78; F1 0.67–0.88) outperformed SAM, U-Net and DeepLabv3+ for about 23.08 %,
3.23 % and 1.59 % in IoU, respectively, while the multi-region model achieved optimal transfer performance
(IoU 0.60–0.77; F1 0.75–0.87). Moreover, applying active learning can meet the saturation accuracy of tradi-
tional  method  with  about  20  %–70  %  less  training  samples,  significantly  reducing  costs  for  fine-tuning  the
foundational model. This study thus provides a novel and efficient framework for large-scale forest disturbance
monitoring  at  fine  spatial-temporal  resolutions,  which  could  be  critical  for  forest  protection  and  ecological
studies.

1. Introduction

Large-scale  forest  disturbance  causes  severe  biodiversity  loss  and
significant  carbon  dioxide  emissions,  thereby  intensifying  the  green-
house effect and destabilizing the global climate (Altarez and Maraseni,
2023; Brockerhoff et al., 2017; Miura et al., 2015). Timely and accurate
monitoring  of  disturbance  is  thus  crucial,  as  it  can  assist  relevant
agencies in promptly detecting and addressing illegal logging activities,

and help assess and adjust forest management strategies through better
understanding its ecological consequences on biodiversity, hydrological
and carbon cycles (Decuyper et al., 2022; Griffiths et al., 2018; Wang
et  al.,  2019).  However,  traditional  field  survey  method  is  time-  and
labor-consuming, and thus cannot meet the need of forest disturbance
mapping at fine spatial-temporal resolution.

Recent advances in remote sensing technology have enabled large-
scale,  accurate  forest  disturbance  mapping  (De  Bem  et  al.,  2020;

* Corresponding authors.

E-mail address: fzhao@nefu.edu.cn (F. Zhao).

https://doi.org/10.1016/j.rse.2025.114775
Received 24 September 2024; Received in revised form 5 April 2025; Accepted 20 April 2025
Available online 29 April 2025
0034-4257/© 2025 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Hethcoat et al., 2021; Jamali et al., 2023; Solorzano et al., 2023). Optical
data served as one of the main sources for forest disturbance mapping,
detecting  disturbance  activity  through  pixel-based  or  object-based
image classification, as well as multi-temporal change detection algo-
rithms based on time series images (Chen et al., 2021; Grecchi et al.,
2017; Hethcoat et al., 2019). While optical data is vital for global forest
monitoring, its effectiveness is hindered by clouds and shadows, limiting
its capability for timely forest disturbance mapping, especially in cloud-
prone tropical areas (Alshehri et al., 2024; Cortez et al., 2024; Hansen
et al., 2013). Techniques such as multi-temporal synthesis, gap-filling,
and  multi-sensor  data  fusion  can  potentially  overcome  cloud  cover
limitations by using cloud-free observations from different times or by
combining  data  from  multiple  sensors  (Qiu  et  al.,  2023;  Wang  et  al.,
2021a, 2021b; Zhou et al., 2021). While these technologies represent a
promising direction, they also introduce some challenges. For example,
multi-sensor fusion increases computational costs and data processing
complexity,  and  may
introduce  uncertainties  due  to  temporal
misalignment or inconsistent spatial resolutions (Ghamisi et al., 2019).
In  contrast,  Synthetic  Aperture  Radar  (SAR)  can  penetrate  clouds,
offering  more  consistent  opportunities  for  frequent  disturbance  map-
ping. Sentinel-1, with its all-weather capability and short revisit inter-
val,  is  particularly  suited  for  continuous  forest  monitoring  in  cloud-
prone  regions  (Ball`ere  et  al.,  2021;  Hethcoat  et  al.,  2021).  Many
studies have utilized SAR data for forest disturbance mapping, primarily
relying on traditional approaches such as threshold-based methods and
probabilistic  detection  method,  which  involve  setting  predefined
thresholds  for  disturbance  detection  (Li  et  al.,  2022a,  2022b;  Reiche
et  al.,  2018).  Recently,  more  and  more  studies  have  highlighted  the
advantages  of  deep  learning  models,  like  U-Net,  for  improving  the
timeliness and accuracy of forest disturbance mapping using Sentinel-1
SAR data, as they can automatically learn complex features and capture
disturbance  patches  across  various  shapes  and  orientations,  out-
performing  traditional  methods  (Kattenborn  et  al.,  2021;  Solorzano
et al., 2023; Zhao et al., 2022). However, they still face challenges when
applied to Sentinel-1 data for forest disturbance mapping. Sentinel-1’s
SAR imagery is prone to speckle noises, which complicate the extraction
of  clear  and  reliable  features  necessary  for  accurate  analysis,  posing
difficulties  when  dealing  with  the  specific  multi-scale  complexities  of
forest environments. Additionally, in terms of contextual awareness, the
model’s reliance on local receptive fields can limit its ability to capture
broader  contextual  information  within  the  vast,  heterogeneous  forest
landscapes across various areas.

With advances in computer vision, foundational image segmentation
models  tailored  for  remote  sensing  data  have  emerged,  open  up  new
avenues for improving large-scale forest disturbance mapping. Recently,
Meta  AI  introduced  the  Segment  Anything  Model  (SAM),  a  powerful
computer  vision  foundation  model  trained  on  11  million  annotated
natural images, capable of accurate segmentation in complex scenarios
(Kirillov et al., 2023). A series of studies have combined optical remote
sensing  data  with  the  SAM  for  land  cover  segmentation  (Zhou  et  al.,
2024)  and  crop  type  classification  (Song  et  al.,  2024),  demonstrating
higher  mapping  accuracy  and  highlighting  the  advantage  of  SAM  in
these  tasks.  The  emergence  of  SAM  provides  new  insights  for  further
improving forest disturbance mapping based on remote sensing data.

However, integrating a foundational model like SAM with Sentinel-1
SAR  data  for  forest  disturbance  mapping  is  not  straightforward.  The
SAM was trained on a large-scale RGB images dataset and demonstrated
excellent performance on segmentation tasks. Optical imagery, such as
RGB  images,  captures  reflected  sunlight  to  provide  rich  spatial  and
spectral information that is crucial for accurate object identification and
segmentation (Liu et al., 2024). This abundance of spectral and textural
details allows models like SAM to effectively distinguish and delineate
various  objects  with  high  precision.  However,  given  the  obvious  dif-
ferences between optical and SAR images, the SAM does not perform
well on SAR images (Yan et al., 2023). SAR images rely on active mi-
crowave signals, which showed prominent speckle noises and reduced

texture features, with varying backscatter characteristics responding to
surface roughness, dielectric constant, etc., and making it difficult for
SAM, pretrained on optical imagery, to effectively identify and segment
targets (Singh and Shree, 2016; Yan et al., 2023). Moreover, the SAM
was designed for versatility and breadth of use, despite of its overall well
performance,  experiments  showed  that  it  may  miss  the  fine  structure
and cannot generate the boundary clearly and accurately for zero-shot
transfers  (Kirillov et  al., 2023). Therefore, it is  necessary to fine-tune
or  revise  the  SAM  to  enable  forest  disturbance  monitoring  based  on
SAR data.

To  achieve  this  goal,  it  is  crucial  to  enhance  the  SAM’s  ability  to
capture  finer  features  and  improve  segmentation  accuracy  for  blurry
boundaries, complex shapes, and small-sized objects. The SAM divides
the  input  image  into  non-overlapping  16  × 16  tokens  before  feature
modeling,  compromising  crucial  local  information  needed  to  identify
small targets and boundaries in S1 images, which complicates accurate
segmentation  of  disturbance  patches  with  low  contrast,  weak  bound-
aries,  and  complex  shapes.  Fortunately,  CNN  can  effectively  extract
details and edge information from images through local convolutional
operations  and  automatically  learn  local  features  at  multiple  scales,
which can significantly enhance the segmentation capability for small
targets and complex shapes (Liu et al., 2022; Ngo et al., 2024). More-
over, the effective integration of local and global features is crucial for
improving model performance. The cross-branch attention mechanism
establishes  information flow  between global  and  local features,  effec-
tively  incorporating  local  features  to  complement  the  deficiencies  of
global features, thereby enhancing the segmentation performance and
generalization ability of SAM on SAR images (Lin et al., 2023). Recent
studies show that incorporating adapters into the basic SAM structure
and  adding  CNN  branches  can  help  suppress  noises  and  enhance
extraction of  fuzzy  boundaries for  small  objects  in  ultrasound images
(Lin et al., 2023; Tu et al., 2024), yet the role of this approach in forest
disturbance monitoring and mapping based on Sentinel-1 data still re-
quires further evaluation.

Despite the promising advancements brought by SAM and its adap-
tations,  several  additional  challenges  still  exist  for  large-scale  distur-
bance mapping at fine spatial-temporal resolution. Firstly, deep learning
models  require  extensive  high-quality  annotated  data  for  training,
which  is  costly  and  time-consuming  to  acquire  (Ahmed  et  al.,  2023;
Wang  et  al.,  2021a,  2021b).  Secondly,  the  heterogenous  topography,
species  composition,  and  deforestation  patterns  make  it  difficult  for
models to transfer across different regions. Ideally, the combination of
transfer and active learning techniques with the adapted SAM can save
computational  resources  while  maximizing  the  use  of  limited  labeled
data, offering a promising solution for addressing the challenges of ef-
ficiency and cost in large-scale mapping (Pan and Yang, 2009; Wu et al.,
2019).  On  one  hand,  transfer  learning  allows  models  to  apply  pre-
trained  knowledge  to  new  tasks,  reducing  the  need  for  labeled  data
and  enhancing  adaptability  across  regions  (Ma  et  al.,  2024a,  2024b;
Martins et al., 2022; Zhu et al., 2024). Fine-tuning with local data is one
of the most used transfer learning techniques: it can reduce the need for
large amounts of labeled data, and enhance the model’s transferability
across different geographic regions and forest types (Vega et al., 2021;
Zhao et al., 2022). On the other hand, active learning addresses those
issues by optimizing the training process. Specifically, it can select the
most  representative  samples  and  avoid  redundancies  to  minimize  the
cost while optimize model performance (Cao et al., 2020; Tuia et al.,
2011; Wan et al., 2023; Wu et al., 2019).

Therefore,  in  this  study,  we  propose  a  novel  framework  called
SAMSR  with  time  series  Sentinel-1  data  to  map  large-scale  forest
disturbance across four pan-tropical hotspot areas. Here, forest distur-
bance was mainly referred to stand-replacing disturbance events. Our
specific objectives include: (1) Evaluate the spatial and temporal per-
formances  of  our  proposed  SAMSR,  with  the  SAM,  U-Net  and  Deep-
Labv3+ models  as  baselines.  (2)  Based  on  transfer  learning  methods,
determine the optimal transfer strategies of our developed framework

2

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

across four large test areas with variations in environmental conditions
(Rondˆonia in Brazil, Guangxi in China, California in USA, and Hainan in
China).  (3)  Evaluate  the  effectiveness  of  active  learning  methods  in
reducing  the  required  number  of  samples  for  model  training  and
enhancing the efficiency of SAMSR.

2. Study area and materials

2.1. Study area

The proposed framework was implemented across four study areas,
characterized  by  varying  topography  and  forest  disturbance  patterns.
The first area, in Rondˆonia, Brazil, spans 10,100 km2 within the tropical
rainforest,  a  key  area  for  large-scale  Amazon  deforestation  since  the
1960s, with elevations ranging from 90 to over  400 m (Fig.  1a). The

Fig. 1. Study areas in (a) Rondˆonia, Brazil, (b) Guangxi, China, (c) California, USA, and (d) Hainan, China. The red areas represent the sample of the study area
utilized during model development, calibration, and evaluation. The green (forest) and grey (non-forest) areas are based on data from the 2015 Hansen Global Forest
Change product. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

3

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

second  area,  in  Guangxi,  China,  covers  236,700  km2  with  elevations
from  10  to  over  2000  m,  where  forests  primarily  face  disturbance
pressures  on  eucalyptus  plantations  driven  by  economic  demands,
which  could  lead  to  significant  ecological  issues  (Fig.  1b).  The  third
area,  in  northern  California,  USA,  spans  16,500  km2  and  is  a  crucial
timber  management region  with elevations  ranging  from 200  to  over
3000 m (Fig. 1c). The fourth area, in Hainan, China, spans 35,400 km2
with elevations from 0 to over 1800 m and contains the country’s most
concentrated and largest contiguous tropical rainforest, a vital part of
the world’s tropical ecosystems, crucial for biodiversity and ecological
stability (Fig. 1d).

2.2. Reference data

High-resolution satellite images enabled the clear  identification of
disturbance  patches,  from  which  we  collected  reference  data  for  sub-
sequent use in model training, parameterization, and testing (Table 1).
Specifically,  we  utilized  3-m  resolution  Planet  images,  collected  be-
tween  January  2016  and  January  2023.  In  the  four  study  areas,  we
generated stratified point locations with uniform spatial and temporal
distribution, and ensured enough true positive and true negative sam-
ples. Each 1280 m × 1280 m square plot surrounding the selected point
(128 × 128 pixels) served as the basic spatial unit for ground reference
labeling and dataset segmentation.

2.3. Sentinel-1 data

Level-1 GRD Sentinel-1 data from the European Space Agency was
utilized for disturbance mapping, with pre-processing steps include the
application of orbit files, the removal of GRD border and thermal noise,
followed by radiometric calibration, and terrain correction. Given the
sensitivity  of  Sentinel-1  data  to  terrain  variations,  the  standardized
level-1 GRD data were further refined using 30-m SRTM DEM data to
ensure accuracy in terrain relief representation (Zhao et al., 2022).

3. Methods

In this study, we proposed a novel approach (Fig. 2) for improved
large-scale  disturbance  mapping  using  Sentinel-1  SAR  data.  The
approach included three parts: data preprocessing, model development,
and postprocessing. First, the pre-processed Sentinel-1 and Planet data
were  divided  into  training,  validation  and  test  data  for  subsequent
model evaluation. Second, the SAMSR model was constructed based on
the  characteristics  of  the  SAM  and  Sentinel-1  data.  Third,  transfer
learning technology was used to test the transferability of the SAMSR,

Table 1
Total number of plots in the study area and number of plots used for training,
parameterization and testing. PAR represents the perimeter area ratio, Q1 rep-
resents the lower quartile, M represents the median, and Q3 represents the upper
quartile.

Study
areas

Total
sample
plots

Training/
Parameterization/
Test plots

PAR
(Q1/M/
Q3)

Sample
elevation
range (m)

Rondˆonia
(Ron)

Guangxi
(GX)

California
(CA)

Hainan
(HN)

198

151 / 24 / 23

495

399 / 49 / 47

242

171 / 36 / 35

392

310 / 42 / 40

0.0103/
0.0122/
0.0138
0.0235/
0.0300/
0.0326
0.0173/
0.0195/
0.0214
0.0225/
0.0305/
0.0354

161.16 ±
20.20

378.41 ±
250.03

1521.61
± 271.42

120.94 ±
77.37

Sample
slope
range
(degree)

1.02 ±
0.43

8.21 ±
4.20

6.48 ±
3.42

2.29 ±
1.97

and evaluate the effectiveness of active learning to further improve the
efficiency  of  the  model.  Finally,  the  spatiotemporal  accuracy  of  the
disturbance products was assessed through independent monthly vali-
dation using 3-m resolution Planet images.

3.1. Forest disturbance mapping models

3.1.1. From SAM to SAMSR: A novel architecture for SAR-based forest
disturbance mapping

The SAM  architecture: The SAM  included three components, the
image  encoder,  prompt  encoder,  and  mask  decoder  (Kirillov  et  al.,
2023). The image encoder used a pre-trained Vision Transformer (ViT)
to generate image embeddings. The prompt encoder handled both sparse
(points,  boxes,  text)  and  dense  (masks)  prompts.  The  mask  decoder,
using modified Transformer blocks, applied self- and cross-attention to
update  image  and  prompt  embeddings.  After  two  decoder  layers,  the
image  embeddings  were  upsampled  and  passed  through  an  MLP  to  a
dynamic  linear  classifier,  outputting  the  foreground  mask  probability
for each position.

The  SAMSR  architecture:  The  SAMSR  retained  SAM’s  prompt
encoder and mask decoder, adding a parallel CNN branch to the image
encoder. The CNN and ViT branches established global dependencies via
a  Cross-Branch  Attention  (CBA)  module,  producing  the  final  image
feature embedding. In the ViT branch, added a position adapter and five
feature adapters fine-tune position embeddings and aligned input fea-
tures  with  the  pre-trained  ViT  encoder.  The  first  feature  adapter
adjusted input features to match the ViT encoder’s distribution, while
the remaining adapters refined the pre-trained encoder through residual
connections to better suit the specific task.

The SAMSR specific details: As shown in Fig. 2, the input image
was  first preprocessed  and  tokenized,  then fed  into  both  the  ViT  and
CNN branches. In the CNN branch, the image passed through a single
convolutional  block,  followed  by  three  convolutional  pooling  blocks,
and then the same convolutional block was repeated four times. In the
ViT  branch,  the  image  undergoes  overlapped  patch  embedding  and
position  embedding  (patch  size:  16  × 16),  followed  by  optimization
through the feature adapter and position adapter modules. The feature
adapter  consisted  of  two  linear  layers  with  an  activation  layer  in  be-
tween, followed by a residual connection, allowing the ViT branch to
better adapt to the SAR image feature distribution. The position adapter
was a convolutional layer that adjusted position embeddings to match
the resolution of the embedding sequence, first by downsampled with
max pooling (stride: 2, kernel size: 2) and then refining with a 3 × 3
convolution.

The embeddings were processed through the window transformer,
where attention was computed only between patches within a 14 × 14
window, reducing computational complexity (Li et al., 2022a, 2022b).
The embeddings then passed through multiple ViT transformer blocks
(using the pre-trained ViT-B model with 12 layers of transformers) and
interacted with every global transformer via the CBA module, injecting
local  CNN  features  into  the  ViT  branch.  The  CBA  module  used  CNN
embeddings  as  key  and  value,  while  ViT  embeddings  serve  as  query.
After fine-tuning each global transformer layer with the feature adapter,
the output was combined with the feedforward network via a residual
connection. The final image embeddings from both the  ViT and  CNN
branches were summed and input to the mask decoder. Simultaneously,
a point prompt was randomly selected from the label mask area, and a
point  prompt  embedding  was  generated  by  the  prompt  encoder.  The
mask decoder combined embeddings from the ViT branch, CNN branch,
and prompt, outputting the image’s features. The image features were
upsampled through convolution and multiplied by the query embedding
to generate the predicted result. This was then interpolated back to the
original resolution and compared with the label masks to calculate the
loss, which was used for backpropagation to train the model.

Training Strategies: SAMSR initialized the parameters from SAM,
and  the  pre-trained  model  used  the  initial  weights  of  SAM’s  ViT-B

4

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Fig. 2. The workflow of the SAMSR model.

(Kirillov  et  al.,  2023).  The  number  of  samples  used  for  training  the
model in the four areas was 198, 495, 242 and 392, respectively, and the
specific  details  were  shown  in  Table  1.  The  training  process  was  su-
pervised  by  a  combined  loss  function,  including  dice  loss  and  binary
cross-entropy  loss.  The  model  was  implemented  within  the  PyTorch
framework, we used Adam as the optimizer with an initial learning rate
of 0.0001, a batch size of 8, and trained the model for 200 epochs. The
input size was 128 × 128 pixels, with 2 bands (VV and VH), and the
output size was 128 × 128 × 1, where each pixel value represented the
probability of forest disturbance. Pixels with a probability greater than
0.5 were classified as disturbance.

3.1.2. Baseline models

We  employed  the  U-Net  model  (Zhao  et  al.,  2022)  and  the  Deep-
Labv3+ model (Chen et al., 2018; Ma et al., 2024a, 2024b) as baselines
to  compare  with  the  SAMSR.  In  the  U-Net’s  ‘downsampling’  section,
pooling reduced spatial dimensions, and we set up four convolutional
layers  where  the  channels  expand  from  8  to  128  to  capture  complex
features. The ‘upsampling’ section then upscaled these features, merging
them with corresponding downsampling features via skip connections to
maintain spatial details. We used ReLU activation in all convolutional
layers  except  the  final  one,  where  a  sigmoid  function  outputs  values
between 0 and 1. The U-Net was trained using a combination of binary
cross-entropy loss and dice loss, with the Adam optimizer set at an initial
learning rate of 0.0001.

DeepLabV3+ was an advanced image semantic segmentation model
that used MobileNetV2 (Sandler et al., 2018) as its backbone network.
MobileNetV2  employed  an  efficient  inverted  residual  structure  and
depthwise  separable  convolutions,  which  significantly  reduce  compu-
tational  complexity  while  maintaining  high  feature  representation
capability. To better recover image boundaries and fine details, Deep-
LabV3+ introduced a decoder module, which combined low-level fea-
tures from the encoder with high-level features through upsampled and

skip  connections,  refining  the  segmentation  results.  Additionally,  the
model integrated atrous spatial pyramid pooling (ASPP) in the decoder,
which extracted multi-scale features using convolutions with different
dilation rates, further improving its segmentation performance in com-
plex scenes. The loss function and hyperparameters used during model
training were consistent with those in SAMSR.

3.2. Accuracy assessments

The  performance  of  the  classification  models  (SAMSR,  U-Net,
DeepLabv3+ and SAM) was evaluated using an independent test data.
To  assess  model  accuracy,  we  calculated  several  metrics,  including
Overall  Accuracy  (OA),  User’s  Accuracy  (UA),  Producer’s  Accuracy
(PA), F1 Score, and Intersection over Union (IoU) as defined in formulas
(1)–(5). The F1 Score, representing the geometric mean of UA and PA,
provides a more precise measure of model performance compared to OA.
IoU quantifies the ratio of the intersection to the union area between
predicted and actual results.

OA =

TP + TN
TP + TN + FP + FN

UA = TP

TP + FP

PA = TP

TP + FN

F1 = 2*UA*PA
UA + PA

=

2TP
2TP + FP + FN

IoU = Area of Overlap
Area of Union

=

TP
TP + FP + FN

(1)

(2)

(3)

(4)

(5)

where TP, TN, FP, FN represent true positive, true negative, false posi-

5

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

tive, and false negative, respectively.

To  evaluate  the  accuracy  of  the  final  monthly  forest  disturbance
products, we randomly selected 100 quadrats (1280 × 1280 m) from the
produced monthly products in each study area, evenly distributed across
time and space during the study interval and area. These quadrats were
independently assessed using Planet imagery. Two interpreters manu-
ally  outlined  disturbance  and  non-disturbance  areas  by  synthesizing
reference images from the target and months before and after. An in-
dependent analyst then compared these manually drawn reference maps
with the final monthly disturbance maps to calculate the accuracy of the
final monthly disturbance products.

“Sigmoid  Accuracy”  (Bullock  et  al.,  2022)  assessment  framework
was used to assess the spatiotemporal accuracy of our monthly distur-
bance  products.  This  framework  focused  on  the  relationship  between
timeliness  and  accuracy,  with  key  indicators  including  the  “Initial
Delay”  and  the  “Level  Off  Point”,  which  were  derived  from  the  “F1
score” curve as a function of “lag”. The “Initial Delay” was identified as
the point where the F1 begins to rise, while the “Level Off Point” was
determined based on the saturation point of the F1. The “lag”  started
from  0,  indicating  that  the  detection  month  was  consistent  with  the
reference data, and 1 indicated that the detection month was one month
later  than  the  reference  data,  and  so  on.  This  approach  provides  a
comprehensive assessment of the temporal and spatial accuracy of our
monthly disturbance mapping results.

3.3. Evaluating the SAMSR’S transferability

To  evaluate  the  transferability  of  our  proposed  framework  across
four  study  areas,  we  conducted  the  following  model  transfer  experi-
ments:  (1)  We  trained  the  SAMSR  model  separately  for  each  area
(Rondˆonia  in  Brazil,  Guangxi  in  China,  California  in  the  USA,  and
Hainan in China) using local samples, starting with 10 input objects and
increasing the training data until performance plateaued (measured by
IoU). (2) We then applied each saturated local model to the remaining
three study areas, progressively adding local samples until saturation.
(3) Finally, we applied integrated models trained on three areas to the
fourth area, incrementally increasing samples.

Gradually  increasing  the  training  data  allowed  us  to  assess  how
performance  improves  with  sample  size  and  determine  the  minimum
data  required  for  stable  results.  Comparing  the  accuracy  of  local  and
transferred models at different sample sizes helped us understand the
relationship  between  data  size  and  performance,  providing  a  more
effective evaluation of the SAMSR model’s transferability. In testing the
model’s  transferability,  we  employed  fine-tuning-based  transfer
learning approach. According to the transfer learning outlined by Ma
et  al.  (2024a,  2024b),  which  categorizes  transfer  learning  into  five
distinct types with fine-tuning being the most common. We began by
initializing the network weights with pre-trained model developed using
Sentinel-1 SAR data from source area. Then, all layers of the network
were retrained using labeled samples from target area, which allowed
the model to fully adjust both low- and high-level feature detectors to
better capture the specific patterns and nuances of the target area. This
comprehensive fine-tuning enabled the model to adapt its feature rep-
resentations to the unique spatial characteristics of the target area while
leveraging the generalized features learned from the source domain.

that measures the randomness or uncertainty of information (Shannon,
1948).  In  image  processing,  entropy  measures  an  image’s  complexity
and information content. High entropy indicates greater complexity and
more  information,  providing  a  quantitative  method  for  analysis.  The
formula is as follows:
∑
n

H(X) = (cid:0)

i=1p(xi)log2p(xi)

(6)

where n is the number of different states that the random pixel value X
can take, and p(xi) is the probability of X taking the value xi.

The iGS process includes: (1) GS for input (GSx), selecting samples
based on proximity to the centroid. (2) GS for output (GSy), selecting
samples based on output value diversity. (3) iGS, combining input and
output  diversity  to  select  samples.  Iterations  continue  until  the
maximum sample number (K) is reached. To compare iGS with random
sampling, nine sets of sample gradient experiments were conducted.

To demonstrate the effectiveness of active learning, T-SNE (Van der
Maaten and Hinton, 2008) was used to visually show the features and
distribution of selected samples. Here, random and active samples were
plotted for each study area with a sample size of 30. Additionally, the
clustering metric F-score of the samples was calculated to evaluate the
impact  of  the  active  learning  selection  sample.  Moreover,  this  study
plotted the distribution histogram of the samples’ VH values as well as
the density plot and information entropy to further assess the perfor-
mance of active learning.

3.5. Monthly forest disturbance map production and analysis

To quantitatively assess the dynamic of large-scale mapping results,
it is crucial to integrate temporal change analysis into the methodology.
This  study  utilized  the  monitoring  window  in  Fusion  Near  Real-Time
(FNRT)  approach  to  continuously  monitor  the  change  of  time  series
(Tang et al., 2023a, 2023b). The FNRT monitoring window based on the
results from the SAMSR to create dense time series, on which the method
operated to monitor disturbances and detect dates. Although the SAMSR
had segmented the disturbance patches, noise in the data may cause the
model  to  incorrectly  segment  an  image,  leading  to  errors.  To  reduce
noise  while  ensuring  timely  detection,  the  FNRT  monitoring  window
minimized  noise  effects  by  “confirm”  changes  through  multiple  suc-
cessive detections. Model parameters, the monitoring window size (n)
and consecutive changes (k), determined the method’s sensitivity. The
method  identified  disturbances  when  k  consecutive  changes  occurred
within the monitoring window, marking the first change’s date. After
testing  various  parameters,  the  final  disturbance  map  was  generated
using  n  = 5  and  k  = 3.  Fig.  S6  illustrates  how  the  FNRT  monitoring
window to continuously monitor the results of the SAMSR. Using the
optimal mapping model, monthly disturbance regions were mapped for
four study areas from 2016 to 2023 (including 96 consecutive months).
First,  non-forest  areas  were  excluded  using  the  Hansen  GFC  product.
Then, the FNRT algorithm assigned year-month labels to each  distur-
bance area. A threshold of 900 m2 was applied to remove small patches,
and only areas overlapping with Hansen GFC changes by more than 50
% were included in the final maps.

4. Results

3.4. The effectiveness of active learning

4.1. Accuracy assessments of forest disturbance mapping models

When  applying  transfer  learning  models,  augmenting  application
scenarios  with  new  local  samples  is  crucial.  This  paper  employed  an
improved  Greedy  Sampling  (iGS)  method  for  selecting  representative
samples,  which  was  shown  to  outperform  traditional  active  learning
algorithms, by achieving comparable performance with fewer samples
while conserving computational resources (Wan et al., 2023). The iGS
algorithm  leveraged  entropy  to  estimate  the  representativeness  of
selected samples, which is an important concept in information theory

Using randomly selected  disturbance patches,  we plotted  the  time
series boxplots of SAR backscattering coefficients (VV and VH boxplots
of nine months before and after forest disturbance) for the four study
areas (Fig. S1). The VH coefficients showed significant deviations be-
tween stable forests and disturbances across all study areas (Ron, GX,
CA, and HN). In contrast, the VV values (Fig. S1a, S1c, S1e, and S1g)
displayed  less  pronounced  variations,  although  disturbances  consis-
tently showed slightly lower VV values compared to stable forests. These

6

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

findings highlight the utility of VH coefficients as a critical indicator in
detecting  forest  disturbance  events  across  diverse  geographical  envi-
ronments, making it a valuable tool for monitoring forest health using
SAR data.

To rigorously examine the specific role played by each module and
assess their true contribution to the model’s performance, we conducted
ablation  study  by  sequentially  introducing  the  four  modules  from
SAMSR—CNN branch, CBA, feature adapter, and position adapter—into
the SAM, with the results shown in Table S1. Each module can effec-
tively improve the segmentation performance and generalization ability
of SAM on SAR images. In particular, the addition of the feature adapter
module led to significant increase in F1 score over the SAM (with local
sample fine-tuning), with improvements of 7 %, 14 %, 7 %, and 10 %
across  four study  areas. Furthermore, simply fusing the  output of the
CNN and ViT branches was not the best approach, introducing the CBA
module further facilitated the integration of local features. By coupling
these four components, SAMSR achieved the best segmentation perfor-
mance and generalization results.

Table  S2  showed  the  results  of  the  original  SAM  (without  local
sample fine-tuning) for direct predictions. The results indicated that the
original SAM performed the worst, with an F1 score of only 0.09 on the
comprehensive  dataset.  After  fine-tuning  with  samples  (SAM),  the  F1
score quickly increased to 0.68, and after improvements, the F1 score to
0.78.

Based on independent test data, the SAMSR outperformed the U-Net,
DeepLabv3+ and SAM in all scenarios, with an overall accuracy ranging
from 86 % to 94 % (the combined model for the four study areas ach-
ieved 88 %). The user’s and producer’s accuracies were 69 %–83 % and
66  %–93  %,  respectively  (for  the  combined  model  of  the  four  study
areas,  the  user’s  and  producer’s  accuracies  were  79  %  and  77  %,
respectively) (Table 2). The SAMSR’s F1 score and IoU ranged from 0.67
to 0.88 and 0.50 to 0.78, respectively (the combined model for the four
study  areas  achieved  an  F1  score  of  0.78  and  an  IoU  of  0.64).  The
combined  model  based  on  DeepLabv3+ for  the  four  study  areas  ach-
ieved an overall accuracy of 88 %, with F1 score of 0.77 and IoU of 0.63,
respectively.  The  U-Net’s  F1  score  and  IoU  were  0.75  and  0.62,
respectively. The SAM had the lowest accuracy, with F1 of 0.68.

Comparing  the  spatial  mapping  results  with  the  reference  and
baseline predictions, the SAMSR showed the greatest similarity to the
reference labels in spatial location and boundary consistency (Fig. 3).
The  U-Net  model  produced  more  false  negatives  than  SAMSR.  In
contrast, SAM’s predictions were the least accurate overall.

Table 2
Values of the evaluation results of the independent test plots.

Study areas

Models

Ron

GX

CA

HN

All data

U-Net
DeepLabv3+
SAM
SAMSR
U-Net
DeepLabv3+
SAM
SAMSR
U-Net
DeepLabv3+
SAM
SAMSR
U-Net
DeepLabv3+
SAM
SAMSR
U-Net
DeepLabv3+
SAM
SAMSR

OA

0.88
0.89
0.84
0.90
0.83
0.84
0.76
0.86
0.93
0.94
0.91
0.94
0.87
0.86
0.83
0.87
0.88
0.88
0.83
0.88

UA

0.85
0.82
0.78
0.83
0.82
0.81
0.70
0.82
0.87
0.80
0.74
0.79
0.71
0.63
0.56
0.69
0.78
0.79
0.71
0.79

PA

0.89
0.92
0.81
0.93
0.69
0.78
0.60
0.77
0.70
0.85
0.72
0.84
0.55
0.61
0.51
0.66
0.73
0.76
0.66
0.77

F1

0.87
0.87
0.79
0.88
0.75
0.79
0.65
0.79
0.77
0.82
0.73
0.81
0.62
0.62
0.53
0.67
0.75
0.77
0.68
0.78

IoU

0.76
0.77
0.66
0.78
0.60
0.64
0.47
0.66
0.63
0.67
0.56
0.68
0.45
0.45
0.36
0.50
0.62
0.63
0.52
0.64

Fig. 3. Spatial display of the reference and prediction results from the U-Net,
DeepLabv3+,  SAM  and  SAMSR  models.  The  first  row  presents  Planet  high-
resolution  images,  followed  by  VV  and  VH  of  Sentinel-1  in  the  second  and
third  rows.  The  fourth  row  contains  manually  drawn  labels,  the  fifth,  sixth,
seventh and eighth rows show the prediction results of the U-Net, DeepLabv3+,
SAM and SAMSR models, respectively.

4.2. SAMSR transferability assessment

Results showed that more complex patches require more samples to
fully train the model, whereas simpler patches require fewer (Table S3).
The PAR in Hainan was significantly higher than that of the other areas,
indicating greater mapping challenges in this region (Table 1). The IoU
in Hainan reached saturation at around 150 local training patches, while
in Ron, with the lowest PAR, it saturates at 100 patches, and reached 0.7
IoU with just 40 patches. Similar trends were observed in F1 and OA
across all areas (Table S4).

The complexity of patches also affected the model’s transferability.
Applying a fully trained model from one area to another without fine-
tuning  did not yield high accuracy.  However,  fine-tuning with  sparse
local  patches  improved  performance  significantly.  This  spatial  trans-
ferability may be influenced by the variations in the complexity of the
disturbance patches shapes (Table S3). For example, a model pre-trained
in  Ron,  when  applied  to  Hainan,  initially  achieved  an  IoU  of  0.31.
Retraining with 10 local patches from Hainan increased the IoU to 0.56,
and the IoU saturated at 150 patches. Conversely, applying a Hainan-
trained model to Ron reached 0.71 in IoU with just 10 samples, while
the  IoU  saturated  at  40.  These  findings  suggest  that  areas  with  more
complex patches (higher PAR) require more local samples for effective
model  transfer.  To  further  explore  transferability,  models  trained  on
three areas were applied to the fourth, with gradually increasing sample
numbers. This approach generally yielded better accuracy compared to
single-area transfers (Table S3), with final accuracies consistently higher
or similar to other methods. Maximum F1 and IoU values for each area
were summarized in Table 3.

4.3. Effectiveness of active learning for SAMSR accuracy and efficiency

This  study  demonstrated  that  active  learning  consistently  out-
performs random sampling in improving model accuracy across study
areas.  Specifically,  as  shown  in  Fig.  4,  Fig.  S2–S5,  and  Table  S5,  the

7

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Table 3
The maximum F1 and IoU values for the transferability testing for study areas.
The values with different samples are shown in Table S1 of the supplementary
material.

Study areas

Maximum F1 / IoU for the models

Ron

GX

CA

HN

Local
0.87/0.77
Local
0.77/0.62
Local
0.81/0.68
Local
0.73/0.58

GX
0.87/0.77
Ron
0.75/0.60
Ron
0.83/0.72
Ron
0.75/0.60

CA
0.86/0.77
CA
0.77/0.62
GX
0.81/0.68
GX
0.75/0.60

HN
0.86/0.76
HN
0.78/0.64
HN
0.82/0.71
CA
0.74/0.58

Multi-region
0.87/0.77
Multi-region
0.79/0.65
Multi-region
0.84/0.74
Multi-region
0.75/0.60

active  learning  method  achieved  higher  accuracy,  particularly  with
fewer  samples,  reducing  annotation  costs.  Additionally,  the  Fig.  4
highlighted the transferability of active learning in multi-region models,
where it reached saturation with fewer samples while maintaining su-
perior accuracy.

Active  learning  technique  can  meet  the  saturation  accuracy  of
traditional random selection with about 20 %–70 % less training sam-
ples. Specifically, the GX model transferred to Ron achieved an IoU of
0.76 with 30 samples using active learning, comparable to or surpassing
random sampling with 100 samples (Fig. S2b). In Ron, active learning
consistently  outperformed  random  methods  under  all  sample  condi-
tions, with accuracy saturating around 40 samples (Fig. S2a), a trend
also observed in GX models. The difference in accuracy between the two
methods  was  more  pronounced  in  GX  models,  with  active  learning
achieving higher final saturation accuracy (Fig. S3). While the difference
between the two methods in CA and HN was smaller, active learning still
required  fewer  samples  to  reach  saturation  compared  to  random
methods  (Fig.  S4  and  S5).  These  findings  highlight  the  advantage  of
active learning, where fewer samples can achieve or exceed the satu-
ration effect of random sampling.

The T-SNE plots (Fig. 5, left) and VH value distribution plots (Fig. 5,
middle and right) demonstrated that the samples selected through active
learning were more evenly distributed in the feature space, indicated
that they covered the underlying data distribution more extensively and
were  thus  more  representative.  The  higher  entropy  values  observed
across all study areas further support this point (Fig. 5, right), suggested
that the active samples were more effective in capturing the diversity
and  key  features  of  the  data.  The  higher  F-scores  also  suggested  that

these samples were more effective in capturing the intrinsic structure of
the data (Fig. 5, left), making them a more valuable choice for training
models.  In  contrast,  the  random  samples  exhibited  a  narrower  distri-
bution  and  lower  entropy,  indicated  that  they  captured  less  of  the
dataset’s complexity. Although the entropy values for random samples
were higher than those for the overall sample in most cases, capturing
some diversity, they often failed to fully represent the complexity of the
data, particularly in certain cases, such as at GX (Fig. 5b). This further
underscore  the  effectiveness  and  stability  of  the  active  learning
approach. Overall, these visualizations and metrics indicated that the
samples  selected  through  active  learning  were  more  representative,
exhibited  a  broader  distribution,  and  contained  richer  information
compared to random samples and the overall dataset.

4.4. Monthly forest disturbance mapping from 2016 to 2023

To  further  evaluate  the  spatiotemporal  accuracy  of  the  monthly
disturbance products, we analyzed the relationship between lag and F1-
scores (Fig. 6). At an initial delay (lag = 0), F1-scores for Ron, GX, CA,
and  HN  were  0.49,  0.49,  0.72,  and  0.60,  respectively.  As  the  lag
increased, the F1-scores gradually increased and saturated at 0.83, 0.61,
0.89 and 0.63, respectively. At this point, the corresponding lags were
four months, three months, three months, and one month, respectively.
The results revealed varying spatiotemporal accuracies across the study
areas. The CA and Ron achieved higher F1-scores, indicating that the
proposed method performed well in these study areas. In contrast, GX
and HN exhibited relatively lower F1-scores, likely because areas had
more  fragmented  disturbance  patches  (mean  perimeter-to-area  of
0.0300 and 0.0305, respectively, compared with 0.0195 and 0.0122 in
CA  and  Ron),  which  posed  greater  challenges  for  the  model.  These
findings  validated  the  overall  effectiveness  of  SAMSR  in  mapping
monthly  disturbance  while  highlighting  the  influence  of  disturbance
patch complexity on model performance.

Utilizing  the  optimal  mapping  framework  identified  earlier  (the
SAMSR), we mapped and analyzed monthly disturbance maps for the
four areas from 2016 to 2023. During the study period, the disturbed
areas of Ron were approximately 819.81 km2, equivalent to 7.46 % of
the study area. The most significant losses occurred in 2017, approxi-
mately 170.28 km2, with a peak in August (approximately 42.26 km2,
Fig.  7a).  In  GX,  the  total  disturbed  areas  were  approximately  121.03
km2, accounting for about 1.10 % of the study area (Fig. 7b). For CA, the

Fig. 4. The IoU values of random and active methods under different samples for the Ron (a), GX (b), CA (c), and HN (d) areas. The figure represents a multi-region
synthesis model for three additional areas. For the single area model, see Fig. S2-S5 in the supplementary material.

8

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Fig. 5. T-SNE visualization and clustering metric F-score (left), VH value distribution histogram (middle), and VH value density distribution and information entropy
(right) for all samples, random samples, and active samples in (a) Ron, (b) GX, (c) CA, and (d) HN.

total  disturbed areas  were approximately  493.06 km2,  accounting  for
about 2.98 % of the study area (Fig. 7c). Disturbance was most prevalent
in  2021  (approximately  276.52  km2,  and  23.04  km2  per  month),  fol-
lowed  by  2022  and  2020.  In  HN,  the  total  disturbed  areas  were
approximately 239.58 km2, accounting for about 2.12 % of the study
area (Fig. 7d). In Ron, the disturbances occurred mainly during the dry
season, especially at the end of the dry season (August–October). The
interannual variation of disturbance in CA was large, which showed the
influence of single disturbance event. In GX and HN, the disturbance was
more evenly distributed throughout the year.

5. Discussion

In  this  study,  we  proposed  a  novel  framework  that  leverages  the
SAM, a vision foundation model, and Sentinel-1 SAR data to map forest
disturbance at fine spatial-temporal scales (Fig. 2). Results showed that
SAMSR (IoU 0.50–0.78; F1 0.67–0.88) outperformed the baseline SAM,
U-Net and DeepLabv3+ methods for about 23.08 %, 3.23 % and 1.59 %
in IoU, respectively, with high transferability across four distinct forest
disturbance hotspots (Rondˆonia in Brazil, Guangxi in China, California
in  the  USA,  and  Hainan  in  China)  (Table  2,  Fig.  3).  The  best  model
transfer strategy across-areas based on transfer learning was the com-
bined  model  trained  on  multi-region  samples,  with  IoU  from  0.60  to
0.77, F1 from 0.75 to 0.87 (Table 3, Table S3, Table S4). Furthermore,
active  learning  significantly  enhanced  the  model’s  efficiency  and

9

Fig. 6. The spatiotemporal accuracy illustrated by the lag / accuracy curve of
monthly forest disturbance mapping. F1 gradually increases with higher lag and
reaches the Level Off Point (stars).

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Fig. 7. (a). Monthly disturbance results for the study area in Rondˆonia from 2016 to 2023. Three green circle areas are shown with zoom-in views. Adjacent to these
zoomed-in views are images from Planet, depicting the months before and after disturbance. The bar chart is the monthly statistical chart of disturbed forest area.
(b). Monthly disturbance results for the study area in Guangxi from 2016 to 2023. Select the central area of Guangxi for mapping and analysis.
(c). Monthly disturbance results for the study area in California from 2016 to 2023.
(d). Monthly disturbance results for the study area in Hainan from 2016 to 2023. Select the central area of Hainan for mapping and analysis.

10

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Fig. 7. (continued).

performance  by  achieving  or  exceeding  the  saturation  accuracy  of
traditional  random  selection  methods  with  20  %–70  %  less  samples
(Table S5, Fig. 4, Fig. S2-S5).

5.1. Performance of the SAMSR in disturbance mapping based on
Sentinel-1 data

The  proposed  SAMSR  significantly  enhanced  the  ability  to  detect
forest disturbance in SAR images. Compared with the SAM, U-Net and

DeepLabv3+ models, the IoU improved by about 23.08 %, 3.23 % and
1.59  %,  respectively  (Table  2).  The  SAM  has  demonstrated  excellent
performance  in  various  scene  segmentation  tasks,  such  as  buildings,
roads, and crop monitoring, based on optical images (Song et al., 2024;
Zhang et al., 2024). However, integrating SAM and S1 SAR for forest
disturbance mapping involves unique challenges due to the differences
between  optical  and  SAR  imagery.  Optical  data,  while  offering  rich
spectral and textural information, is highly dependent on external fac-
tors such as weather conditions and seasonal changes (Alshehri et al.,

11

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

2024).  This  issue  makes  it  difficult  to  obtain  consistent,  high-quality
images  for  accurate  disturbance  detection,  especially  in  tropical  re-
gions  where  cloud  coverage  is  frequent  and  persistent.  Due  to  the
complex and dynamic nature of forest environments, applying SAM to
forest disturbance mapping using SAR data is vital but also more chal-
lenging because of the presence of speckle noise and the variation in the
size, shape, and intensity of disturbance patches (Tsokas et al., 2022).
Therefore, we modified the model by incorporating the CNN branch and
cross-branch attention, which enhanced the extraction of local features
and the integration of global information, significantly improving the
detection  of  forest  disturbance  (Table  2,  Table  S2,  Fig.  3).  The  CNN
offered  significant  advantages  in  extracting  small  targets  and  recog-
nizing fine details, while the cross-branch attention established infor-
mation flow between global and local features, further strengthening the
synergy  between  them.  This  approach  has  been  applied  in  extracting
features from medical images, particularly ultrasound images, success-
fully  capturing  small  targets  and  weak  boundary  objects  (Lin  et  al.,
2023; Tu et al., 2024), while our study serves as the first investigation for
adapting  SAM  to  detect  forest  disturbance  from  S1  SAR  images.  Our
modifications  further  improved  SAM’s  generalization  ability  in  SAR
tasks  and  enhanced  its  adaptability  in  complex  image  segmentation
tasks. Traditional methods often struggle to capture the complex details
of  disturbance  patches  (Kattenborn  et  al.,  2021),  while  the  modified
SAM overcame these challenges by integrating global and local features,
enabling  accurate  detection  of  subtle  disturbance.  By  effectively
applying SAM to SAR data, the proposed approach provides new pos-
sibilities  for  large-scale,  accurate  monitoring  of  global  forest  distur-
bance. However, despite these improvements, there is still potential for
further optimization. Future research could explore effective methods
for integrating and analyzing multi-modal data within the SAM frame-
work,  which  would  enhance  the  model’s  adaptability  and  reliability
across a wider range of data scenarios (Li et al., 2023; Tang et al., 2023a,
2023b).

The superior performance of SAMSR could be attributed to its fine-
tuning, which  leveraged pre-trained  models, a strategy that was  both
cost-effective  and  practical  in  real-world  applications.  Training  large
models from scratch requires  significant computational  resources and
large datasets (Ahmed et al., 2023; Wang et al., 2021a, 2021b), which
many  institutions  cannot  afford.  In  contrast,  fine-tuning  pre-trained
models like SAM enables high performance with fewer training samples,
making it a valuable approach. Thus, the comparison with a small model
like U-Net is not only about model capacity, but also about the practical
feasibility  of  using  a  large  pre-trained  model.  Furthermore,  to  better
understand the detection capabilities and generalization ability of the
SAMSR model, we compared the detection results with the GLAD forest
disturbance dataset (Hansen et al., 2016; Pickens et al., 2020; Reiche
et  al., 2021). For  each study area, we randomly selected 20 quadrats
(1280 × 1280 m) and calculated the accuracy separately according to
the  year.  Since  the  GLAD  dataset  did  not  include  the  CA  area,  we
compared it with the other three areas. According to the Table S6, in the
Ron  area,  the  GLAD  dataset’s  accuracy  was  slightly  higher  than  our
results (mean GLAD-F1 score was 0.07 higher), but for the GX and HN
areas,  the  advantage  of  our  results  was  very  clear  (mean  SAMSR-F1
score was 0.55 and 0.67 higher, respectively). While GLAD combined
data from three sources (Landsat, Sentinel-2, Sentinel-1), our method,
using only Sentinel-1 data, achieved comparable accuracy, highlighting
its advantage. Moreover, we found that the GLAD dataset missed many
detections of GX and HN areas (Fig. S7), compared with other areas, the
GX and HN showed more complex landscape patterns, indicated that our
method has greater advantages in detecting small-scale disturbance and
complex landscape patterns. One possible reason for this was that the
samples of the GLAD-L method were selected in wet forests, which may
have  limitations  when  applied  to  pantropical  regions  (Hansen  et  al.,
2016). Despite the high potential of SAR data for consistent mapping in
cloud-prone  regions  (Mullissa  et  al.,  2023;  Reiche  et  al.,  2021;  Zhao
et  al.,  2022),  the  presence  of  speckle  noise  and  the  lack  of  spectral

information limits its capabilities (Guo et al., 2022), and optical data
could  provide  complementary  spectral  information.  Some  techniques
such  as  multi-temporal  synthesis,  gap-filling,  and  multi-sensor  data
fusion (Qiu et al., 2023; Wang et al., 2021a, 2021b; Zhou et al., 2021),
could  contribute  to  the  fusion  of  SAR  and  optical  data  for  improved
accuracy and robustness in challenging environments, which are beyond
the scope of this study. For future studies, we could explore the hybrid
architecture of SAR and optical image fusion, integrating complemen-
tary information from multiple sources to further improve SAR moni-
toring capabilities (Liu et al., 2024; McGregor et al., 2024; Reichstein
et al., 2019). These efforts would help overcome the inherent limitations
of SAR images and extend the applicability of models like SAMSR to a
broader range of remote sensing tasks.

5.2. Application and advantages of transfer learning in forest disturbance
mapping

This study demonstrated the usefulness of transfer learning in forest
disturbance mapping: the transfer learning technique reduced the need
for extensive labeled data while enhancing the model’s generalization,
maintaining efficiency across various environments. The model achieves
high  accuracy  in  different  areas  with  minimal  local  training  data,
making  it  valuable  for  large-scale,  resource-limited  forest  monitoring
(Table 3, Table S3, Table S4). Transfer learning significantly improved
the accuracy of the model, especially the combined model with multi-
region  achieved  the  best  transfer  performance  (Table  3).  This
improvement may be due to the similarity within disturbance datasets,
allowing the model to leverage learned patterns effectively (Ehrig et al.,
2024; Ma et al., 2024a, 2024b). However, in CA, without local samples,
the model pre-trained in HN (IoU = 0.55) outperformed the combined
model  (IoU  = 0.49),  likely  due  to  the  higher  PAR  and  complexity  of
patches in CA and HN (Table 1). As more local data became available,
the combined model’s advantages became more apparent with the local
sample 30 was added, the combined model (IoU = 0.70) exceeds the HN
model (IoU = 0.69), and the final IoU was 4.2 % higher than the HN
model.

In this study, we gradually increased the training data to assess how
sample size affects model performance and transferability (Table S3-S4).
By comparing local models with transferred models, we gained deeper
insights into the SAMSR model’s ability to transfer across regions and its
transferability  with  varying  sample  sizes.  This  approach  provided  a
more reliable understanding of the model’s adaptability and its potential
for broader application. The application of transfer learning should be
grounded  on  a  solid  understanding  of  the  underlying  remote  sensing
mechanism. The success of our proposed model in transfer learning was
largely  due  to  its  ability  to  capture  landscape  patterns,  which  were
relatively  stable  and  transferable  across  different  regions,  and  thus
enabled effective transfer (Zhao et al., 2022). However, the success of
transfer  learning  is  not  solely  dependent  on  the  similarity  between
source and target domains, but also on the robustness of the model to
adapt  to  different  contexts  (Weiss  et  al.,  2016;  Zhuang  et  al.,  2020).
SAMSR’s  architecture,  designed  to  capture  these  landscape  patterns,
plays a crucial role in this adaptability.

5.3. Active learning techniques improve forest disturbance mapping
efficiencies

The initial performance of model without adaptation was suboptimal
due  to  the  non-stationarity  of  sample  distribution  across  study  areas
(Table  S3–S4).  This  requires  incorporating  target  domain  samples  to
improve the model’s cross-spatial generalization. Traditionally, this in-
volves  random  sample  selection,  which  can  negatively  impact  model
performance  if  selected  ineffectively  (Hamrouni  et  al.,  2021).  Active
learning enhances training efficiency by selecting the most representa-
tive  samples,  minimizing  the  number  of  samples  needed  for  domain
adaptation while maintaining high recognition capability (Alajlan et al.,

12

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

2013;  Crawford  et  al.,  2013).  When  the  comprehensive  model  was
transferred to CA with the addition of 10 local samples, the model ac-
curacy (IoU = 0.55) was much lower than that of the HN pre-trained
model  (IoU  = 0.63).  However,  with  the  participation  of  the  active
learning  method,  the  accuracy  of  the  comprehensive  model  rapidly
improved (IoU = 0.64) and approached the accuracy of the HN model
(IoU = 0.66) (Table S5). In some cases, the number of additional samples
needed by the random method was twice that of the active method. For
example, when transferring the HN model to Ron, to achieve an IoU of
0.77,  the  active  method  required  40  samples,  whereas  the  random
method required 100 samples. Additionally, when the same number of
additional samples were added, the accuracy of the active method was
significantly higher than that of the random method (Fig. 4, Fig. S2–S5,
Table S5). These findings, consistent with those of Alajlan et al. (2013),
validated that active learning was an effective approach to minimizing
the number of samples needed for domain adaptation while maintaining
high recognition capability. Similarly, in the mapping of poplar plan-
tations  in  France,  active  learning  improved  overall  accuracy  by  5  %
compared to random sampling, requiring only 50 % of the samples to
achieve similar performance (Hamrouni et al., 2021).

Accurate sample labeling is crucial for large-scale forest disturbance
mapping,  but  it  also  presents  a  significant  challenge  due  to  the  com-
plexities of labeling diverse and extensive areas. This  study manually
annotated  disturbance  masks  using  high-resolution  Planet  imagery,
ensuring  accurate  labeling  of  subtle  disturbances.  However,  this  may
introduce potential biases, as this process was susceptible to subjectivity
and  errors,  which  can  lead  to  label  noise  (Peng  et  al.,  2024).  Never-
theless, most studies on remote sensing-based forest change monitoring
assumed that manually annotated data accurately represented the un-
derlying reality and were considered a widely accepted method in the
field  (Curtis  et  al.,  2018;  Senf  and  Seidl,  2021;  Slagter  et  al.,  2023).
However, Planet imagery was costly, and its availability may be limited
in remote or low-demand areas, hindering large-scale training. Fortu-
nately, Planet has an official research program that allows researchers to
apply for free access to their data for scientific purposes (https://www.
planet.com/industries/education-and-research/). In addition, Norway’s
NICFI initiative provided free access to Planet’s high-resolution data for
the N30
tropical region, with updated ranging from biannual to
monthly,  enhancing  the  feasibility  of  tropical  forest  monitoring
(Dalagnol et al., 2023). Furthermore, the reference data for validation
can be substituted with other high-resolution imagery, such as World-
view or Google Earth images. Moreover, this further explained the ne-
cessity  of  our  transfer  and  active  learning  to  reduce  our  reliance  on
planet data and hand-annotated. Despite this, data availability and cost
issues  may  persist  for  other  regions  in  future  studies.  To  address  this
issue,  for  future  study,  we  will  further  strengthen  the  generality  and
transferability  of  the  model,  reduce  the  dependence  on  labels  by
exploring  semi-supervised  or  unsupervised  pre-training  methods.
Moreover, while spatial dimension plays a crucial role in forest distur-
bance detection (Hussain et al., 2013; Zhao et al., 2022), temporal in-
formation should not be overlooked, the fusion of spatial and temporal
information  could  further  improve  detection  accuracy.  In  future
research, we will explore the 3D deep learning to effectively integrate
both  spatial  and  temporal  dimensions  for  enhanced  detection
performance.

◦
~ S30

◦

The  monthly  forest  disturbance  mapping  framework  based  on  the
SAMSR offers promising practical applications, particularly in tropical
regions  with  frequent  cloud  cover  that  limits  optical  data.  Although
there have been successful applications of Sentinel-1 for forest distur-
bance  detection  (Hethcoat  et  al.,  2021;  Reiche  et  al.,  2018),  these
methods often lack testing for cross-regional transferability and the use
of  advanced  techniques  to  further  improve  efficiency,  which  signifi-
cantly limits the scalability of the models for large-scale applications. In
contrast,  SAMSR  demonstrated  significant  advantages  by  addressing
these  gaps,  incorporating  both  transfer  learning  and  active  learning
techniques to enhance model efficiency and robustness across diverse

areas.  Overall,  this  study  provides  strong  technical  support  for  large-
scale, across-areas forest disturbance mapping, offering significant sci-
entific and practical value.

6. Conclusion

This study proposed and evaluated the SAMSR framework for map-
ping  large-scale  forest  disturbance  using  Sentinel-1  images  and  an
adapted  SAM  model.  The  proposed  SAMSR  demonstrated  robust  per-
formances in four pan-tropical areas (IoU 0.50–0.78; F1 0.67–0.88). We
further  determined  the  optimal  transfer  strategies  across-areas,  and
explored the potential of active learning to improve model efficiency.
We  found  the  combined  model  with  multi-region  achieved  the  best
transfer  performance  and  active  learning  further  improved  efficiency
with about 20 %–70 % less training samples to reach saturation accu-
racy. This novel framework enables accurate and timely forest distur-
bance  mapping  at  large-scales  and  supports  forest  management  and
protection  by  providing  detailed  insights  into  long-term  forest
dynamics.

CRediT authorship contribution statement

Yuping  Tian:  Writing  –  original  draft,  Visualization,  Validation,
Software,  Methodology,  Formal  analysis,  Data  curation.  Feng  Zhao:
Writing – review & editing, Supervision, Conceptualization. Ran Meng:
Writing – review & editing, Conceptualization. Rui Sun: Writing – re-
view  &  editing,  Software,  Data  curation.  Yuan  Zhang:  Software,
Investigation, Data curation. Yanyan Shen: Writing – review & editing,
Software.  Bin  Wang:  Writing  –  review  &  editing.  Jie  Liu:  Writing  –
review  &  editing.  Mingze  Li:  Writing  –  review  &  editing,  Project
administration, Conceptualization.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgements

for

This work was supported by National Natural Science Foundation of
China (No. 42371395), National Key Research  and Development Pro-
gram  of  China  (No.  2023YFD2201704),  the  Fundamental  Research
Funds
(No.  2572024BR33,  No.
2572024AW01);  Dr.  Ran  Meng  was  supported  by  National  Natural
Science Foundation of China (No. 42471362) and the Key Research and
Development Program of Heilongjiang, China (grant No. 2022ZX01A25;
No. JD2023GJ01).

the  Central  Universities

Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.

org/10.1016/j.rse.2025.114775.

Data availability

Data will be made available on request.

References

Ahmed, S.F., Alam, M.S.B., Hassan, M., Rozbu, M.R., Ishtiak, T., Rafa, N., Mofijur, M.,
Shawkat Ali, A., Gandomi, A.H., 2023. Deep learning modelling techniques: current
progress, applications, advantages, and challenges. Artif. Intell. Rev. 56,
13521–13617.

Alajlan, N., Pasolli, E., Melgani, F., Franzoso, A., 2013. Large-scale image classification

using active learning. IEEE Geosci. Remote Sens. Lett. 11, 259–263.

13

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Alshehri, M., Ouadou, A., Scott, G.J., 2024. Deep Transformer-Based Network

Deforestation Detection in the Brazilian Amazon Using Sentinel-2 Imagery. IEEE
Geosci. Remote Sens. Lett. 21.

Altarez, Armando Apan, Maraseni, T., 2023. Deep learning U-Net classification of
Sentinel-1 and 2 fusions effectively demarcates tropical montane forest’s
deforestation. Remote Sens. Appl. Soc. Environ. 29, 100887.

Ball`ere, M., Bouvet, A., Mermoz, S., Le Toan, T., Koleck, T., Bedeau, C., Andr´e, M.,

Forestier, E., Frison, P.L., Lardeux, C., 2021. SAR data for tropical forest disturbance
alerts in French Guiana: Benefit over optical imagery. Remote Sens. Environ. 252,
112159.

Brockerhoff, Luc Barbaro, Castagneyrol, Bastien, Forrester, David I., Gardiner, Barry,

Gonz´alez-Olabarria, Jos´e Ram´on, Lyver, Phil O’.B., Meurisse, Nicolas,
Oxbrough, Anne, Taki, Hisatomo, Thompson, Ian D., Jactel, F.V.D.P.H., 2017. Forest
biodiversity, ecosystem functioning and the provision of ecosystem services.
Biodivers. Conserv. 26, 3005–3035.

Bullock, E.L., Healey, S.P., Yang, Z., Houborg, R., Gorelick, N., Tang, X., Andrianirina, C.,

2022. Timeliness in forest change monitoring: A new assessment framework
demonstrated using Sentinel-1 and a continuous change detection algorithm.
Remote Sens. Environ. 276, 113043.

Cao, X., Yao, J., Xu, Z., Meng, D., 2020. Hyperspectral image classification with

convolutional neural network and active learning. IEEE Trans. Geosci. Remote Sens.
58, 4604–4616.

Chen, L.C., Zhu, Y., Papandreou, G., Schroff, F., Adam, H., 2018. Encoder-decoder with
atrous separable convolution for semantic image segmentation. In: Proc. European
Conference on Computer Vision, pp. 801–818.

Chen, N., Tsendbazar, N.E., Hamunyela, E., Verbesselt, J., Herold, M., 2021. Sub-annual
tropical forest disturbance monitoring using harmonized Landsat and Sentinel-2
data. Int. J. Appl. Earth Obs. Geoinf. 102, 102386.

Cortez, D., Soto, J., Rom´an-Figueroa, C., Paneque, M., 2024. Monitoring loss and

Kattenborn, T., Leitloff, J., Schiefer, F., Hinz, S., 2021. Review on Convolutional Neural
Networks (CNN) in vegetation remote sensing. ISPRS J. Photogramm. Remote Sens.
173, 24–49.

Kirillov, A., Mintun, Eric, Ravi, Nikhila, Mao, Hanzi, Rolland, Chloe, Gustafson, Laura,
Xiao, Tete, Whitehead, Spencer, Berg, Alexander C., Lo, Wan-Yen, Doll´ar, Piotr,
Girshick, R., 2023. Segment anything. In: Proc. IEEE/CVF International Conference
on Computer Vision, pp. 4015–4026.

Li, Y., Mao, H., Girshick, R., He, K., 2022a. Exploring plain vision transformer backbones
for object detection. In: European conference on computer vision, pp. 280–296.
Li, Y., Xu, X., Wu, Z., Fan, H., Tong, X., Liu, J., 2022b. A forest type-specific threshold
method for improving forest disturbance and agent attribution mapping. GISci.
Remote Sens. 59 (1), 1624–1642.

Li, J., Han, X., Qin, Y., Tan, F., Chen, Y., Wang, Z., Song, H., Zhou, X., Zhang, Y., Hu, L.,

Hu, P., 2023. Artificial intelligence accelerates multi-modal biomedical process: A
Survey. Neurocomputing 558, 126720.

Lin, X., Xiang, Yangyang, Zhang, Li, Yang, Xin, Zengqiang Yan, L.Y., 2023. SAMUS:
Adapting segment anything model for clinically-friendly and generalizable
ultrasound image segmentation. arXiv preprint arXiv: 2309.06824.

Liu, X., Wu, Y., Liang, W., Cao, Y., Li, M., 2022. High resolution SAR image classification
using global-local network structure based on vision transformer and CNN. IEEE
Geosci. Remote Sens, Lett, p. 19.

Liu, C., Sun, Y., Xu, Y., Sun, Z., Zhang, X., Lei, L., Kuang, G., 2024. A review of optical
and SAR image deep feature fusion in semantic segmentation. IEEE J. Sel. Top. Appl.
Earth Obs. Remote Sens. 17.

Ma, J., He, Y., Li, F., Han, L., You, C., Wang, B., 2024a. Segment anything in medical

images. Nat. Commun. 15 (1), 654.

Ma, Y.C., Chen, S., Ermon, S., Lobell, D.B., 2024b. Transfer learning in environmental

remote sensing. Remote Sens. Environ. 301, 113924.

Martins, V.S., Roy, D.P., Huang, H., Boschetti, L., Zhang, H., Yan, L., 2022. Deep learning

degradation of forests and shrubs in the North of Chile using Landsat time series data
sets from 1998 to 2018. Remote Sens. Appl. Soc. Environ. 35, 101244.

high resolution burned area mapping by transfer learning from Landsat-8 to
PlanetScope. Remote Sens. Environ. 280, 113203.

Crawford, M.M., Tuia, D., Yang, H.L., 2013. Active learning: Any value for classification

McGregor, I.R., Connette, G., Gray, J.M., 2024. A multi-source change detection

of remotely sensed data? In Proc. IEEE 101, 593–608.

Curtis, P.G., Slay, C.M., Harris, N.L., Tyukavina, A., Hansen, M.C., 2018. Classifying

drivers of global forest loss. Science 361, 1108–1111.

Dalagnol, R., Wagner, F.H., Galv˜ao, L.S., Braga, D., Osborn, F., Sagang, L.B., da

Conceiç˜ao Bispo, P., Payne, M., Junior, C.S., Favrichon, S., Silgueiro, V., Anderson, L.
O., Arag˜ao, L.E.O.C., Fensholt, R., Brandt, M., Ciais, P., Saatchi, S., 2023. Mapping
tropical forest degradation with deep learning and Planet NICFI data. Remote Sens.
Environ. 298, 113798.

De Bem, P.P., de Carvalho Junior, O.A., Guimaraes, R.F., Trancoso Gomes, R.A., 2020.
Change Detection of Deforestation in the Brazilian Amazon Using Landsat Data and
Convolutional Neural Networks. Remote Sens. 12 (6), 901.

Decuyper, M., Ch´avez, R.O., Lohbeck, M., Lastra, J.A., Tsendbazar, N., Hackl¨ander, J.,
Herold, M., Vågen, T.-G., 2022. Continuous monitoring of forest change dynamics
with satellite time series. Remote Sens. Environ. 269, 112829.

Ehrig, C., Cleophas, C., Forestier, G., 2024. The impact of data set similarity and diversity

on transfer learning success in time series forecasting. arXiv preprint arXiv:
2404.06198.

Ghamisi, P., Rasti, B., Yokoya, N., Wang, Q., Hofle, B., Bruzzone, L., Bovolo, F., Chi, M.
M., Anders, K., Gloaguen, R., Atkinson, P.M., Benediktsson, J.A., 2019. Multisource
and multitemporal data fusion in remote sensing: A comprehensive review of the
state of the art. IEEE Geosci. Remote Sens. Mag. 7 (1), 6–39.

Grecchi, R.C., Beuchle, R., Shimabukuro, Y.E., Arag˜ao, L.E., Arai, E., Simonetti, D.,

Achard, F., 2017. An integrated remote sensing and GIS approach for monitoring
areas affected by selective logging: A case study in northern Mato Grosso, Brazilian
Amazon. Int. J. Appl. Earth Obs. Geoinf. 61, 70–80.

Griffiths, P., Jakimow, B., Hostert, P., 2018. Reconstructing long term annual

deforestation dynamics in Para and Mato Grosso using the Landsat archive. Remote
Sens. Environ. 216, 497–513.

Guo, Z., Guo, H., Liu, X., Zhou, W., Wang, Y., Fan, Y., 2022. Sar2color: learning imaging
characteristics of sar images for sar-to-optical transformation. Remote Sens. 14 (15),
3740.

Hamrouni, Y., Paillassa, E., Ch´eret, V., Monteil, C., Sheeren, D., 2021. From local to
global: A transfer learning based approach for mapping poplar plantations at
national scale using Sentinel-2. ISPRS J. Photogramm. Remote Sens. 171, 76–100.
Hansen, M.C., Potapov, P.V., Moore, R., Hancher, M., Turubanova, S.A., Tyukavina, A.,

Thau, D., Stehman, S.V., Goetz, S.J., Loveland, T.R., 2013. High-resolution global
maps of 21st-century forest cover change. Science 342, 850–853.

Hansen, M.C., Krylov, A., Tyukavina, A., Potapov, P.V., Turubanova, S., Zutta, B., Ifo, S.,
Margono, B., Stolle, F., Moore, R., 2016. Humid tropical forest disturbance alerts
using Landsat data. Environ. Res. Lett. 11 (3), 034008.

Hethcoat, M.G., Edwards, D.P., Carreiras, J.M., Bryant, R.G., Franca, F.M., Quegan, S.,
2019. A machine learning approach to map tropical selective logging. Remote Sens.
Environ. 221, 569–582.

Hethcoat, M.G., Carreiras, J.M.B., Edwards, D.P., Bryant, R.G., Quegan, S., 2021.

Detecting tropical selective logging with C-band SAR data may require a time series
approach. Remote Sens. Environ. 259, 112411.

Hussain, M., Chen, D., Cheng, A., Wei, H., Stanley, D., 2013. Change detection from
remotely sensed images: From pixel-based to object-based approaches. ISPRS J.
Photogramm. Remote Sens. 80, 91–106.

Jamali, A., Roy, S.K., Li, J., Ghamisi, P., 2023. TransU-Net + +: Rethinking attention
gated TransU-Net for deforestation mapping. Int. J. Appl. Earth Obs. Geoinf. 120,
103332.

algorithm supporting user customization and near real-time deforestation detections.
Remote Sens. Environ. 308, 114195.

Miura, S., Amacher, M., Hofer, T., San-Miguel-Ayanz, J., Thackway, R., 2015. Protective
functions and ecosystem services of global forests in the past quarter-century. For.
Ecol. Manag. 352, 35–46.

Mullissa, A., Reiche, J., Herold, M., 2023. Deep learning and automatic reference label
harvesting for Sentinel-1 SAR-based rapid tropical dry forest disturbance mapping.
Remote Sens. Environ. 298, 113799.

Ngo, B.H., Do-Tran, N.T., Nguyen, T.N., Jeon, H.G., Choi, T.J., 2024. Learning CNN on
ViT: A Hybrid Model to Explicitly Class-specific Boundaries for Domain Adaptation.
In: Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 28545–28554.

Pan, S.J., Yang, Q., 2009. A survey on transfer learning. IEEE Trans. Knowl. Data Eng. 22,

1345–1359.

Peng, L., Wei, T., Chen, X., Chen, X., Sun, R., Wan, L., Chen, J., Zhu, X., 2024. Human-
annotated label noise and their impact on ConvNets for remote sensing image scene
classification. IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 18.

Pickens, A.H., Hansen, M.C., Adusei, B., Potapov, P., 2020. Sentinel-2 Forest Loss Alert.

In: Global Land Analysis and Discovery (GLAD). University of Maryland.

Qiu, S., Zhu, Z., Olofsson, P., Woodcock, C.E., Jin, S., 2023. Evaluation of Landsat image

compositing algorithms. Remote Sens. Environ. 285, 113375.

Reiche, J., Hamunyela, E., Verbesselt, J., Hoekman, D., Herold, M., 2018. Improving

near-real time deforestation monitoring in tropical dry forests by combining dense
Sentinel-1 time series with Landsat and ALOS-2 PALSAR-2. Remote Sens. Environ.
204, 147–161.

Reiche, J., Mullissa, A., Slagter, B., Gou, Y., Tsendbazar, N.E., Braun, C., Vollrath, A.,
Weisse, M.J., Stolle, F., Pickens, A., Donchyts, G., Clinton, N., Gorelick, N.,
Herold, M., 2021. Forest disturbance alerts for the Congo Basin using Sentinel-1.
Environ. Res. Lett. 16 (2), 024005.

Reichstein, M., Camps-Valls, G., Stevens, B., Jung, M., Denzler, J., Carvalhais, N.,

Prabhat, F., 2019. Deep learning and process understanding for data-driven Earth
system science. Nature 566, 195–204.

Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., Chen, L.C., 2018. Mobilenetv2:

Inverted residuals and linear bottlenecks. In: Proc. IEEE conference on computer
vision and pattern recognition, pp. 4510–4520.

Senf, C., Seidl, R., 2021. Mapping the forest disturbance regimes of Europe. Nat. Sustain.

4 (1), 63–70.

Shannon, C.E., 1948. A mathematical theory of communication. Bell Syst. Tech. J. 27,

379–423.

Singh, P., Shree, R., 2016. Analysis and effects of speckle noise in SAR images. In: 2016
2nd International Conference on Advances in Computing, Communication, &
Automation (ICACCA)(Fall). IEEE, pp. 1–5.

Slagter, B., Reiche, J., Marcos, D., Mullissa, A., Lossou, E., Pe˜na-Claros, M., Herold, M.,
2023. Monitoring direct drivers of small-scale tropical forest disturbance in near
real-time with Sentinel-1 and-2 data. Remote Sens. Environ. 295, 113655.

Solorzano, J.V., Francois Mas, J., Alberto Gallardo-Cruz, J., Gao, Y., Fernandez-Montes
de Oca, A., 2023. Deforestation detection using a spatio-temporal deep learning
approach with synthetic aperture radar and multispectral images. ISPRS J.
Photogramm. Remote Sens. 199, 87–101.

Song, Hui Yang, Yanlan, Wu, Zhang, Peng, Wang, Biao, Han, G., 2024. A multispectral
remote sensing crop segmentation method based on Segment Anything Model using
Multi-stage Adaptation Fine-tuning. IEEE Trans. Geosci. Remote Sens. 62.

Tang, Q., Liang, J., Zhu, F., 2023a. A comparative review on multi-modal sensors fusion

based on deep learning. Signal Process. 109165.

14

Y. Tian et al.

Remote Sensing of Environment 325 (2025) 114775

Tang, X.J., Bratley, K.H., Cho, K.J., Bullock, E.L., Olofsson, P., Woodcock, C.E., 2023b.
Near real-time monitoring of tropical forest disturbance by fusion of Landsat,
Sentinel-2, and Sentinel-1 data. Remote Sens. Environ. 294, 113626.

Wang, S., Li, C., Wang, R., Liu, Z., Wang, M., Tan, H., Wu, Y., Liu, X., Sun, H., Yang, R.,

2021b. Annotation-efficient deep learning for automatic medical image
segmentation. Nat. Commun. 12, 5915.

Tsokas, A., Rysz, M., Pardalos, P.M., Dipple, K., 2022. SAR data applications in earth

Weiss, K., Khoshgoftaar, T.M., Wang, D., 2016. A survey of transfer learning. J. Big Data

observation: An overview. Expert Syst. Appl. 205, 117342.

Tu, Z., Gu, L., Wang, X., Jiang, B., 2024. Ultrasound SAM Adapter: Adapting SAM for
Breast Lesion Segmentation in Ultrasound Images. arXiv preprint arXiv: 2404.14837.

Tuia, D., Volpi, M., Copa, L., Kanevski, M., Munoz-Mari, J., 2011. A survey of active

learning algorithms for supervised remote sensing image classification. IEEE J. Sel.
Top. Signal Process. 5, 606–617.

Van der Maaten, L., Hinton, G., 2008. Visualizing data using t-SNE. J. Mach. Learn. Res.

9, 2579–2605.

Vega, Juan, P., Ostwald Pedro da Costa, G.A., Feitosa, R.Q., Ortega Adarme, M.X., de
Almeida, C.A., Heipke, C., Rottensteiner, F., 2021. An unsupervised domain
adaptation approach for change detection and its application to deforestation
mapping in tropical biomes. ISPRS J. Photogramm. Remote Sens. 181, 113–128.
Wan, L., Liu, Y.F., He, Y., Cen, H.Y., 2023. Prior knowledge and active learning enable
hybrid method for estimating leaf chlorophyll content from multi-scale canopy
reflectance. Comput. Electron. Agric. 214, 108308.

Wang, Y.X., Ziv, G., Adami, M., Mitchard, E., Batterman, S.A., Buermann, W.,

Marimon, B.S., Marimon Jr., B., Reis, S.M., Rodrigues, D., Galbraith, D., 2019.
Mapping tropical disturbed forests using multi-decadal 30 m optical satellite
imagery. Remote Sens. Environ. 221, 474–488.

Wang, J., Yang, D., Chen, S., Zhu, X., Wu, S., Bogonovich, M., Guo, Z., Zhu, Z., Wu, J.,

2021a. Automatic cloud and cloud shadow detection in tropical areas for
PlanetScope satellite images. Remote Sens. Environ. 264, 112604.

3, 1–40.

Wu, D.R., Lin, C.T., Huang, J., 2019. Active learning for regression using greedy

sampling. Inf. Sci. 474, 90–105.

Yan, Z.Y., Li, J.X., Li, X.X., Zhou, R.X., Zhang, W.K., Feng, Y.C., Diao, W.H., Fu, K.,
Sun, X., 2023. RingMo-SAM: A Foundation Model for Segment Anything in
Multimodal Remote-Sensing Images. IEEE Trans. Geosci. Remote Sens. 61.
Zhang, J., Yang, X., Jiang, R., Shao, W., Zhang, L., 2024. RSAM-Seg: A SAM-based

Approach with Prior Knowledge Integration for Remote Sensing Image Semantic
Segmentation. arXiv preprint arXiv: 2402.19004.

Zhao, F., Sun, R., Zhong, L., Meng, R., Huang, C., Zeng, X., Wang, M., Li, Y., Wang, Z.,
2022. Monthly mapping of forest harvesting using dense time series Sentinel-1 SAR
imagery and deep learning. Remote Sens. Environ. 269, 112822.

Zhou, J., Chen, J., Chen, X., Zhu, X., Qiu, Y., Song, H., Rao, Y., Zhang, C., Cao, X., Cui, X.,
2021. Sensitivity of six typical spatiotemporal fusion methods to different influential
factors: A comparative study for a normalized difference vegetation index time series
reconstruction. Remote Sens. Environ. 252, 112130.

Zhou, X.C., Liang, F., Chen, L.H., Liu, H.J., Song, Q.Q., Vivone, G., Chanussot, J., 2024.
MeSAM: Multiscale Enhanced Segment Anything Model for Optical Remote Sensing
Images. IEEE Trans. Geosci, Remote Sens, p. 62.

Zhu, L.J., Dai, J.J., Liu, Y., Yuan, S.S., Qin, T.L., Walker, J.P., 2024. A cross-resolution
transfer learning approach for soil moisture retrieval from Sentinel-1 using limited
training samples. Remote Sens. Environ. 301, 113944.

Zhuang, F., Qi, Z., Duan, K., Xi, D., Zhu, Y., Zhu, H., Xiong, H., He, Q., 2020.
A comprehensive survey on transfer learning. In Proc. IEEE 109, 43–76.

15

