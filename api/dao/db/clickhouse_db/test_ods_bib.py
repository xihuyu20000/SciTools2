import unittest
from api import config, util
from api.dao.db.clickhouse_db import ods_bib
from api.model import ods


class TestUtil(unittest.TestCase):

    def test_ods_bib(self):
        try:
            ods_bib.drop_ods_bib()
            ods_bib.create_ods_bib()
            ods_bib.truncate_ods_bib()
        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_ods_bib))

    def test_insert(self):
        try:
            result1 = ods_bib.find_ods_bib()

            entity1 = ods.OdsCnkiBib()
            entity1.fileid = util.gen_uuid1()

            entity2 = ods.OdsCnkiBib()
            entity2.fileid = util.gen_uuid1()

            ods_bib.insert_ods_bib([entity1.to_dict(), entity2.to_dict()])

            result2 = ods_bib.find_ods_bib()
            self.assertEqual(len(result2) - len(result1), 2, '插入应该是2条记录')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_ods_bib))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
