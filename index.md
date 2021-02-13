## PhD Student In Medical Imaging With Philips, CREATIS and HCL Lyon
<img src="images/PHD.png?raw=true"/> 

### Computer Vision and Machine Learning Msc Graduate 

---
### Research Projects
#### Computer Vision and Deep Learning Intern at GE Healthcare
**Investigation of automatic search methods for neural network hyperparameters (Neural Architecture Search). Application to Mammographic Data within WHARe team (Women's Health Applied Research)**
<img src="images/GE.jpg?raw=true"/> 
* One of the major challenges in mammography is to develop systems that improve the effec-
tiveness of clinical diagnostic. Deep learning became indispensable in this kind of tasks. It
freed us from features engineering, however, the search for optimal neural network hyperpa-
rameters is a very time-consuming process. The neural architecture search (NAS) methods 
enable to establish optimal hyperparameters automatically and save a lot of time. During
this internship and unlike conventional approaches that apply evolution or reinforcement
learning, we choose to test the efficiency of a gradient-based NAS method called DARTS
(Differentiable Architecture Search) to perform classification tasks on mammographic data
and test learned architecture transfer from one dataset to another. DARTS is shown to require
100x fewer GPU memory than other existing methods and achieved the state-of-the-art in
image classifications tasks on CIFAR and ImageNet datasets.

* We test the efficiency of transfer of architectures learned on different da-
tasets to mammographic data. The process consists of search and evaluation phases. We
perform the search phase on mammographic (or other dataset) where we perform neural
architecture search and establish the architecture. During the evaluation phase, we train
from scratch the discovered architecture and report results on the validation set.

* Based on this motivation, we conduct experiments where we come to significantly out-
perform exiting models on different mammographic dataset. The approach is proven to be
effective and shows promising results on mammography data classification task. Architecture
transfer is also possible with larger, context-similar datasets and gives insights for other
applications. However, DARTS approach is still not hyperparameter-free. It introduces new
hyper-parameters while eliminating some other. For example the models that generate
architectures still need to be hand designed. Furthermore, hyper-paramaters like learning
rate, regularization strength and the type of optimizer are almost always left outside the
scope of search,the choice of the search space also needs careful tuning in many cases.

<img src="images/GE_INTERNSHIP.jpg?raw=true"/> 

[**Unsupervised Spatiotemporal Data Inpainting**](https://github.com/raoufkeskes/Unsupervised-Spatiotemporal-Data-Inpainting)
* This a PyTorch implementaiton of this paper : [**Unsupervised Spatiotemporal Data Inpainting**](https://openreview.net/forum?id=rylqmxBKvH) Under review at ICLR 2020.
* The code is implemented with the help of : Ilyas aroui [Github](https://github.com/ily-R), Raouf Keskes [Github](https://github.com/raoufkeskes)
* Inpainting spatio-temporal sequences is an active research topic that relies heavily on supervision with large datasets. In this work, we consider the problem of reconstructing missing information with an unsupervised learning approach. Following the work of Kim et al. We train a generative model on the occluded sequences. We ensure that the models captured both frame-based and sequential based information. Our proposed model is adapted to large-scale images and can be used to different types of sequences and occlusion processes.
<img src="images/unsupervised.png?raw=true"/> 

[**Cell Images Segmentation Using Cycle Generative Adversarial Network**](https://github.com/AissamDjahnine/CycleGAN)
* Cell images segmentation is a fundamental task for various medical applications, including nuclei
morphology analysis, cell type classification, and cancer grading. Deep learning has emerged as a powerful approach to segment
nuclei, but the accuracy of convolutional neural networks (CNNs) depends on the volume and quality of labeled data for training.Here, we implement an approach to cell segmentation that overcomes this challenge by utilizing a cycleGan framework (cycle generative adversarial network). The main objective of this research project is twofold :
* Generate synthetic cell images that model the distribution of the input images for data augmentation. Use both of the synthetic and real cells images for training a contextaware CNN that can accurately segment these cells.
* We propose to employ a segmentation method based on cycle-consistent generative adversarial networks (CycleGANs) that can be trained even in absence of prepared image-mask pairs.
<img src="images/cycleGan.jpg?raw=true"/>

[**Histopathological Images Generation Using Generative Adversarial Network**](https://github.com/AissamDjahnine/gans)
* Here, we implement an approach to histopathological image generation that overcomes the challenge of dataset size (small datasets) in medical field by utilizing a GAN framework (Generative adversarial network). The main objective of this research project is :
* Generate synthetic histopathological images that model the distribution of the input images for data augmentation. Use both of the synthetic and real images for training in different tasks (detection/segmentation/tracking).
<img src="images/gans_ex.png?raw=true"/>

### Projects


[**Color Transfer between Images in a correlated colour space (RGB)**](https://github.com/AissamDjahnine/ColorTransfer)
* Color transfer between images is the process of altering the color of a target image based on a source image.
The goal is to transfer the look and the feel of this last (i.e : color characteristics) to the target image in order to increase
its visual appeal and improve its appearance (ex: converting a daylight image into a night scene, a cold color image into a
warm one).
In this project, i implemented the Color transfer in Correlated Color Space algorithm specifically in RGB color space
* based on the work of Xuezhong Xiao And Lizhuang.
<img src="images/colortransfer.jpg?raw=true"/>

[**Search Algorithms Implementation ( BFS, DFS, DIJKSTR ,A-Star )**](https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-)
* Searching is the universal technique of problem solving in AI. this project will give you a start with these different algorithms.
* Brute-Force Search Strategies.
* * Breadth-First Search : It can be implemented using FIFO queue data structure. This method provides shortest path to the solution.
* * Depth-First Search : It is implemented in recursion with LIFO stack data structure.

* Informed (Heuristic) Search Strategies
* * A Star Search : It is best-known form of Best First search.In this project I've implemented A* algorithm with :
* * The Manhattan Distance Heuristic : this method of computing is called the Manhattan method because it is computed by calculating the total number of squares moved horizontally and vertically to reach the target square from the current square. We ignore diagonal movement and any obstacles that might be in the way.
* * The Euclidean Distance Heuristic : his heuristic is slightly more accurate than its Manhattan counterpart. If we try run both simultaneously on the same maze, the Euclidean path finder favors a path along a straight line. This is more accurate but it is also slower because it has to explore a larger area to find the path.

<img src="images/searchalgorithms.jpg?raw=true"/>

[**Suppression of Acoustic Noise in Speech Using Spectral Subtraction**](https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-)
* *Based on the work of STEVE F.BOLI , Paper available at : [Paper](https://ieeexplore.ieee.org/document/1163209)*
<img src="images/noisecancelling.jpg?raw=true"/>


[**Markov Decision Process**](https://github.com/AissamDjahnine/markov-decision-process)
* *A Markov decision process (MDP) is a discrete time stochastic control process. It provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are useful for studying optimization problems solved via dynamic programming and reinforcement learning. MDPs were known at least as early as the 1950s;a core body of research on Markov decision processes resulted from Ronald Howard's 1960 book, Dynamic Programming and Markov Processes.They are used in many disciplines, including robotics, automatic control, economics and manufacturing. The name of MDPs comes from the Russian mathematician Andrey Markov.*
<img src="images/markovdecisionprocess.jpg?raw=true"/>

[**Metro Problem**](https://github.com/AissamDjahnine/Metro-Problem-)
* Implementation of Dijkstra's algorithm to compute the shortest path on Paris subway network using C++.
<img src="https://github.com/AissamDjahnine/aissamdjahnine.github.io/blob/master/images/BastilleJussieu.jpg?raw=true"/>

### Online Courses / Achievements 
* **Coursera** : Deep learning Specialization
* **Udemy** : Python for Data Science and Machine Learning Bootcamp Certificate.

