# acse-9-independent-research-project-fy120

## A comparison of dimensionality reduction methods for fluid flow problems focusing on hierarchical autoencoders

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)


<br />
<p align="center">
  <a href="https://github.com/acse-fy120/acse-9-independent-research-project-fy120/blob/main/pics/POD architecture.jpg">
    <img src="pics/POD architecture.jpg">
    <figcaption> Achitechture of principal component analysis</figcaption>
  </a>
</p>

<p align="center">
  <a href="https://github.com/acse-fy120/acse-9-independent-research-project-fy120/blob/main/pics/FCAE architecture.jpg">
    <img src="pics/FCAE architecture.jpg">
    <figcaption> Achitechture of fully-connected autoencoder </figcaption>
  </a>
</p>

<p align="center">
  <a href="https://github.com/acse-fy120/acse-9-independent-research-project-fy120/blob/main/pics/SFCCAE architecture.jpg">
    <img src="pics/SFCCAE architecture.jpg">
    <figcaption> Achitechture of space-filling-curve convolutional autoencoder </figcaption>
  </a>
</p>

<p align="center">
  <a href="https://github.com/acse-fy120/acse-9-independent-research-project-fy120/blob/main/pics/HAE.jpg">
    <img src="pics/HAE.jpg">
    <figcaption> Achitechture of hierarchical autoencoder </figcaption>
  </a>
</p>

<p align="center">
  <a href="https://github.com/acse-fy120/acse-9-independent-research-project-fy120/blob/main/pics/SAE.jpg">
    <img src="pics/SAE.jpg">
    <figcaption> Achitechture of sequential autoencoder </figcaption>
  </a>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-description">Project Description</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Dependencies">Prerequisites & Dependencies</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Template-Notebooks">Colab Notebooks</a>
      <ul>
        <li><a href="#advecting-block">Advection of a Block/Gaussian  (128 * 128 Structured Grid)</a></li>
        <li><a href="#FPC-DG">Flow Past Cylinder - DG Mesh (2000 snapshots, 20550 Nodes, 2/3 components)</a></li>
        <li><a href="#FPC-CG">Flow Past Cylinder - CG Mesh (2000 snapshots, 3571 Nodes, 2 components) </a></li>
        <li><a href="#CO2"> CO2 in the room - CG Mesh (455 snapshots, 148906 Nodes, 4 components)</a></li>
        <li><a href="#Slugflow"> Slugflow - DG mesh (1706 snapshots, 1342756 Nodes, 4 components)</a></li>
      </ul>   
    </li>
    <li><a href="#License">License</a></li>
    <li><a href="#Testing">Testing</a></li>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#Acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- copy_over_N_files.py在压缩包中需要删除 -->


### Burgers equation
<p align="center">
  <p float="left">
     <img src="pics/original_BE.gif">
     <a href="pics/original_BE.gif"><strong>Original Burgers equation</strong></a>
     <img src="pics/POD_BE_2variable.gif">
     <a href="pics/POD_BE_2variable.gif"><strong>Burgers equation POD 2 variables</strong></a>
     <img src="pics/FCAE_BE_2variable.gif">
     <a href="pics/FCAE_BE_2variable.gif"><strong>Burgers equation FC-AE 2 variables</strong></a>
     <img src="pics/CAE_BE_2variable.gif">
     <a href="pics/CAE_BE_2variable.gif"><strong>Burgers equation CAE 2 variables</strong></a>
     <img src="pics/SVDAE_BE_2variable.gif">
     <a href="pics/SVDAE_BE_2variable.gif"><strong>Burgers equation SVD-AE 2 variables</strong></a>
     <img src="pics/HAE_BE_2variable.gif">
     <a href="pics/HAE_BE_2variable.gif"><strong>Burgers equation HAE 2 variables</strong></a>
  </p>
</p>


### FPC
<p align="center">
  <p float="left">
     <img src="pics/Fpc-Orginal.gif">
     <a href="pics/Fpc-Orginal.gif"><strong>Original FPC</strong></a>
     <img src="pics/FPC_SFC_CAE_64.gif">
     <a href="pics/FPC_SFC_CAE_64.gif"><strong>FPC SFC-CAE 64 variables</strong></a>
     <img src="pics/Fpc-Hae_64.gif">
     <a href="pics/Fpc-Hae_64.gif"><strong>FPC SFC-HAE 64 variables</strong></a>
     <img src="pics/Fpc-Sae_64.gif">
     <a href="pics/Fpc-Sae_64.gif"><strong>FPC SFC-SAE 64 variables</strong></a>
     <img src="pics/Fpc-Pod_64.gif">
     <a href="pics/Fpc-Pod_64.gif"><strong>FPC POD 64 variables</strong><a>
     <img src="pics/FPC-SVDAE_64.gif">
     <a href="pics/FPC-SVDAE_64.gif"><strong>FPC SVD-AE 64 variables</strong><a>
  </p>
</p>