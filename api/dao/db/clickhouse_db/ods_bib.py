from typing import Optional, List

from api import config
from api.dao.db.clickhouse_db import __create, __drop, __truncate, __execute, __query

TBL_NAME = config.tbl_ods_bib
def create_ods_bib():
    """
    创建ods_bib表
    """
    sql = """
        CREATE TABLE  {}(
        fileid String(64) NOT NULL,
        id String(64) NOT NULL,
        style String(16) NOT NULL,
        title String(512) NOT NULL,
        title_words Array(String),
        firstduty String(100),
        authors Array(String),
        orgs Array(String),
        kws Array(String),
        summary String(2048),
        summary_words Array(String),
        funds Array(String),
        pubyear Int16,
        pubtime String(16),
        clcs Array(String),
        clc1 String(128),
        clc2 String(128),
        format String(16),
        publication String(100),
        country String(100),
        lang String(16)
        )ENGINE=MergeTree() ORDER BY (pubyear) PARTITION BY (fileid);
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
    :return 返回两个值：fileid、插入条数
    """
    sql = """
        INSERT INTO {} (fileid, id, style, title, title_words, firstduty, authors, orgs, kws, summary, summary_words, funds, pubyear, pubtime, clcs, clc1, clc2, format, publication, country, lang) VALUES
    """.format(TBL_NAME)
    return params[0]['fileid'], __execute(sql, params=params, msg='插入{}失败'.format(TBL_NAME))

def update_ods_bib(id, params):
    sql = """
        ALTER TABLE {} UPDATE  
    """.format(TBL_NAME)

    for key, value in params.items():
        sql += ' {}={} ,'.format(key, value)
    sql = sql[:-1]

    sql += " WHERE id='{}'".format(id)

    return __execute(sql, msg='插入{}失败'.format(TBL_NAME))

def delete_ods_bib(file_id):
    sql = """
        DELETE FROM {} WHERE fileid={}
    """.format(TBL_NAME, file_id)
    return __execute(sql, msg='根据{}删除{}失败'.format(file_id, TBL_NAME))


def find_ods_bib(params: Optional[dict] = None):
    sql = """
        SELECT * FROM {} WHERE 1=1 
    """.format(TBL_NAME)
    if params:
        for key, value in params.items():
            sql += ' AND {}={}'.format(key, value)

    return __query(sql, params=params, msg='查询{}失败'.format(TBL_NAME))
