"""Rotas de API para operações de pedidos.

Expõe endpoints para listar, obter, criar, atualizar status e deletar pedidos.
"""

from fastapi import APIRouter, HTTPException

from src.db.memory_db import orders_db
from src.models.order import Order

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/")
def listar_ordens():
    """Lista todas as ordens.

    Returns:
        list[Order]: Lista de pedidos atualmente armazenados.
    """
    return orders_db


@router.get("/{order_id}")
def obter_ordem(order_id: int):
    """Obtém uma ordem pelo ID.

    Args:
        order_id (int): Identificador único da ordem.

    Returns:
        Order: Ordem correspondente ao ID informado.

    Raises:
        HTTPException: 404 se a ordem não for encontrada.
    """
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Ordem não encontrada")


@router.post("/")
def criar_ordem(order: Order):
    """Cria uma nova ordem.

    Args:
        order (Order): Dados da ordem a ser criada.

    Returns:
        dict: Mensagem de sucesso e a ordem criada.

    Raises:
        HTTPException: 400 se já existir uma ordem com o mesmo ID.
    """
    if any(o.id == order.id for o in orders_db):
        raise HTTPException(status_code=400, detail="ID da ordem já existe")
    orders_db.append(order)
    return {"mensagem": "Ordem criada com sucesso", "ordem": order}


@router.put("/{order_id}/status")
def atualizar_status(order_id: int, status: str):
    """Atualiza o status de uma ordem existente.

    Args:
        order_id (int): Identificador da ordem.
        status (str): Novo status. Valores possíveis: "open", "closed",
        "cancelled".

    Returns:
        dict: Mensagem de sucesso e a ordem atualizada.

    Raises:
        HTTPException: 404 se a ordem não for encontrada.
    """
    for order in orders_db:
        if order.id == order_id:
            order.status = status
            return {
                "mensagem": (
                    f"Status da ordem {order_id} " f"atualizado para {status}"
                ),
                "ordem": order,
            }
    raise HTTPException(status_code=404, detail="Ordem não encontrada")


@router.delete("/{order_id}")
def deletar_ordem(order_id: int):
    """Deleta uma ordem pelo ID.

    Args:
        order_id (int): Identificador da ordem a ser removida.

    Returns:
        dict: Mensagem de sucesso e a ordem deletada.

    Raises:
        HTTPException: 404 se a ordem não for encontrada.
    """
    for idx, order in enumerate(orders_db):
        if order.id == order_id:
            deletada = orders_db.pop(idx)
            return {"mensagem": "Ordem deletada com sucesso", "ordem": deletada}
    raise HTTPException(status_code=404, detail="Ordem não encontrada")
