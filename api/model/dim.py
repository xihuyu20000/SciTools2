class DimDict:
    def __init__(self):
        self.fileid = ''
        self.style = ''
        self.values = []
        self.alias = ''

    def to_dict(self):
        return {'fileid': self.fileid, 'style': self.style, 'values': self.values, 'alias': self.alias}

class DimThreshold:
    def __init__(self):
        self.fileid = ''
        self.name = ''
        self.value = ''

    def to_dict(self):
        return {'fileid':self.fileid, 'name':self.name, 'value':self.value}