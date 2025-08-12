"""Modelos de dados para pedidos.

Fornece o modelo Pydantic Order, que representa um pedido contendo itens,
cliente e status.
"""

from typing import List

from pydantic import BaseModel

from .order_item import OrderItem


class Order(BaseModel):
    """Representa um pedido.

    Attributes:
        id (int): Identificador único do pedido.
        customer_name (str): Nome do cliente associado ao pedido.
        items (List[OrderItem]): Lista de itens que compõem o pedido.
        status (str): Estado atual do pedido. Valores possíveis: "open",
        "closed", "cancelled".
    """

    id: int
    customer_name: str
    items: List[OrderItem]
    status: str = "open"  # open, closed, cancelled
