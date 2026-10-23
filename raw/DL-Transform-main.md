Information Processing in Agriculture xxx (xxxx) xxx

Contents lists available at ScienceDirect

Information Processing in Agriculture

journal homepage: www.keaipublishing.com/en/journals/information-processing-in-agriculture/

LGCA-Net: A time-series anomaly detection method for multiple types of
agricultural sensors

, Laixi Zhang b, Jianbo Guo b, Yuan Huang c, Ping Lin d, Wengang Zheng e,

Zongren Wang a
Lili Zhangzhong a,*
a Information Technology Research Centre, Beijing Academy of Agriculture and Forestry Sciences, Beijing 100097, China
b Beijing Changyang Farm Co., Ltd., Beijing 100097, China
c Shijiazhuang Academy of Agriculture and Forestry Sciences, Shijiazhuang 050041, China
d Xinjiang Tianye Co., Ltd., Xinjiang 832000, China
e Intelligent Equipment Research Center, Beijing Academy of Agriculture and Forestry Sciences, Beijing 100097, China

A R T I C L E  I N F O

A B S T R A C T

Keywords:
MCNN
Transformer
Anomaly detection
Feature fusion
Cross-attention
Agricultural sensors

Agricultural sensors play a crucial role in guiding agricultural production. However, the quality of data collected
by these sensors is often compromised by the complex environmental conditions of farmlands and the diversity of
crop  management  practices.  Particularly  in  precision  agriculture,  even  minor  anomalies  in  data  can  lead  to
significant deviations in critical decisions, such as estimation of crop water demand, fertilization scheduling, and
pest  or  disease  management  strategies,  thereby  resulting  in  substantial  losses.  To  address  this  challenge,  this
study introduces a universal time-series anomaly detection method for multi-type agricultural sensors employing
the  fusion  of  global  and  local  features,  termed  LGCA-Net.  To  capture  the  short-term  change  rule  of  data,  a
multiscale convolutional neural network (MCNN) is employed to extract detailed local information. For iden-
tifying the long-term change rule of data, a transformer neural network is employed to capture the global cor-
relation  within  the  data.  Finally,  the  fusion  of  global  and  local  information  is  achieved  via  a  cross-attention
mechanism,  which enhances  the anomaly recognition ability  of the  model under  different agricultural sensor
data. To evaluate the effectiveness of the proposed model, experiments were conducted using two agricultural
scenario datasets from greenhouses and fields. The results demonstrate that the proposed method achieves F1-
scores  of  0.9580  (field)  and  0.9721  (greenhouse),  which  comprehensively  measures  precision  and  recall.
Compared with the single-structure model, the Accuracy (ACC) of abnormal sample recognition increased by an
average of 6.65% (field) and 6.67% (greenhouse). In summary, the proposed LGCA-Net model adapts to the dual
characteristics  of  short-term  fluctuations and  long-term  cycles in  agricultural  time  series through  the  parallel
fusion of global and local features. It overcomes the limitations of single-structure models in feature capture and
provides a reliable anomaly detection solution for multi-type of agricultural sensors.

1. Introduction

Agricultural  sensors  constitute  an  important  component  of  intelli-
gent  agriculture  and  perform  critical  functions  during  the  digital
transformation  of  agriculture,  including  crop  growth  monitoring,  soil
moisture  measurement,  and  meteorological  environment  observation
[1]. Data collected from these sensors provide a scientific foundation for
downstream  processes  such  as  irrigation  and  fertilization  scheduling,
pest and disease early warning systems, and yield prediction. However,
under  real  agricultural  conditions,  sensors  are  highly  susceptible  to

multiple  external  influences,  such  as  strong  winds,  heavy  rainfall,
farming,  and  sensor  aging,  which  introduce  noise  and  outliers  in  the
collected  data.  These  abnormal  data  directly degrade  the  accuracy of
subsequent  analysis,  modeling,  and  decision-making,  thereby  signifi-
cantly restricting the applicability and operational efficiency of intelli-
gent agriculture.

Common agricultural monitoring indicators include air temperature,
relative humidity, and soil moisture content. In agricultural production
systems,  these  indicators  are  not  independent  but  are  simultaneously
influenced by climate change (seasonal temperature difference, extreme

* Corresponding author.

E-mail addresses: 1308636759@qq.com (Z. Wang), zhangzll@nercita.org.cn (L. Zhangzhong).

https://doi.org/10.1016/j.inpa.2026.01.008
Received 1 September 2025; Received in revised form 7 January 2026; Accepted 11 January 2026
Available online 13 January 2026
2214-3173/© 2026 The Author(s).  Published by Elsevier B.V. on behalf of China Agricultural University.  This is an open access article under the CC BY-NC-ND
license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ).

Please cite this article as: Zongren Wang et al., Information Processing in Agriculture, https://doi.org/10.1016/j.inpa.2026.01.008

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

weather, rainfall spatial and temporal distribution), crop growth stage
(sowing, seedling stage, jointing, grouting, and maturity), agricultural
management measures (irrigation, fertilization, farming, and pest con-
trol), and other multiple effects. These factors produce highly complex
nonlinear  relationships.  In  addition,  agricultural  monitoring  differs
substantially  from  industrial  settings  and  exhibit  strong  nonstandard
characteristics, such as diverse sensor layout conditions, uncontrollable
environmental  disturbances,  difficulty  in  maintaining  long-term  con-
sistency  of  measurement  accuracy,  and  limited  comparability  across
different fields.

In the context of multifactor interweaving and pronounced dynamic
changes,  conventional  anomaly  detection  methods,  such  as  the
threshold  method  [2,3] and  moving  average  method  [4],  exhibit
inherent  limitations  in  agricultural  applications.  Threshold-based
methods significantly depend on expert-defined judgment criteria [5],
which limits adaptability across regions, crops, and highly variable cli-
matic  conditions.  Although  moving  average  methods  have  achieved
satisfactory  performance  in  specific  settings,  they  result  in  loss  of
detailed information and reduced recognition accuracy in complex en-
vironments [6]. Furthermore, agricultural production is influenced by
multiple factors, including seasonal changes, climate fluctuations, and
crop growth cycles, resulting in dynamic changes in water usage pat-
terns and data characteristics [7]. Once established, traditional anomaly
detection models exhibit limited parameter flexibility and weak adapt-
ability to newly emerging data patterns. This significantly restricts the
intelligent  and  refined  development  of  agricultural  water  resource
management.

With the continuous development of artificial intelligence technol-
ogy, machine learning methods have attracted increasing attention in
anomaly detection owing to their powerful feature-learning and pattern-
recognition  capabilities.  In  2021,  Zamry  et  al.  [8] proposed  a  light-
weight  anomaly  detection  scheme  combining  incremental  principal
component analysis (CCIPCA) and a one-class support vector machine
(OCSVM).  The  experimental  results  show  that  this  scheme  achieves
excellent  performance  in  detection  accuracy,  memory  efficiency,
computational  complexity,  and  communication  overhead.  In  2023,
Utkin et al. [9] proposed an attention-based isolation forest (ABIForest)
for  anomaly  detection.  This  method  enhances  the  anomaly  detection
performance by incorporating the Nadaraya–Watson attention mecha-
nism.  The  experimental  results  demonstrated  that  the  ABIForest  out-
performed the traditional isolation forest (iForest) on multiple synthetic
and real-world datasets. In 2024, Chua et al. [10] explored the use of an
isolation forest algorithm for detecting network traffic anomalies. Their
study indicated that isolation forest exhibited outstanding performance
in detecting network traffic anomalies, with an accuracy rate exceeding
90%. Zhang et al. [11] proposed a method for electric vehicle battery
fault prediction and diagnosis based on an improved gradient boosting
decision tree (GBDT)–iForest)–boxplot. By jointly considering the bat-
tery  characteristics  and  driving  behaviors,  accurate  and  effective
anomaly detection was achieved. In 2025, Verma et al. [12] proposed an
anomaly  detection  method  combining  optimal  partitioning  (OP)  and
extreme learning machine (ELM), demonstrating strong performance on
highly  imbalanced  datasets.  Despite  significant  progress  in  machine
learning-based  methods  for  anomaly  detection,  their  applications  re-
mains  predominantly  concentrated  in  industrial  sectors,  and  their
implementation  in  agriculture  continues  to  encounter  considerable
challenges.  Industrial  environments  are  relatively  stable  and  highly
controllable,  with  relatively  uniform  fault  patterns.  Therefore,  tradi-
tional  machine  learning  algorithms  based  on  specific  assumptions  on
data distribution and features often demonstrate optimal performance.
However, data from agricultural environments are highly susceptible to
factors such as weather conditions and crop growth stages, exhibiting a
range  of  normal  fluctuations  and  frequent  “normal  yet  extreme”  pat-
terns.  When  real-world  data  deviate  from  predefined  algorithmic  as-
sumptions, traditional machine learning models struggle to accurately
capture  the  distribution  patterns  of  the  data,  leading  to  a  significant

decline in their detection performance.

Deep learning, as a branch of machine learning, can automatically
learn complex patterns and feature representations from massive data-
sets leveraging multilayer neural networks [13]. Owing to its superior
feature-learning capability compared with traditional machine learning,
it has emerged as a major research focus in anomaly detection. Deep
learning-based  anomaly  detection  methods  are  primarily  categorized
into two types. The first is the method of reconstruction by learning the
patterns of normal data. These include reconstruction models based on
autoencoders such as deep autoencoder [14], long short-term memory
(LSTM)-capsule  autoencoder  [15],  autoencoder  based  on  neural
network  [16],  multi-channel  multi-scale  convolution  attention  varia-
tional  autoencoder  (MCA-VAE)  [17],  and  variational  autoencoders
based on association discrepancy [18], as well as generative adversarial
networks (GAN) such as transformer-based GAN for anomaly detection
of time series data (TGAN-AD) [19], LSTM-Based VAE-GAN [20], and
federated  time  series  anomaly  detection  method  based  on  the  Sobo-
lev–Wasserstein GAN (FedSw-TSAD) [21]. Autoencoder-based methods
identify anomalies by evaluating the degree of reconstruction, whereas
GAN-based  methods  rely  on  discriminator  outputs  for  anomaly  judg-
ment. The second category emphasizes real-time anomaly discrimina-
tion  of  future  data  based  on  the  change  patterns  of  historical  data,
among which LSTM is a commonly used model owing to its structural
suitability  for  time-series  feature  extraction.  Numerous  studies  have
demonstrated  the  effectiveness  of  LSTM-based  models  in  time-series
anomaly  detection,  including  Gopali  [22],  Noh  [23],  Lee  [24],  and
Gomolka [25]. Additionally, some models based on convolutional neu-
ral  network  (CNN),  transformers,  and  their  fusion  variants  have
demonstrated excellent performance in time-series anomaly detection.
Examples include LSTM-CNN [26], CNN-LSTM fused with ARMA [27],
and TCF-Trans [28].

Although  deep  learning  methods  eliminate  the  need  for  manual
feature  design,  they  can  automatically  capture  the  complex  latent
structures  of  data  and  have  demonstrated  robust  performance  across
diverse domains. Agricultural data are closely linked to climate change
and crop growth, resulting in strong temporal characteristics. However,
anomaly detection methods based on data reconstruction often fail to
fully capture the inductive bias of adjacent points at each time point in
time-series data. This inductive bias indicates that, for each time point in
a time series, its immediate neighbors are more relevant or influential
than distant points [29]. For instance, traditional autoencoders may lose
the local correlation information of adjacent points owing to compres-
sion  of  the  encoding  dimension,  making  it  challenging  to  capture
detailed features. In addition, agricultural production requires real-time
and  dynamic  monitoring.  Reconstruction-based  methods  require  the
calculation of the entire sequence for each detection, consume a large
amount of resources, and make real-time detection challenging.

Therefore, this study focuses on an anomaly-detection method based
on  real-time  discrimination.  This  method  can  effectively  extract  the
contextual  information  of  time-series  data  while  emphasizing  the  in-
fluence  of  neighboring  points,  thereby  rendering  it  more  suitable  for
real-time  anomaly  detection  of  time-series  data.  However,  different
models exhibit varying feature-capturing capabilities. The agricultural
data  exhibits  significant  differences  in  their  variation  patterns  across
different timescales. On a short-term scale, sudden temperature fluctu-
ations, unexpected rainfall, and irrigation can lead to rapid changes in
data such as soil moisture. Substantial differences exist in the scales of
the  fluctuations,  and  the  features  interact with  each  other  within  the
feature  space.  Over  long  time  scales,  agricultural  data  follow  pro-
nounced seasonal and periodic patterns and are also influenced by long-
term  factors  such  as  climate  change  and  adjustments  in  the  planting
structure.  Although  data  from  the  same  crop  growth  cycle  showed
similar trends, factors such as climate can cause an overall shift in long-
term data.

Most  existing  real-time  discriminative  anomaly-detection  methods
are based on a single model or serial fusion. A single model struggles to

2

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

adapt to the highly variable characteristics of agricultural environments.
Serial  fusion  method,  exemplified  by  the  CNN-LSTM  model,  perform
feature extraction sequentially, with the CNN output serving as the sole
input  to  LSTM.  The  learning  performance  of  LSTM  is  completely
dependent on the quality of feature extraction by the CNN. If the CNN
fails to capture key information, the subsequent learning of the LSTM
deteriorates, and LSTM cannot compensate for the shortcomings of the
previous module via self-adjustment.

To  address  these  limitations,  this  study  proposes  a  time-series
anomaly  detection  method  (LGCA-Net)  for  multiple  types  of  agricul-
tural sensors based on the parallel fusion of global and local features. It
primarily comprises the following three components:

(1)  To  address  the  short-term  variation  patterns  of  data,  a  local
feature extraction module based on a multi-scale convolutional neural
network  is  constructed.  This  module  utilizes  convolution  kernels  of
different sizes to mine local feature information from the data, enabling
the capture of minor fluctuations and instantaneous changes in the data.
(2)  To  address  the  long-term  variation  patterns  of  data,  a  global
feature extraction module based on Transformer is built. Through the
multi-head self-attention mechanism, this module calculates the atten-
tion  distribution  of  multiple  subspaces  in  parallel,  capturing  global
correlations  of  the  data  from  multiple  perspectives.  This  allows  the
module to identify significant differences in long-term changes, such as
those caused by different seasons, climates, and crop growth cycles.

(3)  A  global  and  local  feature  fusion  module  based  on  the  cross-
attention  mechanism  is  constructed.  The  cross-attention  mechanism
establishes connections between different features, which facilitates the
exchange  and  integration  of  information,  forming  a  complete  feature
extraction system that spans from local to global, thereby enhancing the
model's representational capacity for complex data.

In  Section  2,  we  present  information  pertaining  to  the  algorithm,
including a general flow chart and the theory behind each component. In
Section  3,  we  present  the  experimental  data  and  model  parameter
configurations and verify our method’s effectiveness through compar-
ative  experiments.  In  Section  4,  we  conclude  this  paper,  analyze  the
limitations  of  the  current  study  and  provide  an  outlook  on  future  di-
rections of research.

2. Methodology

In this section, the overall algorithm workflow proposed in this study
is briefly described. We then elaborate on the algorithmic principles of
the  three  modules:  multiscale  local  feature  extraction,  global  feature

extraction, and cross-attention mechanism-based feature fusion. Finally,
the anomaly determination criteria and evaluation metrics employed in
this study are introduced.

The algorithm proposed in this study is illustrated in Fig. 1. In the
multiscale  local  feature  extraction  stage,  three  convolutional  residual
blocks  of  different  scales  are  adopted  for  feature  extraction.  The
extracted multiscale features are concatenated to form a multiscale local
feature map, thereby providing fine-grained feature support for subse-
quent anomaly identification. The encoder structure of the Transformer
was employed in the global feature extraction stage. Using the multi-
head attention mechanism, the attention distribution of multiple sub-
spaces is calculated in parallel, and the dependency relationships across
different time spans are captured. This enables the construction of global
features covering a long time series, preventing misjudgment caused by
local  fluctuations  and  the  consequent  neglect  of  abnormal  overall
trends.  In  the  cross-attention-based  feature-fusion  stage,  the  self-
attention  mechanism  is  first  applied  to  the  global  and  local  feature
maps  to  obtain  their  respective  query  (Q),  key  (K),  and  value  (V)
matrices. Subsequently, the Q matrix of the global features is used to
query the K and V matrices of the local features, whereas the Q matrix of
the local features is used to query the K and V matrices of the global
features.  This  process  enables  information  interaction  between  the
global and local features, thereby enhancing the ability of the model to
learn from complex data. Finally, the interacting features are fused and
input  into  the  fully  connected  layer  to  generate  the  final  anomaly
detection  result.  This  workflow  can  specifically  capture  data  charac-
teristics  in  anomaly  detection  for  typical  agricultural  monitoring  in-
dicators  (such  as  soil  moisture  content,  temperature,  and  humidity),
thereby improving identification accuracy.

2.1. Multi-scale local feature extraction

The  local  feature  extraction  module  employed  a  one-dimensional
(1D)  CNN.  The  1D-CNN  shares  similar  principles  with  the  two-
dimensional  (2D)  CNN,  with  the  primary  distinction  that  the  input
data comprises one-dimensional time-series data. Convolution kernels
slide over the input sequence to compute the convolution results at each
position, forming a new feature map wherein each element represents
the feature of a local region in the input sequence [30].

However, in agricultural applications, temporal data patterns often
exhibit  the  characteristics  of  coexisting  multiscale  features,  such  as
short-term  precipitation  fluctuations  and  medium-term  changes  in
growth  status.  Conventional  1D-CNNs  employ  a  single  convolution

Fig. 1. Overall algorithm flowchart of LGCA-Net for agricultural sensor time-series anomaly detection.

3

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

kernel with a fixed receptive field, which makes it challenging to capture
information at different time granularities.

Therefore, this study employed a multiscale convolutional structure.
By integrating multi-scale techniques with a 1D-CNN, it leverages the
high-efficiency of CNN in extracting local features and also incorporates
multilevel patterns in agricultural data via multi-scale design. Examples
of these patterns are sudden changes in daily temperature and humidity
and the stability of the growth environment within a week. The specific
structures are shown in Fig. 2.

where  kernel  sizes  1–3  correspond  to  convolution  kernels  with
different scales (covering short, medium, and long time spans, respec-
tively). By sliding these multi-scale convolution kernels along the tem-
poral  dimension  of  the  agricultural  sensor  time-series  data,  local
features  corresponding  to  different  time  spans  in  the  sequence  are
extracted, which provides diverse fine-grained feature representations
for subsequent global feature fusion.

In addition, to mitigate  the potential loss of temporal  information
caused by deep-layer convolutions, this study constructed convolutional
residual blocks to replace single-layer convolutions. In the convolutional
residual block, the original input information can be transmitted to the
subsequent layers without loss through skip connections. This feature is
crucial in the context of agricultural time-series data. Sudden short-term
meteorological changes (such as heavy rains) may exert long-term in-
fluences on crop growth. The residual block ensures that key informa-
tion  is  not  excessively  smoothed  by  the  convolution  operation.  The
specific structures are shown in Fig. 3.

In this study, two skip connection methods are employed. When the
input  and  output  dimensions  are  identical,  residual  block  (a)  uses
identity  mapping  to  realize  the  skip  connection,  which  prevents  un-
necessary computation and ensures the integrity of the original features.
When the input and output dimensions are differ, the residual block (b)
performs a dimension alignment through a 1 × 1 1D convolutional layer
to align the feature dimensions from the residual mapping path, thereby
ensuring the feasibility of element-wise addition. In Fig. 3, N represents
the  number  of  output  channels  in  the  convolutional  layer,  which
determine the number of output feature maps in the convolutional layer.
Each channel can capture different types of feature information from the
input data. K denotes the size of the convolutional kernel, which can
control  the  temporal  size  of  the  receptive  field  of  the  convolution
operation, thereby enabling the capture of local feature information at
different scales. The BN is a batch normalization layer that can effec-
tively alleviate the “internal covariate shift” and prevent gradient van-
ishing during later stages of training.

2.2. Global feature extraction

In  the  global  feature  extraction  module,  this  study  adopts  the

Fig. 2. Multi-scale local feature extraction diagram of MCNN.

4

encoder  part  of  the  Transformer.  Its  structure  comprises  positional
encoding,  a  multi-head  self-attention  mechanism,  and  a  feedforward
neural  network.  The  self-attention mechanism  can directly  model  the
dependency relationships between any positions in a sequence. Unlike
the RNN/LSTM, it does not need to transmit information point-by-point
[31],  making  it  particularly  suitable  for  capturing  global  patterns  in
agricultural data. For example, it can simultaneously focus on the long-
term  correlation  between  “high  temperature  in  summer”  and  “low
temperature in winter,” while traditional time-series models struggle to
learn such long-distance dependencies owing to the vanishing gradient
problem. The formula is as follows:

Attention (Q, K, V) = softmax

QKT
√
̅̅̅̅̅̅
dK

× V

(

)

(1)

where  Q, K, and  V  denote  the  query,  key,  and  value  vectors,
respectively. Furthermore, softmax is the normalization function, dK  is
the dimension of the vector, and QKT  is the similarity score between Q
and  K.  The  self-attention  mechanism  enables  the  model  to  perform
weighted aggregation by calculating the relationships between the po-
sitions in the input  sequence. Each  self-attention head acquires  infor-
mation  from  different  positions  within  a  sequence.  Subsequently,  the
multi-head  attention  concatenates  the  output  matrices  and  passes
them  into  a  linear  layer  to  obtain  the  final  output  of  the  multi-head
attention:

headi = Attention

(cid:0)

QWQ
i

, KWK
i

, VWV
i

)

MultiHead (Q, K, V) = Concat ( head1, ⋯, headh)Wo

(2)

(3)

, KWK
i

, and VWV

where “Concat” represents the concatenation operation, headi  is the
i-th attention head, and h is the number of attention heads. Wo  denotes
the  matrix  weight  used  for  linear  transformation  of  the  concatenated
matrix. QWQ
i  are the linear transformation matrices of
i
the i-th attention head. After the aforementioned processing, the long-
range  dependencies  between  features  were  obtained.  Subsequently,
the  output  of  each  attention  layer  is  passed  through  a  feed-forward
neural  network.  The  feed-forward  neural  network  comprises  two
linear layers and a non-linear activation function called ReLU. For the
input  feature  vector  ht  at  the  t-th  time  step,  the  feedforward  neural
network is calculated as follows:

at = ReLU(htWFFN1 + bFFN1)

ot = atWFFN2 + bFFN2

(4)

(5)

where at  is the intermediate activation value; ot  is the final output.
Furthermore, WFFN1  and WFFN2  are learnable weight matrices, and bFFN1
and bFFN2  are bias vectors. Finally, the output of the global feature map
was  obtained  after  normalization,  residual  connections,  and  global
pooling.

2.3. Cross-Attention mechanism feature fusion

The  Cross-Attention  Mechanism  is  an  important  variant  of  the
attention mechanism. This is in contrast to self-attention, which focuses
only on dependency relationships within a single input sequence. Cross-
attention  addresses  this  limitation  by  enabling  information  exchange
between two different sequences (commonly referred to as the “query
sequence” and the “key-value sequence”). Its core idea is to allow one
input  sequence  to  “attend  to”  the  relevant  information  in  another
sequence,  thereby  achieving  effective  integration  across  information
sources. The specific process is illustrated in Fig. 4.

In Fig. 4, the query (Q) matrix is derived from the representation of
the target sequence (Feature map 2), where the key (K) and value (V) are
obtained from the representation of the source sequence (Feature map
1),  A  is  the  cross-attention  weight,  and  the  output  feature  map  Z  is
generated by multiplying A with V.

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 3. Two residual block structures diagram for MCNN multi-scale feature extraction: (a) identity-mapped residual block; (b) 1 × 1 convolution-mapped resid-
ual block.

Fig. 4. Cross-attention structural diagram.

To fully preserve the interaction information between the global and
local  features,  this  study  adopted  a  dual  cross-attention  mechanism.
Dual  cross-attention  enables  two-way  interaction  between  “global  →
local”  and  “local  →  global,”  resulting  in  the  following  two  core  new
capabilities:  the  “global  →  local”  interaction  calibrates  local  features
from a  global  perspective, preventing  misjudgment of data  mutations
caused by sudden environmental influences as anomalies (e.g., a rapid
increase in soil moisture content owing to rainfall); the “local → global”
interaction  supplements  global  features  with  local  details,  preventing

anomaly misjudgment resulting from the loss of key short-term signals
during global modeling (e.g., short-term frequent irrigation leading to
fluctuations in soil moisture content). After layer normalization and 1 ×
1 convolution for dimension alignment, the key-value (KV) matrices of
the global and local features can be dynamically adjusted according to
the data characteristics to achieve multiscale adaptation. The specific
formulae are as follows:

5

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

(

(1) = softmax
A

)

⊤
Qlocal K
global
̅̅̅̅̅
dk

√

(1) = A
Z

(1)

Vglobal

(

(2) = softmax
A

(2) = A
Z

(2)

Vlocal

)

⊤
local

Qglobal K
√
̅̅̅̅̅
dk

(6)

(7)

(8)

(9)

1.  Calculate the autocorrelation coefficients: For the given time series

data, compute ρk  for different lag orders k.

2. Identify the cutoff point: Find the lag order k at which the autocor-
relation coefficient first drops below a specific threshold (set to 0.5 in
this  study).  This  value  indicates  that  the  correlation  between  the
original data and its lagged versions is no longer significant.

3. Determine the window size: Set the window size to k + 1. This en-
sures  that  the  window  includes  all  historical  data  points  with  sig-
nificant correlation.

where dk  is the vector dimension and softmax is the normalization
function. In first-layer cross-attention, Q of the local feature sequence is
used as the query, and KV of the global features is used as the key value,
thereby  enabling  global  information  to  guide  the  local  features.  In
second-layer cross-attention, the Q of the global feature sequence is used
as the query, and the KV of the local features is used as the key value to
achieve the enhancement of global features by local information. The
resulting feature maps, denoted as Z
, correspond to the local
and global features, respectively, after cross attention. This “dual” cross-
attention  mechanism  fully  exploits  feature  interactions  at  different
scales,  incorporating  both  global  information  and  strengthening  local
details. Finally, the two interacting features are concatenated, fused, and
input  into  the  fully  connected  layer  to  complete  the  detection  and
identification of abnormal data.

and Z

(1)

(2)

2.4. Criteria for abnormality determination and evaluation indicators

Given  the  inductive  bias  discussed  earlier  that  the  immediate
neighboring points in a time series exert stronger influence than distant
points,  this study  employed a  sliding-window anomaly  determination
method. For each target point position, this method simultaneously in-
puts both the data within the previous window and the target data, and
then outputs in real time whether the detected data are abnormal. This
process is illustrated in Fig. 5.

To ensure full inclusion of the key reference information required for
anomaly judgment while excluding redundant data that may interfere
with  the  judgment  and  increase  computational  efficiency,  this  study
employed the autocorrelation analysis method to determine the window
length. This method quantifies the correlation between the data and its
lagged versions, reveals the inherent temporal structure of the data, and
ensures that the selected window size contains sufficient historical in-
formation  to  determine  the  anomaly  of  the  current  data  point.  The
specific formula is as follows:

∑

ρk

=

n
(xt (cid:0) x)(xt(cid:0) k (cid:0) x)
t=k+1
∑
xt (cid:0) x)2
n
t=1

(cid:0)

(10)

where ρk  represents the autocorrelation coefficient at a lag of k time
steps, n denotes the length of the time series, and x denotes the mean of
the time series. The steps to determine the window size based on the
autocorrelation analysis are as follows:

To  accurately  evaluate  the  anomaly  detection  performance  of  the
model  proposed  in  this  study,  we  consider  that  the  proportion  of
abnormal  samples  is  typically  extremely  low  in  practical  scenarios.
Consequently, the model tends to identify normal samples more readily.
However, the cases of missed detection of anomalies and misjudgment of
normal samples are precisely what we need to focus on, as these can
directly impact the practicality of the method. Therefore, in this paper,
evaluation metrics are selected based on the model's ability to recognize
abnormal samples and the misjudgment of normal samples. Samples are
classified into four categories according to the true labels and detection
results: true positive (TP), false negative (FN), false positive (FP), and
true negative (TN). Based on these four types of discrimination results,
we selected the following four evaluation metrics to construct a model
performance evaluation system:

1) Recall: Calculated as the ratio of the number of true positives to
the total number of abnormal samples. The recall directly reflects the
ability of a model to capture abnormal samples. A high recall rate in-
dicates significantly few cases of missed detection of anomalies, which is
a core requirement in anomaly detection tasks to ensure that potential
anomalies are not overlooked. The calculation formula is as follows:

Recall = TP

TP + FN

(11)

2)  Precision:  It  is  measured  as  the  proportion  of  the  number  of  true
positives in the total number of samples judged as abnormal. Precision
focuses  on  reducing  misjudgments  of  normal  samples.  The  level  of
precision  directly  reflects  the  model's  ability  to  distinguish  normal
fluctuations during the adaptive adjustment process, avoiding ineffec-
tive warnings caused by over-sensitivity. The calculation formula is as
follows:

Precision = TP

TP + FP

(12)

3) F1-Score: As the harmonic mean of recall and precision, it balances
the potential conflict between the two, and comprehensively evaluates
the overall performance of the method in terms of “minimizing missed
detections”  and  “minimizing  false  alarms,”  particularly  suitable  for
scenarios  with  imbalanced  samples.  The  calculation  formula  is  as
follows:

Fig. 5. Real-time anomaly detection flowchart based on sliding window.

6

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

F1 (cid:0) Score = 2

Precision × Recall
Precision + Recall

(13)

Table 1
Description of field and greenhouse experimental data parameters.

4)  False  Positive  Rate  (FPR):  This  was  calculated  as  the  ratio  of  the
number of false positives to the total number of normal samples. The
FPR  quantifies  the  proportion  of  normal  samples  that  are  incorrectly
predicted  as  abnormal.  The  FPR  reflects  the  ability  of  the  anomaly-
detection  model  to  correctly  identify  normal  samples.  A  low  FPR  in-
dicates that the model can prevent misclassifying normal samples more
accurately, thereby reducing ineffective interference. By contrast, a high
FPR may render the model useless owing to excessive false alarms. The
calculation formula is as follows:

FPR = FP

TN + FP

(14)

3. Experimental results and discussion

3.1. Data Introduction and Preprocessing

This study conducted experimental analyses on common monitoring
indicators in two agricultural scenarios: fields and greenhouses. For the
field scenario, soil moisture content data in the 0–20 cm and 20–40 cm
soil layers were selected. Soil moisture content is a fundamental envi-
ronmental parameter in dryland and irrigated agriculture [32]. Anom-
aly detection in time-series data is critical for ensuring crop growth and
improving  water  use  efficiency.  In  the  greenhouse  scenario,  air  tem-
perature  and  humidity  data  were  selected.  Time-series  characteristics
and  anomaly  patterns  of  air  temperature  and  humidity  are  typical  in
various  controlled  agricultural  environments  as  core  indicators  for
environmental  monitoring  in  protected  agriculture  [33].  Collectively,
they constitute the key time-series monitoring data for two typical sce-
narios characterized by natural and controlled conditions in agricultural
production,  thereby  providing  strong  representativeness.  The  corre-
sponding monitoring environments are shown in Fig. 6.

To  evaluate  the  generalization  of  the  model  under  different  time
spans and data frequencies, the field and greenhouse data were collected
over  distinct  time  periods  and  sampling  intervals.  The  specific  data
parameters are listed in Table 1.

After expert annotation, the field dataset contained 33,650 records,
of which 32,885 were normal and 765 were abnormal. The greenhouse
dataset contained 10,584 records, with 10,524 normal and 60 abnormal
data. To accurately evaluate the anomaly detection performance of the
model, we adopted a stratified random splitting method, splitting each
stratum of the dataset independently at an 8:2 ratio before recombining
them, so as to ensure that the test samples cover all annotated anomaly

Scenario

Input Elements

Time Range

Field

Greenhouse

0–20 cm soil moisture
content
20–40 cm soil moisture
content
Air temperature
Air relative humidity

Sampling
Interval

1 h

2021/1/1–2022/
12/31

2024/10/1–2024/
10/15

5 min

cases in this study. As reflected in the data distribution, the samples were
imbalanced, and the proportion of abnormal data was relatively low. If
the model is trained directly, overfitting may occur, and the model will
tend toward the majority class (normal data), resulting in suboptimal
detection  of  abnormal  data.  Therefore,  to  ensure  effective  detection
performance  of  the  model,  this  study  performed  a  synthetic  minority
oversampling  technique  (SMOTE)  oversampling  operation  on  the
training set data. By calculating the distances between abnormal sam-
ples, synthetic samples were generated between similar samples instead
of simple replications. This ensured that overfitting is avoided with a
balanced training sample.

In addition,  in  the anomaly detection task,  two  key issues  require
attention:  the  false  negative  of  anomalies  (missed  detection)  and  the
false  positive  of  normal  samples  (misjudgment  as  anomalies).  Dis-
tinguishing abnormal samples that closely resemble normal samples or
normal samples that resemble abnormal samples remains significantly
challenging. Although SMOTE achieves “quantity balance,” the model’s
attention to the minority class remains “passive.” To enable the model to
“focus  actively”  on  these  hard-to-distinguish  samples,  this  study  em-
ploys  the  Focal  Loss  function.  Focal  loss  reduces  the  weight  of  easily
distinguishable  samples  and  increases  the  weight  loss  of  hard-to-
distinguish  samples  by  introducing  a  modulating  factor  and  weight
factor [34]. Consequently, it effectively enhanced the anomaly detection
performance of the model. The formula is as follows:
FocalLoss(pt) = (cid:0) αt(1 (cid:0) pt)γ

log(pt)

(15)

{

pt =

p
1 (cid:0) p

if y = 1

otherwise

(16)

where  pt  denotes  the  predicted  probability  of  the  model  for  the
“target class.” Furthermore, γ is the modulating factor, which is used to
reduce  the  loss  weight  of  easily-distinguishable  samples  and  αt  is  the
weight  factor,  which  is  used  to  adjust  the  weights  of  positive  and

Fig. 6. Agricultural sensor deployment in two scenarios: (a) Field soil monitoring; (b) Greenhouse environmental monitoring.

7

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

negative  classes.  Typically,  the  weight  of  the  minority  class  (such  as
abnormal samples) is set to be larger to increase its proportion in the loss
calculation.

Prior to model training, it is crucial to normalize the sensor data with
different dimensions. This ensures the fairness of the model learning for
each feature and prevents the problem of unbalanced gradient updates
caused by dimensional differences. The following is a unified dimension-
handling solution for the agricultural environmental data of fields and
greenhouses:

Min-Max normalization is applicable to data with clear boundaries,
such as soil moisture content and relative humidity. It scales the data to
an interval [0,1], while preserving the distribution characteristics of the
original data. The formula is as follows:
XMin(cid:0) Max = X (cid:0) Xmin
Xmax (cid:0) Xmin

(17)

where X represents a certain sample value in the original data, Xmin is
the  minimum  value  of  this  feature  in  the  entire  dataset, Xmax is  the
maximum value of this feature in the entire dataset, and XMin(cid:0) Max is the
result after normalization.

Z-score standardization is suitable for data that are approximately
normally distributed or have no clear boundaries, such as temperature.
It transforms the data into a standard normal distribution with a mean of
zero and a standard deviation of unity. The formula is as follows:
XZ(cid:0) Score = X (cid:0) μ
σ

(18)

where  X is  defined  as  previously  described, μ  represents  the  mean
value of this feature across the entire dataset, σ represents the standard
deviation  of  this  feature  across  the  entire  dataset,  and  XZ(cid:0) Score is  the
result after standardization.

According  to  the  sliding  window  size  determination  method
described in Section 2.4, the input data of the field and greenhouse were
analyzed, and the results are shown in Fig. 7.

The window sizes for the 0–20 cm and 20–40 cm soil moisture in the
field were 717 and 973 (1-hour interval), respectively; the window sizes
for the air temperature and relative humidity in the greenhouse were 42

and 39 (5-minute interval), respectively.

3.2. Model comparison analysis

To  evaluate  the  advantages  of  the  proposed  model  (LGCA-Net)  in
fusing global and local features, we selected random forest (RF), support
vector machine (SVM), multi-scale CNN (MCNN), Transformer, tempo-
ral convolutional network (TCN), LSTM, and the series-connected TCN-
LSTM  fusion  model  for  comparison  with  the  proposed  model  (LGCA-
Net). The branch parameters of both the TCN-LSTM fusion model and
the proposed model were consistent with those of their respective single-
structure counterparts.

The  multi-scale  convolution  module  in  this  study  adopts  a  three-
layer  structure, with  each  layer utilizing three  convolution kernels of
distinct  scales.  Consequently,  the  three  values  of  the  kernel_size
parameter correspond to the sizes of the different convolution kernels,
whereas the three values of the filter parameter represent the number of
filters  in  each  of  the  three  layers.  The  detailed  parameters  of  all  the
models are presented in Table 2.

Table  3 lists  the  evaluation  metrics  of  the  test  sets  for  the  eight
models under the field and greenhouse scenarios. Both the RF and SVM

Table 2
Parameter configurations of eight models in anomaly detection experiments.

Model

Parameter setting

RF
SVM
MCNN
TCN
LSTM
Transformer

TCN-LSTM

LGCA-Net

n_estimators = 100, max_depth = 5
kernel = rbf, C = 1
kernel_size=(3,5,7), filters=(32,16,8)
kernel_size=(3,5,7), filters=(32,16,8), dilation_rate=(2,4,8)
units=(32,16,8), return_sequences = True
head_size = 256, num_heads = 4, ff_dim = 4, mlp_units = 128,
num_transformer_blocks = 2
TCN: kernel_size=(3,5,7),filters=(32,16,8), dilation_rate=(2,4,8)
LSTM: units=(32,16,8), return_sequences = True
MCNN: kernel_size=(3,5,7), filters=(32,16,8),
Transformer: head_size = 256, num_heads = 4, ff_dim = 4, mlp_units
= 128, num_transformer_blocks = 2

Fig. 7. Autocorrelation coefficient plots of agricultural sensor data in field and greenhouse scenarios.

8

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Table 3
Evaluation metrics of eight anomaly detection models on test sets in field and
greenhouse  scenarios.  sample  count:  Field  (Normal  6577,  Abnormal  153);
Greenhouse (Normal 2105, Abnormal 12).

Scenario

Model

Recall

Precision

F1-Score

FPR

Field

Greenhouse

RF
SVM
MCNN
TCN
LSTM
Transformer
TCN-LSTM
LGCA-Net
RF
SVM
MCNN
TCN
LSTM
Transformer
TCN-LSTM
LGCA-Net

0.8790
0.8601
0.9473
0.9215
0.8817
0.9343
0.9394
0.9477
0.8477
0.8992
0.9497
0.9495
0.9492
0.9000
0.9492
0.9500

0.5724
0.6370
0.9443
0.9218
0.9468
0.9645
0.8787
0.9688
0.7776
0.8923
0.9497
0.9164
0.8783
0.9994
0.8747
0.9997

0.5910
0.6902
0.9452
0.9205
0.9115
0.9489
0.9033
0.9580
0.7901
0.8882
0.9497
0.9314
0.9078
0.9442
0.9086
0.9721

0.8525
0.0468
0.0024
0.0035
0.0020
0.0014
0.0041
0.0012
0.0046
0.0017
0.0006
0.0011
0.0017
0.0000
0.0017
0.0000

models  exhibited  significant  weaknesses  in  the  two  scenarios.  In  the
field (recall 0.8790, precision 0.5724) and greenhouse (recall 0.8477,
precision 0.7776) scenarios, the RF suffers from missed detections and
false alarms.  This  limitation results from the  reliance of  feature engi-
neering  on  manual  design,  making  it  challenging  to  capture  complex
correlations in agricultural data. Although the SVM performs marginally
better than the RF in the two scenarios, it continues to exhibit limited
feature-space mapping capabilities, retaining bottlenecks in missed de-
tections and precision across different scenarios.

Deep  learning  models,  such  as  MCNN,  TCN,  LSTM,  and  Trans-
formers, exhibit advantages in both scenarios because of their automatic
feature-learning  capabilities.  However,  their  adaptability  differs  ac-
cording to the characteristics of the model structures. For the extraction
of local features, the MCNN demonstrated excellent recognition accu-
racy in the field (recall 0.9473, precision 0.9443) and greenhouse (recall
0.9497, precision 0.9497) scenarios. Compared with the TCN model for
the data from both scenarios, all MCNN metrics improved, indicating
that although the TCN aims to capture multiple scales via dilated con-
volutions,  limitations  remain  in  adapting  to  complex  non-linear  re-
lationships  and  dynamic  changes  in  agricultural  time-series  data.
Specifically, TCN cannot integrate the interactive information between
short-term  impulses  and  long-term  trends  as  effectively  as  MCNN,
resulting  in  incomplete  coverage  of  positive  cases  and  an  increase  in
misjudgments.  For  the  extraction  of  global  features,  although  the
Transformer  model,  leveraging  its  self-attention  mechanism,  has  the
advantage of uncovering long-term correlations and exhibits significant
improvements  in  most  metrics  compared  with that  of  LSTM  in  both
scenarios. However, both models exhibit inherent limitations. Although
they  perform  well  with  long-term  soil  moisture  content  data  in  field
environments,  both  models  exhibit  reduced  adaptability  to  high-
frequency  and  short-term  data  in  greenhouses.  Over-attention  to
global correlations results in insufficient modeling of key local features.
Specifically, compared with the MCNN, the recall metric of the Trans-
former decreased by 1.3% in the field scenario and 5.0% in the green-
house scenario.

The TCN-LSTM fusion model, although combining the ability of the
TCN to extract multi-scale local features and the ability of the LSTM to
capture long-term temporal dependencies, owing to the influence of its
tandem structure. The features extracted by the TCN model are used as
the input data of the LSTM. If the features extracted by the TCN fail to
accurately meet the requirements of the LSTM for long-term temporal
features, they can easily cause loss or deviation of the features during the
transfer process. In both the field and greenhouse scenarios, this results
in the fusion models exhibiting marginally lower or equivalent perfor-
mance relative to the single-structure models (TCN and LSTM).

The model presented in this paper attains the optimal performance in
both the field (recall 0.9477, precision 0.9688) and greenhouse (recall
0.9500, precision 0.9997) scenarios. Compared with models employing
single-feature extraction, the proposed model is highly compatible with
the characteristics of agricultural time-series data by integrating multi-
scale local and global features. For the long-term variations in the soil
moisture content in the field, it intensifies the global representation of
trends. For the high-frequency periodic correlations of temperature and
humidity in the greenhouse, it optimizes the learning of local periodic
features. Through the interaction between global and local features, the
model can not only capture the long-term change patterns in the field
but also precisely respond to the short-term dynamics in the greenhouse.
Eventually,  it  achieved  dual  control  over  missed  detections  and  false
alarms in both scenarios, with false positive rates (FPR) of 0.0024 and
0.0000, respectively.

Despite its robust performance, the proposed model exhibits poten-
tial limitations. The substantially low false positive rate (FPR) of 0.000
observed on the test set of the greenhouse dataset indicates nearly no
misjudgment of normal data. However, this result is related to the in-
dicators and quality of the dataset used in this study. The greenhouse
dataset in this study included only two indicators—air temperature and
relative humidity—with minimal interference from human and natural
factors, making the data stable and regular. Additionally, the anomalies
in this dataset stem from only a single type: equipment failure. However,
in  actual  agricultural  production,  the  detection  indicators  for  green-
houses are more diverse, covering light intensity, carbon dioxide, and
water-fertilizer conditions, among others. Meanwhile, abnormal situa-
tions are also more complex. When confronted with these more complex
scenarios  and  anomaly  types,  the  model  may  still  experience  missed
detections or false alarms.

See Figs. 8 and 9 present the normalized confusion matrices of the
eight  models  evaluated  under  the  field  and  greenhouse  scenarios,
respectively.  As  shows  in  the  figures,  in  the  field  scenario,  the  soil
moisture  content  is  influenced  by  multiple  factors  such  as  irrigation,
precipitation,  and  seasonal  cycles,  making  the  boundary  between
“normal” and “abnormal” ambiguous. For example, short-term high soil
moisture content caused by irrigation is a normal fluctuation rather than
an abnormality. For traditional models such as RF and SVM, the distri-
bution  of  the  confusion  matrix  along  the  diagonal  is  uneven.  The
recognition rate of the RF for normal samples was only 67.72%, indi-
cating  that  a  substantial  number  of  normal  soil  moisture  fluctuations
were misclassified as abnormal. RF cannot distinguish between “natural
fluctuations”  and  “true  abnormalities.”  The  recognition  rate  for  the
abnormal  samples  was  88.45%.  Although  it  can  capture  extreme  ab-
normalities such as sudden changes caused by sensor failures, the false
alarm  rate  is  high,  reflecting  a  limited  understanding  of  agricultural
time-series characteristics. The recognition rate of the SVM for normal
samples  increased  to  95.32%;  however,  the  recognition  rate  for
abnormal samples was only 77.12%. Similar to RF, SVM fails to capture
complex abnormal patterns under the combined effects of precipitation
and irrigation, resulting in missed detection of most abnormalities.

Among  deep-learning  models  such  as  MCNN,  TCN,  LSTM,  Trans-
former,  and  TCN-LSTM,  the  recognition  accuracy  of  normal  samples
significantly  increased  compared  with  traditional  machine  learning
models, reaching more than 99.50% in all cases. However, performance
differences emerge in abnormal sample recognition. The MCNN, owing
to  its  multiscale  convolutions,  effectively  captures  multidimensional
differences  in  soil  data,  achieving  abnormal  recognition  rate  that  ex-
ceeds that of TCN by 3.27%. The self-attention mechanism of a Trans-
former can focus dynamically on key abnormal features. Compared with
the sequential calculation of LSTM, it exhibits a higher recognition ac-
curacy for sparse abnormalities (abnormal events with low frequency
and high impact), and its abnormal recognition rate increases by 5.88%.
Although the TCN-LSTM fusion model improved the recognition rate of
abnormal samples compared with the single-structured TCN and LSTM,
owing to the influence of serial feature transmission, it also resulted in

9

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 8. Normalized confusion matrices of eight anomaly detection models on the field scenario test set.

Fig. 9. Normalized confusion matrices of eight anomaly detection models on the greenhouse scenario test set.

an  increase  in  the  false  detection  rate  of  normal  samples.  The  model
proposed in this paper, through the fusion of MCNN and Transformer,
achieved a recognition accuracy of both normal and abnormal samples
exceeding 90%, which is higher than that of other models. Thus, it can
be  seen  that  the  effectiveness  of  each  model  in  detecting  anomalies
largely depends on how well its architecture covers different anomaly
patterns.

Compared with the field scenario, results obtained from the green-
house  dataset  remain  largely  consistent,  except  that  the  LSTM  model
exhibits an abnormal recognition accuracy approximately 10% higher
than that of the Transformer. This is likely attributed to the influence of
data sampling frequency. Greenhouse data are collected at higher tem-
poral resolution, yielding denser time-series information characterized
by  frequent  short-term  fluctuations  and  instantaneous  features.  The
Transformer, which emphasizes global features and is likely to “over-
look”  these  short-term  local  abnormalities,  may  misjudge  the  abnor-
malities  in  high-frequency  normal  fluctuations  as  normal,  thereby
limiting the abnormal recognition accuracy. However, by combining the
local features extracted by the MCNN model, the Transformer abnormal
recognition accuracy is improved while ensuring that the accuracy of

normal sample recognition does not decline. It can be seen that for the
fusion  model  proposed  in  this  paper,  both  low-frequency  field  moni-
toring  scenarios  that  emphasize  long-term  trends  and  high-frequency
greenhouse scenarios that require detection instantaneous fluctuations
and subtle abnormalities benefit from the coordinated global and local
feature extraction. Global feature extraction captures long-range corre-
lations  and  overarching  temporal  patterns,  whereas  local  features
extract short-term and fine-grained abnormal patterns. Their effective
interaction enables the model to accurately characterize normal samples
while sensitively identifying abnormal  patterns, demonstrating strong
robustness across heterogeneous agricultural monitoring conditions.

3.3. Cross-Attention mechanism ablation analysis

To evaluate the advantages of the proposed cross-attention feature
fusion, it was compared with the traditional feature concatenation. The
experiments were performed under both field and greenhouse scenarios.
The results are illustrated in Fig. 10.

As shown in Fig. 10(a), for the field data, the feature fusion method
using the cross-attention mechanism exhibited an overall improvement

10

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 10. Ablation experiment comparison of cross-attention in field and greenhouse scenarios.

in the performance indicators. In particular, the recognition accuracy of
the  abnormal  samples  showed  the  most  significant  increase.  This  is
likely attributed to the greater influence on field soil data by the natural
environment.  Simple  feature  concatenation  is  prone  to  noise  interfer-
ence, whereas cross-attention dynamically emphasizes key features and
suppresses  irrelevant  noise,  thereby  improving  the  recognition  of
abnormal samples.

Compared  with  the  field  soil  data,  the  greenhouse  environmental
data were less disturbed. Therefore, as shown in Fig. 10(b), although the
cross-attention  mechanism  marginally  improves  the  performance  in
terms of precision and recall, the detection accuracy of the normal and
abnormal samples is close to that of the traditional feature concatena-
tion method. These results indicate that the benefits of cross attention
are more pronounced for complex datasets.

Finally,  to  verify  the  practical  effect  of  the  proposed  model  in
detecting abnormal data outside the training samples, for the four ele-
ments in the field and greenhouse scenarios, a continuous time series
outside  the  training  sample  time  was  used  for  real-time  abnormal
detection.  The  results  are  shown  in  Figs.  11–14 (where  the  blue  dots
represent  samples  with  incorrect  abnormal  recognition,  and  the  red
crosses represent samples with correct abnormal recognition).

The figures indicate suboptimal performance of traditional models
(RF and SVM) in detecting soil moisture content, temperature, and hu-
midity.  This  indicates  that  they  are  only  suitable  for  scenarios  with
extremely simple features and single abnormal patterns. The TCN and
MCNN are effective at handling scenarios with significant local features
and numerous minor fluctuations. For the 0–20 cm shallow soil moisture
content dataset, their anomaly detection accuracy outperforms that of
LSTM  and  Transformer.  By  contrast,  the  LSTM  and  Transformer
exhibited stable performance in scenarios with periodic data (such as
greenhouse  humidity)  and  prominent  anomalies  (such  as  deep  soil
moisture content). Their ability to learn long-sequence dependencies is
compatible  with  the  characteristics  of  time-series  data.  However,  in
terms  of  identifying  local  minor  fluctuations,  they  were  marginally
inferior to TCN and MCNN. Although the TCN-LSTM fusion model aims
to  combine  local feature  extraction with  long-sequence modelling ca-
pabilities, its performance is highly dependent on the quality of feature
extraction from the TCN front end because of the limitations of its serial
structure, resulting in only marginal improvements.

The proposed LGCA-Net model exhibits lower overall misjudgment
rate  than  that  of  the  traditional  models,  and  demonstrates  optimal
robustness in different scenarios. In the detection of the 0–20 cm shallow
field  soil  moisture  content,  this  model  exhibited  a  relatively  high
anomaly misjudgment rate, with misjudgments primarily concentrated

in the segment where the soil moisture content at the end of the data had
repeated minor changes. This is because shallow soils are more sensitive
to human and environmental disturbances. Simultaneously, the muta-
tion range of the end-part data is small, which increases the difficulty of
identification.  In  the  identification  of  the  20–40  cm  deep  field  soil
moisture content, although frequent mutations were present at the end
owing to the larger data change amplitude, the model was capable of
effectively  detecting  abnormalities.  In  the  greenhouse  scenario,  the
detection of the environmental temperature and relative humidity was
satisfactory. Except for two minor abnormal fluctuations in the relative
humidity  that  were  not  identified,  nearly  all  other  abnormal  samples
were accurately detected.

In summary, the proposed abnormal detection model of global and
local feature fusion exhibits robust detection capabilities for sensor data
in  different  agricultural  environments.  Although  there  is  room  for
optimization  owing  to  the  influence  of  data  features  in  complex  sce-
narios such as shallow soil, it performs reliably in deep soil and regular
greenhouse  environments,  providing  valuable  technical  support  for
agricultural environment monitoring. In the future, the model structure
can be further optimized for special scenarios to improve the model's
ability to identify minor fluctuating abnormalities.

3.4. Analysis of model complexity and inference efficiency

To  further  evaluate  the  applicability  of  the  proposed  LGCA-Net
model  to  real-time  agricultural  monitoring  scenarios,  we  statistically
analyzed and compared the parameter scale, model size, computational
complexity  (FLOPs),  and  average  inference  time  of  various  models.
Because  traditional  models  (RF  and  SVM)  exhibit  low  accuracy  and
cannot leverage the GPU for inference acceleration, this section focuses
on a horizontal comparison among deep learning models (TCN, MCNN,
LSTM, Transformer,  TCN-LSTM). To  ensure a fair comparison, all the
experiments  were  conducted  under  the  same  hardware  environment
(CPU: Intel Core i7-14700F; memory: 32 GB; GPU: NVIDIA RTX 4060 Ti
(8G)). The results are summarized in Table 4.

As shown in Tables 3 and 4, the LSTM and TCN-LSTM models are
limited  by  the  LSTM  network  structure  and  cannot  achieve  parallel
computing. Their inference times ranged from 42.296 ms to 50.881 ms,
resulting in suboptimal real-time performance and lower accuracy than
that of LGCA-Net. They only have lightweight advantages in terms of
computational  complexity  (12.12  M(cid:0) 34.26  M)  and  model  size  (86
KB–167  KB),  making  them  suitable  only  for  simple  scenarios  with
limited computing performance and low requirements for both real-time
performance and accuracy.

11

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 11. Detection results of abnormal soil moisture content of 0–20 cm in field.

12

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 12. Detection results of abnormal soil moisture content of 20–40 cm in field.

13

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 13. Detection results of abnormal air relative humidity in greenhouse.

14

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Fig. 14. Detection results of abnormal air temperature in greenhouse.

15

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Table 4
Comparison of parameter scale, model sizes, computational complexity (FLOPs),
and inference performance of six deep learning models for agricultural sensor
time-series anomaly detection.

Model

Parameter Scale
(units)

Model
Size (KB)

FLOPs
(M)

Average
Inference Time
(ms)

MCNN
TCN
LSTM
Transformer
TCN-LSTM
LGCA-Net

40,849
19,281
15,497
14,757
28,465
55,605

266
118
86
120
167
388

73.13
21.65
12.12
34.41
34.26
107.55

14.124
10.518
42.296
10.500
50.881
20.209

Although TCN and Transformer are lightweight (size: 118–120 KB)
and have fast inference speed (approximately 10.5 ms), their accuracy is
insufficient,  making  it  difficult  to  balance  “speed  and  performance”.
Although MCNN and the proposed LGCA-Net have higher parameters,
larger sizes, and greater computational complexity than the aforemen-
tioned  models,  the  proposed  LGCA-Net  achieves  a  more  significant
improvement in accuracy. Moreover, its inference time of 20.21 ms is
substantially  lower  than  the  sampling  frequencies  of  5  min  and  1  h,
meeting the requirements of real-time monitoring and delivering higher
comprehensive  cost-effectiveness  under  limited  edge-side  resources.
Additionally,  the  proposed  model  extracts  more  comprehensive  fea-
tures, and its accuracy advantage will be more prominent in complex
scenarios.

4. Conclusion

In  response  to  the  long-term  and  short-  erm  variation  patterns
exhibited by agricultural time-series sensor data, this study introduced a
general  time-series  anomaly  detection  method  for  multiple  types  of
agricultural sensors, LGCA-Net, based on the fusion of global and local
features. This method leverages a multi-scale CNN (MCNN) to extract
local  features,  captures  global  features  via  the  multi-head  attention
mechanism of the transformer, and implement the interactive integra-
tion of global and local features employing the cross-attention mecha-
nism. Consequently, anomaly detection can be effectively performed for
time-series data in diverse agricultural scenarios.

The  experimental  results  indicate  that,  compared  with  the  seven
existing  models,  the  proposed  fusion  model  demonstrates  superior
detection performance in both field and greenhouse scenarios. In terms
of  the  F1-Score  metric,  which  comprehensively  measures  the  balance
between  false  alarms  (precision)  and  missed  detections  (recall),  the
model achieved 0.9580 in the field scenario and 0.9721 in the green-
house scenario. Compared with the single-structure models, it exhibited
an  average  increase  of  6.65%  (in  the  field)  and  6.67%  (in  the  green-
house) in the recognition accuracy of abnormal samples.

In addition, to evaluate the advantages of the cross-attention fusion
mechanism, we conducted an ablation analysis. The results show that
the optimization effect of cross attention is particularly significant when
the data are affected by complex factors. When the influencing factors of
the data are simple, their effect is similar to or marginally better than
that  of  the  traditional  concatenation  method.  This  indicates  that  the
proposed model is more suitable for handling complex agricultural data.
Meanwhile,  LGCA-Net  maintains  good  computational  efficiency,  with
an average inference time of 20.209 ms under the experimental hard-
ware environment, which is substantially lower than the sampling fre-
quencies of the field (1 h) and greenhouse (5 min) scenarios, meeting
real-time monitoring requirements.

Although this study has achieved significant progress, several limi-
tations  remain  that  can  be  further  addressed  in  future  work.  (1)  The
experimental validation was limited to datasets from two scenarios, field
and greenhouse, which constrain the full demonstration of the model’s
performance. In the future, we will expand the research scope to include

agricultural sensor data from more types and application scenarios to
further  explore the  generalizability  of the  model in  complex  environ-
ments; (2) This study employs a supervised learning framework, where
the  range  of  detectable  anomalies  is  constrained  by  the  diversity  of
annotated  anomaly  samples  in  the  dataset.  Therefore,  practical
deployment  requires  fine-tuning  for  specific  datasets  to  adapt  to
different anomaly situations. Future research will further optimize the
model  structure  and  attempt  to  introduce  self-supervised  learning
methods,  enabling  the  model  to  independently  learn  the  distribution
characteristics of normal data, mitigate the reliance on annotated sam-
ples; (3) We will also take into account the requirements of edge-end
deployment and focus on the lightweight optimization of the model to
enhance  its  applicability  in  resource-constrained  agricultural  IoT
scenarios.

CRediT authorship contribution statement

Zongren Wang: Writing – original draft, Visualization, Validation,
Software,  Resources,  Methodology,  Formal  analysis,  Data  curation.
Laixi  Zhang:  Supervision.  Jianbo  Guo:  Supervision.  Yuan  Huang:
Investigation. Ping Lin: Project administration. Wengang Zheng: Su-
pervision, Funding acquisition. Lili Zhangzhong: Writing –  review &
editing, Funding acquisition.

Declaration of competing interest

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

Acknowledgment

This work was supported by the National Key R&D Program of China
[Grant  No.  2022YFD1900803];  the  Bingtuan  Science  and  Technology
Program [Grant No. 2023AB060]; the Beijing Academy of Agriculture
and Forestry Sciences Major Scientific and Technological Achievement
Cultivation Project: Key Technology Equipment and Industrialization of
Smart Irrigation; the Beijing Nova Program [Grant No. 20230484375];
and the Earmarked Fund for CARS-02 and CARS-54. We express great
appreciation to the anonymous reviewers and editors for the improve-
ment of this manuscript. We would also like to thank Editage for English
language editing.

References

[1] Zhong KY, Sun XQ, Liu GD, et al. Attention-based generative adversarial networks
for aquaponics environment time series data imputation [J]. Inform Process Agric
2024;11(4):542–51. https://doi.org/10.1016/j.inpa.2023.10.001.

[2] Pompeo J, Yu Z, Zhang C, et al. Assessing the stability of indoor farming systems
using data outlier detection [J]. Front Plant Sci 2025;15:1270544. https://doi.org/
10.3389/fpls.2024.1270544.

[3] Jung JM, Kim DH, Cho H, et al. Multi-algorithmic approach for detecting outliers in
cattle intake data[J]. J Agric Food Res 2024;15:101021. https://doi.org/10.1016/
j.jafr.2024.101021.

[4] Suryavansh S, Benna A, Guest C, et al. A data-driven approach to increasing the

lifetime of IoT sensor nodes. Sci Rep 2021;11:22459. https://doi.org/10.1038/
s41598-021-01431-y.

[5] Wang, Z.N.; Wang, Y.J, et al. Anomaly Detection for Multivariate Time Series Based

on Multi-Window Segmentation Ensemble Learning[J/OL]. Journal of Computer
Research and Development.2025,1777-1811. https://link.cnki.net/urlid/11.1777.
TP.20250507.1811.002.

[6] Backhus J, Rao AR, Venkatraman C, et al. Time series anomaly detection using

signal processing and deep learning. Appl Sci 2025;15:6254. https://doi.org/
10.3390/app15116254.

[7] Kulanuwat L, Chantrapornchai C, Maleewong M, et al. Anomaly detection using a

sliding window technique and data imputation with machine learning for
hydrological time series. Water 1862;2021:13. https://doi.org/10.3390/
w13131862.

[8] Zamry NM, Zainal A, Rassam MA, et al. Lightweight anomaly detection scheme
using incremental principal component analysis and support vector machine.
Sensors 2021;21:8017. https://doi.org/10.3390/s21238017.

16

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Zongren  Wang:  Master,  Algorithm  Engineer.  Specializing  in
information and communication engineering. Research focus is
on deep learning and agricultural information processing. Ob-
tained the master's degree in Information and Communication
Engineering  from  Yangtze  University  in  2024.  Information
Technology  Research Centre, Beijing Academy  of Agriculture
and Forestry Sciences, Beijing 100097, China. Current institu-
tional mail address: wangzr@nercita.org.cn

Laixi Zhang: Master, Senior Agronomist, Agronomist and di-
rector of the Science and Technology Operation Office of Bei-
jing  Changyang  Farm  Co.,  Ltd.  He  graduated  from  Beijing
Agricultural  College  in  2011  with  a  master's  degree  in
agronomy, specializing in fruit trees. His research interests are
mainly in the fields of fruit tree cultivation management, or-
chard  informatization  and  intelligent  equipment.  Beijing
Changyang  Farm  Co.,  Ltd.,  Beijing  100097,  China.  Current
institutional zlx123456zlx2023@163.com.

Jianbo  Guo:  Senior  Agronomist,  Party  Branch  Secretary,  Di-
rector and Manager of Beijing Changyang Farming Co., Ltd. His
specialisation  lies  in  horticulture.  His  research  interests  pri-
marily focus on horticulture, facility agriculture and intelligent
equipment. Beijing Changyang Farm Co., Ltd., Beijing 100097,
China. Current institutional 13161628911@163.com.

Yuan Huang: Master, Senior Agronomist. She has been mainly
engaged in research and technology promotion of smart water
and fertilizer management. Obtained the master's degree from
Huazhong  Agricultural  University  in  2012.  She  is  currently
working at Shijiazhuang Academy of Agriculture and Forestry
Sciences,  Shijiazhuang  050041,  China.  Current  institutional
17731175112@189.cn.

Ping Lin: Master, Senior Engineer. She is the deputy director of
the Engineering Center of Xinjiang Tianye Co., Ltd. and also an
external  mentor  at  the  Water  Engineering  College  of  Shihezi
University. In 2009, she obtained a master's degree in Hydraulic
Engineering  from  Northwest  A&F  University.  She  has  been
engaged in the research and promotion of agricultural water-
saving  irrigation  technology  products  for  a  long  time.  Xin-
jiang  Tianye  Co.,  Ltd.,  Xinjiang  832000,  China  Current  insti-
tutional xjtylp@qq.com.

[9] Utkin L, Ageev A, Konstantinov A, et al. Improved anomaly detection by using the
attention-based isolation forest. Algorithms 2023;16:19. https://doi.org/10.3390/
a16010019.

[10] Chua W, Pajas ALD, Castro CS, et al. Web traffic anomaly detection using isolation

forest. Informatics 2024;11:83. https://doi.org/10.3390/informatics11040083.

[11] Zhang Z, Dong S, Li D, et al. Prediction and diagnosis of electric vehicle battery
fault based on abnormal voltage: using decision tree algorithm theories and
isolated forest. Processes 2024;12:136. https://doi.org/10.3390/pr12010136.
[12] Verma RD, Keserwani PK, Jain VK, et al. Optimal partitioning of unbalanced

datasets for BGP anomaly detection. Telecom 2025;6:25. https://doi.org/10.3390/
telecom6020025.

[13] Liu GD, Zhong KY, Li HL, et al. A state of art review on time series forecasting with

machine learning for environmental parameters in agricultural greenhouses[J].
Information Processing in Agriculture 2024;11(2):143–62. https://doi.org/
10.1016/j.inpa.2022.10.005.

[14] Nicholaus IT, Park JR, Jung K, et al. Anomaly Detection of Water Level using Deep

Autoencoder. Sensors 2021;21:6679. https://doi.org/10.3390/s21196679.
[15] Elhalwagy A, Kalganova T. Multichannel LSTM-capsule autoencoder network for
anomaly detection on multivariate data. Appl Sci 2022;12:11393. https://doi.org/
10.3390/app122211393.

[16] Esmaeili F, Cassie E, Nguyen HPT, et al. Anomaly detection for sensor signals

utilizing deep learning autoencoder-based neural networks. Bioengineering 2023;
10:405. https://doi.org/10.3390/bioengineering10040405.

[17] Liu J, Huang Y, Wu D, et al. Multi-Channel Multi-Scale Convolution attention
Variational Autoencoder (MCA-VAE): an Interpretable Anomaly Detection
Algorithm based on Variational Autoencoder. Sensors 2024;24:5316. https://doi.
org/10.3390/s24165316.

[18] Wang H, Zhang H. An anomaly detection method for multivariate time series data
based on variational autoencoders and association discrepancy. Mathematics 2025;
13:1209. https://doi.org/10.3390/math13071209.

[19] Xu L, Xu K, Qin Y, et al. TGAN-AD: Transformer-based GAN for anomaly detection

of time series data. Appl Sci 2022;12:8085. https://doi.org/10.3390/
app12168085.

[20] Niu Z, Yu K, Wu X. LSTM-Based VAE-GAN for Time-Series Anomaly Detection.

Sensors 2020;20:3738. https://doi.org/10.3390/s20133738.

[21] Zhang X, Zhao H, Zhang W, et al. FedSW-TSAD: SWGAN-Based federated time
series anomaly detection. Sensors 2025;25:4014. https://doi.org/10.3390/
s25134014.

[22] Gopali S, Siami Namin A. Deep Learning-based Time-Series Analysis for Detecting
Anomalies in internet of things. Electronics 2022;11:3205. https://doi.org/
10.3390/electronics11193205.

[23] Noh S-H, Moon HJ. Anomaly detection based on LSTM Learning in IoT-based

dormitory for indoor environment control. Buildings 2023;13:2886. https://doi.
org/10.3390/buildings13112886.

[24] Lee G, Yoon Y, Lee K. Anomaly detection using an ensemble of multi-point LSTMs.

Entropy 2023;25:1480. https://doi.org/10.3390/e25111480.

[25] Gomolka Z, Zeslawska E, Olbrot L. Using Hybrid LSTM Neural Networks to Detect
Anomalies in the Fiber Tube Manufacturing Process. Appl Sci 2025;15:1383.
https://doi.org/10.3390/app15031383.

[26] Duraj A, Szczepaniak PS, Sadok A. Detection of anomalies in data streams using the

LSTM-CNN Model. Sensors 2025;25:1610. https://doi.org/10.3390/s25051610.

[27] Zhou XC. Anomaly detection of sensor streaming data based on the fusion of ARMA

and CNN-LSTM[J]. Foreign Electronic Measurement Technology 2022;41(04):
55–61. https://doi.org/10.19652/j.cnki.femt.2203663.

[28] Peng X, Li H, Lin Y, et al. TCF-Trans: Temporal Context Fusion Transformer for
Anomaly Detection in Time Series. Sensors 2023;23:8508. https://doi.org/
10.3390/s23208508.

[29] Baidya R, Jeong H. Anomaly detection in time series data using reversible instance
normalized anomaly transformer. Sensors 2023;23:9272. https://doi.org/10.3390/
s23229272.

[30] Hao ZY, Li MZ, Yang W, et al. Evaluation of UAV spraying quality based on 1D-
CNN model and wireless multi-sensors system [J]. Information Processing in
Agriculture 2024;11(1):65–79. https://doi.org/10.1016/j.inpa.2022.07.004.
[31] Zhang JR, Tang C, Wang L, et al. Data mining algorithms for the prediction of

inorganic nitrogen in water: Mechanisms, techniques, and applications [J].
Information Processing in Agriculture 2025. https://doi.org/10.1016/j.
inpa.2025.12.005.

[32] Amiri Z, Gheysari M, Mosaddeghi M R, et al. An attempt to find a suitable place for
soil moisture sensor in a drip irrigation system[J]. Information Processing in
Agriculture, 2022, 9(2): 254-265. doi:10.1016/j.inpa.2021.04.010.

[33] Liu KG, Ji T, Li M, et al. Prediction of greenhouse temperature and humidity across
growing seasons: Hybridization of process-based model and deep neural networks
[J]. Information Processing in Agriculture 2025. https://doi.org/10.1016/j.
inpa.2025.11.002.

[34] Zhang Y, Yue J, Song AH, et al. A High-similarity shellfish recognition method

based on convolutional neural network [J]. Information Processing in Agriculture
2023;10(2):149–63. https://doi.org/10.1016/j.inpa.2022.05.009.

17

Z. Wang et al.

Information Processing in Agriculture xxx (xxxx) xxx

Wengang  Zheng:  Ph.D,  Researcher,  Deputy  Director  of  the
National Research Center of Intelligent Agricultural Equipment
Technology.  He  received  his  Ph.D.  in  Engineering  Mechanics
from Dalian University of Technology in 2002. Research focus
is  on  smart  agriculture  control  technologies  and  equipment.
Intelligent  Equipment  Research  Center,  Beijing  Academy  of
Agriculture  and  Forestry  Sciences,  Beijing  100097,  China.
Current institutional zhengwengang@nercita.org.cn.

Lili Zhangzhong: Ph.D, Associate Researcher. She received her
Ph.D.  in  Agricultural  Engineering  from  China  Agricultural
University in 2016. Research focus is on smart water and fer-
tilizer  regulation  technologies  and  equipment.  Information
Technology  Research Centre, Beijing Academy  of Agriculture
and Forestry Sciences,  Beijing 100097, China.Current institu-
tional zhangzll@nercita.org.cn.

18

