from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __execute, __query
from api.util.utils import gen_uuid4

TBL_NAME = config.tbl_ad_tbls
'''
高级图表：元数据表。
cxx数组中的元素分别是[ 标题, 类型, 宽度 ]
'''
create_sql = """
    CREATE TABLE ad_tbls(
        tblid String DEFAULT toString(generateUUIDv4()) COMMENT '主键',
        pid String COMMENT '父主键',
        userid String NOT NULL COMMENT '用户表主键',
        tblname String COMMENT '表名称',
        cols String COMMENT '数据表的有效列',
        c10 Array(String) COMMENT '列名，列类型',
        c11 Array(String) COMMENT '列名，列类型',
        c12 Array(String) COMMENT '列名，列类型',
        c13 Array(String) COMMENT '列名，列类型',
        c14 Array(String) COMMENT '列名，列类型',
        c15 Array(String) COMMENT '列名，列类型',
        c16 Array(String) COMMENT '列名，列类型',
        c17 Array(String) COMMENT '列名，列类型',
        c18 Array(String) COMMENT '列名，列类型',
        c19 Array(String) COMMENT '列名，列类型',
        c20 Array(String) COMMENT '列名，列类型',
        c21 Array(String) COMMENT '列名，列类型',
        c22 Array(String) COMMENT '列名，列类型',
        c23 Array(String) COMMENT '列名，列类型',
        c24 Array(String) COMMENT '列名，列类型',
        c25 Array(String) COMMENT '列名，列类型',
        c26 Array(String) COMMENT '列名，列类型',
        c27 Array(String) COMMENT '列名，列类型',
        c28 Array(String) COMMENT '列名，列类型',
        c29 Array(String) COMMENT '列名，列类型',
        c30 Array(String) COMMENT '列名，列类型',
        c31 Array(String) COMMENT '列名，列类型',
        c32 Array(String) COMMENT '列名，列类型',
        c33 Array(String) COMMENT '列名，列类型',
        c34 Array(String) COMMENT '列名，列类型',
        c35 Array(String) COMMENT '列名，列类型',
        c36 Array(String) COMMENT '列名，列类型',
        c37 Array(String) COMMENT '列名，列类型',
        c38 Array(String) COMMENT '列名，列类型',
        c39 Array(String) COMMENT '列名，列类型',
        c40 Array(String) COMMENT '列名，列类型',
        c41 Array(String) COMMENT '列名，列类型',
        c42 Array(String) COMMENT '列名，列类型',
        c43 Array(String) COMMENT '列名，列类型',
        c44 Array(String) COMMENT '列名，列类型',
        c45 Array(String) COMMENT '列名，列类型',
        c46 Array(String) COMMENT '列名，列类型',
        c47 Array(String) COMMENT '列名，列类型',
        c48 Array(String) COMMENT '列名，列类型',
        c49 Array(String) COMMENT '列名，列类型',
        c50 Array(String) COMMENT '列名，列类型',
        c51 Array(String) COMMENT '列名，列类型',
        c52 Array(String) COMMENT '列名，列类型',
        c53 Array(String) COMMENT '列名，列类型',
        c54 Array(String) COMMENT '列名，列类型',
        c55 Array(String) COMMENT '列名，列类型',
        c56 Array(String) COMMENT '列名，列类型',
        c57 Array(String) COMMENT '列名，列类型',
        c58 Array(String) COMMENT '列名，列类型',
        c59 Array(String) COMMENT '列名，列类型',
        c60 Array(String) COMMENT '列名，列类型'
    ) ENGINE = MergeTree() PARTITION  BY tblid ORDER BY tblid PRIMARY KEY tblid
"""

def create():
    __create(create_sql, TBL_NAME)


def drop():
    __drop(TBL_NAME)


def execute(sql, params=None):
    return __execute(sql, params)


def query(sql, params=None, result_style='dict'):
    return __query(sql, params, result_style=result_style)


class AdTblColumn:
    def __init__(self, title: str, style: str, width: int = 200):
        """
        @param title: 表格显示的表头
        @param style: 字段的类型：文本、数值、日期
        @param width: 显示时的列宽
        """
        self.title = title
        self.style = style
        self.width = str(width)

    def toch(self):
        # [标题, 类型, 宽度]
        return (self.title, self.style, self.width)

class VxeTableColumn:
    def __init__(self, field, title, style, width):
        """
        @param field
        @param title
        @param style
        @param width
        """
        self.field = field
        self.title = title
        self.style = style
        self.width = width
    def toVxe(self):
        return {'field': self.field, 'title': self.title, 'style': self.style, 'width': self.width + 'px', 'resizable': True, 'sortable': True}

class VxeColumnEdit:
    def __init__(self, field, title, style, width):
        """
        @param field
        @param title
        @param style
        @param width
        """
        self.field = field
        self.title = title
        self.style = style
        self.width = width
    def toVxe(self):
        return {'field': self.field, 'title': self.title, 'style': self.style, 'width': self.width}

def insert(tblid: str, userid: str, tbl_name: str, titles: List[AdTblColumn]):
    '''
    @param tbid 一定是自动生成的id
    @param userid 一定是用户的id
    @param tbl_name 表名
    @param titles 表头数据是一个list，里面是AdTblColumn
    '''
    colstr = ','.join(['c' + str(10 + i) for i in range(len(titles))])
    sql = """INSERT INTO {} ( tblid, userid, tblname, cols, {}) VALUES""".format(TBL_NAME, colstr)
    values = [tblid, userid, tbl_name, colstr]
    titles = [t.toch() for t in titles]  # 对titles进行结构转换
    values.extend(titles)  # 合并list
    values = [values]  # 必须放入到一个list中
    return __execute(sql, params=values)
