from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repository.produto import RepositorioProduto

criar_bd()

appl = FastAPI()


@appl.post("/produtos")
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@appl.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
