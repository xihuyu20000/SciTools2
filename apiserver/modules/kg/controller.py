from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from .manager import kgManager


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# 知识图谱
@router.get("/{userId}/{fileId}/{count}")
def kg(userId, fileId, count: int = 10):
    kg = kgManager.kg(userId, fileId, count)
    return kg





@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):  # 此处q为query的字段
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):  # 此处Item为body的schema
    return {"item_name": item.name, "item_id": item_id}

