from typing import List

import pymysql
from pydantic.main import BaseModel

from api.dao.db.ad_tbls import build_ad_tbl_insert
from api.util.utils import Logger, is_number, isVaildDate, gen_uuid4
from api import dao, config
import xlrd


class FieldsConfigForm(BaseModel):
    tblid:str = None
    dels: List = None
    dataArray :List= None

class ParseMySQL:
    def __init__(self, host='localhost', port=3306, database='test', user='root', password='admin'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def run(self):
        db = pymysql.connect(host = self.host, port= self.port, database = self.database, user = self.user, password = self.password)
        cursor = db.cursor()

        # todo 在这里查询表结构和数据，并写入到ch中

        cursor.close()
        db.close()


class ParseExcel:
    def __init__(self, userid, path, firstTitle=True):
        '''
        @param  path : excel文件路径
        @param  firstTitle : 第一行是表头
        '''
        self.log = Logger(__name__).get_log
        self.dao = dao
        self.userid = userid
        self.path = path
        self.firstTitle = firstTitle

    def run(self):
        book = xlrd.open_workbook(self.path)
        names = book.sheet_names()
        for name in names:
            sheet = book.sheet_by_name(name)
            rows = sheet.nrows  # 行数
            if rows:
                titles = self.__titles(sheet)
                dataset = self.__dataset(sheet)
                # cxx数组中的元素分别是[标题, 类型, 宽度, 顺序号]
                titles = [build_ad_tbl_insert(tit, self.__get_field_style(dataset, i), '200', str(i)) for i, tit in enumerate(titles)]

                tblid = gen_uuid4() # 这是两个表都要用的字段，必须外部生成
                tbl_name = name  # sheet名作为表名
                dao.insert_ad_tbls(tblid, self.userid, tbl_name, titles)
                dao.insert_ad_dataset(tblid, dataset)

    def __get_field_style(self, dataset, i):
        # 类型有：数值、日期、文本
        for row in dataset:
            value = row[i]
            if value:
                value = str(value).strip()
                if is_number(value):
                    return '数值'
                elif isVaildDate(value):
                    return '日期'
                return '文本'

    def __titles(self, sheet):
        # 获取列名称
        if self.firstTitle:
            return [sheet.cell_value(0, i) for i in range(0, sheet.ncols)]
        return ['col{}'.format(i) for i in range(0, sheet.ncols)]

    def __dataset(self, sheet):
        # 获取数据集
        startRow = 1 if self.firstTitle else 0
        dataset = []
        for i in range(startRow, sheet.nrows):
            dataset.append([sheet.cell_value(i, j) for j in range(0, sheet.ncols)])
        return dataset


class AdvancedManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    def parseExcel(self, userid, path):
        ParseExcel(userid, path, firstTitle=True).run()

    def find_tbl_by_userid(self, userid):
        sql = "select tblid, pid, tblname, cols from {} where userid='{}'".format(config.tbl_ad_tbls, userid)
        return self.dao.query_ad_dataset(sql)

    def find_tbl_by_tblid(self, tblid):
        sql = "select cols from {} where tblid='{}'".format(config.tbl_ad_tbls, tblid)
        ad_tbl = self.dao.query_ad_dataset(sql)
        cols = ad_tbl[0]['cols']
        sql = """select tblid, pid, tblname, {} from {} where tblid='{}'""".format(cols, config.tbl_ad_tbls, tblid)
        return self.dao.query_ad_dataset(sql)


    def rename(self, tblid, tblname):
        sql = "ALTER TABLE {} UPDATE tblname= '{}' WHERE tblid='{}'".format(config.tbl_ad_tbls, tblname, tblid)
        return self.dao.execute_ad_dataset(sql)

    def delete(self, tblid):
        sql = "ALTER TABLE {} DELETE WHERE tblid='{}'".format(config.tbl_ad_dataset, tblid)
        self.dao.execute_ad_dataset(sql)
        sql = "ALTER TABLE {} DELETE WHERE tblid='{}'".format(config.tbl_ad_tbls, tblid)
        self.dao.execute_ad_tbls(sql)

    def query_dataset_by(self, tblid):
        # 查询ad_tbls表，获取列数
        sql = """SELECT cols FROM {} WHERE tblid='{}'""".format(config.tbl_ad_tbls, tblid)
        cols = self.dao.query_ad_tbls(sql)
        colstr = cols[0]['cols'] # 取出记录

        # 查询ad_tbls表，获取元表数据
        sql = "SELECT "+colstr+" FROM {} WHERE tblid='{}'".format(config.tbl_ad_tbls, tblid)
        titles = self.dao.query_ad_tbls(sql)
        titles = titles[0]
        # print('标题结构', titles)

        # 最后查询ad_dataset表
        sql = """SELECT {} FROM {} WHERE tblid='{}'""".format('dsid,'+colstr, config.tbl_ad_dataset, tblid)
        dataset = self.dao.query_ad_dataset(sql)
        # print('数据集', dataset)

        return titles, dataset

    def updateFieldConfig(selff,form):
        # 更新列名
        cols = ','.join([data['field'] for data in form.dataArray])
        sql = """ALTER TABLE {} UPDATE cols='{}' WHERE tblid='{}'""".format(config.tbl_ad_tbls, cols, form.tblid)
        dao.execute_ad_tbls(sql)
        # 更新每个字段的内容
        sql = """ALTER TABLE {} UPDATE {}={} WHERE tblid='{}'"""
        for i, row in enumerate(form.dataArray):
            value = list(build_ad_tbl_insert(row['title'], row['style'], row['width'], str(i)))
            sql1 = sql.format(config.tbl_ad_tbls, row['field'], value, form.tblid)
            dao.execute_ad_tbls(sql1)

advancedManager = AdvancedManager()
