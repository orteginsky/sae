from sqlalchemy import text

from backend.crud.Usuario import create_usuario, read_user_by_username, read_user_by_email, read_password_by_user
from backend.crud.Usuario import read_password_by_email
from backend.database.models.Usuario import Usuario
from backend.utils.security import hash_password
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse


from sqlalchemy.orm import Session
from typing import Optional, Dict

import bcrypt

class UserAlreadyExistsError(Exception):
    """Exception raised when a user already exists."""
    pass

#Funciones read
def user_already_exists(db: Session, username: str, email: str) -> bool:
    """Check if user already exists"""
    return read_user_by_username(db, username) is not None \
        or read_user_by_email(db, email) is not None

def validacion_usuario(db: Session, username_email: str, password: str) -> bool:
    try:
        user = read_user_by_email(db, username_email)
        if user is None:
            user = read_user_by_username(db, username_email)
        if user is None:
            return False  
        stored_password: Optional[str] = user.Contraseña
        if stored_password is None:
            return False
        if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error en validacion_usuario: {e}")
        return False

            
def register_usuario(db: Session, user_dict: UsuarioCreate) -> UsuarioResponse:
    try:
        if user_already_exists(db, user_dict.Usuario, user_dict.Email):
            raise ValueError("El usuario o el email ya están registrados")
        user_dict.Contraseña = hash_password(user_dict.Contraseña)
        user = create_usuario(db, user_dict)
        return UsuarioResponse.model_validate(user)

    except Exception as e:
        print(f"Error en usuario_services: {e}")
        raise
    finally:
        db.close()

def register_usuario(db: Session, user_dict: UsuarioCreate) -> dict:
    """
    Llama al stored procedure sp_registrar_usuario para registrar un usuario y retorna el mensaje del SP.
    """
    try:
        # Obtener el cursor nativo de pyodbc desde la sesión SQLAlchemy
        raw_conn = db.connection().connection
        cursor = raw_conn.cursor()
        cursor.execute(
            "EXEC Sp_Registro_Usuario @Nombre=?, @Apellido_Paterno=?, @Apellido_Materno=?, @Unidad_Academica=?, @Rol=?, @Usuario=?, @Contrasena=?, @Email=?",
            user_dict.Nombre,
            user_dict.Paterno,
            user_dict.Materno,
            user_dict.Unidad_Academica if hasattr(user_dict, 'Unidad_Academica') else getattr(user_dict, 'Unidad_Academica', None),
            user_dict.Rol if hasattr(user_dict, 'Rol') else getattr(user_dict, 'Rol', None),
            user_dict.Usuario,
            user_dict.Contraseña,
            user_dict.Email
        )
        row = cursor.fetchone()
        cursor.close()
        db.commit()
        if row:
            return {"exito": row[0], "mensaje": row[1]}
        else:
            return {"exito": 0, "mensaje": "No se obtuvo respuesta del procedimiento."}
    except Exception as e:
        db.rollback()
        return {"exito": 0, "mensaje": str(e)}
