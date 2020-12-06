from pydantic.main import BaseModel

from api import dao
from api.util.utils import Logger

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginForm(BaseModel):
    username: str = None
    password: str = None


class CommonManager:
    def __init__(self):
        self.log = Logger(__name__).get_log
        self.dao = dao

    # 登录验证
    def getUser(self, username, password):
        users = self.dao.get_user(username, password)
        if users:
            return users[0]
        else:
            return {}

    # 所有导航菜单
    # def findMenu(self):
    #     sql = 'SELECT * FROM sys_menu'
    #     all = self.db.fetch_all(sql)
    #     return self._treeMenu(all)
    #
    # def _treeMenu(self, menus):
    #     menu1 = [item for item in menus if item['pid'] == 0]
    #     for item1 in menu1:
    #         menu2 = [item for item in menus if item['pid'] == item1['id']]
    #         item1['children'] = menu2
    #         for item2 in menu2:
    #             menu3 = [item for item in menus if item['pid'] == item2['id']]
    #             item2['children'] = menu3
    #             for item3 in menu3:
    #                 menu4 = [item for item in menus if item['pid'] == item3['id']]
    #                 item3['children'] = menu4
    #     return menu1


commonManager = CommonManager()