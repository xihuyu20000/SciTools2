from fastapi import APIRouter

from api import ok

router = APIRouter()

from .manager import configManager, ConfigForm


# 配置
@router.get('/')
def index():
    userid = 'test'
    sql = "SELECT * FROM default.dim_config WHERE userid='{}'".format(userid)
    configs = configManager.find(sql)
    result = {}
    for config in configs:
        result[config['style']] = config['values']
    return ok(result)


@router.post("/save")
def save(form: ConfigForm):
    configManager.save(form)
    return {'status': 200}
