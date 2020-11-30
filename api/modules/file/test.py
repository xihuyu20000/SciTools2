import unittest

from .manager import FileManager
from .util import *

class FileTest(unittest.TestCase):

    # 如果跑所有用例，只运行一次前提条件和结束条件。则用setupclass()和teardownclass()
    def setUp(self):
        self.biz = FileManager()


    @unittest.skip
    def test_dbscan(self):
        with open(r'E:\workspace\workspace-java\scitools\apiserver\wos数字人文-纯文本.txt', encoding='utf-8') as file:
            all = file.readlines()
            if '﻿FN Clarivate Analytics Web of Science'!=all[0].strip():
                print('格式不对')
            rows = []
            row = []
            for i,line in enumerate(all):
                if line.startswith("PT "):
                    rows.append(row)
                    row = []
                if line.startswith('   '):
                    row.append(row.pop()+line)
                else:
                    row.append(line)
            #把最后一个元素加入
            rows.append(row)
            #第一个是版本信息，删除
            rows = rows[1:]

            arts = []
            art = {}
            for row in rows[:1]:
                for field in row:
                    if field.startswith('PT '):
                        art['PT'] = field[3:].strip()
                    elif field.startswith('AU '):
                        art['AU'] = field[3:].strip().replace('\n   ',' ')
                    elif field.startswith('TI '):
                        art['TI'] = field[3:].strip()
                    elif field.startswith('SO '):
                        art['SO'] = field[3:].strip()
                    elif field.startswith('VL '):
                        art['VL'] = field[3:].strip()
                    elif field.startswith('IS '):
                        art['IIS'] = field[3:].strip()
                    elif field.startswith('BP '):
                        art['BP'] = field[3:].strip()
                    elif field.startswith('EP '):
                        art['EP'] = field[3:].strip()
                    elif field.startswith('DI '):
                        art['DI'] = field[3:].strip()
                    elif field.startswith('PD '):
                        art['PD'] = field[3:].strip()
                    elif field.startswith('PY '):
                        art['PY'] = field[3:].strip()
                    elif field.startswith('AB '):
                        art['AB'] = field[3:].strip().replace('\n  ', '')
                    elif field.startswith('RI '):
                        art['RI'] = field[3:].strip()
                    elif field.startswith('OI '):
                        art['OI'] = field[3:].strip()
                    elif field.startswith('ZB '):
                        art['ZB'] = field[3:].strip()
                    elif field.startswith('Z8 '):
                        art['Z8'] = field[3:].strip()
                    elif field.startswith('ZR '):
                        art['ZR'] = field[3:].strip()
                    elif field.startswith('TC '):
                        art['TC'] = field[3:].strip()
                    elif field.startswith('ZS '):
                        art['ZS'] = field[3:].strip()
                    elif field.startswith('Z9 '):
                        art['Z9'] = field[3:].strip()
                    elif field.startswith('U1 '):
                        art['U1'] = field[3:].strip()
                    elif field.startswith('U2 '):
                        art['U2'] = field[3:].strip()
                    elif field.startswith('SN '):
                        art['SN'] = field[3:].strip()
                    elif field.startswith('UT '):
                        art['UT'] = field[3:].strip()
                    elif field.startswith('ER '):
                        art['ER'] = field[3:].strip()
                print('未解析', row)
                print('解析后', art)
                print(self.buildSQL(art))

    @unittest.skip
    def test_parse_cnki(self):
        parseCnki('admin', '文献检索_自定义.txt', r'C:\Users\Administrator\Desktop\数字人文\20200614\文献检索_自定义.txt')

    @unittest.skip
    def test_parse_cnki_cite(self):
        parseCnkiCite('admin', '引文检索_自定义.txt', r'C:\Users\Administrator\Desktop\数字人文\20200614\引文检索_自定义.txt')

    @unittest.skip
    def test_parse_wos(self):
        self.biz.parseDatafile()

    @unittest.skip
    def test_parse_cssci(self):
        ret = parseCssci(userId = 'admin', fileId = '243916112100712448', filepath=r'E:\workspace\workspace-java\scitools\src\main\webapp\WEB-INF/datafile/upload/20060912/20060912002100001.txt')
        print(ret)

if __name__ == '__main__':
    unittest.main()
