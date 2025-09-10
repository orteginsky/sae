<<<<<<< HEAD
from backend.crud.Usuario import create_usuario, get_user_by_username, get_user_by_email
=======
from backend.crud.Usuario import create_usuario, get_user_by_username, get_user_by_email, read_password_by_user
from backend.crud.Usuario import read_password_by_email
>>>>>>> origin/master
from backend.database.models.Usuario import Usuario
#from backend.utils.security import hash_password
from backend.schemas.Usuario import UsuarioCreate

from sqlalchemy.orm import Session
from typing import Optional

class UserAlreadyExistsError(Exception):
    """Exception raised when a user already exists."""
    pass

#Funciones read
def user_already_exists(db: Session, username: str, email: str) -> bool:
    """Check if user already exists"""
    return get_user_by_username(db, username) is not None \
        or get_user_by_email(db, email) is not None

<<<<<<< HEAD
=======
def validacion_usuario(db: Session, username_email: str, password:str) -> bool:
    """Si el usuario ya exite hay que validar la contraseña"""
    if get_user_by_email(db, username_email) is not None:
        stored_password = read_password_by_email(db, username_email)
        if stored_password == password:  # Comparación directa (no segura)
            return True
        else:
            return False
        
    elif get_user_by_username(db, username_email) is not None:
        stored_password = read_password_by_user(db, username_email)
        if stored_password == password:  # Comparación directa (no segura)
            return True
        else:
            return False
        
    else:
        return False

            

>>>>>>> origin/master
#funciones create

def register_usuario(db: Session, user_dict: UsuarioCreate) -> Usuario:
    """
    Register a new user.
    
    Args:
        db: Session
        user_data: User data to register
        
    Returns:
        The created user
        
    Raises:
        UserAlreadyExistsError: If username or email already exists
    """
    try:
        if user_already_exists(db, user_dict.Usuario, user_dict.Email):
            raise ValueError("El usuario o el email ya están registrados")

        user = create_usuario(db, user_dict)
        return user
    except Exception as e:
        print(f"error en usuario_services:{e}")
        raise
    finally:
        db.close()


from backend.database.connection import get_db
from backend.database.models.Usuario import Usuario
from backend.crud.Usuario import get_user_by_username

import bcrypt
from typing import Dict


"""Verifica que el usuario exista y que la contraseña sea correcta."""

"""def verify_user(user_dict: Dict[str, str]) -> bool:
    
    db = next(get_db())
    try:
        user = get_user_by_username(db, user_dict["username"])
        if not user:
            return False

<<<<<<< HEAD
=======
            # Verificar la contraseña usando bcrypt (encriptado)
>>>>>>> origin/master
        if bcrypt.checkpw(user_dict["password"].encode(), user.password.encode()):
            return True
        return False

    except KeyError as ke:
        print(f"❌ Faltan datos requeridos: {ke}")
    except Exception as e:
        print(f"❌ Error en verify_user: {e}")
    finally:
        db.close()
    return False
"""