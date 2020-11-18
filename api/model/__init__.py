'''
api/model所有的模型
'''


class FileModel:
    """
    上传文件模型
    """

    def __init__(self, data_source=None, doc_dir=None) -> None:
        self.__init__()
        self.id = None
        self.data_source = data_source
        self.doc_dir = doc_dir

    def __repr__(self) -> str:
        return '<FileModel> id:{}   data_source:{}   doc_dir:{}'.format(self.id, self.data_source, self.doc_dir)
