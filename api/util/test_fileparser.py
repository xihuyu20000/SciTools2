'''
api/test负责所有的测试实例
'''
import os
import tempfile
import unittest
import shutil
from api import util
from api.util import fileparser

class TestUtil(unittest.TestCase):

    def test_cnki_es5(self):
        result = fileparser.cnki_es5('../test/dataset/CNKI-02.es5')
        self.assertTrue(len(result)>0, '提取es5格式数据失败')

    def test_gbt_7714_2015(self):
        result = fileparser.gbt_7714_2015('../test/dataset/CNKI-03.txt')
        self.assertTrue(len(result) > 0, '提取gbt_7714_2015格式数据失败')

    def test_noteExpress(self):
        result = fileparser.noteExpress('../test/dataset/CNKI-04.net')
        self.assertTrue(len(result) > 0, '提取NoteExpress格式数据失败')

    @unittest.skip
    def test_cnki_html(self):
        result = fileparser.cnki_html('../test/dataset/1.html')
        self.assertTrue(len(result) > 0, '提取cnki的html格式数据失败')


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
