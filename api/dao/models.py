import copy
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
        self._log = Logger(__name__).get_log
        self._create_sql = ''
        self.TBL_NAME = ''

    def execute(self, sql, params: dict = None, msg: str = None):
        self._log.info(sql)
        client = Client(host=const.clickhouse_ip, user=const.clickhouse_user, password=const.clickhouse_password,
                      database=const.clickhouse_db)
        return client.execute(sql, params=params, with_column_types=True, settings={'max_block_size': 100000})

    def query(self, sql:str, params: dict = None, msg: str = None, result_style: str = 'dict'):
        sql = sql.format(table = self.TBL_NAME)
        result, columns = self.execute(sql, params=params)
        labels = [x[0] for x in columns]
        if result_style == 'dict':
            objs = []
            for x in result:
                obj = object.__new__(self.__class__)
                obj.from_db(dict(zip(labels, x)))
                objs.append(obj)
            return objs
        if result_style == 'list':
            return [labels] + result
        return result

    def create(self):
        return self.execute(self._create_sql, msg='创建表{}失败'.format(self.TBL_NAME))

    def drop(self):
        sql = """DROP TABLE IF EXISTS {};""".format(self.TBL_NAME)
        return self.execute(sql, msg='删除表{}失败'.format(self.TBL_NAME))

    def update(self, sql, params=None):
        return self.execute(sql, params=params, msg='更新{}失败'.format(self.TBL_NAME))

    def dict(self):
        dd = self.__dict__
        for k in ['_log', '_create_sql', 'TBL_NAME']:
            if k in dd.keys():
                del dd[k]
        return dd

    def __repr__(self):
        return str(self.__dict__)

    def from_db(self, data):
        for key,value in data.items():   # 遍历数据字典
            setattr(self,key,value)  # 则添加属性到对象中

