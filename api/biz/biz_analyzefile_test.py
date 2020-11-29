import unittest

from api import db, config, dao
from api.biz import biz_analyzefile, biz_cleaningfiles


class TestUtil(unittest.TestCase):

    def test_analyzefile(self):
        try:
            db.drop_ods_bib()
            db.create_ods_bib()
            fileid, count = biz_cleaningfiles.import_file(config.ds_cnki_es5, 'dataset/importfile_biz/CNKI-02.es5')

            biz_analyzefile.analyzefile(fileid)
        except Exception as e:
            print(e)
            self.fail('对title和summary切词出错')


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
