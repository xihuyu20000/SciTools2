import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import SpectralClustering 
from sklearn.preprocessing import StandardScaler, normalize 
from sklearn.decomposition import PCA 
from sklearn.metrics import silhouette_score 

# 参考 https://www.geeksforgeeks.org/ml-spectral-clustering/
"""
谱聚类，是把数据节点看作是图中的节点，把聚类问题转换为图分区问题。
步骤：
1、根据邻接矩阵构造相似度图
2、将数据投影到低维空间
3、聚类

优点:
1、少假设
2、易于实现且速度快
3、对密集数据集非常耗时
"""
# 加载信用卡数据
X = pd.read_csv('CC GENERAL.csv')

# 删除特定列
X = X.drop('CUST_ID', axis = 1)

# 填充缺失值
X.fillna(method ='ffill', inplace = True)

# Preprocessing the data to make it visualizable

# 标准化，经过处理的数据符合标准正态分布，即均值为0，标准差为1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 归一化
X_normalized = normalize(X_scaled)

# Converting the numpy array into a pandas DataFrame
X_normalized = pd.DataFrame(X_normalized)

# PCA 降维
pca = PCA(n_components = 2)
X_principal = pca.fit_transform(X_normalized)
X_principal = pd.DataFrame(X_principal)
X_principal.columns = ['P1', 'P2']

X_principal.head()

# 构建聚类模型，第2个参数是亲和力，取值是rbf或nearest_neighbors
spectral_model_rbf = SpectralClustering(n_clusters = 2, affinity ='rbf')

# Training the model and Storing the predicted cluster labels
labels_rbf = spectral_model_rbf.fit_predict(X_principal)

# Building the label to colour mapping
colours = {}
colours[0] = 'b'
colours[1] = 'y'

# Building the colour vector for each data point
cvec = [colours[label] for label in labels_rbf]

# Plotting the clustered scatter plot

b = plt.scatter(X_principal['P1'], X_principal['P2'], color ='b');
y = plt.scatter(X_principal['P1'], X_principal['P2'], color ='y');

plt.figure(figsize =(9, 9))
plt.scatter(X_principal['P1'], X_principal['P2'], c = cvec)
plt.legend((b, y), ('Label 0', 'Label 1'))
plt.show()

