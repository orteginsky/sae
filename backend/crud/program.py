from backend.database.models.program import Program

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_program(db: Session, program_data: dict) -> Program:
    new_program = Program(**program_data)
    db.add(new_program)
    try:
        db.commit()
        db.refresh(new_program)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_program