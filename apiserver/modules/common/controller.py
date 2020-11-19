from fastapi import APIRouter

router = APIRouter()
from common.base import ok, fail
from .manager import commonManager, LoginForm

# 登录
@router.post('/login')
def login(form : LoginForm):
    user = commonManager.getUser(form)
    return ok(user)

# 导航菜单
@router.get('/navs')
def navs():
    menus = commonManager.findMenu()
    return ok(menus)