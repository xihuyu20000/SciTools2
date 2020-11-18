'''
api/test负责所有的测试实例
'''
import unittest
from api.biz import importfile_biz
from api import util, db, config


class TestUtil(unittest.TestCase):

    def test_import_file_zip(self):
        """
        测试zip压缩格式
        """
        db.drop_ods_bib()
        db.create_ods_bib()
        count = importfile_biz.import_file(config.ds_gbt_7714_2015, 'dataset/importfile_biz/ds_gbt_7714_2015.zip')
        self.assertEqual(count, 483, '插入483条记录')

    def test_import_file_es5(self):
        """
        测试es5格式
        """
        db.drop_ods_bib()
        db.create_ods_bib()
        count = importfile_biz.import_file(config.ds_cnki_es5, 'dataset/importfile_biz/CNKI-02.es5')
        self.assertEqual(count, 450, '插入450条记录')

    def test_import_file_gbt_7714_2015(self):
        """
        测试gbt_7714_2015格式
        """
        db.drop_ods_bib()
        db.create_ods_bib()
        count = importfile_biz.import_file(config.ds_gbt_7714_2015, 'dataset/importfile_biz/ds_gbt_7714_2015.txt')
        self.assertEqual(count, 161, '插入161条记录')

    def test_import_file_note_express(self):
        """
        测试NoteExpress格式
        """
        db.drop_ods_bib()
        db.create_ods_bib()
        count = importfile_biz.import_file(config.ds_note_express, 'dataset/importfile_biz/NoteExpress.net')
        self.assertEqual(count, 20, '插入20条记录')


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
