from typing import Sequence
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido

router = APIRouter()


@router.post("/pedidos", status_code=status.HTTP_201_CREATED)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pass


@router.get("/pedidos/{id}", response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pass


@router.get("/pedidos")
def listar_pedidos(session: Session = Depends(get_db)):
    # ) -> Sequence[Pedido]:
    pass
