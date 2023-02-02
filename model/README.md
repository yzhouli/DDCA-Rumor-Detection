# DFCA-GCN

A detection model of early rumor at the Graph Convolutional Neural Network-based is proposed. This method is dedicated to solving the problem of early rumor detection. Moreover, it solved the problem of data sparsity in the early stage. With only 4 hours of topic data, rumors can be accurately identified.

## Dataset

This folder contains two processed data sets. 

* **dataset_time_0.zip**: dataset indicates all data that can be obtained when the topic is published. 
* **dataset_time_4.zip**: dataset indicates all data that can be obtained when the topic is released in the 4th hour.

## Model

Core code of DFCA-GCN model. We use the tensorflow framework to train the model on a mac m1 chip.

* **train.py**: Training code of the model.
* **gcn.py**: Source code of the model of self-defined graph convolution neural network.
* **characteristic.py**: The source code for calculating the characteristic matrix.
* **rel.py**: The source code for calculating the relationship matrix.
* **d_matrix.py**: The source code for calculating the degree matrix of the relationship matrix.
* **credit.py**: The source code for calculating element credibility.