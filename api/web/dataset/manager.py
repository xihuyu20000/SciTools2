import sys
from collections import defaultdict

from pydantic.main import BaseModel

from api.util.utils import Logger
from api import dao, config
from api.dao.db.clickhouse_db import __execute as execute

class OdsbibDeleteForm(BaseModel):
    ids:list= []

class OdsbibUpdateForm(BaseModel):
    id:str = None
    k:str = None
    v:str = None

class DatasetManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    # 查询所有数据集的名称
    def list_names(self):
        sql = """ SELECT * FROM {} """.format(config.tbl_dim_dataset)
        self.log.info(sql)
        return self.dao.find_all_names(sql)

    # 根据特定数据集
    def list_dataset(self, dsid):
        sql = "SELECT * FROM {} WHERE dsid ='{}'".format(config.tbl_ods_bib, dsid)
        self.log.info(sql)
        return self.dao.find_ods_bib(sql)

    # 根据dsid删除数据集
    def delete(self, dsid):
        sql = "ALTER TABLE  {} DELETE WHERE dsid = '{}'".format(config.tbl_dim_dataset, dsid)
        self.log.info(sql)
        execute(sql)
        sql = "ALTER TABLE  {} DELETE WHERE dsid='{}'".format(config.tbl_ods_bib, dsid)
        self.log.info(sql)
        execute(sql)

    # 修改数据集名称
    def rename(self, dsid, newName):
        sql = "ALTER TABLE {} UPDATE dsname='{}' WHERE dsid = '{}'".format(config.tbl_dim_dataset, newName, dsid)
        self.log.info(sql)
        execute(sql)

    # 删除ods_bib表中的数据
    def deleteOdsbibById(self, ids):
        for id in ids:
            sql = "ALTER TABLE  {} DELETE WHERE id = '{}'".format(config.tbl_ods_bib, id)
            self.log.info(sql)
            execute(sql)

    # 更新ods_bib表中的数据
    def updateOdsbib(self, form):
        print(form)
        if form.k in ['authors','orgs','funds','clcs']:   # 如果类型是数组，使用这个语句
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib,form.k, form.v.split(','), form.id)
        else:
            sql = "ALTER TABLE {} UPDATE {}='{}' WHERE id='{}'".format(config.tbl_ods_bib, form.k, form.v, form.id)
        self.log.info(sql)
        execute(sql)




datasetManager = DatasetManager()