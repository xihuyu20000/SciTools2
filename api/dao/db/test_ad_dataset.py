import unittest

from api import config
from api.dao.db import ad_tbls
from api.util.utils import gen_uuid4


class TestUtil(unittest.TestCase):
    def test_ddl(self):
        ad_tbls.drop()
        ad_tbls.create()

    def test_insert(self):
        titles = [('列1', '文本'), ('列2', '数值')]
        tblid = gen_uuid4()
        userid = gen_uuid4()
        l1 = len(ad_tbls.query('select tblid from {}'.format(config.tbl_ad_tbls)))
        ad_tbls.insert(tblid, userid, '表面', titles)
        l2 = len(ad_tbls.query('select tblid from {}'.format(config.tbl_ad_tbls)))
        self.assertEquals(l2-l1,1)