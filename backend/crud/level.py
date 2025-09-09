from sqlalchemy.orm import Session
from backend.database.models.level import Level
from sqlalchemy.exc import IntegrityError

def create_level(db: Session, level_data: dict) -> Level:
    new_level = Level(**level_data)
    db.add(new_level)
    try:
        db.commit()
        db.refresh(new_level)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos no son válidos.")
    return new_level
