import unittest
from api import config, util
from api.dao.db.clickhouse_db import dim_file


class TestUtil(unittest.TestCase):

    def test_insert(self):
        try:
            dim_file.drop_dim_file()
            dim_file.create_dim_file()
            dim_file.truncate_dim_file()
            dim_file.insert_dim_file([{'fileid':util.gen_uuid1(),'filename':'数据集'}])
            file = dim_file.find_all_files()
            self.assertIsNotNone(file, '应该存在一个文件')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_dim_file))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
