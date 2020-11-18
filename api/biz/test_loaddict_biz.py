'''
api/test负责所有的测试实例
'''
import unittest
from api import util, db, config

from api.biz import loaddict_biz


class TestUtil(unittest.TestCase):

    def test_load_dict_stop_words(self):
        db.drop_dim_dict()
        db.create_dim_dict()
        count = loaddict_biz.load_dict(util.gen_uuid(), config.dict_stop, 'dataset/loaddict_biz/dict_stop_words.txt')
        self.assertEqual(count, 3, '插入3条记录')

    def test_load_dict_synonym(self):
        db.drop_dim_dict()
        db.create_dim_dict()
        count = loaddict_biz.load_dict(util.gen_uuid(), config.dict_stop, 'dataset/loaddict_biz/dict_synonym.txt')
        self.assertEqual(count, 2, '插入2条记录')

    def test_load_dict_country(self):
        db.drop_dim_dict()
        db.create_dim_dict()
        count = loaddict_biz.load_dict(util.gen_uuid(), config.dict_stop, 'dataset/loaddict_biz/dict_contry.txt')
        self.assertEqual(count, 1, '插入1条记录')

    def test_load_dict_province(self):
        db.drop_dim_dict()
        db.create_dim_dict()
        count = loaddict_biz.load_dict(util.gen_uuid(), config.dict_stop, 'dataset/loaddict_biz/dict_province.txt')
        self.assertEqual(count, 1, '插入1条记录')

    def test_load_dict_org(self):
        db.drop_dim_dict()
        db.create_dim_dict()
        count = loaddict_biz.load_dict(util.gen_uuid(), config.dict_stop, 'dataset/loaddict_biz/dict_org.txt')
        self.assertEqual(count, 1, '插入1条记录')


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
