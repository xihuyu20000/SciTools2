from fastapi import APIRouter

from api import ok

router = APIRouter()

from .manager import configManager, ConfigForm


# 配置
@router.get('/')
def index():
    config = {
        'stopwords_style':0,
        'stopwords_text': '',

        'splitwords_style': 0,
        'splitwords_text': '',

        'synonymwords_style': 0,
        'synonymwords_text': '',

        'combineauthor_style': 0,
        'combineauthor_text': '',

        'combineorg_style': 0,
        'combineorg_text': '',

        'combineprovince_style': 0,
        'combineprovince_text': '',

        'combinecountry_style': 0,
        'combinecountry_text': '',

        'combinefund_style': 0,
        'combinefund_text': '',

        'combinebranch_style': 0,
        'combinebranch_text': '',

        'a':'a'
    }
    return ok(config)


@router.post("/save")
def save(form: ConfigForm):
    configManager.save(form)
    return {'status': 200}
