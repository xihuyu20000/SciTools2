from typing import List
from api import config
from api.model import dim


def parse_dict(file_id, style, file_path) -> List[dim.DimDict]:
    """
    键值之间用空格分割，键之间用|分割。alias在前，values在后
    """
    assert style in [config.dict_stop, config.dict_synonym, config.dict_country, config.dict_province,
                     config.dict_org], '不识别的字典类型{}'.format(style)
    assert str(file_path).endswith('.txt'), '文件必须是.txt格式'

    # 1、读取内容
    reader = open(file_path, encoding='utf8')
    lines = [line.strip() for line in reader.readlines() if line.strip()]
    reader.close()

    # 2、格式转换
    def __parse(line):
        dimd = dim.DimDict()
        dimd.fileid = file_id
        dimd.style = style

        arr = line.split(maxsplit=1)  # 只分割一次
        if len(arr) == 1:
            dimd.values = arr[0].split('|')
            dimd.alias = ''
        if len(arr) == 2:
            dimd.values = arr[1].split('|')
            dimd.alias = arr[0]
        return dimd

    datas = map(__parse, lines)

    return datas
