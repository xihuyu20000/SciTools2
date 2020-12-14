import unittest
from api import config
from api.dao.db.clickhouse_db import dim_org


class TestUtil(unittest.TestCase):

    def test_dim_dict(self):
        try:
            dim_org.drop_dim_org()
            dim_org.create_dim_org()
            dim_org.truncate_dim_org()


        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_dim_org))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
