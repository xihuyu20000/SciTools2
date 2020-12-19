import sys
from collections import defaultdict

from api.util.utils import Logger
from api import dao, config
import numpy as np
import pandas as pd

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
    def statArticlesByYear(self, dsid):
        sql = "SELECT pubyear, COUNT(1) AS count FROM {} WHERE dsid ='{}' AND pubyear!='' GROUP BY pubyear ORDER BY pubyear".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 按照国家统计论文数量
    def statArticlesByCountry(self, dsid):
        sql = "SELECT country, COUNT(1) AS count FROM {} WHERE dsid ='{}' AND country!='' GROUP BY country ORDER BY COUNT(1)".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all


    # 按照地区统计论文数量
    def statArticlesByProvince(self, dsid):
        sql = "SELECT province, COUNT(1) AS count FROM {} WHERE dsid ='{}' AND province!='' GROUP BY province ORDER BY COUNT(1) DESC".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 按照机构统计论文数量
    def statArticlesByOrg2(self, dsid):
        sql = "SELECT org, COUNT(1) AS count FROM  (SELECT arrayJoin(orgs2) AS org FROM {} WHERE dsid ='{}') GROUP BY org HAVING COUNT(1)>3 ORDER BY COUNT(1) DESC".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 按照出版物统计论文数量
    def statArticlesByJournal(self, dsid):
        sql = "SELECT publication, COUNT(1) AS count FROM {} WHERE dsid ='{}' AND publication!='' GROUP BY publication HAVING COUNT(1)>3 ORDER BY COUNT(1) DESC".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 按照一作统计论文数量
    def statArticlesByFirstDuty(self, dsid):
        sql = "SELECT firstduty, COUNT(1) AS count FROM {} WHERE dsid ='{}' AND firstduty!='' GROUP BY firstduty HAVING COUNT(1)>3 ORDER BY COUNT(1) DESC".format(
            config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 按照作者统计论文数量
    def statArticlesByAuthor(self, dsid):
        sql = "SELECT author, COUNT(1) AS count FROM  (SELECT arrayJoin(authors) AS author FROM {} WHERE dsid ='{}') GROUP BY author HAVING COUNT(1)>3 ORDER BY COUNT(1) DESC".format(config.tbl_ods_bib,dsid)
        all = self.dao.find_ods_bib(sql)
        return all


    # 基金支持论文历年统计
    def statArticlesByFund(self, dsid):
        sql = "SELECT pubyear , COUNT(1) AS count FROM  {} WHERE LENGTH(funds)>0 AND dsid ='{}' GROUP BY pubyear HAVING COUNT(*)>2 ORDER BY pubyear ".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['pubyear'])
            yList.append(row['count'])
        return xList, yList

    # 基金类型统计
    def statStyleByFund(self, dsid):
        sql = "SELECT fund, COUNT(1) AS count FROM (SELECT arrayJoin(funds) AS fund FROM {} WHERE dsid ='{}' ) GROUP BY fund HAVING COUNT(*)>2 ORDER BY count DESC".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['fund'])
            yList.append(row['count'])
        return xList, yList

    # 学科分布统计
    def statArticlesBySubject(self, dsid):
        xList = []
        yList = []
        for row in []:
            xList.append(row['persons'])
            yList.append(row['count'])
        return xList, yList

    # 合著人数统计 , 针对堆叠条形图生成数据结构
    def statPersonsByCoAuthor(self, dsid):
        sql = "SELECT LENGTH (authors) as persons,  toInt32(pubyear) as pubyear , COUNT(1) AS count FROM {} WHERE dsid ='{}' AND LENGTH(authors)>0 GROUP BY persons,pubyear ORDER BY count ,pubyear".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)

        def __find(pubyear, persons, datas):
            for row in datas:
                if row['pubyear'] == pubyear and row['persons'] == persons:
                    return row['count']
            return 0

        allpubyears = np.array([row['pubyear'] for row in all])
        allpubyears = [n for n in range(allpubyears.min(), allpubyears.max() + 1)]

        allpersons = np.array([row['persons'] for row in all])
        allpersons = [n for n in range(allpersons.min(), allpersons.max() + 1)]

        series = []
        for persons in allpersons: # 合著人数
            count_list = [__find(pubyear, persons, all) for pubyear in allpubyears]    # 发表年份
            series.append({'name': str(persons)+'人', 'type':'bar', 'stack':'总量', 'label':{'show':False, 'position':'insideRight'}, 'data':count_list})

        legend = {'data': [str(persons)+'人' for persons in allpersons]}
        yAxis = {'type':'category', 'data':allpubyears}

        return legend, yAxis, series

    # 关键词词频统计
    def statKwsByCount(self, dsid):
        sql = "SELECT kw, COUNT(1) AS count FROM (SELECT arrayJoin(kws) AS kw FROM {} WHERE dsid ='{}') GROUP BY kw HAVING COUNT(1)>4 ORDER BY count DESC".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql) # 返回结构[ {'count': 1, 'pubyear': '2009', 'persons': 1} .....]
        return all

    # 作者共现矩阵
    def coocmatrix_author(self, dsid):
        sql = "SELECT authors FROM {} WHERE dsid ='{}' AND LENGTH(authors)>0".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 机构共现矩阵
    def coocmatrix_orgs2(self, dsid):
        sql = "SELECT orgs2 FROM {} WHERE dsid ='{}' AND LENGTH(orgs2)>0".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 关键词共现矩阵
    def coocmatrix_keyword(self, dsid):
        sql = "SELECT kws FROM {} WHERE dsid ='{}' AND LENGTH(kws)>0".format(config.tbl_ods_bib, dsid)
        all = self.dao.find_ods_bib(sql)
        return all

    # 主题词词频统计
    def statTwsByCount(self, dsid):
        sql = "SELECT kw, COUNT(1) AS count FROM (SELECT arrayJoin(kws) AS kw FROM {} WHERE dsid ='{}') GROUP BY kw ORDER BY count DESC".format(config.tbl_ods_bib, dsid)
        print(sql)
        all = self.dao.find_ods_bib(sql)
        xList = []
        yList = []
        for row in all:
            xList.append(row['kw'])
            yList.append(row['count'])
        return xList, yList

    def kg(self, userId, dsid, count):
        sql = "SELECT title,author,organ,source,keyword,summary,firstduty,fund,year FROM sci_cnki  WHERE usercode='{}' AND dsid={}  limit {}".format(
            userId, dsid, count)
        print(sql)
        all = self.db.fetch_all(sql)
        id_gen = 0
        return KGraphData(all).build()

statManager = StatManager()