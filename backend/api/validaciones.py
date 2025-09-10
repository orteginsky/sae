# routers/validaciones.py
"""
Rutas relacionadas con validaciones de usuario y login.
"""
from backend.services.usuario_service import validacion_usuario

from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from backend.database.connection import get_db
#from frontend.database import engine
from backend.core.templates import templates, static

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def login_view(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def login(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    usuario = form.get("usuario")
    contrasena = form.get("contrasena")
    exito = False
    mensaje = ""
    try:
        if True:#validacion_usuario(db, usuario, contrasena):
            exito = True
            mensaje = "¡Bienvenido, acceso concedido!"
        else:
            mensaje = "Usuario o contraseña incorrectos."
    except Exception as e:
        mensaje = f"Error al validar usuario: {str(e)}"
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "mensaje": mensaje, "exito": exito}
    )
