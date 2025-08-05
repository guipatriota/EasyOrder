from fastapi import FastAPI
from src.routes import orders

app = FastAPI(title="EasyOrder API - Sistema de Ordens de Compras Online")

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo à EasyOrder API!"}

# Inclui as rotas de Orders
app.include_router(orders.router)
