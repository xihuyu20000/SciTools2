import unittest
from unittest import defaultTestLoader

# 测试用例存放顶级路径
case_path = 'dao'

# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*_test.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == '__main__':
    # 运行测试用例
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())