'''
api/test负责所有的测试实例
'''
import os
import tempfile
import unittest
import shutil
from api import util
from api.util import CutWords


class TestUtil(unittest.TestCase):

    def test_gen_uuid(self):
        uid = util.gen_uuid1()
        self.assertTrue(len(uid) == 32, 'uuid的长度必须是32位')

    def test_move_file(self):
        srcDir = tempfile.mkdtemp()
        srcFile = os.path.join(srcDir, 'a.txt')
        with open(srcFile, 'w', encoding='utf8') as writer:
            writer.write('aaaaaa')
        dstDir = tempfile.mkdtemp()
        util.move_file(srcFile=srcFile, dstDir=dstDir)
        self.assertTrue(len(os.listdir(dstDir)) == 1, '复制失败')
        self.assertTrue(len(os.listdir(srcDir))==0, '删除源文件失败')

    def test_cut_words_cn(self):
        cutwords = CutWords()
        words = cutwords.cut_words('关键词时间特征分布视角下的研究前沿探测研究', stopwords=set(['下', '的']))
        self.assertTrue(words == ['关键词', '时间', '特征', '分布', '视角', '研究', '前沿', '探测', '研究'], '切词结果必须是'+'、'.join(words))

    def test_cut_words_en(self):
        cutwords = CutWords()
        words = cutwords.cut_words("Tom's dad And mum", stopwords=set(['does', 'to', 'and']))
        self.assertTrue(words == ['Tom', "'s", 'dad', 'mum'], '切词结果必须是' + '、'.join(words))

        pass



if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
