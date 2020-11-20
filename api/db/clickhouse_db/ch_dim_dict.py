from typing import Optional, List

from api import config
from api.db.clickhouse_db import __create, __drop, __truncate, __execute

TBL_NAME = config.tbl_dim_dict


def create_dim_dict():
    """
    创建字典表
    """
    sql = """
            CREATE TABLE  {}(
            fileid String(64) NOT NULL,
            style String(16) NOT NULL,
            values Array(String),
            alias String(512)
            )ENGINE=MergeTree() ORDER BY (style) PARTITION BY (fileid);
        """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_dim_dict():
    """
    删除字典表
    """
    return __drop(TBL_NAME)


def truncate_dim_dict():
    """
    截断字典表
    """
    return __truncate(TBL_NAME)


def insert_dim_dict(params: Optional[List[dict]]):
    sql = """ INSERT INTO {} (fileid, style, values, alias) VALUES """.format(TBL_NAME)
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))


def delete_dim_dict(file_id, style: str = None):
    sql = """ DELETE FROM {} WHERE fileid={} """.format(TBL_NAME, file_id)
    if style:
        sql += ' AND style={}'.format(style)
    return __execute(sql, msg='根据{}和{}删除{}失败'.format(file_id, style, TBL_NAME))
