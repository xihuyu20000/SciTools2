from fastapi import APIRouter

from ...util.base import ok

router = APIRouter()

from .manager import configManager, ConfigForm


# 配置
@router.get('/')
def index():
    config = {'stopwords_dict': '保存后数据'}
    return ok(config)


@router.post("/save")
def save(form: ConfigForm):
    configManager.save(form)
    return {'status': 200}
