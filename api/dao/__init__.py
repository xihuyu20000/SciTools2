'''
api/dao负责所有的数据库层访问
'''
from api.model import FileModel
from api import db



def saveRawData(file_id, datas) -> None:
    sql = ''
    params = {}
    db.insertBatch()

def saveGlobalData(file_id) -> None:
    sql = ''
    params = {}
    db.insertBatch()