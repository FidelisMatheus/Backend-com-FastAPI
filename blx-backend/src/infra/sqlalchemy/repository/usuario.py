from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario:

    def __init__(self, db: Session):
        self.db = db

    # pegamos o schema Produto e transformamos em um Modelo Produto
    # assim então salvamos no BD
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome=usuario.nome, senha=usuario.senha, telefone=usuario.telefone
        )

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)

        return db_usuario

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.db.execute(stmt).scalars().all()

        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass
