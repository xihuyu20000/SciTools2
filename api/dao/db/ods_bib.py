from typing import Optional, List

from api import config
from api.dao.db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_ods_bib

'''
题录数据，
指的是知网、维普等的题录信息。包括分词后的数据也作为字段保存。

[k for k,v in OdsCnkiBib().__dict__.items() if type(v) == list]
'''
class OdsCnkiBib:
    def __init__(self):
        self.dsid = ''
        self.id = ''
        self.pid = ''           # 参考文献指向施引文献
        self.style = ''       # 如期刊、回忆录、图书
        self.title = ''          # 标题
        self.title_words = []    # 标题分词
        self.firstduty = ''      # 一作
        self.authors = []        # 作者
        self.orgs = []           # 机构
        self.orgs2 = []          # 机构名称规范化
        self.kws = []            # 关键词
        self.summary = ''        # 摘要
        self.summary_words = []  # 摘要分词
        self.funds = []          # 基金
        self.funds2 = []         # 基金名称规范化
        self.funds_style = []    # 基金类型
        self.subject1 = ''       # 一级学科分类
        self.subject2 = ''       # 二级学科分类
        self.pubyear = ''        # 出版年
        self.clcs = []           # 主题分类
        self.publication = ''    # 出版物
        self.country = ['中国']   # 国家
        self.province = ''       # 地区，只取第一个机构所在的地区
        self.lang = '中文'        # 语种：中文/外文
        self.ref_style = 'citing'     # 引用类型，citing/cited
        self.refs = []          # 参考文献集合
        self.line = ''           # 原始记录

    def __repr__(self):
        return str(self.to_dict())

    def keys(self):
        return ','.join([k for k,v in vars(self).items()])


def create_ods_bib():
    """
    创建ods_bib表
    """
    sql = """
        CREATE TABLE  {}(
        dsid String(64) NOT NULL,
        id String(64) NOT NULL,
        pid String(64) NOT NULL,
        style String(16) NOT NULL,
        title String(512) NOT NULL,
        title_words Array(String),
        firstduty String(100),
        authors Array(String),
        orgs Array(String),
        orgs2 Array(String),
        kws Array(String),
        summary String(2048),
        summary_words Array(String),
        funds Array(String),
        funds2 Array(String),
        funds_style Array(String),
        subject1 Array(String),
        subject2 Array(String),
        pubyear String(8),
        clcs Array(String),
        publication String(100),
        country Array(String),
        province String(100),
        lang String(16),
        ref_style String(16),
        refs Array(String),
        line String
        )ENGINE=MergeTree() ORDER BY (dsid) PARTITION BY (dsid);
    """.format(TBL_NAME)
    return __create(sql, TBL_NAME)


def drop_ods_bib():
    """
    删除ods_bib表
    """
    return __drop(TBL_NAME)


def truncate_ods_bib():
    """
    截断ods_bib表
    """
    return __truncate(TBL_NAME)


def insert_ods_bib(params: Optional[List[dict]]):
    """
    插入到ods_bib表
    :return 返回两个值：dsid、插入条数
    """
    sql = """
        INSERT INTO {} ({}) VALUES
    """.format(TBL_NAME, OdsCnkiBib().keys())
    return __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))


def update_ods_bib(sql):
    return __execute(sql, msg='更新{}失败'.format(TBL_NAME))


def delete_ods_bib(sql):
    return __execute(sql, msg='删除{}失败'.format(TBL_NAME))


def find_ods_bib(sql):
    return __query(sql, params=None, msg='查询{}失败'.format(TBL_NAME))


