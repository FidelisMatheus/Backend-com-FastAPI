from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import router_produtos, router_usuarios, router_pedidos

# criar_bd()

appl = FastAPI()

# CORS

origins = [
    "http://localhost:3000",
]

appl.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas PRODUIOS
appl.include_router(router_produtos.router)

# Rotas USUÁRIOS
appl.include_router(router_usuarios.router)

# Rotas PEDIDOS
appl.include_router(router_pedidos.router)
