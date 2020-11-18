'''
api/biz负责所有的业务逻辑
'''
import os
import zipfile
from typing import List
from api import dao, util, config
from api.util import fileparser
from api.util import fileanalyzer
from api import model


def importFileBiz(data_source, tempfile_path):
    """
    把临时文件导入到指定文件夹中，并解压缩
    :param data_source: 数据源类型
    :param tempfile_path: 上传的临时文件
    :return:
    """
    # 1、创建存放数据的文件夹，前缀是file_
    dir_name = 'file_' + util.gen_uuid()
    dst_dir = os.path.join(config.base_file_dir, dir_name)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    # 2、从临时文件夹中，移动文件到新的文件夹
    dstFile = util.move_file(tempfile_path, dst_dir)

    # 3、如果文件是压缩格式，解压缩到文件夹中，删除压缩文件
    if 'zip' == str(tempfile_path).lower().endswith(".zip"):
        zip_file = zipfile.ZipFile(dstFile)
        zip_list = zip_file.namelist()
        for f in zip_list:
            zip_file.extract(f, dst_dir)  # 循环解压文件到指定目录
        zip_file.close()
        os.remove(dstFile)

    # todo 4、保存文件信息
    fileModel: model.FileModel = dao.saveFileDao(data_source, doc_dir=dst_dir)

    # 5、根据格式解析数据
    datas = []
    for file in dst_dir:
        dst_file = os.path.join(dst_dir, file)
        result = []
        if data_source == config.ds_gbt_7714_2015:
            result = fileparser.gbt_7714_2015(dst_file)
        elif data_source == config.ds_cnki_es5:
            result = fileparser.cnki_es5(dst_file)
        elif data_source == config.ds_note_express:
            result = fileparser.noteExpress(dst_file)
        else:
            raise Exception('不识别的数据类型{}'.format(data_source))
        datas.extend(result)

    # todo 6、保存解析后的数据
    dao.saveRawData(fileModel.id, datas)

    # todo 7、保存数据到全局表
    dao.saveGlobalData(fileModel.id)

    # # 8、在文件夹中，创建工作空间文件夹，名称是workspace
    # ws_dir = os.path.join(dst_dir, 'workspace')
    # os.mkdir(ws_dir)

def cleanFileBiz(file_id, clean_style, params):
    """
    清洗数据
    :param file_id: 文件id
    :param clean_style: 清洗类型
    :param params: 清洗时需要的参数
    :return:
    """
    # todo 还没有想清楚有哪些清洗方式
    pass

def findGlobalDataBiz(file_id) -> List[dict]:
    """
    根据file_id查询数据
    :param file_id: 文件id
    """
    # todo
    pass

def analyzeFileBiz(file_id):
    """
    根据file_id构建知识体系
    :param file_id: 文件id
    """
    # todo
    fileanalyzer.checkDataIntegrity(file_id)
    fileanalyzer.buildKnowledgeUnit(file_id)