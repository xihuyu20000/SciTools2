from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __execute, __query
from api.util.utils import gen_uuid4

TBL_NAME = config.tbl_ad_tbls
'''
高级图表：元数据表
'''
create_sql = """
    CREATE TABLE ad_tbls(
        tblid String DEFAULT toString(generateUUIDv4()) COMMENT '主键',
        pid String COMMENT '父主键',
        userid String NOT NULL COMMENT '用户表主键',
        tblname String COMMENT '表名称',
        cols UInt32 COMMENT '数据表的列数',
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
    ) ENGINE = MergeTree() ORDER BY tblid PRIMARY KEY tblid
"""

def create():
    __create(create_sql, TBL_NAME)

def drop():
    __drop(TBL_NAME)

def execute(sql, params=None):
    return __execute(sql, params)

def query(sql, params=None, result_style = 'dict'):
    return __query(sql, params, result_style=result_style)

def insert(tblid, userid, tbl_name, titles):
    '''
    @param tbid 一定是自动生成的id
    @param userid 一定是用户的id
    @param tbl_name 表名
    @param titles 表头数据
    '''
    colstr = ', '.join([ 'c'+str(10+i) for i in range(len(titles))])
    sql = """INSERT INTO {} ( tblid, userid, tblname, cols, {}) VALUES""".format(TBL_NAME, colstr)
    values = [tblid, userid, tbl_name, len(titles)]
    values.extend(titles)   # 合并list
    values = [values]   # 必须放入到一个list中
    return __execute(sql, params=values)

