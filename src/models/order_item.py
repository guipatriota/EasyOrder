"""Modelos de dados para itens de pedido.

Define a classe OrderItem, um modelo Pydantic que representa um item em um
pedido (produto, quantidade e preço unitário).
"""

from pydantic import BaseModel


class OrderItem(BaseModel):
    """Representa um item de um pedido.

    Attributes:
        product_id (int): ID interno do produto.
        product_name (str): Nome do produto.
        quantity (int): Quantidade solicitada.
        price (float): Preço unitário do produto.
    """

    product_id: int
    product_name: str
    quantity: int
    price: float  # preço unitário
