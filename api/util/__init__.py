'''
api/util负责管理所有的工具类代码
'''
import uuid
import os
import shutil

def gen_uuid() -> str:
    '''
    生成uuid
    :return: uuid，共32位
    '''
    uid = str(uuid.uuid1())
    suid = ''.join(uid.split('-'))
    return suid

def move_file(srcFile, dstDir) -> str:
    """
    复制文件到目的地，删除源文件
    :param srcFile:
    :param dstDir:
    :return: 新文件路径
    """
    assert os.path.exists(srcFile), '输入文件{}必须存在'.format(srcFile)
    assert os.path.exists(dstDir), '目的地文件夹{}必须存在'.format(dstDir)
    fileName = os.path.split(srcFile)[1]
    dstFile = os.path.join(dstDir, fileName)
    # 复制文件
    shutil.copy(srcFile, dstFile)
    # 删除源文件
    os.remove(srcFile)

    return dstFile
