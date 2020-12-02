from fastapi import APIRouter

from ...util.base import ok

router = APIRouter()

from .manager import statManager

@router.get('/list/names')
def list_names():
    datas = statManager.list_names()
    return ok(data=datas)

@router.get('/list/{fileId}')
def list(fileId):
    datas = statManager.list_dataset(fileId)
    return ok(data=datas)
