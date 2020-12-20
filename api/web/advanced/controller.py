import  os
from urllib import parse

from fastapi import APIRouter

from api import ok, fail
from .manager import advancedManager
router = APIRouter()


# 上传数据文件并分析
@router.post('/upload')
def upload():
    userid = 'f6d2dd05-3cb4-4989-8c22-48c7899d0d0b'
    advancedManager.parseExcel(userid, r'C:\Users\Administrator\Desktop\论文\人工智能500条.xls')
    return ok()

# 查询元表名称信息
@router.get('/tblnames')
def find_tblnames():
    userid = 'f6d2dd05-3cb4-4989-8c22-48c7899d0d0b'
    ret = advancedManager.find_tblname(userid)
    return ok(ret)

# 修改元表名称
@router.get('/tblrename/{tblid}/{newName}')
def tlbrename(tblid, newName):
    newName = parse.unquote(newName)
    advancedManager.rename(tblid, newName)
    return ok()

# 删除元表数据
@router.get('/delete/{tblid}')
def delete(tblid):
    advancedManager.delete(tblid)
    return ok()

# 根据tlbid查询数据
@router.get('/dataset_query/{tlbid}')
def dataset_query(tlbid):
    titles, dataset = advancedManager.query_dataset_by(tlbid)
    # 先排序，再转成vxe-table需要的格式
    titles = sorted(titles.items(), key=lambda x: x[0])
    titles = [{'field':title[0], 'title':title[1][0], 'width':'200px', 'resizable':True, 'sortable':True } for title in titles]
    titles.insert(0, {'type':'checkbox', 'title':'dsid', 'width':'100px'})
    titles.insert(0, {'type':'seq', 'width':'60px'})

    # 每个数据是数组，需要提取数据
    for index, row in enumerate(dataset):
        temp = {}
        for k,v in row.items():
            temp[k] = v[0]
        dataset[index] = temp

    # print('标题', titles)
    # print('数据集', dataset)
    return ok([titles, dataset])