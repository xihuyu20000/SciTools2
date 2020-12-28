import unittest

from api import const

from api.dao.sci_dataset import SciDataset, sci_dataset
from api.util import utils


class TestUtil(unittest.TestCase):
    def test_001(self):
        sci_dataset.drop()
        sci_dataset.create()

    def test_002(self):
        try:
            sql = 'select * from {}'.format(const.tbl_sci_dataset)
            result1 = sci_dataset.query(sql)

            entity1 = SciDataset()
            entity1.fileid = utils.gen_uuid4()

            entity2 = SciDataset()
            entity2.fileid = utils.gen_uuid4()

            sci_dataset.insert([entity1.__dict__, entity2.__dict__])

            result2 = sci_dataset.query(sql)
            self.assertEqual(len(result2) - len(result1), 2, '插入应该是2条记录')
        except Exception as e:
            self.fail('批量插入表{}失败'.format(const.tbl_sci_dataset))

    def test_003(self):
        result = sci_dataset.query('select * from {}'.format(const.tbl_sci_dataset))
        print(result)


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
