from backend.database.connection import get_db
from backend.services.roles_service import get_all_roles
from backend.services.unidad_services import get_all_units
from backend.services.usuario_service import register_usuario
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse
from backend.core.templates import templates

from fastapi import APIRouter, Request, Depends, HTTPException, Form
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

"""@router.post("/", response_model=UsuarioResponse)
async def register_user_endpoint(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return register_usuario(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))"""
 
@router.post("/", response_model=UsuarioResponse)
async def register_user_endpoint(
    nombre: str = Form(...),
    paterno: str = Form(...),
    materno: str = Form(...),
    usuario: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    id_unidad_academica: int = Form(...),
    id_rol: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = UsuarioCreate(
            Usuario=usuario,
            Email=email,
            Password=password,
            Id_Unidad_Academica=id_unidad_academica,
            Id_Rol=id_rol,
            Id_Estatus=1,
            Nombre=nombre,
            Paterno=paterno,
            Materno=materno,
        )
        return register_usuario(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))