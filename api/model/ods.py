class OdsCnkiBib:
    def __init__(self):
        self.fileid = ''
        self.title = ''
        self.firstduty = ''
        self.authors = []
        self.orgs = []
        self.kws = []
        self.summary = ''
        self.funds = []
        self.pubyear = 0
        self.pubmonth = 0
        self.pubtime = ''
        self.clcs = []
        self.publication = ''

    def to_dict(self):
        return {'fileid': self.fileid, 'title': self.title, 'firstduty': self.firstduty, 'authors': self.authors,
                'orgs': self.orgs, 'kws': self.kws, 'summary': self.summary, 'funds': self.funds, 'pubyear': self.pubyear, 'pubmonth': self.pubmonth,
                'pubtime': self.pubtime, 'clcs': self.clcs, 'publication': self.publication}
