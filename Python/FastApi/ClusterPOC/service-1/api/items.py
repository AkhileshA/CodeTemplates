from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.item import Item, ItemCreate, ItemUpdate
from services.item_service import item_service

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/", response_model=List[Item])
async def get_items(
    name: Optional[str] = Query(None, description="Filter by item name"),
    in_stock: Optional[bool] = Query(None, description="Filter by stock status")
):
    """Get all items with optional filters"""
    if name is not None or in_stock is not None:
        return item_service.search_items(name=name, in_stock=in_stock)
    return item_service.get_all_items()


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    item = item_service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    return item


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item"""
    return item_service.create_item(item)


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    updated_item = item_service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    return updated_item


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item"""
    success = item_service.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
