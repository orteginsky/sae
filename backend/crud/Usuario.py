from backend.database.models.Usuario import Usuario
from backend.schemas.Usuario import UsuarioCreate, UsuarioResponse

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from typing import Optional

def create_usuario(db: Session, user_data: UsuarioCreate) -> Usuario:
    new_user = Usuario(**user_data.model_dump())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError as e:
        db.rollback()
        print("❌ Error exacto:", e.orig)
        raise
    return new_user

def get_user_by_username(db: Session, username: str) -> Optional[Usuario]:
    stmt = select(Usuario).where(Usuario.Usuario == username)
    return db.execute(stmt).scalars().first()

def get_user_by_email(db: Session, email: str) -> Optional[Usuario]:
    stmt = select(Usuario).where(Usuario.Email == email)
    return db.execute(stmt).scalars().first()
