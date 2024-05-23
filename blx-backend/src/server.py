from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.routers import router_produtos, router_auth, router_pedidos
from starlette.middleware.base import BaseHTTPMiddleware
from src.middlewares.timer import processar_tempo_requisicao

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

appl.add_middleware(BaseHTTPMiddleware, dispatch=processar_tempo_requisicao)

# Rotas PRODUIOS
appl.include_router(router_produtos.router)

# Rotas SEGURANÇA: Autenticação e Autorização
appl.include_router(router_auth.router, prefix="/auth")

# Rotas PEDIDOS
appl.include_router(router_pedidos.router)


# middlewares
# @appl.middleware("http")
# async def processar_tempo_requisicao(request: Request, next):
#     print("Interceptou Chegada...")
#     # Pode se interceptar qualquer coisa
#     # request.headers.get('Authentication')

#     response = await next(request)
#     print("Interceptou Volta...")
#     return response
