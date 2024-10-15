from fastapi import FastAPI,Response,status
from models import Item
import service
        
# FastAPI app instance
app = FastAPI()
  
# CRUD operations
# Create (Create)
@app.post("/items/")
async def create_item(item:Item,resp:Response):
    service.add(item)
    resp.status_code=status.HTTP_201_CREATED
    return item
  
# Read (GET ALL)
@app.get("/items/",status_code=status.HTTP_200_OK)
async def read_all_items():        
    return service.getAll()
 
# Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int,resp:Response):
    item = service.getById(id)
    
    if item==None:
        resp.status_code=status.HTTP_404_NOT_FOUND
    else:
        resp.status_code=status.HTTP_200_OK
        
    return item
  
# Update (PUT)
@app.put("/items/")
async def update_item(item:Item,resp:Response):
    service.update(item)
    resp.status_code=status.HTTP_202_ACCEPTED
    return item
  
# Delete (DELETE)
@app.delete("/items/{item_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    service.deleteById(item_id)
    return {"message": "Item deleted successfully"}
