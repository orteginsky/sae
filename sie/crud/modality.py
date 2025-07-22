from sqlalchemy.orm import Session
from sie.database.models.modality import Modality
from sqlalchemy.exc import IntegrityError

def create_modality(db: Session, modality_data: dict) -> Modality:
    new_modality = Modality(**modality_data)
    db.add(new_modality)
    try:
        db.commit()
        db.refresh(new_modality)
    except IntegrityError:
        db.rollback()
        raise ValueError("El registro ya existe o los datos no son válidos.")
    return new_modality
