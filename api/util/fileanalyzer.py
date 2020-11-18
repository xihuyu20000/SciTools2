def checkDataIntegrity(file_id) -> bool:
    """
    检查数据完整性
    """
    # todo
    pass

def buildKnowledgeUnit(file_id):
    __buildMetaUnit(file_id)
    __buildCoUnit(file_id)
    __buildCooccurUnit(file_id)
    __buildCouplingUnit(file_id)
    __buildParaCorrelationUnit(file_id)
    __buildCrossCorrelationUnit(file_id)
    __buildRefUnit(file_id)
    __buildWholeTextUnit(file_id)

def __buildMetaUnit(file_id) -> None:
    """
    构建基本知识单元
    """
    # todo 提取出版物、题名、著者、机构、国别、省份、年、月、摘要、关键词、学科分类
    pass

def __buildCoUnit(file_id) ->None:
    """
    构建合作知识单元
    """
    # todo 共现：著者、机构、国家、省份
    pass

def __buildCooccurUnit(file_id)->None:
    """
    构建共现知识单元
    """
    # todo 同现：大学科、小学科、关键词、主题词
    pass

def __buildCouplingUnit(file_id) -> None:
    """
    构建耦合知识单元
    """
    # todo 耦合：文献、著者、机构、国家、省份、出版物
    pass

def __buildParaCorrelationUnit(file_id) -> None:
    """
    构建平行关联知识单元
    """
    # todo
    pass

def __buildCrossCorrelationUnit(file_id) -> None:
    """
    构建交叉关联知识单元
    """
    # todo
    pass
def __buildRefUnit(file_id) -> None:
    """
    构建引文分析单元
    """
    # todo 引文分析：共引、共被引
    pass

def __buildWholeTextUnit(file_id) -> None:
    """
    构建全文分析单元
    """
    # todo 全文分析：
    pass