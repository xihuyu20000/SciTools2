
from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_dim_dataset

'''
数据集，
表示用户一次性上传的数据集，也包括用户etl后产生的数据集。
数据集是进行数据分析和图表展示的数据来源。
'''

def create():
    """
    创建数据集表
    """
    sql = """
            CREATE TABLE  {}(
            dsid UUID default generateUUIDv4() COMMENT '主键',
            pid UUID,
            dsname String(128) NOT NULL,
            status String(64) 
            )ENGINE=MergeTree() ORDER BY (dsid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop():
    """
    删除文件表
    """
    return __drop(TBL_NAME)

def insert(params: Optional[List[dict]]):
    """
    插入文件表
    """
    sql = """ INSERT INTO {} (dsid, dsname, status) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def query(sql):
    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))

def update(sql):
    return __execute(sql, params=None, msg='更新{}失败'.format(TBL_NAME))