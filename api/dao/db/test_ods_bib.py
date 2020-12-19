import unittest
from api import config
from api.dao.db import ods_bib
from api.dao.db.ods_bib import OdsCnkiBib
from api.util import utils


class TestUtil(unittest.TestCase):
    def test_ods_bib(self):
        ods_bib.drop_ods_bib()
        ods_bib.create_ods_bib()
        ods_bib.truncate_ods_bib()

    def test_ods_bib2(self):
        try:
            ods_bib.drop_ods_bib()
            ods_bib.create_ods_bib()
            ods_bib.truncate_ods_bib()


            sql = 'select * from {}'.format(config.tbl_ods_bib)
            result1 = ods_bib.find_ods_bib(sql)

            entity1 = OdsCnkiBib()
            entity1.fileid = utils.gen_uuid1()

            entity2 = OdsCnkiBib()
            entity2.fileid = utils.gen_uuid1()

            ods_bib.insert_ods_bib([entity1.__dict__, entity2.__dict__])

            result2 = ods_bib.find_ods_bib(sql)
            self.assertEqual(len(result2) - len(result1), 2, '插入应该是2条记录')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_ods_bib))

    def test_query(self):
        result = ods_bib.find_ods_bib()
        print(result)


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
