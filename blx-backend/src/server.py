from typing import Sequence
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repository.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repository.repositorio_usuario import RepositorioUsuario

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

# PRODUIOS


@appl.post("/produtos", status_code=status.HTTP_201_CREATED)
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@appl.get("/produtos", status_code=status.HTTP_200_OK)
async def listar_produtos(db: Session = Depends(get_db)) -> Sequence[Produto]:
    produtos = RepositorioProduto(db).listar()
    return produtos


@appl.put("/produtos/{id}", response_model=ProdutoSimples)
def editar_usuario(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@appl.delete("/produtos/{id}")
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return


# USUÁRIOS


@appl.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@appl.get("/usuarios", response_model=Sequence[Usuario])
def listar_usuarios(session: Session = Depends(get_db)) -> Sequence[Usuario]:
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
