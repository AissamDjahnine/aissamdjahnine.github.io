---
layout: default
title: Projects
permalink: /projects/
---
## <span style="color: #267cb9;">Projects</span>

**Segmentation and measurement of skeletal muscle areas on CT scans**

* This project aims to segment and measure skeletal muscle areas on CT scans, specifically at the L3, L2, and L1 vertebrae levels, to improve sarcopenia estimation using deep learning-based methods. By leveraging advanced data augmentation techniques, such as applying filters, rotations, and adding artificial elements, the dataset's diversity and robustness were significantly improved. Post-processing methods were developed to remove artifacts like ribs, ensuring cleaner and more accurate segmentations. The approach showed promising results in accurately segmenting muscle areas, leading to more reliable sarcopenia assessments and potential further improvements.

<img src="/images/SARCO_PROJECT.png?raw=true" />

[**Cell Images Segmentation Using Cycle Generative Adversarial Network**](https://github.com/AissamDjahnine/CycleGAN)

<img src="/images/INSTITUT_PASTEUR_LOGO_2020.jpg?raw=true" width="300"/> 
* During our 6-month curriculum project with Institut Pasteur and Sorbonne University, we focused on cell image segmentation for various medical applications. Recognizing the significance of labeled data for training accurate convolutional neural networks (CNNs), we adopted a cycleGAN framework to overcome the challenge of limited data. Our research objectives were two-fold: first, to generate synthetic cell images that mimic the distribution of input images for data augmentation, combining them with real cell images to train a context-aware CNN for precise cell segmentation. Second, we proposed a segmentation method based on cycle-consistent generative adversarial networks (CycleGANs), which allowed us to train the model even in the absence of prepared image-mask pairs.
<img src="/images/cycleGan.jpg?raw=true"/>

[**Histopathological Images Generation Using Generative Adversarial Network**](https://github.com/AissamDjahnine/gans)
* Here, we implement an approach to histopathological image generation that overcomes the challenge of dataset size (small datasets) in medical field by utilizing a GAN framework (Generative adversarial network). The main objective of this research project is :
* Generate synthetic histopathological images that model the distribution of the input images for data augmentation. Use both of the synthetic and real images for training in different tasks (detection/segmentation/tracking).<br>
<img src="/images/gans_ex.png?raw=true"/>

[**Color Transfer between Images in a correlated colour space (RGB)**](https://github.com/AissamDjahnine/ColorTransfer)
* Color transfer between images is the process of altering the color of a target image based on a source image. The goal is to transfer the look and the feel of this last (i.e : color characteristics) to the target image in order to increase its visual appeal and improve its appearance (ex: converting a daylight image into a night scene, a cold color image into a warm one).<br>
* In this project, I implemented the Color Transfer in Correlated Color Space algorithm specifically in RGB color space (based on the work of Xuezhong Xiao and Lizhuang).<br>

<img src="/images/colortransfer.jpg?raw=true" />

[**Search Algorithms Implementation (BFS, DFS, Dijkstra, A*)**](https://github.com/AissamDjahnine/Search-Algorithms-in-AI)
* This master project aims to provide newcomers in the field of AI with an introduction to the fundamental technique of problem solving: searching. The project covers various search algorithms, including brute-force strategies such as Breadth-First Search (BFS) and Depth-First Search (DFS). It also delves into informed search strategies, specifically focusing on the popular A* algorithm, which is implemented using two heuristic methods: the Manhattan Distance Heuristic and the Euclidean Distance Heuristic. By exploring these algorithms and heuristics, participants will gain a solid foundation in AI problem-solving techniques.<br>

<img src="/images/searchalgorithms.jpg?raw=true"/>

[**Suppression of Acoustic Noise in Speech Using Spectral Subtraction**](https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-)

* In this master project, I successfully implemented the technique of spectral subtraction for the suppression of acoustic noise in speech. The project is based on the pioneering work of Steve F. Boli, as described in his [*paper*](https://ieeexplore.ieee.org/document/1163209).

* By leveraging spectral subtraction, I effectively reduced the impact of background noise, enhancing the clarity and intelligibility of the speech signals. The project can be explored further on the GitHub repository [*here*](https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-).<br>
<img src="/images/noisecancelling.jpg?raw=true"/>

[**Markov Decision Process**](https://github.com/AissamDjahnine/markov-decision-process)

* The proposed master project aims to explore the application of Markov decision processes (MDPs) in various domains, such as robotics, automatic control, economics, and manufacturing. MDPs offer a mathematical framework to model decision-making scenarios where outcomes involve both random elements and the choices made by a decision maker. By leveraging dynamic programming and reinforcement learning techniques, this project seeks to optimize decision-making processes and develop effective strategies within the context of MDPs, contributing to advancements in multiple fields.<br>
<img src="/images/markovdecisionprocess.jpg?raw=true"/>

[**Metro Problem**](https://github.com/AissamDjahnine/Metro-Problem-)
* The "Dijkstra Metro-Problem" project uses Dijkstra's algorithm in C++ to find the shortest path in the Paris subway network. It relies on C/C++ compilers and two CSV files containing station and connection information.<br>

* The program, optimized for accuracy and efficiency, can be executed using either station IDs or names, ensuring user-friendliness and adaptability to minor input errors. This project showcases the practical application of complex algorithms in everyday transportation scenarios.
<img src="/images/BastilleJussieu.png?raw=true" style="height: 300px;">
