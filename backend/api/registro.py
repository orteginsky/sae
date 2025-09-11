from backend.database.connection import get_db
from backend.services.roles_service import get_all_roles
from backend.services.unidad_services import get_all_units
from backend.services.usuario_service import register_usuario
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse
from backend.core.templates import templates

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def registro_view(request: Request, db: Session = Depends(get_db)):
    try:
        unidades_academicas = get_all_units(db)
        roles = get_all_roles(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
    return templates.TemplateResponse(
        "registro.html",
        {"request": request, "unidades_academicas": unidades_academicas, "roles": roles},
    )
    
@router.post("/", response_model=UsuarioResponse)
async def register_user_endpoint(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return register_usuario(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))