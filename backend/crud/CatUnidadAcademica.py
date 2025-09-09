from backend.database.models.CatUnidadAcademica import CatUnidadAcademica

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_unidad(db: Session, dict_unidad: dict) -> CatUnidadAcademica:
    new_unidad = CatUnidadAcademica(**dict_unidad)
    db.add(new_unidad)
    try:
        db.commit()
        db.refresh(new_unidad)
    except IntegrityError:
        db.rollback()
        raise ValueError("Error en CRUD Unidad")
    return new_unidad
