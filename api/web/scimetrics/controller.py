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


# 上传文件，只接收一个压缩文件
