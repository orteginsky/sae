from sie.database.models.unitProgram import UnitProgram

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_unitProgram(db: Session, unitProgram_data: dict) -> UnitProgram:
    new_unitProgram = UnitProgram(**unitProgram_data)
    db.add(new_unitProgram)
    try:
        db.commit()
        db.refresh(new_unitProgram)
    except IntegrityError as e:
        db.rollback
        raise ValueError(f"error:{e}")
    return new_unitProgram