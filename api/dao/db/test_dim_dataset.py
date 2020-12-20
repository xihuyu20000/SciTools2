import unittest
from api import config
from api.dao.db import dim_dataset
from api.util import utils


class TestUtil(unittest.TestCase):
    def test_ddl(self):
        try:
            dim_dataset.drop()
            dim_dataset.create()
        except Exception as e:
            self.fail('修改表{}失败'.format(config.tbl_dim_dataset))


    def test_insert(self):
        try:
            dim_dataset.drop()
            dim_dataset.create()
            dim_dataset.insert([{'dsid':utils.gen_uuid1(), 'dsname': '数据集', 'status': '未解析'}])
            sql = 'select * from {}'.format(config.tbl_dim_dataset)
            file = dim_dataset.find_all_names(sql)
            self.assertIsNotNone(file, '应该存在一个文件')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_dim_dataset))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
