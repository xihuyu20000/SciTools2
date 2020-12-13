import unittest
from api import config
from api.dao.db.clickhouse_db import dim_config
from api.model.dim import DimDict


class TestUtil(unittest.TestCase):
    def read_files(self, filename):
        with open(filename, encoding='utf8') as reader:
            lines = reader.readlines()
            return lines
        return []
    def test_dim_dict(self):
        try:
            dim_config.drop_dim_config()
            dim_config.create_dim_config()
            dim_config.truncate_dim_config()
            # 年份
            year = DimDict()
            year.userid = 'default'
            year.style = 'year'
            year.values = [str(i) for i in range(1900, 2051)]
            dim_config.insert_dim_config([year.to_dict()])
            # 停用词类型
            stopwords_style = DimDict()
            stopwords_style.userid = 'default'
            stopwords_style.style = 'stopwords_style'
            stopwords_style.values = '0'
            dim_config.insert_dim_config([stopwords_style.to_dict()])
            # 停用词内容
            stopwords_text = DimDict()
            stopwords_text.userid = 'default'
            stopwords_text.style = 'stopwords_text'
            stopwords_text.values = self.read_files('stopwords.txt')
            dim_config.insert_dim_config([stopwords_text.to_dict()])


        except Exception as e:
            self.fail('删除然后创建表{}失败'.format(config.tbl_dim_config))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
