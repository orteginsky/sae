
from backend.crud.Usuario import create_usuario, read_user_by_username, read_user_by_email, read_password_by_user
from backend.crud.Usuario import read_password_by_email
from backend.database.models.Usuario import Usuario
from backend.utils.security import hash_password
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse, UsuarioLogin


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

def validacion_usuario(db: Session, username_email: Optional[str], password: Optional[str]) -> bool:
    try:
        if username_email is not None and password is not None:
            user = read_user_by_email(db, username_email)
            if user is None:
                user = read_user_by_username(db, username_email)
            if user is None:
                return False  
            stored_password: Optional[str] = user.Password
            if stored_password is None:
                return False
            if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error en validacion_usuario: {e}")
        return False

def validacion_usuario_2(db: Session, userlogin: Optional[UsuarioLogin]) -> bool:

    try:
        if userlogin is not None:
            user = read_user_by_email(db, userlogin.Usuario)
            if user is None:
                user = read_user_by_username(db, userlogin.Email)
            if user is None:
                return False
            stored_password: Optional[str] = user.Password
            if stored_password is None:
                return False
            if bcrypt.checkpw(userlogin.Password.encode("utf-8"), stored_password.encode("utf-8")):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error en validacion_usuario: {e}")
        return False
            
def register_usuario(db: Session, user_dict: UsuarioCreate) -> UsuarioResponse:
    try:
        if user_already_exists(db, user_dict.Usuario, user_dict.Email):
            raise ValueError("El usuario o el email ya están registrados")
        user_dict.Password = hash_password(user_dict.Password)
        user = create_usuario(db, user_dict)
        return UsuarioResponse.model_validate(user)

    except Exception as e:
        print(f"Error en usuario_services: {e}")
        raise
    finally:
        db.close()
