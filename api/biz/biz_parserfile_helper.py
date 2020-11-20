from lxml import etree
from scrapy import Selector

import os
from typing import List

from api import util, config
from api.util.strutils import strings_is_eng

from api.model import ods


def parsefiles(format, files):
    """
    根据文件类型，解析文件
    """
    datas = []
    for file in files:
        result = []
        if format == config.ds_gbt_7714_2015:
            result = gbt_7714_2015(file)
        elif format == config.ds_cnki_es5:
            result = cnki_es5(file)
        elif format == config.ds_note_express:
            result = noteExpress(file)
        else:
            raise Exception('不识别的数据类型{}'.format(format))
        datas.extend(result)
    return datas


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

    def __style(v):
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

    def __parse(cnkidata):
        cnkiEs5 = ods.OdsCnkiBib()
        cnkiEs5.id = util.gen_uuid4()
        for child in cnkidata.getchildren():
            tag = child.tag.lower()
            content = str(child.text).strip()
            if tag == 'DataType'.lower():
                cnkiEs5.style = __style(content)
            if tag == 'Title'.lower():
                cnkiEs5.title = content
                if strings_is_eng(cnkiEs5.title):
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
            # if tag == 'Year'.lower():
            #     cnkiEs5.pubyear = int(content)
            # if tag == 'Period'.lower():
            #     cnkiEs5.Period = content
            # if tag == 'Roll'.lower():
            #     cnkiEs5.Roll = content
            # if tag == 'PageCount'.lower():
            #     cnkiEs5.PageCount = content
            # if tag == 'Page'.lower():
            #     cnkiEs5.Page = content
            # if tag == 'Link'.lower():
            #     cnkiEs5.Link = content

        return cnkiEs5

    result = [__parse(cnkidata) for cnkidata in cnkidatas]

    return result


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

    def __style(v):
        v = str(v).strip()
        if v == 'J' or v == 'J/OL':
            return '期刊'
        elif v == 'D':
            return '学位论文'
        elif v == 'N':
            return '报纸'
        elif v == '':
            return ''
        else:
            return '不确定类型' + v

    def __parse(line):
        gbt77142015 = ods.OdsCnkiBib()
        gbt77142015.id = util.gen_uuid4()
        if strings_is_eng(line[:line.find('.http')] if line.find('.http') > 0 else line):  # 如果一行内容带有url，必须去掉url再判断
            # 题名
            title = line[:line.find('[')]
            gbt77142015.title = title
            gbt77142015.lang = '外文'
            # print(title)
            line = line[line.find('[') + 1:]
            # 文献类型
            style = line[line.find('[') + 1:line.find(']')]
            gbt77142015.style = __style(style)
            line = line[line.find(']') + 2:]
            # print(style)
        else:
            # 主要责任者
            creator = line[:line.find('.')]
            authors = [a.strip() for a in creator.split(',') if a.strip()]
            if authors:
                gbt77142015.firstduty = authors[0]
                gbt77142015.authors = authors
            line = line[line.find('.') + 1:]
            # 题名
            title = line[:line.find('[')]
            gbt77142015.title = title
            line = line[line.find('['):]
            # 文献类型
            style = line[line.find('[') + 1:line.find(']')]
            gbt77142015.style = __style(style)
            line = line[line.find(']') + 2:]
            if 'J' == style:  # 期刊
                # 出版物
                publication = line[:line.find(',')]
                gbt77142015.publication = publication
                line = line[line.find(',') + 1:]
                # 出版年
                year = line[:line.find(',')]
                gbt77142015.pubyear = int(year[:4])
                line = line[line.find(',') + 1:]
                # 卷
                roll = line[:line.find('(')]
                # gbt77142015.roll = roll
                line = line[line.find('(') + 1:]
                # （期）
                period = line[:line.find('):')]
                # gbt77142015.period = period
                line = line[line.find('):') + 2:]
                # 页码
                pageno = line[:line.find('.')]
                # gbt77142015.pageno = pageno
                line = line[line.find('.') + 1:]
            elif 'J/OL' == style:  # 网络期刊
                # 出版物
                publication = line[:line.find(':')]
                gbt77142015.publication = publication
                line = line[line.find(':') + 1:]
                # 页码
                pageno = line[:line.find('[')]
                # gbt77142015.pageno = pageno
                line = line[line.find('[') + 1:]
                # 出版日期
                pubtime = line[line.find('[') + 1:line.find(']')]
                gbt77142015.pubtime = pubtime
                gbt77142015.pubyear = int(pubtime[:4])
                line = line[line.find(']') + 2:]
                # 获取方式
                # gbt77142015.url = line
            elif 'D' == style:  # 学位论文
                # 授予单位
                org = line[:line.find(',')]
                orgs = [a.strip() for a in org.split(';') if a.strip()]
                gbt77142015.orgs = orgs
                line = line[line.find(',') + 1:]
                # 授予年
                year = line[:line.find('.')]
                gbt77142015.pubyear = int(year)
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
                # gbt77142015.url = url
        return gbt77142015

    return [__parse(line) for line in lines]


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
            noteExpress = ods.OdsCnkiBib()
            noteExpress.id = util.gen_uuid4()
            result.append(noteExpress)
            noteExpress.referenceType = line[len('{Reference Type}:'):].strip()
        elif line.startswith('{Title}: '):
            noteExpress.title = line[len('{Title}: '):].strip()
            if strings_is_eng(noteExpress.title):
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
