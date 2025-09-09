from backend.database.models.basica import Basica
from backend.crud.basica import create_basica
from backend.database.connection import get_db

def register_basica(basica_dict: dict) -> Basica:
    db = next(get_db())
    try:
        """existing = db.query(Basica).filter_by()
        if existing:
            raise ValueError("dicho dato ya existe")"""
        basica = create_basica(basica_dict)
        return basica
    finally:
        db.close()