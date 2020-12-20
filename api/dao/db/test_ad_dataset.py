import unittest

from api import config
from api.dao.db import ad_dataset
from api.util.utils import gen_uuid4


class TestUtil(unittest.TestCase):
    def test_ddl(self):
        ad_dataset.drop()
        ad_dataset.create()
