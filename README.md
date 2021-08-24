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
        <li><a href="#download">Download</a></li>
        <li><a href="#directory-tree">Directory tree</a></li>
      </ul>
    </li>
    <li><a href="#Template-Notebooks">Colab Notebooks</a>
      <ul>
        <li><a href="#Burgers-equation">Burgers equation</a></li>
        <li>
            <a href="#Flow-past-cylinder">Flow past cylinder</a>
            <ul>
              <li><a href="#FPC-SFC-CAE">SFC-CAE</a></li>
              li><a href="#FPC-SFC-HAE">SFC-HAE </a></li>
              <li><a href="#FPC-SFC-CAE">SFC-SAE</a></li>
              <li><a href="#FPC-SVD-AE">SVD-AE</a></li>
              <li><a href="#FPC-SFC-POD">POD</a></li>
            </ul>
        </li>
      </ul>   
    </li>
    <li><a href="#License">License</a></li>
    <li><a href="#Testing">Testing</a></li>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#Acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- copy_over_N_files.py在压缩包中需要删除 -->
## Project Description
To investigate the application of the dimensionality reduction methods in fluid dynamics, this project implements and compares many dimensionality reduction methods including proper orthogonal decomposition(POD), fully-connected autoencoder (FC-AE), convolutional autoencoder (CAE), space-filling curve - convolutional autoencoder (SFC-CAE), hierarchical autoencoder (HAE) and sequential autoencoder (SAE). Moreover, the novel space-filling curve-hierarchical autoencoder (SFC-HAE) is proposed. The mentioned methods are assessed with two fluid solutions, namely: (1) burgers equation, (2) flow past cylinder, in terms of mean square error (MSE) and computation time. 
The project is based on the wokr of previous year https://arxiv.org/abs/2011.14820,https://github.com/ImperialCollegeLondon/SFC-CAE and paper https://arxiv.org/abs/2006.06977.

## Getting Started
### Download

### Directory tree

#### Directory tree in Colab


#### Directory tree in local computer

## Template Notebooks
### Burgers equation
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/burgers_equation_methods/Burgers_equation.ipynb)
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
  </p>
</p>

#### SFC-CAE
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/fpc_methods/SFC_CAE/FPC_SFC_CAE_Sumary.ipynb)
<p align="center">
  <p float="left">
     <img src="pics/FPC_SFC_CAE_64.gif">
     <a href="pics/FPC_SFC_CAE_64.gif"><strong>FPC SFC-CAE 64 variables</strong></a>
  </p>
</p>

#### SFC-HAE
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/fpc_methods/SFC_HAE/FPC_SFC_HAE_Sumary.ipynb)
<p align="center">
  <p float="left">
     <img src="pics/Fpc-Hae_64.gif">
     <a href="pics/Fpc-Hae_64.gif"><strong>FPC SFC-HAE 64 variables</strong></a>
  </p>
</p>

#### SFC-SAE
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/fpc_methods/SFC_SAE/FPC_SFC_SAE_Sumary.ipynb)
<p align="center">
  <p float="left">
     <img src="pics/Fpc-Sae_64.gif">
     <a href="pics/Fpc-Sae_64.gif"><strong>FPC SFC-SAE 64 variables</strong></a>
  </p>
</p>

#### SVD-AE
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/fpc_methods/FPC_SVD_AE_random.ipynb)
<p align="center">
  <p float="left">
     <img src="pics/FPC-SVDAE_64.gif">
     <a href="pics/FPC-SVDAE_64.gif"><strong>FPC SVD-AE 64 variables</strong><a>
  </p>
</p>

#### POD
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/acse-fy120/acse-9-independent-research-project-fy120/blob/main/fpc_methods/FPC_POD.ipynb)
<p align="center">
  <p float="left">
     <img src="pics/Fpc-Pod_64.gif">
     <a href="pics/Fpc-Pod_64.gif"><strong>FPC POD 64 variables</strong><a>
  </p>
</p>
