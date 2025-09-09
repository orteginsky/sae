from backend.database.models.CatRoles import CatRoles

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_rol(db: Session, dict_rol:dict) -> CatRoles:
    new_rol = CatRoles(**dict_rol)
    db.add(new_rol)
    try:
        db.commit()
        db.refresh(new_rol)
    except IntegrityError:
        db.rollback()
        raise ValueError("error en CRUD CatRoles")
    return new_rol