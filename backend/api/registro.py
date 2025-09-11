from backend.database.connection import get_db
from backend.services.roles_service import get_all_roles
from backend.services.unidad_services import get_all_units
from backend.services.usuario_service import register_usuario
from backend.utils.security import hash_password
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
    
from fastapi.responses import JSONResponse
from fastapi import Form

@router.post("/")
async def register_user_endpoint(
    nombre: str = Form(...),
    apellido_paterno: str = Form(...),
    apellido_materno: str = Form(...),
    usuario: str = Form(...),
    email: str = Form(...),
    contrasena: str = Form(...),
    unidad_academica: str = Form(...),
    rol: str = Form(...),
    db: Session = Depends(get_db)
):
    # Crear objeto dinámico con los nombres para el SP
    user_obj = type('User', (), {
        "Nombre": nombre,
        "Paterno": apellido_paterno,
        "Materno": apellido_materno,
        "Usuario": usuario,
        "Email": email,
        "Contraseña": hash_password(contrasena),
        "Unidad_Academica": unidad_academica,  # Aquí va el nombre
        "Rol": rol  # Aquí va el nombre
    })()
    resultado = register_usuario(db, user_obj)
    if resultado["exito"] == 1:
        return JSONResponse(content={"exito": 1, "mensaje": resultado["mensaje"]}, status_code=201)
    else:
        return JSONResponse(content={"exito": 0, "mensaje": resultado["mensaje"]}, status_code=400)