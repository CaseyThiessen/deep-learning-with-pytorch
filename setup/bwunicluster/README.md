# BwUniCluster Guide

This guide provides an introduction to setting up and using the BwUniCluster. It is intended to help you complete the initial setup, become familiar with the basic workflow on the cluster, and prepare your environment for running computations and Jupyter notebooks.

We will go through the first steps needed to access the cluster, transfer files, create a virtual environment, and fix common setup issues. After completing the initial setup, you should be able to run the example notebooks presented in the lecture on your own computer or laptop.

This guide is intended as a practical complement to the official BwUniCluster documentation: <https://wiki.bwhpc.de/e/BwUniCluster3.0>

## Getting Started

A good starting point is to open the Jupyter notebook:

`BwCluster_Introduction.ipynb`

Work through the following sections in order:

1. **Before you start**
2. **Create your BwUniCluster account**
3.1 **Web login (using JupyterHub)**
4.2 **Copy files manually**
5. **Create the virtual environment**
6. **Fix the Jupyter notebook bug**

Following these steps will help you set up your account, prepare the cluster environment, and run the provided example notebooks.

## Required Files

During the setup, you will need to transfer the following files (section 4.2) to the cluster using the JupyterHub web interface:

- `requirements.txt`
- `clean_kernel`
- `job.sh`

These files are included in this repository.

## Repository Contents

This repository contains:

- `BwCluster_Introduction.ipynb`  
  The main guide explaining how to set up and use the BwUniCluster.

- `requirements.txt`  
  A list of Python packages required for the virtual environment.

- `clean_kernel`  
  A helper file used to fix the Jupyter notebook kernel setup.

- `job.sh`  
  A sample Bash job script that can be used to submit jobs on the cluster.

## Recommended Workflow

For the initial setup, it is recommended to use the JupyterHub web login.

After completing the first setup steps and becoming familiar with the cluster, it is recommended to switch to a graphical SSH client for later project work. This usually provides a more convenient workflow for transferring files, editing scripts, and managing larger projects on the cluster.


