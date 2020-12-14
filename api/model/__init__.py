
class OdsCnkiBib:
    def __init__(self):
        self.dsid = ''
        self.id = ''
        self.pid = ''           # 参考文献指向施引文献
        self.style = ''       # 如期刊、回忆录、图书
        self.title = ''          # 标题
        self.title_words = []    # 标题分词
        self.firstduty = ''      # 一作
        self.authors = []        # 作者
        self.orgs = []           # 机构
        self.kws = []            # 关键词
        self.summary = ''        # 摘要
        self.summary_words = []  # 摘要分词
        self.funds = []          # 基金
        self.pubyear = ''        # 出版年
        self.pubtime = ''        # 出版日期
        self.clcs = []           # 主题分类
        self.publication = ''    # 出版物
        self.country = '中国'     # 国家
        self.province = ''       # 地区
        self.lang = '中文'        # 语种：中文/外文
        self.ref_style = 'citing'     # 引用类型，citing/cited
        self.refs = []          # 参考文献集合
        self.line = ''           # 原始记录

    def to_dict(self):
        return {'dsid': self.dsid, 'id':self.id, 'pid':self.pid, 'style':self.style, 'title': self.title, 'title_words':self.title_words,
                'firstduty': self.firstduty, 'authors': self.authors, 'orgs': self.orgs, 'kws': self.kws,
                'summary': self.summary, 'summary_words':self.summary_words, 'funds': self.funds,
                'pubyear': self.pubyear,'pubtime': self.pubtime, 'clcs': self.clcs,'publication': self.publication,'country':self.country, 'province':self.province, 'lang':self.lang, 'ref_style':self.ref_style, 'refs':self.refs, 'line':self.line}

    def __repr__(self):
        return str(self.to_dict())