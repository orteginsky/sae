from backend.database.connection import get_db
from backend.schemas.usuario import UsuarioCreate
from backend.schemas.usuario import UsuarioResponse
from backend.services.usuario_service import register_usuario

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=UsuarioResponse)
def register_user_endpoint(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return register_usuario(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))