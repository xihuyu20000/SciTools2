class OdsCnkiBib:
    def __init__(self):
        self.fileid = ''
        self.id = ''
        self.style = ''
        self.title = ''
        self.title_words = []
        self.firstduty = ''
        self.authors = []
        self.orgs = []
        self.kws = []
        self.summary = ''
        self.summary_words = []
        self.funds = []
        self.pubyear = 0
        self.pubtime = ''
        self.clcs = []
        self.clc1 = ''
        self.clc2 = ''
        self.format = ''
        self.publication = ''
        self.country = '中国'
        self.lang = '中文'

    def to_dict(self):
        return {'fileid': self.fileid, 'id':self.id, 'style':self.style, 'title': self.title, 'title_words':self.title_words,
                'firstduty': self.firstduty, 'authors': self.authors, 'orgs': self.orgs, 'kws': self.kws,
                'summary': self.summary, 'summary_words':self.summary_words, 'funds': self.funds,
                'pubyear': self.pubyear,'pubtime': self.pubtime, 'clcs': self.clcs,'clc1':self.clc1,
                'clc2':self.clc2, 'format':self.format, 'publication': self.publication,'country':self.country, 'lang':self.lang}

    def __repr__(self):
        return str(self.to_dict())