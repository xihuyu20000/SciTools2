import shutil
import uuid
import zipfile
from typing import List
from urllib import parse

import demjson
from fastapi import APIRouter, Form, UploadFile, File

from api import ok
from .manager import advancedManager, FieldsConfigForm, TblsDatasetForm, DatasetCleaningForm
from api.dao.ad_tbls import VxeColumnEdit

from api.util.utils import read_lines
from ...const import get_upload_home

router = APIRouter()


# 上传数据文件并分析
@router.post('/upload')
def upload(style:str =Form(...), files: List[UploadFile] = File(...)):
    # 文件真实名称
    file_name = files[0].filename
    # 随机名称
    raw_name = uuid.uuid4().hex
    # 文件绝对路径
    save_path = os.path.join(get_upload_home(), raw_name)
    with open(save_path, 'wb+') as upload_folder:
        shutil.copyfileobj(files[0].file, upload_folder)
    # # 文件大小
    # file_size = zipfile.Path(save_path).stat().st_size
    #
    # save_path_dir = save_path + "_dir"
    # with zipfile.ZipFile(save_path, "r") as zFile:
    #     # ZipFile.namelist(): 获取ZIP文档内所有文件的名称列表
    #     for fileM in zFile.namelist():
    #         zFile.extract(fileM, save_path_dir)
    print('上传文件', file_name[:-4], style, save_path)
    # datasetManager.saveUpload(file_name[:-4], style, save_path_dir)

    userid = 'f6d2dd05-3cb4-4989-8c22-48c7899d0d0b'
    advancedManager.parseExcel(userid, save_path)
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

@router.post('/dataset_cleaning')
def dataset_cleaning(form:DatasetCleaningForm):
    advancedManager.cleaning_dataset(form)

# 保存元表信息和数据集
@router.post('/dataset_update')
def dataset_update(form:TblsDatasetForm):
    # 先删除，再插入；不能使用UPDATE语法
    advancedManager.update_tbl_dataset(form)
    return ok()

# 另存为新的元表信息和数据集
@router.post('/dataset_saveAsNew')
def dataset_saveAsNew(form:TblsDatasetForm):
    # 先删除，再插入；不能使用UPDATE语法
    advancedManager.saveAsNew_tbl_dataset(form)
    return ok()

# 显示列字段信息
@router.get('/list_fieldconfigs/{tblid}')
def list_fieldconfigs(tblid):
    colstr, titles = advancedManager.query_tbl_by_tblid(tblid)
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

import os
# 加载图表的配置信息和数据
@router.get('/graph/load_option_data/{graphStyle}')
def graph_load_option_data(graphStyle:str):
    jsfile = os.path.join(os.getcwd(), 'graph-options', graphStyle+'.js')
    jsstr = ''.join(read_lines(jsfile)).strip()
    jsstr = jsstr[:-1] if jsstr.endswith(';') else jsstr
    option = demjson.decode(jsstr)
    print('加载的配置', option)
    return ok({'option':option})