from typing import Optional, List

from api import config
from api.db.clickhouse_db import __create, __drop, __truncate, __execute


def create_ods_bib():
    """
    创建ods_bib表
    """
    sql = """
        CREATE TABLE  {}(
        fileid String(64) NOT NULL,
        style String(16) NOT NULL,
        title String(512) NOT NULL,
        firstduty String(100),
        authors Array(String),
        orgs Array(String),
        kws Array(String),
        summary String(2048),
        funds Array(String),
        pubyear Int16,
        pubtime String(16),
        clcs Array(String),
        format String(16),
        publication String(100)
        )ENGINE=MergeTree() ORDER BY (pubyear) PARTITION BY (fileid);
    """.format(config.tbl_ods_bib)
    return __create(sql, config.tbl_ods_bib)


def drop_ods_bib():
    """
    删除ods_bib表
    """
    return __drop(config.tbl_ods_bib)


def truncate_ods_bib():
    """
    截断ods_bib表
    """
    return __truncate(config.tbl_ods_bib)


def insert_ods_bib(params: Optional[List[dict]]):
    sql = """
        INSERT INTO {} (fileid, style, title, firstduty, authors, orgs, kws, summary, funds, pubyear, pubtime, clcs, format, publication) VALUES
    """.format(config.tbl_ods_bib)
    return __execute(sql, params=params, msg='插入{}失败'.format(config.tbl_ods_bib))

def delete_ods_bib(file_id):
    sql = """
        DELETE FROM {} WHERE fileid={}
    """.format(config.tbl_ods_bib, file_id)
    return __execute(sql, msg='根据{}删除{}失败'.format(file_id, config.tbl_ods_bib))


def find_ods_bib(params: Optional[dict] = None):
    sql = """
        SELECT * FROM {} WHERE 1=1 
    """.format(config.tbl_ods_bib)
    return __execute(sql, params=params, msg='查询{}失败'.format(config.tbl_ods_bib))
