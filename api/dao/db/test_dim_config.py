import unittest
from api import config
from api.dao.db import dim_config
from api.model import DimConfig


class TestUtil(unittest.TestCase):
    def read_files(self, filename):
        with open(filename, encoding='utf8') as reader:
            lines = reader.readlines()
            return lines
        return []
    def test_dim_dict(self):
        try:
            dim_config.drop_dim_config()
            dim_config.create_dim_config()
            dim_config.truncate_dim_config()
            # 年份
            year = DimConfig()
            year.userid = 'default'
            year.style = 'year'
            year.values = [str(i) for i in range(1900, 2051)]
            dim_config.insert_dim_config([year.to_dict()])


        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_dim_config))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
