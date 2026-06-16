from sqlmodel import SQLModel, Field
from typing import Optional

# SQLModel - combines SQLAlchemy ORM and Pydantic validation
class Item(SQLModel, table=True):
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    item_name: str = Field(max_length=100, index=True)
    price: float


# ============== OLD CODE (COMMENTED OUT) ==============
# from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, Float
# from database import Base
#
# # SQLAlchemy ORM Model
# class Item(Base):
#     __tablename__ = "items"
#     
#     id = Column(Integer, primary_key=True, index=True)
#     item_name = Column(String(100), nullable=False, index=True)
#     price = Column(Float, nullable=False)
#
# # Pydantic Schema for request/response validation
# class ItemSchema(BaseModel):
#     id: int
#     item_name: str
#     price: float
#     
#     class Config:
#         from_attributes = True
# ======================================================