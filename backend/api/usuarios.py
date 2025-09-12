from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from backend.core.templates import templates
from backend.database.connection import get_db
from backend.services.usuario_service import (
    get_usuarios_by_unidad,
    get_usuario_by_id,
    update_usuario,
    get_all_roles,
)
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def usuarios_view(
    request: Request,
    db: Session = Depends(get_db),
    id_unidad_academica: int = 1,
):
    usuarios = get_usuarios_by_unidad(db, id_unidad_academica)
    # Leer el rol desde la cookie
    id_rol = int(request.cookies.get("id_rol", 2))
    return templates.TemplateResponse(
        "usuarios.html",
        {"request": request, "usuarios": usuarios, "id_rol": id_rol},
    )


@router.get("/editar/{id_usuario}", response_class=HTMLResponse)
async def editar_usuario_view(
    request: Request, id_usuario: int, db: Session = Depends(get_db)
):
    usuario = get_usuario_by_id(db, id_usuario)
    roles = get_all_roles(db)
    id_rol = int(request.cookies.get("id_rol", 2))
    return templates.TemplateResponse(
        "editar_usuario.html",
        {"request": request, "usuario": usuario, "roles": roles, "id_rol": id_rol},
    )


@router.post("/editar/{id_usuario}", response_class=HTMLResponse)
async def editar_usuario_post(
    request: Request,
    id_usuario: int,
    db: Session = Depends(get_db),
    Nombre: str = Form(...),
    Paterno: str = Form(...),
    Materno: str = Form(...),
    Email: str = Form(...),
    Id_Rol: int = Form(...),
):
    update_usuario(db, id_usuario, Nombre, Paterno, Materno, Email, Id_Rol)
    usuario = get_usuario_by_id(db, id_usuario)
    roles = get_all_roles(db)
    mensaje = "Usuario actualizado correctamente."
    # Obtener el rol del usuario actual desde la query o simulado
    id_rol = int(request.query_params.get('id_rol', 2))
    return templates.TemplateResponse(
        "editar_usuario.html",
        {"request": request, "usuario": usuario, "roles": roles, "mensaje": mensaje, "id_rol": id_rol},
    )
