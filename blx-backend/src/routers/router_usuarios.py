from typing import Sequence
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repositorio_usuario import RepositorioUsuario

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@router.get("/usuarios", response_model=Sequence[Usuario])
def listar_usuarios(session: Session = Depends(get_db)) -> Sequence[Usuario]:
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
