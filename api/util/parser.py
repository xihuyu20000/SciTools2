'''
api/util负责管理所有的工具类代码
'''
from typing import List, Set
import os
import copy
import jieba
import nltk
from lxml import etree
from scrapy import Selector

from api import config, util
from api.dao.db.ods_bib import OdsCnkiBib
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
        elif format == config.ds_cnki_self:
            result = File_cnki_self_Parser(file).parse()
        elif format == config.ds_cssci_format:
            result = File_cssci_Parser(file).parse()
        elif format == config.ds_wos_tab_format:
            result = File_wos_tab_Parser(file).parse()

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
        if os.path.exists(filepath):
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
                    # cnkiEs5.pubtime = content[:10]
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
        if os.path.exists(filepath):
            # 读取内容
            lines = utils.read_lines(filepath)
            # 去掉开头的序号
            lines = [line[line.find(']') + 1:].strip() for line in lines]
            # 如果一行内容带有url，必须去掉url再判断
            self.lines = [line[:line.find('.http')] if line.find('.http') > 0 else line for line in lines]
            # 如果一行内容中带有DOI，去掉
            self.lines = [line[:line.find('DOI:')] if line.find('DOI:') > 0 else line for line in lines]

    def parse(self):
        return [self._parse(line) for line in self.lines]

    def _parse(self, line):
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
        entity = OdsCnkiBib()
        entity.id = utils.gen_uuid4()
        entity.line = line
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
        if len(s22) == 1:
            return s22[0], ''
        else:
            return s22[0], s22[1].split(':')[0].strip()


class File_noteExpress_Parser:
    def __init__(self, filepath):
        """
            解析NoteExpress格式
            :param filepath: 文件路径
            :return: 解析后的数据列表
            """
        if os.path.exists(filepath):
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
        if os.path.exists(filepath):
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


class File_cnki_self_Parser:
    def __init__(self, filepath):
        """
        解析cnki的自定义格式
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
        if os.path.exists(filepath):
            self.lines = utils.read_lines(filepath)

    def parse(self):
        art_lines = self.__build_raw_articles()
        return [self.__parse_raw_article(art) for art in art_lines]

    def __build_raw_articles(self):
        arts = []
        temp_art = []
        for line in self.lines:
            if line.startswith('SrcDatabase-来源库'):
                if temp_art:
                    arts.append(copy.deepcopy(temp_art))
                temp_art = []
            temp_art.append(line)
        return arts

    def __parse_raw_article(self, lines):
        model = OdsCnkiBib()
        model.id = utils.gen_uuid4()
        model.line = '\t'.join(lines)
        model.style = '期刊'

        for line in lines:
            if line.startswith('Title-题名'):
                model.title = line[len('Title-题名:'):].strip()
            elif line.startswith('Author-作者:'):
                authors = line[len('Author-作者:'):].strip()
                authors = authors.split(';')
                authors = [x.strip() for x in authors if x.strip()]
                model.authors = authors
            elif line.startswith('Organ-单位:'):
                orgs = line[len('Organ-单位:'):].strip()
                orgs = orgs.split(';')
                orgs = [x.strip() for x in orgs if x.strip()]
                model.orgs = orgs
            elif line.startswith('Source-文献来源:'):
                publication = line[len('Source-文献来源:'):].strip()
                model.publication = publication
            elif line.startswith('Keyword-关键词:'):
                kws = line[len('Keyword-关键词:'):].strip()
                kws = kws.split(';')
                kws = [x.strip() for x in kws if x.strip()]
                model.kws = kws
            elif line.startswith('Summary-摘要:'):
                summary = line[len('Summary-摘要:'):].strip()
                model.summary = summary
            # elif line.startswith('PubTime-发表时间:'):
            #     pubtime = line[len('PubTime-发表时间:'):].strip()
            #     pubtime = line[:10]
            #     model.pubtime = pubtime
            elif line.startswith('FirstDuty-第一责任人:'):
                firstduty = str(line[len('FirstDuty-第一责任人:'):]).strip()
                firstduty = firstduty.split(';')[0]
                model.firstduty = firstduty
            elif line.startswith('Fund-基金:'):
                funds = line[len('Fund-基金:'):].strip()
                funds = funds.split(';')
                funds = [x.strip() for x in funds if x.strip()]
                model.funds = funds
            elif line.startswith('Year-年:'):
                pubyear = str(line[len('Year-年:'):]).strip()
                model.pubyear = pubyear
            elif line.startswith('CLC-中图分类号:'):
                clc = str(line[len('CLC-中图分类号:'):]).strip()
                clc = clc.split(';')
                clc = [x.strip() for x in clc if x.strip()]
                model.clcs = clc

        return model


class File_cssci_Parser:
    def __init__(self, filepath):
        """
        解析cssci格式
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
        self.lines = []
        if os.path.exists(filepath):
            lines = utils.read_lines(filepath)
            self.lines = lines[3:]
        self.model_list = []

    def parse(self):
        art_lines = self.__build_raw_articles()
        [self.__parse_raw_article(art) for art in art_lines]
        return self.model_list

    def __build_raw_articles(self):
        arts = []
        temp_art = []
        for line in self.lines:
            if line.startswith('【来源篇名】'):
                if temp_art:
                    arts.append(copy.deepcopy(temp_art))
                temp_art = []
            temp_art.append(line)
        return arts

    def __include(self, model):
        ret = [m for m in self.model_list if m.title == model.title and m.firstduty == model.firstduty]
        if ret:
            return ret[0]
        else:
            self.model_list.append(model)
            return model

    def __parse_raw_article(self, lines):
        model = OdsCnkiBib()
        model.id = utils.gen_uuid4()
        model.line = '\t'.join(lines)

        for line in lines:
            if line.startswith('【来源篇名】'):
                title = line[len('【来源篇名】'):].strip()
                model.title = title
            elif line.startswith('【来源作者】'):
                authors = line[len('【来源作者】'):].strip()
                model.authors = authors.split('/')
            elif line.startswith('【基    金】'):
                funds = line[len('【基    金】'):].strip()
                model.funds = funds.split('/')
            elif line.startswith('【期    刊】'):
                publication = line[len('【期    刊】'):].strip()
                model.publication = publication
            elif line.startswith('【机构名称】'):
                orgs = line[len('【机构名称】'):].strip()
                orgs = orgs.split('/')
                orgs = [x.split('.')[0] for x in orgs]  # 去掉院系
                orgs = [x[x.find(']') + 1:] for x in orgs]  # 去掉姓名
                model.orgs = orgs
            elif line.startswith('【第一作者】'):
                firstduty = line[len('【第一作者】'):].strip()
                model.firstduty = firstduty
            elif line.startswith('【中图类号】'):
                clcs = line[len('【中图类号】'):].strip()
                clcs = clcs if clcs.find('***') == -1 else ''  # 三个***表示没有中图类号
                model.clcs = clcs.split('/')
            elif line.startswith('【年代卷期】'):
                pubyear = line[len('【年代卷期】'):].strip()
                model.pubyear = pubyear.split(',')[0]
            elif line.startswith('【关 键 词】'):
                kws = line[len('【关 键 词】'):].strip()
                model.kws = kws.split('/')
        self.model_list.append(model)

        # 下面分析参考文献
        refs = lines[lines.index('【参考文献】') + 1:-1]
        if refs:
            ref_ids = []
            model.refs = ref_ids
            refs = [ref[ref.find('.') + 1:] for ref in refs]
            for ref in refs:
                model_ref = OdsCnkiBib()
                model_ref.id = utils.gen_uuid4()
                model_ref.pid = model.id
                model_ref.ref_style = 'cited'
                model_ref.line = ref

                model_ref.lang = '外文' if utils.strings_is_eng(ref) else '中文'

                ref_sp = ref.split('.')
                if len(ref_sp) == 1:  # 只有一个，设置为title
                    title = ref_sp[0]
                    model_ref.title = title

                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)
                elif len(ref_sp) == 2:  # 第0个是作者，第1个是标题
                    authors = ref_sp[0].split(',')
                    firstduty = authors[0] if len(authors) else ''
                    title = ref_sp[1].split(':')[0]

                    model_ref.authors = authors
                    model_ref.firstduty = firstduty
                    model_ref.title = title
                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)
                elif len(ref_sp) == 3:  # 第0个是作者，第1个是标题，第2个是来源
                    firstduty = ref_sp[0]
                    authors = ref_sp[0].split(',')
                    title = ref_sp[1]
                    s2 = ref_sp[2].split(',')
                    publication = s2[0]
                    pubyear = s2[1] if len(s2) > 1 else ''
                    pubyear = pubyear[:4] if len(pubyear.strip()) >= 4 else ''

                    model_ref.authors = authors
                    model_ref.firstduty = firstduty
                    model_ref.title = title
                    model_ref.publication = publication
                    model_ref.pubyear = pubyear
                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)
                elif len(ref_sp) == 4:  # 第0个是作者，第1个无意义，第2个是标题，第3个是来源
                    firstduty = ref_sp[0]
                    authors = ref_sp[0].split(',')
                    title = ref_sp[2]
                    publication = ref_sp[3]

                    model_ref.authors = authors
                    model_ref.firstduty = firstduty
                    model_ref.title = title
                    model_ref.publication = publication
                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)
                elif len(ref_sp) == 5:  # 第0个是作者，第1个是标题，第2个是来源，第3个是出版年
                    firstduty = ref_sp[0]
                    authors = ref_sp[0].split(',')
                    title = ref_sp[1]
                    publication = ref_sp[2]
                    pubyear = ref_sp[2]

                    model_ref.authors = authors
                    model_ref.firstduty = firstduty
                    model_ref.title = title
                    model_ref.publication = publication
                    model_ref.pubyear = pubyear
                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)
                elif len(ref_sp) == 6:  # 基本是外语引文，
                    firstduty = ref_sp[0]
                    authors = [ref_sp[0]]
                    title = ref_sp[2]
                    publication = ref_sp[3]
                    pubyear = ref_sp[4]

                    model_ref.authors = authors
                    model_ref.firstduty = firstduty
                    model_ref.title = title
                    model_ref.publication = publication
                    model_ref.pubyear = pubyear
                    model_ref = self.__include(model_ref)
                    ref_ids.append(model_ref.id)


import pandas as pd


class File_wos_tab_Parser:
    def __init__(self, filepath):
        """
        解析wos使用tab分割的文本
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
        self.filepath = ''
        if os.path.exists(filepath):
            self.filepath = filepath

    def __parse(self, row):
        model = OdsCnkiBib()
        model.id = utils.gen_uuid4()
        model.line = str(row)

        model.title = self.__isnan(row['TI'])
        model.style = self.__style(row['PT'])
        s_au = self.__isnan(row['AU']).split(';')
        model.firstduty = s_au[0]
        model.authors = s_au

        orgs = self.__isnan(row['SP'])
        orgs = orgs.split(';')
        orgs = [org.strip() for org in orgs]
        model.orgs = orgs

        ##### 关键词，没找到

        summary = self.__isnan(row['AB'])
        model.summary = summary

        ##### 基金，没找到
        model.pubyear = str(self.__isnan(row['PY']))
        model.publication = self.__isnan(row['SO'])

        ##### 国家没找到
        model.country = '国外'
        model.lang = '外文'

        return model

    def parse(self):
        df = pd.read_csv(self.filepath, sep='\t', dtype=str)
        return [self.__parse(row) for index, row in df.iterrows()]

    def __isnan(self, s):
        return '' if s != s else s  # 如果是nan表示空

    def __style(self, s):
        if s == 'J':
            return '期刊'
        elif s == 'B':
            return '书籍'
        elif s == 'S':
            return '丛书'
        elif s == 'P':
            return '专利'
        return ''