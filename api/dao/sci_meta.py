
from typing import Optional, List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger

'''
数据集，
表示用户一次性上传的数据集，也包括用户etl后产生的数据集。
数据集是进行数据分析和图表展示的数据来源。
'''
class sci_meta(BaseDao):

    def __init__(self):
        self._log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_sci_meta
        self._create_sql = """
            CREATE TABLE  {}(
            dsid String default toString(generateUUIDv4()) COMMENT '主键',
            pid String ,
            dsname String NOT NULL,
            status String
            )ENGINE=MergeTree() ORDER BY (dsid);
        """.format(self.TBL_NAME)

    def insert(self, params: Optional[List[dict]]):
        """
        插入文件表
        """
        sql = """ INSERT INTO {} (dsid, dsname, status) VALUES """.format(self.TBL_NAME)
        return self.execute(sql, params=params, msg='插入{}失败'.format(self.TBL_NAME))

    def update(self,sql):
        return self.execute(sql, msg='更新{}失败'.format(self.TBL_NAME))

sci_meta = sci_meta()