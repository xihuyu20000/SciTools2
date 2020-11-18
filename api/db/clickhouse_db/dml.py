from typing import Optional,List
from api import config
from api.db.clickhouse_db import execute


def insert_ods_cnki_bib(params: Optional[List[dict]]):
    sql = """
        INSERT INTO {} (fileid, title, firstduty, authors, orgs, kws, summary, funds, pubyear, pubmonth, pubtime, clcs, publication) VALUES
    """.format(config.tbl_ods_cnki_bib)
    return execute(sql, params=params, msg='插入{}失败'.format(config.tbl_ods_cnki_bib))
