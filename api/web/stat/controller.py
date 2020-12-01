from fastapi import APIRouter

router = APIRouter()

from .manager import statManager


# 论文历年发文量
@router.get("/statArticlesByYear/{fileId}")
def statArticlesByYear(fileId):
    xList, yList = statManager.statArticlesByYear(fileId)
    return {'config': {'titleText': '论文历年发文量', 'xAxisName': '年', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'series': [{'type': 'line', 'data': yList}]}}


# 著者历年统计
@router.get("/statAuthorsByYear/{fileId}")
def statAuthorsByYear(fileId):
    xList, yList = statManager.statAuthorsByYear(fileId)
    return {'config': {'titleText': '著者历年统计', 'xAxisName': '年', 'yAxisName': '人数'},
            'data': {'xData': xList, 'series': [{'type': 'line', 'data': yList}]}}


# 第一作者累计发文量
@router.get("/statArticlesByFirstDuty/{fileId}")
def statArticlesByFirstDuty(fileId):
    xList, yList = statManager.statArticlesByFirstDuty(fileId)
    return {'config': {'titleText': '第一作者累计发文量', 'xAxisName': '作者', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 第一作者累计发文量(表)
@router.get("/statArticlesByFirstDutyTable")
def statArticlesByFirstDutyTable():
    list = statManager.statArticlesByFirstDutyTable()
    return list


# 历年论文篇均合著人数统计
@router.get("/statCoauthorByYear/{fileId}")
def statCoauthorByYear(fileId):
    xList, yList = statManager.statCoauthorByYear(fileId)
    return {'config': {'titleText': '历年论文篇均合著人数统计', 'xAxisName': '年', 'yAxisName': '平均合著人数'},
            'data': {'xData': xList, 'yData': yList}}


# 论文合著人数统计
@router.get("/statArticlesByCoAuthors/{fileId}")
def statArticlesByCoAuthors(fileId):
    xList, yList = statManager.statArticlesByCoAuthors(fileId)
    return {'config': {'titleText': '论文合著人数统计', 'xAxisName': '合著人数', 'yAxisName': '论文数'},
            'data': {'xData': xList, 'yData': yList}}


# 发文频次统计
@router.get("/statPubFrequencyByAuthor/{fileId}")
def statPubFrequencyByAuthor(fileId):
    xList, yList = statManager.statPubFrequencyByAuthor(fileId)
    return {'config': {'titleText': '发文频次统计', 'xAxisName': '发文数量', 'yAxisName': '第一作者人数'},
            'data': {'xData': xList, 'yData': yList}}


# 历年关键词Top
@router.get("/statTopKeywordsByYear/{fileId}/{count}")
def statTopKeywordsByYear(fileId, count: int = 10):
    years, kws, series = statManager.statTopKeywordsByYear(fileId, count)
    series = [{'name': kw, 'type': 'line', 'data': [v for k, v in seri.items()]} for kw, seri in
              series.items()]
    return {
        'titleText': '历年关键词Top{}'.format(count),
        'xAxisName': '年份',
        'yAxisName': '个数',
        'xAxisData': years,
        'legendData': kws,
        'series': series
    }
