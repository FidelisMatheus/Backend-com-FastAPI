from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repository.produto import RepositorioProduto

# criar_bd()

appl = FastAPI()


@appl.post("/produtos", status_code=status.HTTP_201_CREATED)
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@appl.get("/produtos", status_code=status.HTTP_200_OK)
async def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
