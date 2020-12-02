import sys
from collections import defaultdict
from api.util.utils import Logger
from api import dao, config


class StatManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    # 查询所有数据集的名称
    def list_names(self):
        sql = """ SELECT * FROM {} """.format(config.tbl_dim_file)
        self.log.info(sql)
        return self.dao.find_all_names(sql)

    # 根据特定数据集
    def list_dataset(self, fileId):
        sql = "SELECT * FROM {} WHERE fileid ='{}'".format(config.tbl_ods_bib, fileId)
        self.log.info(sql)
        return self.dao.find_ods_bib(sql)


statManager = StatManager()