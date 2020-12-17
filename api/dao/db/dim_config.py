from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_dim_config

'''
配置信息表
包括系统自定义的配置信息，也包括用户上传的自定义信息，还包括配置信息的使用策略（系统默认、自定义、合并后的配置）
'''
class DimConfig:
    def __init__(self):
        self.userid = ''
        self.style = ''
        self.values = ''

def create_dim_config():
    """
    创建字典表
    """
    sql = """
            CREATE TABLE  {}(
            userid String(64) NOT NULL,
            style String(16) NOT NULL,
            values String
            )ENGINE=MergeTree() ORDER BY (userid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_dim_config():
    """
    删除字典表
    """
    return __drop(TBL_NAME)


def truncate_dim_config():
    """
    截断字典表
    """
    return __truncate(TBL_NAME)


def insert_dim_config(params: Optional[List[dict]]):
    sql = """ INSERT INTO {} (userid, style, values) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))


def delete_dim_config(userid, style: str = None):
    sql = """ ALTER TABLE {} DELETE WHERE userid='{}' """.format(TBL_NAME, userid)
    if style:
        sql += ' AND style={}'.format(style)
    return __execute(sql, msg='根据{}和{}删除{}失败'.format(userid, style, TBL_NAME))

def find_dim_config(sql):
    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))