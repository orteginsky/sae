from sie.crud.user import create_user
from sie.database.connection import get_db
from sie.database.models.user import User
from sie.utils.security import hash_password

from sqlalchemy.orm import Session
from typing import Optional

#Funciones read
def user_already_exists(db: Session, username: str, email: str) -> bool:
    return db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first() is not None

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

#funciones create

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

#Funciones Update

def update_username():
    return 0

def update_firs_name():
    return 0

def update_paternal_surname():
    return 0

def update_paternal_surname():
    return 0

def update_password():
    return 0

def update_password():
    return 0

def update_password():
    return 0
