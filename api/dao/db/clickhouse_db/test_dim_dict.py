import unittest
from api import config
from api.dao.db.clickhouse_db import dim_dict
from api.model.dim import DimDict


class TestUtil(unittest.TestCase):

    def test_dim_dict(self):
        try:
            dim_dict.drop_dim_dict()
            dim_dict.create_dim_dict()
            dim_dict.truncate_dim_dict()

            year = DimDict()
            year.fileid = 'default'
            year.style = 'year'
            year.values = [str(i) for i in range(1900, 2051)]
            dim_dict.insert_dim_dict([year.to_dict()])
        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_dim_dict))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
