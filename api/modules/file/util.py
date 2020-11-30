import json
import re
import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import xlwt
from bs4 import BeautifulSoup

from api.common.dbhelper import db
from api.common.utils import buildsql

def updateDatafileStatus(msg, fileId):
    # 修改数据文件的状态
    return db.update('UPDATE sci_datafile SET status="{}" WHERE id={}'.format(msg, fileId))


def parseCnki(fileId, dirpath):
    absdir = dirpath+'_dir'
    for file in os.listdir(absdir):
        filepath = os.path.join(absdir, file)
        sqls = []
        with open(filepath, encoding='UTF-8') as file:
            all = file.readlines()
            if False == all[0].strip().startswith('SrcDatabase'):  # 格式校验
                return updateDatafileStatus('CNKI文件格式不正确，请使用官网导出的格式，选择自定义', fileId)

            art = {'FILEID': fileId}
            for i, line in enumerate(all):
                if line and line.strip():  # 过滤掉空行
                    line = line.strip()

                    if line.startswith("Title-题名:"):
                        art['title'] = line.replace("Title-题名:", '').strip()
                    if line.startswith("Author-作者:"):
                        art['author'] = line.replace("Author-作者:", '').strip()
                    if line.startswith("Organ-单位:"):
                        art['organ'] = line.replace("Organ-单位:", "").strip()
                    if line.startswith("Source-文献来源:"):
                        art['source'] = line.replace("Source-文献来源:", '').strip()
                    if line.startswith("Keyword-关键词:"):
                        art['keyword'] = line.replace("Keyword-关键词:", '').strip()
                    if line.startswith("Summary-摘要:"):
                        art['summary'] = line.replace("Summary-摘要:", '').strip()
                    if line.startswith("PubTime-发表时间:"):
                        art['pubtime'] = line.replace("PubTime-发表时间:", '').strip()[:10]
                        # 如果没有年份，就使用出版年
                        if 'year' not in art.keys():
                            art['year'] = art['pubtime'][:4]
                    if line.startswith("FirstDuty-第一责任人:"):
                        art['firstduty'] = line.replace("FirstDuty-第一责任人:", '').strip().replace(";", '')
                    if line.startswith("Year-年:"):
                        year = line.replace("Year-年:", '').strip()
                        art['year'] = year
                    if line.startswith("Fund-基金:"):
                        art['fund'] = line.replace("Fund-基金:", '').strip()
                    if line.startswith("Period-期:"):
                        art['period'] = line.replace("Period-期:", '').strip()
                    if line.startswith("PageCount-页码:"):
                        art['pagecount'] = line.replace("PageCount-页码:", '').strip()
                    if line.startswith("CLC-中图分类号:"):
                        art['clc'] = line.replace("CLC-中图分类号:", '').strip()
                        sql = buildsql('sci_cnki', art)
                        sqls.append(sql)
                        art = {'FILEID': fileId}

        multiThreadingInsert(sqls, fileId)

def parseCnkiFull(userId, fileId, filepath):
    """
    CNKI 全文
    :param userId:
    :param fileId:
    :param filepath:
    :return:
    """
    sqls = []
    arti = {'USERCODE': userId, 'FILEID': fileId}
    with open(filepath, encoding='utf-8') as f:
        bs = BeautifulSoup(''.join(f.readlines()), 'html.parser', from_encoding='utf-8')
        title = bs.select('span.vm')[0].get_text()
        title = str(title).strip()
        arti['title'] = title

        authors = [item.text.strip() for item in bs.select('div.top-title ~ h2')[0].select('a')]
        # print('作者：', authors)
        arti['authors'] = '|||||'.join(authors)

        orgs = [item.text.strip() for item in bs.select('div.top-title ~ h2')[1].select('a')]
        # print('单位：', orgs)
        arti['orgs'] = '|||||'.join(orgs)

        abs = bs.select_one('#a_abstract p').text
        abs = str(abs).replace('摘要', '').replace(' ', '')
        # print('摘要：', abs)
        arti['abs'] = abs

        kws = bs.select_one('#a_keywords p')
        if kws and kws.text:
            kws = kws.text
            kws = kws.split(';')
            kws = [kw.strip() for kw in kws if len(kw.strip())]
            # print('关键词：', kws)
            arti['kws'] = '|||||'.join(kws)
        else:
            arti['kws'] = ''

        tag = bs.find(attrs={'class': 'anchor-tag'})
        content_list = []
        while tag:
            if 'id' in tag.attrs.keys() and tag.attrs['id'] == 'a_bibliography':
                break
            content_list.append(tag)
            tag = tag.find_next_sibling(True)
        arti['content'] = ''.join([tag.text.strip() for tag in content_list])

        content_standard = []
        for index, paragraph in enumerate(content_list):
            text = paragraph.text.strip()
            if paragraph.name == 'h3':
                content_standard.append({'h3': text})
                # print('一级标题：', text)
            if paragraph.name == 'h4':
                content_standard.append({'h4': text})
                # print('下级标题：', text)
            if paragraph.name == 'div':
                content_standard.append({'text': text})
                # print('正文' + str(index) + '\r\n'+text)

        arti['contents'] = json.dumps(content_standard, ensure_ascii=False)

        bibs = bs.select('#a_bibliography a')
        bibs_text = []
        for bib in bibs:
            no = bib.find('b').text.replace('[', '').replace(']', '')
            bib.b.extract()
            bibs_text.append({no:bib.text})
            # print('参考文献' + str(no) + '\r\n', bib.text)
        arti['bibs'] = json.dumps(bibs_text, ensure_ascii=False)

        subindexes = __parse_cnkihtml_subindex(arti['content'])
        arti['bibindex'] =json.dumps(subindexes, ensure_ascii=False)

    sql = buildsql('sci_cnki_full', arti)
    # print(sql)
    sqls.append(sql)

    multiThreadingInsert(sqls, fileId, filepath)

def parseCnkiCite(fileId, dirpath):
    absdir = dirpath+'_dir'
    for file in os.listdir(absdir):
        filepath = os.path.join(absdir, file)
        sqls = []

        with open(filepath, encoding='utf-8') as file:
            all = file.readlines()
            flag = all[0].strip()

            if str(flag).find('、$$题名$$') == -1:  # 格式校验
                return updateDatafileStatus('cnki引文文件格式不正确，请使用网站直接导出的格式', fileId)
            rows = []
            row = []

            ref_flag = 0  # 0表示题名等信息，1表示参考文献，2表示引证文献
            for i, line in enumerate(all):
                if len(line.strip()) == 0:
                    continue
                line = line.strip()
                if line.find('、$$题名$$') > 0:
                    if len(row) > 0:
                        rows.append(row)
                    row = []
                    line = line.split('、$$')[1] #去掉开头的顺序号数字
                    if line.rfind(',')>0:   #去掉末尾的逗号
                        line = line[:-1]
                    for info in line.split(',$$'):  #使用分隔符，这个写法很重要
                        row.append(info)
                    ref_flag = 0  # 重新赋值
                # 参考文献直接使用|||分割
                if line.find('参考文献如下：') == 0:
                    ref_flag = 1
                    row.append('')
                if ref_flag == 1:
                    row.append(row.pop() + "|||" + line)
                # 引证文献直接使用|||分割
                if line.find('引证文献如下：') == 0:
                    ref_flag = 2
                    row.append('')
                if ref_flag == 2:
                    row.append(row.pop() + "|||" + line)
            # 把最后一个元素加入
            rows.append(row)

        for row in rows:
            art = {'fileid': fileId}
            for field in row:
                if field.startswith("题名$$"):
                    art['title'] = field.replace("题名$$", '').strip()
                elif field.startswith("作者$$"):
                    art['author'] = field.replace("作者$$", '').strip()
                elif field.startswith("第一责任人$$"):
                    art['firstduty'] = field.replace("第一责任人$$", '').strip()
                elif field.startswith("单位$$"):
                    art['organ'] = field.replace("单位$$", "").strip()
                elif field.startswith("中文关键词$$"):
                    art['keyword'] = field.replace("中文关键词$$", '').strip()
                elif field.startswith("中文摘要$$"):
                    art['summary'] = field.replace("中文摘要$$", '').strip()
                elif field.startswith("来源$$"):
                    art['source'] = field.replace("来源$$", '').strip()
                elif field.startswith("年卷期$$"):
                    njq = field.replace("年卷期$$", '').strip()
                    njq = njq.split(',')
                    art['year'] = njq[0][:4] if len(njq)>0 else ''
                    art['period'] = njq[2] if len(njq)>2 else ''
                elif field.startswith("页$$"):
                    art['pagecount'] = field.replace("页$$", '').strip()
                elif field.startswith("基金$$"):
                    art['fund'] = field.replace("基金$$", '').strip()
                elif field.startswith("ISSN$$"):
                    art['issn'] = field.replace("ISSN$$", '').strip()
                elif field.startswith("CN$$"):
                    art['cn'] = field.replace("CN$$", '').strip()
                elif field.startswith("语种$$"):
                    art['lang'] = field.replace("语种$$", '').strip()
                elif field.startswith("关键词$"):
                    art['keyword'] = field.replace("关键词$$", '').strip()
                elif field.startswith("分类号$$"):
                    art['clc'] = field.replace("分类号$$", '').strip()
                elif field.startswith("分类号$$"):
                    art['clc'] = field.replace("分类号$$", '').strip()
                elif field.startswith("被引频次$$"):
                    art['citedcount'] = field.replace("被引频次$$", '').strip()
                elif field.startswith("他引频次$$"):
                    art['ocitedcount'] = field.replace("他引频次$$", '').strip()
                elif field.startswith("|||参考文献如下"):
                    art['refdocs'] = field.replace("|||参考文献如下：|||", '').strip()
                elif field.startswith("|||引证文献如下"):
                    art['citingdocs'] = field.replace("|||引证文献如下：|||", '').strip()

                    sql = buildsql('sci_cnki', art)
                    sqls.append(sql)
                else:
                    print('无法识别的字段', field)

        multiThreadingInsert(sqls, fileId, filepath)


def parseWos(fileId, dirpath):
    absdir = dirpath+'_dir'
    for file in os.listdir(absdir):
        filepath = os.path.join(absdir, file)
        sqls = []
        with open(filepath, encoding='utf-8') as file:
            all = file.readlines()
            if '﻿FN Clarivate Analytics Web of Science' != all[0].strip():  # 格式校验
                return updateDatafileStatus('WOS文件格式不正确，请使用网站导出格式，选择纯文本', fileId)
            rows = []
            row = []
            for i, line in enumerate(all):
                if line.startswith("PT "):
                    rows.append(row)
                    row = []
                if line.startswith('   '):
                    row.append(row.pop() + line)
                else:
                    row.append(line)
            # 把最后一个元素加入
            rows.append(row)
            # 第一个是版本信息，删除
            rows = rows[1:]

            for row in rows:
                # 解析一篇论文，保存到art中
                art = {'FILEID': fileId}
                for field in row:
                    if field.startswith('PT'):
                        art['PT'] = field[3:].strip()
                    if field.startswith('AU'):
                        art['AU'] = field[3:].strip().replace('\n   ', ' ')
                    if field.startswith('TI'):
                        art['TI'] = field[3:].strip()
                    if field.startswith('SO'):
                        art['SO'] = field[3:].strip()
                    if field.startswith('VL'):
                        art['VL'] = field[3:].strip()
                    if field.startswith('IS'):
                        art['IIS'] = field[3:].strip()
                    if field.startswith('BP'):
                        art['BP'] = field[3:].strip()
                    if field.startswith('EP'):
                        art['EP'] = field[3:].strip()
                    if field.startswith('DI'):
                        art['DI'] = field[3:].strip()
                    if field.startswith('PD'):
                        art['PD'] = field[3:].strip()
                    if field.startswith('PY'):
                        art['PY'] = field[3:].strip()
                    if field.startswith('FU'):
                        art['FU'] = field[3:].strip().replace('\n  ', '')
                    if field.startswith('AB'):
                        art['AB'] = field[3:].strip().replace('\n  ', '')
                    if field.startswith('C1'):
                        art['C1'] = field[3:].strip().replace('\n  ', '')
                    if field.startswith('RI'):
                        art['RI'] = field[3:].strip()
                    if field.startswith('OI'):
                        art['OI'] = field[3:].strip()
                    if field.startswith('ZB'):
                        art['ZB'] = field[3:].strip()
                    if field.startswith('Z8'):
                        art['Z8'] = field[3:].strip()
                    if field.startswith('ZR'):
                        art['ZR'] = field[3:].strip()
                    if field.startswith('TC'):
                        art['TC'] = field[3:].strip()
                    if field.startswith('ZS'):
                        art['ZS'] = field[3:].strip()
                    if field.startswith('Z9'):
                        art['Z9'] = field[3:].strip()
                    if field.startswith('U1'):
                        art['U1'] = field[3:].strip()
                    if field.startswith('U2'):
                        art['U2'] = field[3:].strip()
                    if field.startswith('SN'):
                        art['SN'] = field[3:].strip()
                    if field.startswith('UT'):
                        art['UT'] = field[3:].strip()
                    if field.startswith('ER'):
                        art['ER'] = field[3:].strip()
                        sql = buildsql('sci_wos', art)
                        sqls.append(sql)
                        art = {'FILEID': fileId}

        for sql in sqls:
            print(sql)
        multiThreadingInsert(sqls, fileId, filepath)


def parseCssci(fileId, dirpath):
    absdir = dirpath+'_dir'
    for file in os.listdir(absdir):
        filepath = os.path.join(absdir, file)
        sqls = []
        with open(filepath, encoding='utf-8') as file:
            all = file.readlines()
            flag = all[0].strip()

            if '南京大学中国社会科学研究评价中心' != flag:  # 格式校验
                return updateDatafileStatus('cssci文件格式不正确，请使用网站直接导出的格式', fileId)
            rows = []
            row = []
            for i, line in enumerate(all[5:]):
                if line.startswith("----------------"):
                    continue
                if line.startswith("【来源篇名】"):
                    rows.append(row)
                    row = []

                if line[0].isdigit():
                    row.append(row.pop() + "|||" + line)
                else:
                    row.append(line)
            # 把最后一个元素加入
            rows.append(row)

            for row in rows:
                # 解析一篇论文，保存到art中
                art = {'FILEID': fileId}
                for field in row:
                    if field.startswith('【来源篇名】'):
                        art['title'] = field[len('【来源篇名】'):].strip()
                    if field.startswith('【英文篇名】'):
                        art['entitle'] = field[len('【英文篇名】'):].strip()
                    if field.startswith('【来源作者】'):
                        art['author'] = field[len('【来源作者】'):].strip()
                    if field.startswith('【基    金】'):
                        art['fund'] = field[len('【基    金】'):].strip()
                    if field.startswith('【期    刊】'):
                        art['journal'] = field[len('【期    刊】'):].strip()
                    if field.startswith('【第一机构】'):
                        art['firstorg'] = field[len('【第一机构】'):].strip()
                    if field.startswith('【机构名称】'):
                        art['org'] = field[len('【机构名称】'):].strip()
                    if field.startswith('【第一作者】'):
                        art['firstduty'] = field[len('【第一作者】'):].strip()
                    if field.startswith('【中图类号】'):
                        art['clc'] = field[len('【中图类号】'):].strip()
                    if field.startswith('【年代卷期】'):
                        art['yearcolumn'] = field[len('【年代卷期】'):].strip()
                    if field.startswith('【关 键 词】'):
                        art['keyword'] = field[len('【关 键 词】'):].strip()
                    if field.startswith('【基金类别】'):
                        art['fundstyle'] = field[len('【基金类别】'):].strip()
                    if field.startswith('【参考文献】'):
                        art['ref'] = field[len('【参考文献】'):].strip()
                        sql = buildsql('sci_cssci', art)
                        sqls.append(sql)
                        art = {'FILEID': fileId}

        for sql in sqls:
            print(sql)
        multiThreadingInsert(sqls, fileId, filepath)


def writeExcel(fileid, wholePath):
    # 关于样式
    style_head = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 初始化字体相关
    font.name = "微软雅黑"
    font.bold = True
    font.colour_index = 1  # TODO 必须是数字索引

    bg = xlwt.Pattern()  # 初始背景图案
    bg.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    bg.pattern_fore_colour = 4  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray

    # 设置字体
    style_head.font = font
    # 设置背景
    style_head.pattern = bg

    # 创建一个excel
    excel = xlwt.Workbook()
    # 添加工作区
    sheet = excel.add_sheet("wos格式1")

    sql = 'SELECT PT,AU,BA,CA,GP,RI,OI,BE,Z2,TI,X1,Y1,Z1,FT,PN,AE,Z3,SO,S1,SE,BS,VL,FU,C1,IIS,SI,MA,BP,EP,AR,DI,D2,EA,SU,PD,PY,AB,X4,Y4,Z4,AK,CT,CY,SP,CL,TC,Z8,ZR,ZB,ZS,Z9,U1,U2,SN,EI,BN,UT,PM,ER FROM sci_wos WHERE FILEID={}'.format(
        fileid)
    print(sql)
    all = db.fetch_all(sql)
    # 标题
    head = all[0].keys()
    for index, value in enumerate(head):
        sheet.write(0, index, value, style_head)

    # 内容信息
    row_index = 0
    for row in all:
        row_index += 1
        column_index = 0
        print(row)
        for key, value in row.items():
            sheet.write(row_index, column_index, value)
            column_index += 1

    # 保存excel
    excel.save(wholePath)


def __parse_cnkihtml_subindex(content):
    '''
    解析内容中的文内引用
    :param content:
    :return:
    '''
    indexdict = defaultdict(list)  # key是参考文献编号，value是引用的位置
    p = re.compile(r"\[([^\[\]]*)\]")
    for m in p.finditer(content):
        pp = re.compile(r'\d+')
        for n in pp.finditer(m.group()):
            start = m.start() + n.start()
            subindex = n.group()
            # print(start, subindex)
            indexdict[subindex].append(start)
    # print(indexdict)
    return indexdict



def multiThreadingInsert(sqls, fileId):
    # 含有10个线程的线程池
    executor = ThreadPoolExecutor(max_workers=10)
    # 启动线程
    all_task = [executor.submit(db.insert_one, (sql)) for sql in sqls]
    # 等待所有的线程结束
    wait(all_task, return_when=ALL_COMPLETED)
    # 更新数据文件的状态
    updateDatafileStatus('解析成功', fileId)



