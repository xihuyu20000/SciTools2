import datetime
from datetime import timedelta
from typing import Optional

import jwt as jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

router = APIRouter()
from api.util.base import ok, fail
from .manager import commonManager, LoginForm, Token

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# 校验密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# 密码哈希
def get_password_hash(password):
    return pwd_context.hash(password)

# 用户信息校验：username和password分别校验
def authenticate_user(username: str, password: str):
    user = commonManager.getUser(username, password)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 生成token，带有过期时间
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

######################   https://www.cnblogs.com/mazhiyong/p/13219300.html

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 首先校验用户信息
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return fail('不正确的用户名或密码')

    # 生成并返回token信息
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": "test"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 登录
@router.post('/login')
def login(form : LoginForm):
    user = commonManager.getUser(form.username, form.password)
    return ok(user)

# 导航菜单
@router.get('/navs')
def navs():
    menus = commonManager.findMenu()
    return ok(menus)