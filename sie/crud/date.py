from sie.database.models.date import Date

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_date(db: Session, date_data: dict) -> Date:
    new_date = Date(**date_data)
    db.add(new_date)
    try:
        db.commit()
        db.refresh(new_date)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"error:{e}")
    return new_date