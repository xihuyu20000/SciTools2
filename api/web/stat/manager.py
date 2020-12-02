import sys
from collections import defaultdict

from api.util.utils import Logger
from api import dao, config


class KGraphData:
    def __init__(self, all_rows):
        self.id_gen = 0
        self.all_rows = all_rows

        self.nodes = []
        self.links = []
        self.category = {"title": "论文", "author": "作者", "organ": "机构", "source": "期刊", "keyword": "关键词",
                         "firstduty": "第一作者", "fund": "基金", "year": "发表年份"}

    def build(self):
        for row in self.all_rows:
            summary = row['summary']
            title = row['title']
            authorField = row['author']
            organField = row['organ']
            source = row['source']
            keywordField = row['keyword']
            firstduty = row['firstduty']
            fundField = row['fund']
            year = row['year']
            ############标 题###########
            # 节点：标题
            titleNode = self.createNode(title, 0, "title", summary)
            ############作 者###########
            if authorField:
                coAuthorList = []
                for author in str(authorField).split(";"):
                    if author and str(author).strip() != '':
                        # 节点：作者
                        authorNode = self.createNode(author, 0, "author", '作者：' + author)
                        coAuthorList.append(authorNode)
                        # 连线：论文——作者
                        self.createLink('作者', authorNode['id'], titleNode['id'])
                for author1 in coAuthorList:
                    for author2 in coAuthorList:
                        if author1['label'] != author2['label']:
                            # 连线： 共现作者
                            self.createLink('共现作者', author1['id'], author2['id'])
            ############机 构###########
            if organField:
                coOrganList = []
                for organ in organField.split(';'):
                    if organ and str(organ).strip() != '':
                        # 节点：机构
                        organNode = self.createNode(organ, 0, "organ", '机构：' + organ)
                        coOrganList.append(organNode)
                        # 连线：机构——>论文
                        self.createLink("发文机构", organNode['id'], titleNode['id'])
                for organ1 in coOrganList:
                    for organ2 in coOrganList:
                        if organ1['label'] != organ2['label']:
                            # 连线： 共现机构
                            self.createLink('共现机构', organ1['id'], organ2['id'])

            ############标 题###########
            # 节点：发文期刊
            sourceNode = self.createNode(source, 0, 'source', '期刊：' + source)
            # 连线：发文期刊——>论文
            self.createLink('发文期刊', sourceNode['id'], titleNode['id'])

            ###########关 键 词###########
            if keywordField:
                coKeywordList = []
                for keyword in keywordField.split(';'):
                    if keyword and str(keyword).strip() != '':
                        # 节点：关键词
                        keywordNode = self.createNode(keyword, 0, 'keyword', '关键词：' + keyword)
                        coKeywordList.append(keywordNode)
                        # 连线：关键词——>论文
                        self.createLink('关键词', titleNode['id'], keywordNode['id'])
                for keyword1 in coKeywordList:
                    for keyword2 in coKeywordList:
                        if keyword1['label'] != keyword2['label']:
                            # 连线：共现关键词
                            self.createLink('共现关键词', keyword1['id'], keyword2['id'])

            ###########第 一 作 者###########
            if firstduty:
                firstduty = str(firstduty).replace(";", "")
                # 节点：第一作者
                firstdutyNode = self.createNode(firstduty, 0, 'firstduty', '第一作者：' + firstduty)
                # 连线：第一作者——>论文
                self.createLink('第一作者', firstdutyNode['id'], titleNode['id'])

            ###########基  金###########
            if fundField:
                cofundList = []
                for fund in fundField.split(';'):
                    # 节点：基金
                    fundNode = self.createNode(fund, 0, 'fund', '基金：' + fund)
                    cofundList.append(fundNode)
                    # 连线：基金——>论文
                    self.createLink('基金支持', fundNode['id'], titleNode['id'])
                    # 连线：基金——>第一作者
                    self.createLink('作者基金', fundNode['id'], firstdutyNode['id'])
                for fund1 in cofundList:
                    for fund2 in cofundList:
                        if fund1['label'] != fund2['label']:
                            # 连线：共现基金
                            self.createLink('共现基金', fund1['id'], fund2['id'])

            ###########年###########
            if year and str(year).strip() != '':
                yearNode = self.createNode(str(year) + '年', 0, 'year', '发表年：' + str(year))
                self.createLink('发表年', yearNode['id'], titleNode['id'])

        return {'categories': self.category, 'data': {'nodes': self.nodes, 'edges': self.links}}

    def createNode(self, label, value, category, info):
        for node in self.nodes:
            if label == node['label']:
                return node
        self.id_gen += 1
        node = {"id": self.id_gen, "label": label, "value": value, "categories": [category], "info": info}
        self.nodes.append(node)
        return node

    def createLink(self, label, source, target):
        for link in self.links:
            if (link['label'] == label and link['from'] == source and link['to'] == target):
                return link
        self.id_gen += 1
        link = {"id": self.id_gen, "label": label, "from": source, "to": target}
        self.links.append(link)
        return link

class StatManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao


    # 按照年份统计论文数量
    def statArticlesByYear(self, fileId):
        sql = "SELECT pubyear, COUNT(1) AS count FROM {} WHERE fileid ='{}' GROUP BY pubyear ORDER BY pubyear".format(config.tbl_ods_bib,fileId)
        self.log.info(sql)
        all = self.dao.find_ods_bib(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(int(row['pubyear']))
            yList.append(int(row['count']))

        minYear, maxYear = min(xList), max(xList)
        xList2, yList2 = [], []

        for year in range(minYear, maxYear + 1):  # 所有年份
            xList2.append(year)
            if year in xList:
                yList2.append(yList[xList.index(year)])
            else:
                yList2.append(0)  # 没有记录的年份，补0

        return xList2, yList2

    # 按照国家统计论文数量
    def statArticlesByCountry(self, fileId):
        sql = "SELECT country, COUNT(1) AS count FROM {} WHERE fileid ='{}' GROUP BY country  ORDER BY count  ".format(
            config.tbl_ods_bib, fileId)
        self.log.info(sql)
        all = self.dao.find_ods_bib(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['country'])
            yList.append(int(row['count']))

        return xList, yList

    # 按照年份统计作者人数
    def statAuthorsByYear(self, fileId):
        sql = 'SELECT  year, COUNT(distinct firstduty) AS count FROM sci_cnki WHERE year>0 AND fileid={} GROUP BY YEAR ORDER BY year'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['year'])
            yList.append(row['count'])
        return xList, yList

    # 按照年份统计关键词
    def statTopKeywordsByYear(self, fileId, count):
        sql = 'SELECT year,keyword FROM sci_cnki WHERE year>0 AND fileid={} order by year'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)

        kw_dict = defaultdict(int)
        min_year = sys.maxsize
        max_year = 0 - sys.maxsize

        for row in all:
            year = int(row['year'])
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year
            kw_arr = row['keyword'].split(';')
            for kw in kw_arr:
                if str(kw).strip() != '':
                    kw_dict[kw] += 1
        kw_dict = sorted(kw_dict.items(), key=lambda x: x[1], reverse=True)
        '''
        [('数字人文', 309), ('图书馆', 37), ('高校图书馆', 27), ('数字学术', 22), ('人文计算', 21), ('可视化', 15), ('大数据', 13), ('美国', 13), ('数字图书馆', 12), ('关联数据', 12)]
        '''

        topkws = [item[0] for item in kw_dict[:count]]
        years = [x for x in range(min_year, max_year + 1)]

        topkw_dict = dict()
        for kw in topkws:
            topkw_dict[kw] = defaultdict(int)
            for year in years:
                topkw_dict[kw][year] = 0

        for row in all:
            year = row['year']
            kw_arr = row['keyword'].split(';')
            for kw in kw_arr:
                if str(kw).strip() != '' and kw in topkws:
                    topkw_dict[kw][year] += 1
        return years, topkws, topkw_dict

    # 按照第一作者统计论文数量
    def statArticlesByFirstDuty(self, fileId):
        sql = 'SELECT firstduty, COUNT(*) AS count FROM sci_cnki WHERE fileid={} GROUP BY FIRSTDUTY ORDER BY COUNT DESC'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['firstduty'])
            yList.append(row['count'])
        return xList, yList

    def statArticlesByCoAuthors(self, fileId):
        sql = 'SELECT author FROM sci_cnki WHERE fileid={}'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        dd = defaultdict(int)
        for row in all:
            author = row['author']
            if author and author.strip():
                dd[author.count(';')] += 1
        if 0 in dd.keys():
            del dd[0]
        dd = sorted(dd.items(), key=lambda x: x[0])
        xList = [str(item[0]) + '人合著' for item in dd]
        xList[0] = '独著'
        yList = [item[1] for item in dd]
        return xList, yList

    def statArticlesByFirstDutyTable(self):
        sql = 'SELECT firstduty, COUNT(*) AS count FROM sci_cnki GROUP BY FIRSTDUTY ORDER BY COUNT DESC'
        print(sql)
        all = self.db.fetch_all(sql)
        dd = defaultdict(int)
        for row in all:
            dd[row['firstduty']] += row['count']

        ll = [{'author': k.replace(';', ''), 'count': v} for k, v in dd.items() if k]
        return ll

    def statPubFrequencyByAuthor(self, fileId):
        sql = 'SELECT firstduty, COUNT(*) AS count FROM sci_cnki WHERE fileid={} GROUP BY FIRSTDUTY ORDER BY COUNT DESC'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        dd = defaultdict(int)
        for row in all:
            dd[row['firstduty']] += row['count']

        ll = defaultdict(int)
        for k, v in dd.items():
            ll[v] += 1
        return list(ll.keys()), list(ll.values())

    def statCoauthorByYear(self, fileId):
        sql = 'SELECT year, author FROM sci_cnki WHERE year>0 AND fileid={}'.format(fileId)
        print(sql)
        all = self.db.fetch_all(sql)
        year_arts_dict = defaultdict(int)
        year_authors_dict = defaultdict(int)
        for row in all:
            year = row['year']
            year_arts_dict[year] += 1
            if row['author']:
                year_authors_dict[year] += len(row['author'].split(';'))

        xList = list(year_arts_dict.keys())
        yList = []
        for year in xList:
            yList.append('%.2f' % (year_authors_dict[year] / year_arts_dict[year]))

        return xList, yList


    def kg(self, userId, fileId, count):
        sql = "SELECT title,author,organ,source,keyword,summary,firstduty,fund,year FROM sci_cnki  WHERE usercode='{}' AND fileid={}  limit {}".format(
            userId, fileId, count)
        print(sql)
        all = self.db.fetch_all(sql)
        id_gen = 0
        return KGraphData(all).build()

statManager = StatManager()