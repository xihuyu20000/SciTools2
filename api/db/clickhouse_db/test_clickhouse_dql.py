import unittest
from api import config
from api import util
from api.model import ods
from api.db.clickhouse_db import dml, dql


class TestUtil(unittest.TestCase):

    def test_dml(self):
        try:
            dql.find_ods_cnki_bib()
        except Exception as e:
            self.fail('查询表{}失败'.format(config.tbl_ods_cnki_bib))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
