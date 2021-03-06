import unittest

from api import dao
from api.web import biz_cleaningfiles, biz_analyzefile, config


class TestUtil(unittest.TestCase):

    def test_analyzefile(self):
        try:
            dao.drop_sci_dataset()
            dao.create_sci_dataset()
            fileid, count = biz_cleaningfiles.import_file(config.ds_cnki_es5, 'dataset/importfile_biz/CNKI-02.es5')

            biz_analyzefile.analyzefile(fileid)
        except Exception as e:
            print(e)
            self.fail('对title和summary切词出错')


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
