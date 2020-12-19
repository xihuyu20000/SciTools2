import pandas as pd
import numpy as np
from collections import defaultdict
# 参考 https://blog.csdn.net/u014108004/article/details/84141746
class CoocMatrix:

    def __init__(self, ddata_arr, cut_method = 1, cut_value=10, norm_method = 1):
        """
        共现矩阵，进行裁剪，数值规范化
        @param ddata_arr
        @param cut_method : 裁剪方法：1表示取top K, 2表示取top K% 3表示区间裁剪
        @param cut_value : 裁剪值：若cut_method的值，当是1，这里是整数；当是2，这里是整数/100；当是3，这里是一个范围，格式“12-31”
        @param norm_method :  规范化方法：1表示绝对词频，2表示等价系数法
        """
        self.ddata_arr = ddata_arr
        self.cut_method = cut_method
        self.cut_value = cut_value
        self.norm_method = norm_method

    def __items_stat(self):
        co_item = defaultdict(int)  # 共现次数
        single_item = defaultdict(int)    # 单个出现次数
        for items in self.ddata_arr:
            for i, e1 in enumerate(items):
                single_item[e1] += 1
                for j, e2 in enumerate(items):
                    if j > i:  # 保障每个只能匹配一次
                        k = e1 + ',' + e2 if e1 < e2 else e2 + ',' + e1  # 设置k
                        co_item[k] += 1
        # 共现次数 降序 排列
        co_item = sorted(co_item.items(), key=lambda x:x[1], reverse=True)
        # 裁剪
        if self.cut_method == 1:    # top K
            co_item = co_item[:self.cut_value]
        elif self.cut_method == 2:  # top K%
            count = int(len(co_item)*self.cut_value/100)
            co_item = co_item[:count]
        elif self.cut_method == 3: #区间裁剪
            min = int(self.cut_value.split('-')[0])
            max = int(self.cut_value.split('-')[1])
            co_item = [item for item in co_item if item[1]>= min and item[1]<=max]

        # 取出top item的共现情况
        au_set = set()
        for au in co_item:
            for a in au[0].split(','):
                au_set.add(a)

        # 判断top item的最大出现次数
        s_item = defaultdict(int)
        for item in au_set:
            if item in single_item.keys():
                s_item[item] = single_item[item]
        return dict(co_item), s_item

    def __generate_matrix(self, au_group, au_dict, matrix):
        for key, value in au_group.items():
            A = key.split(',')[0]  # item A
            B = key.split(',')[1]  # item B

            freq = 0
            if self.norm_method ==1:    # 使用绝对数，作为共现次数
                freq = value
            elif self.norm_method == 2: # 使用等价系数法，进行归一化处理
                freq = value*value/(au_dict[A] * au_dict[B])

            matrix.loc[A,A] = au_dict[A]    # 主对角线是单个作者的最大次数
            matrix.loc[B, A] = matrix.loc[A, B] = freq  #更新对称矩阵
        return matrix

    def run(self):

        co_group, single_item_max = self.__items_stat()
        single_items = list(single_item_max.keys())  # 取出所有单个作者
        # 新建一个空矩阵，np.identity()建立一个方阵，对角线是1，其余都是0，类型是float
        matrix = pd.DataFrame(np.identity(len(single_items)), columns=single_items, index=single_items)

        matrix = self.__generate_matrix(co_group, single_item_max, matrix)
        return matrix

# if __name__ == '__main__':
#     co_items = '张三,里斯,和,sd//和,徐徐,里斯,有,sd//有,和,星,b,sd'
#     # co_items = 'a,b,n,g,d,y//v,b,d,a,s//a,n,d,b,s'
#     co_items_list = co_items.split('//')
#     co_items_list = [line.split(',') for line in co_items_list]
#     cooc = CoocMatrix(co_items_list, cut_method=3, cut_value='2-3')
#     print(cooc.run())
