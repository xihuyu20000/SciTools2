from pydantic.main import BaseModel

from api import dao
from api.util.utils import Logger

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginForm(BaseModel):
    username: str = None
    password: str = None


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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


commonManager = CommonManager()
