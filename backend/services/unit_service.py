from backend.crud.unit import create_unit
from backend.database.connection import get_db
from backend.database.models.unit import Unit

def register_unit(unit_dict: dict) -> Unit:
    db = next(get_db())
    try:
        """existing = db.query(Unit).filter_by(unit_name=unit_dict["unit_name"]).first()
        if existing:
            raise ValueError("Ya existe dicha información")"""
        user = create_unit(db, unit_dict)
        return user
    finally:
        db.close()