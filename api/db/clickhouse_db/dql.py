from typing import Optional
from api import config
from api.db.clickhouse_db import execute


def find_ods_cnki_bib(params: Optional[dict] = None):
    sql = """
        SELECT * FROM {} WHERE 1=1 
    """.format(config.tbl_ods_cnki_bib)
    return execute(sql, params=params, msg='查询{}失败'.format(config.tbl_ods_cnki_bib))
