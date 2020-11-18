from api import config
from api.db.clickhouse_db import execute


def create_cnki_bib():
    sql = """
        CREATE TABLE  {}(
        fileid String(64) NOT NULL,
        title String(512) NOT NULL,
        firstduty String(100),
        authors Array(String),
        orgs Array(String),
        kws Array(String),
        summary String(2048),
        funds Array(String),
        pubyear Int8,
        pubmonth Int8,
        pubtime String(16),
        clcs Array(String),
        publication String(100)
        )ENGINE=MergeTree() ORDER BY (pubyear) PARTITION BY (fileid);
    """.format(config.tbl_ods_cnki_bib)
    return execute(sql, msg='创建表{}失败'.format(config.tbl_ods_cnki_bib))


def drop_cnki_bib():
    sql = """
        DROP TABLE IF EXISTS {};
    """.format(config.tbl_ods_cnki_bib)
    return execute(sql, msg='删除表{}失败'.format(config.tbl_ods_cnki_bib))


def truncate_cnki_bib():
    sql = """
        TRUNCATE TABLE IF EXISTS {};
    """.format(config.tbl_ods_cnki_bib)
    return execute(sql, msg='截断表{}失败'.format(config.tbl_ods_cnki_bib))
