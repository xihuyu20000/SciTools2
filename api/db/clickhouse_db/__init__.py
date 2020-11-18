'''
api/db/clickhouse_db 所有的clickhouse数据库操作
安装clickhouse后，需要在/etc/clickhouse-server的配置文件，users.xml中修改password，config.xml中修改host
'''
from typing import Optional
from api import config
from clickhouse_driver import Client, connect


# __conn = connect(host=config.clickhouse_ip, user=config.clickhouse_user, password=config.clickhouse_password,
#                  database=config.clickhouse_db)


def __execute(sql, params: dict = None, msg: str = None):
    try:
        __client = Client(host=config.clickhouse_ip, user=config.clickhouse_user, password=config.clickhouse_password,
                          database=config.clickhouse_db)
        return __client.execute(sql, params=params)
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