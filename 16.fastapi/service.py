from models import Item
from database import SessionLocal
from typing import List

def getAll() -> List[Item]:
    """Get all items from database"""
    db = SessionLocal()
    try:
        items = db.query(Item).all()
        return items
    finally:
        db.close()

def getById(id: int) -> Item | None:
    """Get item by ID"""
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == id).first()
        return item
    finally:
        db.close()

def add(item: Item):
    """Add new item to database"""
    db = SessionLocal()
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    finally:
        db.close()

def update(item: Item):
    """Update existing item"""
    db = SessionLocal()
    try:
        existing_item = db.query(Item).filter(Item.id == item.id).first()
        if existing_item:
            existing_item.item_name = item.item_name
            existing_item.price = item.price
            db.commit()
            db.refresh(existing_item)
            return existing_item
        return None
    finally:
        db.close()

def deleteById(id: int):
    """Delete item by ID"""
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == id).first()
        if item:
            db.delete(item)
            db.commit()
            return True
        return False
    finally:
        db.close()

