from api.common.utils import Logger
from api.common.dbhelper import db

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

class KgManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.db = db

    def kg(self, userId, fileId, count):
        sql = "SELECT title,author,organ,source,keyword,summary,firstduty,fund,year FROM sci_cnki  WHERE usercode='{}' AND fileid={}  limit {}".format(
            userId, fileId, count)
        print(sql)
        all = self.db.fetch_all(sql)
        id_gen = 0
        return KGraphData(all).build()

kgManager = KgManager()