from api import dao
from api.web import biz_analyzefile_helper

"""
分析文件的时候，主要是构建各个知识单元，建立具体的表，或者字段；并生成对应的数据
"""
def analyzefile(fileid):
    # 1、查询出所有数据
    df = dao.findOdsData(fileid)
    # 2、对title和summary切词
    # biz_analyzefile_helper.cut_words(df)
    # 3、共词
    biz_analyzefile_helper.co_keywords(df)
