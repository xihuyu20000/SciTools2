from typing import Optional, List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger

'''
机构信息表
包括机构名称、机构所在省市
'''
class dim_org(BaseDao):


    def __init__(self):
        self.log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_dim_org
        self.create_sql ="""
            CREATE TABLE  {}(
            orgname String(512) NOT NULL,
            province String(100)
            )ENGINE=MergeTree() ORDER BY (orgname);
        """.format(self.TBL_NAME)


    def insert(self, params: Optional[List[dict]]):
        sql = """ INSERT INTO {} (orgname, province) VALUES """.format(self.TBL_NAME)
        return self.execute(sql, params=params, msg='插入{}失败'.format(self.TBL_NAME))

dim_org = dim_org()