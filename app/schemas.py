from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .models import ItemType, EventType

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
class ItemBase(BaseModel):
    title: str
    type: ItemType
    tags: Optional[str] = None
    item_metadata: Optional[dict] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class InteractionBase(BaseModel):
    event_type: EventType
    rating: Optional[float] = None

class InteractionCreate(InteractionBase):
    user_id: int
    item_id: int

class Interaction(InteractionBase):
    id: int
    user_id: int
    item_id: int
    created_at: datetime

    class Config:
        orm_mode = True
