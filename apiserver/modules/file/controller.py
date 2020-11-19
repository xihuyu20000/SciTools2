import os
import shutil
import uuid
import zipfile
from pathlib import Path
from common.constant import get_upload_home
from threading import Thread
from common.utils import remove_dir
from typing import List

from fastapi import APIRouter, Request, File, Form, UploadFile
router = APIRouter()

from .manager import fileManager

@router.get('/list')
def list():
    all = fileManager.list()
    return {'data':all}

# 上传文件，只接收一个压缩文件
@router.post('/upload')
async def upload(files: List[UploadFile] = File(...), source: str = Form(...), name: str = Form(...)):
    print(source, name, files[0].filename, )
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

    with zipfile.ZipFile(save_path, "r") as zFile:
        # ZipFile.namelist(): 获取ZIP文档内所有文件的名称列表
        for fileM in zFile.namelist():
            zFile.extract(fileM, save_path+"_dir")

    fileManager.saveUpload(source, file_name, file_size, raw_name, save_path)

    return {"status": 200}

# 解析数据文件
@router.get('/parse/{fileId}')
def parseDatafile(fileId):
    Thread(target=fileManager.parseDatafile, args=(fileId,)).start()
    return {'status': 200}

# 删除
@router.delete('/{fileId}')
def delete(fileId):
    file = fileManager.get(fileId)
    fileManager.remove(fileId)
    try:
        Path(file['save_path']).unlink()
        remove_dir(file['save_path']+'_dir')
    except Exception as e:
        print(e)
    return {'status':200}

# 生成WOS的excel格式
@router.get("/genWosExcel/{userId}/{fileId}")
def generateWosExcel(userId, fileId):
    path = fileManager.generateWosExcel(userId, fileId)
    return path