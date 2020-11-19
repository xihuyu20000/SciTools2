class OdsCnkiBib:
    def __init__(self):
        self.fileid = ''
        self.style = ''
        self.title = ''
        self.firstduty = ''
        self.authors = []
        self.orgs = []
        self.kws = []
        self.summary = ''
        self.funds = []
        self.pubyear = 0
        self.pubtime = ''
        self.clcs = []
        self.format = ''
        self.publication = ''
        self.country = '中国'

    def to_dict(self):
        return {'fileid': self.fileid, 'style':self.style, 'title': self.title, 'firstduty': self.firstduty, 'authors': self.authors,
                'orgs': self.orgs, 'kws': self.kws, 'summary': self.summary, 'funds': self.funds, 'pubyear': self.pubyear,
                'pubtime': self.pubtime, 'clcs': self.clcs, 'format':self.format, 'publication': self.publication, 'country':self.country}
