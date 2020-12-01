from typing import Optional, List

from api import config
from api.dao.db.clickhouse_db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_dim_user


def create_dim_user():
    """
    创建用户表
    """
    sql = """
            CREATE TABLE  {}(
            id String(64) NOT NULL,
            username String(128) NOT NULL,
            password String(512) NOT NULL
            )ENGINE=MergeTree() ORDER BY (id) PARTITION BY (id);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_dim_user():
    """
    删除用户表
    """
    return __drop(TBL_NAME)


def truncate_dim_user():
    """
    截断用户表
    """
    return __truncate(TBL_NAME)

def insert_dim_user(params: Optional[List[dict]]):
    """
    插入用户表
    """
    sql = """ INSERT INTO {} (id, username, password) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def get_user(username:str, password:str):
    """
    根据用户名和密码查询
    """
    sql = """
        SELECT * FROM {} WHERE username='{}' AND password='{}' 
    """.format(TBL_NAME, username, password)

    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))