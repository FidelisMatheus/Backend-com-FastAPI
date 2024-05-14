from pydantic import BaseModel
from typing import Optional, List

from __future__ import annotations

class Usuario(BaseModel):
  id: Optional[str] = None
  nome: str
  telefone: str
  meus_produtos: List[Produto]
  minhas_vendas: List[Pedido]
  meus_pedidos: List[Pedido]
  
class Produto(BaseModel):
  id: Optional[str] = None
  nome: str
  detalhes: str
  preco: float
  disponivel: bool = False
  
class Pedido(BaseModel) :
  id: Optional[str] = None
  usuario: Usuario
  produto: Produto
  quantidade: int
  entrega: bool = False
  endereco: str
  observacoes: Optional[str] = 'Sem observações'