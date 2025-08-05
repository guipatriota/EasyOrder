from fastapi import APIRouter, HTTPException
from src.models.order import Order
from src.db.memory_db import orders_db

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def listar_ordens():
    return orders_db

@router.get("/{order_id}")
def obter_ordem(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Ordem não encontrada")

@router.post("/")
def criar_ordem(order: Order):
    if any(o.id == order.id for o in orders_db):
        raise HTTPException(status_code=400, detail="ID da ordem já existe")
    orders_db.append(order)
    return {"mensagem": "Ordem criada com sucesso", "ordem": order}

@router.put("/{order_id}/status")
def atualizar_status(order_id: int, status: str):
    for order in orders_db:
        if order.id == order_id:
            order.status = status
            return {"mensagem": f"Status da ordem {order_id} atualizado para {status}", "ordem": order}
    raise HTTPException(status_code=404, detail="Ordem não encontrada")

@router.delete("/{order_id}")
def deletar_ordem(order_id: int):
    for idx, order in enumerate(orders_db):
        if order.id == order_id:
            deletada = orders_db.pop(idx)
            return {"mensagem": "Ordem deletada com sucesso", "ordem": deletada}
    raise HTTPException(status_code=404, detail="Ordem não encontrada")
