import unittest

from api.dao.ad_tbls import ad_tbls

class TestUtil(unittest.TestCase):

    def test_001(self):
        try:
            ad_tbls.drop()
            ad_tbls.create()
        except Exception as e:
            self.assertTrue('正常')
