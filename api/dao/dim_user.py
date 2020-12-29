from typing import Optional, List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger


class dim_user(BaseDao):

    def __init__(self):
        self._log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_dim_user
        self._create_sql = """
                CREATE TABLE  {}(
                userid String DEFAULT toString(generateUUIDv4()) COMMENT '主键',
                username String(128) NOT NULL,
                password String(512) NOT NULL
                )ENGINE=MergeTree() ORDER BY (userid);
            """.format(self.TBL_NAME)


    def insert(self, sql, params: Optional[List[dict]]):
        """
        插入用户表
        """
        return self.execute(sql, params=params, msg='插入{}失败'.format(self.TBL_NAME))

    def get_user(self, username:str, password:str):
        """
        根据用户名和密码查询
        """
        sql = """
            SELECT * FROM {} WHERE username='{}' AND password='{}' 
        """.format(self.TBL_NAME, username, password)

        return self.query(sql, params=None, msg='查询{}失败'.format(self.TBL_NAME))


dim_user = dim_user()