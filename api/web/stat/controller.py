from fastapi import APIRouter
from pydantic import BaseModel

from api.util.coocmatrix import CoocMatrix

router = APIRouter()

from api.web.stat.manager import statManager

######### plotly图库  https://dash-gallery.plotly.host/Portal/

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# node的属性又color、label、id、size
# edge的属性又sourceID、targetID、size
cluster_spectral_dataset = {
    "nodes": [{"label": "a", "id": "a", "size": 4, "color": "#4f19c7"},
              {"label": "b", "id": "b", "size": 5, "color": "#4f19c7"},
              {"label": "c", "id": "c", "size": 5, "color": "#4f19c7"},
              ],
    "edges": [{"sourceID": "a", "targetID": "b", "size": 1},
              {"sourceID": "a", "targetID": "c", "size": 3},
              {"sourceID": "b", "targetID": "c", "size": 3},
              ]
}

forcetrend_data = {
    "nodes": [
        {
            "id": "0",
            "name": "Myriel",
            "symbolSize": 19.12381,
            "x": 1,
            "y": 1,
            "value": 28.685715,
            "category": 0
        },
        {
            "id": "1",
            "name": "Napoleon",
            "symbolSize": 2.6666666666666665,
            "x": 2,
            "y": 2,
            "value": 4,
            "category": 0
        },
        {
            "id": "2",
            "name": "MlleBaptistine",
            "symbolSize": 6.323809333333333,
            "x": 2,
            "y": 3,
            "value": 9.485714,
            "category": 1
        },
        {
            "id": "3",
            "name": "MmeMagloire",
            "symbolSize": 6.323809333333333,
            "x": 3,
            "y": 6,
            "value": 9.485714,
            "category": 1
        }
    ],
    "edges": [
        {
            "source": "0",
            "target": "1"
        },
        {
            "source": "0",
            "target": "2"
        },
        {
            "source": "0",
            "target": "3"
        },
        {
            "source": "1",
            "target": "2"
        },
        {
            "source": "1",
            "target": "3"
        }
    ],
    "categories": [
        {
            "name": "类目0"
        },
        {
            "name": "类目1"
        }
    ]
}


# echarts折线图/柱状图的配置
def __line_graph_option(titleText='', xAxisName='', axisLabelRotate=0, yAxisName='', source=[], series=[]):
    return {'option':
                {'title': {'show': True, 'text': titleText, 'textStyle': {'color': 'black', 'fontSize': 20}},
                 'legend': {'show': True},
                 'grid': {'show': True, 'top': 60, 'bottom': 60, 'right': 80, 'left': 80, 'height': 'auto', 'width': 'auto'},
                 'xAxis': {'show': True, 'position': 'bottom', 'type': 'category', 'name': xAxisName, 'nameLocation': 'end', 'nameGap': 15,
                           'nameRotate': 0, 'inverse': False,
                           'nameTextStyle': {'fontSize': 12},
                           'axisLabel': {'rotate': axisLabelRotate, 'fontSize': 12, 'fontFamily': 'sans-serif', 'marginTop': '35px', 'show': True, 'interval': 0}
                           },
                 'yAxis': {'show': True, 'position': 'left', 'type': 'value', 'name': yAxisName, 'nameLocation': 'end',
                           'nameTextStyle': {'fontStyle': 'normal'}
                           },
                 'toolbox': {'show': True, 'orient': 'horizontal', 'showTitle': True,
                             'feature': {
                                 'dataView': {'show': True}, 'restore': {'show': True}, 'dataZoom': {'show': True}, 'saveAsImage': {'show': True}
                             }
                             },
                 'tooltip': {'show': False, 'trigger': 'item', 'formatter': '{a} {b} {c}'},
                 'dataset': {'source': source},
                 'series': series
                 }}

# 关键词共现关系图
@router.get('/circularGraph/keyword/{dsid}')
def statArticlesByYear(dsid):
    source = statManager.coocmatrix_keyword(dsid)
    source = [row['kws'] for row in source]  # 从dict中取kws数组
    option = __build_circular_graph(source)
    return option

def __build_circular_graph(source, titleText = ''):
    '''
data数组中元素的结构如下
{
    attributes: { modularity_class: 0 },
    category: 0,
    id: "0",
    itemStyle: null,
    label: { normal: { show: true }},
    name: "Myriel",
    symbolSize: 19.12381,
    value: 28.685715,
    x: -266.82776,
    y: 299.6904
}

link数组中元素的结构如下
{
    id: "0",
    lineStyle:{ normal: {} },
    name: null,
    source: "1",
    target: "0"
}
categories数组中元素的结构如下
{
    id: "0",
    lineStyle: { normal: {} },
    name: null,
    source: "1",
    target: "0"
}
    '''
    nodes = []
    links = []
    categories = []
    legend = [] # 名称列表



    option = {
        'title': {
            'text': titleText,
            'top': 'bottom',
            'left': 'right'
        },
        'tooltip': {},
        'legend': legend,
        'animationDurationUpdate': 1500,
        'animationEasingUpdate': 'quinticInOut',
        'series': [
            {
                'name': 'Les Miserables',
                'type': 'graph',
                'layout': 'circular',
                'circular': {
                    'rotateLabel': True
                },
                'data': nodes,
                'links': links,
                'categories': categories,
                'roam': True,
                'label': {
                    'position': 'right',
                    'formatter': '{b}'
                },
                'lineStyle': {
                    'color': 'source',
                    'curveness': 0.3
                }
            }
        ]
        }
    return option

# 论文历年发文量
@router.get("/statArticlesByYear/{dsid}")
def statArticlesByYear(dsid):
    source = statManager.statArticlesByYear(dsid)
    series = [{'type': 'line', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 12, 'color': '#333'}}}}]
    return __line_graph_option(titleText='论文历年发文量', xAxisName='年', yAxisName='发文量(篇)', source=source, series=series)


# 论文国别发文量
@router.get("/statArticlesByCountry/{dsid}")
def statArticlesByCountry(dsid):
    source = statManager.statArticlesByCountry(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 12, 'color': '#333'}}}}]
    return __line_graph_option(titleText='论文国家发文量', xAxisName='国家', yAxisName='发文量(篇)', source=source, series=series)


# 论文地区发文量
@router.get("/statArticlesByProvince/{dsid}")
def statArticlesByProvince(dsid):
    source = statManager.statArticlesByProvince(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 12, 'color': '#333'}}}}]
    return __line_graph_option(titleText='论文地区发文量', xAxisName='省', axisLabelRotate=-30, yAxisName='发文量(篇)', source=source, series=series)


# 论文机构发文量
@router.get("/statArticlesByOrg/{dsid}")
def statArticlesByOrg(dsid):
    source = statManager.statArticlesByOrg2(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 12, 'color': '#333'}}}}]
    return __line_graph_option(titleText='机构发文量', xAxisName='机构', axisLabelRotate=-40, yAxisName='发文量(篇)', source=source, series=series)


# 期刊发文量
@router.get("/statArticlesByJournal/{dsid}")
def statArticlesByJournal(dsid):
    source = statManager.statArticlesByJournal(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 12, 'color': '#333'}}}}]
    return __line_graph_option(titleText='期刊发文量', xAxisName='期刊', axisLabelRotate=-50, yAxisName='发文量(篇)', source=source, series=series)


# 一作累计发文量
@router.get("/statArticlesByFirstDuty/{dsid}")
def statArticlesByFirstDuty(dsid):
    source = statManager.statArticlesByFirstDuty(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 18, 'color': '#333'}}}}]
    return __line_graph_option(titleText='一作发文量', xAxisName='作者', yAxisName='发文量(篇)', source=source, series=series)


# 作者累计发文量
@router.get("/statArticlesByAuthor/{dsid}")
def statArticlesByAuthor(dsid):
    source = statManager.statArticlesByAuthor(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 18, 'color': '#333'}}}}]
    return __line_graph_option(titleText='一作发文量', xAxisName='作者', yAxisName='发文量(篇)', source=source, series=series)


# 基金支持历年统计
@router.get('/statArticlesByFund/{dsid}')
def statArticlesByFund(dsid):
    xList, yList = statManager.statArticlesByFund(dsid)
    return {'config': {'titleText': '基金支持发文量', 'xAxisName': '年份', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 基金类型统计
@router.get('/statStyleByFund/{dsid}')
def statStyleByFund(dsid):
    xList, yList = statManager.statStyleByFund(dsid)
    return {'config': {'titleText': '基金类型', 'xAxisName': '基金', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}


# 学科分布统计
@router.get('/statArticlesBySubject/{dsid}')
def statArticlesBySubject(dsid):
    xList, yList = statManager.statArticlesBySubject(dsid)
    return {'config': {'titleText': '学科分布'}, 'data': {'xData': [], 'yData': []}}


# 合著人数统计，堆叠条形图
@router.get('/statPersonsByCoAuthor/{dsid}')
def statPersonsByCoAuthor(dsid):
    legend, yAxis, series = statManager.statPersonsByCoAuthor(dsid)

    option = {
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': { # 坐标轴指示器，坐标轴触发有效
                'type': 'shadow' # 默认为直线，可选为：'line' | 'shadow'
            }
        },
        'legend': legend,
        'grid': {
            'left': '3%',
            'right': '4%',
            'bottom': '3%',
            'containLabel': True
        },
        'xAxis': {
            'type': 'value'
        },
    'yAxis': yAxis,
    'series': series
    };

    return {'option': option}


# 关键词词频统计
@router.get('/statKwsByCount/{dsid}')
def statKwsByCount(dsid):
    source = statManager.statKwsByCount(dsid)
    series = [{'type': 'bar', 'itemStyle': {'normal': {'label': {'show': True, 'fontSize': 18, 'color': '#333'}}}}]
    return __line_graph_option(titleText='关键词词频统计', xAxisName='关键词',axisLabelRotate=-50,  yAxisName='数量', source=source, series=series)


# 关键词词云
@router.get("/wordcloud/keyword/{dsid}")
def wordcloud_keyword(dsid):
    return {}

# 作者共现矩阵
@router.get("/coocMatrix/author/{dsid}")
def coocmatrix_author(dsid):
    source = statManager.coocmatrix_author(dsid)
    source = [row['authors'] for row in source] # 从dict中取kws数组
    xData, yData, points = __build_comatrix(source, cut_method = 1, cut_value=10, norm_method = 1)
    print(points)
    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}


# 国家共现矩阵
@router.get("/coocMatrix/country/{dsid}")
def coocmatrix_country(dsid):
    return {}


# 基金共现矩阵
@router.get("/coocMatrix/fund/{dsid}")
def coocmatrix_fund(dsid):
    return {}


# 机构共现矩阵
@router.get("/coocMatrix/org/{dsid}")
def coocmatrix_org(dsid):
    source = statManager.coocmatrix_orgs2(dsid)
    source = [row['orgs2'] for row in source]  # 从dict中取kws数组
    xData, yData, points = __build_comatrix(source, cut_method = 1, cut_value=10, norm_method = 1)
    print(points)
    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}


# 关键词共现矩阵
@router.get("/coocMatrix/keyword/{dsid}")
def coocmatrix_keyword(dsid):
    source = statManager.coocmatrix_keyword(dsid)
    source = [row['kws'] for row in source] # 从dict中取kws数组
    xData, yData, points = __build_comatrix(source, cut_method = 1, cut_value=10, norm_method = 1)
    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}

def __build_comatrix(source, cut_method, cut_value, norm_method):
    matrix = CoocMatrix(source, cut_method = cut_method, cut_value=cut_value, norm_method = norm_method)
    matrix_data = matrix.run()
    xData = list(matrix_data.columns)   #Series转list类型
    yData = list(matrix_data.index)
    values = matrix_data.values     #DataFrame转list类型
    points = []
    for i, row_arr in enumerate(values):
        for j, v in enumerate(row_arr):
            points.append([i, j, v if v else '-'])
    return xData, yData, points

cooc_matrix_data = [
    ['', '文献计量', '知识图谱', '文献计量分析', '研究热点', 'CiteSpace', '可视化分析', '可视化', '文献计量法', 'Citespace', '发展态势', 'VOSviewer'],
    ['文献计量', '0', '21', '0', '12', '15', '10', '10', '0', '3', '5', '2'],
    ['知识图谱', '21', '0', '5', '7', '9', '7', '3', '2', '1', '0', '2'],
    ['文献计量分析', '0', '5', '0', '7', '2', '3', '1', '0', '1', '0', '1'],
    ['研究热点', '12', '7', '7', '0', '1', '5', '1', '2', '3', '0', '0'],
    ['CiteSpace', '15', '9', '2', '1', '0', '4', '4', '0', '0', '1', '2'],
    ['可视化分析', '10', '7', '3', '5', '4', '0', '0', '2', '0', '0', '3'],
    ['可视化', '10', '3', '1', '1', '4', '0', '0', '1', '0', '0', '0'],
    ['文献计量法', '0', '2', '0', '2', '0', '2', '1', '0', '1', '0', '0'],
    ['Citespace', '3', '1', '1', '3', '0', '0', '0', '1', '0', '0', '0'],
    ['发展态势', '5', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
    ['VOSviewer', '2', '2', '1', '0', '2', '3', '0', '0', '0', '0', '0']
]


# 共现关键词散点图
@router.get("/scatter/coockeyword/{dsid}")
def scatter_coockeyword(dsid):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])
    print('散点图', points)

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}


# 关键词突现图谱
@router.get("/cluster/bursting/keyword/{dsid}")
def cluster_bursting_keyword(dsid):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': hierarchy_data}}


hierarchy_data = {
    "name": "flare",
    "children": [
        {
            "name": "analytics",
            "children": [
                {
                    "name": "cluster",
                    "children": [
                        {"name": "AgglomerativeCluster", "value": 3938},
                        {"name": "CommunityStructure", "value": 3812},
                        {"name": "HierarchicalCluster", "value": 6714},
                        {"name": "MergeEdge", "value": 743}
                    ]
                },
                {
                    "name": "graph",
                    "children": [
                        {"name": "BetweennessCentrality", "value": 3534},
                        {"name": "LinkDistance", "value": 5731},
                        {"name": "MaxFlowMinCut", "value": 7840},
                        {"name": "ShortestPaths", "value": 5914},
                        {"name": "SpanningTree", "value": 3416}
                    ]
                },
                {
                    "name": "optimization",
                    "children": [
                        {"name": "AspectRatioBanker", "value": 7074}
                    ]
                }
            ]
        },
        {
            "name": "animate",
            "children": [
                {"name": "Easing", "value": 17010},
                {"name": "FunctionSequence", "value": 5842},
                {
                    "name": "interpolate",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                        {"name": "ColorInterpolator", "value": 2047},
                        {"name": "DateInterpolator", "value": 1375},
                        {"name": "Interpolator", "value": 8746},
                        {"name": "MatrixInterpolator", "value": 2202},
                        {"name": "NumberInterpolator", "value": 1382},
                        {"name": "ObjectInterpolator", "value": 1629},
                        {"name": "PointInterpolator", "value": 1675},
                        {"name": "RectangleInterpolator", "value": 2042}
                    ]
                },
                {"name": "ISchedulable", "value": 1041},
                {"name": "Parallel", "value": 5176},
                {"name": "Pause", "value": 449},
                {"name": "Scheduler", "value": 5593},
                {"name": "Sequence", "value": 5534},
                {"name": "Transition", "value": 9201},
                {"name": "Transitioner", "value": 19975},
                {"name": "TransitionEvent", "value": 1116},
                {"name": "Tween", "value": 6006}
            ]
        },
        {
            "name": "data",
            "children": [
                {
                    "name": "converters",
                    "children": [
                        {"name": "Converters", "value": 721},
                        {"name": "DelimitedTextConverter", "value": 4294},
                        {"name": "GraphMLConverter", "value": 9800},
                        {"name": "IDataConverter", "value": 1314},
                        {"name": "JSONConverter", "value": 2220}
                    ]
                },
                {"name": "DataField", "value": 1759},
                {"name": "DataSchema", "value": 2165},
                {"name": "DataSet", "value": 586},
                {"name": "DataSource", "value": 3331},
                {"name": "DataTable", "value": 772},
                {"name": "DataUtil", "value": 3322}
            ]
        },
        {
            "name": "display",
            "children": [
                {"name": "DirtySprite", "value": 8833},
                {"name": "LineSprite", "value": 1732},
                {"name": "RectSprite", "value": 3623},
                {"name": "TextSprite", "value": 10066}
            ]
        },
        {
            "name": "flex",
            "children": [
                {"name": "FlareVis", "value": 4116}
            ]
        },
        {
            "name": "physics",
            "children": [
                {"name": "DragForce", "value": 1082},
                {"name": "GravityForce", "value": 1336},
                {"name": "IForce", "value": 319},
                {"name": "NBodyForce", "value": 10498},
                {"name": "Particle", "value": 2822},
                {"name": "Simulation", "value": 9983},
                {"name": "Spring", "value": 2213},
                {"name": "SpringForce", "value": 1681}
            ]
        },
        {
            "name": "query",
            "children": [
                {"name": "AggregateExpression", "value": 1616},
                {"name": "And", "value": 1027},
                {"name": "Arithmetic", "value": 3891},
                {"name": "Average", "value": 891},
                {"name": "BinaryExpression", "value": 2893},
                {"name": "Comparison", "value": 5103},
                {"name": "CompositeExpression", "value": 3677},
                {"name": "Count", "value": 781},
                {"name": "DateUtil", "value": 4141},
                {"name": "Distinct", "value": 933},
                {"name": "Expression", "value": 5130},
                {"name": "ExpressionIterator", "value": 3617},
                {"name": "Fn", "value": 3240},
                {"name": "If", "value": 2732},
                {"name": "IsA", "value": 2039},
                {"name": "Literal", "value": 1214},
                {"name": "Match", "value": 3748},
                {"name": "Maximum", "value": 843},
                {
                    "name": "methods",
                    "children": [
                        {"name": "add", "value": 593},
                        {"name": "and", "value": 330},
                        {"name": "average", "value": 287},
                        {"name": "count", "value": 277},
                        {"name": "distinct", "value": 292},
                        {"name": "div", "value": 595},
                        {"name": "eq", "value": 594},
                        {"name": "fn", "value": 460},
                        {"name": "gt", "value": 603},
                        {"name": "gte", "value": 625},
                        {"name": "iff", "value": 748},
                        {"name": "isa", "value": 461},
                        {"name": "lt", "value": 597},
                        {"name": "lte", "value": 619},
                        {"name": "max", "value": 283},
                        {"name": "min", "value": 283},
                        {"name": "mod", "value": 591},
                        {"name": "mul", "value": 603},
                        {"name": "neq", "value": 599},
                        {"name": "not", "value": 386},
                        {"name": "or", "value": 323},
                        {"name": "orderby", "value": 307},
                        {"name": "range", "value": 772},
                        {"name": "select", "value": 296},
                        {"name": "stddev", "value": 363},
                        {"name": "sub", "value": 600},
                        {"name": "sum", "value": 280},
                        {"name": "update", "value": 307},
                        {"name": "variance", "value": 335},
                        {"name": "where", "value": 299},
                        {"name": "xor", "value": 354},
                        {"name": "-", "value": 264}
                    ]
                },
                {"name": "Minimum", "value": 843},
                {"name": "Not", "value": 1554},
                {"name": "Or", "value": 970},
                {"name": "Query", "value": 13896},
                {"name": "Range", "value": 1594},
                {"name": "StringUtil", "value": 4130},
                {"name": "Sum", "value": 791},
                {"name": "Variable", "value": 1124},
                {"name": "Variance", "value": 1876},
                {"name": "Xor", "value": 1101}
            ]
        },
        {
            "name": "scale",
            "children": [
                {"name": "IScaleMap", "value": 2105},
                {"name": "LinearScale", "value": 1316},
                {"name": "LogScale", "value": 3151},
                {"name": "OrdinalScale", "value": 3770},
                {"name": "QuantileScale", "value": 2435},
                {"name": "QuantitativeScale", "value": 4839},
                {"name": "RootScale", "value": 1756},
                {"name": "Scale", "value": 4268},
                {"name": "ScaleType", "value": 1821},
                {"name": "TimeScale", "value": 5833}
            ]
        },
        {
            "name": "util",
            "children": [
                {"name": "Arrays", "value": 8258},
                {"name": "Colors", "value": 10001},
                {"name": "Dates", "value": 8217},
                {"name": "Displays", "value": 12555},
                {"name": "Filter", "value": 2324},
                {"name": "Geometry", "value": 10993},
                {
                    "name": "heap",
                    "children": [
                        {"name": "FibonacciHeap", "value": 9354},
                        {"name": "HeapNode", "value": 1233}
                    ]
                },
                {"name": "IEvaluable", "value": 335},
                {"name": "IPredicate", "value": 383},
                {"name": "IValueProxy", "value": 874},
                {
                    "name": "math",
                    "children": [
                        {"name": "DenseMatrix", "value": 3165},
                        {"name": "IMatrix", "value": 2815},
                        {"name": "SparseMatrix", "value": 3366}
                    ]
                },
                {"name": "Maths", "value": 17705},
                {"name": "Orientation", "value": 1486},
                {
                    "name": "palette",
                    "children": [
                        {"name": "ColorPalette", "value": 6367},
                        {"name": "Palette", "value": 1229},
                        {"name": "ShapePalette", "value": 2059},
                        {"name": "SizePalette", "value": 2291}
                    ]
                },
                {"name": "Property", "value": 5559},
                {"name": "Shapes", "value": 19118},
                {"name": "Sort", "value": 6887},
                {"name": "Stats", "value": 6557},
                {"name": "Strings", "value": 22026}
            ]
        },
        {
            "name": "vis",
            "children": [
                {
                    "name": "axis",
                    "children": [
                        {"name": "Axes", "value": 1302},
                        {"name": "Axis", "value": 24593},
                        {"name": "AxisGridLine", "value": 652},
                        {"name": "AxisLabel", "value": 636},
                        {"name": "CartesianAxes", "value": 6703}
                    ]
                },
                {
                    "name": "controls",
                    "children": [
                        {"name": "AnchorControl", "value": 2138},
                        {"name": "ClickControl", "value": 3824},
                        {"name": "Control", "value": 1353},
                        {"name": "ControlList", "value": 4665},
                        {"name": "DragControl", "value": 2649},
                        {"name": "ExpandControl", "value": 2832},
                        {"name": "HoverControl", "value": 4896},
                        {"name": "IControl", "value": 763},
                        {"name": "PanZoomControl", "value": 5222},
                        {"name": "SelectionControl", "value": 7862},
                        {"name": "TooltipControl", "value": 8435}
                    ]
                },
                {
                    "name": "data",
                    "children": [
                        {"name": "Data", "value": 20544},
                        {"name": "DataList", "value": 19788},
                        {"name": "DataSprite", "value": 10349},
                        {"name": "EdgeSprite", "value": 3301},
                        {"name": "NodeSprite", "value": 19382},
                        {
                            "name": "render",
                            "children": [
                                {"name": "ArrowType", "value": 698},
                                {"name": "EdgeRenderer", "value": 5569},
                                {"name": "IRenderer", "value": 353},
                                {"name": "ShapeRenderer", "value": 2247}
                            ]
                        },
                        {"name": "ScaleBinding", "value": 11275},
                        {"name": "Tree", "value": 7147},
                        {"name": "TreeBuilder", "value": 9930}
                    ]
                },
                {
                    "name": "events",
                    "children": [
                        {"name": "DataEvent", "value": 2313},
                        {"name": "SelectionEvent", "value": 1880},
                        {"name": "TooltipEvent", "value": 1701},
                        {"name": "VisualizationEvent", "value": 1117}
                    ]
                },
                {
                    "name": "legend",
                    "children": [
                        {"name": "Legend", "value": 20859},
                        {"name": "LegendItem", "value": 4614},
                        {"name": "LegendRange", "value": 10530}
                    ]
                },
                {
                    "name": "operator",
                    "children": [
                        {
                            "name": "distortion",
                            "children": [
                                {"name": "BifocalDistortion", "value": 4461},
                                {"name": "Distortion", "value": 6314},
                                {"name": "FisheyeDistortion", "value": 3444}
                            ]
                        },
                        {
                            "name": "encoder",
                            "children": [
                                {"name": "ColorEncoder", "value": 3179},
                                {"name": "Encoder", "value": 4060},
                                {"name": "PropertyEncoder", "value": 4138},
                                {"name": "ShapeEncoder", "value": 1690},
                                {"name": "SizeEncoder", "value": 1830}
                            ]
                        },
                        {
                            "name": "filter",
                            "children": [
                                {"name": "FisheyeTreeFilter", "value": 5219},
                                {"name": "GraphDistanceFilter", "value": 3165},
                                {"name": "VisibilityFilter", "value": 3509}
                            ]
                        },
                        {"name": "IOperator", "value": 1286},
                        {
                            "name": "label",
                            "children": [
                                {"name": "Labeler", "value": 9956},
                                {"name": "RadialLabeler", "value": 3899},
                                {"name": "StackedAreaLabeler", "value": 3202}
                            ]
                        },
                        {
                            "name": "layout",
                            "children": [
                                {"name": "AxisLayout", "value": 6725},
                                {"name": "BundledEdgeRouter", "value": 3727},
                                {"name": "CircleLayout", "value": 9317},
                                {"name": "CirclePackingLayout", "value": 12003},
                                {"name": "DendrogramLayout", "value": 4853},
                                {"name": "ForceDirectedLayout", "value": 8411},
                                {"name": "IcicleTreeLayout", "value": 4864},
                                {"name": "IndentedTreeLayout", "value": 3174},
                                {"name": "Layout", "value": 7881},
                                {"name": "NodeLinkTreeLayout", "value": 12870},
                                {"name": "PieLayout", "value": 2728},
                                {"name": "RadialTreeLayout", "value": 12348},
                                {"name": "RandomLayout", "value": 870},
                                {"name": "StackedAreaLayout", "value": 9121},
                                {"name": "TreeMapLayout", "value": 9191}
                            ]
                        },
                        {"name": "Operator", "value": 2490},
                        {"name": "OperatorList", "value": 5248},
                        {"name": "OperatorSequence", "value": 4190},
                        {"name": "OperatorSwitch", "value": 2581},
                        {"name": "SortOperator", "value": 2023}
                    ]
                },
                {"name": "Visualization", "value": 16540}
            ]
        }
    ]
}


# 关键词层级聚类
@router.get("/cluster/hierarchy/keyword/{dsid}")
def cluster_hierarchy_keyword(dsid):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': hierarchy_data}}


# 关键词谱聚类
@router.get("/cluster/spectral/keyword/{dsid}")
def cluster_spectral_keyword(dsid):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': cluster_spectral_dataset}}


# 关键词趋势聚类
@router.get("/cluster/trend/keyword/{dsid}")
def cluster_trend_keyword(dsid):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': forcetrend_data}}


# 知识图谱
@router.get("/{userId}/{dsid}/{count}")
def kg(userId, dsid, count: int = 10):
    kg = statManager.kg(userId, dsid, count)
    return kg
