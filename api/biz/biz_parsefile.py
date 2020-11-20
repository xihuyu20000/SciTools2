import os
import zipfile
import tempfile
from api import util, dao
from api.biz import biz_parserfile_helper

"""
导入文件并解析
"""

def import_file(format, tempfile_path):
    """
    把临时文件解析，插入到数据库
    :param format: 数据源类型
    :param tempfile_path: 上传的临时文件
    :return: 两个变量，分别是：fileid、插入数量
    """
    assert os.path.exists(tempfile_path), '{}文件必须存在'.format(tempfile_path)
    # 1、如果是压缩文件，解压缩到临时文件夹
    files = []
    if str(tempfile_path).lower().endswith(".zip"):
        zip_file = zipfile.ZipFile(tempfile_path)
        zip_list = zip_file.namelist()
        dst_dir = tempfile.mkdtemp()
        for f in zip_list:
            zip_file.extract(f, dst_dir)  # 循环解压文件到指定目录
            files.append(os.path.join(dst_dir, f))
        zip_file.close()
    else:
        files.append(tempfile_path)

    # 2、循环解析
    fileid = util.gen_uuid1()

    def set_const(v):
        v.fileid = fileid
        v.format = format
        return v

    datas = biz_parserfile_helper.parsefiles(format, files)
    datas = map(set_const, datas)
    datas = [a.to_dict() for a in datas]

    # 3、写入到ods表
    return dao.saveOdsData(datas)
