from fastapi import APIRouter, HTTPException, Depends
from database import Item, get_db
from typing import Dict

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)

def get_item(cart_id: int, db: Dict[int, Item] = Depends(get_db)):
    if cart_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[cart_id]

@router.post("")
def add_item(item: Item, db: Dict[int, Item] = Depends(get_db)):
    if item.cart_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item.cart_id] = item
    return item

@router.get("")
def get_all_items(db: Dict[int, Item] = Depends(get_db)):
    return db

@router.get("/{cart_id}")
def get_one_item(item: Item = Depends(get_item)):
    return item

@router.put("/{cart_id}")
def update_item(
    updated_item: Item,
    existing_item: Item = Depends(get_item),
    db: Dict[int, Item] = Depends(get_db),
):
    if updated_item.cart_id != existing_item.cart_id:
        raise HTTPException(status_code=400, detail="cart_id mismatch")
    db[existing_item.cart_id] = updated_item
    return updated_item

@router.delete("/{cart_id}")
def delete_item(
    item: Item = Depends(get_item),
    db: Dict[int, Item] = Depends(get_db),
):
    del db[item.cart_id]
    return {"message": "Item deleted", "item": item}