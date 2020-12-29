from typing import List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger


'''
高级图表：数据表
'''

class ad_dataset(BaseDao):
    def __init__(self):
        self._log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_ad_dataset
        self._create_sql = """
            CREATE TABLE ad_dataset(
                dsid String default toString(generateUUIDv4()) COMMENT '主键',
                tblid String NOT NULL COMMENT '元表主键',
                c10 Array(String) COMMENT '列名，列类型',
                c11 Array(String) COMMENT '列名，列类型',
                c12 Array(String) COMMENT '列名，列类型',
                c13 Array(String) COMMENT '列名，列类型',
                c14 Array(String) COMMENT '列名，列类型',
                c15 Array(String) COMMENT '列名，列类型',
                c16 Array(String) COMMENT '列名，列类型',
                c17 Array(String) COMMENT '列名，列类型',
                c18 Array(String) COMMENT '列名，列类型',
                c19 Array(String) COMMENT '列名，列类型',
                c20 Array(String) COMMENT '列名，列类型',
                c21 Array(String) COMMENT '列名，列类型',
                c22 Array(String) COMMENT '列名，列类型',
                c23 Array(String) COMMENT '列名，列类型',
                c24 Array(String) COMMENT '列名，列类型',
                c25 Array(String) COMMENT '列名，列类型',
                c26 Array(String) COMMENT '列名，列类型',
                c27 Array(String) COMMENT '列名，列类型',
                c28 Array(String) COMMENT '列名，列类型',
                c29 Array(String) COMMENT '列名，列类型',
                c30 Array(String) COMMENT '列名，列类型',
                c31 Array(String) COMMENT '列名，列类型',
                c32 Array(String) COMMENT '列名，列类型',
                c33 Array(String) COMMENT '列名，列类型',
                c34 Array(String) COMMENT '列名，列类型',
                c35 Array(String) COMMENT '列名，列类型',
                c36 Array(String) COMMENT '列名，列类型',
                c37 Array(String) COMMENT '列名，列类型',
                c38 Array(String) COMMENT '列名，列类型',
                c39 Array(String) COMMENT '列名，列类型',
                c40 Array(String) COMMENT '列名，列类型',
                c41 Array(String) COMMENT '列名，列类型',
                c42 Array(String) COMMENT '列名，列类型',
                c43 Array(String) COMMENT '列名，列类型',
                c44 Array(String) COMMENT '列名，列类型',
                c45 Array(String) COMMENT '列名，列类型',
                c46 Array(String) COMMENT '列名，列类型',
                c47 Array(String) COMMENT '列名，列类型',
                c48 Array(String) COMMENT '列名，列类型',
                c49 Array(String) COMMENT '列名，列类型',
                c50 Array(String) COMMENT '列名，列类型',
                c51 Array(String) COMMENT '列名，列类型',
                c52 Array(String) COMMENT '列名，列类型',
                c53 Array(String) COMMENT '列名，列类型',
                c54 Array(String) COMMENT '列名，列类型',
                c55 Array(String) COMMENT '列名，列类型',
                c56 Array(String) COMMENT '列名，列类型',
                c57 Array(String) COMMENT '列名，列类型',
                c58 Array(String) COMMENT '列名，列类型',
                c59 Array(String) COMMENT '列名，列类型',
                c60 Array(String) COMMENT '列名，列类型'
            ) ENGINE = MergeTree() PARTITION BY tblid ORDER BY dsid PRIMARY KEY dsid
        """

    def insert(self, tblid, dataset: List[List[str]]):
        '''
        @param tblid : 元表id
        @param dataset : 数据集，这是页面表格传递过来的二维数组，数值类型是str
        '''
        colstr = 'tblid, ' + ', '.join(['c' + str(10 + i) for i in range(len(dataset[0]))])
        sql = 'INSERT INTO {table_name} ({fields}) VALUES '.format(table_name=self.TBL_NAME, fields=colstr)

        dataset2 = []
        for i, row in enumerate(dataset):
            row = [[col] for col in row]  # 因为列字段是数组类型，所以插入到每个字段的，必须是一个list
            row.insert(0, tblid)  # 第一列是tblid字段
            dataset2.append(row)
        return self.execute(sql, dataset2)

ad_dataset = ad_dataset()