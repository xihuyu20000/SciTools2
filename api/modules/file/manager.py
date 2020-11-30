import time

from api.common.utils import Logger
from .util import parseWos, parseCnki, parseCnkiCite, parseCssci, updateDatafileStatus, writeExcel
from api.common.dbhelper import db


class FileManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.db = db

    # 某一个
    def get(self, fileId):
        sql = 'SELECT * FROM sci_datafile WHERE id='+fileId
        all = self.db.fetch_all(sql=sql)
        if all:
            return all[0]
        return {}

    # 删除
    def remove(self, fileId):
        sql = 'DELETE FROM sci_datafile WHERE id='+fileId
        self.db.update(sql)

    # 所有文件
    def list(self):
        return self.db.fetch_all('SELECT * FROM sci_datafile')

    # 保存文件
    def saveUpload(self, source, file_name, file_size, raw_name, save_path):
        sql = 'INSERT INTO sci_datafile(file_name, file_size, save_path, source, raw_name, STATUS, create_date) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        self.db.insert_one(sql, (file_name, file_size, save_path, source, raw_name, '未解析', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))

    # 解析上传文件
    def parseDatafile(self, fileId):
        sql = 'select * from sci_datafile where id={}'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        print(all)
        if len(all) == 0:
            return '数据文件{}不存在'.format(fileId)

        # 更新状态
        updateDatafileStatus('解析中...', fileId)

        datafile = all[0]
        source = datafile['source']
        savePath = datafile['save_path']
        if str(source).startswith('wos'):
            parseWos(fileId, savePath)
        elif str(source).startswith('cnkicite'):
            parseCnkiCite(fileId, savePath)
        elif str(source).startswith('cnki'):
            parseCnki(fileId, savePath)
        elif str(source).startswith('cssci'):
            parseCssci(fileId, savePath)
        else:
            return '数据格式{}不识别'.format(source)


    # 生成wos的excel文件
    def generateWosExcel(self, fileId):
        sql = 'select * from sci_datafile where id={}'.format(fileId)
        datafile = self.db.fetch_all(sql)[0]
        file_path = datafile['save_path']
        file_name = datafile['file_name']
        excelpath = str(file_path).replace('.txt', '.xlsx')
        writeExcel(fileId, excelpath)
        print(excelpath)
        return excelpath


fileManager = FileManager()