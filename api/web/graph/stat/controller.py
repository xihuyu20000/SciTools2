from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from .manager import statManager


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None






# 论文历年发文量
@router.get("/statArticlesByYear/{fileId}")
def statArticlesByYear(fileId):
    xList, yList = statManager.statArticlesByYear(fileId)
    return {'config': {'titleText': '论文历年发文量', 'xAxisName': '年', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'series': [{'type': 'line', 'data': yList}]}}

# 论文国别发文量
@router.get("/statArticlesByCountry/{fileId}")
def statArticlesByCountry(fileId):
    xList, yList = statManager.statArticlesByCountry(fileId)
    return {'config': {'titleText': '不同国家论文发文量', 'xAxisName': '国家', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'series': [{'type': 'bar', 'data': yList}]}}

# 论文地区发文量
@router.get("/statArticlesByProvince/{fileId}")
def statArticlesByProvince(fileId):

    return {}

# 论文机构发文量
@router.get("/statArticlesByOrg/{fileId}")
def statArticlesByOrg(fileId):

    return {}

# 一作累计发文量
@router.get("/statArticlesByFirstDuty/{fileId}")
def statArticlesByFirstDuty(fileId):
    xList, yList = statManager.statArticlesByFirstDuty(fileId)
    return {'config': {'titleText': '一作累计发文量', 'xAxisName': '作者', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 作者累计发文量
@router.get("/statArticlesByAuthor/{fileId}")
def statArticlesByAuthor(fileId):
    xList, yList = statManager.statArticlesByAuthor(fileId)
    return {'config': {'titleText': '作者累计发文量', 'xAxisName': '作者', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}

# 期刊来源发文量
@router.get("/statArticlesByJournal/{fileId}")
def statArticlesByJournal(fileId):
    xList, yList = statManager.statArticlesByJournal(fileId)
    return {'config': {'titleText': '期刊来源发文量', 'xAxisName': '出版物', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 基金支持历年统计
@router.get('/statArticlesByFund/{fileId}')
def statArticlesByFund(fileId):
    xList, yList = statManager.statArticlesByFund(fileId)
    return {'config': {'titleText': '基金支持发文量', 'xAxisName': '年份', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}

# 基金类型统计
@router.get('/statStyleByFund/{fileId}')
def statStyleByFund(fileId):
    xList, yList = statManager.statStyleByFund(fileId)
    return {'config': {'titleText': '基金类型', 'xAxisName': '基金', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}

# 学科分布统计
@router.get('/statArticlesBySubject/{fileId}')
def statArticlesBySubject(fileId):
    xList, yList = statManager.statArticlesBySubject(fileId)
    return {'config': {'titleText': '学科分布'},'data': {'xData': [], 'yData': []}}

# 合著人数统计
@router.get('/statPersonsByCoAuthor/{fileId}')
def statPersonsByCoAuthor(fileId):
    xList, yList = statManager.statPersonsByCoAuthor(fileId)
    return {'config': {'titleText': '合著人数', 'xAxisName': '人数', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}


# 关键词词频统计
@router.get('/statKwsByCount/{fileId}')
def statKwsByCount(fileId):
    xList, yList = statManager.statKwsByCount(fileId)
    return {'config': {'titleText': '关键词词频统计', 'xAxisName': '关键词', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}

# 主题词词频统计
@router.get('/statTwsByCount/{fileId}')
def statTwsByCount(fileId):
    xList, yList = statManager.statTwsByCount(fileId)
    return {'config': {'titleText': '主题词词统计', 'xAxisName': '主题词', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}




# 知识图谱
@router.get("/{userId}/{fileId}/{count}")
def kg(userId, fileId, count: int = 10):
    kg = statManager.kg(userId, fileId, count)
    return kg

