from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="EasyOrder API - Sistema de Ordens de Compras Online")

# ------------------------------
# Modelos de Dados
# ------------------------------
class OrderItem(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float  # preço unitário

class Order(BaseModel):
    id: int
    customer_name: str
    items: List[OrderItem]
    status: str = "open"  # open, closed, cancelled

# Banco de dados em memória
orders_db: List[Order] = []

# ------------------------------
# Rotas da API
# ------------------------------

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo à EasyOrder API! Sistema de ordens de compras online."}

@app.get("/orders")
def listar_ordens():
    return orders_db

@app.get("/orders/{order_id}")
def obter_ordem(order_id: int):
    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Ordem não encontrada")

@app.post("/orders")
def criar_ordem(order: Order):
    # Verifica se o ID já existe
    if any(o.id == order.id for o in orders_db):
        raise HTTPException(status_code=400, detail="ID da ordem já existe")
    orders_db.append(order)
    return {"mensagem": "Ordem criada com sucesso", "ordem": order}

@app.put("/orders/{order_id}/status")
def atualizar_status(order_id: int, status: str):
    for order in orders_db:
        if order.id == order_id:
            order.status = status
            return {"mensagem": f"Status da ordem {order_id} atualizado para {status}", "ordem": order}
    raise HTTPException(status_code=404, detail="Ordem não encontrada")

@app.delete("/orders/{order_id}")
def deletar_ordem(order_id: int):
    for idx, order in enumerate(orders_db):
        if order.id == order_id:
            deletada = orders_db.pop(idx)
            return {"mensagem": "Ordem deletada com sucesso", "ordem": deletada}
    raise HTTPException(status_code=404, detail="Ordem não encontrada")
