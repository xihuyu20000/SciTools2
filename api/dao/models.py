from typing import List

from clickhouse_driver import Client

from api import const
from api.util.utils import Logger

'''
api/db/clickhouse_db 所有的clickhouse数据库操作
安装clickhouse后，需要在/etc/clickhouse-server的配置文件，users.xml中修改password，config.xml中修改host
'''
class BaseDao:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.create_sql = ''
        self.TBL_NAME = ''

    def __get_client(self):
        return Client(host=const.clickhouse_ip, user=const.clickhouse_user, password=const.clickhouse_password,
                      database=const.clickhouse_db)

    def execute(self, sql, params: dict = None, msg: str = None):
        self.log.info(sql)
        return self.__get_client().execute(sql, params=params, with_column_types=True, settings={'max_block_size': 100000})

    def query(self, sql, params: dict = None, msg: str = None, result_style: str = 'dict'):
        result, columns = self.execute(sql, params=params)
        labels = [x[0] for x in columns]
        if result_style == 'dict':
            return [dict(zip(labels, x)) for x in result]
        if result_style == 'list':
            return [labels] + result
        return result

    def create(self):
        return self.execute(self.create_sql, msg='创建表{}失败'.format(self.TBL_NAME))

    def drop(self):
        sql = """DROP TABLE IF EXISTS {};""".format(self.TBL_NAME)
        return self.execute(sql, msg='删除表{}失败'.format(self.TBL_NAME))

    def update(self, sql, params=None):
        return self.execute(sql, params=params, msg='更新{}失败'.format(self.TBL_NAME))

