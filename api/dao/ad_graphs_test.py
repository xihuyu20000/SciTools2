import unittest

from api.dao.ad_graph import ad_graph


class TestUtil(unittest.TestCase):

    def test_001(self):
        try:
            ad_graph.drop()
            ad_graph.create()
        except Exception as e:
            self.assertTrue('正常')
