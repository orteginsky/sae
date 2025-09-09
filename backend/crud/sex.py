from backend.database.models.sex import Sex

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_sex(db: Session, sex_data: dict) -> Sex:
    new_sex = Sex(**sex_data)
    db.add(new_sex)
    try:
        db.commit()
        db.refresh(new_sex)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_sex