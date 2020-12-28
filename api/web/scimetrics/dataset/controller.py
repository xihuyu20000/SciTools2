from fastapi import APIRouter
from threading import Thread
from urllib import parse
import os
import shutil
import uuid
import zipfile
from pathlib import Path

from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from api import ok
from api.const import get_upload_home


router = APIRouter()

from .manager import datasetManager, OdsbibDeleteForm, OdsbibUpdateForm

# 上传文件，只接收一个压缩文件
@router.post('/upload')
async def upload(style:str =Form(...), files: List[UploadFile] = File(...)):
    # 文件真实名称
    file_name = files[0].filename
    # 随机名称
    raw_name = uuid.uuid4().hex
    # 文件绝对路径
    save_path = os.path.join(get_upload_home(), raw_name)
    with open(save_path, 'wb+') as upload_folder:
        shutil.copyfileobj(files[0].file, upload_folder)
    # 文件大小
    file_size = Path(save_path).stat().st_size

    save_path_dir = save_path+"_dir"
    with zipfile.ZipFile(save_path, "r") as zFile:
        # ZipFile.namelist(): 获取ZIP文档内所有文件的名称列表
        for fileM in zFile.namelist():
            zFile.extract(fileM, save_path_dir)
    datasetManager.saveUpload(file_name[:-4], style, save_path_dir)
    return ok()

@router.get('/list/names')
def list_names():
    datas = datasetManager.list_names()
    return ok(data=datas)

@router.get('/list/{dsid}')
def list(dsid):
    datas = datasetManager.list_dataset(dsid)
    return ok(data=datas)

@router.get('/clean/{dsid}')
def clean(dsid):
    userid = 'test'
    CleanDatasetThread(dsid, userid).start()
    return ok()

class CleanDatasetThread(Thread):
    def __init__(self, dsid = '', userid = ''):
        super().__init__()
        self.dsid = dsid
        self.userid = userid

    def run(self) -> None:
        if self.dsid:
            datasetManager.clean(self.dsid, self.userid)

@router.get('/show/process/{dsid}')
def show_process(dsid):
    dim_ds = datasetManager.showProcess(dsid)
    return ok(data=dim_ds)

@router.get('/delete/{dsid}')
def delete(dsid):
    datasetManager.delete(dsid)
    return ok()


@router.get('/rename/{dsid}/{newName}')
def rename(dsid, newName):
    newName = parse.unquote(newName)
    datasetManager.rename(dsid, newName)
    return ok()


@router.post('/odsbib/delete')
def odsbibdelete(form : OdsbibDeleteForm):
    datasetManager.deleteOdsbibById(form.ids)
    return ok()


@router.post('/odsbib/update')
def odsbibupdate(form : OdsbibUpdateForm):
    datasetManager.updateOdsbib(form)
    return ok()