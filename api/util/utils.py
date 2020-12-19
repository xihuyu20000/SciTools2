import hashlib
import logging
import os

import shutil
import uuid

from pdfminer.high_level import extract_text

'''
api/util负责管理所有的工具类代码
'''
import uuid
import os
import shutil


def read_lines(filepath):
    '''
    读取文件内容，已经去除空行
    '''
    with open(filepath, encoding='utf8') as reader:
        lines = reader.readlines()
        return [line.strip() for line in lines if line.strip()]
    return []



def iter_file_names(dir_path: str):
    '''
    迭代文件夹中的所有文件，多层目录也可以
    '''
    result = []

    def __iter(dir_path):
        if os.path.isdir(dir_path):
            files = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
            result.extend([file for file in files if os.path.isfile(file)])
            for dir in [file for file in files if os.path.isdir(file)]:
                __iter(dir)

    __iter(dir_path)
    return result


def remove_dir(dir):
    # 删除非空目录
    if not os.path.exists(dir):
        return
    dir = dir.replace('\\', '/')
    if (os.path.isdir(dir)):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir, p))
        if (os.path.exists(dir)):
            os.rmdir(dir)
    else:
        if (os.path.exists(dir)):
            os.remove(dir)


def pdf2text(pdffilepath):
    '''
    pdf转text
    :param pdffilepath: pdf文件路径
    :return: 内容
    '''
    text = extract_text(pdf_file=pdffilepath)
    txtfilepath = str(pdffilepath).replace('.pdf', '.txt')
    with open(txtfilepath, 'w', encoding='utf-8') as f:
        f.write(text)

    print(text)


def getFileMd5(filename):
    # 生成文件的MD5
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
    return myhash.hexdigest()


def gen_uuid1() -> str:
    '''
    生成uuid
    :return: uuid，共32位
    '''
    uid = str(uuid.uuid1())
    suid = ''.join(uid.split('-'))
    return suid


def gen_uuid4() -> str:
    '''
    生成uuid
    :return: uuid，共32位
    '''
    uid = str(uuid.uuid4())
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


def buildsql(tname, dt):
    # 构造INSERT语句
    ls = [(k, dt[k]) for k in dt if dt[k] is not None]
    sql1 = 'INSERT %s (' % tname
    sql2 = ','.join(i[0] for i in ls)
    sql3 = ') VALUES ('
    sql4 = ','.join('%r' % i[1] for i in ls)
    sql5 = ');'
    sql6 = ''.join([sql1, sql2, sql3, sql4, sql5])
    return sql6


def is_all_chinese(strs):
    # 判断是否是纯中文
    for i in strs:
        if not '\u4e00' <= i <= '\u9fa5':
            return False
    return True


# 判断是否是纯英文
def is_all_eng(strs):
    import string
    for i in strs:
        if i not in string.ascii_lowercase + string.ascii_uppercase:
            return False
    return True


# 判断字符串是英文还是中文
def strings_is_eng(strings):
    words = [word for word in strings if
             word != '[' and word != ']' and word != '.' and word != ',' and word != '(' and word != ')' and word.strip()]
    words_cn = len([word for word in words if is_all_chinese(word)])
    words_en = len([word for word in words if is_all_eng(word)])
    return True if words_cn < words_en else False


class Logger:
    def __init__(self, name=__name__):
        # 创建一个loggger
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.path.abspath(__file__))
        logname = log_path + '/' + 'out.txt'  # 指定输出的日志文件名
        # fh = logging.handlers.TimedRotatingFileHandler(logname, when='M', interval=1, backupCount=5,encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        fh = logging.FileHandler(logname, mode='w', encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger
