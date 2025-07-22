from sie.database.connection import get_db
from sie.database.models.date import Date
from sie.crud.date import create_date

def register_date(date_dict: dict) -> Date:
    db = next(get_db())
    try:
        """existing = db.query(Date).filter_by().first()
        if existing:
            raise ValueError"""
        date = create_date(date_dict)
        return date
    finally:
        db.close()