from pydantic import BaseModel
from typing import List
from .order_item import OrderItem

class Order(BaseModel):
    id: int
    customer_name: str
    items: List[OrderItem]
    status: str = "open"  # open, closed, cancelled
