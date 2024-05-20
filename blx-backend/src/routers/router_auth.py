from typing import Sequence
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider

router = APIRouter()


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples
)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    # verificar se já existe um user para o telefone
    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(
        usuario.telefone
    )

    if usuario_localizado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um usuário para este telefone",
        )

    # criar novo usuario
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


# @router.get("/usuarios", response_model=Sequence[Usuario])
# def listar_usuarios(session: Session = Depends(get_db)) -> Sequence[Usuario]:
#     usuarios = RepositorioUsuario(session).listar()
#     return usuarios
