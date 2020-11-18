import unittest
from api import config
from api.db.clickhouse_db import ddl


class TestUtil(unittest.TestCase):

    def test_ddl(self):
        try:
            ddl.drop_cnki_bib()
            ddl.create_cnki_bib()
            ddl.truncate_cnki_bib()
        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_ods_cnki_bib))



if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
