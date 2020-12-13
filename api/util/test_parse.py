'''

'''
import os
import tempfile
import unittest
import shutil
from api import config
from api.util import utils
from api.util.utils import CutWords
from api.util import parser

class TestUtil(unittest.TestCase):

    def test(self):
        datas = parser.parsefiles(config.ds_gbt_7714_2015, utils.iter_file_names(r'E:\workspace\workspace-js\ai-edu\SciTools2\api\upload\2020-12-12\628f5ec29792422e8c6749ed85f9ca4e_dir'))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
