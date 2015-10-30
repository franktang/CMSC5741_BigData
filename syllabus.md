# Syllabus

###1. Introduction

just introduction

###2. MapReduce/Frequent Itemsets

* **HDFS** is a distributed file system built with robust in mind 
* **MapReduce** is a convenient paradigm to implement parallel program 
* **Hadoop** is an open source implementation of **MapReduce** 
* **Hadoop streaming** allows you to use any language to program **mapper** and **reducer** 
* Monotonicity property enable efficient algorithms for Frequent Itemsets problem

###3. Locality Sensitive Hashing

* Finding similar documents: 
  - Shingling
  - Min Hashing
  - Locality-Sensitive Hashing
* Other LSH applications
* Appendix: How to construct locality-sensitive hash functions

###4. Mining Data Streams

* Sampling from a streaming data
  - How to get a fixed proportion or a fixed-size Sample
* Queries over a long sliding windows
  - understand **DGIM** algorithm
* Filtering Data Streams
  - understand first cut solution and Bloom Filter
* Counting distinct elements
  - Understand Flajolet-Martin Approach
* Appendix: computing moments and counting item sets 

###5. Scalable Clustering

* **Clustering:**  
  Given a set of points, with a notion of distance between points, group the points into some number of clusters 
* **Algorithms:**
  - Agglomerative hierarchical clustering:
    - Centroid and clustroid
  - **k-means**:
    - Initialization, picking k
  - k-means++
  - k-means||
  - BFR
  - CURE

###6. Dimensionality Reduction

* Dimensionality reduction
  - compress/reduce dimension
  - reconstruct the original matrix by two or more smaller matrices
* Singular value decomposition (**SVD**)
  - decompose a matrix into [TO DO]
* CUR decomposition
  - [TO DO]
* Principle component analysis (PCA)
  - reconstruct data matrix by a smaller number of eigenvectors
  - view the data from a *literally* different angle.

###7. Recommender systems/Matrix

* Matrix Factorization is the key to recommender systems
* **LU-decomposition**
  - Decompose a matrix into a lower triangular matrix and an upper triangular matrix
* **SVD decomposition**
  - See part 6 above
* **Probabilistic Matrix Factorization**
  - Factorize a partially observed matrix into the product of two low-rank matrices, usually used in recommender systems
* **Non-negative Matrix Factorization**
  - Factorize a matrix into the produce of two non-negative matrices, can be used to learn the "parts"

###8. Massive Link Analysis

* Web as a Graph
  - Denote the web structure as a graph
* **PageRank**
  - PageRank score reflect the importance of web pages
* Topic-Specific PageRank
  - Evaluate web pages by their popularity as well as particular topic
* Trust-Rank
  - Deal with link spams

To be continued...

