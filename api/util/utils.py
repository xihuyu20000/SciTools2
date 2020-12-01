from pdfminer.high_level import extract_text
import hashlib
import logging
import os

# 删除非空目录
def remove_dir(dir):
    if not os.path.exists(dir):
        return
    dir = dir.replace('\\', '/')
    if(os.path.isdir(dir)):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir,p))
        if(os.path.exists(dir)):
            os.rmdir(dir)
    else:
        if(os.path.exists(dir)):
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

# def getFileMd5(filename):
#     # 生成文件的MD5
#     if not os.path.isfile(filename):
#         return
#     myhash = hashlib.md5()
#     with open(filename, 'rb') as f:
#         while True:
#             b = f.read(8096)
#             if not b:
#                 break
#             myhash.update(b)
#     return myhash.hexdigest()


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



class Logger:
    def __init__(self, name=__name__):
        # 创建一个loggger
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.path.abspath(__file__))
        logname = log_path + '/' + 'out.log'  # 指定输出的日志文件名
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
