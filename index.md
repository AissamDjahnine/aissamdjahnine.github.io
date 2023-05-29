## Researcher Phd Candidate @ Philips AI Research Hub France In collaboration with CREATIS Lab and HCL Lyon

<img src="images/PHD.png?raw=true"/> 

### Publications :
[*Research in Diagnostic and Interventional Imaging : BERT-based natural language processing analysis of French CT reports: Application to the measurement of the positivity rate for pulmonary embolism*](https://www.sciencedirect.com/science/article/pii/S2772652523000066)<br> 
Émilien Jupin-Delevaux, **Aissam Djahnine**, François Talbot, Antoine Richard, Sylvain Gouttard, Adeline Mansuy, Philippe Douek, Salim Si-Mohamed, Loïc Boussel

<!-- [*Research in Diagnostic and Interventional Imaging : BERT-based natural language processing analysis of French CT reports: Application to the measurement of the positivity rate for pulmonary embolism*](https://www.sciencedirect.com/science/article/pii/S2772652523000066)<br> 
Émilien Jupin-Delevaux, **Aissam Djahnine**, François Talbot, Antoine Richard, Sylvain Gouttard, Adeline Mansuy, Philippe Douek, Salim Si-Mohamed, Loïc Boussel -->

### Conferences & Summer Schools :
[*16th IEEE International Conference on Signal Processing (ICSP), Beijing, China : Tailored 3D CT contrastive pretraining to improve pulmonary pathology classification*](https://www.researchgate.net/publication/365967135_Tailored_3D_CT_contrastive_pretraining_to_improve_pulmonary_pathology_classification)<br>
**Djahnine Aissam**, Popoff Alexandre, Jupin-Delevaux Emilien, Cotin Vincent, Nempont Olivier, Boussel Loic

<!-- This is a comment that won't be rendered  [*Oxford Machine Learning Summer School (13 July - 16 July 2023)*]() -->

### Honors & awards
[*Data Challenge : Pulmonary embolism detection in CT*](https://www.linkedin.com/posts/nicolas-villain-9422122_fier-de-cette-belle-%C3%A9quipe-bravo-pour-activity-6985258006707851264-w3i9?utm_source=share&utm_medium=member_desktop)

* I was a member of the Philips team in collaboration with Hospices Civils de Lyon that won the JFR (les Journées Francophones de Radiologie) data challenge. The solution used Deep Learning for Computer Vision to detect pulmonary embolism in CT scans. ([*Journal Paper*]())
<img src="images/JFR_port.png?raw=true"/> 
---

#### Computer Vision and Machine Learning Msc Graduate at Sorbonne Université 
---
### Research Projects
#### Computer Vision and Deep Learning Intern at GE Healthcare
**Investigation of automatic search methods for neural network hyperparameters (Neural Architecture Search). Application to Mammographic Data within WHARe team (Women's Health Applied Research)**
<img src="images/GE.jpg?raw=true"/> 

* In this internship, we focused on improving mammography systems for clinical diagnosis by utilizing deep learning techniques. 
We specifically explored the efficiency of a gradient-based NAS method called DARTS (Differentiable Architecture Search) for classification 
tasks on mammographic data. Through experiments, we achieved state-of-the-art results on mammography data classification, outperforming existing models. 

<img src="images/GE_INTERNSHIP.jpg?raw=true"/> 

[**Unsupervised Spatiotemporal Data Inpainting**](https://github.com/raoufkeskes/Unsupervised-Spatiotemporal-Data-Inpainting)
* This a PyTorch implementaiton of this paper : [**Unsupervised Spatiotemporal Data Inpainting**](https://openreview.net/forum?id=rylqmxBKvH) Under review at ICLR 2020.
* The code is implemented in collaboration of : Ilyas aroui [Github](https://github.com/ily-R), Raouf Keskes [Github](https://github.com/raoufkeskes)
* Inpainting spatio-temporal sequences is an active research topic that relies heavily on supervision with large datasets. In this work, we consider the problem of reconstructing missing information with an unsupervised learning approach. Following the work of Kim et al. We train a generative model on the occluded sequences. We ensure that the models captured both frame-based and sequential based information. Our proposed model is adapted to large-scale images and can be used to different types of sequences and occlusion processes.
<img src="images/unsupervised.png?raw=true"/> 

[**Cell Images Segmentation Using Cycle Generative Adversarial Network**](https://github.com/AissamDjahnine/CycleGAN)

<img src="images/INSTITUT_PASTEUR_LOGO_2020.jpg?raw=true" width="300"/> 
* During our 6-month curriculum project with Institut Pasteur and Sorbonne University, we focused on cell image segmentation for various medical applications. Recognizing the significance of labeled data for training accurate convolutional neural networks (CNNs), we adopted a cycleGAN framework to overcome the challenge of limited data. Our research objectives were two-fold: first, to generate synthetic cell images that mimic the distribution of input images for data augmentation, combining them with real cell images to train a context-aware CNN for precise cell segmentation. Second, we proposed a segmentation method based on cycle-consistent generative adversarial networks (CycleGANs), which allowed us to train the model even in the absence of prepared image-mask pairs.
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
In this project, i implemented the Color Transfer in Correlated Color Space algorithm specifically in RGB color space
* based on the work of Xuezhong Xiao And Lizhuang.
<img src="images/colortransfer.jpg?raw=true"/,>

[**Search Algorithms Implementation ( BFS, DFS, DIJKSTR ,A-Star )**](https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-)
* Searching is the universal technique of problem solving in AI. this project will give you a start with these different algorithms.
* Brute-Force Search Strategies.
  * Breadth-First Search : It can be implemented using FIFO queue data structure. This method provides shortest path to the solution.
  * Depth-First Search : It is implemented in recursion with LIFO stack data structure.

* Informed (Heuristic) Search Strategies : 
  * A Star Search : It is best-known form of Best First search.In this project I've implemented A* algorithm with :
  * The Manhattan Distance Heuristic : this method of computing is called the Manhattan method because it is computed by calculating the total number of squares moved horizontally and vertically to reach the target square from the current square. We ignore diagonal movement and any obstacles that might be in the way.
  * The Euclidean Distance Heuristic : his heuristic is slightly more accurate than its Manhattan counterpart. If we try run both simultaneously on the same maze, the Euclidean path finder favors a path along a straight line. This is more accurate but it is also slower because it has to explore a larger area to find the path.

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

