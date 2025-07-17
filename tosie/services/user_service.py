from tosie.crud.user import create_user
from tosie.database.connection import get_db
from tosie.database.models.user import User
from tosie.utils.security import hash_password

def user_already_exists(db, username: str, email: str) -> bool:
    return db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first() is not None

def register_user(user_dict: dict):
    db = next(get_db())
    try:
        if user_already_exists(db, user_dict["username"], user_dict["email"]):
            raise ValueError("El usuario o el email ya están registrados")

        user_dict["password"] = hash_password(user_dict["password"])
        user = create_user(db, user_dict)
        return user
    finally:
        db.close()
