'''
api/action负责所有的控制逻辑
'''

import os
from typing import List
from api import config
from api import util
from api import biz

def importFile(data_source, tempfile_path) ->None:
    """
    上传数据文件并解析
    :param data_source: 数据源类型
    :param tempfile_path: 上传的数据文件
    :return:
    """
    biz.importFileBiz(data_source, tempfile_path)

def cleanFile(file_id, clean_style, params) -> List[dict]:
    """
    清洗文件中的数据
    :param file_id: 文件ID
    """
    biz.cleanFileBiz(file_id, clean_style, params)
    return biz.findGlobalDataBiz(file_id)

def loadDict(dict_style, file_path):
    """
    加载数据字典，用于清洗数据和分析数据
    """
    pass

def loadThreshold(dict):
    """
    加载各个阈值
    """
    pass

def analyzeFile(file_id):
    """
    分析清洗后的数据
    :param file_id: 文件ID
    """
    biz.analyzeFileBiz(file_id)