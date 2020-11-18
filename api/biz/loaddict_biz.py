from api.model import dim
from api.util import dictparser
from api import dao, config


def load_dict(file_id, style, file_path):
    # 1、解析字典
    datas = dictparser.parse_dict(file_id, style, file_path)
    # 2、保存到dim_dict中
    datas = [a.to_dict() for a in datas]

    return dao.saveDimDict(datas)
