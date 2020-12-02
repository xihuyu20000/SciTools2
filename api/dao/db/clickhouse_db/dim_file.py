from typing import Optional, List

from api import config
from api.dao.db.clickhouse_db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_dim_file


def create_dim_file():
    """
    创建文件表
    """
    sql = """
            CREATE TABLE  {}(
            fileid String(64) NOT NULL,
            pid String(64) ,
            filename String(128) NOT NULL
            )ENGINE=MergeTree() ORDER BY (fileid) PARTITION BY (fileid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_dim_file():
    """
    删除文件表
    """
    return __drop(TBL_NAME)


def truncate_dim_file():
    """
    截断文件表
    """
    return __truncate(TBL_NAME)


def insert_dim_file(params: Optional[List[dict]]):
    """
    插入文件表
    """
    sql = """ INSERT INTO {} (fileid, filename) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def find_all_names(sql):
    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))
