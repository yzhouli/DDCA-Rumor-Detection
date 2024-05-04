# DFCA-Rumor-Detection

Source code corresponding to the paper “Yang Z, Pang Y, Li Q, et al. A model for early rumor detection base on topic-derived domain compensation and multi-user association[J]. Expert Systems with Applications, 2024: 123951.”

Subsequently, the next version of the MisDerdect dataset link: https://github.com/yzhouli/SocialNet-Weibo/tree/master . The next version of the dataset will introduce multimodal data to reproduce real-world environments. Meanwhile, continuously collect and update the magnitude of the dataset.

# Model

A detection model of early rumor at the Graph Convolutional Neural Network-based (DFCA-GCN) is proposed. This method is dedicated to solving the problem of early rumor detection. Moreover, it solved the problem of data sparsity in the early stage. With only 4 hours of topic data, rumors can be accurately identified.

# MisDerdect

These topics are publicized through the official website of the Weibo Community Management Center. The center displays topics that have been officially identified as rumors by Weibo. We collected information on 2067 original topics. There were 1,000 rumor topics and 1,067 non-rumor topics. Meanwhile, we perform manual identification of derived topics based on official facts. Strong-related derivative topics were collected nearly 270,000 posts, and nearly 300,000 unrelated posts were randomly added. The set of Web-wide topics is composed of them together. 
