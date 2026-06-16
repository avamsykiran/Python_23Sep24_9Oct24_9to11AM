from fastapi import FastAPI, Response, status
from models import Item
from database import engine, Base, init_db
import service

# Create all database tables
init_db()

# FastAPI app instance
app = FastAPI(title="Item API", version="1.0.0")

# CRUD operations

# Create (POST)
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """Create a new item"""
    return service.add(item)

# Read All (GET)
@app.get("/items/", response_model=list[Item], status_code=status.HTTP_200_OK)
async def read_all_items():
    """Get all items"""
    return service.getAll()

# Read by ID (GET)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """Get item by ID"""
    item = service.getById(item_id)
    
    if item is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return item

# Update (PUT)
@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_202_ACCEPTED)
async def update_item(item_id: int, item: Item):
    """Update an existing item"""
    db_item = Item(id=item_id, item_name=item.item_name, price=item.price)
    updated_item = service.update(db_item)
    
    if updated_item is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return updated_item

# Delete (DELETE)
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item"""
    success = service.deleteById(item_id)
    
    if not success:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return None

# Health check endpoint
@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    """Health check endpoint"""
    return {"message": "Item API is running", "version": "1.0.0"}
