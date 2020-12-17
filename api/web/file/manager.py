import time

from api.util import utils, parser
from api import dao, config
from api.util.utils import Logger


class FileManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao


    def saveUpload(self, file_name, file_style, save_path_dir):
        files = utils.iter_file_names(save_path_dir)
        datas = parser.parsefiles(file_style, files)
        dsid = utils.gen_uuid4()
        for entity in datas:
            entity.dsid = dsid
        datas = [data.__dict__ for data in datas]
        dao.insert_ods_bib(datas)
        dao.insert_dim_dataset([{'dsid':dsid, 'dsname':file_name, 'status':'未解析'}])


fileManager = FileManager()