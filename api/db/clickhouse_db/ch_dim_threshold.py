from typing import Optional, List

from api import config
from api.db.clickhouse_db import __create, __drop, __truncate, __execute, __query


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
        """.format(config.tbl_dim_threshold)
    return __create(sql, config.tbl_dim_threshold)

def drop_dim_threshold():
    """
    删除阈值表
    """
    return __drop(config.tbl_dim_threshold)

def truncate_dim_threshold():
    """
    截断阈值表
    """
    return __truncate(config.tbl_dim_threshold)

def insert_dim_threshold(params: Optional[List[dict]]):
    """
    插入阈值表
    """
    sql = """
        INSERT INTO {} (fileid, name, value) VALUES
    """.format(config.tbl_dim_threshold)
    return __execute(sql, params=params, msg='插入{}失败'.format(config.tbl_dim_threshold))

def delete_dim_threshold(file_id):
    """
    删除阈值表
    """
    sql = """ DELETE FROM {} WHERE fileid={} """.format(config.tbl_dim_threshold, file_id)
    return __execute(sql, msg='根据{}删除{}失败'.format(file_id, config.tbl_dim_threshold))


def find_dim_threshold(params: Optional[dict] = None):
    sql = """
        SELECT * FROM {} WHERE 1=1 
    """.format(config.tbl_dim_threshold)
    return __query(sql, params=params, msg='查询{}失败'.format(config.tbl_dim_threshold))
