"""
FastAPI basics:
- GET /health
- GET list/detail
- POST create
- PUT update
- DELETE remove
"""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(title="Lesson 10: FastAPI")
"""
# pip install fastapi,pydantic uvicorn
# запуск: python -m uvicorn lesson10.fastapi_part1_examples:app --reload
# документация по API http://127.0.0.1:8000/docs
"""


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    price: float = Field(ge=0)
    in_stock: bool = True


class Item(ItemCreate):
    id: int


_items: list[Item] = [
    Item(id=1, name="Keyboard", price=49.99, in_stock=True),
    Item(id=2, name="Mouse", price=24.50, in_stock=True),
    Item(id=3, name="Monitor", price=199.00, in_stock=False),
]


def _find_item_index(item_id: int) -> int:
    for idx, item in enumerate(_items):
        if item.id == item_id:
            return idx
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items", response_model=list[Item])
def list_items(
    limit: int = Query(default=10, ge=1, le=100),
    min_price: Optional[float] = Query(default=None, ge=0),
) -> list[Item]:
    data = _items
    if min_price is not None:
        data = [item for item in data if item.price >= min_price]
    return data[:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    idx = _find_item_index(item_id)
    return _items[idx]


@app.post("/items", status_code=201, response_model=Item)
def create_item(payload: ItemCreate) -> Item:
    new_id = max((item.id for item in _items), default=0) + 1
    item = Item(id=new_id, **payload.model_dump())
    _items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate) -> Item:
    idx = _find_item_index(item_id)
    updated = Item(id=item_id, **payload.model_dump())
    _items[idx] = updated
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    idx = _find_item_index(item_id)
    _items.pop(idx)
    return {"message": "deleted"}

