from sie.database.connection import get_db
from sie.database.models.user import User
from sie.services.user_service import get_user_by_username

import bcrypt
from typing import Dict

def verify_user(user_dict: Dict[str, str]) -> bool:
    """Verifica que el usuario exista y que la contraseña sea correcta."""
    db = next(get_db())
    try:
        user = get_user_by_username(db, user_dict["username"])
        if not user:
            return False

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

