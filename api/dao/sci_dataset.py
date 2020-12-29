from typing import Optional, List

from api import const
from api.dao.models import BaseDao
from api.util.utils import Logger


'''
题录数据，
指的是知网、维普等的题录信息。包括分词后的数据也作为字段保存。

[k for k,v in SciDataset().__dict__.items() if type(v) == list]
'''
class SciDataset(BaseDao):

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
        self.province = []       # 地区
        self.lang = '中文'        # 语种：中文/外文
        self.ref_style = 'citing'     # 引用类型，citing/cited
        self.refs = []          # 参考文献集合
        self.line = ''           # 原始记录

        self._log = Logger(__name__).get_log
        self.TBL_NAME = const.tbl_sci_dataset
        self._create_sql = """
            CREATE TABLE  {}(
            id String default toString(generateUUIDv4()) COMMENT '主键',
            dsid String NOT NULL,
            pid String NOT NULL,
            style String NOT NULL,
            title String NOT NULL,
            title_words Array(String),
            firstduty String,
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
            province Array(String),
            lang String(16),
            ref_style String(16),
            refs Array(String),
            line String
            )ENGINE=MergeTree() ORDER BY (dsid) PARTITION BY (dsid);
        """.format(self.TBL_NAME)

    def insert(self, params: Optional[List[dict]]):
        """
        插入到ods_bib表
        :return 返回两个值：dsid、插入条数
        """
        sql = """
            INSERT INTO {table} ({fields}) VALUES
        """.format(table=self.TBL_NAME, fields=SciDataset().keys())
        return self.execute(sql, params=params, msg='插入{}失败'.format(self.TBL_NAME))

    def keys(self):
        return ','.join([k for k,v in self.dict().items() ])



sci_dataset = SciDataset()