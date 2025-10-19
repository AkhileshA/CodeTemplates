from typing import List, Optional
from models.item import Item, ItemCreate, ItemUpdate


class ItemService:
    """Service layer for Item business logic"""

    def __init__(self):
        # In-memory storage (for demo purposes)
        # In a real application, this would be a database
        self.items_db: List[Item] = [
            Item(id=1, name="Laptop", description="High-performance laptop", price=999.99, in_stock=True),
            Item(id=2, name="Mouse", description="Wireless mouse", price=29.99, in_stock=True),
            Item(id=3, name="Keyboard", description="Mechanical keyboard", price=79.99, in_stock=False),
        ]
        self.next_id = 4

    def get_all_items(self) -> List[Item]:
        """Retrieve all items"""
        return self.items_db

    def get_item_by_id(self, item_id: int) -> Optional[Item]:
        """Retrieve a specific item by ID"""
        for item in self.items_db:
            if item.id == item_id:
                return item
        return None

    def create_item(self, item_data: ItemCreate) -> Item:
        """Create a new item"""
        new_item = Item(
            id=self.next_id,
            **item_data.model_dump()
        )
        self.items_db.append(new_item)
        self.next_id += 1
        return new_item

    def update_item(self, item_id: int, item_data: ItemUpdate) -> Optional[Item]:
        """Update an existing item"""
        for idx, item in enumerate(self.items_db):
            if item.id == item_id:
                updated_item = Item(
                    id=item_id,
                    **item_data.model_dump()
                )
                self.items_db[idx] = updated_item
                return updated_item
        return None

    def delete_item(self, item_id: int) -> bool:
        """Delete an item by ID"""
        for idx, item in enumerate(self.items_db):
            if item.id == item_id:
                self.items_db.pop(idx)
                return True
        return False

    def search_items(self, name: Optional[str] = None, in_stock: Optional[bool] = None) -> List[Item]:
        """Search items by name or stock status"""
        results = self.items_db

        if name is not None:
            results = [item for item in results if name.lower() in item.name.lower()]

        if in_stock is not None:
            results = [item for item in results if item.in_stock == in_stock]

        return results


# Singleton instance
item_service = ItemService()
