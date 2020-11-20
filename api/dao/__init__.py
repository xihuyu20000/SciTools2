'''
api/dao负责所有的数据库层访问
'''
from typing import List

from api import db
from api.model import ods


def saveOdsData(datas):
    """
    插入到ods_bib表
    :return 返回两个值：fileid、插入条数
    """
    return db.insert_ods_bib(datas)

def findOdsData(file_id) -> List[ods.OdsCnkiBib]:
    return db.find_ods_bib({'fileid':"'{}'".format(file_id)})

def updateOdsData(id, params):
    return db.update_ods_bib(id, params)

def saveDimDict(datas) -> int:
    return db.insert_dim_dict(datas)