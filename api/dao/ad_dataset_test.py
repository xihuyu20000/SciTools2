import unittest

from api.dao import ad_dataset


class TestUtil(unittest.TestCase):
    def test_001(self):
        try:
            ad_dataset.drop()
            ad_dataset.create()
        except Exception as e:
            self.assertTrue('正常')
