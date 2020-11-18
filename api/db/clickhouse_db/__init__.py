'''
api/db/clickhouse_db 所有的clickhouse数据库操作
安装clickhouse后，需要在/etc/clickhouse-server的配置文件，users.xml中修改password，config.xml中修改host
'''
import pandas as pd
from typing import Optional
from api import config
from clickhouse_driver import Client, connect


__client = Client(host=config.clickhouse_ip, user=config.clickhouse_user, password=config.clickhouse_password, database=config.clickhouse_db)
# __conn = connect(host=config.clickhouse_ip, user=config.clickhouse_user, password=config.clickhouse_password,
#                  database=config.clickhouse_db)


def __execute(sql, params: dict = None, msg: str = None):
    try:
        return __client.execute(sql, params=params)
    except Exception as e:
        print(e)
        raise Exception(msg)

def __query(sql,params: dict = None, msg: str = None):
    # 150，设置打印宽度
    pd.set_option('display.width', 180)
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)


    try:
        result, columns = __client.execute(sql, params=params, with_column_types=True)
        df = pd.DataFrame(result, columns=[t[0] for t in columns])
        return df
    except Exception as e:
        print(e)
        raise Exception(msg)

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