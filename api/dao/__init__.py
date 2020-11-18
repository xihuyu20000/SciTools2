'''
api/dao负责所有的数据库层访问
'''
from typing import List

from api import db
from api.model import ods


def saveOdsData(datas) -> int:
    return db.insert_ods_bib(datas)

def findOdsData(file_id) -> List[ods.OdsCnkiBib]:
    return db.find_ods_bib({'fileid':file_id})

def saveDimDict(datas) -> int:
    return db.insert_dim_dict(datas)