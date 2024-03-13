from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 모델 정의
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 루트 엔드포인트
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# 아이템 가져오기 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# 아이템 생성 엔드포인트
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

# 서버 실행 방법 (터미널):
# uvicorn main:app --reload
# `main`은 이 파일의 이름 (main.py라 가정). `app`은 FastAPI 인스턴스 이름.
