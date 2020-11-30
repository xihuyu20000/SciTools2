import sys
from collections import defaultdict
from api.common.utils import Logger
from api.common.dbhelper import db


class StatManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.db = db

    # 按照年份统计论文数量
    def statArticlesByYear(self, fileId):
        sql = 'SELECT  year, COUNT(*) AS count FROM sci_cnki WHERE year>0 AND fileid={} GROUP BY year ORDER BY year'.format(fileId)
        self.log.info(sql)
        all = self.db.fetch_all(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(int(row['year']))
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


statManager = StatManager()