from lxml import etree
from scrapy import Selector

import os
from typing import List
from utils import strings_is_eng

class CnkiEs5:
    def __init__(self):
        self.DataType = None
        self.Title = None
        self.Author = None
        self.Source = None
        self.Year = None
        self.PubTime = None
        self.Keyword = None
        self.Summary = None
        self.Period = None
        self.Roll = None
        self.PageCount = None
        self.Page = None
        self.Organ = None
        self.Link = None

    def __repr__(self):
        return '<CnkiEs5> Title:{}'.format(self.Title)

def cnki_es5(filepath: str) -> List[dict]:
    """
    解析cnki的es5格式
    :param filepath: 文件路径
    :return: 解析后的数据列表
    """
    assert os.path.exists(filepath), 'es5文件{}必须存在'.format(filepath)
    # 读取内容
    reader = open(filepath, 'r', encoding='UTF-8')
    text = reader.read()
    xml = text[:text.find('</CNKINOTE>') + len('</CNKINOTE>')]
    xml = bytes(bytearray(xml, encoding='utf-8'))
    root = etree.XML(xml)
    if 'CNKINOTE' != root.tag:
        raise Exception('不是es5格式')
    cnkiliters = root.getchildren()[0]
    cnkidatas = [cnkidata for cnkidata in cnkiliters]
    reader.close()

    def __parse(cnkidata):
        cnkiEs5 = CnkiEs5()
        for child in cnkidata.getchildren():
            tag = child.tag.lower()
            content = child.text
            if tag == 'DataType'.lower():
                cnkiEs5.DataType = content
            if tag == 'Title'.lower():
                cnkiEs5.Title = content
            if tag == 'Author'.lower():
                cnkiEs5.Author = content
            if tag == 'Source'.lower():
                cnkiEs5.Source = content
            if tag == 'Year'.lower():
                cnkiEs5.Year = content
            if tag == 'PubTime'.lower():
                cnkiEs5.PubTime = content
            if tag == 'Keyword'.lower():
                cnkiEs5.Keyword = content
            if tag == 'Summary'.lower():
                cnkiEs5.Summary = content
            if tag == 'Period'.lower():
                cnkiEs5.Period = content
            if tag == 'Roll'.lower():
                cnkiEs5.Roll = content
            if tag == 'PageCount'.lower():
                cnkiEs5.PageCount = content
            if tag == 'Page'.lower():
                cnkiEs5.Page = content
            if tag == 'Organ'.lower():
                cnkiEs5.Organ = content
            if tag == 'Link'.lower():
                cnkiEs5.Link = content
        return cnkiEs5

    result = [__parse(cnkidata) for cnkidata in cnkidatas]

    return result


class GBT77142015:
    def __init__(self):
        self.style = None
        self.creator = None
        self.title = None
        self.publication = None
        self.year = None
        self.roll = None
        self.period = None
        self.pageno = None
        self.pubtime = None
        self.url = None
        self.org = None

    def __repr__(self):
        return '<GBT77142015> title:{}'.format(self.title)


def gbt_7714_2015(filepath) -> List[dict]:
    # GBT 7714-2015格式，参考http://manu49.magtech.com.cn/journalx_gdgyzrb/UserFiles/File/GBT7714-2015.pdf
    """
    解析gbt/7714-2015格式
    :param filepath: 文件路径
    :return: 解析后的数据列表
    """
    assert os.path.exists(filepath), 'gbt/7714-2015文件{}必须存在'.format(filepath)
    # 读取内容
    reader = open(filepath, 'r', encoding='UTF-8', errors='strict')
    lines = reader.readlines()
    lines = [line.strip() for line in lines if len(line.strip())]
    for line in lines:
        if line.find(']') == -1:
            raise Exception('必须是[序号]开头')
    lines = [line[line.find(']') + 1:] for line in lines]
    reader.close()

    def __parse(line):
        gbt77142015 = GBT77142015()
        if strings_is_eng(line):
            # 题名
            title = line[:line.find('[')]
            line = line[line.find('[') + 1:]
            # print(title)
            # 文献类型
            style = line[line.find('[') + 1:line.find(']')]
            gbt77142015.style = style
            line = line[line.find(']') + 2:]
            # print(style)
        else:
            # 主要责任者
            creator = line[:line.find('.')]
            gbt77142015.creator = creator
            line = line[line.find('.') + 1:]
            # 题名
            title = line[:line.find('[')]
            gbt77142015.title = title
            line = line[line.find('['):]
            # 文献类型
            style = line[line.find('[') + 1:line.find(']')]
            gbt77142015.style = style
            line = line[line.find(']') + 2:]
            if 'J' == style:  # 期刊
                # 出版物
                publication = line[:line.find(',')]
                gbt77142015.publication = publication
                line = line[line.find(',') + 1:]
                # 出版年
                year = line[:line.find(',')]
                gbt77142015.year = year
                line = line[line.find(',') + 1:]
                # 卷
                roll = line[:line.find('(')]
                gbt77142015.roll = roll
                line = line[line.find('(') + 1:]
                # （期）
                period = line[:line.find('):')]
                gbt77142015.period = period
                line = line[line.find('):') + 2:]
                # 页码
                pageno = line[:line.find('.')]
                gbt77142015.pageno = pageno
                line = line[line.find('.') + 1:]
            elif 'J/OL' == style:  # 网络期刊
                # 出版物
                publication = line[:line.find(':')]
                gbt77142015.publication = publication
                line = line[line.find(':') + 1:]
                # 页码
                pageno = line[:line.find('[')]
                gbt77142015.pageno = pageno
                line = line[line.find('[') + 1:]
                # 出版日期
                pubtime = line[line.find('[') + 1:line.find(']')]
                gbt77142015.pubtime = pubtime
                line = line[line.find(']') + 2:]
                # 获取方式
                gbt77142015.url = line
            elif 'D' == style:  # 学位论文
                # 授予单位
                org = line[:line.find(',')]
                gbt77142015.org = org
                line = line[line.find(',') + 1:]
                # 授予年
                year = line[:line.find('.')]
                gbt77142015.year = year
            elif 'N' == style:  # 报纸文章
                # 授予单位
                publication = line[:line.find(',')]
                gbt77142015.publication = publication
                line = line[line.find(',') + 1:]
                # 发表时间
                pubtime = line[:line.find('(')]
                gbt77142015.pubtime = pubtime
            else:
                raise Exception('解析出现没有识别到的类型 {}\r\n'.format(style))

                # 获取和访问路径
                url = line
                gbt77142015.url = url
        return gbt77142015

    return [__parse(line) for line in lines]

class NoteExpress:
    def __init__(self):
        self.title = None
        self.tertiaryTile = None
        self.author = None
        self.authorAddress = None
        self.secondaryTitle = None
        self.placePublished = None
        self.subsidiaryAuthor = None
        self.year = None
        self.pages = None
        self.keywords = None
        self.abstract = None

    def __repr__(self):
        return '<NoteExpress> title:{}'.format(self.title)

def noteExpress(filepath) -> List[dict]:
    """
        解析NoteExpress格式
        :param filepath: 文件路径
        :return: 解析后的数据列表
        """
    assert os.path.exists(filepath), 'NoteExpress文件{}必须存在'.format(filepath)
    # 读取内容
    reader = open(filepath, 'r', encoding='UTF-8', errors='strict')
    lines = reader.readlines()
    lines = [line.strip() for line in lines if len(line.strip())]
    reader.close()

    result = []
    for line in lines:
        if line.startswith('{Reference Type}:'):
            noteExpress = NoteExpress()
            result.append(noteExpress)
            noteExpress.referenceType = line[len('{Reference Type}:'):].strip()
        elif line.startswith('{Title}: '):
            noteExpress.title = line[len('{Title}: '):].strip()
        elif line.startswith('{Tertiary Title}: '):
            noteExpress.tertiaryTile = line[len('{Tertiary Title}: '):].strip()
        elif line.startswith('{Author}: '):
            noteExpress.author = line[len('{Author}: '):].strip()
        elif line.startswith('{Author Address}: '):
            noteExpress.authorAddress = line[len(
                '{Author Address}: '):].strip()
        elif line.startswith('{Secondary Title}: '):
            noteExpress.secondaryTitle = line[len(
                '{Secondary Title}: '):].strip()
        elif line.startswith('{Place Published}: '):
            noteExpress.placePublished = line[len(
                '{Place Published}: '):].strip()
        elif line.startswith('{Subsidiary Author,}: '):
            noteExpress.subsidiaryAuthor = line[len(
                '{Subsidiary Author,}: '):].strip()
        elif line.startswith('{Year}: '):
            noteExpress.year = line[len('{Year}: '):].strip()
        elif line.startswith('{Pages}: '):
            noteExpress.pages = line[len('{Pages}: '):].strip()
        elif line.startswith('{Keywords}: '):
            noteExpress.keywords = line[len('{Keywords}: '):].strip()
        elif line.startswith('{Abstract}: '):
            noteExpress.abstract = line[len('{Abstract}: '):].strip()

    return result


def cnki_html(filepath) -> List[dict]:
    """
            解析cnki的html格式
            :param filepath: 文件路径
            :return: 解析后的数据列表
            """
    assert os.path.exists(filepath), 'CNKI的html文件{}必须存在'.format(filepath)
    reader = open(filepath, 'r', encoding='utf8')
    content = reader.read()
    reader.close()

    selector = Selector(text=content)
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

