from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    """Base Item model with common attributes"""
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True


class ItemCreate(ItemBase):
    """Model for creating a new item"""
    pass


class ItemUpdate(ItemBase):
    """Model for updating an existing item"""
    pass


class Item(ItemBase):
    """Complete Item model with ID"""
    id: int

    class Config:
        from_attributes = True
