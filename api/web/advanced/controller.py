import  os
from urllib import parse

from fastapi import APIRouter

from api import ok, fail
from .manager import advancedManager, FieldsConfigForm
from ...dao.db.ad_tbls import build_vxe_table, build_field_config

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
    ret = advancedManager.find_tbl_by_userid(userid)
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

# 根据tblid查询并显示数据集
@router.get('/dataset_query/{tblid}')
def dataset_query(tblid):
    titles, dataset = advancedManager.query_dataset_by(tblid)
    # titles是list嵌套dict，{'c10': ['SrcDatabase-来源库', '文本', '200px', '0'],......}先排序
    titles = sorted(titles.items(), key=lambda x: int(x[1][3])) # 按照顺序号 排序
    # ，再转成vxe-table需要的格式
    titles = [build_vxe_table(title) for title in titles]
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

# 显示列字段信息
@router.get('/list_fieldconfigs/{tblid}')
def list_fieldconfigs(tblid):
    titles = advancedManager.find_tbl_by_tblid(tblid)
    titles = titles[0]
    [titles.pop(k) for k in ('tblid','pid','tblname') if k in titles.keys()]
    titles = sorted(titles.items(), key=lambda x:int(x[1][3]))  #dict转为list
    titles = [build_field_config(tc) for tc in titles]
    return ok(titles)

# 保存字段配置信息
@router.post(('/save_fieldconfigs'))
def save_fieldconfigs(form:FieldsConfigForm):
    print('字段配置信息', form)
    advancedManager.updateFieldConfig(form)
    return ok()