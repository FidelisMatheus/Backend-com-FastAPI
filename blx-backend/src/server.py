from typing import Sequence
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repository.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repository.repositorio_usuario import RepositorioUsuario

# criar_bd()

appl = FastAPI()

# PRODUIOS


@appl.post("/produtos", status_code=status.HTTP_201_CREATED)
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@appl.get("/produtos", status_code=status.HTTP_200_OK)
async def listar_produtos(db: Session = Depends(get_db)) -> Sequence[Produto]:
    produtos = RepositorioProduto(db).listar()
    return produtos


@appl.put("/produtos", response_model=Produto)
def editar_usuario(produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(produto)
    return produto


@appl.delete("/produtos/{id}")
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return


# USUÁRIOS


@appl.post("/usuarios", status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@appl.get("/usuarios", response_model=Sequence[Usuario])
def listar_usuarios(session: Session = Depends(get_db)) -> Sequence[Usuario]:
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
