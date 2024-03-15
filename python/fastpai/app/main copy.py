from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

# 기본 홈페이지 엔드포인트
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI test server!"}

# GET 요청 처리
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST 요청 처리를 위한 데이터 모델
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# POST 요청 처리
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# 경로 매개변수 처리
@app.get("/users/{user_id}")
async def read_user(user_id: int = Path(..., title="The ID of the user to get")):
    return {"user_id": user_id}

# 쿼리 매개변수 처리
@app.get("/query/")
async def read_query(needs_query: bool = False, q: str = Query(None, max_length=50)):
    return {"needs_query": needs_query, "q": q}

# 시작
# uvicorn main:app --reload