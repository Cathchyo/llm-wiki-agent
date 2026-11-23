# Prithvi-EO-2.0: A Versatile Multitemporal Foundation Model for Earth Observation Applications

**Authors:** Daniela Szwarcman, Sujit Roy, Senior Member, IEEE, Paolo Fraccaro, Þorsteinn Elí Gíslason, Benedikt Blumenstiel, Member, IEEE, Rinki Ghosal, Pedro Henrique de Oliveira, Joao Lucas de Sousa Almeida, Rocco Sedona, Member, IEEE, Yanghui Kang, Srija Chakraborty, Member, IEEE, Sizhe Wang, Carlos Gomes, Ankur Kumar, Vishal Gaur, Myscon Truong, Denys Godwin, Sam Khallaghi, Hyunho Lee, Graduate Student Member, IEEE, Chia-Yu Hsu, Ata Akbari Asanjan, Besart Mujeci, Disha Shidham, Rufai Omowunmi Balogun, Venkatesh Kolluru, Trevor Keenan, Paulo Arevalo, Wenwen Li, Hamed Alemohammad, Member, IEEE, Pontus Olofsson, Timothy Mayer, Christopher Hain, Robert Kennedy, Bianca Zadrozny, David Bell, Gabriele Cavallaro, Senior Member, IEEE, Campbell Watson, Manil Maskey, Senior Member, IEEE, Rahul Ramachandran, and Juan Bernabe Moreno

**Publication:** *IEEE Transactions on Geoscience and Remote Sensing*, vol. 64, 2026, article 4400120  
**DOI:** [10.1109/TGRS.2025.3642610](https://doi.org/10.1109/TGRS.2025.3642610)  
**Dates:** Received 21 May 2025, revised 25 September 2025, accepted 5 December 2025, published 11 December 2025, current version 2 January 2026.

This work was supported in part by the National Aeronautics and Space Administration (NASA) under Grant 80MSFC22M004 and in part by the Gauss Centre for Supercomputing e.V. The work of Yanghui Kang was supported by NASA under Award 80NSSC24K1562.

Daniela Szwarcman, Sujit Roy, and Paolo Fraccaro contributed equally to this work. Corresponding authors: Sujit Roy (sr0197@uah.edu) and Paolo Fraccaro (paolo.fraccaro@ibm.com).

© 2025 The Authors. This work is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).

## Author Affiliations

Daniela Szwarcman, Paolo Fraccaro, Benedikt Blumenstiel, Pedro Henrique de Oliveira, Joao Lucas de Sousa Almeida, Carlos Gomes, Bianca Zadrozny, Campbell Watson, and Juan Bernabe Moreno are with IBM Research, Washington, DC 20024 USA (e-mail: paolo.fraccaro@ibm.com).

Sujit Roy is with the NASA Marshall Space Flight Center, Huntsville, AL 35808 USA, and also with the Earth System Science Center, The University of Alabama in Huntsville, Huntsville, AL 35805 USA (e-mail: sr0197@uah.edu).

Þorsteinn Elí Gíslason is with the School of Engineering and Natural Sciences, University of Iceland, Reykjavik, 101 Iceland.

Rinki Ghosal, Ankur Kumar, Vishal Gaur, Venkatesh Kolluru, and Timothy Mayer are with the Earth System Science Center, University of Alabama in Huntsville, Huntsville, AL 35805 USA.

Rocco Sedona is with Jülich Supercomputing Centre, Forschungszentrum Jülich, 52428 Jülich, Germany.

Yanghui Kang is with the Department of Biological Systems Engineering, Virginia Tech, Blacksburg, VA 24061 USA.

Srija Chakraborty, Ata Akbari Asanjan, Besart Mujeci, Disha Shidham, and David Bell are with the Earth from Space Institute, Universities Space Research Association, Washington, DC 20024 USA.

Sizhe Wang, Hyunho Lee, Chia-Yu Hsu, and Wenwen Li are with the School of Geographical Sciences and Urban Planning, Arizona State University, Tempe, AZ 85281 USA.

Myscon Truong and Robert Kennedy are with the College of Earth, Ocean, and Atmospheric Sciences, Oregon State University, Corvallis, OR 97331 USA.

Denys Godwin, Sam Khallaghi, Rufai Omowunmi Balogun, and Hamed Alemohammad are with the Center for Geospatial Analytics, Clark University, Worcester, MA 01610 USA.

Trevor Keenan is with the Department of Environmental Science, Policy, and Management, University of California, Berkeley, Berkeley, CA 94720 USA.

Paulo Arevalo is with the Department of Earth and Environment, Boston University, Boston, MA 02215 USA.

Pontus Olofsson, Christopher Hain, Manil Maskey, and Rahul Ramachandran are with the NASA Marshall Space Flight Center, Huntsville, AL 35808 USA.

Gabriele Cavallaro is with the School of Engineering and Natural Sciences, University of Iceland, Reykjavik, 101 Iceland, and also with Jülich Supercomputing Centre, Forschungszentrum Jülich, 52428 Jülich, Germany.

## Abstract

This article presents Prithvi-EO-2.0, a new geospatial foundation model (GFM) that offers significant improvements over its predecessor, Prithvi-EO-1.0. Trained on 4.2 million global time-series samples from NASA’s Harmonized Landsat and Sentinel-2 data archive at 30-m resolution, the new model incorporates temporal and location embeddings for enhanced performance across various geospatial tasks. Through extensive benchmarking with GEO-Bench, the model outperforms the previous Prithvi-EO model by 8% across a range of tasks. It also outperforms six other GFMs when benchmarked on remote sensing tasks from different domains and resolutions (i.e., from 0.1 to 15 m). The results demonstrate the versatility of the model in both classical Earth observation (EO) and high-resolution applications. Early involvement of end-users and subject matter experts (SMEs) allowed constant feedback on model and dataset design, enabling customization across diverse SME-led applications in disaster response, land cover and crop mapping, and ecosystem dynamics monitoring. Prithvi-EO-2.0 is available as an open-source model on Hugging Face and IBM TerraTorch, with additional resources on GitHub. The project exemplifies the Trusted Open Science approach embraced by all involved organizations.

## Index Terms

Earth observation (EO), geospatial foundation model (GFM), Harmonized Landsat and Sentinel-2 (HLS), machine learning, multi-temporal remote sensing.

## I. Introduction

In recent years, Earth observation (EO) has entered a new era with the rise of geospatial foundation models (GFMs)—large-scale artificial intelligence (AI) systems trained on vast amounts of unlabeled satellite imagery using self-supervised learning [1]. Foundation models are general-purpose neural networks (often based on transformer architectures) that learn broad representations from massive datasets and can be fine-tuned for many downstream tasks with minimal labeled data [2]. These models can help address long-standing challenges in EO by reducing the need for manually labeled samples, which are usually hard to obtain at scale [1]. Remote sensing is especially well-suited for foundation model development due to its global coverage, frequent revisits, and the sheer scale of unstructured imagery. Once pretrained, GFMs require less data to achieve similar or even superior performance across various domains [3], [4]. Despite their potential, real-world adoption remains limited.

We identify three main limitations with available GFMs. First, although EO data is inherently multitemporal, most GFMs do not account for this characteristic. Those that do either process only point data or focus on long time series restricted to small patches or individual pixels [4], [5]. Second, in-depth validation considering diverse types of tasks and clear comparison protocols remains limited. This hinders users’ ability to assess whether the models are suitable for their use case. Third, adapting state-of-the-art GFMs to different applications may require AI expertise in the absence of the proper tools and guidance. While several GFMs have released the weights and model architecture [3], [4], [6], [7], [8], which is an important step toward community adoption, we believe that the lack of clear instructions or a streamlined code base for fine-tuning remains a significant barrier to broader use and further evaluation of GFMs. To address these issues and increase the impact of GFMs within the EO community, we developed a new multitemporal GFM called Prithvi-EO-2.0.[^1] Building on its US-only predecessor, Prithvi-EO-1.0 [9], our new model explicitly uses transformer attention in both spatial and temporal dimensions and also incorporates metadata for location and time to better organize the embedding space. Pretraining was conducted at scale on a large dataset of medium resolution (30 m) satellite imagery created from NASA’s Harmonized Landsat Sentinel-2 (HLS) archive spanning a decade. We designed a new sampling strategy for our pretraining dataset to focus on long-term trends and seasonal patterns, while also ensuring diverse and high-quality samples, so the model can better capture these characteristics. The scale of this dataset also allowed us to increase the model size up to 600 million parameters, placing Prithvi-EO-2.0 among the largest in the field of EO.

In addition, we conducted extensive validation, in close collaboration with remote sensing subject matter experts (SMEs), who were also involved in the dataset and model design. In particular, we validated Prithvi-EO-2.0 through a comprehensive benchmarking process with GEO-Bench [10], a robust framework for assessing EO Foundation Models. Furthermore, we evaluated the models across a diverse set of applications, with SMEs playing a central role in implementation and assessment of results. To facilitate adoption and fine-tuning for new downstream tasks, we integrated Prithvi-EO-2.0 into TerraTorch,[^2] a toolkit powered by PyTorch Lightning[^3] and TorchGeo[^4] that simplifies customization of GFMs for various EO applications. The data loaders used in this work were also included in TerraTorch for reproducibility. Our results show that Prithvi-EO-2.0 can generalize across a wide range of remote sensing tasks, spanning different spatiotemporal resolutions and domains, often requiring fewer labeled samples to achieve strong performance compared to baseline models.

The structure of the article is as follows. First, we introduce related work and then our methodology, starting with the description of our sampling strategy and the processes to build our global pretraining dataset. Next, we present the Prithvi-EO-2.0 architecture and the pretraining procedure. We then detail our evaluation approach, including benchmarking on the GEO-Bench [10] framework and SME-led downstream tasks. Finally, we present our results for benchmarking and applications, and discuss the outcomes.

## II. Related Work

Recent advances in self-supervised learning and large-scale pretraining have enabled the development of GFMs for EO data. Early work includes SatMAE [3], which adapts masked autoencoders (MAEs) to satellite imagery with two variants: a spectral model with multiple patch embeddings grouping similar bands, and a temporal model trained on sequences of three RGB images with a shared 2-D patch embeddings layer [3]. Although multispectral and temporal aspects are studied, they are not combined into a unified model. Scale-MAE [11] also builds on MAE, addressing scale variation by introducing a bandpass filter to separate and reconstruct low- and high-frequency images at different scales [11]. However, Scale-MAE is limited to RGB data and lacks temporal modeling.

Other approaches explore contrastive learning and distillation methods. The SSL4EO-S12 [12] is a large-scale dataset of Sentinel-1/2 imagery (3-M patches, four seasonal frames per location). The authors pretrain ResNet-50 and ViT-S backbones using MoCo (contrastive) and DINO (distillation) on the Sentinel-2 part [12]. The frames, however, serve only as augmentation rather than explicit sequence modeling.

DeCUR [7] and DOFA [6] invest in multimodal pretraining, with the first adopting the SSL4EO-S12 dataset and the latter considering several data sources. DeCUR employs separate encoders for each modality and proposes to decouple common and unique modality representations via multimodal redundancy reduction [7]. DOFA adopts a hypernetwork approach that generates weights conditioned on the central wavelength of each band. The pretraining procedure combines masked image modeling with distillation from ImageNet-based models [6]. Both DeCUR and DOFA operate on 2-D inputs only.

Temporal modeling is the focus of Presto [4], a lightweight transformer for EO pixel time series. The model is trained with 12 months of data from different sources, with each month represented by a monthly timestamp, including Sentinel-1/2, topography, ERA-5, and metadata. While effective for time-series tasks, Presto is evaluated on image tasks in a limited manner: nine pixels are sampled from the images, and the results are the mode of the corresponding predictions [4]. In contrast, U-BARN [5] also considers the spatial aspect: a BERT-like approach is used for pretraining, with an architecture that combines a U-Net with a transformer. Despite its spatiotemporal design, U-BARN is trained with small 64 × 64 patches and a very restricted pretraining dataset, considering only nine Sentinel-2 tiles from France over two years [5].

In this context, Prithvi-EO-2.0 focuses on a larger, higher quality global dataset with more than 4-M samples, as well as larger models, and flexibility regarding the use of metadata. Our approach emphasizes spatiotemporal modeling, incorporating seasonal and long-term dynamics over a decade, significantly exceeding the temporal coverage of prior models, while maintaining spatial representation capabilities.

## III. Methods

### A. Dataset Description and Sampling

The HLS product [13] is a deliverable from the Satellite Needs Working Group that harmonizes data from NASA/USGS’s Landsat 8 and 9 and the ESA’s Sentinel-2A and -2B satellites to achieve a higher temporal resolution. HLS is compatible with the 40-year Landsat data record at 30-m spatial resolution but with a temporal resolution of two to three days on average. The data is framed into tiles measuring 109.8 × 109.8 km (3660 × 3660 pixels) in the UTM-based military grid reference system (MGRS) [13]. Fifteen visible and infrared bands are available in HLS, however, not all spectral bands are present in Sentinel and Landsat. Therefore, we used the six spectral bands common to both: blue, green, red, NIR, SWIR1, and SWIR2. This band combination will be referred to as the six-band HLS reflectance data.

Our sampling approach aimed at creating a high-quality dataset representing diverse land cover and ecosystems for robust model training, while minimizing cloud and missing data issues. To achieve this, we first calculated the proportion of LULC classes and ecoregions for each HLS tile using the Copernicus Land Cover 100 m [14] and RESOLVE Ecoregions [15] labels. Second, after merging the 12 closed and open forest classes into two classes, we sampled 100 tiles (full size of 3660 × 3660 pixels) per LULC class from the 500 tiles with the highest class proportion. Urban areas were over-sampled by selecting 1000 tiles that cover about 60% of the global urban areas. In addition, we included 1000 tiles with a high LULC class entropy to capture heterogeneous landscapes. Next, we ensured that the 846 ecoregions were represented if the region’s size allowed it, which is thresholded at 5% of tile area coverage. In total, 712 ecoregions are present in three or more tiles, while 68 are not included due to limited area coverage. We applied a 95%–5% training-validation split and dropped 133 sampled tiles due to quality issues or insufficient data coverage, e.g., in Greenland and Antarctica. This process resulted in 3028 training and 163 validation tiles. The LULC distribution of the final dataset is visualized in Fig. 1, showing that sea and bare vegetation (desert) classes were downsampled compared to all 18 000-HLS land tiles. Because we oversampled build-up areas, managed vegetation is also over-represented due to the geographical proximity.

Once we ensured that our selection included a diversified and representative set of tiles, the next phase of our dataset preparation aimed at optimizing both temporal and spatial coverage when sampling individual patches from the selected HLS tile IDs (i.e., the actual satellite images used in pretraining). This was particularly important to allow Prithvi-EO-2.0 to capture seasonal patterns and longer term changes. To achieve this, we built temporal sequences of four HLS images with intervals of one to six months between consecutive timestamps, spanning the period from 2014 and 2023. By enforcing a minimum separation between consecutive timestamps, we ensure that each sample contains images spanning a longer period of time, even with a relatively small sequence. However, the most relevant pattern changes might occur at different time scales across regions, and no timestamp selection strategy is optimal for the entire globe. Our approach guarantees at least monthly variations between images, which can highlight seasonal changes while avoiding overly similar consecutive images. Sequence length is another tradeoff: longer sequences increase the number of tokens to process and make pretraining more computationally expensive. Therefore, we used samples with four timestamps, as it leads to a reasonable token count while still gathering images from four different months.

The sequences were iteratively sampled from the selected HLS tiles until all candidates (minimum of four timestamps) were processed or 1500 samples per tile (250 for validation) were reached. Then, the sequences were split into nonoverlapping 256 × 256 patches with four consecutive timestamps. We discarded samples that contained more than 1% of missing value pixels in any band or more than 20% of cloudy pixels using the cloud and cloud shadow data contained in the Fmask band. Missing value pixels were filled using nearest-neighbor interpolation. We ensured that each 256 × 256 patch did not contain more than ten samples (two for validation) and randomly downsampled otherwise to avoid over-representing cloud-free areas and maintain spatial diversity.

Finally, all training samples that spatially overlapped any validation area were discarded. This patch-sampling strategy helped maintain high data quality while ensuring a comprehensive representation of different temporal and spatial contexts.

After preliminary pretraining experiments, we applied additional filtering to address data quality issues and keep stable training conditions. Specifically, HLS tiles from central Greenland with persistent artifacts were removed. We also downsampled full sea and desert regions due to their very low or high reflectance values to improve pretraining stability and avoid over-representation of homogeneous areas. Sea-only samples were filtered using the Fmask band, while desert samples were randomly subsampled from all desert tiles. The resulting pretraining dataset includes 4.2-M training and 46k validation samples of size 256 × 256 pixels, which are visualized in Fig. 2.

### B. Model Architecture and Pretraining

The pretraining process of our foundation model is based on the MAE approach [16], a self-supervised learning method widely used and extended for different data types, including video [17] and multispectral images [3], [11]. The MAE reconstructs masked images using an asymmetric encoder–decoder architecture with a vision transformer (ViT) backbone [18]. In detail, each input image is divided into nonoverlapping patches of the same size and the ViT encoder embeds the patches using a linear projection with added 2-D sin/cos positional embeddings. A subset of the patches is randomly masked and only the unmasked tokens are processed by the transformer blocks of the encoder [16]. The decoder receives the encoded visible patches and mask tokens, which are learned vectors representing a missing token to be predicted. Positional embeddings are added to the full set of tokens and sent to the decoder’s series of transformer blocks to perform the image reconstruction task [16]. The loss function is the mean squared error (mse) between the masked and predicted tokens in the pixel space [16].

Fig. 3 shows the overall MAE structure for pretraining Prithvi-EO-2.0, which modifies the original MAE in two ways. First, we replaced the 2-D patch embeddings and 2-D positional embeddings with 3-D versions to support inputs with spatiotemporal characteristics, i.e., a sequence of $T$ images of size $(H, W)$. Following approaches to adapt MAE to video processing [17], [19], our 3-D patch embeddings consist of a 3-D convolutional layer, dividing the 3-D input into nonoverlapping cubes of size $(t, h, w)$ for time, height, and width dimensions, respectively. These are image dimensions: number of images in the sequence and height and width in pixels. Unlike videos, satellite data can be acquired at nonregular and relatively low frequency in time (days), so we set $t = 1$ in our models. For the 3-D positional encodings, we first generate 1-D sin/cos encodings [16], [20] individually for time, height, and width dimensions and then combine them into a single 3-D positional encoding. The 1-D sin/cos positional encodings are defined as [20]

$$
\begin{aligned}
\mathrm{PE}_{\mathrm{pos},2i} &= \sin\left(\frac{\mathrm{pos}}{10000^{2i/D}}\right) \\
\mathrm{PE}_{\mathrm{pos},2i+1} &= \cos\left(\frac{\mathrm{pos}}{10000^{2i/D}}\right)
\end{aligned}
\tag{1}
$$

where $\mathrm{pos}$ represents the position, $i$ is the dimension, and $D$ is the embedding dimension size.

Second, we considered metadata on geolocation (latitude and longitude) and date (year and day-of-year ranging 1–365) in pretraining. The model receives time and location information for each sample (i.e., date for each image in the sequence and the center latitude and longitude) and encodes them independently. Latitude and longitude are encoded separately using the 1-D sin/cos strategy, similar to (1), and the resulting embeddings are concatenated together. The same is done for year and day-of-year.

The metadata encodings are added to the embedded tokens via a weighted sum with learned weights: one for time and one for location (see Fig. 3). This means that we let the model learn how the metadata should be added to the embedded tokens. Since this metadata is often not available, we decided to include it not as additional inputs in patch embeddings, but as a simple bias, similar to the idea of positional encodings. For the same reason, we also added a drop mechanism during pretraining that randomly drops the geolocation and/or the temporal data to help the model learn how to handle the absence of this information. Note that the metadata encodings are designed to inform the model about the sample’s general location (center coordinates) and corresponding timestamp, while only the 3-D positional encodings are responsible for conveying the positions of the tokens within the sample.

Using the architecture and MAE approach described, we developed Prithvi-EO-2.0 in two sizes, 300 and 600 M, based on ViT-L and ViT-H, respectively [18]. We trained versions with (`Prithvi-EO-2.0-*-TL`) and without (`Prithvi-EO-2.0-*`) temporal (T) and location (L) information. The models were trained for 400 epochs on A100 40-GB GPUs; for the 300-M models we used 80 GPUs (utilizing ~21 000 GPU-hours for the full training), while for the 600-M models, 240 GPUs (utilizing ~58 000 GPU-hours for the full training). The local batch size (i.e., the batch size per GPU) was set to 48 for ViT-L and 16 for ViT-H, to accommodate the larger model; a global batch size (local batch size multiplied by the number of GPUs) of 3840 was used for all models. We used a weight decay of 0.05 and a cosine scheduler with a maximum learning rate of $5 \times 10^{-4}$ and linear warmup for 40 epochs starting from a learning rate of $1 \times 10^{-6}$. For models with temporal and location data, we set the drop probability to 0.1. As described in Section III-A, the samples have shape 4 × 256 × 256 for time, height, and width, respectively, and we used random crop to 4 × 224 × 224 and random horizontal flips as data augmentation. The models were pretrained on the Booster partition of the JUWELS (Jülich Wizard for European Leadership Science) supercomputer [21] hosted at JSC.

### C. Evaluation

There are two key aspects to consider when evaluating the usefulness of a foundation model. The first involves benchmarking the model against published competitors using a standardized set of tasks, following a rigorous protocol that ensures fair comparison and reproducibility. The second focuses on assessing the model’s performance in real-world downstream tasks, comparing it to state-of-the-art methods in those domains.

For the benchmarking evaluation, we selected GEO-Bench [10], a widely used and rigorous benchmark framework available for EO foundation models.

As for the downstream evaluation, SMEs assessed the Prithvi-EO-2.0 models across multiple tasks in three categories of applications: disaster response, land cover and crop mapping, and ecosystem dynamics. The approaches adopted in each use case vary because of the different requirements and practices in their respective domains, reinforcing the importance of testing the model with a variety of real-world applications. The overall characteristics of the downstream tasks can be seen in Table I.

For classification tasks, we use accuracy as the evaluation metric, defined as

$$
\mathrm{Accuracy} = \frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}}
\tag{2}
$$

where TP, TN, FP, and FN denote the number of true positives, true negatives, false positives, and false negatives, respectively. For segmentation tasks, we use the mean intersection over union (mIoU) as the evaluation metric. It measures the average overlap between predicted and ground truth regions across all classes, defined as

$$
\mathrm{mIoU} = \frac{1}{C}\sum_c^C \frac{\mathrm{prediction}_c \cap \mathrm{truth}_c}{\mathrm{prediction}_c \cup \mathrm{truth}_c}
\tag{3}
$$

where $C$ is the total number of classes and $\mathrm{prediction}_c$ and $\mathrm{truth}_c$ denote the predicted and ground truth regions for class $c$, respectively. For some tasks, we also report the precision, recall, and F1-score, defined as

$$
\mathrm{Precision} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}
\tag{4}
$$

$$
\mathrm{Recall} = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}
\tag{5}
$$

$$
\mathrm{F1\text{-}Score} = \frac{2\mathrm{TP}}{2\mathrm{TP}+\mathrm{FP}+\mathrm{FN}}.
\tag{6}
$$

In Sections III-C1–III-C4, we provide a detailed description of the benchmarking protocol and the downstream tasks for each of the three application categories (disaster response, land cover and crop mapping, and ecosystem dynamics). We highlight that all fine-tuning experiments conducted in this work require a single GPU.

#### 1) Benchmarking

GEO-Bench offers a carefully curated collection of six classification and six semantic segmentation datasets [10], encompassing a range of spatial resolutions and domains (see Table II). In addition, it establishes an evaluation protocol [10] designed to enable fair and reproducible comparisons across models. This protocol begins with hyperparameter tuning, where each model is allowed a fixed number of trials (ten in our study) on each dataset. The best hyperparameters identified on the validation set for each task are then used to conduct repeated experiments (N = 10) with different random seeds. Repeating the experiments accounts for the inherent randomness in training AI models, thereby enabling more robust and reliable comparisons of results.

We added the GEO-Bench datasets to TerraTorch and used its companion library TerraTorch-iterate[^5] to perform the hyperparameter tuning search via Bayesian Optimization in Optuna,[^6] as well as the repeated experiments. We compare Prithvi-EO-2.0 against six of the most popular and performant EO foundation models recently released for optical data (see Table III), as well as the earlier version of Prithvi trained with data only from the U.S. released last year [9]. For classification tasks, all models were paired with a linear layer, while we used a U-Net architecture [22] for ResNets and UPerNet [23] decoder for transformer-based architectures, which represent the most adopted choices for these types of architectures. Hyperparameter tuning was done across the same search space that included learning rate, decoder depth, and weight decay. For comparability, the batch size was fixed to a reasonable value for each dataset for all models. Finally, we used only the multispectral sensors from each dataset to conduct our benchmarking experiments. For each model, we utilized the specific spectral bands it was pretrained on. For example, if a model was pretrained on RGB images and the dataset contains all Sentinel-2 bands, only the RGB bands were provided. We use the same data augmentation techniques (random horizontal and vertical flips) for all models and datasets. Also, all images were uniformly resized to 224 × 224 pixels.

To conduct the benchmark comparison, we computed the mIoU for the segmentation tasks and the overall accuracy (micro-averaged accuracy) for the classification tasks; the exception is the m-big-earthnet dataset, which is a multilabel classification task, and we used the micro-averaged F1 score. For each GFM evaluated, we averaged those metrics to obtain an aggregated measure of each model’s performance, grouping them in classification, segmentation, and combined tasks. While these metrics are different in nature, they range between 0 and 1. Therefore, we believe this procedure is appropriate to get an overall performance picture across the GEO-Bench datasets.

#### 2) Disaster Response

##### a) Flood Mapping

Sen1Floods11 [24] is a surface water dataset including labels for water and land, and related Sentinel-1 and Sentinel-2 imagery. The dataset consists of 446 512 × 512 images covering 14 biomes, 357 ecoregions, and 6 continents of the world across 11 flood events between 2018 and 2020. The dataset and a reference training and evaluation code are available on GitHub.[^7] This dataset was used for testing Prithvi-EO-1.0, where the model showed beyond-state-of-the-art performance [9]. Here, we compare it with the newer Prithvi-EO version.

The 512 × 512 images were resized to 448 × 448 as the first is not divisible by the patch size of the 600-M models (14 × 14). This guarantees that all models are trained and validated with the uncropped and unpadded images. To increase data variability, random vertical and horizontal flips were applied as part of the data augmentation process. The associated masks present two categories: 0 for land and 1 for water. For all models, we used a UPerNet [23] decoder and tuned hyperparameters with TerraTorch-iterate (ten trials, tuning weight decay and learning rate). Then, we repeated the training with the best validation hyperparameters ten times with different seeds and reported results on the test set. The loss used was cross-entropy and the models ran for 50 epochs with early stopping patience set to 20 epochs. We used the same six bands as in the pretraining set.

For this task, we report the mIoU and the IoU for the water class. In addition, we provide the micro-averaged F1 score.

##### b) Wildfire Scar Mapping

The wildfire scars dataset contains shapefiles of both intentional and wildfires burning from 2018 to 2021 as described in [9]. This dataset[^8] was also used for testing Prithvi-EO-1.0, where the model showed state-of-the-art performance [9]. Therefore, we compare it with the newer Prithvi-EO version.

The 512 × 512 images were also resized to 448 × 448, as explained in Section III-C.2a. For data augmentation, we used random vertical and horizontal flips along with random crop to 224 × 224. The corresponding masks show 0 for unburnt areas and 1 for burned areas. We used an UPerNet decoder [23] and ran hyperparameter tuning with TerraTorch-iterate for all models (ten trials, tuning weight decay and learning rate). The training with the best validation hyperparameters was repeated ten times with different seeds, and the results are reported on the test set. We used cross-entropy as loss and set maximum epochs to 50, with early stopping patience of 20 epochs.

In this case, we report the mIoU, the IoU for the burn scar class, and the aggregated F1 score.

##### c) Burn Intensity Mapping

We collected burn scar intensity data using paired HLS imagery and burn scar intensity classifications from burned area emergency response (BAER) [25], which evaluates fire impacts on vegetation, soil, and watershed functionality. BAER teams rapidly analyze postfire conditions to stabilize affected landscapes and mitigate hazards.

The dataset includes 5692 images capturing spatial burn scar data and top-of-atmosphere (TOA) reflectance values across three temporal stages: preburn, during-burn, and postburn. The data was collected from 2018 to 2023, over the western CONUS (126°W to −104°W, 32.5°N to 48°N). Burn scar intensity classifications, ranging from 0 (no burn) to 4 (high severity), were derived from burn severity analysis (see Fig. 4). The HLS imagery was carefully selected to match the temporal criteria for prefire and postfire stages, ensuring that changes in burn intensity and reflectance values were accurately captured. Each fire event is represented by paired 224 × 224 images: one for burn scar intensity and another for TOA reflectance across six spectral bands (blue, green, red, NIR, SWIR1, and SWIR2). The images were visually inspected to confirm burn scar visibility and cloud-free conditions. The dataset was further refined by excluding entries with more than 25% missing or zero values, ensuring high-quality data for training AI models. The dataset’s design ensures reproducibility and usability for wildfire monitoring and environmental research.

Out of the 5692 224 × 224 images, 80% were used for training and 20% for testing. The architecture for this task consisted of the Prithvi encoder along with an UperNet decoder. The model was trained for 50 epochs using a parameter-efficient fine-tuning technique called Low-Rank Adaptation, or LoRA [26], with weighted cross-entropy (wCE) as the loss function. We set the learning rates to $5 \times 10^{-4}$ (encoder) and $5 \times 10^{-5}$ (decoder), with a cosine annealing schedule, weight decay of 0.05 and random horizontal flips for data augmentation. As baseline for comparison, we used a regular U-Net [22] and a larger U-Net version with a ResNet-50 backbone. For this use case, we provide the mIoU along with per class IoU.

##### d) Landslide Detection

The Landslide4Sense (L4S) dataset [27] is a comprehensive benchmark for large-scale landslide detection research, utilizing multisource satellite imagery to study landslide-affected areas globally from 2015 to 2021. It includes 14 data layers: Sentinel-2 multispectral bands (B1–B12), a digital elevation model (DEM), and slope data from ALOS PALSAR [27]. All layers are resized to a resolution of 10 m/pixel and labeled at the pixel level as landslide or nonlandslide; the images have 128 × 128 pixels of size. The dataset is divided into training, validation, and test sets, covering diverse mountainous regions worldwide. The training data comes from four sites: Iburi-Tobu (Hokkaido), Kodagu (Karnataka), Rasuwa (Bagmati), and western Taitung County, comprising 3799 image patches. The validation and test sets include 245 and 800 images, respectively.

To fine-tune the Prithvi-EO-2.0 models, we incorporated a decoder consisting of four deconvolutional layers, along with layer normalization and activation functions, to map the model outputs from embeddings back to the original input image size. A final set of two convolutional layers was then applied to project the latent space to class probabilities. For the Prithvi-EO-2.0-600M configuration, which uses a patch size of 14 × 14, this decoder architecture does not allow for the perfect restoration of embeddings to the input image size. To address this issue, we added a bilinear interpolation layer following the final convolutional layers to resize the output and ensure it matches the original input image dimensions.

The models were fine-tuned using the data splits described above. Six-band HLS reflectance images were selected and upsampled to 224 × 224 to match the configuration of the Prithvi-EO-2.0 backbone. Data augmentation was applied by randomly flipping images both vertically and horizontally. We considered two different loss functions: wCE loss, with a weighted ratio of 2:8 for negative and positive pixels, and Lovasz loss [28]. Gradient descent was performed using the Adam optimizer with a learning rate of $1 \times 10^{-5}$. In addition, a cosine learning rate scheduler with warm-up and restart [29] was utilized to enhance model convergence. The models were trained for 100 epochs with a batch size of 8, and the checkpoints with the lowest validation loss were selected for evaluation.

For this task, U-Net [22] and U-Net++ [30] were used as baselines models for comparison, both with a ResNet50 as the backbone. These are popular and powerful models that have been used to support a wide range of environmental mapping tasks, including landslide mapping [27], [31], [32]. It is worth noting that this dataset was also used in the 2022 Landslide4Sense competition, with several winning models reported by [27]. However, those results were based on customized training strategies, such as self-training using test data, pseudo-label refinement, and ensemble methods. In contrast, our study focuses on evaluating the performance of the Prithvi-EO-2.0 models on the L4S task and comparing it with existing deep learning models under a standardized training protocol (i.e., consistent data splits, augmentation techniques, and training platforms) to ensure a fair comparison.

We evaluated model performance under two fine-tuning data regimes: using the full training set and a reduced subset comprising approximately 1% of the full data. The latter allows us to assess the models’ few-shot learning capabilities. Three evaluation metrics were considered: mIoU, F1 score, and micro-averaged accuracy (mAcc).

#### 3) Land Cover and Crop Mapping

##### a) Multitemporal Crop Segmentation in the United States

The crop segmentation task was one of the datasets used to evaluate Prithvi-EO-1.0, where the model showed state-of-the-art performance [9], [33]. In this work, we compare it with the newer Prithvi-EO version. We also include a U-Net as an additional baseline model for this task.

The 224 × 224 images were used for both training and validation without cropping. To enhance data variability, random vertical and horizontal flips were applied as part of the data augmentation process. The corresponding masks contain thirteen classes: 1) “natural vegetation,” 2) “forest,” 3) “corn,” 4) “soybeans,” 5) “wetlands,” 6) “developed/barren,” 7) “open water,” 8) “winter wheat,” 9) “alfalfa,” 10) “fallow/idle cropland,” 11) “cotton,” 12) “sorghum,” and 13) “other.”

For fine-tuning, we used the wCE as the loss function. All Prithvi-EO encoders were combined with a simple segmentation decoder consisting of convolutional and upsampling blocks, and trained for 80 epochs. Besides the mIoU, we also provide the aggregated accuracy for all models.

##### b) Multitemporal Land Cover and Crop Classification in Europe

Sen4Map [34] is a benchmark dataset designed for multitemporal land-cover and crop classification tasks with Sentinel-2 satellite data. Sen4Map comprises 335 125 time series of 64 × 64 pixels multispectral images, extracted from Sentinel-2 tiles and annotated with geolocated land-cover data collected through extensive in situ surveys using LUCAS points [35]. The dataset includes time series of varying lengths from 2018, covering countries across the European Union. We utilized the monthly composites, feeding the models with time series of length 12, in line with the original approach [34]. The spatial resolution of the images in Sen4Map is natively 10 m or upsampled to 10 m from the native 20-m resolution, depending on the band. Each image covers an area of 640 × 640 m, which contrasts with our pretraining dataset, where the images are 224 × 224 pixels with a resolution of 30 m, covering approximately 6720 × 6720 m—over 100 times the area of the Sen4Map samples.

The patch-processing methodology further compounds the fine-tuning challenge. In Sen4Map, the original 64 × 64 pixel images are cropped to smaller 15 × 15 regions to focus on the central pixels, around the available label from LUCAS. This ensures that classification is based solely on the area of interest, minimizing the influence of irrelevant spatial context. We adopted a similar setup to maintain a fair comparison. However, 15 × 15 pixels is comparable to the Prithvi-EO patch sizes, which means that the input image would have a single patch. Hence, to avoid changing the model’s patch size and train the patch-embedding layer from scratch, the 15 × 15 patches were upscaled to 224 × 224 pixels.

In addition to differences in spatial resolution and image size, the datasets vary in the spectral bands. The pretraining dataset includes six bands from HLS data, while the Sen4Map dataset provides four additional bands (NIR-Broad, Red-Edge 1, 2, and 3). The differences in spatial, spectral, and contextual characteristics can imply a greater degree of adaptation for the Prithvi models, potentially extending or complicating the fine-tuning process.

We fine-tuned the original Prithvi-EO-1.0-100M model, Prithvi-EO-2.0-300M, and Prithvi-EO-2.0-600M, on different ratios of the Sen4Map training data. We used the weighted F1 score to compare them with the baseline ViViT [36] adopted in Sen4Map, which was recreated to be trained from scratch on the data subsets.

##### c) Multitemporal Crop Segmentation With PASTIS

The PASTIS dataset contains 2433 sequences of 128 × 128 multi-spectral images, from four regions in France. Sequence lengths range from 38 to 61 frames, collected at irregular intervals between September 2018 and November 2019. The samples include ten channels from Sentinel-2’s nonatmospheric bands, resampled to a 10-m resolution. The dataset provides segmentation labels for 18 crop types plus a background class and it is highly imbalanced: the most frequent classes appear over 50 times more often than the rarest. The authors estimate that about 28% of the images have some cloud cover [37].

Given the large and variable sequence lengths, we standardized them to 20 frames per sample. The sequences were divided into 20 equal-width temporal bins, and one image was randomly selected from each bin. This strategy ensures coverage across the entire sequence, better preserving temporal diversity, which could be compromised with simple truncation or random sampling. The frame selection was fixed for validation and test. In addition, we removed samples with high cloud coverage as it was beneficial for all tested models.

We compared Prithvi-EO-2.0 with the PASTIS baseline, U-TAE [37] (a U-Net architecture enhanced with temporal attention mechanisms), and also with other foundation models: Satlas [8], DOFA [6], and Presto [4].

All models were fine-tuned with the same procedure. Data augmentation included random resized cropping, horizontal flipping, and rotation. The dataset followed the original split [37]: folds 1–3 for training, 4 for validation, and 5 for testing. Each GFM was paired with a UPerNet decoder [23], and fine-tuned with 100% and 10% of the training data.

Since Satlas and DOFA do not process image sequences, frames were passed independently through their backbones, and the features were concatenated. Except for Presto, the GFM encoders were connected to a lightweight temporal attention encoder (LTAE) [38] followed by a temporal aggregator [38] before the UPerNet decoder. With long input sequences, these models generate a large number of tokens, and directly connecting them to the UPerNet would have resulted in a substantial increase of decoder parameters, hindering training and efficiency.

The GFMs were trained using LoRA [26], cross-entropy loss, and the AdamW optimizer, with different learning rates for the encoder and decoder: $5 \times 10^{-4}$ and $5 \times 10^{-5}$, respectively. We set the weight decay to 0.05 and trained the models for 50 epochs with early stopping (patience of 10 epochs). The mIoU was used as the evaluation metric.

#### 4) Ecosystem Dynamics

##### a) Above Ground Biomass (AGB) Estimation

AGB is a crucial climate variable that encompasses all living biomass above the soil, essential for understanding land cover/use changes and carbon sinks. Although direct measurement of AGB is challenging, remote sensing methods and machine learning techniques can be used to estimate it, providing comprehensive spatial and temporal data. The BioMassters dataset was generated to explore deep learning approaches for predicting yearly AGB in Finnish forests using multimodal, multitemporal Sentinel-1 and Sentinel-2 satellite data from 2016 to 2022 [39]. The dataset comprises 11 462 AGB reference images, each paired with 12 months of corresponding satellite imagery, covering 2560 × 2560 m forest patches, with AGB measured in metric tons per pixel and derived from LiDAR data calibrated with in situ measurements. The winning model from the BioMassters data challenge was used as the baseline for comparison with Prithvi-EO-2.0. This model is based on a U-Net architecture with temporal attention encoding [37], using all 12 timestamps and all 15 bands from Sentinel-1 and Sentinel-2 imagery as inputs for each yearly AGB prediction. It achieved an RMSE of 27.49 in the holdout test set.

The dataset was divided into 80% training and 20% validation sets for consistent experimental use. Also, we tested different input configurations given the differences between the BioMassters dataset and Prithvi-EO pretraining data: the first includes 12 observations of Sentinel-1 and -2 data for each target AGB image, while the second considers four frames from HLS data. The configurations include:

1. 6-band Sentinel-2, 4 frames;
2. 6-band Sentinel-2, Sentinel-1, 4 frames;
3. 6-band Sentinel-2, 12 frames;
4. 6-band Sentinel-2, Sentinel-1, 12 frames; and
5. 11-band Sentinel-2, Sentinel-1, 12 frames.

Where the six bands are the same as used in the HLS pretraining data and the four timestamps were chosen out of 12 based on the quality of the Sentinel-2 data, prioritizing scenes with no missing data, followed by scenes with the lowest cloud cover. The highest performing configuration was then selected as the subject of subset training, where performance of the model was tested when trained on subsets of 50%, 20%, 10%, and 5% of the original training set.

We fine-tuned the Prithvi-EO-2.0-300M encoder paired with an FCN decoder and a regression head. We used the AdamW optimizer, with a learning rate of $6 \times 10^{-5}$ and weight decay of 0.05. As data augmentation, random flips and rotations were applied. For the cases using the 6-band Sentinel-2 data, we experimented with the efficient fine-tuning technique LoRA [26]. In the experiments utilizing Sentinel-1 data, we included the ascending and descending VV, VH, and RVI bands.

##### b) Estimation of Gross Primary Productivity (GPP) at Globally Distributed Sites

Photosynthesis (GPP), the critical process converting solar radiation into energy and materials that sustain life, represents the largest global carbon cycle flux, yet remains challenging to quantify accurately without direct observation [40]. Data-driven approaches using machine learning to integrate satellite data with site-level information (e.g., from eddy covariance measurement networks [41]) provide diagnostic constraints on global GPP, complementing process-based models [42]. However, these approaches face challenges due to scale mismatches between in situ measurements and satellite data, as well as generalization issues, which could potentially be mitigated by using foundation models like Prithvi-EO that embed generalized representations of high-resolution data [43].

This downstream application aims to evaluate the potential of Prithvi-EO-2.0 to estimate GPP at globally distributed eddy covariance sites. We utilized daily GPP data from 37 eddy covariance flux towers, obtained from FLUXNET [44], AmeriFlux,[^9] and ICOS [45] networks. We use datasets processed by the ONEFLUX pipeline for high-quality and consistent data. The target variable for analysis is the GPP estimate derived from net ecosystem exchange (NEE) measurements using the nighttime approach (`GPP_NT_VUT_REF`). We selected daily GPP data with at least 60% of high-quality hourly or half-hourly data for temporal aggregation. The latitude and longitude of the flux tower sites were recorded to retrieve HLS and MERRA-2 data from corresponding locations. For HLS, the recorded coordinates define the center of the images, while for MERRA-2 variables, the nearest grid point is used.

The dataset combines three primary components: 1) HLS six-band reflectance data organized as 50 × 50 × 6 pixels (TIFF files); 2) 10-D modern-era retrospective analysis for research and applications version 2 (MERRA-2) atmospheric and land surface variables capturing environmental conditions; and 3) daily GPP measurements derived using the night-time partitioning approach. HLS and MERRA-2 data are centered on flux tower locations. The GPP data span 37 globally distributed flux tower sites from 2018 to 2021, encompassing 975 samples. MERRA-2 variables include minimum, maximum, and mean temperatures, soil moisture, heat flux, radiation, precipitation, and other key environmental metrics, identified using the codes M2T1NXSLV and M2T1NXLND.

The dataset preparation process involves meticulous filtering and quality checks. HLS data are preselected based on a 25% maximum cloud threshold and 75% minimum spatial coverage threshold, with further filtering to remove scenes with >2% snow cover and >5% cloud cover. HLS reflectance values are scaled accordingly. MERRA-2 data are aggregated as daily mean values for each flux site. Instances with GPP values $\leq -0.1\,\mathrm{g\,C\,m^{-2}\,s^{-1}}$, indicative of poor data, are removed. Corresponding HLS and MERRA-2 inputs for each GPP record are matched, and additional filters exclude data with spatial mean enhanced vegetation index (EVI) values ≤ −0.1 across images, which signal snow or cloud contamination. This dataset provides a high-quality, integrated framework of remote sensing and ground observations for studying GPP dynamics under diverse environmental conditions.

The fine-tuning architecture developed for this task (see Fig. 5) combines the Prithvi-EO-2.0 encoder, which receives the six-band HLS reflectance data, with a simple convolutional network that processes the ten input features from MERRA-2. This approach is designed to facilitate extending the Prithvi-EO-2.0 HLS representation with additional environmental variables to predict GPP values at flux tower sites. More specifically, the multispectral HLS input is passed through the pretrained and frozen Prithvi-EO-2.0 encoder to generate latent HLS representations (Prithvi embeddings) of the flux observation sites. These embeddings are then passed through a lightweight decoder composed of two linear layers with ReLU activation. The MERRA-2 input features are transformed in parallel via a separate branch consisting of three 2-D convolutional layers with ReLU activations followed by a linear layer. The Prithvi embeddings and the MERRA-2 latent representation are both flattened, then concatenated and regressed to predict the GPP values using a linear layer. The models are trained by minimizing the mse loss between the predicted GPP and the true GPP. Data splitting for training and evaluation follows a leave-one-year-out cross-validation approach, where three years are used for training and one for testing to reduce the challenges posed by the relatively small dataset size.

We experimented with all variants of Prithvi-EO-2.0, and quantify the models’ skill in predicting GPP using the coefficient of determination, $R^2$ measure, between the predicted and the true GPP values. Prithvi-EO-2.0 is compared against three baseline models based on random forest, XGBoost, and ResNet18. The random forest and XGBoost models use the spatial average of HLS bands across each image and the MERRA-2 data, representing the state-of-the-art approaches [43]. These models also incorporate vegetation indices, including EVI, normalized difference vegetation index (NDVI), normalized difference water index (NDWI), green chlorophyll index (GCI), near-infrared reflectance of vegetation (NIRv), and kernel NDVI. The ResNet model uses the same inputs as Prithvi-EO-2.0.

## IV. Results and Discussion

In this section, we provide and discuss the results of the evaluation experiments. We begin with the benchmarking results followed by the three categories of downstream tasks.

### A. Benchmarking

Fig. 6 shows the aggregated results of benchmarking with GEO-Bench datasets, including the average performance across the classification and segmentation datasets, as well as the overall performance across all 12 datasets. The results indicate that for the classification tasks, DOFA [6], Prithvi-EO-2.0-600M-TL, and Prithvi-EO-2.0-600M are the top-performing models. For segmentation, Prithvi-EO-2.0-600M-TL and Prithvi-EO-2.0-600M show the highest performance, with a noticeable margin over the next best models, DeCUR [7] and DINO [12] ResNets. Overall, Prithvi-EO-2.0-600M-TL and Prithvi-EO-2.0-600M obtained the best combined performance across all 12 datasets. Also, all versions of Prithvi-EO-2.0 performed better than their predecessor Prithvi-EO-1.0 highlighting the improvement of the new version of the model.

Fig. 7 provides a more detailed view of the distribution of the ten repeated experiments for each model across the different tasks. For some datasets, multiple models perform equally well, with accuracies ≥ 97% (e.g., m-brik-klin or m-pv4ger). Among the remaining datasets, Prithvi-EO-2.0-600M-TL and Prithvi-EO-2.0-600M outperformed other models in four out of six tasks targeting medium resolution imagery (i.e., Sentinel-2 at 10 m). In particular, tasks such as m-bigearthnet and m-SA-crop-type show better results from all versions of Prithvi-EO-2.0-600M and Prithvi-EO-2.0-300M compared to the other models. This is noteworthy because these tasks involve EO applications like land use classification using the CORINE Land Cover product [46], heavily focused on forest and crop classification, which are tasks associated with strong seasonality. The strong performance of Prithvi-EO-2.0-600M-TL highlights the importance of designing models capable of learning relevant multitemporal features useful for key remote sensing tasks.

In Fig. 7, we can also observe that several models show a wide range of scores on the m-cashew-plant dataset. This variation is related to the presence of seven classes in the training and validation sets, while the test set only contains six: class 0 is absent. When a model correctly avoids assigning any pixel of the test set as class 0, that class is excluded from the average IoU calculation. However, if a model does predict class 0, it becomes part of the average computation, which lowers the aggregated score.

The performance comparison across models revealed four key insights. First, the benefits of using a larger, global dataset are evident after comparing the performance of Prithvi-EO-2.0-100M and Prithvi-EO-1.0-100M. Both models have identical architectures and model sizes, but the former was pretrained on the larger dataset and showed a 3% improvement on the overall GEO-Bench score, with differences that are even larger for some of the tasks. Second, increasing the number of parameters correlated with better performance, evidenced in larger Prithvi-EO-2.0 models performing better than smaller models. Third, the models incorporating temporal and location embeddings had a higher overall performance compared to their non-TL counterparts, which is especially interesting considering that not all datasets included in GEO-Bench contain temporal and location information. Finally, Prithvi-EO-2.0 showed good performance on high-resolution tasks, despite being pretrained only with 30-m data. This improved performance on higher resolution tasks shows the versatility of our model for multiresolution applications, including those that are more typical in computer-vision tasks, such as tree crown identification or cattle tracking using drone imagery.

### B. Disaster Response

#### 1) Flood Mapping

Table IV shows the results of our experiments on the test set of the Sen1Floods11 dataset. Prithvi-EO-2.0 improves over its previous version. Given the unbalanced nature of this dataset, where the land class is predominant and easily identifiable, improvements in the average metrics are not substantial. However, we observe a clear difference when comparing the IoU for the water class between Prithvi-EO-1.0-100M and the new versions, with Prithvi-EO-2.0-600M-TL achieving an IoU 3.5 points higher than its predecessor.

#### 2) Wildfire Scar Mapping

Table V presents the performance of the models on the wildfire scar mapping test set. We notice similar trends to those observed in the flood detection task, with the new versions of the model outperforming Prithvi-EO-1.0. Once again, the differences become more evident when focusing on the IoU for the wildfire scar class, where the gap between the previous version of the model and Prithvi-EO-2.0-600M-TL is 5.6 points, indicating the improved capabilities of our new models.

#### 3) Burn Intensity Mapping

In Table VI we present the results of the burn intensity predictions on the test set. The results showed that both Prithvi-EO-2.0 models outperform the U-Net versions in terms of mIoU. Interestingly, although the mIoU is generally low for all models, they seem capable of distinguishing unburnt from burned areas, with $\mathrm{IoU}_0$ above 67%. Prithvi-EO-2.0-600M achieves the higher IoU for class 0 (75.9%), representing a significant improvement over the U-Net models. However, all models seem to struggle to differentiate between the various severity classes, with the Prithvi models demonstrating better overall performance. We believe this might be linked to two data-related aspects. The first is that a number of samples shows a high coverage of smoke in the “during” image, introducing noise the models must learn to filter out. The second is related to the label masks: they show discontinuity and a general pattern where very small regions of higher severity classes appear within a larger, more continuous regions of lower severity classes. These characteristics can be challenging for models with larger patch sizes, such as the Prithvi models. The U-Nets, on the other hand, despite having access to pixel-level information and typically showing better capabilities in capturing more local patterns, were unable to accurately distinguish the burn-severity classes.

#### 4) Landslide Detection

Table VII shows the results for the full training set of the L4S task, where only the configurations yielding the best performance for each model are shown. From the results, Prithvi-EO-2.0-300M, trained with Lovasz loss, outperformed both U-Net models in terms of mIoU, F1 score, and precision by a noticeable margin. Prithvi-EO-2.0-600M, trained with wCE loss, exhibited a slightly lower mIoU of 70.4% and an F1 score of 58.6%, but achieved a higher recall than Prithvi-EO-2.0-300M. In summary, Prithvi-EO-2.0-300M demonstrated the best overall performance based on mIoU and F1 score, while Prithvi-EO-2.0-600M showed a higher recall but sacrificed precision.

In Table VIII, we present the results for models trained on a small subset of the training data (only 50 images). As expected, training on such a small subset led to performance degradation across all models, but the degree of decline varied. Both U-Net and U-Net++ experienced significant performance drops. For instance, U-Net’s mIoU decreased from 70.4% to 59.7%, and its F1 score fell from 59.7% to 35.0%. U-Net++’s performance declined even more sharply, yielding a very low recall score (16.9%). In contrast, Prithvi-EO-2.0-300M and Prithvi-EO-2.0-600M showed more stable performance. Although both models experienced some performance drops, they were considerably smaller than those observed for U-Net and U-Net++. Overall, Prithvi-EO-2.0-600M consistently achieved the best results among all models in the small sample set evaluation. This highlights the advantages of large GFMs in learning generalizable patterns from large-scale datasets, as well as the benefits of specialized pretraining on EO data.

We also selected three pairs of segmentation results from the top-performing Prithvi and U-Net models to conduct a visual comparative analysis of segmentation performance, using sensitivity and specificity statistics. Fig. 8(a) illustrates the results of U-Net and Prithvi-EO-2.0-300M, both fine-tuned on the full training dataset, while Fig. 8(b) shows the results for U-Net and Prithvi-EO-2.0-600M, fine-tuned on the smaller subset with 50 images.

From Fig. 8(a), we notice that Prithvi-EO-2.0-300M exhibits a more conservative detection approach, with fewer False Positives (blue) but a broader coverage of true positives (green), capturing the target regions with higher accuracy. However, it shows a slightly higher incidence of false negatives (red) in some cases. In contrast, U-Net results in more false positives (blue), leading to a lower accuracy and an overall lower F1 score. This indicates that Prithvi-EO-2.0-300M prioritizes detection accuracy by effectively reducing false positives. While this approach may potentially sacrifice recall in certain areas, it achieves the best predictive performance among all models when the full L4S dataset is used.

Fig. 8(b) reveals a different pattern in the segmentation results of U-Net and Prithvi-EO-2.0-600M. U-Net tends to produce more false negatives, often missing parts of the target regions, resulting in a decrease in recall. Prithvi-EO-2.0-600M, in comparison, shows stronger performance with the detection of substantial true positives across the target regions, although it it tends to generate more false positives, lowering precision compared to when the full training dataset is used. Overall, Prithvi-EO-2.0-600M remains strong when trained with a small sample size, benefiting from its enhanced model capacity to generalize to unseen locations effectively, even with limited training data, prioritizing sensitivity and reducing under-segmentation compared to U-Net.

### C. Land Cover and Crop Mapping

#### 1) Multitemporal Crop Segmentation in the United States

The results in Table IX for the crop segmentation task in the United States show that all Prithvi-EO models outperform the U-Net model in terms of mIoU. Furthermore, the Prithvi-EO-2.0 versions achieved considerably higher mIoU and mAcc values compared to their predecessor. Among all the Prithvi models, the 600-M variant achieved the best performance, with a mIoU of 50.7% and mAcc of 68.8%. These results indicate that Prithvi-EO-2.0 was able to capture changes over time in the three-frame inputs required to correctly identify the crops.

#### 2) Multitemporal Land Cover and Crop Classification in Europe

Table X presents the results for the land cover classification task in Europe. In terms of weighted-averaged F1 score, all Prithvi-EO models outperform the baseline ViViT, with significant margins considering the smaller data subsets. Compared to the other models, Prithvi-EO-2.0-600M consistently demonstrates superior performance across all data availability scenarios. In addition, our new versions of the model surpass Prithvi-EO-1.0 performance.

Table XI depicts results on the crop type classification task, where the Prithvi models also outperform the baseline. In this case, Prithvi-EO-2.0-600M achieves F1 scores comparable to Prithvi-EO-2.0-300M, showing marginally better results on two data ratios and slightly lower performance on the other three. Both models demonstrate superior performance compared to Prithvi-EO-1.0-100M.

It is worth noting that even though the Prithvi-EO models were pretrained with samples containing four frames, they show robust performance on the Sen4Map tasks, which comprise 12-frame input samples. This indicates they can effectively handle larger time-series inputs.

#### 3) Multitemporal Crop Segmentation With PASTIS

Table XII shows the results for our experiments with the PASTIS dataset, considering 100% and 10% of the training data. Prithvi-EO-2.0-600M achieved the highest mIoU in both scenarios, followed by the baseline model. As expected, all models experienced a significant drop in performance when trained on only 10% of the data, which corresponds to approximately 200 images.

DOFA and Satlas present lower scores compared to the baseline, which indicates that the lack of temporal modeling in the architectures and pretraining datasets may limit their ability to handle long sequences. In contrast, Presto showed the worst results. We attribute this to the input image size, which may be large for a model originally designed for single-pixel time-series data.

These results suggest that Prithvi-EO-2.0 was able to learn with long sequences, better capturing the temporal patterns compared to the other GFMs, highlighting the value of its pretraining data and architecture.

### D. Ecosystem Dynamics

#### 1) AGB Estimation

Table XIII shows the test set results for Prithvi-EO-2.0-300M and the baseline U-Net. The best performance for Prithvi-EO is achieved using 12 timestamps of Sentinel-2 MSI as inputs and LoRA. Performance for the same model fine-tuned on 5% of the training set (348 images) only differs by 10.36% from the best result on the full training set (6951 images), as seen in Table XIV.

Fig. 9 shows the $R^2$ scores of the best performing Prithvi-EO-300M and the baseline model across all AGB targets in the test set. The baseline model exhibits a tighter distribution around the identity line and more accurate predictions of high AGB values at the range 300–400. However, both models underestimate higher AGB values (>400).

A qualitative comparison of selected outputs depicted in Fig. 10 reveals that the baseline model and fine-tuned Prithvi generate visually similar outputs for some input scenes. Both models produce smoother predictions than the observed AGB values. The baseline model appears to predict higher AGB values more accurately and with more granularity than the fine-tuned Prithvi-EO model.

This result is consistent with existing findings that a combination of SAR and multispectral imagery is superior to multispectral imagery alone for biomass estimation, especially in locations with high biomass [39], [47]. Optical data is prone to saturation in high biomass regions where reflectance values no longer increase proportionally with biomass. This is because multispectral sensors are only capable of sensing the reflectance of the top layer of the canopy, and so cannot be used to accurately estimate the biomass of vegetation obscured by a full canopy. In these regions, SAR sensors are capable of providing information about the physical structure of vegetation because their microwave signals can penetrate the canopy and interact with branches, stems, and trunks. This penetration capability gives SAR the ability to sense the vertical and structural variability of biomass, which is not directly captured by optical multispectral sensors.

Our results show that Prithvi approaches the performance of multimodal models on this task using solely multispectral imagery, and is capable of adapting to and benefiting from longer time series of inputs than used in pretraining. This is achieved with an efficient fine-tuning technique, lowering training time and cost. Incorporating SAR inputs as additional bands to the Prithvi-EO encoder did not result in increased performance for biomass estimation in our experiment setting. We note that adapting to the new SAR inputs can be challenging for Prithvi-EO given the fundamental differences between optical and SAR data. Therefore, other methods of incorporating different modalities, such as fusing outputs of a separate SAR encoder with the outputs of the pretrained Prithvi-EO encoder, could improve performance for this task.

#### 2) Estimation of GPP at Globally Distributed Sites

We provide the $R^2$ values on the GPP estimation task for all tested models in Table XV. The $R^2$ performance in each train test split across all years is shown in Fig. 11. The results show that Prithvi-EO-2.0 models performed better than the random forest and XGBoost models without vegetation indices with up to 20% improvement on $R^2$. The Prithvi-EO-2.0-600M-TL version achieved the highest scores among all models across all testing years. Notably, while including vegetation indices marginally increased the performance of random forest and XGBoost models, Prithvi-EO-2.0 does not use VIs as inputs. This indicates the superior ability of Prithvi-EO-2.0 to efficiently utilize spatio-spectral information.

Both random forest and XGBoost baselines use spatial averages of HLS image tiles (1.5 × 1.5 km²) around the tower location, which reflect the current state-of-the-art eddy covariance upscaling approaches using coarse-resolution (e.g., from 500 m to 5 km) satellite data [43], [48]. This method overlooks the spatial heterogeneity of the areas surrounding flux towers and the dynamic nature of the flux measurement footprint. As many sites are situated in heterogeneous landscapes, featuring multiple land cover types and diverse vegetation conditions, the mismatch between the fixed satellite pixel grid and the measurement footprint introduces substantial biases to the upscaling estimation [42], [49].

Prithvi-EO benefits from the detailed spatial information of the HLS data, thereby enhancing the representation of remote sensing data within the flux measurement footprints. Notably, while the ResNet model also leverages spatial information from HLS images, its performance is consistently lower than Prithvi-EO (i.e., average $R^2$ of 0.75 for ResNet vs. 0.81 for Prithvi-EO-2.0-600M-TL). The superior performance of Prithvi-EO demonstrates the advantage of extracting generalizable spatial context by pretraining on massive satellite datasets and incorporating temporal and location embeddings. Furthermore, the proposed fine-tuning approach using Prithvi-EO-2.0 and MERRA-2 data shows promise for expanding the study to additional flux tower sites and extrapolating GPP beyond the flux network to derive a key climatic variable.

## V. Conclusion

We presented Prithvi-EO-2.0, the second iteration of the Prithvi-EO family. Prithvi-EO-2.0 showed strong performance in both standard benchmarking experiments at different resolutions, where it improved up to 8% its predecessor and outperformed some of the most popular GFMs on GEO-Bench datasets [10]. Prithvi-EO-2.0 also showed state-of-the-art results across a range of SME-led real-world applications in disaster response, land cover and crop mapping, and ecosystem dynamics monitoring. As future work, comparisons with multimodal GFMs could help identify the benefits of multimodal pretraining for tasks that include multiple modalities as well as the limitations of incorporating additional data into Prithvi at the fine-tuning stage. Key to the success of this multidisciplinary cross-institution project was developing a carefully crafted unbiased multitemporal dataset for pretraining, and the transparent and thorough evaluation of many aspects of Prithvi-EO-2.0. The project exemplifies the Trusted Open Science Pledge that all project partners subscribed to. In this spirit, we release our models with a permissive license in two different sizes (300 and 600 M) on Hugging Face.[^10] To maximize community impact and reduce barriers to entry, we have also onboarded the models into TerraTorch,[^11] enabling easy customization and adoption.

## Appendix

### GEO-Bench Detailed Results

Here, we present the detailed GEO-Bench evaluation results for all models (Tables XVI–XIX). The tables report the mean, standard deviation, maximum, and minimum metrics on the test set, computed over ten repeated runs using the best hyperparameters for all models. These results correspond to the boxplots shown in Fig. 7.

## Acknowledgment

The authors want to express their gratitude to Hugging Face for hosting Prithvi, associated demos, and the corresponding datasets for fine-tuning. They gratefully acknowledge the Gauss Centre for Supercomputing e.V. (www.gauss-centre.eu) by providing computing time through the John von Neumann Institute for Computing (NIC) on the GCS Supercomputer JUWELS [21] at Jülich Supercomputing Centre (JSC).

The model is available at: <https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0>. The code is available at: <https://github.com/NASA-IMPACT/Prithvi-EO-2.0>

[^1]: Prithvi means Earth in Sanskrit.
[^2]: <https://github.com/IBM/terratorch>
[^3]: <https://lightning.ai/docs/pytorch/stable/>
[^4]: <https://torchgeo.readthedocs.io/en/stable/>
[^5]: <https://github.com/IBM/terratorch-iterate>
[^6]: <https://optuna.readthedocs.io/en/stable/>
[^7]: <https://github.com/cloudtostreet/Sen1Floods11>
[^8]: <https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars>
[^9]: <https://ameriflux.lbl.gov/data/flux-data-products/>
[^10]: <https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0>
[^11]: <https://github.com/NASA-IMPACT/Prithvi-EO-2.0>
