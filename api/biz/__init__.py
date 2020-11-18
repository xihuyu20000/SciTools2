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