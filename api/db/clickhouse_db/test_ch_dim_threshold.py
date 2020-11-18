import unittest
from api import config, util
from api.db.clickhouse_db import ch_dim_threshold
from api.model import dim


class TestUtil(unittest.TestCase):

    def test_ddl(self):
        try:
            ch_dim_threshold.drop_dim_threshold()
            ch_dim_threshold.create_dim_threshold()
            ch_dim_threshold.truncate_dim_threshold()
        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_dim_dict))

    def test_insert(self):
        try:
            result1 = ch_dim_threshold.find_dim_threshold()

            entity1 = dim.DimThreshold()
            entity1.fileid = util.gen_uuid()
            entity1.name = 'a'
            entity1.value = 'a'

            entity2 = dim.DimThreshold()
            entity2.fileid = util.gen_uuid()
            entity2.name = 'b'
            entity2.value = 'b'


            ch_dim_threshold.insert_dim_threshold(
                [entity1.to_dict(), entity2.to_dict()])

            result2 = ch_dim_threshold.find_dim_threshold()

            self.assertEqual(len(result2) - len(result1), 2, '插入应该是2条记录')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_dim_threshold))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
