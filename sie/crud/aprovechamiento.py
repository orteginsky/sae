from sqlalchemy.orm import Session
from sie.database.models.aprovechamiento import Aprovechamiento
from sqlalchemy.exc import IntegrityError

def create_aprovechamiento(db: Session, aprovechamiento_data: dict) -> Aprovechamiento:
    new_aprovechamiento = Aprovechamiento(**aprovechamiento_data)
    db.add(new_aprovechamiento)
    try:
        db.commit()
        db.refresh(new_aprovechamiento)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos no son válidos.")
    return new_aprovechamiento

def read_aprovechamiento(db: Session, aprovechamiento_data:dict) -> Aprovechamiento:
    new_aprovechamiento = Aprovechamiento(**aprovechamiento_data)
    return new_aprovechamiento