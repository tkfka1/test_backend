from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 데이터 저장을 위한 가상 DB
items_db = {}

# 아이템 모델 정의
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# CREATE
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.name] = item
    return item

# READ (All)
@app.get("/items/", response_model=List[Item])
async def read_items():
    return list(items_db.values())

# READ (One)
@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    if item_name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_name]

# UPDATE
@app.put("/items/{item_name}", response_model=Item)
async def update_item(item_name: str, item: Item):
    if item_name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_name] = item
    return item

# DELETE
@app.delete("/items/{item_name}", response_model=Item)
async def delete_item(item_name: str):
    if item_name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db.pop(item_name)

