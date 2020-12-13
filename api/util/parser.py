'''
api/util负责管理所有的工具类代码
'''
from typing import List, Set
import os
import jieba
import nltk
from lxml import etree
from scrapy import Selector

from api import config, model, util
from api.model.__init__ import OdsCnkiBib
from api.util import utils


def parsefiles(format, files: List[str]) -> List[OdsCnkiBib]:
    """
    根据文件类型，解析文件
    """
    def __parse_onefile(file):
        result = []
        if format == config.ds_gbt_7714_2015:
            result = File_gbt_7714_2015_Parser(file).parse()
        elif format == config.ds_cnki_es5:
            result = File_cnki_es5_Parser(file).parse()
        elif format == config.ds_note_express:
            result = File_noteExpress_Parser(file).parse()
        return result

    datas = []
    for file in files:
        datas.extend(__parse_onefile(file))
    return datas

class File_cnki_es5_Parser:
    def __init__(self, filepath):
        """
            解析cnki的es5格式
            :param filepath: 文件路径
            :return: 解析后的数据列表
            """
        assert os.path.exists(filepath), 'es5文件{}必须存在'.format(filepath)
        # 读取内容
        text = utils.read_lines(filepath)
        text = ''.join(text)
        xml = text[:text.find('</CNKINOTE>') + len('</CNKINOTE>')]
        xml = bytes(bytearray(xml, encoding='utf-8'))
        root = etree.XML(xml)
        if 'CNKINOTE' != root.tag:
            raise Exception('不是es5格式')
        cnkiliters = root.getchildren()[0]
        self.cnkidata = [cnkidata for cnkidata in cnkiliters]

    def parse(self):
        return [self.__parse(cnkidata) for cnkidata in self.cnkidatas]

    def __parse(self, cnkidata):
        cnkiEs5 = OdsCnkiBib()
        cnkiEs5.id = utils.gen_uuid4()
        for child in cnkidata.getchildren():
            tag = child.tag.lower()
            content = str(child.text).strip()
            if tag == 'DataType'.lower():
                cnkiEs5.style = self.__style(content)
            if tag == 'Title'.lower():
                cnkiEs5.title = content
                if utils.strings_is_eng(cnkiEs5.title):
                    cnkiEs5.lang = '外文'
            if tag == 'Author'.lower():
                authors = content.split(';')
                authors = [a.strip() for a in authors if a.strip()]
                cnkiEs5.firstduty = authors[0]
                cnkiEs5.authors = authors
            if tag == 'Source'.lower():
                cnkiEs5.publication = content
            if tag == 'PubTime'.lower():
                if content:
                    cnkiEs5.pubtime = content[:10]
                    cnkiEs5.pubyear = int(content[:4])
            if tag == 'Keyword'.lower():
                kws = content.split(';')
                kws = [a.strip() for a in kws if a.strip()]
                cnkiEs5.kws = kws
            if tag == 'Summary'.lower():
                cnkiEs5.summary = content
            if tag == 'Organ'.lower():
                orgs = content.split(';')
                orgs = [a.strip() for a in orgs if a.strip()]
                cnkiEs5.orgs = orgs

        return cnkiEs5

    def __style(self, v):
        v = str(v).strip()
        if v == '1':
            return '期刊'
        elif v == '2':
            return '学位论文'
        elif v == '3':
            return '会议'
        elif v == '4':
            return '报纸'
        elif v == '5':
            return '图书'
        elif v == '6':
            return '年鉴'
        elif v == '60':
            return '专利'
        elif v == '61':
            return '成果'
        elif v == '62':
            return '标准'
        else:
            return '不确定值' + v

class File_gbt_7714_2015_Parser:
    def __init__(self, filepath):
        # GBT 7714-2015格式，参考http://manu49.magtech.com.cn/journalx_gdgyzrb/UserFiles/File/GBT7714-2015.pdf
        """
        解析gbt/7714-2015格式
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
        assert os.path.exists(filepath), 'gbt/7714-2015文件{}必须存在'.format(filepath)
        # 读取内容
        lines = utils.read_lines(filepath)
        # 去掉开头的序号
        lines = [line[line.find(']') + 1:].strip() for line in lines]
        # 如果一行内容带有url，必须去掉url再判断
        self.lines = [line[:line.find('.http')] if line.find('.http') > 0 else line for line in lines]
        # 如果一行内容中带有DOI，去掉
        self.lines = [line[:line.find('DOI:')] if line.find('DOI:') > 0 else line for line in lines]

    def parse(self):
        return [self.__parse(line) for line in self.lines]

    def __parse(self, line):
        if utils.strings_is_eng(line):
            return self.__parse_eng(line)
        else:
            return self.__parse_cn(line)

    def __style(self, v):
        v = str(v).strip()
        if v == 'J' or v == 'J/OL':
            return '期刊'
        elif v == 'D':
            return '学位论文'
        elif v == 'N':
            return '报纸'
        else:
            return '不确定类型'

    def __parse_eng(self, line):
        print(line)
        entity = OdsCnkiBib()
        entity.id = utils.gen_uuid4()
        # 语种
        entity.lang = '外文'
        # 题名
        title = line[:line.find('[')]
        entity.title = title
        # print(title)
        line = line[line.find('[') + 1:]
        # 文献类型
        style = line[line.find('[') + 1:line.find(']')]
        entity.style = self.__style(style)
        return entity

    def __parse_cn(self, line):
        entity = OdsCnkiBib()
        entity.id = utils.gen_uuid4()
        entity.line = line
        subs = line.split('.')

        if len(subs) == 2:
            entity.firstduty, entity.authors = self.__parse_cn_firstduty_authors(subs[0])
            entity.title = subs[1]
        elif len(subs) >= 3:
            entity.firstduty, entity.authors = self.__parse_cn_firstduty_authors(subs[0])
            entity.title, entity.style = self.__parse_cn_title_style(subs[1])
            entity.publication, entity.pubyear = self.__parse_cn_publication_pubyear(subs[2].strip())

        return entity


    def __parse_cn_firstduty_authors(self, s: str):
        ss = s.split(',')
        return ss[0], ss

    def __parse_cn_title_style(self, s1: str):
        style = s1[s1.find('[') + 1:s1.find(']')]
        return s1[:s1.find('[')], self.__style(style)

    def __parse_cn_publication_pubyear(self, s):
        s22 = s.split(',')
        if len(s22) == 2:
            return s22[0], s22[1].split(':')[0].strip()
        return s22[0], ''

class File_noteExpress_Parser:
    def __init__(self, filepath):
        """
            解析NoteExpress格式
            :param filepath: 文件路径
            :return: 解析后的数据列表
            """
        assert os.path.exists(filepath), 'NoteExpress文件{}必须存在'.format(filepath)
        # 读取内容
        self.lines = utils.read_lines(filepath)

    def parse(self):

        result = []
        for line in self.lines:
            if line.startswith('{Reference Type}:'):
                noteExpress = model.OdsCnkiBib()
                noteExpress.id = util.gen_uuid4()
                result.append(noteExpress)
                noteExpress.referenceType = line[len('{Reference Type}:'):].strip()
            elif line.startswith('{Title}: '):
                noteExpress.title = line[len('{Title}: '):].strip()
                if utils.strings_is_eng(noteExpress.title):
                    noteExpress.lang = '外文'
            elif line.startswith('{Tertiary Title}: '):
                pass
                # noteExpress.tertiaryTitle = line[len('{Tertiary Title}: '):].strip()
            elif line.startswith('{Author}: '):
                author = line[len('{Author}: '):].strip()
                authors = [a.strip() for a in author.split(';') if a.strip()]
                noteExpress.authors = authors
                noteExpress.firstduty = authors[0]
            elif line.startswith('{Author Address}: '):
                orgs = line[len('{Author Address}: '):].strip()
                orgs = [a.strip() for a in orgs.split(';') if a.strip()]
                noteExpress.orgs = orgs
            elif line.startswith('{Secondary Title}: '):
                pass
                # noteExpress.secondaryTitle = line[len('{Secondary Title}: '):].strip()
            elif line.startswith('{Place Published}: '):
                pass
                # noteExpress.placePublished = line[len('{Place Published}: '):].strip()
            elif line.startswith('{Subsidiary Author,}: '):
                pass
                # noteExpress.subsidiaryAuthor = line[len('{Subsidiary Author,}: '):].strip()
            elif line.startswith('{Year}: '):
                noteExpress.pubyear = int(line[len('{Year}: '):].strip())
            elif line.startswith('{Pages}: '):
                pass
                # noteExpress.pages = line[len('{Pages}: '):].strip()
            elif line.startswith('{Keywords}: '):
                kws = line[len('{Keywords}: '):].strip()
                kws = [a.strip() for a in kws.split(';') if a.strip()]
                noteExpress.kws = kws
            elif line.startswith('{Abstract}: '):
                noteExpress.summary = line[len('{Abstract}: '):].strip()

        return result

class File_cnki_html_Parser:
    def __init__(self, filepath):
        """
        解析cnki的html格式
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
        assert os.path.exists(filepath), 'CNKI的html文件{}必须存在'.format(filepath)
        content = utils.read_lines(filepath)
        self.content = ''.join(content)

    def parse(self):
        selector = Selector(text=self.content)
        # 来源url
        source_url = selector.xpath(
            '//div[@class="content"]/div[@class="tips"]/a/@href').extract_first()
        # 来源name
        source_name = selector.xpath(
            '//div[@class="content"]/div[@class="tips"]/a/text()').extract_first()
        print(source_name)
        # TODO 来源其他信息
        source_other = selector.xpath(
            '//div[@class="content"]/div[@class="tips"]/text()').extract_first()
        source_other = source_other.strip() if source_other else ''
        print(source_other)
        # 标题
        title = selector.xpath('//h1[@class="title"]/span/text()').extract_first()
        title = title.strip() if title else ''
        print(title)
        # 作者
        authors = selector.xpath('//h2[1]/a/text()').extract()
        print(authors)
        # 作者url
        authors_url = selector.xpath('//h2[1]/a/@href').extract()
        print(authors_url)
        # 机构
        orgs = selector.xpath('//h2[2]/a/text()').extract()
        print(orgs)
        # 机构url
        orgs_url = selector.xpath('//h2[1]/a/@href').extract()
        print(orgs_url)
        # 摘要
        abstract = selector.xpath(
            '//div[@id="a_abstract"]/p/text()').extract_first()
        abstract = abstract.strip() if abstract else ''
        print('摘要', abstract)
        # 关键词
        keywords = selector.xpath('//div[@id="a_keywords"]/p/a/text()').extract()
        keywords = [str(kw).replace(';', '') for kw in keywords]
        print('关键词', keywords)
        # 参考文献
        for ref in selector.xpath('//div[@id="a_bibliography"]/p'):
            name = ref.xpath('a//text()').extract_first()
            url = ref.xpath('a/@href').extract_first()
            print('参考文献', name, url)

def stopwords(splitwords_userdict_path: str = None):
    if not os.path.exists(splitwords_userdict_path):
        return set()
    reader = open(splitwords_userdict_path, encoding='utf8')
    lines = reader.readlines()
    reader.close()
    lines = [w.lower().strip() for w in lines]
    # todo 这里还不对那
    # nltk.download('stopwords')
    # nltk_stop_words = set(nltk.corpus.stopwords.words('english'))
    # return set(lines) | nltk_stop_words
    return set(lines)

class CutWords:
    def __init__(self, splitwords_userdict_path: str = ''):
        if os.path.exists(splitwords_userdict_path):
            jieba.load_userdict(splitwords_userdict_path)
        nltk.download('punkt')
        nltk.download('wordnet')

    def cut_words(self, line: str, stopwords: Set[str]) -> List[str]:
        """
        切词，可以使用停用词
        """
        assert stopwords != None, '必须使用停用词'
        if utils.strings_is_eng(line):
            words = nltk.word_tokenize(line)
        else:
            words = [w for w in jieba.cut(line)]
        # 过滤停用词
        words = [w for w in words if str(w).lower() not in stopwords]
        # 英文词干化、词性还原
        if utils.strings_is_eng(line):
            lemma_word = []
            wordnet_lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
            for w in words:
                word1 = wordnet_lemmatizer.lemmatize(w, pos="n")
                word2 = wordnet_lemmatizer.lemmatize(word1, pos="v")
                word3 = wordnet_lemmatizer.lemmatize(word2, pos=("a"))
                # pos参数 是词性
                lemma_word.append(word3)
            # todo 英文切词后，还会有一个单引号在里面，这是不正确的
            words = [w for w in lemma_word if str(w).find("'") == -1]

        return words
