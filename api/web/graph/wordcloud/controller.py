from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from .manager import wordCloudManager



# 关键词词云
@router.get("/keyword/{fileId}")
def keyword(fileId):
    return {}

# 主题词词云
@router.get("/topicword/{fileId}")
def topicword(fileId):
    return {}