import  os
from urllib import parse

from fastapi import APIRouter

from api import ok, fail
from .manager import advancedManager, FieldsConfigForm, TblsDatasetForm
from ...dao.db.ad_tbls import build_field_config, VxeColumnEdit

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
    _, vxeColumns, dataset = advancedManager.query_dataset_by(tblid)

    vxeColumns.insert(0, {'type': 'seq', 'width': '100px'})
    vxeColumns.insert(0, {'type':'checkbox', 'title':'', 'width':'60px'})

    return ok([vxeColumns, dataset])

# 保存元表信息和数据集
@router.post('/dataset_update')
def dataset_update(form:TblsDatasetForm):
    # 先删除，再插入；不能使用UPDATE语法
    advancedManager.update_tbl_dataset(form)
    return ok()

# 显示列字段信息
@router.get('/list_fieldconfigs/{tblid}')
def list_fieldconfigs(tblid):
    colstr, titles = advancedManager.find_tbl_by_tblid(tblid)
    result = []
    for name in colstr.split(','):
        value = titles[name]
        result.append(VxeColumnEdit(name, value[0], value[1], value[2]).toVxe())
    return ok(result)

# 保存字段配置信息
@router.post(('/save_fieldconfigs'))
def save_fieldconfigs(form:FieldsConfigForm):
    # print('字段配置信息', form)
    advancedManager.updateFieldConfig(form)
    return ok()