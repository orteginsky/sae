from backend.database.models.CatEstatus import CatEstatus

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_Estatus(db: Session, Estatus_dict: dict) -> CatEstatus:
    new_Estatus = CatEstatus(**Estatus_dict)
    db.add(new_Estatus)
    try:
        db.commit()
        db.refresh(new_Estatus)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos son invalidos")
    return(new_Estatus)

def read_estatus_by_name():
    return 0

def update_estatus_by_name():
    return 0

def delete_Estatus_by_name():
    return 0

