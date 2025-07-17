from tosie.database.models.programModality import ProgramModality

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_programModality(db: Session, programModality_data: dict) -> ProgramModality:
    new_programModality = ProgramModality(**programModality_data)
    db.add(new_programModality)
    try:
        db.commit()
        db.refresh(new_programModality)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error en crud:{e}")
    return new_programModality
