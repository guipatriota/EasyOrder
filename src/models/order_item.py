from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float  # preço unitário
