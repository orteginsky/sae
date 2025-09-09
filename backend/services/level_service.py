from backend.database.connection import get_db
from backend.database.models.level import Level
from backend.crud.level import create_level

def register_level(level_dict:dict) -> Level:
    db = next(get_db())
    try:
        existing = db.query(Level).filter_by().first()
        if existing:
            raise ValueError("error en level_service.py")
        level = create_level(level_dict)
        return level
    finally:
        db.close()