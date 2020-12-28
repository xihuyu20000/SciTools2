import unittest

from api import const
from api.dao.sci_meta import sci_meta

from api.util import utils


class TestUtil(unittest.TestCase):
    def test_ddl(self):
        try:
            sci_meta.drop()
            sci_meta.create()
        except Exception as e:
            self.fail('修改表{}失败'.format(const.tbl_sci_meta))


    def test_insert(self):
        try:
            sci_meta.drop()
            sci_meta.create()
            sci_meta.insert([{'dsid':utils.gen_uuid4(), 'dsname': '数据集', 'status': '未解析'}])
            sql = 'select * from {}'.format(const.tbl_sci_meta)
            file = sci_meta.query(sql)
            self.assertIsNotNone(file, '应该存在一个文件')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(const.tbl_sci_meta))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
