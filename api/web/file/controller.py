import os
import shutil
import uuid
import zipfile
from pathlib import Path
from api.config import get_upload_home
from threading import Thread
from api.util.utils import remove_dir
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from ... import fail, ok

router = APIRouter()

from .manager import fileManager

# 上传文件，只接收一个压缩文件
@router.post('/upload')
async def upload( style:str =Form(...), files: List[UploadFile] = File(...)):
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
    fileManager.saveUpload(file_name[:-4], style, save_path_dir)
    return ok()