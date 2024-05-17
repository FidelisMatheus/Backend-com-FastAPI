from typing import Sequence
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repositorio_produto import RepositorioProduto

router = APIRouter()


@router.get("/produtos", status_code=status.HTTP_200_OK)
async def listar_produtos(db: Session = Depends(get_db)) -> Sequence[ProdutoSimples]:
    produtos = RepositorioProduto(db).listar()
    return produtos


@router.post("/produtos", status_code=status.HTTP_201_CREATED)
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.put("/produtos/{id}", response_model=ProdutoSimples)
def editar_usuario(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@router.delete("/produtos/{id}")
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return
