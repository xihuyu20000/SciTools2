# 谱聚类、层次聚类、Louvain聚类
import numpy as np
from sklearn.cluster import SpectralClustering

X = np.array([[1, 1], [2, 1], [1, 0],[4, 7], [3, 5], [3, 6]])

# clustering = SpectralClustering(n_clusters=2, assign_labels='discretize', random_state=0).fit(X)
# print(clustering.labels_)