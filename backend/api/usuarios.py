from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from backend.core.templates import templates
from backend.database.connection import get_db
from backend.services.usuario_service import (
    get_usuarios_by_unidad,
    get_usuario_by_id,
    update_usuario,
    get_usuarios_by_unidad_con_rol,
    get_unidad_academica_nombre,
    register_usuario
)
from backend.services.roles_service import get_all_roles
from backend.services.unidad_services import get_all_units
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse
from sqlalchemy.orm import Session

router = APIRouter()


# Vista unificada: registro y lista de usuarios
@router.get("/", response_class=HTMLResponse)
async def usuarios_view(
    request: Request,
    db: Session = Depends(get_db),
    id_unidad_academica: int = 1,
):
    usuarios_con_rol = get_usuarios_by_unidad_con_rol(db, id_unidad_academica)
    nombre_ua = get_unidad_academica_nombre(db, id_unidad_academica)
    id_rol = int(request.cookies.get("id_rol", 2))
    nombre_usuario = request.cookies.get("nombre_usuario", "")
    apellidoP_usuario = request.cookies.get("apellidoP_usuario", "")
    apellidoM_usuario = request.cookies.get("apellidoM_usuario", "")
    nombre_completo = " ".join(filter(None, [nombre_usuario, apellidoP_usuario, apellidoM_usuario]))
    roles = get_all_roles(db)
    unidades_academicas = get_all_units(db)
    return templates.TemplateResponse(
        "usuarios.html",
        {
            "request": request,
            "usuarios_con_rol": usuarios_con_rol,
            "id_rol": id_rol,
            "nombre_ua": nombre_ua,
            "nombre_usuario": nombre_completo,
            "roles": roles,
            "unidades_academicas": unidades_academicas
        },
    )


# Endpoint para registrar usuario desde la misma página (AJAX)
@router.post("/registrar", response_class=HTMLResponse)
async def registrar_usuario_view(
    request: Request,
    db: Session = Depends(get_db),
):
    data = await request.json()
    try:
        user = UsuarioCreate(**data)
        usuario_registrado = register_usuario(db, user)
        return {"Id_Usuario": usuario_registrado.Id_Usuario}
    except Exception as e:
        return {"detail": str(e)}

# Endpoint para editar usuario desde la misma página (AJAX)
from fastapi.responses import JSONResponse

@router.post("/editar/{id_usuario}", response_class=JSONResponse)
async def editar_usuario_ajax(
    id_usuario: int,
    request: Request,
    db: Session = Depends(get_db),
):
    try:
        data = await request.json()
        update_usuario(
            db,
            id_usuario,
            data.get("Nombre"),
            data.get("Paterno"),
            data.get("Materno"),
            data.get("Email"),
            data.get("Id_Rol")
        )
        return JSONResponse(content={"mensaje": "Usuario actualizado correctamente."})
    except Exception as e:
        return JSONResponse(content={"mensaje": str(e)}, status_code=500)

# Vista para editar un usuario
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
