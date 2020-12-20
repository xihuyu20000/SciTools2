import threading

import jieba
from pydantic.main import BaseModel

from api.dao.db.ods_bib import OdsCnkiBib
from api.util.utils import Logger
from api import dao, config
import re

regex = re.compile('\s+')


class OdsbibDeleteForm(BaseModel):
    ids: list = []


class OdsbibUpdateForm(BaseModel):
    id: str = None
    k: str = None
    v: str = None


class DatasetManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    # 查询所有数据集的名称
    def list_names(self):
        sql = """ SELECT * FROM {} """.format(config.tbl_dim_dataset)
        return self.dao.find_dim_dataset(sql)

    # 根据特定数据集
    def list_dataset(self, dsid):
        sql = "SELECT * FROM {} WHERE dsid ='{}'".format(config.tbl_ods_bib, dsid)
        return self.dao.find_ods_bib(sql)


    def __update_clean_status(self, dsid, status):
        sql = "ALTER TABLE {} UPDATE status='{}' WHERE dsid = '{}'".format(config.tbl_dim_dataset, status, dsid)
        dao.update_dim_dataset(sql)

    def showProcess(self, dsid):
        sql = "SELECT * FROM {} WHERE dsid='{}'".format(config.tbl_dim_dataset, dsid)
        self.log.info(sql)
        return self.dao.find_dim_dataset(sql)

    # 根据dsid删除数据集
    def delete(self, dsid):
        sql = "ALTER TABLE  {} DELETE WHERE dsid = '{}'".format(config.tbl_dim_dataset, dsid)
        dao.update_dim_dataset(sql)
        sql = "ALTER TABLE  {} DELETE WHERE dsid='{}'".format(config.tbl_ods_bib, dsid)
        dao.update_ods_bib(sql)

    # 修改数据集名称
    def rename(self, dsid, newName):
        sql = "ALTER TABLE {} UPDATE dsname='{}' WHERE dsid = '{}'".format(config.tbl_dim_dataset, newName, dsid)
        dao.update_dim_dataset(sql)

    # 删除ods_bib表中的数据
    def deleteOdsbibById(self, ids):
        for id in ids:
            sql = "ALTER TABLE  {} DELETE WHERE id = '{}'".format(config.tbl_ods_bib, id)
            dao.update_ods_bib(sql)

    # 更新ods_bib表中的数据
    def updateOdsbib(self, form):
        arr_keys = [k for k, v in OdsCnkiBib().__dict__.items() if type(v) == list] # 列表类型的字段
        if form.k in arr_keys:  # 如果类型是数组，使用这个语句
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, form.k, form.v.split(','), form.id)
        else:
            sql = "ALTER TABLE {} UPDATE {}='{}' WHERE id='{}'".format(config.tbl_ods_bib, form.k, form.v, form.id)
        dao.update_ods_bib(sql)

    # 清洗数据集，清洗结束，修改dim_dataset的状态
    def clean(self, dsid, userid):
        self.__update_clean_status(dsid, '开始清洗')

        cleaner = DatasetCleaner(dsid, userid)

        # 标题分词，加载停用词表、自定义词典，填充title_words
        self.__update_clean_status(dsid, '标题分词')
        cleaner.fill_title_words()

        # 摘要分词，加载停用词表、自定义词典，填充summary_words
        self.__update_clean_status(dsid, '摘要分词')
        cleaner.fill_summary_words()

        # 机构名称规范
        self.__update_clean_status(dsid, '机构名称规范')
        cleaner.fill_orgs2()

        # 根据orgs2判断地区，填充province
        self.__update_clean_status(dsid, '地区名称规范')
        cleaner.fill_province()

        # 基金类型，填充funds2
        self.__update_clean_status(dsid, '基金名称规范')
        cleaner.fill_funds2()

        # todo 学科分类，填充subject1、subject2
        self.__update_clean_status(dsid, '学科名称规范')
        cleaner.fill_subject()

        # todo 国家共现
        self.__update_clean_status(dsid, '国家共现')
        cleaner.co_country()

        # todo 机构共现
        self.__update_clean_status(dsid, '机构共现')
        cleaner.co_org()

        # todo 地区共现
        self.__update_clean_status(dsid, '地区共现')
        cleaner.co_province()

        # todo 关键词共现
        self.__update_clean_status(dsid, '关键词共现')
        cleaner.co_keywords()

        # 清洗结束，修改dim_dataset的状态
        self.__update_clean_status(dsid, '清洗完成')



datasetManager = DatasetManager()

import collections
# 下面的清洗操作，一定要使用线程池
import threadpool

pool = threadpool.ThreadPool(100)  # clickhouse默认允许线程池最大100


class DatasetCleaner:
    def __init__(self, dsid, userid):
        self.dsid = dsid
        self.userid = userid
        self.log = Logger(__name__).get_log
        self.dao = dao
        sql = "SELECT * FROM {} WHERE dsid ='{}'".format(config.tbl_ods_bib, dsid)
        self.dataset = self.dao.find_ods_bib(sql)

        # 加载停用词表
        self.stopwords = self.__load_dim_config_text('stopwords_style', 'stopwords_text')
        print('停用词大小', len(self.stopwords))

        # 加载自定义词典
        splitwords = self.__load_dim_config_text('splitwords_style', 'splitwords_text')
        print('自定义分词大小', len(splitwords))
        for word in splitwords:
            jieba.add_word(word)

        # 加载同义词词典
        synonymwords = self.__load_dim_config_text('synonymwords_style', 'synonymwords_text')
        self.synonydict = collections.defaultdict(str)
        for line in synonymwords:
            arr = line.split('=')
            if len(arr) == 2:
                olds = arr[0].split(';')
                for old in olds:
                    self.synonydict[old.strip()] = arr[1].strip()
        print('同义词字典大小', len(self.synonydict))

        # 加载机构规范字典
        self.orgnorm = self.__load_dim_config_text('orgnorm_style', 'orgnorm_text')
        self.orgnorm = [name.strip() for name in self.orgnorm if name.strip()]
        self.orgnorm = [name for name in self.orgnorm if len(name.split(';'))==2] #只有分割是2部分的才可以使用
        print('机构名称规范词典大小', len(self.orgnorm))
        # 该属性在处理province的时候使用
        self.dim_orgs = dao.find_dim_org("""SELECT * FROM {} """.format(config.tbl_dim_org))
        orgnames = [org['orgname'] for org in self.dim_orgs]
        orgnames.extend([org.split(';')[0].strip() for org in self.orgnorm])
        for name in orgnames:
            jieba.add_word(name)

        # todo 加载机构合并词典

        # todo 加载著者合并词典

        # todo 加载地区合并词典

        # todo 加载国家合并词典

        # todo 加载基金合并词典

        # todo 加载学科分类词典

    def fill_title_words(self):
        # 标题分词，填充title_words
        sqls = []
        for row in self.dataset:
            words = [x for x in jieba.cut(row['title']) if x not in self.stopwords]
            words = [self.synonydict.get(x) if x in self.synonydict.keys() else x for x in words]  # 同义词处理，替换为新的词
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'title_words', words,
                                                                     row['id'])
            sqls.append(sql)
        requests = threadpool.makeRequests(dao.update_ods_bib, sqls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def fill_summary_words(self):
        # 摘要分词，填充summary_words
        sqls = []
        for row in self.dataset:
            words = [x for x in jieba.cut(row['summary']) if x not in self.stopwords]
            words = [self.synonydict.get(x) if x in self.synonydict.keys() else x for x in words]  # 同义词处理，替换为新的词
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'summary_words', words, row['id'])
            sqls.append(sql)
        requests = threadpool.makeRequests(dao.update_ods_bib, sqls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def fill_orgs2(self):
        # 判断机构名称，填充orgs2
        sqls = []
        for row in self.dataset:
            orgs2 = [[x for x in jieba.cut(org)][0] for org in row['orgs']]
            row['org2'] = orgs2 # 填充数据，在后面清洗时立刻使用
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'orgs2', orgs2, row['id'])
            sqls.append(sql)
        requests = threadpool.makeRequests(dao.update_ods_bib, sqls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def fill_province(self):
        # 根据orgs2判断地区，填充province
        org_dict = dict([(org['orgname'],org['province']) for org in self.dim_orgs])
        org_dict_user = dict([(org.split(';')[0].strip(), org.split(';')[1].strip()) for org in self.orgnorm])    # 这是用户自己输入的
        org_dict = {**org_dict, **org_dict_user}    # 把2个字典合并成一个

        def __get_province(org_name):
            return org_dict[org_name] if org_name in org_dict.keys() else ''

        sqls = []
        for row in self.dataset:
            if row['orgs2']:    # 可能没有值
                province = [__get_province(org_name) for org_name in row['orgs2']]
                province = [p for p in province if p]   # 去除空白
                sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'province', province, row['id'])
                sqls.append(sql)
        requests = threadpool.makeRequests(dao.update_ods_bib, sqls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def fill_funds2(self):
        # 基金类型，填充funds2
        def __get_fund_style(s):
            s = str(s)
            if s.startswith('国家'):
                return '国家'
            elif s.find('省')>0 or s.find('市')>0:
                return '省市'
            elif s.find('高校')>-1 or s.find('大学')>-1:
                return '高校'
            elif s.find('部')>-1:
                return '部委'
            elif s.find('公司')>-1 or s.find('企业')>-1:
                return '企业'
            return '其他'

        sqls = []
        for row in self.dataset:
            if row['funds']:
               funds2 = [__get_fund_style(fund) for fund in row['funds']]
               sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'funds2', funds2, row['id'])
               sqls.append(sql)


        requests = threadpool.makeRequests(dao.update_ods_bib, sqls)
        [pool.putRequest(req) for req in requests]
        pool.wait()


    def fill_subject(self):
        # todo 学科分类，填充subject1、subject2
        pass

    def co_country(self):
        # todo 国家共现
        pass

    def co_org(self):
        # todo 机构共现
        pass

    def co_province(self):
        # todo 地区共现
        pass

    def co_keywords(self):
        # todo 关键词共现
        pass

    def __load_dim_config_text(self, config_style, text):
        # 查询使用策略
        style = self.__query_dim_config(self.userid, config_style)

        # 根据策略，加载词典
        if style == '1':
            result = self.__query_dim_config(config.default_user, text)
            return set(regex.split(result))
        elif style == '2':
            result = self.__query_dim_config(self.userid, text)
            return set(regex.split(result))
        elif style == '3':
            result1 = self.__query_dim_config(config.default_user, text)
            result2 = self.__query_dim_config(self.userid, text)
            return set(regex.split(result1)) | set(regex.split(result2))
        return set()

    def __query_dim_config(self, userid, style):
        '''
        查询dim_config文件的值。返回值是个字符串
        '''
        sql = "SELECT values FROM {} WHERE userid ='{}' AND style='{}'".format(config.tbl_dim_config, userid, style)
        result = dao.query_dim_config(sql)
        return result[0]['values'] if result else ''


OdsbibDeleteForm
