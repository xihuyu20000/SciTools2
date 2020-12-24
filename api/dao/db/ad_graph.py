from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __execute, __query
from api.util.utils import gen_uuid4

TBL_NAME = config.tbl_ad_graphs
'''
高级图表：图表定义。
'''
create_sql = """
    CREATE TABLE ad_graphs(
        graphid String DEFAULT toString(generateUUIDv4()) COMMENT '主键',
        userid String NOT NULL COMMENT '用户表主键',
        tblid String NOT NULL COMMENT '数据元表主键',
        graphname String COMMENT '表名称',
        option String COMMENT 'echarts的配置项目'
    ) ENGINE = MergeTree() PARTITION  BY graphid ORDER BY graphid PRIMARY KEY graphid
"""

def create():
    __create(create_sql, TBL_NAME)


def drop():
    __drop(TBL_NAME)


def execute(sql, params=None):
    return __execute(sql, params)


def query(sql, params=None, result_style='dict'):
    return __query(sql, params, result_style=result_style)

