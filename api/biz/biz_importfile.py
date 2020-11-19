import os
import zipfile
import tempfile
from api import util, config, dao
from api.biz import helper_fileparser


def import_file(format, tempfile_path):
    """
    把临时文件解析，插入到数据库
    :param format: 数据源类型
    :param tempfile_path: 上传的临时文件
    :return:
    """

    def __parse(files):
        datas = []
        for file in files:
            result = []
            if format == config.ds_gbt_7714_2015:
                result = helper_fileparser.gbt_7714_2015(file)
            elif format == config.ds_cnki_es5:
                result = helper_fileparser.cnki_es5(file)
            elif format == config.ds_note_express:
                result = helper_fileparser.noteExpress(file)
            else:
                raise Exception('不识别的数据类型{}'.format(format))
            datas.extend(result)
        return datas

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
    fileid = util.gen_uuid()
    def set_const(v):
        v.fileid = fileid
        v.format = format
        return v
    datas = __parse(files)
    datas = map(set_const, datas)
    datas = [a.to_dict() for a in datas]

    # 3、写入到ods表
    return dao.saveOdsData(datas)

