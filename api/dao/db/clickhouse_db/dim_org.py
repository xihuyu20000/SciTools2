from typing import Optional, List

from api import config
from api.dao.db.clickhouse_db import __create, __drop, __truncate, __execute

TBL_NAME = config.tbl_dim_org

'''
机构信息表
包括机构名称、机构所在省市
'''

def create_dim_org():
    """
    创建机构表
    """
    sql = """
            CREATE TABLE  {}(
            orgid String(64) NOT NULL,
            orgname String(512) NOT NULL,
            province String(100)
            )ENGINE=MergeTree() ORDER BY (orgid) PARTITION BY (orgid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_dim_org():
    """
    删除机构表
    """
    return __drop(TBL_NAME)


def truncate_dim_org():
    """
    截断机构表
    """
    return __truncate(TBL_NAME)


def insert_dim_org(params: Optional[List[dict]]):
    sql = """ INSERT INTO {} (orgid, orgname, province) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))
