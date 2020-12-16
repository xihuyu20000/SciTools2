'''
api/db/clickhouse_db 所有的clickhouse数据库操作
安装clickhouse后，需要在/etc/clickhouse-server的配置文件，users.xml中修改password，config.xml中修改host
'''
# import pandas as pd
from typing import Optional
from api import config
from clickhouse_driver import Client


def __get_client():
    return Client(host=config.clickhouse_ip, user=config.clickhouse_user, password=config.clickhouse_password,
           database=config.clickhouse_db)

def __execute(sql, params: dict = None, msg: str = None):
    return __get_client().execute(sql, params=params)


def __query(sql, params: dict = None, msg: str = None, result_style: str = 'dict'):
    result, columns = __get_client().execute(sql, params=params, with_column_types=True, settings={'max_block_size': 100000})
    labels = [x[0] for x in columns]
    if result_style == 'dict':
        return [dict(zip(labels, x)) for x in result]
    if result_style == 'list':
        return [labels] + result
    return result



def __create(sql, tbl_name):
    return __execute(sql, msg='创建表{}失败'.format(tbl_name))


def __drop(tbl_name):
    sql = """
            DROP TABLE IF EXISTS {};
        """.format(tbl_name)
    return __execute(sql, msg='删除表{}失败'.format(tbl_name))


def __truncate(tbl_name):
    sql = """
        TRUNCATE TABLE IF EXISTS {};
    """.format(tbl_name)
    return __execute(sql, msg='截断表{}失败'.format(tbl_name))
