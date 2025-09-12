# routers/login.py
from backend.database.connection import get_db
from backend.services.usuario_service import validacion_usuario
from backend.schemas.Usuario import UsuarioLogin, UsuarioResponse
from backend.core.templates import templates, static

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse, Response

from sqlalchemy.orm import Session

from typing import Optional

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def login_view(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def login(
    request: Request,
    usuario_email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    exito = False
    mensaje = ""
    try:
        if validacion_usuario(db, usuario_email, password):
            exito = True
            # Obtener el usuario para extraer su Unidad Académica
            from backend.crud.Usuario import read_user_by_email, read_user_by_username
            user = read_user_by_email(db, usuario_email)
            if user is None:
                user = read_user_by_username(db, usuario_email)
            id_unidad = user.Id_Unidad_Academica if user else 1
            id_rol = user.Id_Rol if user else 2
            # Redirigir y guardar el rol en una cookie
            response = RedirectResponse(url=f"/usuarios/?id_unidad_academica={id_unidad}", status_code=303)
            response.set_cookie(key="id_rol", value=str(id_rol), httponly=True)
            return response
        else:
            mensaje = "Usuario o contraseña incorrectos."
    except Exception as e:
        mensaje = f"Error al validar usuario: {str(e)}"

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "mensaje": mensaje, "exito": exito}
    )


"""@router.post("/", response_model=UsuarioResponse)
async def register_user_endpoint(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return register_usuario(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))"""