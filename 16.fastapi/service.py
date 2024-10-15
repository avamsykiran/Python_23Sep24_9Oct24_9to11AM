from models import Item
from typing import List

_items:List[Item] = []

def getAll() -> List[Item]:
    return _items

def getById(id:int) -> Item | None:
    item:Item | None = None
    
    for i in range(0,_items.count):
        if _items[i].id==id:
            item=_items[i]
            break 
        
    return item

def add(item:Item):
    _items.append(item)
    
def update(item:Item):
    for i in range(0,_items.count):
        if _items[i].id==item.id:
            _items[i]=item
            break 

def deleteById(id:int):
    _item:Item | None = None
    
    for i in range(0,_items.count):
        if _items[i].id==id:
            item=_items[i]
            break 
    
    if item!=None:
        _items.remove(item)

