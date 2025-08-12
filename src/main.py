"""Ponto de entrada da API FastAPI.

Inicializa a aplicação, define o endpoint raiz e registra as rotas de pedidos.
"""

from fastapi import FastAPI

from src.routes import orders

app = FastAPI(title="EasyOrder API - Sistema de Ordens de Compras Online")


@app.get("/")
def root():
    """Endpoint raiz da API.

    Returns:
        dict: Mensagem de boas-vindas.
    """
    return {"mensagem": "Bem-vindo à EasyOrder API!"}


# Inclui as rotas de Orders
app.include_router(orders.router)

# Para rodar localmente ou no Docker
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
