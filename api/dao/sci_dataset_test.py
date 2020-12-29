import unittest

from api import const

from api.dao.sci_dataset import SciDataset, sci_dataset
from api.util import utils


class TestUtil(unittest.TestCase):
    def test_001(self):
        sci_dataset.drop()
        sci_dataset.create()

    def test_002(self):
        sql = 'select * from {table}'
        result1 = sci_dataset.query(sql)

        entity1 = SciDataset()
        entity1.fileid = utils.gen_uuid4()

        entity2 = SciDataset()
        entity2.fileid = utils.gen_uuid4()

        sci_dataset.insert([entity1.dict(), entity2.dict()])

        result2 = sci_dataset.query(sql)
        self.assertEqual(len(result2) - len(result1), 2, '插入应该是2条记录')


    def test_003(self):
        result = sci_dataset.query('select * from {table}')
        print(result)


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
