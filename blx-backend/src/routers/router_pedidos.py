from typing import Sequence
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.routers.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido, Usuario
from src.infra.sqlalchemy.repository.repositorio_pedido import RepositorioPedido

router = APIRouter()


@router.post("/pedidos", status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado


@router.get("/pedidos/{id}", response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    try:
        pedido = RepositorioPedido(session).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não há um pedido com id = {id}",
        )


@router.get("/pedidos", response_model=list[Pedido])
def listar_pedidos(
    usuario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)
) -> Sequence[Pedido]:
    if usuario.id is not None:
        pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(
            usuario.id
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail=f"Erro no usuário id= {id}",
        )
    return pedidos


@router.get("/pedidos/{usuario_id}/vendas", response_model=list[Pedido])
def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)

    return pedidos
