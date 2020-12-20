from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __execute, __query

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

create_sql = """
    CREATE TABLE  {}(
    userid UUID default generateUUIDv4() COMMENT '主键',
    style String(16) NOT NULL,
    values String
    )ENGINE=MergeTree() ORDER BY (userid);
""".format(TBL_NAME)

def create():
    return __create(create_sql, TBL_NAME)

def drop():
    return __drop(TBL_NAME)

def insert(sql, params: Optional[List[dict]]):
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def delete(userid, style: str = None):
    sql = """ ALTER TABLE {} DELETE WHERE userid='{}' """.format(TBL_NAME, userid)
    if style:
        sql += ' AND style={}'.format(style)
    return __execute(sql, msg='根据{}和{}删除{}失败'.format(userid, style, TBL_NAME))

def query(sql):
    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))