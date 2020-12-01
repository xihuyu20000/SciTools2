import unittest
from api import config, util
from api.dao.db.clickhouse_db import dim_user


class TestUtil(unittest.TestCase):

    def test_insert(self):
        try:
            dim_user.drop_dim_user()
            dim_user.create_dim_user()
            dim_user.truncate_dim_user()
            dim_user.insert_dim_user([{'id':util.gen_uuid1(),'username':'root', 'password':'admin'}])
            user = dim_user.get_user('root', 'admin')
            self.assertIsNotNone(user, '应该存在一个用户')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(config.tbl_ods_bib))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
