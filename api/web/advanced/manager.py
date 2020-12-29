from typing import List

import pymysql
from pydantic.main import BaseModel

from api.dao.ad_tbls import AdTblColumn, VxeTableColumn
from api.util.utils import Logger, is_number, isVaildDate, gen_uuid4
from api import dao, const
from api.web import config
import xlrd
from sklearn.preprocessing import OneHotEncoder

class DatasetCleaningForm(BaseModel):
    tblid: str = None
    func: str = None
    newcol: bool = None
    colname: str = None

class FieldsConfigForm(BaseModel):
    tblid: str = None
    dels: List = None
    colArray: List = None


class TblsDatasetForm(BaseModel):
    tblid: str = None
    titles: List = None
    dataset: List = None


class ParseMySQL:
    def __init__(self, host='localhost', port=3306, database='test', user='root', password='admin'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def run(self):
        db = pymysql.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
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
                titles = [AdTblColumn(tit, self.__get_field_style(dataset, i)) for i, tit in enumerate(titles)]

                tblid = gen_uuid4()  # 这是两个表都要用的字段，必须外部生成
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
        sql = "SELECT tblid, pid, tblname, cols FROM {} WHERE userid='{}'".format(const.tbl_ad_tbls, userid)
        return self.dao.query_ad_dataset(sql)

    def query_tbl_by_tblid(self, tblid):
        """
        @return 返回2条记录，第1个是field名称str，第2个是行记录
        """
        sql = "SELECT cols FROM {} WHERE tblid='{}'".format(const.tbl_ad_tbls, tblid)
        ad_tbl = self.dao.query_ad_dataset(sql)
        cols = ad_tbl[0].cols    # str类型
        assert type(cols)==str

        sql = "SELECT tblid, pid, tblname, userid, {} FROM {} WHERE tblid='{}'".format(cols, const.tbl_ad_tbls, tblid)
        resultset = self.dao.query_ad_dataset(sql)
        return cols, resultset[0]

    def rename(self, tblid, tblname):
        sql = "ALTER TABLE {} UPDATE tblname= '{}' WHERE tblid='{}'".format(const.tbl_ad_tbls, tblname, tblid)
        return self.dao.execute_ad_dataset(sql)

    def delete(self, tblid):
        sql = "ALTER TABLE {} DELETE WHERE tblid='{}'".format(const.tbl_ad_dataset, tblid)
        self.dao.execute_ad_dataset(sql)
        sql = "ALTER TABLE {} DELETE WHERE tblid='{}'".format(const.tbl_ad_tbls, tblid)
        self.dao.execute_ad_tbls(sql)

    def query_dataset_by(self, tblid):
        """
        @return 返回值是3个，第1个是标题 dict类型， 第2个是供vxe-table使用的表头 list类型，第3个是数据集 list类型，如下
        标题结构
              { 'c10': ['SrcDatabase-来源库', '文本', '200'],
                'c11': ['Title-题名', '文本', '200'],
                'c12': ['Author-作者', '文本', '200'],
                ......
              }


        vxe-table表头
               [
                  {'field': 'c10', 'title': 'SrcDatabase-来源库', 'style': '文本', 'width': '200px', 'resizable': True, 'sortable': True},
                  {'field': 'c11', 'title': 'Title-题名', 'style': '文本', 'width': '200px', 'resizable': True, 'sortable': True},
                  {'field': 'c12', 'title': 'Author-作者', 'style': '文本', 'width': '200px', 'resizable': True, 'sortable': True},
                  ......
              ]


        数据集  [
                  {'dsid': '00e7dc12-2579-466f-a239-a0d482257abc', 'c10': ['期刊'], 'c11': ['基于改进遗传算法的机器人路径规划'], ......},
                  {'dsid': '01861b52-770f-481a-a600-5f8926b5e4f8', 'c10': ['期刊'], 'c11': ['图书馆古籍阅读推广工作的现状与思考'], ......},
                  {'dsid': '0211111d-0e97-4624-adac-d88f6cd818cb', 'c10': ['期刊'], 'c11': ['模具行业信息'], ......},
                  ......
               ]

        """
        # 查询ad_tbls表，获取列数
        sql = """SELECT cols FROM {} WHERE tblid='{}'""".format(const.tbl_ad_tbls, tblid)
        resultset = self.dao.query_ad_tbls(sql)
        colstr = resultset[0].cols  # 取出记录

        # 查询ad_tbls表，获取元表数据
        sql = "SELECT " + colstr + " FROM {} WHERE tblid='{}'".format(const.tbl_ad_tbls, tblid)
        titles = self.dao.query_ad_tbls(sql)
        titles = titles[0]  # 结果是dict类型
        # print('标题结构', titles)

        # 格式转换
        vxeColumns = []
        for name in str(colstr).split(','):

            value = getattr(titles, name)    # 返回值是list类型
            vxeColumns.append(VxeTableColumn(name, value[0], value[1], value[2]).toVxe())
        # print('表头形式' , vxeColumns)

        # 最后查询ad_dataset表
        sql = """SELECT {} FROM {} WHERE tblid='{}'""".format('dsid,' + colstr, const.tbl_ad_dataset, tblid)
        dataset = self.dao.query_ad_dataset(sql)
        # print('数据集', dataset[:3])

        return titles, vxeColumns, dataset


    def cleaning_dataset(self, form:DatasetCleaningForm):
        titles, _, dataset = self.query_dataset_by(form.tblid)
        values = [row[form.colname] for row in dataset]

        max_len = 0
        for i, row in enumerate(values):
            row = row[0]
            row = row.split(';')
            row = [word for word in row if word]
            row = row if type(row)==list else [row]
            if len(row)>max_len:
                max_len = len(row)
            values[i] = row

        for i,row in enumerate(values):
            for i in range(max_len-len(row)):
                row.append('')
            values[i] = row

        ohenc = OneHotEncoder()
        ohenc.fit(values)
        for i, row in enumerate(values):
            print(i, row, ohenc.transform([row]).toarray())

    def update_tbl_dataset(self, form: TblsDatasetForm):
        # print('传入的表单数据集', form)
        _, adtbl = self.query_tbl_by_tblid(form.tblid)
        self.delete(form.tblid)


        adTblColumns = [AdTblColumn(title['title'], title['style'], title['width']) for title in form.titles if str(title['field']).startswith('c')]
        dao.insert_ad_tbls(form.tblid, adtbl['userid'], adtbl['tblname'], adTblColumns)

        '''
        页面传入的数据集结构
        [
           {'dsid': '01cc781b-1f68-4381-9f54-0b0c40b10bd0', 'c17': ['2020-12-10'], 'c10': ['期刊'], 'c11': ['“医学继续教育”答题'], 'c12': [''], 'c13': ['上海医药'], 'c14': ['上海医药'], 'c15': ['医学继续教育;医学影像分析;'], ......
           ......
        ]
        '''
        cols, adtbl = self.query_tbl_by_tblid(form.tblid)
        values = []
        for row in form.dataset:
            row_values = []
            for name in cols.split(','):
                v = row[name][0]
                row_values.append(v)
            values.append(row_values)
        dao.insert_ad_dataset(form.tblid, values)

    def saveAsNew_tbl_dataset(self, form: TblsDatasetForm):
        # print('传入的表单数据集', form)
        _, adtbl = self.query_tbl_by_tblid(form.tblid)

        new_tblid = gen_uuid4()
        adTblColumns = [AdTblColumn(title['title'], title['style'], title['width']) for title in form.titles if str(title['field']).startswith('c')]
        dao.insert_ad_tbls(new_tblid, adtbl['userid'], adtbl['tblname']+'(新)', adTblColumns)

        '''
        页面传入的数据集结构
        [
           {'dsid': '01cc781b-1f68-4381-9f54-0b0c40b10bd0', 'c17': ['2020-12-10'], 'c10': ['期刊'], 'c11': ['“医学继续教育”答题'], 'c12': [''], 'c13': ['上海医药'], 'c14': ['上海医药'], 'c15': ['医学继续教育;医学影像分析;'], ......
           ......
        ]
        '''
        cols, adtbl = self.query_tbl_by_tblid(form.tblid)
        values = []
        for row in form.dataset:
            row_values = []
            for name in cols.split(','):
                v = row[name][0]
                row_values.append(v)
            values.append(row_values)
        dao.insert_ad_dataset(new_tblid, values)


    def updateFieldConfig(self, form: FieldsConfigForm):
        # 更新列名
        cols = ','.join([data['field'] for data in form.colArray])
        sql = "ALTER TABLE {} UPDATE cols='{}' WHERE tblid='{}'".format(const.tbl_ad_tbls, cols, form.tblid)
        dao.execute_ad_tbls(sql)

        # 更新每个字段的内容
        sql = "ALTER TABLE {} UPDATE {}={} WHERE tblid='{}'"
        for i, row in enumerate(form.colArray):
            value = AdTblColumn(row['title'], row['style'], row['width']).toch()
            sql1 = sql.format(const.tbl_ad_tbls, row['field'], list(value), form.tblid)
            dao.execute_ad_tbls(sql1)


advancedManager = AdvancedManager()
