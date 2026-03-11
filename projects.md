---
layout: default
title: Research Projects
permalink: /projects/
---
## <span style="color: #267cb9;">Research</span>

### PhD Thesis

<div class="gh-card no-media thesis-card">
  <div>
    <div class="thesis-meta-grid">
      <div class="thesis-meta-item"><strong>Field:</strong> Biomedical Imaging</div>
      <div class="thesis-meta-item"><strong>Institution:</strong> INSA Lyon</div>
      <div class="thesis-meta-item"><strong>Lab:</strong> CREATIS</div>
      <div class="thesis-meta-item"><strong>Defended:</strong> Sep 17, 2024</div>
    </div>
    <div class="gh-title">Automatic Detection of Pathologies in Conventional Scanner Data</div>
    <div class="gh-description">This thesis investigates AI-based detection and characterization of pulmonary pathologies in conventional CT scans, with a focus on reducing annotation requirements. It explores supervised, weakly supervised, and unsupervised learning strategies to detect anomalies and support radiologists in identifying incidental findings beyond the initial clinical indication.</div>
    <div class="gh-description"><strong>Author:</strong> Aissam Djahnine · <strong>Supervisor:</strong> Loïc Boussel</div>
    <div class="thesis-footer">
      <div class="gh-actions">
        <a class="gh-link" href="https://theses.hal.science/tel-05263492/" target="_blank" rel="noopener">Read Manuscript ↗</a>
        <a class="gh-link" href="https://hal.science/tel-05263492/" target="_blank" rel="noopener">HAL ↗</a>
        <a class="gh-link" href="https://theses.fr/2024LYO10167" target="_blank" rel="noopener">theses.fr ↗</a>
      </div>
      <div class="thesis-stats" aria-label="Thesis metrics">
        <span class="thesis-stat">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5c-5.23 0-9.27 4.11-10.5 6 1.23 1.89 5.27 6 10.5 6s9.27-4.11 10.5-6C21.27 9.11 17.23 5 12 5zm0 10a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm0-2.2A1.8 1.8 0 1 0 12 9.2a1.8 1.8 0 0 0 0 3.6z"/></svg>
          {{ site.data.thesis_stats.views }}
        </span>
        <span class="thesis-stat">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a1 1 0 0 1 1 1v8.59l2.3-2.29a1 1 0 1 1 1.4 1.41l-4 4a1 1 0 0 1-1.4 0l-4-4a1 1 0 1 1 1.4-1.41L11 12.59V4a1 1 0 0 1 1-1zm-7 14a1 1 0 0 1 1 1v1h12v-1a1 1 0 1 1 2 0v2a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1z"/></svg>
          {{ site.data.thesis_stats.downloads }}
        </span>
      </div>
    </div>
  </div>
</div>

<div style="height: 18px;"></div>

### Projects

<div class="gh-grid">
  <div class="gh-card">
    <img class="gh-media-img" src="/images/SARCO_PROJECT.png?raw=true" alt="Sarcopenia muscle segmentation project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Medical Imaging</span>
      </div>
      <div class="gh-title">Segmentation and Measurement of Skeletal Muscle Areas on CT Scans</div>
      <div class="gh-description">Developed deep learning-based segmentation at L3/L2/L1 levels to improve sarcopenia estimation with stronger data augmentation and post-processing for cleaner masks.</div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/cycleGan.jpg?raw=true" alt="CycleGAN cell segmentation project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Deep Learning</span>
      </div>
      <div class="gh-title">Cell Image Segmentation with CycleGAN</div>
      <div class="gh-description">Built a cycle-consistent GAN workflow for cell image segmentation with limited labels, enabling synthetic data generation and context-aware training.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/CycleGAN" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/gans_ex.png?raw=true" alt="Histopathological GAN generation preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Generative Models</span>
      </div>
      <div class="gh-title">Histopathological Image Generation Using GANs</div>
      <div class="gh-description">Implemented GAN-based synthetic histopathology generation to address small datasets and improve downstream detection/segmentation/tracking tasks.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/gans" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/colortransfer.jpg?raw=true" alt="Color transfer project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Computer Vision</span>
      </div>
      <div class="gh-title">Color Transfer in Correlated RGB Space</div>
      <div class="gh-description">Implemented correlated color transfer to adapt visual tone and style between images, based on the method by Xuezhong Xiao and Lizhuang.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/ColorTransfer" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/searchalgorithms.jpg?raw=true" alt="AI search algorithms project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">AI Algorithms</span>
      </div>
      <div class="gh-title">Search Algorithms (BFS, DFS, Dijkstra, A*)</div>
      <div class="gh-description">Implemented core search strategies and heuristics (Manhattan/Euclidean) to provide practical foundations for AI pathfinding and problem-solving.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/Search-Algorithms-in-AI" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/noisecancelling.jpg?raw=true" alt="Noise suppression project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Signal Processing</span>
      </div>
      <div class="gh-title">Speech Denoising via Spectral Subtraction</div>
      <div class="gh-description">Applied spectral subtraction for acoustic noise suppression in speech signals, improving clarity and intelligibility in noisy environments.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/Suppression-of-Acoustic-Noise-in-Speech-Using-Spectral-Subtraction-" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/markovdecisionprocess.jpg?raw=true" alt="Markov decision process project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Reinforcement Learning</span>
      </div>
      <div class="gh-title">Markov Decision Process</div>
      <div class="gh-description">Explored decision-making under uncertainty with MDP modeling and dynamic programming principles for optimization across applied domains.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/markov-decision-process" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>

  <div class="gh-card">
    <img class="gh-media-img" src="/images/BastilleJussieu.png?raw=true" alt="Metro problem project preview"/>
    <div>
      <div class="gh-meta">
        <span class="gh-tag">Optimization</span>
      </div>
      <div class="gh-title">Metro Problem (Dijkstra in Paris Subway)</div>
      <div class="gh-description">Built a shortest-path tool over subway graph data with user-friendly station matching and efficient path computation in C++.</div>
      <div class="gh-actions">
        <a class="gh-link" href="https://github.com/AissamDjahnine/Metro-Problem-" target="_blank" rel="noopener">GitHub ↗</a>
      </div>
    </div>
  </div>
</div>
