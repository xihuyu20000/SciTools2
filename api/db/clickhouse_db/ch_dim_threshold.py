from typing import Optional, List

from api import config
from api.db.clickhouse_db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_dim_threshold
def create_dim_threshold():
    """
    创建阈值表
    """
    sql = """
            CREATE TABLE  {}(
            fileid String(64) NOT NULL,
            name String(128) NOT NULL,
            value String(512) NOT NULL
            )ENGINE=MergeTree() ORDER BY (name) PARTITION BY (fileid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)

def drop_dim_threshold():
    """
    删除阈值表
    """
    return __drop(TBL_NAME)

def truncate_dim_threshold():
    """
    截断阈值表
    """
    return __truncate(TBL_NAME)

def insert_dim_threshold(params: Optional[List[dict]]):
    """
    插入阈值表
    """
    sql = """
        INSERT INTO {} (fileid, name, value) VALUES
    """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def delete_dim_threshold(file_id):
    """
    删除阈值表
    """
    sql = """ DELETE FROM {} WHERE fileid={} """.format(TBL_NAME, file_id)
    return __execute(sql, msg='根据{}删除{}失败'.format(file_id, TBL_NAME))


def find_dim_threshold(params: Optional[dict] = None):
    sql = """
        SELECT * FROM {} WHERE 1=1 
    """.format(TBL_NAME)
    return __query(sql, params=params, msg='查询{}失败'.format(TBL_NAME))
