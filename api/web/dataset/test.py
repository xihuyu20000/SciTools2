import unittest

from api.web.dataset.manager import StatManager


class StatTest(unittest.TestCase):

    # 如果跑所有用例，只运行一次前提条件和结束条件。则用setupclass()和teardownclass()
    def setUp(self):
        self.biz = StatManager()


import unittest

if __name__ == '__main__':
    unittest.main()
