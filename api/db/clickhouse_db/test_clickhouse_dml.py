import unittest
from api import config
from api import util
from api.model import ods
from api.db.clickhouse_db import dml, dql


class TestUtil(unittest.TestCase):

    def test_dml(self):
        try:
            result1 = dql.find_ods_cnki_bib()

            entity1 = ods.OdsCnkiBib()
            entity1.fileid = util.gen_uuid()

            entity2 = ods.OdsCnkiBib()
            entity2.fileid = util.gen_uuid()

            dml.insert_ods_cnki_bib(
                [entity1.to_dict(), entity2.to_dict()])

            result2 = dql.find_ods_cnki_bib()

            self.assertEqual(len(result2)-len(result1), 2, '插入应该是2条记录')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_ods_cnki_bib))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
