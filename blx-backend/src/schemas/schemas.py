from __future__ import annotations

# O cara que vem e vai no Request/Response

from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    # produtos: List[Produto] = []

    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]
    class Config:
        from_attributes = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    usuario: Optional[Usuario] = None

    class Config:
        from_attributes = True


class ProdutoSimples(BaseModel):
    nome: str
    preco: float


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = "Sem observações"
