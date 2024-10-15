from pydantic import BaseModel
 
#model
class Item(BaseModel):
    id: int
    itemName: str
    price: float