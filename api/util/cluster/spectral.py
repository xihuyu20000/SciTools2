from sklearn.cluster import KMeans
import numpy as np
import math as m
import matplotlib.pyplot as plt
import evaluate as eval

# flame.txt
# Jain_cluster=2.txt
# Aggregation_cluster=7.txt
# Spiral_cluster=3.txt
# Pathbased_cluster=3.txt



class SpectralClustering:
    def __init__(self):
        pass

    def load_data(self, data_path):
        """
        导入数据
        :return:
        """
        points = np.loadtxt(data_path, delimiter='\t')
        return points


    def get_dis_matrix(self, data):
        """
        获得邻接矩阵
        :param data: 样本集合
        :return: 邻接矩阵
        """
        nPoint = len(data)
        dis_matrix = np.zeros((nPoint, nPoint))
        for i in range(nPoint):
            for j in range(i + 1, nPoint):
                dis_matrix[i][j] = dis_matrix[j][i] = m.sqrt(np.power(data[i] - data[j], 2).sum())
        return dis_matrix


    def getW(self, data, k):
        """
        利用KNN获得相似矩阵
        :param data: 样本集合
        :param k: KNN参数
        :return:
        """
        dis_matrix = self.get_dis_matrix(data)
        W = np.zeros((len(data), len(data)))
        for idx, each in enumerate(dis_matrix):
            index_array = np.argsort(each)
            W[idx][index_array[1:k+1]] = 1
        tmp_W = np.transpose(W)
        W = (tmp_W+W)/2
        return W


    def getD(self, W):
        """
        获得度矩阵
        :param W:  相似度矩阵
        :return:   度矩阵
        """
        D = np.diag(sum(W))
        return D


    def getL(self, D, W):
        """
        获得拉普拉斯举着
        :param W: 相似度矩阵
        :param D: 度矩阵
        :return: 拉普拉斯矩阵
        """
        return D - W


    def getEigen(self, L, cluster_num):
        """
        从拉普拉斯矩阵获得特征矩阵
        :param L: 拉普拉斯矩阵
        :return:
        """
        eigval, eigvec = np.linalg.eig(L)
        ix = np.argsort(eigval)[0:cluster_num]
        return eigvec[:, ix]


    def plotRes(self, data, clusterResult, clusterNum):
        """
        结果可视化
        :param data:  样本集
        :param clusterResult: 聚类结果
        :param clusterNum:  聚类个数
        :return:
        """
        nPoints = len(data)
        scatterColors = ['black', 'blue', 'green', 'yellow', 'red', 'purple', 'orange']
        for i in range(clusterNum):
            color = scatterColors[i % len(scatterColors)]
            x1 = [];  y1 = []
            for j in range(nPoints):
                if clusterResult[j] == i:
                    x1.append(data[j, 0])
                    y1.append(data[j, 1])
            plt.scatter(x1, y1, c=color, alpha=1, marker='+')
        plt.show()


    def run(self, data_path, KNN_k, cluster_num):


        data = self.load_data(data_path)
        data = np.asarray(data)
        W = self.getW(data, KNN_k)
        D = self.getD(W)
        L = self.getL(D, W)
        eigvec = self.getEigen(L, cluster_num)
        clf = KMeans(n_clusters=cluster_num)
        s = clf.fit(eigvec)
        C = s.labels_
        nmi, acc, purity = eval.eva(C+1, data[:, 2])
        print(nmi, acc, purity)
        self.plotRes(data, np.asarray(C), 7)

data_path = "data/flame.txt"
cluster_num = 2
KNN_k = 5
c = SpectralClustering()
c.run(data_path, KNN_k, cluster_num)