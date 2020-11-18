'''
api/dao负责所有的数据库层访问
'''

from api import db



def saveOdsData(datas) -> None:
    return db.insert_ods_bib(datas)


def saveDimDict(datas) -> None:
    return db.insert_dim_dict(datas)