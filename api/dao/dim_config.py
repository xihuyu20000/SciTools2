from typing import Optional, List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger

'''
配置信息表
包括系统自定义的配置信息，也包括用户上传的自定义信息，还包括配置信息的使用策略（系统默认、自定义、合并后的配置）
'''
class DimConfig:
    def __init__(self, userid = '', style='', values=''):
        self.userid = userid
        self.style = style
        self.values = values


class dim_config(BaseDao):

    def __init__(self):
        self.log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_dim_config
        self.create_sql = """
            CREATE TABLE  {}(
            userid String default toString(generateUUIDv4()) COMMENT '主键',
            style String(16) NOT NULL,
            values String
            )ENGINE=MergeTree() ORDER BY (userid);
        """.format(self.TBL_NAME)

    def delete(self, userid, style: str = None):
        sql = """ ALTER TABLE {} DELETE WHERE userid='{}' """.format(self.TBL_NAME, userid)
        if style:
            sql += ' AND style={}'.format(style)
        return self.execute(sql, msg='根据{}和{}删除{}失败'.format(userid, style, self.TBL_NAME))

    def insert(self, params: Optional[List[DimConfig]]):
        sql = "INSERT INTO {} (userid, style, values) VALUES".format(self.TBL_NAME)
        params = [x.__dict__ for x in params]
        return self.execute(sql, params=params, msg='插入{}失败'.format(self.TBL_NAME))


dim_config = dim_config()