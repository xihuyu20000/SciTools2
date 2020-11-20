from api.biz import biz_loaddict_helper
from api import dao


def load_dict(file_id, style, file_path):
    # 1、解析字典
    datas = biz_loaddict_helper.parse_dict(file_id, style, file_path)
    # 2、调用to_dict() 转换形式
    datas = [a.to_dict() for a in datas]
    # 3、保存到dim_dict中
    count = dao.saveDimDict(datas)
    return count
