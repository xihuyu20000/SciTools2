import jieba
from pydantic.main import BaseModel

from api.util.utils import Logger
from api import dao, config
from api.dao.db import __execute as execute

class OdsbibDeleteForm(BaseModel):
    ids:list= []

class OdsbibUpdateForm(BaseModel):
    id:str = None
    k:str = None
    v:str = None

class DatasetManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    # 查询所有数据集的名称
    def list_names(self):
        sql = """ SELECT * FROM {} """.format(config.tbl_dim_dataset)
        self.log.info(sql)
        return self.dao.find_dim_dataset(sql)


    # 根据特定数据集
    def list_dataset(self, dsid):
        sql = "SELECT * FROM {} WHERE dsid ='{}'".format(config.tbl_ods_bib, dsid)
        self.log.info(sql)
        return self.dao.find_ods_bib(sql)

    # 清洗数据集，清洗结束，修改dim_dataset的状态
    def clean(self, dsid):
        self.__update_clean_status(dsid, '开始清洗')

        cleaner = DatasetCleaner(dsid)

        # todo 标题分词，加载停用词表、自定义词典，填充title_words
        cleaner.fill_title_words()
        self.__update_clean_status(dsid, '标题分词')

        # todo 摘要分词，加载停用词表、自定义词典，填充summary_words
        cleaner.fill_summary_words()
        self.__update_clean_status(dsid, '摘要分词')

        # todo 判断地区，填充province
        cleaner.fill_province()
        self.__update_clean_status(dsid, '地区规范')

        # todo 基金类型，填充funds_style
        cleaner.fill_funds_style()
        self.__update_clean_status(dsid, '基金规范')

        # todo 学科分类，填充subject1、subject2
        cleaner.fill_subject()
        self.__update_clean_status(dsid, '学科规范')

        # todo 国家共现
        cleaner.co_country()
        self.__update_clean_status(dsid, '国家共现')

        # todo 机构共现
        cleaner.co_org()
        self.__update_clean_status(dsid, '机构共现')

        # todo 地区共现
        cleaner.co_province()
        self.__update_clean_status(dsid, '地区共现')

        # todo 关键词共现
        cleaner.co_keywords()
        self.__update_clean_status(dsid, '词规范')

        # 清洗结束，修改dim_dataset的状态
        self.__update_clean_status(dsid, '清洗完成')

    def __update_clean_status(self, dsid, status):
        sql = "ALTER TABLE {} UPDATE status='{}' WHERE dsid = '{}'".format(config.tbl_dim_dataset, status, dsid)
        self.log.info(sql)
        execute(sql)

    def showProcess(self, dsid):
        sql = "SELECT * FROM {} WHERE dsid='{}'".format(config.tbl_dim_dataset, dsid)
        self.log.info(sql)
        return self.dao.find_dim_dataset(sql)

    # 根据dsid删除数据集
    def delete(self, dsid):
        sql = "ALTER TABLE  {} DELETE WHERE dsid = '{}'".format(config.tbl_dim_dataset, dsid)
        self.log.info(sql)
        execute(sql)
        sql = "ALTER TABLE  {} DELETE WHERE dsid='{}'".format(config.tbl_ods_bib, dsid)
        self.log.info(sql)
        execute(sql)

    # 修改数据集名称
    def rename(self, dsid, newName):
        sql = "ALTER TABLE {} UPDATE dsname='{}' WHERE dsid = '{}'".format(config.tbl_dim_dataset, newName, dsid)
        self.log.info(sql)
        execute(sql)

    # 删除ods_bib表中的数据
    def deleteOdsbibById(self, ids):
        for id in ids:
            sql = "ALTER TABLE  {} DELETE WHERE id = '{}'".format(config.tbl_ods_bib, id)
            self.log.info(sql)
            execute(sql)

    # 更新ods_bib表中的数据
    def updateOdsbib(self, form):
        print(form)
        if form.k in ['authors','orgs','funds','clcs']:   # 如果类型是数组，使用这个语句
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib,form.k, form.v.split(','), form.id)
        else:
            sql = "ALTER TABLE {} UPDATE {}='{}' WHERE id='{}'".format(config.tbl_ods_bib, form.k, form.v, form.id)
        self.log.info(sql)
        execute(sql)

datasetManager = DatasetManager()

class DatasetCleaner:
    def __init__(self, dsid):
        self.dsid = dsid
        self.log = Logger(__name__).get_log
        self.dao = dao
        sql = "SELECT * FROM {} WHERE dsid ='{}'".format(config.tbl_ods_bib, dsid)
        self.log.info(sql)
        self.dataset = self.dao.find_ods_bib(sql)

    def fill_title_words(self):
        # todo 标题分词，加载停用词表、自定义词典，填充title_words
        for row in self.dataset:
            words = [x for x in jieba.cut(row['title'])]
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'title_words', words, row['id'])
            self.log.info(sql)
            execute(sql)


    def fill_summary_words(self):
        # todo 摘要分词，加载停用词表、自定义词典，填充summary_words
        for row in self.dataset:
            words = [x for x in jieba.cut(row['summary'])]
            sql = "ALTER TABLE {} UPDATE {}={} WHERE id='{}'".format(config.tbl_ods_bib, 'summary_words', words, row['id'])
            self.log.info(sql)
            execute(sql)


    def fill_province(self):
        # todo 判断地区，填充province
        pass


    def fill_funds_style(self):
        # todo 基金类型，填充funds_style
        pass


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


    def __load_stopwords_text(self):
        # todo 加载停用词词典
        pass

    def __load_splitwords_text(self):
        # todo 加载分词词典
        pass

    def __load_synonymwords_text(self):
        # todo 加载同义词词典
        pass

    def __load_combineauthor_text(self):
        # todo 加载著者合并词典
        pass

    def __load_combineorg_text(self):
        #todo 加载机构合并词典
        pass

    def __load_combineprovince_text(self):
        # todo 加载地区合并词典
        pass

    def __load_combinecountry_text(self):
        # todo 加载国家合并词典
        pass

    def __load_combinefund_text(self):
        # todo 加载基金合并词典
        pass

    def __load_combinebranch_text(self):
        # todo 加载学科分类词典
        pass