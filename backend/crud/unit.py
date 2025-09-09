from backend.database.models.unit import Unit

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_unit(db: Session, unit_data: dict) -> Unit:
    new_unit = Unit(**unit_data)
    db.add(new_unit)
    try:
        db.commit()
        db.refresh(new_unit)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos no son válidos.")
    return new_unit
