# routers/validaciones.py
"""
Rutas relacionadas con validaciones de usuario y login.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from frontend.database import engine
from frontend.main import templates

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_view(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
async def login(request: Request):
    form = await request.form()
    usuario = form.get("usuario")
    contrasena = form.get("contrasena")
    exito = False
    mensaje = ""
    try:
        # Ejecutar SP para validar usuario y contraseña
        with engine.connect() as conn:
            result = conn.execute(
                text("EXEC sp_login_usuario @usuario=:usuario, @contrasena=:contrasena"),
                {"usuario": usuario, "contrasena": contrasena}
            )
            row = result.fetchone()
            if row and row[0] == 1:
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

@router.get("/validar-usuario", response_class=HTMLResponse)
async def validar_usuario_view(request: Request):
    return templates.TemplateResponse("validar_usuario.html", {"request": request})

@router.post("/validar-usuario", response_class=HTMLResponse)
async def validar_usuario(request: Request):
    form = await request.form()
    usuario = form.get("usuario")
    validacion = None
    mensaje_validacion = ""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("EXEC sp_validar_usuario @usuario=:usuario"), {"usuario": usuario})
            row = result.fetchone()
            if row and row[0] == 1:
                validacion = True
                mensaje_validacion = f"El usuario '{usuario}' SÍ existe."
            else:
                validacion = False
                mensaje_validacion = f"El usuario '{usuario}' NO existe."
    except SQLAlchemyError as e:
        validacion = False
        mensaje_validacion = f"Error al validar usuario: {str(e)}"
    return templates.TemplateResponse(
        "validar_usuario.html",
        {"request": request, "validacion": validacion, "mensaje_validacion": mensaje_validacion}
    )
