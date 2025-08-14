"""Banco de dados em memória para o EasyOrder.

Mantém uma lista mutável de pedidos durante a execução do processo. Útil para
desenvolvimento, exemplos e testes, sem persistência em disco.

Attributes:
    orders_db (List[Order]): Armazenamento em memória dos pedidos.

Note:
    Os dados são perdidos quando o processo encerra e não há segurança para
    acesso concorrente.
"""

from typing import List

from src.models.order import Order

__all__ = ["orders_db"]

orders_db: List[Order] = []
